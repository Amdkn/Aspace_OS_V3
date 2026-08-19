#!/usr/bin/env bash
# Lance une escouade de la vague 2 sur M3.
#   Usage : ./lance-vague2.sh normatif-sdd-prd|normatif-adr|life-wheel|templates

set -u
QUOI="${1:?usage: lance-vague2.sh normatif-sdd-prd|normatif-adr|life-wheel|templates}"

V3="C:/Users/amado/ASpace_OS_V3"
BRIEFS="$V3/50_Distillation/_briefs_vague2"

case "$QUOI" in normatif-sdd-prd|normatif-adr|life-wheel|templates) ;;
  *) echo "inconnu : $QUOI" >&2; exit 2 ;; esac

GARDE="$BRIEFS/GARDE_FOU.md"
BRIEF="$BRIEFS/BRIEF_${QUOI}.md"
LOG="$BRIEFS/journal_${QUOI}.log"

for f in "$GARDE" "$BRIEF"; do
  [ -f "$f" ] || { echo "manquant : $f" >&2; exit 3; }
done

export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"

cd "$V3" || exit 1

cat "$GARDE" "$BRIEF" \
  | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
  > "$LOG" 2>&1
CODE=$?
echo "escouade vague2 $QUOI terminee, exit=$CODE, journal=$LOG"
exit $CODE
