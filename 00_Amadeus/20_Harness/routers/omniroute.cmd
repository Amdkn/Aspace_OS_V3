@echo off
REM OmniRoute — routeur LLM avec fallback automatique.
REM Port 20128 (son defaut). 9Router a le meme defaut : voir 9router.cmd, deplace en 20129.
REM Lance par Demarrage\omniroute.vbs, fenetre masquee.
REM Chemin absolu obligatoire : Windows n'a pas le repertoire courant dans PATH.

REM Le serveur est un Next.js : c'est HOSTNAME qu'il lit, pas HOST.
REM Sans ca il annonce "Network: http://0.0.0.0:20128" et repond a tout le reseau local.
set "HOSTNAME=127.0.0.1"
set "OMNIROUTE_HOST=127.0.0.1"

cd /d "%USERPROFILE%"
"%APPDATA%\npm\omniroute.cmd" serve --port 20128 --no-open --no-tray --log >> "%~dp0omniroute.log" 2>&1
