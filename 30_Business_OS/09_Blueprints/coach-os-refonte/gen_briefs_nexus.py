# -*- coding: utf-8 -*-
"""Genere les 4 briefs d'exploration des depots OMK."""
import pathlib
P = pathlib.Path(__file__).parent

PIEGE = """
## Piege obligatoire — les jonctions NTFS

Ce disque porte des **jonctions NTFS** : des dossiers qui pointent ailleurs dans
l'arbre, parfois en boucle. `os.path.islink()` **ne les voit pas**. Un `os.walk`
naif a deja compte 13,8 millions de fichiers la ou il y en a 14 613.

Elles ont ete cartographiees pour toi : **32 jonctions** sous `30_Business_OS`
(dont tout `00_Jerry_Business_Pulse/04_Business_Domains/00_Links/`, qui reboucle
dans l'arbre) et **1** sous `01-omk-business-os`.

Si tu parcours l'arborescence par script, **tu dois** ecarter les points de
reanalyse :

```python
import os, stat
RP = getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)
for cur, ds, fs in os.walk(root):
    ds[:] = [d for d in ds
             if not (os.stat(os.path.join(cur, d), follow_symlinks=False)
                     .st_file_attributes & RP)
             and d not in {'node_modules', '.git', '.next', 'dist', 'build',
                           '__pycache__', '.venv'}]
```

**Ne supprime jamais un dossier de ce disque.** `rm -rf`, `rmtree` et
`Remove-Item -Recurse` suivent les jonctions et detruisent la cible reelle.
De toute facon tu es en lecture seule (voir Interdits).
"""

CONTEXTE = """
## Le contexte

**OMK Nexus** est le produit actuel : un Business OS cible sur la niche des
**coachs**. L'ambition va plus loin — que la meme base serve d'autres niches, et
qu'elle devienne le socle de deux produits a venir, **Solaris** et **Orbiter**.

La question qu'on instruit : **qu'est-ce qui, dans ce qui existe deja, est propre
au metier de coach, et qu'est-ce qui est generique ?** C'est cette frontiere qui
decide si le produit se duplique ou se reecrit a chaque niche.

Un travail parallele a etabli une these : le metier de *Forward Deployed
Engineer* se decompose en gestes, dont cinq sont automatisables et quatre
resistent (mandat hierarchique, consentement a reveler l'exception,
responsabilite juridique, promotion d'un constat en primitive de plateforme).
La couche manquante identifiee est un **graphe de contexte** : un depot versionne
des entites, relations et regles du domaine du client. Tu n'as pas a valider
cette these — mais si tu croises dans le corpus quelque chose qui la confirme ou
la contredit, **dis-le**.
"""

DISCIPLINE = """
## Discipline de lecture — tu ne peux pas tout lire

{VOLUME}

Procede **de haut en bas**, jamais en balayage :

1. Liste l'arborescence sur 2 ou 3 niveaux (jonctions ecartees).
2. Lis d'abord les `README`, `INDEX`, `CANON`, `NORTH_STAR`, `MAP`, `CHARTE`,
   `*_CANON.md` — les fichiers qui se presentent comme des points d'entree.
3. Ne descends dans un dossier que si ce que tu as lu te dit qu'il porte une
   reponse a l'une des questions ci-dessous.

**Budget : environ {BUDGET} fichiers lus en entier.** Tiens le compte et
annonce-le dans ton rapport. Un rapport qui pretend avoir tout lu sera lu comme
un rapport qui a invente.

Quand tu cites un fait, donne le **chemin du fichier**. Un constat sans chemin
verifiable ne vaut rien.
"""

INTERDITS = """
## Interdits

1. **Lecture seule.** Tu ne modifies, ne deplaces, ne supprimes aucun fichier de
   ces depots. Tu ecris **un seul fichier** : `{SORTIE}`.
2. Ne descends dans aucune jonction NTFS (voir plus haut).
3. Ne lis pas `node_modules`, `.git`, `.next`, `dist`, `build`.
4. Pas de recherche web, pas d'installation, pas de `npm`, pas de build.
5. **N'invente rien.** Si tu ne trouves pas la reponse a une question, ecris
   « non trouve » et dis ou tu as cherche. C'est une information utile ; une
   reponse brodee ne l'est pas.
6. Ne redige pas de plan d'implementation ni de code.

## Si tu dois t'arreter

Ecris le rapport avec ce que tu as etabli, ton compte de fichiers lus, et une
section « **reste a couvrir** ». Un rapport partiel et date vaut mieux qu'un
rapport complet et approximatif.
"""

