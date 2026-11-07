@echo off
setlocal enabledelayedexpansion
title YouTube Desktop Lyrics Overlay - PyInstaller Builder

cd /d "%~dp0"

echo =======================================================
echo    YouTube Desktop Lyrics Overlay - Executable Builder
echo =======================================================
echo.

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

echo [Error] Python 3 was not found in your system PATH!
pause
exit /b 1

:PYTHON_READY
echo [1/4] Checking PyInstaller...
%PY_CMD% -c "import PyInstaller" >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [Info] Installing PyInstaller...
    %PY_CMD% -m pip install pyinstaller
)

echo [2/4] Verifying dependencies...
%PY_CMD% -m pip install -r "overlay_app\requirements.txt"

echo [3/4] Compiling standalone Windows executable...
cd overlay_app
if not exist "dist" mkdir "dist"

set "ICON_PARAM="
if exist "..\extension\icons\icon128.png" (
    REM If an .ico exists, use it, otherwise PyInstaller uses default Windows icon
    if exist "icon.ico" (
        set "ICON_PARAM=--icon=icon.ico"
    )
)

%PY_CMD% -m PyInstaller ^
    --noconsole ^
    --onefile ^
    --name "YT_Lyrics_Overlay" ^
    --clean ^
    !ICON_PARAM! ^
    main_overlay.py

if %ERRORLEVEL% neq 0 (
    echo [Error] Executable build failed!
    cd ..
    pause
    exit /b 1
)

cd ..
echo.
echo [4/4] Build succeeded!
echo Output executable: overlay_app\dist\YT_Lyrics_Overlay.exe
echo.
echo =======================================================
echo  Standalone executable is ready for public distribution!
echo =======================================================
echo.
pause
exit /b 0
