# BRIEF — escouade 20_Life_OS

## Ce que tu produis : TROIS livrables, une seule lecture

Tu lis ta couche **une fois** et tu en tires trois formes. Un agent qui
relirait le corpus pour chaque destination paierait trois fois la lecture.

```
1. C:/Users/amado/ASpace_OS_V3/50_Distillation/domaines/life/            concepts OKF v0.2
2. C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/domaines/life.md   la methode
3. C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/dom-life.jsonl    les triplets
```

Plus ton rapport : `C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_domaines/RAPPORT_life.md`.

**Aucun autre fichier, nulle part.** Trois autres escouades travaillent en
parallele sur les trois autres couches.

**La V2 est en LECTURE SEULE.** Tu la distilles, tu ne la touches pas.

## Ce que tu lis

```
C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat_domaines/CARTE_20_Life_OS.md    ta carte — commence par la
C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat_domaines/20_Life_OS.jsonl       le substrat : plan, liens, titres
C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/                                                 ta couche, en entier
```

La carte te dit ou regarder **avant** d'ouvrir quoi que ce soit. Un agent qui
lit dans l'ordre alphabetique consomme son budget dans les dossiers les moins
interessants.

## Ta couche

**159 fichiers `.md` ecrits a la main.**

Zones : `22_Wheel_Discovery` 78 · `21_Ikigai_Orville` 24 · `23_12WY_SNW` 16 · `25_GTD_Cerritos` 13 · `26_DEAL_Protostar` 11 · `00_Gatekeepers_Beth_Morty` 7

**159 fichiers. Lisible en entier.**

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
source et cite-la.

## Livrable 1 — les concepts OKF (16 minimum)

Dans `50_Distillation/domaines/life/`, en `kebab-case.md`, avec le frontmatter
OKF v0.2 complet et des `sources` pointant sur des chemins reels de la V2.

Un concept est une **notion**, pas le resume d'un fichier : une entite, une
relation, une decision, un piege deja paye. S'il ne pouvait pas etre relu dans
six mois par quelqu'un sans le corpus sous les yeux, ce n'est pas un concept.

Cree aussi `index.md` dans ce dossier : une ligne par concept sous `# Files`.

## Livrable 2 — la methode (un seul fichier)

`60_Implementation_Méthodologiques/domaines/life.md`, au format OKF v0.2.

Ce fichier ne repete pas les concepts. Il repond a **une** question : *qu'est-ce
que cette couche nous apprend sur la maniere de travailler ?* Rituels,
garde-fous, cadences, regles chiffrees, pieges documentes.

Une methode sans son *pourquoi* ne se generalise pas aux cas non prevus. Donne
la raison, pas seulement la regle.

## Livrable 3 — les triplets (55 minimum)

`70_Onthologies/triplets/dom-life.jsonl`, un par ligne, JSON strict :

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

`C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_domaines/RAPPORT_life.md` :

- combien de fichiers tu as **reellement ouverts**, sur 159 ;
- ce que tu as ecrit dans chacun des trois livrables ;
- les contradictions rencontrees, **nommees et non tranchees** ;
- ce que tu **attendais et n'as pas trouve** — c'est le plus utile pour la
  suite.
