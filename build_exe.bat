@echo off
setlocal enabledelayedexpansion
title Build Standalone Executable - YouTube Lyrics Overlay

cd /d "%~dp0"

echo =======================================================
echo   YouTube Desktop Lyrics Overlay - Executable Builder
echo =======================================================
echo.

where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    where py >nul 2>nul
    if %ERRORLEVEL% neq 0 (
        echo [Error] Python 3 was not found in your system PATH!
        echo Please install Python 3.8+ from https://www.python.org/
        pause
        exit /b 1
    )
    set "PY_CMD=py"
) else (
    set "PY_CMD=python"
)

echo [1/3] Checking build tool dependencies...
%PY_CMD% -c "import PyInstaller" >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [Notice] Installing PyInstaller...
    %PY_CMD% -m pip install --upgrade pyinstaller
    if %ERRORLEVEL% neq 0 (
        echo [Error] Failed to install PyInstaller. Check internet connection.
        pause
        exit /b 1
    )
)

echo [2/3] Installing application dependencies...
%PY_CMD% -m pip install -r "overlay_app\requirements.txt" >nul 2>nul

echo [3/3] Compiling standalone executable with PyInstaller...
cd overlay_app
%PY_CMD% -m PyInstaller --noconsole --onefile --name "YT_Lyrics_Overlay" --clean main_overlay.py

if exist "dist\YT_Lyrics_Overlay.exe" (
    echo.
    echo =======================================================
    echo  SUCCESS: Standalone executable created!
    echo  Output: overlay_app\dist\YT_Lyrics_Overlay.exe
    echo =======================================================
) else (
    echo.
    echo [Error] PyInstaller build failed. Check console output above.
)

cd ..
pause
