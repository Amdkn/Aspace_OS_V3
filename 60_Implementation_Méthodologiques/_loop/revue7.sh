#!/usr/bin/env bash
# Revue des 7 domaines restants, via 9Router.
#
# Variante ciblee de `revue.sh`, qui reste intact. Quatre differences, toutes
# nees d'un echec mesure le 2026-08-21 :
#
#  1. PORT 20129, pas 20128. 9Router a ete deplace le 2026-08-21 : les deux
#     routeurs avaient 20128 en defaut et ne pouvaient pas coexister au
#     demarrage. 20128 sert desormais OmniRoute, qui n'a AUCUN fournisseur
#     connecte — y taper rend un pool vide sans message clair.
#  2. `nvidia/z-ai/glm-5.2` RETIRE des voies : mesure du 2026-08-21, il rend
#     410 Gone. Le modele a ete retire par NVIDIA. Une voie morte dans la
#     rotation gaspille un tour sur trois.
#  3. RECUL EXPONENTIEL avec alea sur 429. L'ancienne boucle changeait de voie
#     et abandonnait. Toutes les voies ayant 429 le meme matin, elle a rendu
#     zero fichier en dix-huit lancements. Sans recul, une nouvelle tentative
#     immediate ajoute a la charge qui a cause le refus.
#  4. VERROU et GARDE MEMOIRE. Le 2026-08-21, l'empilement de lancements a
#     epuise le commit Windows : `MEM_COMMIT failed, Win32 error 1455` puis
#     `fork: Resource temporarily unavailable`. Un enfant `claude -p` pese
#     plusieurs centaines de Mo.

set -uo pipefail

V3="C:/Users/amado/ASpace_OS_V3"
LOOP="$V3/60_Implementation_Méthodologiques/_loop"
SORTIE="$V3/70_Onthologies/_revue"
JOURNAL="$LOOP/REVUE7.log"
STOP="$LOOP/STOP_REVUE"
VERROU="$LOOP/.verrou_revue7"
DB="C:/Users/amado/AppData/Roaming/9router/db/data.sqlite"
CLAUDE="/c/Users/amado/AppData/Roaming/npm/claude"

COMMIT_MINI_MB=4000   # marge de commit exigee avant de lancer un enfant
essais_max=3          # budget de tentatives par domaine

# DELAI MAXIMUM PAR ENFANT — le defaut le plus couteux de la premiere version.
# Le 2026-08-21, `claude -p` sur `ollama/nemotron-3-ultra` s'est fige : ni
# reponse, ni erreur, ni sortie. La vague a attendu 6 h 28 sur un seul enfant.
# Pire : la boucle etant bloquee DANS l'enfant, elle n'atteignait jamais le
# test du fichier STOP — l'arret demande ne pouvait pas se produire.
# Un lot de 35 concepts se traite en 1 a 3 minutes quand ca marche.
TIMEOUT_ENFANT=900    # 15 minutes, large

# SEUIL DE COUVERTURE — un rendu creux est pire qu'un echec.
# Le 2026-08-21, `ollama/gpt-oss:120b` a rendu un fichier de 42 lignes en
# 60 secondes annoncant « Couverture : 1 concept lu sur 33 », avec UN verdict.
# Le script l'a compte comme RENDU. Un tel fichier occupe la place, la reprise
# le saute, et le tableau de bord affiche « batman relu » — un faux positif
# exactement du type que le canon nomme : l'instrument accuse le bon coupable
# d'avoir travaille.
# On lit donc la couverture declaree par l'agent lui-meme et on refuse en
# dessous du seuil. C'est le brief qui oblige a la declarer ; autant s'en servir.
SEUIL_COUVERTURE=80   # pourcentage minimum de concepts lus

mkdir -p "$SORTIE"

journal() { echo "[$(date +%H:%M:%S)] $*" | tee -a "$JOURNAL"; }

# --- Verrou ---------------------------------------------------------------
# `mkdir` est atomique : deux instances ne peuvent pas le reussir toutes les
# deux. Un fichier temoin teste puis cree ne l'est pas.
if ! mkdir "$VERROU" 2>/dev/null; then
  echo "Une vague tourne deja (verrou : $VERROU)."
  echo "Si c'est un residu : rmdir '$VERROU'"
  exit 1
fi
trap 'rmdir "$VERROU" 2>/dev/null' EXIT

# --- Le canal -------------------------------------------------------------
ANTHROPIC_API_KEY="$(python -c "
import sqlite3
d = sqlite3.connect(r'$DB')
r = d.execute('select key from apiKeys where isActive=1 order by createdAt limit 1').fetchone()
print(r[0] if r else '')
")"
export ANTHROPIC_API_KEY
export ANTHROPIC_BASE_URL="http://127.0.0.1:20129"

