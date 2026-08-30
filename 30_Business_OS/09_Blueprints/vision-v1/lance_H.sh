#!/bin/bash
# Lance l'agent H — remesure du tableau des ecarts. Bloc d'invocation de CLAUDE.md,
# recopie tel quel : les cinq pieges y sont neutralises.
set -u

DEPOT="C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/vision-v1"

export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"

cd "$DEPOT" || exit 1

# Le brief ouvre sur `---` : par STDIN, jamais en argument (piege 3).
cat BRIEF_H_ECARTS_REELS.md \
  | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
  > journal_H.log 2>&1

echo "[$(date '+%H:%M:%S')] agent H termine (exit $?)" >> journal_H.log
