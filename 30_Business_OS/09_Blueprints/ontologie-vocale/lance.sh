#!/bin/bash
set -u
N="$1"
D=/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/ontologie-vocale
REPO=/c/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os
BRIEF=$(ls "$D"/BRIEF_${N}_*.md | head -1)
export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"
cd "$REPO" || exit 1
{ echo "Les briefs, l'analyse, la transcription et les planches-contact sont dans : $D"; echo;
  cat /c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/correctifs/GARDE_FOU.md; echo;
  cat "$D/ANALYSE_PALANTIR.md"; echo; echo "---"; echo; cat "$BRIEF"; } \
  | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
  > "$D/journal_${N}.log" 2>&1
echo "${N} termine, code $?" >> "$D/journal_${N}.log"
