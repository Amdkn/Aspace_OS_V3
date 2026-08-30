# BRIEF — unifier les memoires autour d'Agent OS

Tu produis **une architecture, pas un produit**. Le livrable principal est un
document de conception. Le code ne vient qu'apres, et seulement s'il est
necessaire pour prouver que l'architecture tient.

## Le probleme

La memoire de cet ecosysteme existe en **quatre endroits qui s'ignorent**. Aucun
n'est faux ; aucun ne sait ce que savent les autres. Il faut les unifier autour
d'Agent OS, sans en detruire aucun.

**Ne suppose rien.** Chaque source ci-dessous doit etre **ouverte et lue** avant
d'ecrire une ligne d'architecture. Un plan bati sur ce que tu crois savoir de
PocketBase ou de TencentDB sera faux.

### 1. TencentDB Agent Memory

`C:/Users/amado/TencentDB-Agent-Memory/`

Depot TencentCloud, MIT, Node >= 22.16, ponts OpenClaw et Hermes. Quatre modules
dont tu dois etablir le role exact en lisant leur code et leurs README :
`MemoryCore`, `MemoryKnowledge`, `MemoryPanel`, `MemoryProxy`.

Le proprietaire dit qu'il porte **quatre couches de memoire**. Trouve-les dans le
depot et **nomme-les avec les mots du depot**, pas avec la taxonomie generique
(episodique / semantique / procedurale...) — sauf si c'est exactement ce que le
depot emploie. Lis aussi `RAPPORT_knowledge_config.md` et
`BRIEF_knowledge_config.md` a la racine : quelqu'un a deja travaille dessus.

### 2. PocketBase avec sqlite-vec

`C:/Users/amado/pocketbase-vec/`
(jonction : `ASpace_OS_V3/00_Amadeus/10_Observers/pocketbase-vec`)

PocketBase compile comme cadriciel Go, pilote SQLite WASM (ncruces), extension
vectorielle `sqlite-vec`, **sans CGO**. Etabli ce qu'il stocke aujourd'hui, s'il
tourne, et ce qu'il apporte que TencentDB n'apporte pas.

**Attention aux jonctions NTFS.** `os.path.islink()` ne les voit pas. Pour en
detecter une, tester `FILE_ATTRIBUTE_REPARSE_POINT` (0x400) sur
`st_file_attributes`. **Ne supprime jamais une jonction autrement que par
`os.rmdir`** — `rmtree`, `rm -rf` et `Remove-Item -Recurse` suivent le lien et
detruisent la cible reelle. Ici tu ne supprimes rien, mais un parcours naif de
l'arborescence peut compter 13,8 millions de fichiers la ou il y en a 14 613.

### 3. Les quatre piliers de la base de connaissance

`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/`

- **OKF** — le format : ce qui fait qu'un paquet est valide.
  `00_Index/OKF_INDEX.md`
- **Wiki** — le canon des concepts. `03_Memory_Unified/LLM_Wiki/wiki/index.md`,
  1 773 pages, 319 liens.
- **Graphify** — la topologie. `wiki/graphify-out/GRAPH_REPORT.json`, plus un
  `graph.json` de 4 Mo. **Ne charge pas le graphe entier en memoire** : lis le
  rapport, et les fragments de `chunks/` si besoin.
- **Dox** — la loi et le comportement. `06_Claude_Code_Bare/CLAUDE.md`.

Point d'entree : `CLAUDE.md` a la racine de Geordi, puis
`00_Index/INDEX_OF_INDEXES.md`.

### 4. Le plan meta-memoire, deja ecrit

`00_Index/PLAN_META_MEMOIRE_2026-08-01.md`

**Lis-le en entier avant de proposer quoi que ce soit.** Il contient deja : les
strates de memoire dans Geordi (section 3), la taxonomie (4), la sequence
d'execution (5), les sources introuvables (6), et surtout **ce que ce document ne
fait pas** (7). Cette derniere section est la plus utile : elle borne le
perimetre. Ne repropose pas ce qu'il a deja tranche, et ne contredis pas ses
decisions sans dire explicitement laquelle et pourquoi.

