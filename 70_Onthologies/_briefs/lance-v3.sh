#!/usr/bin/env bash
# Lance un agent d'ontologie V3 sur M3.
#   Usage : ./lance-v3.sh v3-amadeus|v3-tech|v3-life|v3-business

set -u
QUOI="${1:?usage: lance-v3.sh v3-amadeus|v3-tech|v3-life|v3-business}"

V3="C:/Users/amado/ASpace_OS_V3"
D="$V3/70_Onthologies"
BRIEFS="$D/_briefs"

case "$QUOI" in v3-amadeus|v3-tech|v3-life|v3-business) ;;
  *) echo "inconnu : $QUOI" >&2; exit 2 ;; esac

GARDE="$BRIEFS/GARDE_FOU.md"
BRIEF="$BRIEFS/BRIEF_${QUOI}.md"
LOG="$BRIEFS/journal_${QUOI}.log"

for f in "$GARDE" "$BRIEF"; do
  [ -f "$f" ] || { echo "manquant : $f" >&2; exit 3; }
done

# La carte est la matiere premiere : sans elle l'agent broderait.
CARTE="$D/_structure/CARTE_V3.md"
[ -s "$CARTE" ] || { echo "carte absente : $CARTE" >&2; exit 4; }

export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"

cd "$V3" || exit 1

cat "$GARDE" "$BRIEF" \
  | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
  > "$LOG" 2>&1
CODE=$?
echo "ontologie V3 $QUOI terminee, exit=$CODE, journal=$LOG"
exit $CODE
