# BRIEF — ontologie V3 : 30_Business_OS — l'action

## Ce que tu produis

Des **triplets sujet-verbe-objet** sur A'Space OS, lus dans l'arborescence
**V3** et dans ses fichiers. Pas un resume : des assertions atomiques,
chacune sourcee par un chemin reel.

## Ton perimetre EXCLUSIF en ecriture

```
C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl
C:/Users/amado/ASpace_OS_V3/70_Onthologies/_briefs/RAPPORT_v3-business.md
```

**Deux fichiers.** Trois autres agents travaillent sur les trois autres
couches. Tu ne touches a rien d'autre — ni aux `.ttl`, qui sont generes, ni
aux triplets d'une autre couche.

**`ASpace_OS_V3/` est en lecture seule.** Tu l'ontologises, tu ne le modifies
pas.

## Ce que tu lis

```
C:/Users/amado/ASpace_OS_V3/70_Onthologies/_structure/CARTE_V3.md               la carte complete — 48 Ko, lisible d'un trait
C:/Users/amado/ASpace_OS_V3/70_Onthologies/_structure/structure_mesure.json     les 73 fichiers porteurs d'un code de rang
C:/Users/amado/ASpace_OS_V3/30_Business_OS/                    TA couche, en entier
```

**Commence par la carte.** Elle donne toute l'arborescence, avec les codes de
rang deja reperes. Ouvre ensuite les fichiers de ta couche.

## Ce qui est DEJA fait, et que tu ne refais pas

L'imbrication (`partOf`) et les codes de rang (`hasRank`, `operatesLayer`) ont
ete extraits mecaniquement : **6 091 triplets structurels** sont deja poses.

Ne les reproduis pas. Tu poses ce que la structure **ne peut pas dire** : ce
que chaque acteur fait, sur quoi il a autorite, ce qu'il produit, ce qu'il
interdit, dans quel ordre les choses s'enchainent.

## Ta couche

**Racine** : `30_Business_OS/` — 2 988 fichiers, mais l'immense majorite sont des captures .png

**Attention au compte.** Sur 2 988 fichiers, la plupart sont des `.png` de
captures d'ecran. Le corpus porteur de structure est bien plus petit : va voir
la carte plutot que de te fier au volume.

C'est la couche la moins bien couverte par la structure : peu de codes de rang
dans les noms (`B1` 3, `B2` 1, `B3` 3). Deux lectures possibles, et tu dois
trancher : soit la fractale B1/B2/B3 n'est pas encore posee dans la V3, soit
elle l'est ailleurs qu'en nom de fichier.

`09_Blueprints/` porte les plans. Si Coach OS y figure comme premiere franchise
prototype, dis-le avec sa source.

## La difference avec la passe V2

La V2 comptait 63 260 fichiers : les agents travaillaient sur un echantillon
declare, et c'etait honnete de le dire.

**Ici le corpus tient.** Ta couche est lisible en entier. Si ta couverture est
partielle, la cause ne sera pas la taille — dis laquelle.

## Le format de sortie

`triplets/v3-business.jsonl` — un triplet par ligne, JSON strict :

```json
{"sujet":"beth","verbe":"hasRank","objet":"a1","objet_type":"entite","phrase":"Beth est une persona de rang A1, gardienne avec Morty","source":"20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md","confiance":"haute"}
```

| champ | regle |
|---|---|
| `sujet` | cle en `kebab-case` |
| `verbe` | voir ci-dessous |
| `objet` | une entite, ou un litteral si `objet_type` vaut `litteral` |
| `source` | **obligatoire** — chemin relatif a `ASpace_OS_V3/`, qui doit exister |
| `confiance` | `haute` si un fichier l'ecrit ; `moyenne` si tu deduis |

Verbes du schema, a reutiliser en priorite : `governs`, `partOf`, `dependsOn`,
`appliesTo`, `refines`, `instantiates`, `pairedWith`, `handledBy`, `cites`,
`supersedes`, `seeAlso`, `stewards`, `covers`, `routes`, `hasVetoOver`,
`produces`, `escalates`, `directs`, `inherits`.

Un verbe neuf doit servir **au moins trois fois**. En dessous, ce n'est pas un
verbe, c'est une occurrence.

**Un mot sur le veto** : la passe precedente a produit trois verbes pour la
meme notion (`hasVetoOver`, `vetoes`, `halts`) parce que trois agents ne se
voyaient pas. **Utilise `hasVetoOver`** et rien d'autre pour un droit d'arret.

## Ce qu'on attend

**35 triplets au minimum**, tous sources.

Atomicite : un triplet qui contient « et » est presque toujours a couper.
Utilite : si un triplet ne changerait la reponse a aucune question, ne
l'ecris pas.

## Interdits

- Aucune assertion sans source verifiable dans la V3.
- Aucune modification de quoi que ce soit hors de tes deux fichiers.
- Ne tranche aucune contradiction : ecris les deux versions avec leurs sources.
- Aucun `git`, aucune installation.

## Ton rapport

`_briefs/RAPPORT_v3-business.md` : combien de triplets, combien de fichiers de ta
couche tu as **reellement ouverts** sur combien, les verbes neufs proposes, les
contradictions, et **les ecarts entre ce que la structure dit et ce que les
documents disent** — c'est ce qui a le plus de valeur.
