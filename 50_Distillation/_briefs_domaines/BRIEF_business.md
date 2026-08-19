# BRIEF — escouade 30_Business_OS

## Ce que tu produis : TROIS livrables, une seule lecture

Tu lis ta couche **une fois** et tu en tires trois formes. Un agent qui
relirait le corpus pour chaque destination paierait trois fois la lecture.

```
1. C:/Users/amado/ASpace_OS_V3/50_Distillation/domaines/business/            concepts OKF v0.2
2. C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/domaines/business.md   la methode
3. C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/dom-business.jsonl    les triplets
```

Plus ton rapport : `C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_domaines/RAPPORT_business.md`.

**Aucun autre fichier, nulle part.** Trois autres escouades travaillent en
parallele sur les trois autres couches.

**La V2 est en LECTURE SEULE.** Tu la distilles, tu ne la touches pas.

## Ce que tu lis

```
C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat_domaines/CARTE_30_Business_OS.md    ta carte — commence par la
C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat_domaines/30_Business_OS.jsonl       le substrat : plan, liens, titres
C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/                                                 ta couche, en entier
```

La carte te dit ou regarder **avant** d'ouvrir quoi que ce soit. Un agent qui
lit dans l'ordre alphabetique consomme son budget dans les dossiers les moins
interessants.

## Ta couche

**1335 fichiers `.md` ecrits a la main.**

Zones : `10_Projects` 861 · `00_Jerry_Business_Pulse` 466 · `09_Blueprints` 5 · `02_Meta_Factory` 2 · `00_Summers_Verse` 1

**1 335 fichiers ecrits a la main** — et c'est deja un chiffre nettoye :
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

`09_Blueprints` ne fait que 5 fichiers mais porte les plans — lis-les tous.

## Livrable 1 — les concepts OKF (16 minimum)

Dans `50_Distillation/domaines/business/`, en `kebab-case.md`, avec le frontmatter
OKF v0.2 complet et des `sources` pointant sur des chemins reels de la V2.

Un concept est une **notion**, pas le resume d'un fichier : une entite, une
relation, une decision, un piege deja paye. S'il ne pouvait pas etre relu dans
six mois par quelqu'un sans le corpus sous les yeux, ce n'est pas un concept.

Cree aussi `index.md` dans ce dossier : une ligne par concept sous `# Files`.

## Livrable 2 — la methode (un seul fichier)

`60_Implementation_Méthodologiques/domaines/business.md`, au format OKF v0.2.

Ce fichier ne repete pas les concepts. Il repond a **une** question : *qu'est-ce
que cette couche nous apprend sur la maniere de travailler ?* Rituels,
garde-fous, cadences, regles chiffrees, pieges documentes.

Une methode sans son *pourquoi* ne se generalise pas aux cas non prevus. Donne
la raison, pas seulement la regle.

## Livrable 3 — les triplets (50 minimum)

`70_Onthologies/triplets/dom-business.jsonl`, un par ligne, JSON strict :

```json
{"sujet":"rick","verbe":"governs","objet":"replicator","objet_type":"entite","phrase":"Rick gouverne le mecanisme qui produit les trois OS, pas les trois OS","source":"10_Tech_OS/00_Governance_Rick/Loi_L0.md","confiance":"haute"}
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

`C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_domaines/RAPPORT_business.md` :

- combien de fichiers tu as **reellement ouverts**, sur 1335 ;
- ce que tu as ecrit dans chacun des trois livrables ;
- les contradictions rencontrees, **nommees et non tranchees** ;
- ce que tu **attendais et n'as pas trouve** — c'est le plus utile pour la
  suite.