Lis aussi `wiki/ROT.md` : les strates S0 a S4 et leurs taux de peremption. Une
memoire sans date de peremption devient un depotoir — c'est le sujet.

## Ce que le document doit trancher

1. **Une carte de l'existant.** Qui detient quoi, aujourd'hui. Un tableau :
   source, nature de ce qu'elle stocke, format, volume, si elle tourne, et **ce
   qui se perd si on la debranche**. Mesure, ne suppose pas.

2. **Les recouvrements.** Ou deux sources stockent la meme chose, et laquelle
   doit gagner. C'est la decision centrale : sans arbitrage de propriete, une
   unification produit deux verites au lieu d'une.

3. **Les couches, unifiees.** Une seule taxonomie qui absorbe les quatre couches
   de TencentDB, les strates S0-S4 de Geordi, et les vecteurs de PocketBase.
   Pour chaque couche : ce qu'elle retient, qui l'ecrit, qui la lit, sa duree de
   vie, et **comment on sait qu'une entree est perimee**.

4. **Le role d'Agent OS.** Le proprietaire veut l'unification **autour** d'Agent
   OS (`C:/Users/amado/agent-os/`) — le systeme de specs et de standards de
   Brian Casel. Sois honnete sur ce qu'il est : il cadre l'ecriture, il ne
   stocke rien. Dis precisement ce qu'il peut porter (l'index, les standards,
   les contrats de lecture et d'ecriture) et ce qu'il ne peut pas.

5. **Le chemin, par etapes reversibles.** Chaque etape doit valoir seule : si on
   s'arrete apres la deuxieme, on doit etre en meilleur etat qu'avant. Pas de
   grand soir. Et un `MANIFEST.json` (`src` -> `dst`) pour toute etape qui
   deplace des fichiers — **deplacer, jamais supprimer.**

6. **Ce que tu refuses de trancher**, avec la raison et la question exacte a
   poser au proprietaire.

## Cloisonnement

Un autre agent travaille **en ce moment** dans
`C:/Users/amado/agent-os/observatoire/`. **N'y touche sous aucun pretexte.**

Ton perimetre en ecriture :
- `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/` — le
  document de conception et tes notes ;
- `C:/Users/amado/agent-os/memoire/` — **si et seulement si** ton architecture
  demande du code, et uniquement dans ce dossier neuf.

Partout ailleurs : **lecture seule**.

## Interdits

0. **N'invoque aucun workflow BMAD.** Ils ouvrent une porte « [A] Approve » que
   personne ne peut franchir : la session est non interactive.
1. Tu ne supprimes rien, nulle part. Tu ne deplaces rien sans `MANIFEST.json`.
2. Tu ne demarres aucun service, tu ne migres aucune donnee, tu n'ecris dans
   aucune base. Ce brief produit un plan, pas une migration.
3. **Scanne les secrets avant de citer un fichier** — motifs `sk-`, `sbp_`,
   `vcp_`, `ghp_`, JWT, cles PEM, `.env` hors `.example`. Ne recopie jamais une
   valeur dans le document : nomme le fichier et la ligne.
4. Aucune dependance installee. Pas de `git commit`, pas de `git push`.
5. Chemins **absolus** partout.

## Rapport et livrable

**Le document** :
`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/ARCHITECTURE_MEMOIRE_UNIFIEE.md`

**Le rapport** :
`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/RAPPORT_UNIFICATION_MEMOIRE.md`

Le rapport dit : ce que tu as **reellement ouvert et lu** (liste des fichiers,
pas des dossiers), ce que tu as **mesure** et comment, ce que tu as **suppose**
faute d'acces — dis-le, ne le maquille pas — et **tout point non fait avec sa
raison**.

Un point non fait et signale vaut mieux qu'un point bacle en silence. Une
architecture batie sur une supposition non signalee est pire que pas
d'architecture du tout.

Si tu dois t'arreter avant la fin, ecris quand meme ces deux fichiers avec
l'etat exact.
