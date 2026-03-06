@echo off
cd /d "C:\dev\Potty Pal Landing Page"

:: Log file with date stamp
set LOGFILE=C:\dev\Potty Pal Landing Page\.claude\logs\blog-%date:~-4,4%%date:~-10,2%%date:~-7,2%.log

:: Create logs directory if needed
if not exist "C:\dev\Potty Pal Landing Page\.claude\logs" mkdir "C:\dev\Potty Pal Landing Page\.claude\logs"

:: Run the blog command, log output
echo [%date% %time%] Starting daily blog generation >> "%LOGFILE%"
claude --dangerously-skip-permissions --print "Run /project:blog auto" >> "%LOGFILE%" 2>&1
echo [%date% %time%] Finished >> "%LOGFILE%"
