# BRIEF — distiller 01_Projects_Picard vers des concepts OKF v0.2

## Ton perimetre EXCLUSIF en ecriture

```
C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/                      (tes concepts, et son index.md)
C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/RAPPORT_projets.md    (ton rapport)
```

**Aucun autre fichier, nulle part.** Trois autres agents travaillent en
parallele sur les trois autres seaux. `C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/` ne t'appartient pas.

Sans ce cloisonnement, deux agents se reecrivent sans que ni l'un ni l'autre ne
le voie — c'est arrive, et le cout n'a ete decouvert qu'a la fin.

## Ce que tu peux lire

```
C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/                     (LECTURE SEULE — c'est le corpus)
C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat/01_Projects_Picard.jsonl    (l'extraction — commence par la)
C:/Users/amado/ASpace_OS_V3/50_Distillation/index.md                  (la methode)
```

## Commence par le substrat, pas par les fichiers

`_substrat/01_Projects_Picard.jsonl` contient **une ligne par fichier .md du seau** :
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

- **2154 fichiers `.md`**, hors `node_modules`, `.git` et `dist`
- zones : `04 Alikaly Bana Holding to LLC` (208) - `03_RILCOT_Members_Space_OS` (203) - `05 marina Cleaning BOS & SOP` (197) - `02 ABC OS & Child Care BOS` (193) - `01-omk-business-os` (137) - `ClaudeClaw Agent` (5) - `Cerritos_Plane_Onboarding` (3) - `graphify-out` (1 208, sorties generees)

Cinq chantiers clients reels, plus deux embryons.

**Attention au compte.** Sur 2 154 fichiers, 1 208 sont dans `graphify-out/` —
des sorties generees. Le corpus ecrit a la main est donc d'environ **950
fichiers**, pas 2 154. Ce chiffre doit figurer dans ton rapport : il corrige une
impression fausse que tout le monde aurait reprise.

Pour chaque projet, un concept qui repond a trois questions : **ce qu'il visait,
ce qui a ete livre, ce qui ne l'a pas ete.** Un projet dont tu ne peux pas dire
s'il est fini est un projet dont tu ecris qu'on ne peut pas le dire.

`01-omk-business-os` a une suite vivante ailleurs (le depot `coach-os`). Note le
lien, ne va pas le verifier : il est hors de ton perimetre.

Un projet sans echeance n'est pas un projet, c'est un domaine mal range.
Signale-le. Ne le deplace pas.

## Ce qu'on attend

**16 concepts OKF v0.2 au minimum**, dans `C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/`, nommes en
`kebab-case.md`, chacun avec son frontmatter complet et des `sources` qui
pointent sur des chemins reels.

Un concept n'est pas le resume d'un fichier. C'est une **notion** : une entite,
une relation, une decision, un piege deja paye. Si ton concept ne pouvait pas
etre relu dans six mois par quelqu'un qui n'a pas le corpus sous les yeux, ce
n'est pas un concept.

Vise en priorite ce qui alimente un **graphe RDF** : des entites nommees, des
relations typees entre elles, et les proprietes qui les qualifient. Pense en
triplets sujet-predicat-objet meme quand tu ecris en prose.

Mets a jour `C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/index.md` : une ligne par concept, sous `# Files`.

## Ton rapport

`C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/RAPPORT_projets.md`. Le garde-fou dit ce qu'il doit contenir.
Le chiffre le plus important est **combien tu as lu, sur combien de disponibles**.
