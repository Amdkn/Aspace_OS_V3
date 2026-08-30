#!/bin/bash
set -u
DEPOT="C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/ontologie-trois-couches"
export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"
cd "$DEPOT" || exit 1
cat BRIEF_I_GEORDI_ENTITES.md \
  | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
  > journal_I.log 2>&1
echo "[$(date '+%H:%M:%S')] agent I termine (exit $?)" >> journal_I.log
