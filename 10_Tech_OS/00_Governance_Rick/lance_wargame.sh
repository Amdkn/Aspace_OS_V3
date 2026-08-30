#!/bin/bash
# Deux agents, perimetres exclusifs, echelonnes de 3 min (piege 5 de CLAUDE.md).
# NE PAS lancer avec `&` : ce script part en tache de fond par l'outil.
set -u
D="C:/Users/amado/ASpace_OS_V3/10_Tech_OS/00_Governance_Rick"
export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"
cd "$D" || exit 1
for B in BRIEF_WARGAME_ACCES BRIEF_JCODE_SDK; do
  n=$(tasklist 2>/dev/null | grep -c node)
  if [ "$n" -ge 45 ]; then echo "[$(date '+%H:%M:%S')] $n node — REFUSE $B" >> journal_wargame.log; continue; fi
  cat "$B.md" | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
    > "journal_$B.log" 2>&1 &
  echo "[$(date '+%H:%M:%S')] $B lance (pid $!)" >> journal_wargame.log
  sleep 180
done
wait
echo "[$(date '+%H:%M:%S')] les deux termines" >> journal_wargame.log
