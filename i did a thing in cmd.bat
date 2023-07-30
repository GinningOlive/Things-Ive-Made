@echo off
:restart
cls
echo                                           ~Welcome to my game of numbers!~
echo.
echo Pick a number, 1 or 2; I will print what you dont pick.
set /p Input=Enter 1 or 2:
If /I "%Input%"=="1" goto 1
If /I "%Input%"=="2" goto 2
If /I "%Input%"=="fuck you" goto easter_egg
goto other
:1
echo 2
pause
goto restart question
:2
echo 1
pause
goto restart question
:other
echo I said 1 or 2, please try again
pause
goto restart question
:easter_egg
echo Well that's not very nice, is it?
pause
:restart question
echo Would you like to play again?
set /p Input=Enter y or n:
If /I "%Input%"=="y" goto restart
echo Goodbye
pause
exit