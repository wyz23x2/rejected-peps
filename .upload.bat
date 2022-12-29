@echo off
py check.py
if %ERRORLEVEL% NEQ 0 echo, && echo Tests failed! && exit /B %ERRORLEVEL%
del /s /f /q dist
py setup.py sdist
twine upload dist/*
