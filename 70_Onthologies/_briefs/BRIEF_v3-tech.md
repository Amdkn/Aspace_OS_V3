# BRIEF — ontologie V3 : 10_Tech_OS — le mecanisme

## Ce que tu produis

Des **triplets sujet-verbe-objet** sur A'Space OS, lus dans l'arborescence
**V3** et dans ses fichiers. Pas un resume : des assertions atomiques,
chacune sourcee par un chemin reel.

## Ton perimetre EXCLUSIF en ecriture

```
C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-tech.jsonl
C:/Users/amado/ASpace_OS_V3/70_Onthologies/_briefs/RAPPORT_v3-tech.md
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
C:/Users/amado/ASpace_OS_V3/10_Tech_OS/                    TA couche, en entier
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

**Racine** : `10_Tech_OS/` — 97 fichiers — la couche la plus petite, donc la plus lisible entierement

97 fichiers : **tu peux tout ouvrir**. Aucune excuse de couverture ici.

Cherche `00_Governance_Rick/` (LAW.md, SOUL.md, le replicator, `cores.json`,
`spawn.py`) et `11_Kernel_Core_13th/` avec ses compagnons.

La these a verifier contre la structure : Rick gouverne **le mecanisme qui
produit les trois OS**, pas les trois OS. Si l'arborescence dit autre chose que
les documents, **dis-le** — c'est exactement le genre d'ecart qui compte.

`cores.json` et `spawn.py` sont des artefacts executables : ils disent ce qui
se passe vraiment, pas ce qu'on a voulu. Un fichier de configuration prime sur
une prose qui le decrit.

## La difference avec la passe V2

La V2 comptait 63 260 fichiers : les agents travaillaient sur un echantillon
declare, et c'etait honnete de le dire.

**Ici le corpus tient.** Ta couche est lisible en entier. Si ta couverture est
partielle, la cause ne sera pas la taille — dis laquelle.

## Le format de sortie

`triplets/v3-tech.jsonl` — un triplet par ligne, JSON strict :

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

**40 triplets au minimum**, tous sources.

Atomicite : un triplet qui contient « et » est presque toujours a couper.
Utilite : si un triplet ne changerait la reponse a aucune question, ne
l'ecris pas.

## Interdits

- Aucune assertion sans source verifiable dans la V3.
- Aucune modification de quoi que ce soit hors de tes deux fichiers.
- Ne tranche aucune contradiction : ecris les deux versions avec leurs sources.
- Aucun `git`, aucune installation.

## Ton rapport

`_briefs/RAPPORT_v3-tech.md` : combien de triplets, combien de fichiers de ta
couche tu as **reellement ouverts** sur combien, les verbes neufs proposes, les
contradictions, et **les ecarts entre ce que la structure dit et ce que les
documents disent** — c'est ce qui a le plus de valeur.
