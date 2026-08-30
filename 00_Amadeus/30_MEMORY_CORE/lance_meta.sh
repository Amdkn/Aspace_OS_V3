#!/bin/bash
set -u
DEPOT="C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE"
export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"
cd "$DEPOT" || exit 1
cat BRIEF_META_ONTOLOGIE.md \
  | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
  > journal_meta.log 2>&1
echo "[$(date '+%H:%M:%S')] meta-ontologie terminee (exit $?)" >> journal_meta.log
