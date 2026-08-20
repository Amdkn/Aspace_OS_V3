#!/usr/bin/env bash
# Vague de revue — 386 concepts en attente d'un humain, 18 lots.
#
# POURQUOI CETTE BOUCLE NE RESSEMBLE PAS AUX PRECEDENTES
# Les vagues 1 et 2 produisaient. Celle-ci ne produit rien : elle relit,
# elle contredit, elle propose des verdicts. Le seul chiffre qu'elle doit
# faire bouger est celui des concepts revus par un humain — 37 sur 423.
#
# UN AGENT, UN LOT, UN FICHIER DE SORTIE
# Perimetre exclusif par construction : chaque agent ne peut ecrire que
# _revue/REVUE_<lot>.md. Deux agents ne partagent aucun fichier, donc ils
# ne peuvent pas se reecrire sans le voir.
#
# PLAFOND DE CONCURRENCE
# Deux lancements simultanes au maximum — la ligne de base du poste est
# deja a ~31 node.exe, et le canon plafonne a 45. Le canon du poste documente le
# cout d'en lancer cinq : trois n'ont pas demarre du tout, journal vide,
# exit 127 — le script d'enrobage npm est un fichier que Windows verrouille.

set -uo pipefail

V3="C:/Users/amado/ASpace_OS_V3"
LOOP="$V3/60_Implementation_Méthodologiques/_loop"
SORTIE="$V3/70_Onthologies/_revue"
JOURNAL="$LOOP/REVUE.log"
STOP="$LOOP/STOP_REVUE"
MAX_PARALLELE=1
DB="C:/Users/amado/AppData/Roaming/9router/db/data.sqlite"
CLAUDE="/c/Users/amado/AppData/Roaming/npm/claude"

mkdir -p "$SORTIE"

# --- Le canal -------------------------------------------------------------
# La cle vit dans la base locale de 9Router. Elle n'est jamais affichee ni
# journalisee : seule sa longueur l'est, ce qui suffit a diagnostiquer une
# lecture ratee sans jamais l'ecrire quelque part.
ANTHROPIC_API_KEY="$(python -c "
import sqlite3
d = sqlite3.connect(r'$DB')
r = d.execute('select key from apiKeys where isActive=1 order by createdAt limit 1').fetchone()
print(r[0] if r else '')
")"
export ANTHROPIC_API_KEY
export ANTHROPIC_BASE_URL="http://127.0.0.1:20128"

# --- LES VOIES, ET POURQUOI IL EN FAUT PLUSIEURS -------------------------
# Mesure du 2026-08-20 : deux agents simultanes sur `nvidia/minimaxai/
# minimax-m3` rendent tous les deux
#   429 [nvidia/minimaxai/minimax-m3] Too Many Requests (reset after 3m 5s)
# La voie gratuite NVIDIA ne porte qu'UN agent long a la fois. Le premier
# lot rendu (aquaman) l'a ete parce qu'il etait seul.
#
# Baisser la concurrence a 1 marcherait, et prendrait dix-huit fois le
# temps d'un lot. La bonne reponse est de repartir les lots sur des
# FOURNISSEURS DISTINCTS — c'est la raison d'etre du gateway. Deux agents
# en vol tapent alors deux quotas separes, et aucun ne voit l'autre.
#
# L'ordre compte : les voies sont alternees pour que deux lots consecutifs
# ne tombent jamais chez le meme fournisseur.
# Voies testees une a une le 2026-08-20 avant lancement :
#   ollama/nemotron-3-ultra    PONG
#   nvidia/z-ai/glm-5.2        PONG
#   ollama/gpt-oss:120b        PONG
#   kc/deepseek/deepseek-chat  402 — Kilo Code sans credit
#   qd/qmodel_38max            403 — Qoder non authentifie
# Les deux voies mortes sont ecartees : les garder en rotation ferait
# echouer un lot sur trois pour une raison qui n'a rien a voir avec lui.
#
# ATTENTION : les deux `ollama/` partagent LE MEME quota. Ils ne comptent
# donc que pour UN fournisseur. La separation reelle est Ollama <-> NVIDIA,
# et l'ordre ci-dessous alterne strictement entre les deux — avec
# MAX_PARALLELE=2, les deux agents en vol sont toujours sur des quotas
# differents.
VOIES=(
  "ollama/nemotron-3-ultra"      # Ollama Cloud
  "nvidia/z-ai/glm-5.2"          # NVIDIA NIM
  "ollama/gpt-oss:120b"          # Ollama Cloud
  "nvidia/minimaxai/minimax-m3"  # NVIDIA NIM
)
I_VOIE=0
# Ces trois-la forcaient tous les alias vers un modele mort. Les laisser
# court-circuiterait la bascule automatique du gateway.
unset ANTHROPIC_DEFAULT_SONNET_MODEL ANTHROPIC_DEFAULT_OPUS_MODEL ANTHROPIC_DEFAULT_HAIKU_MODEL

