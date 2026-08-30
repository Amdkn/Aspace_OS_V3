#!/usr/bin/env bash
BP="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte"
F="$BP/logs/sales_os.log"
DEBUT=$SECONDS
while true; do
  grep -q "\[code de sortie:" "$F" 2>/dev/null && { echo "TERMINE : Sales OS a rendu."; break; }
  [ $(( SECONDS - DEBUT )) -gt 14400 ] && { echo "ARRET DE LA VEILLE : 4 h sans code de sortie."; break; }
  sleep 90
done
echo; echo "journal : $(stat -c%s "$F" 2>/dev/null || echo 0) octets"
tail -c 900 "$F" 2>/dev/null
echo; echo "=== rapport ==="; ls -l "$BP/RAPPORT_SALES_OS.md" 2>/dev/null || echo "aucun rapport"
