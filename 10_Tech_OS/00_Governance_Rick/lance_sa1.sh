#!/bin/bash
set -u
D="C:/Users/amado/ASpace_OS_V3/10_Tech_OS/00_Governance_Rick"
export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"
cd "$D" || exit 1
cat "$D/HANDOFF_SECURITY_ARCHITECTURE_V1.md" "$D/SECURITY_ARCHITECTURE_V1.md" \
  | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
  > "$D/journal_security.log" 2>&1
echo "[$(date '+%H:%M:%S')] Sec Arch V1 termine (exit $?)" >> "$D/journal_security.log"
