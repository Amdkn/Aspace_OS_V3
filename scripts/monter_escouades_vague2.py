"""Vague 2 : le corpus normatif, la Life Wheel, les Templates.

CE QUE CETTE VAGUE AJOUTE
La vague 1 a couvert les quatre couches d'A'Space (00_Amadeus, 10_Tech_OS,
20_Life_OS, 30_Business_OS) sous `05_From_V2_Domains/`. Elle a laisse trois
gisements hors perimetre :

  346 documents normatifs   SDD 33 · PRD 53 · ADR 259 (81 familles)
  297 fichiers Life Wheel   09_Life_OS, huit domaines LD01-LD08
  136 fichiers Templates    02_Templates, neuf kits

LE CAS D'ECOLE QUI DEFINIT LA TACHE
SDD-006 a ete trouve le 2026-08-19 : ratifie, scelle, et faux sur un point
(7 domaines au lieu de 8). Il n'est pas perime pour autant — 95 % de son
contenu tient, et c'est la seule source qui detaille les sept escouades
Marvel.

C'est exactement ce que l'utilisateur demande de reperer : **une distillation
obsolete de la V2, mais une synthese quand meme**. Un document peut etre
depasse sur un point et rester la meilleure source sur dix autres. Le declarer
perime en bloc detruirait de la connaissance ; le declarer valide en bloc
propagerait une erreur.

LE PIEGE DE LA DUPLICATION
1 016 fichiers pour 346 documents : la plupart existent en cinq exemplaires.
Un agent qui compte les fichiers au lieu des documents croira son corpus trois
fois plus gros qu'il n'est.
"""

import io
import os
import shutil

V3 = r"C:\Users\amado\ASpace_OS_V3"
BASE = "C:/Users/amado/ASpace_OS_V3"
GEORDI = ("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise"
          "/03_Resources_Geordi")
BRIEFS = os.path.join(V3, "50_Distillation", "_briefs_vague2")