if [ ${#ANTHROPIC_API_KEY} -lt 10 ]; then
  echo "ARRET : cle du gateway illisible dans $DB" | tee -a "$JOURNAL"
  exit 1
fi

journal() { echo "[$(date +%H:%M:%S)] $*" | tee -a "$JOURNAL"; }

# --- LE CRENEAU, COMPTE SUR DES PID REELS --------------------------------
# `jobs -r` a l'interieur d'une substitution de commande `$( )` s'evalue
# dans un sous-shell, dont la table des taches n'est pas celle du script.
# Le compte rendu etait faux et la boucle restait bloquee apres UN seul
# lancement, sans message. Un verrou de concurrence qui se trompe est pire
# qu'une absence de verrou : il donne l'illusion d'une vague qui tourne.
#
# On tient donc la liste des PID lances et on interroge le systeme.
PIDS=()

attendre_creneau() {
  while :; do
    local vivants=()
    local p
    for p in ${PIDS[@]+"${PIDS[@]}"}; do
      kill -0 "$p" 2>/dev/null && vivants+=("$p")
    done
    PIDS=(${vivants[@]+"${vivants[@]}"})
    [ "${#PIDS[@]}" -lt "$MAX_PARALLELE" ] && return 0
    sleep 15
  done
}

lancer() {
  local lot="$1" n_attente="$2"
  local nom; nom="$(echo "$lot" | sed 's|[/\\]|-|g')"
  local cible="$SORTIE/REVUE_$nom.md"

  # Reprise : un lot deja relu ne se refait pas. Relancer la vague apres un
  # arret ne doit pas jeter le travail rendu.
  if [ -s "$cible" ]; then
    journal "saute   $lot (deja relu)"
    return 0
  fi

  local brief; brief="$(mktemp)"
  {
    cat "$LOOP/GARDE_FOU_REVUE.md"
    cat <<EOF

---

# BRIEF — relire le lot \`$lot\`

## Ton perimetre, exclusif

**Lecture seule** : tous les fichiers \`.md\` de
\`$V3/$lot/\` — **$n_attente concepts en attente d'un humain**.

**Ecriture, un seul fichier** :
\`$cible\`

Aucun autre fichier. Ni dans ce lot, ni ailleurs.

## Le fichier que tu rends

Commence par declarer ta couverture, puis suis ce plan :

\`\`\`markdown
# Revue — $lot

**Couverture : X concepts lus sur $n_attente.**
(si X < $n_attente, dis lesquels tu n'as pas lus et pourquoi)

## Verdicts proposes

| concept | verdict | motif |
|---|---|---|
| \`nom-du-fichier.md\` | accepter \| reserver \| rejeter | une phrase |

## Contradictions

Pour chacune : les deux concepts, la citation de chacun, et **pourquoi le
corpus ne permet pas de trancher**. Laisse-la ouverte.

## Affirmations a source unique

Le concept, la citation, et la source unique sur laquelle elle repose.

## Decisions presentees comme acquises

Ce qui est ecrit au present de l'indicatif alors qu'aucun humain n'a tranche.

## Ce qui manque

Ce que ce bundle aurait du contenir et ne contient pas.
\`\`\`

## Les trois verdicts, et ce qu'ils engagent

- **accepter** : tu ne vois aucune raison de douter. Le proprietaire
  tamponnera sans relire le concept entier.
- **reserver** : c'est probablement juste, mais une affirmation precise
  demande verification. **Dis laquelle.** C'est le verdict le plus utile.
- **rejeter** : tu as trouve une erreur, une contradiction non resolue, ou
  une source qui ne dit pas ce que le concept lui fait dire. **Cite.**

Dans le doute, **reserver**. Un « accepter » de complaisance fait passer une
affirmation non verifiee pour une decision du proprietaire — c'est
exactement la faute que cette vague repare.

## Rappel

Tu n'ecris **aucun concept**, tu ne modifies **aucun \`verified\`**. Tu
proposes ; le proprietaire tranche.
EOF
  } > "$brief"

  # La voie de ce lot. On tourne, pour que deux agents en vol ne tapent
  # jamais le meme quota fournisseur.
  local voie="${VOIES[$((I_VOIE % ${#VOIES[@]}))]}"
  I_VOIE=$((I_VOIE + 1))

  journal "lance   $lot ($n_attente concepts) via $voie"
  # `< "$brief"` plutot que `cat | claude` : une redirection ne laisse
  # aucun doute sur ce que l'enfant lit. Avec un tube, l'enfant garde un
  # acces a l'entree standard heritee — c'est ce qui a vide le fichier des
  # lots au premier tour et fige la boucle apres un seul lancement.
  (
    export ANTHROPIC_MODEL="$voie"
    export ANTHROPIC_SMALL_FAST_MODEL="$voie"
    "$CLAUDE" -p --permission-mode bypassPermissions \
      < "$brief" > "$SORTIE/.log_$nom" 2>&1
    rc=$?
    if [ -s "$cible" ]; then
      journal "RENDU   $lot ($(wc -l < "$cible") lignes) via $voie"
    else
      # On remonte la PREMIERE ligne d'erreur dans le journal. Un « VIDE »
      # sans motif oblige a ouvrir dix-huit fichiers pour comprendre.
      journal "VIDE    $lot (rc=$rc, $voie) — $(head -1 "$SORTIE/.log_$nom" 2>/dev/null | cut -c1-90)"
    fi
    rm -f "$brief"
  ) &
  PIDS+=("$!")
}

# --- La boucle ------------------------------------------------------------
journal "=== vague de revue : 386 concepts, 18 lots, max $MAX_PARALLELE en vol ==="

# La liste des lots est lue sur le DESCRIPTEUR 3, pas sur l'entree standard.
# Tout processus lance dans la boucle herite de stdin ; s'il le lit — et un
# agent le fait — il vide la liste et la boucle s'arrete apres un tour, sans
# le moindre message d'erreur. C'est ce qui s'est produit au premier essai :
# un seul lot lance, journal muet, boucle figee.
while IFS='|' read -r lot n <&3; do
  [ -z "$lot" ] && continue
  [ -f "$STOP" ] && { journal "STOP demande"; break; }

  attendre_creneau

  lancer "$lot" "$n"
  sleep 90   # echelonnement : cinq lancements dans la meme seconde ont deja
             # produit trois journaux vides et des exit 127.
done 3< "$LOOP/LOTS_REVUE.txt"

wait
journal "=== vague terminee — $(ls -1 "$SORTIE"/REVUE_*.md 2>/dev/null | wc -l) lots rendus ==="
