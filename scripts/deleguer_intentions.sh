#!/bin/bash
# Delegue l'analyse des intentions a claude-glm, tranche par tranche.
#
# POURQUOI SEQUENTIEL
#   Le plafond mesure du poste est de 2 cadences vives ; au-dela, on a deja vu
#   103 node.exe et un STATUS_COMMITMENT_LIMIT. Une boucle sequentielle en tient
#   une seule. C'est plus lent et ca finit ; du parallele agressif ne finit pas.
#
# POURQUOI EN TRANCHES
#   L'appel unique sur 409 Ko a rendu « Prompt is too long ». Chaque tranche
#   fait ~40 Ko et passe.
#
# set -e est volontaire : un script sans arret sur erreur annonce un succes
# apres l'echec, et c'est un piege deja paye cinq fois sur ce poste.
set -euo pipefail

V3="C:/Users/amado/ASpace_OS_V3"
TR="$V3/50_Distillation/_tranches"
PART="$V3/50_Distillation/_partiels"
GLM="C:/Users/amado/.claude/custom-models/claude-glm.cmd"
mkdir -p "$PART"

echo "=== $(date +%H:%M:%S) demarrage, $(ls -1 "$TR"/tranche_*.md | wc -l) tranches ==="

for f in "$TR"/tranche_*.md; do
  n=$(basename "$f" .md)
  o="$PART/$n.analyse.md"
  if [ -s "$o" ]; then echo "  $n : deja fait, saute"; continue; fi

  echo "  $(date +%H:%M:%S) $n ..."
  # --strict-mcp-config + config MCP vide : sans ca, le plancher de demarrage
  # (~127k tokens de schemas d'outils et de greffons, mesure sur les logs
  # OpenRouter) ne laisse pas de place au travail et l'appel rend
  # « Prompt is too long » avant meme de lire la tranche.
  "$GLM" --dangerously-skip-permissions \
         --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
         -p "Lis le fichier $f en entier.

C'est une tranche d'un corpus d'intentions : chaque puce est le PREMIER message
humain d'une session de travail d'Amadeus, architecte systeme, avec sa date. Les
sous-puces sont ce qui a reellement ete traite ensuite.

Produis en francais, en markdown, SANS preambule :

## Intentions
Les intentions dominantes de cette tranche, avec pour chacune 2 citations reelles
et datees tirees du fichier.

## Besoins reveles
Ce que la repetition trahit et qui n'est pas demande explicitement.

## Problematiques
Ce qui bloque et revient. Nomme les boucles.

## Desirs
Ce qui oriente sans etre demande.

## Ecarts demande/traitement
Les cas ou la sous-puce ne correspond pas a la puce. C'est la que se trouve
souvent le vrai besoin.

REGLES : n'invente aucune date ni citation. Sois concret et bref. Ne resume pas,
analyse. Ecris uniquement le rapport." > "$o" 2>"$PART/$n.err" || {
      echo "    ECHEC sur $n — voir $PART/$n.err"; continue; }

  echo "    -> $(wc -c < "$o") octets"
done

echo "=== $(date +%H:%M:%S) tranches finies, synthese ==="
cat "$PART"/tranche_*.analyse.md > "$PART/_tous_partiels.md" 2>/dev/null || true
echo "  partiels concatenes : $(wc -c < "$PART/_tous_partiels.md") octets"
echo "=== $(date +%H:%M:%S) termine ==="
