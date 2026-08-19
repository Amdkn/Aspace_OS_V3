#!/usr/bin/env bash
# Vague 2 — huit escouades de domaine, quatre par tour.
#   Usage : ./boucle2.sh [heures]      (defaut : 4)
#
# Le verrou a jetons est partage avec toute autre boucle du poste : deux
# boucles qui comptent en meme temps verraient toutes deux de la place. Le
# jeton, lui, ne se prend qu'une fois.

set -u
HEURES="${1:-4}"
V3="C:/Users/amado/ASpace_OS_V3"
L="$V3/60_Implementation_Méthodologiques/_loop"
source "$L/slots.sh"
FIN=$(( $(date +%s) + HEURES * 3600 ))

export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"

DOMAINES=(aquaman wonder-woman batman superman cyborg green-lantern flash john-jones)

lancer_dom() {
  local d="$1" tour="$2"
  local brief="$L/BRIEF_dom-${d}.md"
  [ -f "$brief" ] || { echo "brief manquant : $brief" >&2; return 1; }
  local jeton
  jeton=$(attendre_jeton "dom-$d/t$tour" 2400) || {
    echo "[$(date +%H:%M:%S)] dom-$d tour $tour : aucun jeton, saute" >> "$L/VAGUE2.log"; return 1; }
  cd "$V3" || return 1
  cat "$L/MODE_FABLE.md" "$brief" \
    | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
    > "$L/journal_dom-${d}_t${tour}.log" 2>&1
  local code=$?
  rendre_jeton "$jeton"
  echo "[$(date +%H:%M:%S)] dom-$d tour $tour termine (exit=$code)" >> "$L/VAGUE2.log"
}

tour=0
echo "[$(date +%H:%M:%S)] Vague 2 demarree — 8 domaines, echeance ${HEURES}h" > "$L/VAGUE2.log"

while true; do
  [ -f "$L/STOP2" ] && { echo "[$(date +%H:%M:%S)] STOP2 — arret propre" >> "$L/VAGUE2.log"; break; }
  [ "$(date +%s)" -ge "$FIN" ] && { echo "[$(date +%H:%M:%S)] echeance — arret" >> "$L/VAGUE2.log"; break; }

  tour=$((tour + 1))
  # Deux vagues de quatre : les huit domaines passent a chaque tour.
  for groupe in "0 1 2 3" "4 5 6 7"; do
    echo "[$(date +%H:%M:%S)] tour $tour, groupe $groupe" >> "$L/VAGUE2.log"
    for i in $groupe; do
      lancer_dom "${DOMAINES[$i]}" "$tour" &
      sleep 30
    done
    wait
  done
done

echo "[$(date +%H:%M:%S)] Vague 2 terminee apres $tour tours" >> "$L/VAGUE2.log"
