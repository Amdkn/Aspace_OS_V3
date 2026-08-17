# BRIEF — la hierarchie des entites d'A'Space

## Ce qui existe deja, et ce qui manque

La couche ENTITES vient d'etre posee : 21 acteurs d'A'Space sont desormais des
sujets du graphe, avec leurs alias et les concepts qui les mentionnent.

```
 84  Life OS      41  B2        38  A0/Amadeus   33  B3
 31  Summer       30  A3        30  Jerry        29  B1
 27  Picard       26  Geordi    23  A1  A2  Beth 20  Business OS
 19  Rick  Spock  16  Data      15  Morty         8  Tech OS
  6  Les Docteurs  1  Les Compagnons
```

Ce comptage dit **qui existe et ou on en parle**. Il ne dit **rien de la
hierarchie** : qui gouverne qui, quelle couche opere quelle autre, qui a un
droit de veto sur qui. Cela se lit dans le canon, pas dans un comptage
d'occurrences. C'est ton travail.

## Ton perimetre EXCLUSIF en ecriture

```
C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/hierarchie.jsonl
C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/RAPPORT_hierarchie.md
```

**Deux fichiers.** Tu ne modifies aucun `.ttl` — ils sont generes. Tu ne
modifies aucun concept.

## Ce que tu lis, dans cet ordre

```
1. C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/META_ONTOLOGIE.md
   Le rapport de reconstitution des trois couches. Il porte deja des tableaux
   d'entites SOURCES — c'est ta matiere premiere.

2. C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/meta_ontologie.json
   La version structuree du meme travail.

3. ontologie/aspace-entites.ttl     les 21 entites et leurs alias
4. ontologie/CATALOGUE.md           les 102 concepts, pour retrouver une source
5. ontologie/aspace-schema.ttl      les 11 predicats disponibles
```

**META_ONTOLOGIE.md est une source, pas une verite.** Il porte lui-meme cet
avertissement : *« Aucun SDD n'est source de verite. V3 et le code priment. Une
entree sans source est une invention. »* Il documente aussi un cas ou le code
etait en avance sur le document pris pour reference. Traite-le comme un temoin
serieux et faillible.

## Le format de sortie

`hierarchie.jsonl` — une relation par ligne, meme forme que `relations.jsonl` :

```json
{"de":"rick","vers":"tech-os","predicat":"governs","pourquoi":"LAW.md : Rick ne gouverne pas les trois OS, il gouverne le mecanisme qui les produit","source":"META_ONTOLOGIE.md §1","confiance":"haute"}
```

| champ | regle |
|---|---|
| `de`, `vers` | la **cle courte** de l'entite : `a0-amadeus`, `a1`, `a2`, `a3`, `rick`, `docteur`, `compagnons`, `b1`, `b2`, `b3`, `business-os`, `life-os`, `tech-os`, `beth`, `morty`, `jerry`, `summer`, `picard`, `spock`, `data`, `geordi` |
| `predicat` | l'un des 11 : `governs`, `partOf`, `dependsOn`, `appliesTo`, `refines`, `instantiates`, `pairedWith`, `handledBy`, `cites`, `seeAlso`, `supersedes` |
| `pourquoi` | une phrase, lisible par quelqu'un qui n'a pas ton contexte |
| `source` | **obligatoire** — le fichier et la section d'ou vient l'affirmation |
| `confiance` | `haute` si une source l'ecrit noir sur blanc ; `moyenne` si tu deduis |

**Une relation sans `source` sera rejetee.** C'est la regle du poste : une
entree sans source est une invention.

## Les questions auxquelles la hierarchie doit repondre

1. **Les trois OS et leur mecanisme.** Rick gouverne-t-il les trois OS, ou le
   mecanisme qui les produit ? La distinction est explicite dans le canon et
   elle est structurante.
2. **Les Cores et les Docteurs.** Trois Cores issus du meme gabarit, chacun
   operant une couche. Etablis la correspondance Docteur -> Core -> OS.
3. **A0, A1, A2, A3.** Que designent ces codes — des couches, des rangs
   d'agents, des deux ? A0 est nomme « orchestrateur » ; qui orchestre-t-il ?
4. **B1, B2, B3.** Meme question cote Business OS.
5. **Le veto.** Le canon mentionne un droit d'arret de Life OS sur Business OS
   (un HALT qui gele l'acceleration). Modelise-le : c'est une relation
   d'autorite, pas une simple dependance.
6. **Les gardiens PARA.** Picard, Spock, Geordi, Data tiennent chacun un seau.
   Relie-les aux seaux et aux couches.
7. **Beth, Morty, Jerry, Summer.** Quels roles, dans quelle couche.

## Une tension a ne pas lisser

`META_ONTOLOGIE.md` la nomme deja : le canon pose une **pyramide stricte**
(L0 >= L1 > L2 en autorite), mais l'utilisateur dit que **L2 est unifie dans
L1**. Les deux lignes cohabitent dans les sources.

**Ne tranche pas.** Ecris les deux, chacune avec sa source, et signale la
contradiction dans ton rapport. L'arbitrage appartient au proprietaire du
produit.

## Trois entites sont maigres — dis pourquoi

`Les Compagnons` n'apparait que dans **1** concept, `Les Docteurs` dans **6**,
`Tech OS` dans **8** — alors que `Life OS` est dans 84.

Deux explications possibles, et il faut trancher : soit ces notions sont
marginales dans A'Space, soit **la distillation les a ratees** parce qu'aucun
des quatre seaux PARA ne les portait. Regarde `META_ONTOLOGIE.md` : s'il en
parle abondamment alors que le graphe les ignore, c'est un trou de couverture,
et c'est une information plus utile que la hierarchie elle-meme.

## Ce qu'on attend

- **au moins 25 relations** dans `hierarchie.jsonl`, toutes sourcees ;
- **trois concepts OKF v0.2** dans ton rapport... non : le rapport suffit. Ne
  cree aucun fichier hors des deux nommes.

## Ton rapport

`_briefs/RAPPORT_hierarchie.md` : combien de relations, lesquelles sont
`moyenne` et pourquoi, la ou les contradictions rencontrees, et le verdict sur
les trois entites maigres.
