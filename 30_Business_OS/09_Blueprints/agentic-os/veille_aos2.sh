#!/usr/bin/env bash
D="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os"
F="$D/logs/agent_os_v2.log"
DEBUT=$SECONDS
while true; do
  grep -q "\[code de sortie:" "$F" 2>/dev/null && { echo "TERMINE : Agent OS a rendu."; break; }
  [ $(( SECONDS - DEBUT )) -gt 30000 ] && { echo "ARRET DE LA VEILLE : plus de 8 h sans code de sortie."; break; }
  sleep 180
done
echo
echo "journal : $(stat -c%s "$F" 2>/dev/null || echo 0) octets"
tail -c 1000 "$F" 2>/dev/null
echo
echo "=== rapport ==="; ls -l "$D/RAPPORT_AGENT_OS_V1.md" 2>/dev/null || echo "aucun rapport"
echo "=== fichiers source ==="; find /mnt/c/Users/amado/agent-os/desktop/src -type f 2>/dev/null | wc -l
