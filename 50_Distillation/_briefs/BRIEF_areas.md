# BRIEF — distiller 02_Areas_Spock vers des concepts OKF v0.2

## Ton perimetre EXCLUSIF en ecriture

```
C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/                      (tes concepts, et son index.md)
C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/RAPPORT_areas.md    (ton rapport)
```

**Aucun autre fichier, nulle part.** Trois autres agents travaillent en
parallele sur les trois autres seaux. `C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/` ne t'appartient pas.

Sans ce cloisonnement, deux agents se reecrivent sans que ni l'un ni l'autre ne
le voie — c'est arrive, et le cout n'a ete decouvert qu'a la fin.

## Ce que tu peux lire

```
C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/                     (LECTURE SEULE — c'est le corpus)
C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat/02_Areas_Spock.jsonl    (l'extraction — commence par la)
C:/Users/amado/ASpace_OS_V3/50_Distillation/index.md                  (la methode)
```

## Commence par le substrat, pas par les fichiers

`_substrat/02_Areas_Spock.jsonl` contient **une ligne par fichier .md du seau** :
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

- **444 fichiers `.md`**, hors `node_modules`, `.git` et `dist`
- zones : `J01_Jerry_Prime_LD01_Business` (134) - `the-bridge-__-life-os` (34) - `J03_Jerry_Nexus_LD02_LD06_Finance_Family` (32) - `J04_Jerry_Solarpunk` (20) - `J02_Jerry_Bio` (20) - `Business_Pulse` (17) - `graphify-out` (181, sorties generees)

Ce seau est le plus petit et le plus dense du PARA : 444 fichiers pour quatre
Jerry, Business_Pulse et le pont Life OS. **Tu peux esperer une couverture
reelle proche de l'exhaustivite** — c'est le seul seau dans ce cas. Profites-en
pour poser le vocabulaire que les autres reutiliseront.

Ce qui distingue un Area d'un Projet n'est pas la taille, c'est **l'absence
d'echeance**. Si un dossier de ce seau porte une date de fin, dis-le : il est
peut-etre mal range, et c'est une information.

Les quatre Jerry portent des codes `LD01` a `LD08`. Etablis la correspondance
Jerry -> LD -> domaine, et signale tout LD qui n'est rattache a aucun Jerry, ou
rattache a deux.

`graphify-out/` contient des **sorties generees** par un outil, pas de la
connaissance ecrite a la main. Ne les distille pas comme des concepts :
compte-les et dis ce qu'elles sont.

## Ce qu'on attend

**14 concepts OKF v0.2 au minimum**, dans `C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/`, nommes en
`kebab-case.md`, chacun avec son frontmatter complet et des `sources` qui
pointent sur des chemins reels.

Un concept n'est pas le resume d'un fichier. C'est une **notion** : une entite,
une relation, une decision, un piege deja paye. Si ton concept ne pouvait pas
etre relu dans six mois par quelqu'un qui n'a pas le corpus sous les yeux, ce
n'est pas un concept.

Vise en priorite ce qui alimente un **graphe RDF** : des entites nommees, des
relations typees entre elles, et les proprietes qui les qualifient. Pense en
triplets sujet-predicat-objet meme quand tu ecris en prose.

Mets a jour `C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/index.md` : une ligne par concept, sous `# Files`.

## Ton rapport

`C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/RAPPORT_areas.md`. Le garde-fou dit ce qu'il doit contenir.
Le chiffre le plus important est **combien tu as lu, sur combien de disponibles**.
