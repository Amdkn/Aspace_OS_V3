@echo off
REM 9Router — passerelle LLM locale.
REM Port 20128 : son defaut. Arbitrage du 2026-08-30 -- la mise a jour de
REM 9Router l'a ramene sur 20128 et il squattait OmniRoute. On lui laisse
REM son defaut, et c'est OmniRoute qui bouge.
REM -H 127.0.0.1 : son defaut est 0.0.0.0, qui expose la passerelle a tout le reseau local.
REM -n : pas d'ouverture de navigateur au boot.
REM -t/--tray : sans lui, 9Router s'arrete sur un menu "Choose Interface" qui attend
REM             une frappe clavier. En fenetre masquee au boot, personne ne repond.
REM Lance par Demarrage\9router.vbs, fenetre masquee.

cd /d "%USERPROFILE%"
"%APPDATA%\npm\9router.cmd" --port 20128 --host 127.0.0.1 --no-browser --tray --log >> "%~dp0log-9router.log" 2>&1