ESCOUADES = {
    "normatif-sdd-prd": dict(
        titre="les SDD et les PRD",
        volume="33 SDD + 53 PRD = 86 documents distincts",
        racines="`05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/`, `04_From_V2_Root/_SPECS/`, et partout ou un fichier commence par `SDD-` ou `PRD-`",
        cible_concepts=14, cible_triplets=45,
        angle="""Les familles visibles : `SDD-V0.2_Micro`, `SDD-V0.3_EngineRoom`,
`SDD-V0.4_EnterpriseComputer`, `SDD-V0.4-Phase2_TacticalOrchestration`,
`SDD-V0.4-Phase3_SummersFractal`, `SDD-V0.5_SovereignConstitution`, et la
serie numerotee `SDD-000` a `SDD-006`.

Cote PRD : `PRD-V0.2.4_UILayout`, `PRD-V0.2.5_IkigaiDeep`,
`PRD-V0.2.6_PARAComplete`, `PRD-V0.2.7_12WYDisciplines`,
`PRD-V0.2.8_GTDComplete`, `PRD-V0.2.9_DEALWorkflow`.

**Les numeros de version portent la chronologie.** V0.2 precede V0.3 precede
V0.4. Etablis la ligne du temps : ce qui est remplace par quoi.

**Le cas SDD-006, deja instruit, est ton modele.** Le fichier s'appelle
`SDD-006_business-pulse-l2-pyramide.md`, mais son titre, son pied de page et
son chemin d'origine disent tous `SDD-005`. Il a ete renomme sans que le
contenu suive, et il est entre en collision avec un autre `SDD-006`
(`_SPECS/SDD/SDD-006_definition-deal-h1-isaac-12wy-curie.md`).

**Cherche d'autres cas de ce type** : un fichier dont le nom contredit son
titre interne, deux documents sous le meme numero. Dans un systeme ou le
numero sert de reference, chaque collision rend une citation ambigue."""),

    "normatif-adr": dict(
        titre="les ADR",
        volume="259 ADR distincts, 81 familles",
        racines="`04_From_V2_Root/_SPECS/ADR/`, `05_From_V2_Domains/**/ADR/`, et partout ou un fichier commence par `ADR-`",
        cible_concepts=16, cible_triplets=50,
        angle="""Les familles les plus fournies :

```
46 ADR-V0      18 ADR-LD01    15 ADR-L2      12 ADR-FWK
10 ADR-AAAS     9 ADR-OMK      8 ADR-INFRA    8 ADR-META
 6 ADR-WARMODE  5 ADR-LOOP     5 ADR-COGNITION
```

81 familles pour 259 documents : la moyenne est de trois ADR par famille.
**Une famille qui n'a qu'un seul ADR n'est pas une famille**, c'est une
occurrence — signale-les, elles disent ou la decision n'a pas fait ecole.

Un ADR porte normalement un **statut** : proposed, accepted, ratified,
superseded, deprecated. **Releve-le systematiquement.** Un ADR `superseded`
qui ne dit pas par quoi est un lien mort ; un ADR `proposed` traite comme du
canon est une erreur qui se propage.

Ne distille pas 259 concepts. Distille les **familles** et les **decisions
structurantes**. Un ADR isole qui ne change rien a l'architecture ne merite
pas un concept — il merite une ligne dans ton rapport."""),

    "life-wheel": dict(
        titre="la Life Wheel — huit domaines LD01 a LD08",
        volume="297 fichiers",
        racines="`09_Life_OS/`",
        cible_concepts=16, cible_triplets=55,
        angle="""Huit domaines, chacun avec sa persona Discovery, et la structure les nomme :

```
LD01_Business_Picard    37    LD02_Finance_Saru       34
LD03_Health_Culber      33    LD04_Cognition_Tilly    68
LD05_Social_Stamets     24    LD06_Family_Burnham     35
LD07_Creativity_Reno    40    LD08_Impact_Georgiou    26
```

**Huit domaines de vie, comme les huit domaines Business.** Cette symetrie est
probablement structurante — verifie si un document la nomme explicitement, ou
si c'est une coincidence de numerotation. Ne l'affirme pas sans source.

`LD04_Cognition_Tilly` est le plus gros (68) : commence par la.

Etablis pour chaque domaine : la persona, son role, ses jauges s'il y en a,
et son rattachement a un Jerry. Une passe precedente a montre que les quatre
Jerry portent des codes `LD01` a `LD08` — **c'est ici que la correspondance
Jerry vers LD se verifie a la source.**

Signale tout LD rattache a aucun Jerry, ou a deux."""),

    "templates": dict(
        titre="les Templates — neuf kits",
        volume="136 fichiers",
        racines="`02_Templates/`",
        cible_concepts=12, cible_triplets=35,
        angle="""Neuf kits, tres inegaux :

```
39  Enterprise_OS_Blueprint_Kit      32  The Perfect Agentic OS Kit
22  FULL Agentic Patterns Kit        16  ClaudeClaw Mission Control Kit
13  fable-wargame-kit                 7  Fable Mindset
 4  ClaudeClaw OS Blueprint Kit       1  Memory Architect Kit
```

Un template n'est pas une doctrine : c'est un **moule**. La question utile
n'est donc pas « qu'est-ce qu'il dit » mais **« qu'est-ce qu'il impose a ce
qui en sort »**.

Pour chaque kit : de quoi est-il le moule, quelles contraintes impose-t-il, et
**a-t-il ete utilise** ? Un kit dont aucun artefact du corpus ne porte la
marque est un moule mort — c'est une information, dis-la.

`Memory Architect Kit` ne fait qu'un seul fichier. Soit c'est un embryon, soit
c'est un index vers autre chose. Tranche."""),
}

