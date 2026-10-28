param(
    [string]$RepositoryRoot = (Split-Path $PSScriptRoot -Parent),
    [ValidateRange(1, 90)][int]$MaximumMinutes = 45,
    [switch]$CheckOnly
)
$ErrorActionPreference = 'Stop'
$root = [IO.Path]::GetFullPath($RepositoryRoot)
$logRoot = Join-Path $root '.claude/logs'
New-Item -ItemType Directory -Path $logRoot -Force | Out-Null
$runId = Get-Date -Format 'yyyyMMdd-HHmmss'
$logPath = Join-Path $logRoot "blog-$runId.log"
$statePath = Join-Path $logRoot 'publisher-state.json'
$lock = $null
$clone = $null
$result = 1
function Write-Log([string]$Message) {
    $line = "[$([DateTime]::UtcNow.ToString('o'))] $Message"
    Add-Content -LiteralPath $logPath -Value $line -Encoding UTF8
    Write-Output $line
}
function Invoke-Git([string[]]$Arguments) {
    $output = & git @Arguments 2>&1
    if ($LASTEXITCODE -ne 0) { throw "git failed ($LASTEXITCODE): $($output -join ' ')" }
    return $output
}
try {
    # Presence is never proof of activity. Windows releases this exclusive handle
    # if the process crashes or Task Scheduler terminates it. No stale-lock delete.
    try {
        $lock = [IO.File]::Open((Join-Path $root '.claude/.blog-publish.lock'),
            [IO.FileMode]::OpenOrCreate, [IO.FileAccess]::ReadWrite, [IO.FileShare]::None)
    } catch [IO.IOException] {
        Write-Log 'Skipped: another publisher holds the exclusive lock.'
        exit 0
    }
    $lock.SetLength(0)
    $metadata = [Text.Encoding]::UTF8.GetBytes("PID=$PID; started=$([DateTime]::UtcNow.ToString('o'))")
    $lock.Write($metadata, 0, $metadata.Length)
    $lock.Flush()
    if (Test-Path -LiteralPath $statePath) {
        $prior = Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json
        if ($prior.status -eq 'published' -and $prior.date -eq (Get-Date -Format 'yyyy-MM-dd')) {
            Write-Log 'Skipped: one post has already been published today.'
            $result = 0
            exit $result
        }
    }
    $remote = (Invoke-Git @('-C', $root, 'remote', 'get-url', 'origin') | Out-String).Trim()
    if ($remote -ne 'https://github.com/Tiste42/Potty-Pal-Landing-Page.git') {
        throw 'Unexpected publishing repository; refusing to run.'
    }
    if ($CheckOnly) {
        Write-Log 'Preflight passed: exclusive lock acquired and publishing repository matches.'
        $result = 0
        exit $result
    }
    $clone = Join-Path $root ".claude/publish-runs/$runId"
    New-Item -ItemType Directory -Path (Split-Path $clone -Parent) -Force | Out-Null
    Invoke-Git @('clone', '--depth', '1', '--single-branch', '--branch', 'master', $remote, $clone) | Out-Null
    $queuePath = Join-Path $clone '.claude/topics.md'
    $topicLine = @(Get-Content -LiteralPath $queuePath | Where-Object { $_ -match '^- \[ \] ' }) | Select-Object -First 1
    if (-not $topicLine) {
        Write-Log 'No approved topic remains; nothing to publish.'
        $result = 0
        exit $result
    }
    $topic = $topicLine.Substring(6)
    Write-Log "Generating one approved article: $topic"
    $claude = Join-Path $env:APPDATA 'npm/claude.cmd'
    if (-not (Test-Path -LiteralPath $claude)) { throw 'Existing Claude CLI was not found.' }
    $outPath = Join-Path $logRoot "blog-$runId-worker.log"
    $errPath = Join-Path $logRoot "blog-$runId-worker-error.log"
    $allowed = 'Read,Glob,Grep,WebSearch,Write,Edit,MultiEdit,Bash(git status *),Bash(git diff *),Bash(python scripts/generate-blog-hero.py *),Bash(python scripts/validate-blog-release.py *)'
    $prompt = 'Run /project:blog auto. Generate exactly one complete article. Do not edit the topic queue, commit, push, modify other articles, or change infrastructure. The outer runner validates and publishes. Do not fabricate detection scores or claim tests that did not run.'
    $arguments = '/d /s /c ""' + $claude + '" --permission-mode acceptEdits --permission-prompts none --allowedTools "' + $allowed + '" --disallowedTools "Bash(git add *),Bash(git commit *),Bash(git push *)" --print "' + $prompt + '""'
    $process = Start-Process -FilePath $env:ComSpec -ArgumentList $arguments -WorkingDirectory $clone -WindowStyle Hidden -RedirectStandardOutput $outPath -RedirectStandardError $errPath -PassThru
    $null = $process.Handle
    if (-not $process.WaitForExit($MaximumMinutes * 60000)) {
        # Only terminate this invocation and its descendants, never unrelated agents.
        & taskkill.exe /PID $process.Id /T /F | Out-Null
        throw "Publisher exceeded $MaximumMinutes minutes. Isolated draft retained at $clone"
    }
    $process.Refresh()
    if ($process.ExitCode -ne 0) { throw "Generation failed with exit $($process.ExitCode); draft retained at $clone" }
    $newPaths = @(Invoke-Git @('-C', $clone, 'ls-files', '--others', '--exclude-standard'))
    $articles = @($newPaths | Where-Object { $_ -match '^blog/[a-z0-9-]+\.html$' })
    if ($articles.Count -ne 1) { throw "Expected exactly one new article, found $($articles.Count). Draft retained." }
    $article = $articles[0]
    $slug = [IO.Path]::GetFileNameWithoutExtension($article)
    $html = Get-Content -LiteralPath (Join-Path $clone $article) -Raw
    $categoryMatch = [regex]::Match($html, 'href=["'']category/([a-z0-9-]+)\.html["'']')
    if (-not $categoryMatch.Success) { throw 'Article category link missing.' }
    $category = $categoryMatch.Groups[1].Value
    $allowedPaths = @($article, "images/blog/$slug.webp", 'sitemap.xml', 'blog/index.html', "blog/category/$category.html")
    $changed = @((Invoke-Git @('-C', $clone, 'diff', '--name-only')) + $newPaths | Select-Object -Unique)
    $unexpected = @($changed | Where-Object { $_ -notin $allowedPaths })
    if ($unexpected.Count) { throw "Unexpected file changes: $($unexpected -join ', '). Draft retained; no publish." }
    Push-Location $clone
    try {
        & python scripts/validate-blog-release.py --slug $slug --category $category 2>&1 | ForEach-Object { Write-Log "$_" }
        if ($LASTEXITCODE -ne 0) { throw 'Release validation failed; nothing was published.' }
    } finally { Pop-Location }
    $queue = [IO.File]::ReadAllText($queuePath)
    if (-not $queue.Contains($topicLine)) { throw 'Approved queue item changed unexpectedly.' }
    [IO.File]::WriteAllText($queuePath, $queue.Replace($topicLine, ('- [x] ' + $topic)), (New-Object Text.UTF8Encoding($false)))
    Invoke-Git (@('-C', $clone, 'add', '--') + $allowedPaths + @('.claude/topics.md')) | Out-Null
    Invoke-Git @('-C', $clone, 'commit', '-m', "Add blog post: $topic") | Out-Null
    Invoke-Git @('-C', $clone, 'push', 'origin', 'HEAD:master') | Out-Null
    $commit = (Invoke-Git @('-C', $clone, 'rev-parse', 'HEAD') | Out-String).Trim()
    @{ status='published'; date=(Get-Date -Format 'yyyy-MM-dd'); at=[DateTime]::UtcNow.ToString('o'); commit=$commit; slug=$slug } | ConvertTo-Json | Set-Content -LiteralPath $statePath -Encoding UTF8
    Write-Log "Published $commit https://www.pottypalai.com/blog/$slug.html"
    $result = 0
} catch {
    Write-Log "FAILED: $($_.Exception.Message)"
    @{ status='failed'; date=(Get-Date -Format 'yyyy-MM-dd'); at=[DateTime]::UtcNow.ToString('o'); error=$_.Exception.Message; draft=$clone } | ConvertTo-Json | Set-Content -LiteralPath $statePath -Encoding UTF8
} finally {
    if ($lock) { $lock.Dispose() }
}
exit $result
