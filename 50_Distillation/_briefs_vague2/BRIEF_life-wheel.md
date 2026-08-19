# BRIEF — vague 2 : la Life Wheel — huit domaines LD01 a LD08

## Ce que tu produis : TROIS livrables, une seule lecture

```
1. C:/Users/amado/ASpace_OS_V3/50_Distillation/domaines/life-wheel/          concepts OKF v0.2
2. C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/domaines/life-wheel.md   la methode
3. C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/dom-life-wheel.jsonl  les triplets
```

Plus ton rapport : `C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/RAPPORT_life-wheel.md`.

**Aucun autre fichier.** Trois autres escouades travaillent en parallele.
**La V2 est en LECTURE SEULE.**

## Ton corpus

**297 fichiers**

Ou : `09_Life_OS/`

Huit domaines, chacun avec sa persona Discovery, et la structure les nomme :

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

Signale tout LD rattache a aucun Jerry, ou a deux.

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

`triplets/dom-life-wheel.jsonl`, un triplet par ligne, JSON strict :

```json
{"sujet":"sdd-006","verbe":"supersedes","objet":"sdd-005","objet_type":"entite","phrase":"SDD-006 remplace SDD-005 sur le decompte des domaines","source":"...chemin reel...","confiance":"haute"}
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

- **16 concepts OKF** minimum dans `50_Distillation/domaines/life-wheel/`, avec `index.md`
- **1 fichier methode** dans `60_Implementation_Méthodologiques/domaines/life-wheel.md`
- **55 triplets** minimum

## Interdits

- Aucune assertion sans source verifiable.
- Aucun verdict `superseded` sans successeur nomme.
- Ne tranche aucune contradiction : ecris les deux versions avec leurs dates.
- Aucune ecriture dans la V2. Aucun `git`, aucune installation.

## Ton rapport

`C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/RAPPORT_life-wheel.md` : combien de documents examines sur combien, la
repartition des quatre verdicts, les collisions de numerotation ou de nom
trouvees, et ce que tu attendais sans le trouver.
