@echo off
REM 9Router — passerelle LLM locale.
REM Port 20129 : son defaut (20128) entre en collision avec OmniRoute.
REM -H 127.0.0.1 : son defaut est 0.0.0.0, qui expose la passerelle a tout le reseau local.
REM -n : pas d'ouverture de navigateur au boot.
REM -t/--tray : sans lui, 9Router s'arrete sur un menu "Choose Interface" qui attend
REM             une frappe clavier. En fenetre masquee au boot, personne ne repond.
REM Lance par Demarrage\9router.vbs, fenetre masquee.

cd /d "%USERPROFILE%"
"%APPDATA%\npm\9router.cmd" --port 20129 --host 127.0.0.1 --no-browser --tray --log >> "%~dp0log-9router.log" 2>&1
