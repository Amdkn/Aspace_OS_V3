"""Genere les quatre briefs de distillation, a perimetres disjoints.

Un generateur plutot que quatre fichiers ecrits a la main : la tete du brief
est identique pour les quatre (perimetre, methode, format de sortie), et seule
la partie propre au seau change. Ecrire quatre fois la meme tete, c'est
garantir qu'elle divergera.
"""

import io
import os

BASE = "C:/Users/amado/ASpace_OS_V3/50_Distillation"
V2 = "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise"

SEAUX = {
    "areas": dict(
        seau="02_Areas_Spock", dossier="areas", md=444, cible=14,
        zones=("`J01_Jerry_Prime_LD01_Business` (134) - `the-bridge-__-life-os` (34) - "
               "`J03_Jerry_Nexus_LD02_LD06_Finance_Family` (32) - `J04_Jerry_Solarpunk` (20) - "
               "`J02_Jerry_Bio` (20) - `Business_Pulse` (17) - `graphify-out` (181, sorties generees)"),
        specifique="""Ce seau est le plus petit et le plus dense du PARA : 444 fichiers pour quatre
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
compte-les et dis ce qu'elles sont."""),

    "projets": dict(
        seau="01_Projects_Picard", dossier="projets", md=2154, cible=16,
        zones=("`04 Alikaly Bana Holding to LLC` (208) - `03_RILCOT_Members_Space_OS` (203) - "
               "`05 marina Cleaning BOS & SOP` (197) - `02 ABC OS & Child Care BOS` (193) - "
               "`01-omk-business-os` (137) - `ClaudeClaw Agent` (5) - "
               "`Cerritos_Plane_Onboarding` (3) - `graphify-out` (1 208, sorties generees)"),
        specifique="""Cinq chantiers clients reels, plus deux embryons.

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
Signale-le. Ne le deplace pas."""),

    "archives": dict(
        seau="04_Archives_Data", dossier="archives", md=12284, cible=12,
        zones=("`_V3_STRUCTURE_2026-08-02` (11 504) - `Legacy_LifeOS_App_Specs_2026-05-22` (375) - "
               "`graphify-out` (387) - `03_OpenClaw_Body_Legacy` (10) - `Backup_01` (6)"),
        specifique="""**94 % de ce seau tient dans un seul dossier** : `_V3_STRUCTURE_2026-08-02`,
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
echantillon, et ne le presente jamais comme un inventaire."""),

    "ressources": dict(
        seau="03_Resources_Geordi", dossier="ressources", md=48378, cible=20,
        zones=("`01_Guides` (15 560) - `04_From_V2_Root` (14 632) - `05_From_V2_Domains` (8 888) - "
               "`06_Claude_Code_Bare` (5 460) - `03_Memory_Unified` (1 774) - "
               "`graphify-out` (1 195) - `09_Life_OS` (297) - `08_Workspaces_Dormants_2026-08-01` (268)"),
        specifique="""**76 % du corpus distillable est ici** : 48 378 fichiers sur 63 260. C'est le
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
zone combien tu as lu sur combien, et laisse une carte de ce qui reste."""),
}

TETE = """# BRIEF — distiller {seau} vers des concepts OKF v0.2

## Ton perimetre EXCLUSIF en ecriture

```
{base}/{dossier}/                      (tes concepts, et son index.md)
{base}/_briefs/RAPPORT_{dossier}.md    (ton rapport)
```

**Aucun autre fichier, nulle part.** Trois autres agents travaillent en
parallele sur les trois autres seaux. `{base}/ontologie/` ne t'appartient pas.

Sans ce cloisonnement, deux agents se reecrivent sans que ni l'un ni l'autre ne
le voie — c'est arrive, et le cout n'a ete decouvert qu'a la fin.

## Ce que tu peux lire

```
{v2}/{seau}/                     (LECTURE SEULE — c'est le corpus)
{base}/_substrat/{seau}.jsonl    (l'extraction — commence par la)
{base}/index.md                  (la methode)
```

## Commence par le substrat, pas par les fichiers

`_substrat/{seau}.jsonl` contient **une ligne par fichier .md du seau** :
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

- **{md} fichiers `.md`**, hors `node_modules`, `.git` et `dist`
- zones : {zones}

{specifique}

## Ce qu'on attend

**{cible} concepts OKF v0.2 au minimum**, dans `{base}/{dossier}/`, nommes en
`kebab-case.md`, chacun avec son frontmatter complet et des `sources` qui
pointent sur des chemins reels.

Un concept n'est pas le resume d'un fichier. C'est une **notion** : une entite,
une relation, une decision, un piege deja paye. Si ton concept ne pouvait pas
etre relu dans six mois par quelqu'un qui n'a pas le corpus sous les yeux, ce
n'est pas un concept.

Vise en priorite ce qui alimente un **graphe RDF** : des entites nommees, des
relations typees entre elles, et les proprietes qui les qualifient. Pense en
triplets sujet-predicat-objet meme quand tu ecris en prose.

Mets a jour `{base}/{dossier}/index.md` : une ligne par concept, sous `# Files`.

## Ton rapport

`{base}/_briefs/RAPPORT_{dossier}.md`. Le garde-fou dit ce qu'il doit contenir.
Le chiffre le plus important est **combien tu as lu, sur combien de disponibles**.
"""


def main() -> None:
    os.makedirs(os.path.join(BASE, "_briefs"), exist_ok=True)
    for cle, d in SEAUX.items():
        txt = TETE.format(base=BASE, v2=V2, **d)
        chemin = os.path.join(BASE, "_briefs", f"BRIEF_{cle}.md")
        with io.open(chemin, "w", encoding="utf-8") as f:
            f.write(txt)
        print(f"BRIEF_{cle}.md  {len(txt):>6} octets  cible={d['cible']} concepts  corpus={d['md']} md")


if __name__ == "__main__":
    main()
