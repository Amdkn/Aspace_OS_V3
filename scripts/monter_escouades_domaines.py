"""Genere les briefs des quatre escouades de domaine, et leur lanceur.

CE QU'EST UNE ESCOUADE ICI
Un agent par couche d'A'Space, qui alimente les TROIS bundles a la fois :

  50_Distillation/domaines/<couche>/       concepts OKF v0.2
  60_Implementation_Methodologiques/domaines/<couche>.md   methode
  70_Onthologies/triplets/dom-<couche>.jsonl               triplets

C'est plus economique que douze agents (4 couches x 3 destinations) : l'agent
lit sa couche une fois et en tire trois formes. Un agent qui relirait le meme
corpus pour chaque destination paierait trois fois la lecture.

Les sorties restent disjointes entre escouades : aucune ne peut ecraser une
autre.

LE CHIFFRE QUI COMMANDE LE DECOUPAGE
2 348 fichiers ecrits a la main, pas 8 888. Les trois quarts du corpus brut
sont des artefacts `graphify-burst`/`graphify-out`. Chaque brief porte le
volume REEL de sa couche, pour qu'aucun agent ne renonce a l'exhaustivite en
croyant la tache plus grosse qu'elle n'est.
"""

import io
import os
import shutil

V3 = r"C:\Users\amado\ASpace_OS_V3"
BASE = "C:/Users/amado/ASpace_OS_V3"
SRC = ("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise"
       "/03_Resources_Geordi/05_From_V2_Domains")
BRIEFS = os.path.join(V3, "50_Distillation", "_briefs_domaines")

ESCOUADES = {
    "10_Tech_OS": dict(
        cle="tech", volume=97, cible_concepts=12, cible_triplets=45,
        zones="`00_Governance_Rick` 42 · `12_Blueprints` 26 · `11_Infra_13th_Doctor` 16 · `13_Data_12th_Doctor` 6 · `12_Interface_11th_Doctor` 5",
        angle="""**97 fichiers. Tu peux tout ouvrir.** Aucune excuse de couverture ne tiendra.

`00_Governance_Rick/` porte `Loi_L0.md`, `Sobriete.md`, `VPS_AUDIT_PROTOCOL.md`,
`Drivers/`, `Rituals/`, `Scripts_Python/`, `openclaw-mission-control/`.

La these a verifier : **Rick gouverne le mecanisme qui produit les trois OS**,
pas les trois OS. Si `Loi_L0.md` dit autre chose, cite les deux.

Les trois Doctors ont chacun leur dossier : `11_Infra_13th_Doctor`,
`12_Interface_11th_Doctor`, `13_Data_12th_Doctor`. **Etablis la correspondance
Doctor -> domaine -> couche.** C'est un trou identifie : une passe precedente
n'a trouve les Docteurs que comme attributs, jamais comme entites.

Un fait deja etabli et a verifier contre les documents : dans la V3,
`13_Buzz_Core_12th/compagnons/` contient `01_Clara_MCP`, `02_Nardole_A2A`,
`03_Bill_AG-UI`. Un `cores.json` donne pourtant a Bill le numero 04. Si tu
trouves la trace de cette renumerotation, dis-la."""),

    "20_Life_OS": dict(
        cle="life", volume=159, cible_concepts=16, cible_triplets=55,
        zones="`22_Wheel_Discovery` 78 · `21_Ikigai_Orville` 24 · `23_12WY_SNW` 16 · `25_GTD_Cerritos` 13 · `26_DEAL_Protostar` 11 · `00_Gatekeepers_Beth_Morty` 7",
        angle="""**159 fichiers. Lisible en entier.**

Les cinq methodes ont chacune leur dossier, et leur nom porte le vaisseau :
`21_Ikigai_Orville`, `22_Wheel_Discovery`, `23_12WY_SNW`, `25_GTD_Cerritos`,
`26_DEAL_Protostar`. **Etablis methode -> vaisseau -> role.**

`22_Wheel_Discovery` est la zone la plus grosse (78) : commence par la.

`00_Gatekeepers_Beth_Morty` ne fait que 7 fichiers mais porte le veto — c'est
la relation d'autorite la plus structurante d'A'Space. Utilise `hasVetoOver`
et **rien d'autre** pour un droit d'arret : une passe precedente a produit
trois verbes synonymes parce que trois agents ne se voyaient pas.

`26_DEAL_Protostar` : le protocole D.E.A.L. a une regle chiffree connue —
trois occurrences pour automatiser, cinq pour rembourser. Verifie-la a la
source et cite-la."""),

    "00_Amadeus": dict(
        cle="amadeus", volume=757, cible_concepts=18, cible_triplets=55,
        zones="`05_OSS_TSTwin` 283 · `05_OSS_Twin` 277 · `01_Identity_Core` 150 · `sob` 31 · `(racine)` 14",
        angle="""**757 fichiers, mais le coeur est petit.**

`01_Identity_Core` (150 fichiers) porte `CONSTITUTION.md`, `IDENTITY.md`,
`AGENTS.md`, `AGENTS_REGISTRY.md`, `HEARTBEAT.md`, `a0_l_canon.md`,
`a0_l_geordi_canon.md`, une `AMENDMENT-001` au statut `PROPOSED`.
**Commence par la** : c'est la source la plus haute de la hierarchie du poste.

La `CONSTITUTION.md` prime sur tout en cas de conflit — c'est ecrit dans le
canon Geordi. Si un autre document la contredit, la Constitution gagne, et tu
signales l'autre comme perime.

`05_OSS_Twin` (277) et `05_OSS_TSTwin` (283) font ensemble 560 fichiers, soit
74 % de ta couche. **Etablis d'abord ce qu'ils sont** — un jumeau de code ? une
transposition TypeScript du meme jumeau ? Leur nature change entierement leur
valeur, et si ce sont des miroirs l'un de l'autre, dis-le plutot que de les
distiller deux fois.

`AMENDMENT-001_terminal-lifecycle_PROPOSED.md` : un amendement *propose*, donc
non ratifie. Ne le traite jamais comme du canon."""),

    "30_Business_OS": dict(
        cle="business", volume=1335, cible_concepts=16, cible_triplets=50,
        zones="`10_Projects` 861 · `00_Jerry_Business_Pulse` 466 · `09_Blueprints` 5 · `02_Meta_Factory` 2 · `00_Summers_Verse` 1",
        angle="""**1 335 fichiers ecrits a la main** — et c'est deja un chiffre nettoye :
le comptage brut donnait 7 212, dont 4 766 d'artefacts `graphify-burst` pour
le seul Business_Pulse. Ne te fie pas a un volume que tu n'as pas verifie.

`00_Jerry_Business_Pulse` porte `CEO_Directives.md`, `01_Vision_Strategy`,
`02_Global_Dashboard`, `03_Master_Agreements`, `04_Business_Domains`.
**`04_Business_Domains` est le coeur de la fractale B1/B2/B3** : c'est la que
se decide le nombre de domaines.

Un ecart connu et a trancher a la source : un SDD decrit **7 domaines**, le
canon a jour en compte **8** — il manquait Sales. Cite le compte le plus
recent ET l'ancien, avec leurs dates.

`10_Projects` (861) contient les chantiers clients, dont `omk/repos/coach-os`,
la premiere franchise prototype. **N'entre pas dans le code** : tu distilles la
doctrine, pas l'implementation.

`09_Blueprints` ne fait que 5 fichiers mais porte les plans — lis-les tous."""),
}

