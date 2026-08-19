# BRIEF — vague 2 : les ADR

## Ce que tu produis : TROIS livrables, une seule lecture

```
1. C:/Users/amado/ASpace_OS_V3/50_Distillation/domaines/normatif-adr/          concepts OKF v0.2
2. C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/domaines/normatif-adr.md   la methode
3. C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/dom-normatif-adr.jsonl  les triplets
```

Plus ton rapport : `C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/RAPPORT_normatif-adr.md`.

**Aucun autre fichier.** Trois autres escouades travaillent en parallele.
**La V2 est en LECTURE SEULE.**

## Ton corpus

**259 ADR distincts, 81 familles**

Ou : `04_From_V2_Root/_SPECS/ADR/`, `05_From_V2_Domains/**/ADR/`, et partout ou un fichier commence par `ADR-`

Les familles les plus fournies :

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
pas un concept — il merite une ligne dans ton rapport.

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

`triplets/dom-normatif-adr.jsonl`, un triplet par ligne, JSON strict :

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

- **16 concepts OKF** minimum dans `50_Distillation/domaines/normatif-adr/`, avec `index.md`
- **1 fichier methode** dans `60_Implementation_Méthodologiques/domaines/normatif-adr.md`
- **50 triplets** minimum

## Interdits

- Aucune assertion sans source verifiable.
- Aucun verdict `superseded` sans successeur nomme.
- Ne tranche aucune contradiction : ecris les deux versions avec leurs dates.
- Aucune ecriture dans la V2. Aucun `git`, aucune installation.

## Ton rapport

`C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/RAPPORT_normatif-adr.md` : combien de documents examines sur combien, la
repartition des quatre verdicts, les collisions de numerotation ou de nom
trouvees, et ce que tu attendais sans le trouver.
