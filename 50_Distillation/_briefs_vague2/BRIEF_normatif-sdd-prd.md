# BRIEF — vague 2 : les SDD et les PRD

## Ce que tu produis : TROIS livrables, une seule lecture

```
1. C:/Users/amado/ASpace_OS_V3/50_Distillation/domaines/normatif-sdd-prd/          concepts OKF v0.2
2. C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/domaines/normatif-sdd-prd.md   la methode
3. C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/dom-normatif-sdd-prd.jsonl  les triplets
```

Plus ton rapport : `C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/RAPPORT_normatif-sdd-prd.md`.

**Aucun autre fichier.** Trois autres escouades travaillent en parallele.
**La V2 est en LECTURE SEULE.**

## Ton corpus

**33 SDD + 53 PRD = 86 documents distincts**

Ou : `05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/`, `04_From_V2_Root/_SPECS/`, et partout ou un fichier commence par `SDD-` ou `PRD-`

Les familles visibles : `SDD-V0.2_Micro`, `SDD-V0.3_EngineRoom`,
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
numero sert de reference, chaque collision rend une citation ambigue.

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

`triplets/dom-normatif-sdd-prd.jsonl`, un triplet par ligne, JSON strict :

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

- **14 concepts OKF** minimum dans `50_Distillation/domaines/normatif-sdd-prd/`, avec `index.md`
- **1 fichier methode** dans `60_Implementation_Méthodologiques/domaines/normatif-sdd-prd.md`
- **45 triplets** minimum

## Interdits

- Aucune assertion sans source verifiable.
- Aucun verdict `superseded` sans successeur nomme.
- Ne tranche aucune contradiction : ecris les deux versions avec leurs dates.
- Aucune ecriture dans la V2. Aucun `git`, aucune installation.

## Ton rapport

`C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/RAPPORT_normatif-sdd-prd.md` : combien de documents examines sur combien, la
repartition des quatre verdicts, les collisions de numerotation ou de nom
trouvees, et ce que tu attendais sans le trouver.
