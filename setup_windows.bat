@echo off
setlocal enabledelayedexpansion
title YouTube Desktop Lyrics Overlay - Environment Setup

cd /d "%~dp0"

echo =======================================================
echo    YouTube Desktop Lyrics Overlay - Environment Setup
echo =======================================================
echo.

where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    set "PY_CMD=python"
    goto :FOUND_PYTHON
)

where py >nul 2>nul
if %ERRORLEVEL% equ 0 (
    set "PY_CMD=py"
    goto :FOUND_PYTHON
)

echo [Error] Python 3.8+ was not found on your system!
echo Please install Python from https://www.python.org/
echo Make sure to check "Add Python to PATH" during installation.
echo.
pause
exit /b 1

:FOUND_PYTHON
echo [1/3] Python interpreter found:
%PY_CMD% --version
echo.

echo [2/3] Upgrading pip and installing required dependencies...
%PY_CMD% -m pip install --upgrade pip
%PY_CMD% -m pip install -r "overlay_app\requirements.txt"
if %ERRORLEVEL% neq 0 (
    echo [Error] Failed to install dependencies. Check your internet connection.
    pause
    exit /b 1
)

echo.
echo [3/3] Running environment diagnostics...
%PY_CMD% overlay_app\diagnostics.py

echo.
echo =======================================================
echo  Setup Completed Successfully!
echo  You can now launch the app anytime with run_overlay.bat
echo =======================================================
echo.
pause
exit /b 0
