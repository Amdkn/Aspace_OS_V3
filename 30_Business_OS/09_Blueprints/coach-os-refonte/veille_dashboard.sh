#!/usr/bin/env bash
# Attend que les trois vagues aient rendu, puis rend la main.
# Le lanceur ecrit "[code de sortie: N]" en fin de chaque journal — c'est le seul
# marqueur fiable de fin : un journal qui grossit encore ne prouve rien, et un
# processus vivant encore moins (leçon du 2026-08-06).
BP="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte"
LIMITE=$(( 3 * 3600 ))   # borne dure : au-dela, on rend la main quoi qu'il arrive
DEBUT=$SECONDS

while true; do
  FINIS=0
  for V in V1 V2 V3; do
    grep -q "\[code de sortie:" "$BP/sortie_dashboard_$V.log" 2>/dev/null && FINIS=$((FINIS+1))
  done
  [ "$FINIS" -eq 3 ] && { echo "TERMINE : les trois vagues ont rendu."; break; }
  if [ $(( SECONDS - DEBUT )) -gt "$LIMITE" ]; then
    echo "ARRET DE LA VEILLE : $FINIS/3 rendues apres 3 h."
    break
  fi
  sleep 60
done

echo
for V in V1 V2 V3; do
  F="$BP/sortie_dashboard_$V.log"
  printf '=== %s : %s octets — %s\n' "$V" \
    "$(stat -c%s "$F" 2>/dev/null || echo 0)" \
    "$(grep -o '\[code de sortie: [0-9]*\]' "$F" 2>/dev/null || echo 'EN COURS')"
  tail -c 300 "$F" 2>/dev/null
  echo
done

echo "=== rapports deposes ==="
ls -1 "$BP"/RAPPORT_DASHBOARD_V*.md 2>/dev/null || echo "aucun"
