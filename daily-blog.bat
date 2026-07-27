@echo off
cd /d "%~dp0"

:: Log file with date stamp
set LOGFILE=%~dp0.claude\logs\blog-%date:~-4,4%%date:~-10,2%%date:~-7,2%.log

:: Create logs directory if needed
if not exist "%~dp0.claude\logs" mkdir "%~dp0.claude\logs"

:: Fail closed if another run is active or the tracked worktree is not clean.
if exist ".claude\.blog-publish.lock" (
  echo [%date% %time%] Skipped: publish lock already exists. >> "%LOGFILE%"
  exit /b 2
)

git diff --quiet
if errorlevel 1 (
  echo [%date% %time%] Skipped: tracked worktree has unstaged changes. >> "%LOGFILE%"
  exit /b 2
)

git diff --cached --quiet
if errorlevel 1 (
  echo [%date% %time%] Skipped: tracked worktree has staged changes. >> "%LOGFILE%"
  exit /b 2
)

findstr /R /C:"^- \[ \]" ".claude\topics.md" >nul
if errorlevel 1 (
  echo [%date% %time%] Skipped: no approved topic is available. >> "%LOGFILE%"
  exit /b 0
)

type nul > ".claude\.blog-publish.lock"
echo [%date% %time%] Starting guarded blog generation >> "%LOGFILE%"
"C:\Users\bapti\AppData\Roaming\npm\claude.cmd" --permission-mode acceptEdits --allowedTools "Read,Glob,Grep,WebSearch,Write,Edit,MultiEdit,Bash(git status *),Bash(git diff *),Bash(git add *),Bash(git commit *),Bash(git push *),Bash(py scripts/generate-blog-hero.py *),Bash(py scripts/validate-blog-release.py *)" --print "Run /project:blog auto" >> "%LOGFILE%" 2>&1
set EXITCODE=%ERRORLEVEL%
del ".claude\.blog-publish.lock" >nul 2>&1
echo [%date% %time%] Finished with exit code %EXITCODE% >> "%LOGFILE%"
exit /b %EXITCODE%