BRIEF = """# BRIEF — escouade {couche}

## Ce que tu produis : TROIS livrables, une seule lecture

Tu lis ta couche **une fois** et tu en tires trois formes. Un agent qui
relirait le corpus pour chaque destination paierait trois fois la lecture.

```
1. {base}/50_Distillation/domaines/{cle}/            concepts OKF v0.2
2. {base}/60_Implementation_Méthodologiques/domaines/{cle}.md   la methode
3. {base}/70_Onthologies/triplets/dom-{cle}.jsonl    les triplets
```

Plus ton rapport : `{briefs}/RAPPORT_{cle}.md`.

**Aucun autre fichier, nulle part.** Trois autres escouades travaillent en
parallele sur les trois autres couches.

**La V2 est en LECTURE SEULE.** Tu la distilles, tu ne la touches pas.

## Ce que tu lis

```
{base}/50_Distillation/_substrat_domaines/CARTE_{couche}.md    ta carte — commence par la
{base}/50_Distillation/_substrat_domaines/{couche}.jsonl       le substrat : plan, liens, titres
{src}/{couche}/                                                 ta couche, en entier
```

La carte te dit ou regarder **avant** d'ouvrir quoi que ce soit. Un agent qui
lit dans l'ordre alphabetique consomme son budget dans les dossiers les moins
interessants.

## Ta couche

**{volume} fichiers `.md` ecrits a la main.**

Zones : {zones}

{angle}

## Livrable 1 — les concepts OKF ({cible_concepts} minimum)

Dans `50_Distillation/domaines/{cle}/`, en `kebab-case.md`, avec le frontmatter
OKF v0.2 complet et des `sources` pointant sur des chemins reels de la V2.

Un concept est une **notion**, pas le resume d'un fichier : une entite, une
relation, une decision, un piege deja paye. S'il ne pouvait pas etre relu dans
six mois par quelqu'un sans le corpus sous les yeux, ce n'est pas un concept.

Cree aussi `index.md` dans ce dossier : une ligne par concept sous `# Files`.

## Livrable 2 — la methode (un seul fichier)

`60_Implementation_Méthodologiques/domaines/{cle}.md`, au format OKF v0.2.

Ce fichier ne repete pas les concepts. Il repond a **une** question : *qu'est-ce
que cette couche nous apprend sur la maniere de travailler ?* Rituels,
garde-fous, cadences, regles chiffrees, pieges documentes.

Une methode sans son *pourquoi* ne se generalise pas aux cas non prevus. Donne
la raison, pas seulement la regle.

## Livrable 3 — les triplets ({cible_triplets} minimum)

`70_Onthologies/triplets/dom-{cle}.jsonl`, un par ligne, JSON strict :

```json
{{"sujet":"rick","verbe":"governs","objet":"replicator","objet_type":"entite","phrase":"Rick gouverne le mecanisme qui produit les trois OS, pas les trois OS","source":"10_Tech_OS/00_Governance_Rick/Loi_L0.md","confiance":"haute"}}
```

`source` est un chemin **relatif a `05_From_V2_Domains/`** et il doit exister :
un validateur le verifie, et rejette la ligne sinon. Une source inventee est
pire qu'une source absente, parce qu'elle rassure.

Verbes a reutiliser en priorite : `governs`, `partOf`, `dependsOn`,
`appliesTo`, `refines`, `instantiates`, `pairedWith`, `handledBy`, `cites`,
`supersedes`, `stewards`, `covers`, `routes`, `hasVetoOver`, `produces`,
`escalates`, `directs`, `inherits`.

Un verbe neuf doit servir **au moins trois fois**. En dessous, ce n'est pas un
verbe, c'est une occurrence.

Atomicite : un triplet qui contient « et » est presque toujours a couper.

## Interdits

- Aucune assertion sans source verifiable.
- Aucune ecriture hors de tes quatre fichiers/dossiers.
- Ne tranche aucune contradiction : ecris les deux versions avec leurs sources
  et leurs dates.
- Aucun `git`, aucune installation, aucun agent delegue.

## Ton rapport

`{briefs}/RAPPORT_{cle}.md` :

- combien de fichiers tu as **reellement ouverts**, sur {volume} ;
- ce que tu as ecrit dans chacun des trois livrables ;
- les contradictions rencontrees, **nommees et non tranchees** ;
- ce que tu **attendais et n'as pas trouve** — c'est le plus utile pour la
  suite.
"""

