#!/usr/bin/env bash
A="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/logs"
B="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/logs"
F1="$A/v4_THEME_A.log"; F2="$A/v4_WELCOME.log"; F3="$B/observatoire_v2.log"
DEBUT=$SECONDS
while true; do
  N=0
  for F in "$F1" "$F2" "$F3"; do grep -q "\[code de sortie:" "$F" 2>/dev/null && N=$((N+1)); done
  [ "$N" -eq 3 ] && { echo "TERMINE : les trois derniers agents ont rendu."; break; }
  [ $(( SECONDS - DEBUT )) -gt 25200 ] && { echo "ARRET DE LA VEILLE : $N/3 apres 7 h."; break; }
  sleep 120
done
echo
for P in "THEME_A:$F1" "WELCOME:$F2" "OBSERVATOIRE:$F3"; do
  N="${P%%:*}"; F="${P#*:}"
  printf '=== %-12s %8s o — %s\n' "$N" "$(stat -c%s "$F" 2>/dev/null || echo 0)" \
    "$(grep -o '\[code de sortie: [0-9]*\]' "$F" 2>/dev/null || echo 'EN COURS')"
  tail -c 450 "$F" 2>/dev/null; echo
done
