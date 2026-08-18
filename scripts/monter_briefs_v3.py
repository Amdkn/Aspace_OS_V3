"""Genere les briefs de la passe V3 : quatre couches, sorties disjointes.

POURQUOI CETTE PASSE DIFFERE DE CELLE SUR LA V2
Sur la V2, les agents distillaient un corpus qu'ils ne pouvaient pas lire —
63 260 fichiers. Ils travaillaient sur un echantillon declare.

Sur la V3, le corpus tient : 501 dossiers, 1 014 fichiers porteurs, et une
carte de 48 Ko qui se lit d'un trait. **L'exhaustivite est atteignable**, et
les briefs l'exigent. Un agent qui rend une couverture partielle ici doit dire
pourquoi, et ce ne sera pas la taille.

CE QUI CHANGE AUSSI : LA STRUCTURE EST DEJA UN GRAPHE
L'imbrication (partOf) et les codes de rang (hasRank, operatesLayer) sont deja
extraits mecaniquement — 6 091 triplets. Les agents ne les reproduisent pas.
Ils posent ce que la structure ne peut pas dire : ce que chaque acteur FAIT.
"""

import io
import os
import shutil

V3 = r"C:\Users\amado\ASpace_OS_V3"
D = os.path.join(V3, "70_Onthologies")
BASE = "C:/Users/amado/ASpace_OS_V3/70_Onthologies"
RACINE = "C:/Users/amado/ASpace_OS_V3"

COUCHES = {
    "v3-amadeus": dict(
        titre="00_Amadeus — l'identite et l'appareil",
        racine="00_Amadeus/",
        volume="543 fichiers",
        angle="""C'est la racine identitaire, et elle porte l'appareil qui fait tourner le
reste : `10_Observers/` (les observateurs et leur REGISTRY.json),
`20_Harness/` (les runners : agentgateway, bmad-loop, hermes, codex, multica…),
`30_MEMORY_CORE/` (la memoire et ses cartographies), `30_Shadow/`,
`40_Predictions/`, `60_Tape_Specs/ADR/`.

**Les ADR de `60_Tape_Specs/ADR/` sont la matiere la plus dense** : quatre
dossiers nommes `L0_Kernel_OS`, `L0_Tech_OS`, `L1_Life_OS`, `L2_Business_OS`.
Ils disent la correspondance couche -> OS en clair. Commence par la.

`REGISTRY.json` dans `10_Observers/`, `20_Harness/` et `30_Shadow/` : ces trois
registres declarent ce qui existe. Lis-les : un registre est un contrat, pas
une liste."""),

    "v3-tech": dict(
        titre="10_Tech_OS — le mecanisme",
        racine="10_Tech_OS/",
        volume="97 fichiers — la couche la plus petite, donc la plus lisible entierement",
        angle="""97 fichiers : **tu peux tout ouvrir**. Aucune excuse de couverture ici.

Cherche `00_Governance_Rick/` (LAW.md, SOUL.md, le replicator, `cores.json`,
`spawn.py`) et `11_Kernel_Core_13th/` avec ses compagnons.

La these a verifier contre la structure : Rick gouverne **le mecanisme qui
produit les trois OS**, pas les trois OS. Si l'arborescence dit autre chose que
les documents, **dis-le** — c'est exactement le genre d'ecart qui compte.

`cores.json` et `spawn.py` sont des artefacts executables : ils disent ce qui
se passe vraiment, pas ce qu'on a voulu. Un fichier de configuration prime sur
une prose qui le decrit."""),

    "v3-life": dict(
        titre="20_Life_OS — la conscience",
        racine="20_Life_OS/",
        volume="361 fichiers",
        angle="""La couche la mieux structuree de la V3, et celle ou l'arborescence est la
plus parlante.

`00_Gatekeepers_Beth_Morty/` porte `A1_Beth_Spec.md` et `A1_Morty_Spec.md` :
deux personas au **rang A1**, plus `Beth_Alignment_Log/`,
`Morty_Global_Queue/`, `Sunday_Uplink_Protocols/`.

`21_Ikigai_Orville/` porte `A2_Orville_Spec.md` (**rang A2**) et se decompose
en deux axes que la structure nomme explicitement :

- `01_Pillars_Identity/` — quatre piliers, chacun avec sa persona **A3** :
  Profession/Mercer, Mission/Grayson, Passion/Malloy, Vocation/Finn ;
- `02_Horizons_Time/` — quatre horizons avec leur persona **A3** :
  H1/Isaac, H3/Lamarr, H10/Bortus, H30/Alara.

**La correspondance pilier -> persona et horizon -> persona est portee par les
noms de dossiers.** Ecris-la en triplets ; c'est le coeur de cette couche.

Chaque persona a deux fichiers : un `_Spec.md` et un `_Bootstrap_Finding.md`.
Ils ne disent pas la meme chose — la spec pose l'intention, le bootstrap
rapporte ce qui a ete constate. **Quand ils divergent, cite les deux.**"""),

    "v3-business": dict(
        titre="30_Business_OS — l'action",
        racine="30_Business_OS/",
        volume="2 988 fichiers, mais l'immense majorite sont des captures .png",
        angle="""**Attention au compte.** Sur 2 988 fichiers, la plupart sont des `.png` de
captures d'ecran. Le corpus porteur de structure est bien plus petit : va voir
la carte plutot que de te fier au volume.

C'est la couche la moins bien couverte par la structure : peu de codes de rang
dans les noms (`B1` 3, `B2` 1, `B3` 3). Deux lectures possibles, et tu dois
trancher : soit la fractale B1/B2/B3 n'est pas encore posee dans la V3, soit
elle l'est ailleurs qu'en nom de fichier.

`09_Blueprints/` porte les plans. Si Coach OS y figure comme premiere franchise
prototype, dis-le avec sa source."""),
}

