echo off

pyinstaller --clean --icon=Kara.ico --hidden-import= --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.sapi5 --onefile Light.py

del /s /q /f Light.spec
rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null