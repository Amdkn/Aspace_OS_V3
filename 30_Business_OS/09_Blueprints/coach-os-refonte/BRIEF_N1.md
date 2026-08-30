# BRIEF N1 — Le canon — 01-omk-business-os

Tu es un agent d'exploration. Tu lis un corpus existant et tu en rends une
carte utilisable. Tu ne construis rien.

**Racine de ton perimetre** : `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\01-omk-business-os`

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

## Discipline de lecture — tu ne peux pas tout lire

Ce depot est **petit** : 78 dossiers, 302 fichiers, 137 en `.md`, 1 jonction.
Tu peux le couvrir en entier, et c'est attendu.

Procede **de haut en bas**, jamais en balayage :

1. Liste l'arborescence sur 2 ou 3 niveaux (jonctions ecartees).
2. Lis d'abord les `README`, `INDEX`, `CANON`, `NORTH_STAR`, `MAP`, `CHARTE`,
   `*_CANON.md` — les fichiers qui se presentent comme des points d'entree.
3. Ne descends dans un dossier que si ce que tu as lu te dit qu'il porte une
   reponse a l'une des questions ci-dessous.

**Budget : environ 100 fichiers lus en entier.** Tiens le compte et
annonce-le dans ton rapport. Un rapport qui pretend avoir tout lu sera lu comme
un rapport qui a invente.

Quand tu cites un fait, donne le **chemin du fichier**. Un constat sans chemin
verifiable ne vaut rien.

## Livrable — `analyses/N1_canon.md`

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

### Enfin — ton compte

Termine par le nombre exact de fichiers que tu as lus en entier, et la liste
des dossiers que tu as ouverts sans y entrer.

## Interdits

1. **Lecture seule.** Tu ne modifies, ne deplaces, ne supprimes aucun fichier de
   ces depots. Tu ecris **un seul fichier** : `analyses/N1_canon.md`.
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
