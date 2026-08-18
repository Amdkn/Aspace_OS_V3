#!/usr/bin/env bash
# Lance un agent d'ontologie sur M3.
#   Usage : ./lance.sh tech|life|business
#
# Memes cinq pieges neutralises que dans 50_Distillation/_briefs/lance.sh :
# exports explicites, chemin absolu, brief par STDIN, garde-fou en tete,
# lancements echelonnes.

set -u
QUOI="${1:?usage: lance.sh tech|life|business}"

V3="C:/Users/amado/ASpace_OS_V3"
D="$V3/70_Onthologies"
BRIEFS="$D/_briefs"

case "$QUOI" in tech|life|business) ;; *) echo "inconnu : $QUOI" >&2; exit 2 ;; esac

GARDE="$BRIEFS/GARDE_FOU.md"
BRIEF="$BRIEFS/BRIEF_${QUOI}.md"
LOG="$BRIEFS/journal_${QUOI}.log"

for f in "$GARDE" "$BRIEF"; do
  [ -f "$f" ] || { echo "manquant : $f" >&2; exit 3; }
done

# Le catalogue et les entites sont la matiere premiere : sans eux l'agent
# broderait au lieu de lire.
for s in "$V3/50_Distillation/ontologie/CATALOGUE.md" \
         "$V3/50_Distillation/ontologie/aspace-entites.ttl"; do
  [ -s "$s" ] || { echo "source absente : $s" >&2; exit 4; }
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
echo "ontologie $QUOI terminee, exit=$CODE, journal=$LOG"
exit $CODE
