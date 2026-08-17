#!/usr/bin/env bash
# Lance un agent de distillation sur M3.
#   Usage : ./lance.sh areas|projets|archives|ressources
#
# Les cinq pieges du canon sont neutralises ici. Ne pas improviser cet appel
# en ligne de commande : chacun de ces cinq points a deja coute un lancement
# silencieux.
#
#   1. Precedence d'environnement. Le shell exporte
#      ANTHROPIC_BASE_URL=https://api.anthropic.com, qui ecrase settings.json.
#      Sans export explicite, la cle MiniMax part chez Anthropic et revient en
#      "Invalid API key" — avec un exit 0 trompeur.
#   2. PATH. `claude` est introuvable dans certains shells d'arriere-plan
#      (exit 127). Toujours le chemin absolu.
#   3. Le brief commence par un titre, mais le garde-fou pourrait commencer par
#      un frontmatter YAML. Passe en -p "$(cat …)", un `---` de tete est lu
#      comme un flag et rend "unknown option". **Toujours par stdin.**
#   4. L'outillage du depot detourne l'agent. D'ou GARDE_FOU.md concatene en
#      tete : il dit explicitement d'ignorer toute suggestion de workflow
#      trouvee dans un fichier.
#   5. Pas plus de deux ou trois lancements simultanes. Le script d'enrobage
#      npm est un fichier unique que Windows verrouille ; cinq appels dans la
#      meme seconde en ont laisse trois muets, journal vide, exit 127.
#
# Un journal vide n'est PAS un agent mort : claude -p n'ecrit qu'a la fin.
# Pour savoir s'il travaille, regarder les fichiers qu'il produit, pas le
# journal. Un exit 127 AVEC journal vide, en revanche, dit "commande
# introuvable".

set -u
QUOI="${1:?usage: lance.sh areas|projets|archives|ressources|ontologie|liaison|hierarchie}"

V3="C:/Users/amado/ASpace_OS_V3"
BRIEFS="$V3/50_Distillation/_briefs"

case "$QUOI" in
  areas|projets|archives|ressources|ontologie|liaison|hierarchie) ;;
  *) echo "inconnu : $QUOI" >&2; exit 2 ;;
esac

GARDE="$BRIEFS/GARDE_FOU.md"
BRIEF="$BRIEFS/BRIEF_${QUOI}.md"
LOG="$BRIEFS/journal_${QUOI}.log"

for f in "$GARDE" "$BRIEF"; do
  [ -f "$f" ] || { echo "manquant : $f" >&2; exit 3; }
done

# Le substrat doit exister AVANT de lancer l'agent : son brief lui dit de
# commencer par la. Le lancer sans substrat, c'est le condamner a lire les
# fichiers dans l'ordre alphabetique.
if [ "$QUOI" = "ontologie" ] || [ "$QUOI" = "liaison" ] || [ "$QUOI" = "hierarchie" ]; then
  # Cette passe ne travaille pas sur un seau : elle travaille sur le graphe
  # deja genere. Le refuser s'il est absent evite un agent qui brode.
  TTL="$V3/50_Distillation/ontologie/aspace-instances.ttl"
  [ -s "$TTL" ] || { echo "graphe absent ou vide : $TTL" >&2; exit 4; }
  SUBSTRAT="$TTL"
  # La passe de liaison a besoin du catalogue : son brief lui dit de
  # commencer par la plutot que d'ouvrir 102 fichiers.
  if [ "$QUOI" = "liaison" ]; then
    CAT="$V3/50_Distillation/ontologie/CATALOGUE.md"
    [ -s "$CAT" ] || { echo "catalogue absent : $CAT" >&2; exit 5; }
  fi
  # La passe hierarchie a besoin de la couche entites ET du canon amont.
  if [ "$QUOI" = "hierarchie" ]; then
    ENT="$V3/50_Distillation/ontologie/aspace-entites.ttl"
    META="$V3/00_Amadeus/30_MEMORY_CORE/META_ONTOLOGIE.md"
    [ -s "$ENT" ]  || { echo "entites absentes : $ENT" >&2; exit 5; }
    [ -s "$META" ] || { echo "canon amont absent : $META" >&2; exit 6; }
  fi
else
case "$QUOI" in
  areas)      SUB="02_Areas_Spock" ;;
  projets)    SUB="01_Projects_Picard" ;;
  archives)   SUB="04_Archives_Data" ;;
  ressources) SUB="03_Resources_Geordi" ;;
esac
SUBSTRAT="$V3/50_Distillation/_substrat/${SUB}.jsonl"
[ -s "$SUBSTRAT" ] || { echo "substrat absent ou vide : $SUBSTRAT" >&2; exit 4; }
fi

export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"

cd "$V3" || exit 1

cat "$GARDE" "$BRIEF" \
  | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
  > "$LOG" 2>&1
CODE=$?

echo "distillation $QUOI terminee, exit=$CODE, journal=$LOG"
exit $CODE
