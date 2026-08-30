#!/bin/bash
# Un agent par seau. Perimetres exclusifs, echelonnes de 3 min (piege 5).
set -u
D="C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE"
export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"
cd "$D" || exit 1
for SEAU in 02_Areas_Spock 01_Projects_Picard 04_Archives_Data 03_Resources_Geordi; do
  n=$(tasklist 2>/dev/null | grep -c node)
  if [ "$n" -ge 45 ]; then echo "[$(date '+%H:%M:%S')] $n node — REFUSE $SEAU" >> journal_carto.log; continue; fi
  { printf '# TON SEAU : %s\n\nLa liste de travail est dans `carto/structure.txt`. Filtre les lignes dont la premiere colonne vaut `%s`.\nTes sorties : `carto/%s.md` et `carto/%s.json`.\n\n---\n\n' "$SEAU" "$SEAU" "$SEAU" "$SEAU"; cat BRIEF_CARTO_PARA.md; } \
    | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
    > "journal_carto_$SEAU.log" 2>&1 &
  echo "[$(date '+%H:%M:%S')] $SEAU lance (pid $!)" >> journal_carto.log
  sleep 180
done
wait
echo "[$(date '+%H:%M:%S')] les quatre seaux termines" >> journal_carto.log
