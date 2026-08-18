"""Monte le bundle 60_Onthologies : index, briefs par couche, lanceur.

POURQUOI CE BUNDLE EST DISTINCT DE 50_Distillation/ontologie/
`50_Distillation/ontologie/` porte le graphe **mecanique** : les 102 concepts
distilles comme sujets, leurs metadonnees, leurs liens. Il decrit des
DOCUMENTS.

`60_Onthologies` porte la reconstitution d'**A'Space lui-meme** en
sujet-verbe-objet : ce qu'est A'Space, qui y agit, selon quelle regle. Les
concepts distilles y deviennent des SOURCES, plus des sujets.

TROIS AGENTS, TROIS COUCHES, SORTIES DISJOINTES
Un agent par couche d'A'Space (Tech, Life, Business). Chacun ecrit dans son
propre fichier de triplets : aucun ne peut ecraser un autre. Le cloisonnement
qui avait coute la connectivite dans la distillation ne coute rien ici, parce
qu'un quatrieme passage recoud, et parce que les triplets sont valides et
fusionnes par script.
"""

import io
import os
import shutil

V3 = r"C:\Users\amado\ASpace_OS_V3"
D = os.path.join(V3, "60_Onthologies")
DIST = "C:/Users/amado/ASpace_OS_V3/50_Distillation"
BASE = "C:/Users/amado/ASpace_OS_V3/60_Onthologies"

COUCHES = {
    "tech": dict(
        titre="Tech OS — le mecanisme qui produit les trois OS",
        entites="`rick`, `tech-os`, `docteur`, `compagnons`, `a0-amadeus`",
        cible=45,
        angle="""Rick gouverne **le mecanisme qui produit les trois OS**, pas les trois OS.
Cette distinction est la these centrale de la couche ; toute assertion qui
l'ignore est fausse.

Cherche : le replicator et ses trois Cores issus du meme gabarit, le noyau et
ses organes, les roles (Spec / Build / Spawn / Review) et la regle que nul ne
cumule Build et Review, le watchdog et ses seuils, les cadences.

`Les Compagnons` n'apparait que dans 1 concept distille et `Les Docteurs` dans
6. Si tu ne trouves pas de quoi les decrire, **dis-le** plutot que d'inventer :
c'est un trou de couverture de la distillation, et c'est une information."""),

    "life": dict(
        titre="Life OS — la conscience",
        entites="`life-os`, `a1`, `a2`, `a3`, `beth`, `morty`, `picard`, `spock`, `data`, `geordi`",
        cible=45,
        angle="""C'est la couche la mieux couverte : `life-os` est cite dans 84 concepts sur
102.

Cherche : les quatre gardiens PARA et le seau que chacun tient, le veto de
Life OS sur Business OS (un HALT qui gele l'acceleration — c'est une relation
d'autorite, pas une dependance), les rangs A1/A2/A3 et ce qu'ils designent,
l'Ikigai et les horizons, les jauges, GTD et 12WY.

Attention a un piege deja documente : le registre Owner « Doctor Who » et le
registre « Star Trek » ne se recouvrent pas terme a terme. Ne les fusionne
pas."""),

    "business": dict(
        titre="Business OS — l'action",
        entites="`business-os`, `b1`, `b2`, `b3`, `jerry`, `summer`",
        cible=45,
        angle="""Cherche : la fractale B1/B2/B3 et ce que chaque etage decide, les huit
domaines et leurs escouades, les quatre Jerry et leur macro-portefeuille, les
Summer's Verse en micro-executif, Coach OS comme premiere franchise prototype.

Une contradiction est **deja connue et ne doit pas etre tranchee** : le canon
pose une pyramide stricte (L0 >= L1 > L2 en autorite), l'utilisateur dit que L2
est unifie dans L1. Ecris les deux assertions, chacune avec sa source, et
signale-les dans ton rapport.

Un rapport anterieur note aussi que SDD-006 decrit 7 domaines alors que le
canon a jour en compte 8 — le code etait en avance sur le document. Si tu
rencontres les deux comptes, ecris le plus recent et signale l'ecart."""),
}

