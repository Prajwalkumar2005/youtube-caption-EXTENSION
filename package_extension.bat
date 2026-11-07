@echo off
setlocal
title YouTube Desktop Lyrics Overlay - Extension Packager

cd /d "%~dp0"

echo =======================================================
echo   YouTube Desktop Lyrics Overlay - Extension Packager
echo =======================================================
echo.

if not exist "dist" mkdir "dist"

set "ZIP_PATH=dist\yt-lyrics-overlay-extension.zip"
if exist "%ZIP_PATH%" del /f /q "%ZIP_PATH%"

echo [1/2] Verifying extension manifest...
if not exist "extension\manifest.json" (
    echo [Error] extension\manifest.json missing!
    pause
    exit /b 1
)

echo [2/2] Creating production ZIP archive: %ZIP_PATH%...
powershell -NoProfile -Command ^
    "Compress-Archive -Path 'extension\*' -DestinationPath '%ZIP_PATH%' -Force"

if %ERRORLEVEL% equ 0 (
    echo.
    echo =======================================================
    echo  Extension packaged successfully!
    echo  Location: %ZIP_PATH%
    echo  Ready for submission to the Chrome Web Store.
    echo =======================================================
) else (
    echo [Error] Failed to package extension.
    pause
    exit /b 1
)

echo.
pause
exit /b 0
