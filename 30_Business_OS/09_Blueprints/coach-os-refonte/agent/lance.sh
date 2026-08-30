#!/bin/bash
# Lance un chantier agent sur M3. Argument : A ou B.
set -u
N="$1"
BASE=/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte
DOSSIER="$BASE/agent"
REPO=/c/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os
BRIEF=$(ls "$DOSSIER"/BRIEF_AGENT_${N}_*.md | head -1)

export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"

cd "$REPO" || exit 1
{ cat "$BASE/correctifs/GARDE_FOU.md"; echo;
  echo "Les briefs de ce chantier sont dans : $DOSSIER"; echo;
  cat "$DOSSIER/CONTRAT.md"; echo; echo "---"; echo;
  cat "$BRIEF"; } \
  | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
  > "$DOSSIER/journal_${N}.log" 2>&1
echo "AGENT-${N} termine, code $?" >> "$DOSSIER/journal_${N}.log"
