@echo off
setlocal

cd /d "%~dp0"

set "PATH=%USERPROFILE%\.local\bin;%USERPROFILE%\AppData\Roaming\Python\Python314\Scripts;%PATH%"

echo Starting Polymarket CS2 alerts bot...
echo Workspace: %CD%
echo.

uv run polymarket-cs2-alerts

echo.
echo Bot stopped with exit code %ERRORLEVEL%.
pause
