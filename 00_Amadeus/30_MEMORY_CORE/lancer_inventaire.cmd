@echo off
cd /d "%~dp0"
start "" /b python -u inventaire_sessions.py > inventaire_stdout.log 2>&1
