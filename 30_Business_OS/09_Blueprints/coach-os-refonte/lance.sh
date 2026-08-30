#!/usr/bin/env bash
# Lance des agents M3 en parallele. Usage : bash lance.sh N1 N2 N3 N4
#
# Pieges de CLAUDE.md respectes :
#  - export explicite de ANTHROPIC_BASE_URL (le shell exporte api.anthropic.com
#    et ecrase settings.json : la cle M3 partirait chez Anthropic, avec un
#    "Invalid API key" et un exit 0 trompeur) ;
#  - chemin absolu vers claude (introuvable dans les shells d'arriere-plan) ;
#  - brief par STDIN (un brief commencant par # ou --- casse le parseur d'options).
set -u
cd "$(dirname "$0")"

export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"
CC=/c/Users/amado/AppData/Roaming/npm/claude

V2="C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise"
mkdir -p analyses logs

for T in "$@"; do
  [ -f "BRIEF_$T.md" ] || { echo "BRIEF_$T.md introuvable"; continue; }
  # timeout : un agent qui n'a pas rendu en 1h est bloque, pas lent. Sans cette
  # borne, un fils qui n'ecrit jamais son code de sortie fige le `wait` final —
  # c'est arrive le 2026-08-05 : 4h15 d'attente pour un travail deja termine.
  ( cat "BRIEF_$T.md" | timeout 3600 "$CC" -p --effort max --permission-mode bypassPermissions \
        --add-dir "$V2" > "logs/$T.log" 2>&1
    echo "$T rendu (rc=$?)" ) &
  sleep 5      # etalement : 4 coeurs seulement
done
wait
echo "=== tous rendus ==="
ls -la analyses/
