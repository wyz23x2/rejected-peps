@echo off
del /s /f /q dist
py setup.py sdist
twine upload dist/*
