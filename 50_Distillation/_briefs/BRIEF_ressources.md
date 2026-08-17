# BRIEF — distiller 03_Resources_Geordi vers des concepts OKF v0.2

## Ton perimetre EXCLUSIF en ecriture

```
C:/Users/amado/ASpace_OS_V3/50_Distillation/ressources/                      (tes concepts, et son index.md)
C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/RAPPORT_ressources.md    (ton rapport)
```

**Aucun autre fichier, nulle part.** Trois autres agents travaillent en
parallele sur les trois autres seaux. `C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/` ne t'appartient pas.

Sans ce cloisonnement, deux agents se reecrivent sans que ni l'un ni l'autre ne
le voie — c'est arrive, et le cout n'a ete decouvert qu'a la fin.

## Ce que tu peux lire

```
C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/                     (LECTURE SEULE — c'est le corpus)
C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat/03_Resources_Geordi.jsonl    (l'extraction — commence par la)
C:/Users/amado/ASpace_OS_V3/50_Distillation/index.md                  (la methode)
```

## Commence par le substrat, pas par les fichiers

`_substrat/03_Resources_Geordi.jsonl` contient **une ligne par fichier .md du seau** :
frontmatter, titre, plan, liens, tags, date de modification, nombre de mots. Il
a ete produit par script sur 100 % du corpus.

C'est ta carte. Elle te dit ou regarder avant d'ouvrir quoi que ce soit. Un
agent qui lit les fichiers dans l'ordre alphabetique aura consomme son budget
dans les dossiers les moins interessants.

Exploitation suggeree, avec `python` :

- grouper par premier segment du chemin, pour voir la structure reelle ;
- compter les `fm_cles`, pour reperer les familles de documents ;
- extraire les `wikilinks` les plus cites : ce sont **les noeuds du graphe** ;
- croiser fort `nb_titres` et fort `mots` : ce sont les documents structurants ;
- trier par `modifie` : le recent est plus proche du canon actuel que l'ancien.

## Etat du seau, mesure le 2026-08-17

- **48378 fichiers `.md`**, hors `node_modules`, `.git` et `dist`
- zones : `01_Guides` (15 560) - `04_From_V2_Root` (14 632) - `05_From_V2_Domains` (8 888) - `06_Claude_Code_Bare` (5 460) - `03_Memory_Unified` (1 774) - `graphify-out` (1 195) - `09_Life_OS` (297) - `08_Workspaces_Dormants_2026-08-01` (268)

**76 % du corpus distillable est ici** : 48 378 fichiers sur 63 260. C'est le
seau ou la distillation compte le plus, et ou l'exhaustivite est la moins
atteignable. Ne pretends jamais l'avoir couvert.

Les quatre piliers de la base de connaissance sont **OKF** (le format), **Wiki**
(les concepts), **Graphify** (le graphe) et **Dox** (le contrat). Ils vivent
dans `03_Memory_Unified/`. **Commence par la** : 1 774 fichiers, et c'est le
coeur methodologique — ce que tu y comprends structure la lecture de tout le
reste.

`05_From_V2_Domains/` est l'endroit ou l'utilisateur a deplace **tout ce qui
sortait du PARA**. Il contient donc `00_Amadeus`, `10_Tech_OS`, `20_Life_OS` et
`30_Business_OS` : les trois couches d'A'Space plus l'identite. C'est la matiere
ontologique la plus directe de tout le corpus. Deuxieme priorite apres
`03_Memory_Unified`.

`04_From_V2_Root` (14 632) est un deversoir de racine. Attends-toi a du bruit et
a des doublons. Ta valeur ajoutee y est de dire **ce qui merite d'etre garde**,
pas de tout decrire.

**Tu ne peux pas lire 48 378 fichiers.** Travaille par zone, declare pour chaque
zone combien tu as lu sur combien, et laisse une carte de ce qui reste.

## Ce qu'on attend

**20 concepts OKF v0.2 au minimum**, dans `C:/Users/amado/ASpace_OS_V3/50_Distillation/ressources/`, nommes en
`kebab-case.md`, chacun avec son frontmatter complet et des `sources` qui
pointent sur des chemins reels.

Un concept n'est pas le resume d'un fichier. C'est une **notion** : une entite,
une relation, une decision, un piege deja paye. Si ton concept ne pouvait pas
etre relu dans six mois par quelqu'un qui n'a pas le corpus sous les yeux, ce
n'est pas un concept.

Vise en priorite ce qui alimente un **graphe RDF** : des entites nommees, des
relations typees entre elles, et les proprietes qui les qualifient. Pense en
triplets sujet-predicat-objet meme quand tu ecris en prose.

Mets a jour `C:/Users/amado/ASpace_OS_V3/50_Distillation/ressources/index.md` : une ligne par concept, sous `# Files`.

## Ton rapport

`C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/RAPPORT_ressources.md`. Le garde-fou dit ce qu'il doit contenir.
Le chiffre le plus important est **combien tu as lu, sur combien de disponibles**.
