#!/usr/bin/env bash
# Enrichissement des apps : un agent M3 par app, en parallele.
# Chacun travaille dans le depot coach-os (--add-dir) et n'y touche que son app.
set -u
cd "$(dirname "$0")"
export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"
CC=/c/Users/amado/AppData/Roaming/npm/claude
REPO="C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os"
mkdir -p logs
for A in "$@"; do
  ( cd "$REPO" && cat "C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/BRIEF_APP_$A.md" \
      | timeout 3600 "$CC" -p --effort max --permission-mode bypassPermissions \
      > "C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/logs/app_$A.log" 2>&1
    echo "$A rendu (rc=$?)" ) &
  sleep 6
done
wait
echo "=== toutes les apps rendues ==="
