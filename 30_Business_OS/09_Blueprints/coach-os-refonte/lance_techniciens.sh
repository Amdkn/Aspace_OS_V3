#!/usr/bin/env bash
# Lance les 5 techniciens M3 en parallele, un par grappe thematique.
#
# Pieges de CLAUDE.md respectes ici :
#  - export explicite de ANTHROPIC_BASE_URL : le shell exporte api.anthropic.com
#    et ecrase settings.json, la cle M3 partirait chez Anthropic (Invalid API key
#    avec un exit 0 trompeur).
#  - chemin absolu vers claude : introuvable dans certains shells d'arriere-plan.
#  - brief par STDIN : un brief commencant par --- ou # fait echouer le parseur
#    d'options s'il est passe en argument.
set -u
cd "$(dirname "$0")"

export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"
CC=/c/Users/amado/AppData/Roaming/npm/claude

mkdir -p analyses logs
for T in T1 T2 T3 T4 T5; do
  ( cat "BRIEF_$T.md" | "$CC" -p --effort max --permission-mode bypassPermissions \
      > "logs/$T.log" 2>&1
    echo "$T termine (rc=$?)" ) &
  sleep 4          # etalement : evite 5 demarrages simultanes sur 4 coeurs
done
wait
echo "=== tous les techniciens ont rendu ==="
ls -la analyses/
