@echo off

IF "%1"=="" GOTO :Continue

set file=%~n1
set mPath=%~dp1
echo %file%

python main.py --gts2 --file %1
pause
GTR2_Packer.exe -cmp2 %mPath%%file%_packed.bin
pause
if exist "%mPath%%file%_packed_cmp.bin" del "%mPath%%file%_packed_cmp.bin"
ren "%mPath%%file%_packed.bin.cmp" "%file%_packed_cmp.bin"

echo.
echo Install "%mPath%%file%_packed_cmp.bin" to Watch
echo.
pause

:Continue
IF "%1"=="" echo No json given. Usage: %~nx0 path\to\file.json

