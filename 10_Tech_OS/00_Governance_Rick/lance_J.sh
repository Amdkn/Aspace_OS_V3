#!/bin/bash
set -u
DEPOT="C:/Users/amado/ASpace_OS_V3/10_Tech_OS/00_Governance_Rick"
export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"
cd "$DEPOT" || exit 1
cat BRIEF_J_DECISIONS_OUBLIEES.md \
  | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
  > journal_J.log 2>&1
echo "[$(date '+%H:%M:%S')] agent J termine (exit $?)" >> journal_J.log
