@echo off
cd /d "%~dp0"
start "" /b python -u distiller_sessions.py > distillation.log 2>&1