INDEX = """---
type: Bundle index
title: 60_Onthologies — A'Space OS reconstitue en sujet-verbe-objet
description: Le graphe RDF d'A'Space lui-meme, forme par des agents lisant la distillation. Trois couches, trois agents, un vocabulaire ferme.
tags: [ontologie, rdf, triplets, aspace, sujet-verbe-objet]
generated: {{ by: claude-opus-5, at: 2026-08-17T22:00:00Z }}
verified:
  - {{ by: process:graphe-distillation, at: 2026-08-17T21:55:00Z }}
sources:
  - id: distillation
    resource: 50_Distillation/ — 102 concepts OKF, 3 624 triplets sur six fichiers Turtle
    title: La distillation du PARA V2
    last_modified: 2026-08-17
  - id: rdf
    resource: https://www.w3.org/TR/rdf12-concepts/
    title: RDF 1.2 Concepts and Abstract Data Model
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Ce que ce bundle contient, et ce qu'il n'est pas

Il porte la **reconstitution d'A'Space OS** : ce qu'A'Space est, qui y agit,
selon quelle regle — en triplets sujet-verbe-objet.

Il ne faut pas le confondre avec `50_Distillation/ontologie/`, qui porte le
graphe **mecanique** de la distillation : les 102 concepts comme sujets, leurs
metadonnees, leurs liens. Celui-la decrit des **documents**.

| | sujet du graphe | question a laquelle il repond |
|---|---|---|
| `50_Distillation/ontologie/` | les concepts distilles | « ou est-ce ecrit ? » |
| `60_Onthologies` | A'Space lui-meme | « qu'est-ce qui est vrai ? » |

Ici, les 102 concepts distilles deviennent des **sources**, plus des sujets.

# La forme d'une assertion

Chaque ligne est un triplet, et rien d'autre :

```
sujet          verbe          objet
rick           governs        replicator
life-os        hasVetoOver    business-os
picard         stewards       projets
```

Un triplet sans source n'entre pas dans le graphe. C'est la regle du poste, et
elle est appliquee par un validateur, pas par la bonne volonte : **une entree
sans source est une invention**.

# Trois couches, trois agents

| Agent | Couche | Entites principales |
|---|---|---|
| `tech` | Tech OS — le mecanisme | Rick, les Cores, les Docteurs, A0 |
| `life` | Life OS — la conscience | les gardiens PARA, A1/A2/A3, Beth, Morty |
| `business` | Business OS — l'action | B1/B2/B3, les Jerry, les Summer |

Chacun ecrit dans son propre fichier de triplets. Aucun ne peut ecraser un
autre, et la fusion est faite par script apres validation.

# Directories

- [_briefs](_briefs/) - Garde-fou, briefs par couche, lanceur.
- [triplets](triplets/) - Les assertions brutes, un fichier par couche.
- [sujets](sujets/) - Concepts OKF sur les entites d'A'Space.
- [verbes](verbes/) - Concepts OKF sur les predicats retenus.
"""

BRIEF = """# BRIEF — reconstituer {titre}

## Ce que tu produis

Des **triplets sujet-verbe-objet** sur A'Space OS lui-meme, lus dans la
distillation. Pas un resume, pas une synthese : des assertions atomiques,
chacune sourcee.

## Ton perimetre EXCLUSIF en ecriture

```
{base}/triplets/{cle}.jsonl
{base}/_briefs/RAPPORT_{cle}.md
```

**Deux fichiers.** Deux autres agents travaillent en parallele sur les deux
autres couches. Tu ne touches a rien d'autre — ni aux concepts distilles, ni
aux `.ttl`, qui sont generes.

## Ce que tu lis

```
{dist}/ontologie/CATALOGUE.md        les 102 concepts distilles : titre, description, tags
{dist}/ontologie/aspace-entites.ttl  les 21 entites deja identifiees et leurs alias
{dist}/ontologie/aspace-schema.ttl   les predicats deja definis
{dist}/areas/  {dist}/projets/  {dist}/archives/  {dist}/ressources/
                                     les concepts eux-memes, quand le catalogue ne suffit pas
```

**Commence par le CATALOGUE**, puis ouvre les concepts qui portent ta couche.
Il fait 42 Ko et se lit d'un trait ; il te dit lesquels ouvrir.

## Ta couche

**Entites principales** : {entites}

{angle}

## Le format de sortie

`triplets/{cle}.jsonl` — un triplet par ligne, JSON strict :

```json
{{"sujet":"rick","verbe":"governs","objet":"replicator","objet_type":"entite","phrase":"Rick gouverne le replicator, pas les trois OS qu'il produit","source":"ressources/adr-immutability-ricks-law.md","confiance":"haute"}}
```

| champ | regle |
|---|---|
| `sujet` | une cle d'entite existante, ou une nouvelle en `kebab-case` |
| `verbe` | voir la liste ci-dessous |
| `objet` | une entite, ou un litteral si `objet_type` vaut `litteral` |
| `objet_type` | `entite` ou `litteral` |
| `phrase` | l'assertion en francais, lisible seule |
| `source` | **obligatoire** — le concept distille d'ou elle vient, chemin relatif |
| `confiance` | `haute` si une source l'ecrit ; `moyenne` si tu deduis |

### Les verbes disponibles

Reutilise en priorite ceux du schema : `governs`, `partOf`, `dependsOn`,
`appliesTo`, `refines`, `instantiates`, `pairedWith`, `handledBy`, `cites`,
`supersedes`, `seeAlso`.

Tu peux en **proposer de nouveaux** quand aucun ne dit ce que tu constates —
par exemple `hasVetoOver`, `stewards`, `produces`, `operates`. Un verbe neuf
doit servir **au moins trois fois**, sinon ce n'est pas un verbe, c'est une
occurrence. Liste-les dans ton rapport avec leur definition.

## Ce qu'on attend

**{cible} triplets au minimum**, tous sources.

Vise l'atomicite. « Rick gouverne le mecanisme et delegue aux Cores » n'est pas
un triplet, c'en est deux. Un triplet qui contient « et » est presque toujours
a couper.

Evite les triplets vides de sens : `aspace partOf aspace`, `life-os cites
life-os`. Si un triplet ne changerait la reponse a aucune question, ne l'ecris
pas.

## Interdits

- Aucune assertion sans source. Elle sera rejetee par le validateur.
- N'invente aucun fait que la distillation ne porte pas. Si tu penses savoir
  quelque chose qui n'y est pas, **dis-le dans ton rapport**, pas dans les
  triplets.
- Ne tranche aucune contradiction : ecris les deux versions avec leurs sources.
- Aucun `git`, aucune installation.

## Ton rapport

`_briefs/RAPPORT_{cle}.md` : combien de triplets, quels verbes neufs tu
proposes et pourquoi, quelles contradictions tu as rencontrees, et **ce que la
distillation ne portait pas** alors que tu l'attendais — c'est le plus utile
pour la suite.
"""

