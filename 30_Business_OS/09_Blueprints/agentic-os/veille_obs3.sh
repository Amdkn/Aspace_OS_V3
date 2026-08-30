#!/usr/bin/env bash
F="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/logs/observatoire_v3.log"
DEBUT=$SECONDS
while true; do
  grep -q "\[code de sortie:" "$F" 2>/dev/null && { echo "TERMINE : Observatoire V3 a rendu."; break; }
  [ $(( SECONDS - DEBUT )) -gt 21600 ] && { echo "ARRET DE LA VEILLE : 6 h sans code de sortie."; break; }
  sleep 120
done
echo; echo "journal : $(stat -c%s "$F" 2>/dev/null || echo 0) octets"; tail -c 800 "$F" 2>/dev/null