LANCE = """#!/usr/bin/env bash
# Lance une escouade de domaine sur M3.
#   Usage : ./lance-domaines.sh tech|life|amadeus|business

set -u
QUOI="${1:?usage: lance-domaines.sh tech|life|amadeus|business}"

V3="C:/Users/amado/ASpace_OS_V3"
BRIEFS="$V3/50_Distillation/_briefs_domaines"

case "$QUOI" in tech|life|amadeus|business) ;;
  *) echo "inconnu : $QUOI" >&2; exit 2 ;; esac

case "$QUOI" in
  tech)     COUCHE="10_Tech_OS" ;;
  life)     COUCHE="20_Life_OS" ;;
  amadeus)  COUCHE="00_Amadeus" ;;
  business) COUCHE="30_Business_OS" ;;
esac

GARDE="$BRIEFS/GARDE_FOU.md"
BRIEF="$BRIEFS/BRIEF_${QUOI}.md"
LOG="$BRIEFS/journal_${QUOI}.log"

for f in "$GARDE" "$BRIEF"; do
  [ -f "$f" ] || { echo "manquant : $f" >&2; exit 3; }
done

# La carte est la matiere premiere : sans elle l'agent lit dans l'ordre
# alphabetique et gaspille son budget.
CARTE="$V3/50_Distillation/_substrat_domaines/CARTE_${COUCHE}.md"
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
echo "escouade $QUOI terminee, exit=$CODE, journal=$LOG"
exit $CODE
"""


def main():
    os.makedirs(BRIEFS, exist_ok=True)
    for sd in ("50_Distillation/domaines",
               "60_Implementation_Méthodologiques/domaines",
               "70_Onthologies/triplets"):
        os.makedirs(os.path.join(V3, sd), exist_ok=True)

    shutil.copy(os.path.join(V3, "50_Distillation", "_briefs", "GARDE_FOU.md"),
                os.path.join(BRIEFS, "GARDE_FOU.md"))

    for couche, d in ESCOUADES.items():
        os.makedirs(os.path.join(V3, "50_Distillation", "domaines", d["cle"]), exist_ok=True)
        champs = {k: v for k, v in d.items() if k != "cle"}
        txt = BRIEF.format(couche=couche, cle=d["cle"], base=BASE, src=SRC,
                           briefs=BRIEFS.replace("\\", "/"), **champs)
        io.open(os.path.join(BRIEFS, f"BRIEF_{d['cle']}.md"), "w", encoding="utf-8").write(txt)
        print(f"BRIEF_{d['cle']}.md  {len(txt)} octets  {d['volume']} fichiers  "
              f"cibles {d['cible_concepts']} concepts / {d['cible_triplets']} triplets")

    io.open(os.path.join(BRIEFS, "lance-domaines.sh"), "w", encoding="utf-8", newline="\n").write(LANCE)
    print("lance-domaines.sh pose")


if __name__ == "__main__":
    main()
