#!/usr/bin/env bash
# Lance l'agent de conversion methodologique sur M3.
#   Usage : ./lance.sh methodes
#
# Memes cinq pieges neutralises que dans 50_Distillation/_briefs/lance.sh :
# exports explicites, chemin absolu vers claude, brief par STDIN, garde-fou en
# tete, lancements echelonnes.

set -u
QUOI="${1:-methodes}"

V3="C:/Users/amado/ASpace_OS_V3"
D="$V3/60_Implementation_Méthodologiques"
BRIEFS="$D/_briefs"

GARDE="$BRIEFS/GARDE_FOU.md"
BRIEF="$BRIEFS/BRIEF_${QUOI}.md"
LOG="$BRIEFS/journal_${QUOI}.log"

for f in "$GARDE" "$BRIEF"; do
  [ -f "$f" ] || { echo "manquant : $f" >&2; exit 3; }
done

# Les deux extractions doivent exister : le brief dit d'en partir.
for s in "$D/_sources/indydevdan-prompt-systeme.md" "$D/_sources/echelle-autonomie-agents.md"; do
  [ -s "$s" ] || { echo "source absente ou vide : $s" >&2; exit 4; }
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

echo "conversion $QUOI terminee, exit=$CODE, journal=$LOG"
exit $CODE