# `settings.json` porte desormais une cle OpenRouter et quatre slots de
# modeles. Les variables d'environnement priment sur le fichier — c'est la
# lecon du 2026-08-21 — mais un AUTH_TOKEN non vide partirait quand meme en
# bearer vers 9Router, qui attend une x-api-key. On le vide, et on retire les
# alias qui forceraient un modele OpenRouter dans un appel 9Router.
export ANTHROPIC_AUTH_TOKEN=""
unset ANTHROPIC_DEFAULT_SONNET_MODEL ANTHROPIC_DEFAULT_OPUS_MODEL \
      ANTHROPIC_DEFAULT_HAIKU_MODEL ANTHROPIC_CUSTOM_MODEL_OPTION 2>/dev/null

if [ ${#ANTHROPIC_API_KEY} -lt 10 ]; then
  journal "ABANDON — cle 9Router illisible (${#ANTHROPIC_API_KEY} caracteres)"
  exit 1
fi

# --- Les voies ------------------------------------------------------------
# Testees vivantes le 2026-08-21 sur 20129. Les deux `ollama/` partagent LE
# MEME quota Ollama Cloud : elles ne comptent que pour une reserve. Il y a
# donc deux reserves reelles, pas trois voies independantes.
VOIES=(
  "nvidia/minimaxai/minimax-m3"   # NVIDIA NIM
  "ollama/gpt-oss:120b"           # Ollama Cloud
  "ollama/nemotron-3-ultra"       # Ollama Cloud (meme quota que ci-dessus)
)

# --- Les 7 domaines restants ---------------------------------------------
# aquaman est deja relu. La reprise le sauterait de toute facon, mais le
# nommer ici evite d'avoir a le deduire.
LOTS=(
  "70_Onthologies/pulse/domaines/batman|33"
  "70_Onthologies/pulse/domaines/cyborg|30"
  "70_Onthologies/pulse/domaines/flash|35"
  "70_Onthologies/pulse/domaines/green-lantern|35"
  "70_Onthologies/pulse/domaines/john-jones|30"
  "70_Onthologies/pulse/domaines/superman|32"
  "70_Onthologies/pulse/domaines/wonder-woman|35"
)

commit_libre_mb() {
  powershell -NoProfile -Command \
    'Get-CimInstance Win32_OperatingSystem | ForEach-Object { [int]($_.FreeVirtualMemory/1KB) }' \
    2>/dev/null | tr -d '\r ' || echo 999999
}

attendre_memoire() {
  local libre
  for _ in $(seq 1 20); do
    libre="$(commit_libre_mb)"
    [ -z "$libre" ] && return 0
    [ "$libre" -ge "$COMMIT_MINI_MB" ] && return 0
    journal "        memoire basse (${libre} Mo de commit libre) — attente 60 s"
    sleep 60
  done
  journal "        memoire toujours basse — on tente quand meme"
}

# Lit « Couverture : X concepts lus sur N » et rend X, ou -1 si la ligne est
# absente. L'agent ecrit parfois « **Couverture : 3 concepts lus sur 33.** » ou
# « Couverture: 3/33 » — on accepte les deux formes.
couverture_lue() {
  local f="$1"
  sed -n 's/.*[Cc]ouverture[^0-9]*\([0-9][0-9]*\).*/\1/p' "$f" 2>/dev/null | head -1
}

# Rend 0 si le rendu est assez couvrant pour etre garde.
rendu_acceptable() {
  local f="$1" n_attente="$2" lot="$3"
  local x seuil
  x="$(couverture_lue "$f")"
  if [ -z "$x" ]; then
    journal "        $lot — aucune ligne de couverture declaree, rendu refuse"
    return 1
  fi
  seuil=$(( n_attente * SEUIL_COUVERTURE / 100 ))
  if [ "$x" -lt "$seuil" ]; then
    journal "        $lot — couverture $x/$n_attente sous le seuil de $seuil, rendu refuse"
    return 1
  fi
  journal "        $lot — couverture $x/$n_attente, au-dessus du seuil de $seuil"
  return 0
}

ecrire_brief() {
  local lot="$1" n_attente="$2" cible="$3" brief="$4"
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
| \\\`nom-du-fichier.md\\\` | accepter \\| reserver \\| rejeter | une phrase |

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
}

# --- La boucle ------------------------------------------------------------
journal "=== revue 7 domaines via 9Router :20129 — ${#VOIES[@]} voies, 1 en vol ==="

i_voie=0
rendus=0

for entree in "${LOTS[@]}"; do
  lot="${entree%%|*}"
  n_attente="${entree##*|}"
  nom="$(echo "$lot" | sed 's|[/\\]|-|g')"
  cible="$SORTIE/REVUE_$nom.md"

  [ -f "$STOP" ] && { journal "STOP demande — arret"; break; }

  if [ -s "$cible" ]; then
    journal "saute   $lot (deja relu)"
    rendus=$((rendus + 1))
    continue
  fi

  essai=1
  while [ "$essai" -le "$essais_max" ]; do
    [ -f "$STOP" ] && { journal "STOP demande — arret"; break 2; }

    voie="${VOIES[$((i_voie % ${#VOIES[@]}))]}"
    i_voie=$((i_voie + 1))

    attendre_memoire

    brief="$(mktemp)"
    ecrire_brief "$lot" "$n_attente" "$cible" "$brief"

    journal "lance   $lot ($n_attente concepts) essai $essai/$essais_max via $voie"

    # Un journal PAR ESSAI. La premiere version reutilisait le meme nom avec
    # `>` : l'essai 3 a efface la sortie de l'essai 2, qui contenait une revue
    # complete des 33 concepts. Le livrable a ete detruit par la mecanique
    # censee le tracer.
    sortie_essai="$SORTIE/.log_${nom}_e${essai}"

    (
      export ANTHROPIC_MODEL="$voie"
      export ANTHROPIC_SMALL_FAST_MODEL="$voie"
      timeout "$TIMEOUT_ENFANT" "$CLAUDE" -p --permission-mode bypassPermissions \
        < "$brief" > "$sortie_essai" 2>&1
    )
    rc=$?
    rm -f "$brief"

    if [ -s "$cible" ]; then
      if rendu_acceptable "$cible" "$n_attente" "$lot"; then
        journal "RENDU   $lot ($(wc -l < "$cible") lignes) via $voie"
        rendus=$((rendus + 1))
        break
      fi
      # Ecarte sans etre detruit : un rendu creux reste une piece a charge
      # contre la voie qui l'a produit.
      mv -f "$cible" "$SORTIE/.creux_${nom}_e${essai}.md" 2>/dev/null
    fi

    # RECUPERATION DE LA SORTIE STANDARD.
    # Les modeles gratuits d'Ollama et NVIDIA sont moins disciplines que Claude
    # sur l'appel de l'outil Write : ils rendent la revue dans leur reponse au
    # lieu de l'ecrire. Mesure du 2026-08-21 : `ollama/gpt-oss:120b` a rendu
    # « Couverture : 33 concepts lus sur 33 » avec le plan complet — sur stdout,
    # et le script a declare VIDE une revue entiere.
    # Le contenu EST le livrable ; le fichier n'est qu'un endroit ou le poser.
    if [ -s "$sortie_essai" ] \
       && grep -qiE '^\s*#{0,3}\s*\**Revue' "$sortie_essai" \
       && grep -qiE 'couverture\s*:' "$sortie_essai"; then
      # On coupe tout ce qui precede le titre : preambule, bavardage, traces.
      if awk '/^\s*#{0,3}\s*\**Revue/{trouve=1} trouve{print}' \
           "$sortie_essai" > "$cible" && [ -s "$cible" ] \
         && rendu_acceptable "$cible" "$n_attente" "$lot"; then
        journal "RECUP   $lot ($(wc -l < "$cible") lignes) via $voie — sortie standard, l'agent n'a pas ecrit le fichier"
        rendus=$((rendus + 1))
        break
      fi
      [ -s "$cible" ] && mv -f "$cible" "$SORTIE/.creux_${nom}_e${essai}.md" 2>/dev/null
      rm -f "$cible"
    fi

    if [ "$rc" -eq 124 ]; then
      motif="FIGE — tue apres ${TIMEOUT_ENFANT}s sans reponse"
    else
      motif="$(head -c 400 "$sortie_essai" 2>/dev/null | tr -d '\n' | cut -c1-110)"
    fi
    journal "VIDE    $lot (rc=$rc, $voie) — $motif"

    # Recul exponentiel avec alea. Sans l'alea, deux reprises retombent en
    # phase et frappent la meme seconde — c'est ce qui transforme un 429 en
    # panne. Base 45 s : 45, 90, 180, plus 0-30 s de dispersion.
    if [ "$essai" -lt "$essais_max" ]; then
      recul=$(( 45 * (2 ** (essai - 1)) + (RANDOM % 30) ))
      journal "        recul ${recul}s avant l'essai suivant"
      sleep "$recul"
    fi
    essai=$((essai + 1))
  done

  [ -s "$cible" ] || journal "ECHEC   $lot — $essais_max essais epuises"
  sleep 20   # echelonnement entre domaines
done

journal "=== termine — $rendus/7 domaines rendus (total corpus : $(ls -1 "$SORTIE"/REVUE_*.md 2>/dev/null | wc -l)) ==="
