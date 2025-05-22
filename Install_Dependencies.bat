@echo off
color 0A
echo ===================================
echo    INSTALLING JARVIS DEPENDENCIES
echo ===================================
echo.

echo Installing required packages...
"C:\Program Files\Python312\python.exe" -m pip install -r "u:\Preparation Journey\MyProjects\Python Projects\virtual assistant\requirements.txt" --user

echo.
echo Installation complete!
echo.
echo You can now run Jarvis using the Jarvis_Menu.bat file.
echo.
pause