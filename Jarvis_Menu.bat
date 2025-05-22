@echo off
color 0A
cls
echo ===================================
echo        JARVIS VIRTUAL ASSISTANT
echo ===================================
echo.
echo Choose language / भाषा चुनें:
echo.
echo 1. English
echo 2. Hindi / हिंदी
echo.
echo ===================================
echo.

set /p choice="Enter your choice (1 or 2): "

if "%choice%"=="1" (
    cls
    echo Starting Jarvis in English...
    "C:\Program Files\Python312\python.exe" "u:\Preparation Journey\MyProjects\Python Projects\virtual assistant\Jarvis_English.py"
) else if "%choice%"=="2" (
    cls
    echo Starting Jarvis in Hindi...
    "C:\Program Files\Python312\python.exe" "u:\Preparation Journey\MyProjects\Python Projects\virtual assistant\Jarvis_Hindi.py"
) else (
    echo Invalid choice. Please try again.
    timeout /t 3 >nul
    call %0
)

pause