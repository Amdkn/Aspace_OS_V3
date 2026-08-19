#!/usr/bin/env bash
# Boucle d'implementation Business OS / Pulse.
#   Usage : ./boucle.sh [heures]      (defaut : 5)
#
# Rotation : (protocoles + b1) -> (b2 + b3) -> (b1 + b2) -> (b3 + b1) -> ...
# Deux agents en parallele au maximum — borne du canon.
#
# TROIS FREINS
#   1. fichier STOP  : depose _loop/STOP et la boucle s'arrete au tour suivant
#   2. echeance      : par defaut 5 heures apres le demarrage
#   3. plafond node  : si plus de 40 node.exe tournent, on attend
#
# Un journal vide n'est PAS un agent mort : claude -p n'ecrit qu'a la fin.

set -u
HEURES="${1:-5}"
V3="C:/Users/amado/ASpace_OS_V3"
L="$V3/60_Implementation_Méthodologiques/_loop"
FIN=$(( $(date +%s) + HEURES * 3600 ))

export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"

lancer() {
  local quoi="$1" tour="$2"
  local brief="$L/BRIEF_${quoi}.md"
  [ -f "$brief" ] || { echo "brief manquant : $brief" >&2; return 1; }
  cd "$V3" || return 1
  cat "$L/MODE_FABLE.md" "$brief" \
    | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
    > "$L/journal_${quoi}_t${tour}.log" 2>&1
  echo "[$(date +%H:%M:%S)] $quoi tour $tour termine (exit=$?)" >> "$L/BOUCLE.log"
}

# Rotation elargie. B3 etait servi une fois sur trois dans la version
# precedente — un desequilibre de ma table, pas des agents. Chaque etage
# apparait maintenant quatre fois sur dix paires.
ROTATION=("frameworks b3" "b1 b2" "protocoles b3" "b2 b1"
          "frameworks b1" "b3 b2" "protocoles b1" "b3 frameworks"
          "b2 b3" "b1 protocoles")
tour=0

echo "[$(date +%H:%M:%S)] boucle demarree, echeance dans ${HEURES}h" > "$L/BOUCLE.log"

while true; do
  if [ -f "$L/STOP" ]; then
    echo "[$(date +%H:%M:%S)] STOP present — arret propre" >> "$L/BOUCLE.log"; break
  fi
  if [ "$(date +%s)" -ge "$FIN" ]; then
    echo "[$(date +%H:%M:%S)] echeance atteinte — arret" >> "$L/BOUCLE.log"; break
  fi

  # Plafond de concurrence : on attend qu'il redescende plutot que de saturer.
  while [ "$(ps -W 2>/dev/null | grep -c node.exe)" -gt 40 ]; do
    echo "[$(date +%H:%M:%S)] plafond node atteint, attente 60s" >> "$L/BOUCLE.log"
    sleep 60
  done

  tour=$((tour + 1))
  paire="${ROTATION[$(( (tour - 1) % ${#ROTATION[@]} ))]}"
  a="${paire%% *}"; b="${paire##* }"
  echo "[$(date +%H:%M:%S)] tour $tour : $a + $b" >> "$L/BOUCLE.log"

  lancer "$a" "$tour" &
  sleep 90                      # echelonnement : npm verrouille son wrapper
  lancer "$b" "$tour" &
  wait                          # les deux finissent avant le tour suivant
done

echo "[$(date +%H:%M:%S)] boucle terminee apres $tour tours" >> "$L/BOUCLE.log"
