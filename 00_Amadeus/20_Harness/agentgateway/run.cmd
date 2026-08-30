@echo off
rem Le cd est necessaire : config.yaml et run.log sont resolus relativement au
rem repertoire courant. Le ".\" l'est tout autant : Windows n'inclut pas le
rem repertoire courant dans le PATH, donc "agentgateway.exe" nu est introuvable.
set HERE=C:\Users\amado\ASpace_OS_V3\00_Amadeus\20_Harness\agentgateway
cd /d "%HERE%"
"%HERE%\agentgateway.exe" -f "%HERE%\config.yaml" >> "%HERE%\run.log" 2>&1