BRIEF = """# BRIEF — vague 2 : {titre}

## Ce que tu produis : TROIS livrables, une seule lecture

```
1. {base}/50_Distillation/domaines/{cle}/          concepts OKF v0.2
2. {base}/60_Implementation_Méthodologiques/domaines/{cle}.md   la methode
3. {base}/70_Onthologies/triplets/dom-{cle}.jsonl  les triplets
```

Plus ton rapport : `{briefs}/RAPPORT_{cle}.md`.

**Aucun autre fichier.** Trois autres escouades travaillent en parallele.
**La V2 est en LECTURE SEULE.**

## Ton corpus

**{volume}**

Ou : {racines}

{angle}

## LA QUESTION QUI COMMANDE CETTE VAGUE

L'utilisateur la pose ainsi : reperer les documents qui sont **une distillation
obsolete de la V2 par rapport a la V3, mais une synthese quand meme.**

Un document peut etre **depasse sur un point et rester la meilleure source sur
dix autres**. Le declarer perime en bloc detruirait de la connaissance ; le
declarer valide en bloc propagerait une erreur.

**Le cas d'ecole, deja instruit le 2026-08-19 :**
`SDD-006_business-pulse-l2-pyramide.md` est ratifie, scelle, et **faux sur un
point** — il enumere 7 domaines Business la ou le canon en compte 8, le
huitieme etant John Jones / Martian Manhunter (Sales, escouade Illuminati),
declare dans
`05_From_V2_Domains/00_Amadeus/01_Identity_Core/agents/L2_B2_JohnJones_Sales.md`.

Il n'a **pas** ete reecrit : un amendement a ete appose en fin de fichier,
selon la regle append-only du canon. Le corps reste intact parce que le fait
qu'A'Space ait fonctionne a 7 domaines pendant un mois est lui-meme une
information.

**Pour chaque document que tu examines, classe-le :**

| Verdict | Sens |
|---|---|
| `canon` | fait toujours autorite, rien a signaler |
| `synthese-datee` | depasse sur un point precis, **valable sur le reste** — dis lequel et lequel |
| `superseded` | remplace en entier, et **dis par quoi** |
| `orphelin` | ne se rattache a rien, statut indeterminable |

Un verdict `superseded` sans successeur nomme est un lien mort. Ne l'ecris pas.

## LE PIEGE DE LA DUPLICATION

**1 016 fichiers pour 346 documents normatifs** : la plupart existent en cinq
exemplaires (source du wiki, deux chunks generes, copie vivante, archive).

Compte les **documents**, pas les fichiers. Et quand deux copies divergent, la
copie vivante sous `05_From_V2_Domains/` fait foi — les `chunks/` sont
generes, `_V3_STRUCTURE_2026-08-02/` est une archive.

## Format de sortie

`triplets/dom-{cle}.jsonl`, un triplet par ligne, JSON strict :

```json
{{"sujet":"sdd-006","verbe":"supersedes","objet":"sdd-005","objet_type":"entite","phrase":"SDD-006 remplace SDD-005 sur le decompte des domaines","source":"...chemin reel...","confiance":"haute"}}
```

`source` doit exister — un validateur le verifie. Une source inventee est pire
qu'une source absente, parce qu'elle rassure.

Verbes : `governs`, `partOf`, `dependsOn`, `appliesTo`, `refines`,
`instantiates`, `pairedWith`, `handledBy`, `cites`, `supersedes`, `stewards`,
`covers`, `routes`, `hasVetoOver`, `produces`, `escalates`, `directs`,
`inherits`. Un verbe neuf doit servir **trois fois** au moins.

`supersedes` est le verbe central de cette vague. Utilise-le avec rigueur : il
affirme qu'un document en invalide un autre **en entier**.

## Cibles

- **{cible_concepts} concepts OKF** minimum dans `50_Distillation/domaines/{cle}/`, avec `index.md`
- **1 fichier methode** dans `60_Implementation_Méthodologiques/domaines/{cle}.md`
- **{cible_triplets} triplets** minimum

## Interdits

- Aucune assertion sans source verifiable.
- Aucun verdict `superseded` sans successeur nomme.
- Ne tranche aucune contradiction : ecris les deux versions avec leurs dates.
- Aucune ecriture dans la V2. Aucun `git`, aucune installation.

## Ton rapport

`{briefs}/RAPPORT_{cle}.md` : combien de documents examines sur combien, la
repartition des quatre verdicts, les collisions de numerotation ou de nom
trouvees, et ce que tu attendais sans le trouver.
"""

LANCE = """#!/usr/bin/env bash
# Lance une escouade de la vague 2 sur M3.
#   Usage : ./lance-vague2.sh normatif-sdd-prd|normatif-adr|life-wheel|templates

set -u
QUOI="${1:?usage: lance-vague2.sh normatif-sdd-prd|normatif-adr|life-wheel|templates}"

V3="C:/Users/amado/ASpace_OS_V3"
BRIEFS="$V3/50_Distillation/_briefs_vague2"

case "$QUOI" in normatif-sdd-prd|normatif-adr|life-wheel|templates) ;;
  *) echo "inconnu : $QUOI" >&2; exit 2 ;; esac

GARDE="$BRIEFS/GARDE_FOU.md"
BRIEF="$BRIEFS/BRIEF_${QUOI}.md"
LOG="$BRIEFS/journal_${QUOI}.log"

for f in "$GARDE" "$BRIEF"; do
  [ -f "$f" ] || { echo "manquant : $f" >&2; exit 3; }
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
echo "escouade vague2 $QUOI terminee, exit=$CODE, journal=$LOG"
exit $CODE
"""


def main():
    os.makedirs(BRIEFS, exist_ok=True)
    shutil.copy(os.path.join(V3, "50_Distillation", "_briefs", "GARDE_FOU.md"),
                os.path.join(BRIEFS, "GARDE_FOU.md"))
    for cle, d in ESCOUADES.items():
        os.makedirs(os.path.join(V3, "50_Distillation", "domaines", cle), exist_ok=True)
        txt = BRIEF.format(cle=cle, base=BASE, geordi=GEORDI,
                           briefs=BRIEFS.replace("\\", "/"), **d)
        io.open(os.path.join(BRIEFS, f"BRIEF_{cle}.md"), "w", encoding="utf-8").write(txt)
        print(f"BRIEF_{cle}.md  {len(txt)} octets  cibles {d['cible_concepts']}c / {d['cible_triplets']}t")
    io.open(os.path.join(BRIEFS, "lance-vague2.sh"), "w", encoding="utf-8", newline="\n").write(LANCE)
    print("lance-vague2.sh pose")


if __name__ == "__main__":
    main()
