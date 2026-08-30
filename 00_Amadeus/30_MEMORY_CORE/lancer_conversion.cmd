@echo off
REM Detache la conversion du shell appelant : un processus lance depuis un
REM shell d'agent meurt avec lui (constate trois fois sur ce poste).
cd /d "%~dp0"
start "" /b python -u jsonl_vers_md.py > conversion.log 2>&1
