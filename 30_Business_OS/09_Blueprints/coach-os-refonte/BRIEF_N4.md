# BRIEF N4 — La ligne de produits — Nexus, Solaris, Orbiter

Tu es un agent d'exploration. Tu lis un corpus existant et tu en rends une
carte utilisable. Tu ne construis rien.

**Racine de ton perimetre** : `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise`

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

Tu fouilles **deux depots** :
- `03_Resources_Geordi\05_From_V2_Domains\30_Business_OS` (6 979 `.md`, 32 jonctions)
- `01_Projects_Picard\01-omk-business-os` (137 `.md`, 1 jonction)

Tu ne les cartographies pas — d'autres agents s'en chargent. Tu **cherches**.

Procede **de haut en bas**, jamais en balayage :

1. Liste l'arborescence sur 2 ou 3 niveaux (jonctions ecartees).
2. Lis d'abord les `README`, `INDEX`, `CANON`, `NORTH_STAR`, `MAP`, `CHARTE`,
   `*_CANON.md` — les fichiers qui se presentent comme des points d'entree.
3. Ne descends dans un dossier que si ce que tu as lu te dit qu'il porte une
   reponse a l'une des questions ci-dessous.

**Budget : environ 50 fichiers lus en entier.** Tiens le compte et
annonce-le dans ton rapport. Un rapport qui pretend avoir tout lu sera lu comme
un rapport qui a invente.

Quand tu cites un fait, donne le **chemin du fichier**. Un constat sans chemin
verifiable ne vaut rien.

## Livrable — `analyses/N4_ligne_produits.md`

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

### Enfin — ton compte

Termine par le nombre exact de fichiers que tu as lus en entier, et la liste
des dossiers que tu as ouverts sans y entrer.

## Interdits

1. **Lecture seule.** Tu ne modifies, ne deplaces, ne supprimes aucun fichier de
   ces depots. Tu ecris **un seul fichier** : `analyses/N4_ligne_produits.md`.
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
