#!/usr/bin/env bash
# Verrou a jetons partage entre TOUTES les boucles d'agents du poste.
#
# POURQUOI UN VERROU ET PAS UN COMPTEUR
# `ps -W | grep -c node.exe` compte deja tous les processus de la machine :
# le compteur est partage de fait. Ce qui manque, c'est l'exclusion mutuelle.
# Deux boucles peuvent compter en meme temps, voir de la place, et lancer
# toutes les deux — le compte etait juste, la decision etait fausse.
#
# Un jeton = un fichier dans SLOTS. Sa creation par `mkdir` est ATOMIQUE sur
# NTFS comme sur POSIX : deux boucles qui tentent le meme jeton, une seule
# gagne. C'est ce que ne garantit aucune lecture de compteur.
#
# LE JETON PERIME
# Un agent tue laisse son jeton derriere lui et bloquerait une place pour
# toujours. Tout jeton plus vieux que TTL est donc balaye avant chaque
# tentative. Sans ce balayage, le verrou se degrade en blocage.

SLOTS="${SLOTS:-C:/Users/amado/.aspace_slots}"
MAX_SLOTS="${MAX_SLOTS:-8}"     # agents claude -p simultanes, TOUTES boucles
TTL_MIN="${TTL_MIN:-45}"        # au-dela, le jeton est repute perime

mkdir -p "$SLOTS" 2>/dev/null

_balayer() {
  find "$SLOTS" -maxdepth 1 -type d -name 'slot_*' -mmin "+$TTL_MIN" \
    -exec rm -rf {} + 2>/dev/null
}

slots_libres() {
  _balayer
  local pris
  pris=$(find "$SLOTS" -maxdepth 1 -type d -name 'slot_*' 2>/dev/null | wc -l)
  echo $(( MAX_SLOTS - pris ))
}

# prendre_jeton <etiquette> -> imprime le chemin du jeton, ou rien si plein
prendre_jeton() {
  local etiquette="$1"
  _balayer
  local i
  for i in $(seq 1 "$MAX_SLOTS"); do
    local j="$SLOTS/slot_$i"
    # mkdir echoue si le repertoire existe : c'est l'atomicite qu'on veut.
    if mkdir "$j" 2>/dev/null; then
      echo "$etiquette $$ $(date +%s)" > "$j/proprietaire"
      echo "$j"
      return 0
    fi
  done
  return 1
}

rendre_jeton() {
  [ -n "${1:-}" ] && rm -rf "$1" 2>/dev/null
}

# attendre_jeton <etiquette> [secondes_max] -> imprime le jeton obtenu
attendre_jeton() {
  local etiquette="$1" max="${2:-1800}" debut
  debut=$(date +%s)
  while true; do
    local j
    if j=$(prendre_jeton "$etiquette"); then echo "$j"; return 0; fi
    if [ $(( $(date +%s) - debut )) -ge "$max" ]; then return 1; fi
    sleep 20
  done
}

etat_slots() {
  _balayer
  local pris
  pris=$(find "$SLOTS" -maxdepth 1 -type d -name 'slot_*' 2>/dev/null | wc -l)
  echo "  jetons : $pris / $MAX_SLOTS pris"
  local d
  for d in "$SLOTS"/slot_*; do
    [ -d "$d" ] || continue
    echo "    $(basename "$d") : $(cat "$d/proprietaire" 2>/dev/null)"
  done
}
