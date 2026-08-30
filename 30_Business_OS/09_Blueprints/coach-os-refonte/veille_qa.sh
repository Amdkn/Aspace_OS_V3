#!/usr/bin/env bash
BP="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte"
DEBUT=$SECONDS
while true; do
  N=0
  for G in A B C D; do grep -q "\[code de sortie:" "$BP/logs/qa_$G.log" 2>/dev/null && N=$((N+1)); done
  [ "$N" -eq 4 ] && { echo "TERMINE : les quatre testeurs ont rendu."; break; }
  [ $(( SECONDS - DEBUT )) -gt 21600 ] && { echo "ARRET DE LA VEILLE : $N/4 apres 6 h."; break; }
  sleep 150
done
echo
for G in A B C D; do
  F="$BP/logs/qa_$G.log"; R="$BP/RAPPORT_QA_$G.md"
  printf '=== QA_%s  %s o — %s | rapport %s\n' "$G" "$(stat -c%s "$F" 2>/dev/null || echo 0)" \
    "$(grep -o '\[code de sortie: [0-9]*\]' "$F" 2>/dev/null || echo 'EN COURS')" \
    "$(stat -c%s "$R" 2>/dev/null || echo 'absent')"
done
echo "=== defauts par gravite (toutes lignes de tableau) ==="
cat "$BP"/RAPPORT_QA_*.md 2>/dev/null | grep -oiE "\| *(bloquant|visible|mineur) *\|" | tr -d '| ' | sort | uniq -c