LANCE = """#!/usr/bin/env bash
# Lance un agent d'ontologie sur M3.
#   Usage : ./lance.sh tech|life|business
#
# Memes cinq pieges neutralises que dans 50_Distillation/_briefs/lance.sh :
# exports explicites, chemin absolu, brief par STDIN, garde-fou en tete,
# lancements echelonnes.

set -u
QUOI="${1:?usage: lance.sh tech|life|business}"

V3="C:/Users/amado/ASpace_OS_V3"
D="$V3/60_Onthologies"
BRIEFS="$D/_briefs"

case "$QUOI" in tech|life|business) ;; *) echo "inconnu : $QUOI" >&2; exit 2 ;; esac

GARDE="$BRIEFS/GARDE_FOU.md"
BRIEF="$BRIEFS/BRIEF_${QUOI}.md"
LOG="$BRIEFS/journal_${QUOI}.log"

for f in "$GARDE" "$BRIEF"; do
  [ -f "$f" ] || { echo "manquant : $f" >&2; exit 3; }
done

# Le catalogue et les entites sont la matiere premiere : sans eux l'agent
# broderait au lieu de lire.
for s in "$V3/50_Distillation/ontologie/CATALOGUE.md" \\
         "$V3/50_Distillation/ontologie/aspace-entites.ttl"; do
  [ -s "$s" ] || { echo "source absente : $s" >&2; exit 4; }
done

export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"

cd "$V3" || exit 1

cat "$GARDE" "$BRIEF" \\
  | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \\
  > "$LOG" 2>&1
CODE=$?
echo "ontologie $QUOI terminee, exit=$CODE, journal=$LOG"
exit $CODE
"""


def main():
    for sd in ("_briefs", "triplets", "sujets", "verbes"):
        os.makedirs(os.path.join(D, sd), exist_ok=True)

    io.open(os.path.join(D, "index.md"), "w", encoding="utf-8").write(INDEX)

    shutil.copy(os.path.join(V3, "50_Distillation", "_briefs", "GARDE_FOU.md"),
                os.path.join(D, "_briefs", "GARDE_FOU.md"))

    for cle, d in COUCHES.items():
        txt = BRIEF.format(cle=cle, base=BASE, dist=DIST, **d)
        io.open(os.path.join(D, "_briefs", f"BRIEF_{cle}.md"), "w", encoding="utf-8").write(txt)
        print(f"BRIEF_{cle}.md  {len(txt)} octets  cible={d['cible']} triplets")

    io.open(os.path.join(D, "_briefs", "lance.sh"), "w", encoding="utf-8", newline="\n").write(LANCE)
    io.open(os.path.join(D, ".gitignore"), "w", encoding="utf-8").write("_briefs/journal_*.log\n")
    print("index.md, lance.sh, GARDE_FOU.md poses")


if __name__ == "__main__":
    main()
