@echo off
set ZIP=C:\PROGRA~1\7-Zip\7z.exe a -tzip -y -r
set REPO=small_potatoes
set NAME=small_potatoes
set PACKID=75718778
set VERSION=0.0.2


echo %VERSION% >%REPO%\VERSION

fsum -r -jm -md5 -d%REPO% * > checksum.md5
move checksum.md5 %REPO%\checksum.md5

%ZIP% %REPO%_v%VERSION%_Anki20.zip *.py %REPO%\*

cd %REPO%

quick_manifest.exe "%NAME%" "%PACKID%" >manifest.json
%ZIP% ../%REPO%_v%VERSION%_Anki21.ankiaddon *


REM Already integreated with CCBC

REM quick_manifest.exe "%NAME%" "%NAME%" >manifest.json
REM %ZIP% ../%REPO%_v%VERSION%_CCBC.adze *
