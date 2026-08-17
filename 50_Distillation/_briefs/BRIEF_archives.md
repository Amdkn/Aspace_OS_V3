# BRIEF — distiller 04_Archives_Data vers des concepts OKF v0.2

## Ton perimetre EXCLUSIF en ecriture

```
C:/Users/amado/ASpace_OS_V3/50_Distillation/archives/                      (tes concepts, et son index.md)
C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/RAPPORT_archives.md    (ton rapport)
```

**Aucun autre fichier, nulle part.** Trois autres agents travaillent en
parallele sur les trois autres seaux. `C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/` ne t'appartient pas.

Sans ce cloisonnement, deux agents se reecrivent sans que ni l'un ni l'autre ne
le voie — c'est arrive, et le cout n'a ete decouvert qu'a la fin.

## Ce que tu peux lire

```
C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/                     (LECTURE SEULE — c'est le corpus)
C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat/04_Archives_Data.jsonl    (l'extraction — commence par la)
C:/Users/amado/ASpace_OS_V3/50_Distillation/index.md                  (la methode)
```

## Commence par le substrat, pas par les fichiers

`_substrat/04_Archives_Data.jsonl` contient **une ligne par fichier .md du seau** :
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

- **12284 fichiers `.md`**, hors `node_modules`, `.git` et `dist`
- zones : `_V3_STRUCTURE_2026-08-02` (11 504) - `Legacy_LifeOS_App_Specs_2026-05-22` (375) - `graphify-out` (387) - `03_OpenClaw_Body_Legacy` (10) - `Backup_01` (6)

**94 % de ce seau tient dans un seul dossier** : `_V3_STRUCTURE_2026-08-02`,
11 504 fichiers.

Commence par etablir ce que c'est — un instantane ? une migration abandonnee ?
une structure proposee puis remplacee ? La reponse change entierement la valeur
des 11 504 autres, et elle se trouve probablement dans les quelques fichiers de
tete du dossier, pas dans le tas.

Une archive ne se distille pas pour ce qu'elle contient mais **pour ce qu'elle
apprend**. La question utile est : *qu'est-ce qui a ete tente ici, et pourquoi
ca s'est arrete ?* Un inventaire de fichiers morts n'interesse personne ; une
tentative abandonnee et sa raison, si.

`Legacy_LifeOS_App_Specs_2026-05-22` porte des specifications d'applications.
Compare-les a ce qui existe aujourd'hui **quand tu peux le faire sans sortir de
ton perimetre de lecture** — sinon, dis que tu ne peux pas, plutot que de
supposer.

**Tu ne peux pas lire 12 284 fichiers.** Echantillonne par dossier, declare ton
echantillon, et ne le presente jamais comme un inventaire.

## Ce qu'on attend

**12 concepts OKF v0.2 au minimum**, dans `C:/Users/amado/ASpace_OS_V3/50_Distillation/archives/`, nommes en
`kebab-case.md`, chacun avec son frontmatter complet et des `sources` qui
pointent sur des chemins reels.

Un concept n'est pas le resume d'un fichier. C'est une **notion** : une entite,
une relation, une decision, un piege deja paye. Si ton concept ne pouvait pas
etre relu dans six mois par quelqu'un qui n'a pas le corpus sous les yeux, ce
n'est pas un concept.

Vise en priorite ce qui alimente un **graphe RDF** : des entites nommees, des
relations typees entre elles, et les proprietes qui les qualifient. Pense en
triplets sujet-predicat-objet meme quand tu ecris en prose.

Mets a jour `C:/Users/amado/ASpace_OS_V3/50_Distillation/archives/index.md` : une ligne par concept, sous `# Files`.

## Ton rapport

`C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/RAPPORT_archives.md`. Le garde-fou dit ce qu'il doit contenir.
Le chiffre le plus important est **combien tu as lu, sur combien de disponibles**.
