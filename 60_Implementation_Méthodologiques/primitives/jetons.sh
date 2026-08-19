#!/usr/bin/env bash
# Verrou a jetons partage entre TOUTES les boucles d'agents du poste.
#
# Source :  source "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/primitives/jetons.sh"
#
# ------------------------------------------------------------------------
# CE QUI EST REPRIS DE LA PREMIERE VERSION, ET QUI ETAIT JUSTE
#
# Le diagnostic : `ps -W | grep -c node.exe` compte deja tous les processus
# de la machine, donc le compteur etait partage de fait. Ce qui manquait,
# c'est l'EXCLUSION MUTUELLE — deux boucles peuvent compter au meme instant,
# voir de la place, et lancer toutes les deux. Le compte etait juste, la
# decision etait fausse.
#
# Le mecanisme : `mkdir` echoue si le repertoire existe, et cette operation
# est atomique. MESURE, pas supposee : 40 `mkdir` simultanes sur le meme
# chemin, exactement 1 gagnant.
#
# ------------------------------------------------------------------------
# LES DEUX DEFAUTS CORRIGES ICI, TOUS DEUX REPRODUITS AVANT CORRECTION
#
# 1. LE BALAYAGE VOLAIT LES JETONS VIVANTS.
#    L'age d'un jeton etait lu sur la mtime du repertoire, qui ne bouge plus
#    apres la creation. Un agent vivant depuis plus que TTL perdait donc son
#    jeton, et un second le prenait : deux agents, une place, en silence.
#    Reproduit : jeton vieilli de 60 min, agent vivant, jeton supprime, second
#    `mkdir` reussi.
#
#    Correction : BATTEMENT DE COEUR. Le detenteur touche son jeton tant qu'il
#    vit. La mtime devient donc le dernier signe de vie, et non l'heure de
#    naissance. TTL veut alors dire « aucun signe de vie depuis N minutes »,
#    ce qui est le sens qu'on voulait.
#
# 2. UNE LECTURE D'ETAT MUTAIT L'ETAT.
#    `slots_libres` et `etat_slots` appelaient le balayage. Afficher le statut
#    pouvait donc supprimer le jeton d'un agent vivant. Une commande de
#    diagnostic ne doit jamais changer ce qu'elle diagnostique.
#
#    Correction : le balayage n'a lieu qu'a l'ACQUISITION. Les lectures sont
#    pures et signalent les jetons suspects sans y toucher.
#
# ------------------------------------------------------------------------
# CE QUE CE VERROU NE GARANTIT PAS
#
# Il borne le nombre d'agents lances simultanement. Il ne dit rien de ce
# qu'ils ECRIVENT : deux agents dans des jetons differents peuvent parfaitement
# ecraser le meme fichier. Le cloisonnement des ecritures reste affaire de
# perimetre exclusif dans les briefs.

JETONS_DIR="${JETONS_DIR:-C:/Users/amado/.aspace_slots}"
JETONS_MAX="${JETONS_MAX:-8}"        # agents simultanes, TOUTES boucles confondues
JETONS_TTL_MIN="${JETONS_TTL_MIN:-6}" # minutes sans battement avant peremption
JETONS_BATTEMENT_S="${JETONS_BATTEMENT_S:-60}"

mkdir -p "$JETONS_DIR" 2>/dev/null

# --- interne : ne balaie que ce qui n'a plus donne signe de vie -----------
_jetons_balayer() {
  # -mmin +TTL sur un jeton avec battement signifie : le detenteur n'a pas
  # touche son jeton depuis TTL minutes. Il est mort, ou bloque au point de
  # ne plus battre — dans les deux cas la place doit revenir.
  find "$JETONS_DIR" -maxdepth 1 -type d -name 'jeton_*' \
       -mmin "+$JETONS_TTL_MIN" -exec rm -rf {} + 2>/dev/null
}