V2 = r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise"

AGENTS = {
"N1": dict(
  titre="Le canon — 01-omk-business-os",
  racine=V2 + r"\01_Projects_Picard\01-omk-business-os",
  volume="Ce depot est **petit** : 78 dossiers, 302 fichiers, 137 en `.md`, 1 jonction.\nTu peux le couvrir en entier, et c'est attendu.",
  budget="100",
  sortie="analyses/N1_canon.md",
  questions="""
### 1. Que declare ce depot ?

Il porte des `chartes`, `chartes_cycle_2`, `ownerbooks`, `runbooks`,
`B2_Business_Domains`, `B3_Warp_Core_Execution`. Explique **ce que chacun de ces
mots designe** dans ce systeme, en une phrase chacun, avec le fichier qui te le
fait dire. Ne devine pas d'apres le nom.

### 2. Les domaines metier

`B2_Business_Domains` : liste les domaines declares, et pour chacun son
proprietaire, son perimetre, et ce qui le relie aux autres.

### 3. Coach ou generique ?

Un tableau, une ligne par artefact structurant :

| artefact | fichier | propre au coaching | generique | ce qu'il faudrait pour le generaliser |

C'est **la question centrale**. Sois severe : un artefact qui mentionne
« client » et « seance » n'est pas generique parce qu'on pourrait renommer les
mots.

### 4. Nexus, Solaris, Orbiter

Ces trois noms apparaissent-ils ? Ou, et que disent les fichiers qui les portent
de leur relation ? Si l'un des trois est absent, dis-le.

### 5. Ce qui est mort

Quels artefacts sont manifestement perimes, contredits ailleurs, ou jamais
references ? Donne le chemin et le signe qui te le fait dire.
"""),

"N2": dict(
  titre="Le pouls metier — 00_Jerry_Business_Pulse",
  racine=V2 + r"\03_Resources_Geordi\05_From_V2_Domains\30_Business_OS\00_Jerry_Business_Pulse",
  volume="Ce dossier contient **5 232 fichiers `.md`** hors jonctions. C'est la plus\ngrosse masse du corpus. Tu n'en liras qu'une fraction, et c'est voulu.",
  budget="70",
  sortie="analyses/N2_pulse.md",
  questions="""
### 1. La carte

Que contient ce dossier, structurellement ? Donne l'arborescence utile sur 3
niveaux avec, pour chaque branche, ce qu'elle porte en une ligne.

### 2. Le modele de travail

Ce corpus decrit une facon d'operer une entreprise. **Nomme-la.** Quels sont ses
objets de premiere classe (les choses qu'il manipule), ses roles, ses cycles ?
Cherche notamment ce que designent `B1`/`B2`/`B3`, `Squad`, `Owner`, `Verse`,
`Pulse`, `12WY`, `North Star` — chacun avec le fichier qui te le fait dire.

### 3. Coach ou generique ?

Meme tableau que N1 : | artefact | fichier | propre au coaching | generique |
ce qu'il faudrait pour le generaliser |

### 4. Ce que ca dit de l'ontologie

Ce corpus nomme-t-il deja des entites metier et leurs relations ? Si oui, liste
celles que tu trouves — c'est peut-etre l'ontologie du produit, deja ecrite en
prose sans avoir ete reconnue comme telle. Si non, dis-le : c'est une reponse.

### 5. Les trois choses a garder

Parmi tout ce que tu as lu, les trois artefacts qui meritent de survivre a une
refonte, et pourquoi. Classe-les.
"""),

"N3": dict(
  titre="Ce qui est reellement construit — 10_Projects",
  racine=V2 + r"\03_Resources_Geordi\05_From_V2_Domains\30_Business_OS\10_Projects",
  volume="Ce dossier contient **1 738 fichiers `.md`** hors jonctions, et du code.\nC'est la ou vivent les projets reels, dont `omk/repos/coach-os`.",
  budget="60",
  sortie="analyses/N3_projets.md",
  questions="""
### 1. L'inventaire

Quels projets vivent ici ? Pour chacun : son nom, son etat apparent (vivant,
dormant, mort), sa pile technique, et le fichier qui te le fait dire.

Attention : plusieurs projets peuvent etre des variantes ou des snapshots du
meme. Dis lesquels, et lequel est le canon.

### 2. Coach OS

C'est le projet central (`omk/repos/coach-os`). Decris ce qu'il EST aujourd'hui :
son shell, ses 19 apps, ce que chaque app fait reellement — pas ce que son nom
suggere. Distingue les apps qui portent du contenu reel de celles qui sont des
coquilles.

### 3. Le fosse entre la doctrine et le code

Le corpus documentaire (chartes, ownerbooks, runbooks) decrit un modele de
travail. Le code implemente autre chose. **Ou est l'ecart ?** Nomme trois
endroits precis ou ce qui est ecrit n'est pas ce qui est construit.

### 4. Ce qui est reutilisable au-dela du coaching

Dans le code, qu'est-ce qui ne suppose rien du metier de coach et pourrait servir
telle quelle a une autre niche ? Et qu'est-ce qui est coache jusqu'a l'os ?

### 5. Nexus, Solaris, Orbiter dans le code

Ces noms apparaissent-ils dans le code ou la configuration ? Ou, et que disent
ces occurrences ?
"""),

"N4": dict(
  titre="La ligne de produits — Nexus, Solaris, Orbiter",
  racine=V2,
  volume=("Tu fouilles **deux depots** :\n"
          "- `03_Resources_Geordi\\05_From_V2_Domains\\30_Business_OS` (6 979 `.md`, 32 jonctions)\n"
          "- `01_Projects_Picard\\01-omk-business-os` (137 `.md`, 1 jonction)\n\n"
          "Tu ne les cartographies pas — d'autres agents s'en chargent. Tu **cherches**."),
  budget="50",
  sortie="analyses/N4_ligne_produits.md",
  questions="""
Tu instruis **une seule question** : quelle est la ligne de produits, et qu'est-ce
qui la rend duplicable ?

Commence par une recherche textuelle sur `Nexus`, `Solaris`, `Orbiter`, `niche`,
`vertical`, `multi-tenant`, `white label`, `AaaS`, `Agency as a Service`. Puis
lis les fichiers qui ressortent.

### 1. Les trois noms

Pour chacun : ce qu'il designe, son etat (idee, specifie, construit, abandonne),
et les fichiers qui l'etablissent. Si un nom n'existe nulle part, dis-le
clairement — c'est un fait important.

### 2. La relation entre eux

Nexus est-il decrit comme la base de Solaris et Orbiter, ou est-ce une intention
non ecrite ? Cite les passages qui l'etablissent, ou constate leur absence.

### 3. La frontiere du generique

**La question qui compte.** Qu'est-ce qui, dans le systeme actuel, devrait etre
**partage** entre niches, et qu'est-ce qui doit rester **par niche** ?

Un tableau : | element | partage | par niche | pourquoi |

Cherche particulierement : le modele de donnees, l'ontologie metier, les
runbooks, les squads/roles, les offres, le tunnel d'acquisition, la marque.

### 4. Ce qui empeche aujourd'hui la duplication

Nomme trois obstacles concrets — pas « il faudrait refactorer », mais des
endroits precis ou une hypothese coach est cablee en dur.

### 5. Le pari

Si OMK devait ouvrir une deuxieme niche demain, quelle serait-elle d'apres ce
corpus, et qu'est-ce qui casserait en premier ?
"""),
}

for aid, a in AGENTS.items():
    txt = ("# BRIEF " + aid + " — " + a["titre"] + "\n\n"
           "Tu es un agent d'exploration. Tu lis un corpus existant et tu en rends une\n"
           "carte utilisable. Tu ne construis rien.\n"
           "\n**Racine de ton perimetre** : `" + a["racine"] + "`\n"
           + CONTEXTE + PIEGE
           + DISCIPLINE.replace("{VOLUME}", a["volume"]).replace("{BUDGET}", a["budget"])
           + "\n## Livrable — `" + a["sortie"] + "`\n"
           + a["questions"]
           + "\n### Enfin — ton compte\n\n"
             "Termine par le nombre exact de fichiers que tu as lus en entier, et la liste\n"
             "des dossiers que tu as ouverts sans y entrer.\n"
           + INTERDITS.replace("{SORTIE}", a["sortie"]))
    (P / ("BRIEF_" + aid + ".md")).write_text(txt, encoding="utf-8")
    print("BRIEF_%s.md  %6d car.  -> %s" % (aid, len(txt), a["sortie"]))
