@echo off
cd /d "%~dp0"
start "" /b python -u jsonl_vers_md.py > conversion2.log 2>&1
