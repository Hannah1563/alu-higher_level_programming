#!/usr/bin/python3#
Create the Python script
echo print("Best School") > main.py 
# Set the environment variable 
set PYFILE=main.py 
# Create the batch script
echo @echo off > 0-run.bat 
echo python %PYFILE% >> 0-run.bat
