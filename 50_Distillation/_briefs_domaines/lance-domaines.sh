#!/usr/bin/env bash
# Lance une escouade de domaine sur M3.
#   Usage : ./lance-domaines.sh tech|life|amadeus|business

set -u
QUOI="${1:?usage: lance-domaines.sh tech|life|amadeus|business}"

V3="C:/Users/amado/ASpace_OS_V3"
BRIEFS="$V3/50_Distillation/_briefs_domaines"

case "$QUOI" in tech|life|amadeus|business) ;;
  *) echo "inconnu : $QUOI" >&2; exit 2 ;; esac

case "$QUOI" in
  tech)     COUCHE="10_Tech_OS" ;;
  life)     COUCHE="20_Life_OS" ;;
  amadeus)  COUCHE="00_Amadeus" ;;
  business) COUCHE="30_Business_OS" ;;
esac

GARDE="$BRIEFS/GARDE_FOU.md"
BRIEF="$BRIEFS/BRIEF_${QUOI}.md"
LOG="$BRIEFS/journal_${QUOI}.log"

for f in "$GARDE" "$BRIEF"; do
  [ -f "$f" ] || { echo "manquant : $f" >&2; exit 3; }
done

# La carte est la matiere premiere : sans elle l'agent lit dans l'ordre
# alphabetique et gaspille son budget.
CARTE="$V3/50_Distillation/_substrat_domaines/CARTE_${COUCHE}.md"
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
echo "escouade $QUOI terminee, exit=$CODE, journal=$LOG"
exit $CODE
