@echo off
cd /d "%~dp0"
REM PowerShell waits for the publisher and releases the OS lock even after failure.
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\run-daily-blog.ps1"
exit /b %ERRORLEVEL%