BRIEF = """# BRIEF — ontologie V3 : {titre}

## Ce que tu produis

Des **triplets sujet-verbe-objet** sur A'Space OS, lus dans l'arborescence
**V3** et dans ses fichiers. Pas un resume : des assertions atomiques,
chacune sourcee par un chemin reel.

## Ton perimetre EXCLUSIF en ecriture

```
{base}/triplets/{cle}.jsonl
{base}/_briefs/RAPPORT_{cle}.md
```

**Deux fichiers.** Trois autres agents travaillent sur les trois autres
couches. Tu ne touches a rien d'autre — ni aux `.ttl`, qui sont generes, ni
aux triplets d'une autre couche.

**`ASpace_OS_V3/` est en lecture seule.** Tu l'ontologises, tu ne le modifies
pas.

## Ce que tu lis

```
{base}/_structure/CARTE_V3.md               la carte complete — 48 Ko, lisible d'un trait
{base}/_structure/structure_mesure.json     les 73 fichiers porteurs d'un code de rang
{racine}/{racine_couche}                    TA couche, en entier
```

**Commence par la carte.** Elle donne toute l'arborescence, avec les codes de
rang deja reperes. Ouvre ensuite les fichiers de ta couche.

## Ce qui est DEJA fait, et que tu ne refais pas

L'imbrication (`partOf`) et les codes de rang (`hasRank`, `operatesLayer`) ont
ete extraits mecaniquement : **6 091 triplets structurels** sont deja poses.

Ne les reproduis pas. Tu poses ce que la structure **ne peut pas dire** : ce
que chaque acteur fait, sur quoi il a autorite, ce qu'il produit, ce qu'il
interdit, dans quel ordre les choses s'enchainent.

## Ta couche

**Racine** : `{racine_couche}` — {volume}

{angle}

## La difference avec la passe V2

La V2 comptait 63 260 fichiers : les agents travaillaient sur un echantillon
declare, et c'etait honnete de le dire.

**Ici le corpus tient.** Ta couche est lisible en entier. Si ta couverture est
partielle, la cause ne sera pas la taille — dis laquelle.

## Le format de sortie

`triplets/{cle}.jsonl` — un triplet par ligne, JSON strict :

```json
{{"sujet":"beth","verbe":"hasRank","objet":"a1","objet_type":"entite","phrase":"Beth est une persona de rang A1, gardienne avec Morty","source":"20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md","confiance":"haute"}}
```

| champ | regle |
|---|---|
| `sujet` | cle en `kebab-case` |
| `verbe` | voir ci-dessous |
| `objet` | une entite, ou un litteral si `objet_type` vaut `litteral` |
| `source` | **obligatoire** — chemin relatif a `ASpace_OS_V3/`, qui doit exister |
| `confiance` | `haute` si un fichier l'ecrit ; `moyenne` si tu deduis |

Verbes du schema, a reutiliser en priorite : `governs`, `partOf`, `dependsOn`,
`appliesTo`, `refines`, `instantiates`, `pairedWith`, `handledBy`, `cites`,
`supersedes`, `seeAlso`, `stewards`, `covers`, `routes`, `hasVetoOver`,
`produces`, `escalates`, `directs`, `inherits`.

Un verbe neuf doit servir **au moins trois fois**. En dessous, ce n'est pas un
verbe, c'est une occurrence.

**Un mot sur le veto** : la passe precedente a produit trois verbes pour la
meme notion (`hasVetoOver`, `vetoes`, `halts`) parce que trois agents ne se
voyaient pas. **Utilise `hasVetoOver`** et rien d'autre pour un droit d'arret.

## Ce qu'on attend

**{cible} triplets au minimum**, tous sources.

Atomicite : un triplet qui contient « et » est presque toujours a couper.
Utilite : si un triplet ne changerait la reponse a aucune question, ne
l'ecris pas.

## Interdits

- Aucune assertion sans source verifiable dans la V3.
- Aucune modification de quoi que ce soit hors de tes deux fichiers.
- Ne tranche aucune contradiction : ecris les deux versions avec leurs sources.
- Aucun `git`, aucune installation.

## Ton rapport

`_briefs/RAPPORT_{cle}.md` : combien de triplets, combien de fichiers de ta
couche tu as **reellement ouverts** sur combien, les verbes neufs proposes, les
contradictions, et **les ecarts entre ce que la structure dit et ce que les
documents disent** — c'est ce qui a le plus de valeur.
"""

