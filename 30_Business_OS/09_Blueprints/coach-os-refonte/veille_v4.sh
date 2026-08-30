#!/usr/bin/env bash
BP="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte"
DEBUT=$SECONDS
while true; do
  N=0
  for V in THEME_A THEME_B LEGAL WELCOME; do
    grep -q "\[code de sortie:" "$BP/logs/v4_$V.log" 2>/dev/null && N=$((N+1))
  done
  [ "$N" -eq 4 ] && { echo "TERMINE : les quatre chantiers ont rendu."; break; }
  [ $(( SECONDS - DEBUT )) -gt 25200 ] && { echo "ARRET DE LA VEILLE : $N/4 apres 7 h."; break; }
  sleep 120
done
echo
for V in THEME_A THEME_B LEGAL WELCOME; do
  F="$BP/logs/v4_$V.log"
  printf '=== %-8s %8s o — %s\n' "$V" "$(stat -c%s "$F" 2>/dev/null || echo 0)" \
    "$(grep -o '\[code de sortie: [0-9]*\]' "$F" 2>/dev/null || echo 'EN COURS')"
  tail -c 400 "$F" 2>/dev/null; echo
done
echo "=== rapports ==="; ls -1 "$BP"/RAPPORT_*.md 2>/dev/null | tail -8