# --- lecture PURE : ne modifie rien --------------------------------------
jetons_pris() {
  find "$JETONS_DIR" -maxdepth 1 -type d -name 'jeton_*' 2>/dev/null | wc -l
}

jetons_libres() {
  echo $(( JETONS_MAX - $(jetons_pris) ))
}

jetons_etat() {
  echo "  jetons : $(jetons_pris) / $JETONS_MAX pris   (TTL ${JETONS_TTL_MIN} min sans battement)"
  local d age
  for d in "$JETONS_DIR"/jeton_*; do
    [ -d "$d" ] || continue
    age=$(find "$d" -maxdepth 0 -mmin "+$JETONS_TTL_MIN" 2>/dev/null)
    printf "    %-12s %s%s\n" "$(basename "$d")" \
      "$(cat "$d/proprietaire" 2>/dev/null)" \
      "$([ -n "$age" ] && echo '   <- SUSPECT : plus de battement')"
  done
  # Une lecture ne balaie pas. Elle signale, et laisse decider.
}

# --- acquisition ---------------------------------------------------------
# jetons_prendre <etiquette> -> imprime le chemin du jeton, ou echoue
jetons_prendre() {
  local etiquette="${1:-anonyme}" i j
  _jetons_balayer
  for i in $(seq 1 "$JETONS_MAX"); do
    j="$JETONS_DIR/jeton_$i"
    if mkdir "$j" 2>/dev/null; then
      printf '%s pid=%s depuis=%s\n' "$etiquette" "$$" "$(date '+%H:%M:%S')" \
        > "$j/proprietaire"
      echo "$j"
      return 0
    fi
  done
  return 1
}

jetons_rendre() {
  [ -n "${1:-}" ] && rm -rf "$1" 2>/dev/null
  return 0
}

# jetons_attendre <etiquette> [secondes_max]
jetons_attendre() {
  local etiquette="${1:-anonyme}" max="${2:-2400}" debut j
  debut=$(date +%s)
  while true; do
    if j=$(jetons_prendre "$etiquette"); then echo "$j"; return 0; fi
    if [ $(( $(date +%s) - debut )) -ge "$max" ]; then return 1; fi
    sleep 20
  done
}

# --- LA fonction a utiliser : correcte par construction ------------------
# jetons_avec <etiquette> <commande...>
#
# Prend un jeton, bat pendant toute l'execution, le rend quoi qu'il arrive.
# Le battement meurt avec la commande : c'est ce qui empeche a la fois le
# vol d'un jeton vivant et la fuite d'un jeton mort.
jetons_avec() {
  local etiquette="${1:?etiquette requise}"; shift
  local jeton bat code
  jeton=$(jetons_attendre "$etiquette") || {
    echo "jetons : aucune place pour '$etiquette' apres attente" >&2
    return 75
  }

  # battement de coeur en arriere-plan
  ( while [ -d "$jeton" ]; do touch "$jeton" 2>/dev/null; sleep "$JETONS_BATTEMENT_S"; done ) &
  bat=$!

  # La commande tourne en ARRIERE-PLAN et on attend dessus.
  #
  # Pourquoi ce detour : bash DIFFERE un trap tant qu'une commande de premier
  # plan s'execute. Avec `"$@"` en premier plan, un SIGTERM n'etait traite
  # qu'a la fin de la commande — le jeton restait pris jusqu'a peremption.
  # Mesure : test 7 en echec, jeton toujours la 2 s apres l'interruption.
  #
  # Avec `wait`, bash est interruptible : le trap part tout de suite.
  "$@" &
  local tache=$!

  trap 'kill "$tache" 2>/dev/null; kill "$bat" 2>/dev/null; jetons_rendre "$jeton"; trap - INT TERM; return 130' INT TERM

  wait "$tache"
  code=$?

  kill "$bat" 2>/dev/null
  jetons_rendre "$jeton"
  trap - INT TERM
  return $code
}