LANCE = """#!/usr/bin/env bash
# Lance un agent d'ontologie V3 sur M3.
#   Usage : ./lance-v3.sh v3-amadeus|v3-tech|v3-life|v3-business

set -u
QUOI="${1:?usage: lance-v3.sh v3-amadeus|v3-tech|v3-life|v3-business}"

V3="C:/Users/amado/ASpace_OS_V3"
D="$V3/70_Onthologies"
BRIEFS="$D/_briefs"

case "$QUOI" in v3-amadeus|v3-tech|v3-life|v3-business) ;;
  *) echo "inconnu : $QUOI" >&2; exit 2 ;; esac

GARDE="$BRIEFS/GARDE_FOU.md"
BRIEF="$BRIEFS/BRIEF_${QUOI}.md"
LOG="$BRIEFS/journal_${QUOI}.log"

for f in "$GARDE" "$BRIEF"; do
  [ -f "$f" ] || { echo "manquant : $f" >&2; exit 3; }
done

# La carte est la matiere premiere : sans elle l'agent broderait.
CARTE="$D/_structure/CARTE_V3.md"
[ -s "$CARTE" ] || { echo "carte absente : $CARTE" >&2; exit 4; }

export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"

cd "$V3" || exit 1

cat "$GARDE" "$BRIEF" \\
  | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \\
  > "$LOG" 2>&1
CODE=$?
echo "ontologie V3 $QUOI terminee, exit=$CODE, journal=$LOG"
exit $CODE
"""

CIBLES = {"v3-amadeus": 50, "v3-tech": 40, "v3-life": 60, "v3-business": 35}


def main():
    for cle, d in COUCHES.items():
        champs = {k: v for k, v in d.items() if k != "racine"}
        txt = BRIEF.format(cle=cle, base=BASE, racine=RACINE,
                           racine_couche=d["racine"], cible=CIBLES[cle], **champs)
        io.open(os.path.join(D, "_briefs", f"BRIEF_{cle}.md"), "w", encoding="utf-8").write(txt)
        print(f"BRIEF_{cle}.md  {len(txt)} octets  cible={CIBLES[cle]}")
    io.open(os.path.join(D, "_briefs", "lance-v3.sh"), "w", encoding="utf-8", newline="\n").write(LANCE)
    print("lance-v3.sh pose")


if __name__ == "__main__":
    main()
