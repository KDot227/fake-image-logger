@echo off
::made by K.Dot#0001
color a

:poop
py --version 3>NUL
if errorlevel 1 goto errorNoPython

goto damn

:damn
pip install -r requirements.txt
if errorlevel 1 goto dang
start main.py
cls

:dang
echo .
echo YOU NEED TO ADD PYTHON TO PATH!!!
echo.
echo IF YOU DONT KNOW HOW TO JOIN THE SERVER THAT IS LINKED IN THE README