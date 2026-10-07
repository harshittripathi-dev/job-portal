@echo off
title Job In India - Server + Cloudflare

cd /d "C:\Users\Harshit Tripathi\Desktop\Job In India"

echo ==========================================
echo        JOB IN INDIA - STARTING
echo ==========================================
echo.

echo Starting PHP server...
start "PHP Server" cmd /k "php -S localhost:8000"

timeout /t 3 /nobreak >nul

echo Starting Cloudflare Tunnel...
start "Cloudflare Tunnel" cmd /k "cloudflared tunnel --url http://localhost:8000"

timeout /t 5 /nobreak >nul

echo Opening localhost...
start "" "http://localhost:8000"

echo.
echo ==========================================
echo PHP Server : http://localhost:8000
echo Cloudflare : Check the Cloudflare window
echo ==========================================
echo.

pause