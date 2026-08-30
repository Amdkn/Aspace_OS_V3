#!/bin/bash
# Lance un correctif QA sur M3. Un argument : le numero du fix (1..5).
#
# Trois pieges deja payes, tous les trois neutralises ici :
#  - le shell exporte ANTHROPIC_BASE_URL vers api.anthropic.com et ecrase
#    settings.json ; sans export explicite la cle MiniMax part chez Anthropic
#    et revient en "Invalid API key" avec un exit 0 trompeur ;
#  - `claude` est introuvable dans un shell d'arriere-plan (exit 127) : chemin absolu ;
#  - un brief qui commence par --- est lu comme un flag : il passe par stdin.
set -u
N="$1"
BASE=/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/correctifs
REPO=/c/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os

BRIEF=$(ls "$BASE"/BRIEF_FIX_${N}_*.md | head -1)

export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"

cd "$REPO" || exit 1
{ cat "$BASE/GARDE_FOU.md"; echo; cat "$BASE/COMMUN.md"; echo; echo "---"; echo; cat "$BRIEF"; } \
  | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
  > "$BASE/journal_fix_${N}.log" 2>&1
echo "FIX-${N} termine, code $?" >> "$BASE/journal_fix_${N}.log"
