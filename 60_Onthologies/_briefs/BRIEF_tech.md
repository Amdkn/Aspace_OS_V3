# BRIEF — reconstituer Tech OS — le mecanisme qui produit les trois OS

## Ce que tu produis

Des **triplets sujet-verbe-objet** sur A'Space OS lui-meme, lus dans la
distillation. Pas un resume, pas une synthese : des assertions atomiques,
chacune sourcee.

## Ton perimetre EXCLUSIF en ecriture

```
C:/Users/amado/ASpace_OS_V3/60_Onthologies/triplets/tech.jsonl
C:/Users/amado/ASpace_OS_V3/60_Onthologies/_briefs/RAPPORT_tech.md
```

**Deux fichiers.** Deux autres agents travaillent en parallele sur les deux
autres couches. Tu ne touches a rien d'autre — ni aux concepts distilles, ni
aux `.ttl`, qui sont generes.

## Ce que tu lis

```
C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/CATALOGUE.md        les 102 concepts distilles : titre, description, tags
C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/aspace-entites.ttl  les 21 entites deja identifiees et leurs alias
C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/aspace-schema.ttl   les predicats deja definis
C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/  C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/  C:/Users/amado/ASpace_OS_V3/50_Distillation/archives/  C:/Users/amado/ASpace_OS_V3/50_Distillation/ressources/
                                     les concepts eux-memes, quand le catalogue ne suffit pas
```

**Commence par le CATALOGUE**, puis ouvre les concepts qui portent ta couche.
Il fait 42 Ko et se lit d'un trait ; il te dit lesquels ouvrir.

## Ta couche

**Entites principales** : `rick`, `tech-os`, `docteur`, `compagnons`, `a0-amadeus`

Rick gouverne **le mecanisme qui produit les trois OS**, pas les trois OS.
Cette distinction est la these centrale de la couche ; toute assertion qui
l'ignore est fausse.

Cherche : le replicator et ses trois Cores issus du meme gabarit, le noyau et
ses organes, les roles (Spec / Build / Spawn / Review) et la regle que nul ne
cumule Build et Review, le watchdog et ses seuils, les cadences.

`Les Compagnons` n'apparait que dans 1 concept distille et `Les Docteurs` dans
6. Si tu ne trouves pas de quoi les decrire, **dis-le** plutot que d'inventer :
c'est un trou de couverture de la distillation, et c'est une information.

## Le format de sortie

`triplets/tech.jsonl` — un triplet par ligne, JSON strict :

```json
{"sujet":"rick","verbe":"governs","objet":"replicator","objet_type":"entite","phrase":"Rick gouverne le replicator, pas les trois OS qu'il produit","source":"ressources/adr-immutability-ricks-law.md","confiance":"haute"}
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

**45 triplets au minimum**, tous sources.

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

`_briefs/RAPPORT_tech.md` : combien de triplets, quels verbes neufs tu
proposes et pourquoi, quelles contradictions tu as rencontrees, et **ce que la
distillation ne portait pas** alors que tu l'attendais — c'est le plus utile
pour la suite.
