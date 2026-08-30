#!/usr/bin/env bash
F="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/logs/agent_os_v1.log"
DEBUT=$SECONDS
while true; do
  grep -q "\[code de sortie:" "$F" 2>/dev/null && { echo "TERMINE : Agent OS V1 a rendu."; break; }
  [ $(( SECONDS - DEBUT )) -gt 30000 ] && { echo "ARRET DE LA VEILLE : plus de 8 h sans code de sortie."; break; }
  sleep 180
done
echo; echo "journal : $(stat -c%s "$F" 2>/dev/null || echo 0) octets"; tail -c 900 "$F" 2>/dev/null
echo; echo "=== ce qui existe dans desktop/ ==="
ls -1 /mnt/c/Users/amado/agent-os/desktop 2>/dev/null | head -12
