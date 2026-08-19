# BRIEF — vague 2 : les Templates — neuf kits

## Ce que tu produis : TROIS livrables, une seule lecture

```
1. C:/Users/amado/ASpace_OS_V3/50_Distillation/domaines/templates/          concepts OKF v0.2
2. C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/domaines/templates.md   la methode
3. C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/dom-templates.jsonl  les triplets
```

Plus ton rapport : `C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/RAPPORT_templates.md`.

**Aucun autre fichier.** Trois autres escouades travaillent en parallele.
**La V2 est en LECTURE SEULE.**

## Ton corpus

**136 fichiers**

Ou : `02_Templates/`

Neuf kits, tres inegaux :

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
c'est un index vers autre chose. Tranche.

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

`triplets/dom-templates.jsonl`, un triplet par ligne, JSON strict :

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

- **12 concepts OKF** minimum dans `50_Distillation/domaines/templates/`, avec `index.md`
- **1 fichier methode** dans `60_Implementation_Méthodologiques/domaines/templates.md`
- **35 triplets** minimum

## Interdits

- Aucune assertion sans source verifiable.
- Aucun verdict `superseded` sans successeur nomme.
- Ne tranche aucune contradiction : ecris les deux versions avec leurs dates.
- Aucune ecriture dans la V2. Aucun `git`, aucune installation.

## Ton rapport

`C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/RAPPORT_templates.md` : combien de documents examines sur combien, la
repartition des quatre verdicts, les collisions de numerotation ou de nom
trouvees, et ce que tu attendais sans le trouver.
