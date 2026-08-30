#!/bin/bash
# Vague 2 — on repart sur les fichiers NON LUS, avec un quota explicite.
set -u
D="C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE"
export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"
cd "$D" || exit 1
for SEAU in 02_Areas_Spock 01_Projects_Picard 04_Archives_Data 03_Resources_Geordi; do
  n=$(tasklist 2>/dev/null | grep -c node)
  if [ "$n" -ge 45 ]; then echo "[$(date '+%H:%M:%S')] $n node — REFUSE $SEAU v2" >> journal_carto.log; continue; fi
  { printf '# TON SEAU : %s — VAGUE 2\n\nLa vague 1 a lu peu de fichiers et l a declare. Tu reprends ou elle s est arretee.\n\n**Lis `carto/%s.json` en premier** : le champ `types[].chemins` et `relations[].chemin` te disent ce qui a DEJA ete lu. **Ne les relis pas.**\n\nQuota : **au moins 120 fichiers non deja lus**. Si tu ne peux pas, dis pourquoi.\n\nTes sorties, a ne pas ecraser : `carto/%s_v2.md` et `carto/%s_v2.json`.\nMeme format JSON que la vague 1.\n\n---\n\n' "$SEAU" "$SEAU" "$SEAU" "$SEAU"; cat BRIEF_CARTO_PARA.md; } \
    | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
    > "journal_carto2_$SEAU.log" 2>&1 &
  echo "[$(date '+%H:%M:%S')] $SEAU vague 2 lancee (pid $!)" >> journal_carto.log
  sleep 180
done
wait
echo "[$(date '+%H:%M:%S')] vague 2 terminee" >> journal_carto.log
