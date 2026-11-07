@echo off
setlocal enabledelayedexpansion
title YouTube Desktop Lyrics Overlay - 1-Click Setup

cd /d "%~dp0"

echo =======================================================
echo    YouTube Desktop Lyrics Overlay - 1-Click Setup
echo =======================================================
echo.
echo Welcome! This script will prepare and launch your lyrics overlay.
echo.

REM 1. Check for standalone pre-built executable first
if exist "overlay_app\dist\YT_Lyrics_Overlay.exe" (
    echo [OK] Standalone executable detected!
    echo Launching YouTube Desktop Lyrics Overlay...
    start "" "overlay_app\dist\YT_Lyrics_Overlay.exe"
    goto :EXTENSION_PROMPT
)

REM 2. Check for Python runtime
where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    set "PY_CMD=python"
    goto :PYTHON_READY
)

where py >nul 2>nul
if %ERRORLEVEL% equ 0 (
    set "PY_CMD=py"
    goto :PYTHON_READY
)

echo [Notice] Python was not detected in PATH.
echo Please either:
echo   1. Install Python 3.8+ from https://www.python.org/
echo      (Check "Add Python to PATH" during installation)
echo   OR
echo   2. Run build_exe.bat to compile the standalone app.
echo.
pause
exit /b 1

:PYTHON_READY
echo [1/2] Checking Python dependencies...
%PY_CMD% -c "import websockets, tkinter" >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [Info] Installing requirements...
    %PY_CMD% -m pip install -r "overlay_app\requirements.txt"
)

echo [2/2] Launching YouTube Desktop Lyrics Overlay...
cd overlay_app
start "" %PY_CMD% main_overlay.py
cd ..

:EXTENSION_PROMPT
echo.
echo =======================================================
echo  Overlay is now active on your desktop!
echo.
echo  Next Steps:
echo  1. Open Chrome -> chrome://extensions
echo  2. Enable "Developer mode" (top right)
echo  3. Click "Load unpacked" -> Select the 'extension' folder
echo  4. Play any YouTube video with Closed Captions (CC)!
echo =======================================================
echo.
pause
exit /b 0
