@echo off
title Kalybana Production - Sovereign Node
color 0A

echo ===================================================
echo   KALYBANA HOLDING - SOVEREIGN DEV ENVIRONMENT
echo ===================================================
echo.
echo Initializing isolated terminal to prevent IDE blockage...
echo.

cd /d "%~dp0"

echo [1/2] Verifying and installing dependencies natively...
call npm install --no-audit --no-fund

echo.
echo [2/2] Igniting the SOB Engine (Vite)...
echo.
call npm run dev

pause
