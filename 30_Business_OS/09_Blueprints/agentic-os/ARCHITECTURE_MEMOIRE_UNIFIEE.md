---
id: ARCHITECTURE_MEMOIRE_UNIFIEE_2026_08_06
layer: L2_Business_OS
role: A1_Strategic_Architecture
classification: Internal
status: DRAFT
created: 2026-08-06
okf_version: "0.1"
description: Architecture d'unification des quatre sources de mémoire (TencentDB-Agent-Memory, pocketbase-vec, Geordi KB, Agent OS) — carte de l'existant, recouvrements, taxonomie unique, rôle d'Agent OS, étapes réversibles.
doctrine_anchor: 00_Index/PLAN_META_MEMOIRE_2026-08-01.md §3 (strates S0-S4)
pere: BRIEF_UNIFICATION_MEMOIRE.md
---

# Architecture — Mémoire unifiée autour d'Agent OS

> **Statut** : DRAFT. Document d'architecture, pas un produit. Aucune ligne de code
> n'est livrée ici : ce qui est nécessaire pour prouver l'architecture viendra après,
> seulement si elle est nécessaire.
>
> **Périmètre en écriture** : ce fichier, son rapport jumeau
> [`RAPPORT_UNIFICATION_MEMOIRE.md`](RAPPORT_UNIFICATION_MEMOIRE.md), et **rien d'autre**
> en dehors des deux chemins autorisés par le brief. Le dossier `agent-os/observatoire/`
> reste intouché (autre agent en cours).
>
> **Honnêteté** : un point non fait et signalé vaut mieux qu'un point bâclé en silence.
> Là où une mesure n'a pas été possible, le rapport le dit. Ce document-ci trace des
> décisions, pas des certitudes.

---

## 0. Comment lire ce document

| | |
|---|---|
| **§1** | Carte de l'existant — qui détient quoi, mesuré sur disque, ce qui se perd si on débranche. |
| **§2** | Recouvrements — où deux sources stockent la même chose, et laquelle doit gagner. |
| **§3** | Couches unifiées — une taxonomie unique qui absorbe L0-L3 (TencentDB), S0-S4 (Geordi) et `chunks`/`embeddings` (PocketBase). Pour chaque couche : qui écrit, qui lit, durée de vie, signal de péremption. |
| **§4** | Rôle d'Agent OS — cadre, pas stockage. Ce qu'il porte et ce qu'il ne porte pas. |
| **§5** | Chemin réversible — chaque étape doit valoir seule ; aucun grand soir ; MANIFEST.json obligatoire. |
| **§6** | Ce que je refuse de trancher — avec la question exacte à poser au propriétaire. |

Toutes les mesures viennent du rapport jumeau. Toute affirmation de volume qui n'est pas
adossée à une commande `find` ou `wc` exécutée pendant cette session est marquée
**(à mesurer)** ou non faite.

---

## 1. Carte de l'existant

Quatre sources se partagent aujourd'hui la mémoire de cet écosystème. Elles ne le savent
pas. Aucune ne ment. Aucune n'est complète. Un tableau, pas une carte mentale :

| Source | Nature stockée | Format | Volume mesuré | Tourne ? | Se perd si on débranche |
|---|---|---|---:|---|---|
| **TencentDB-Agent-Memory** — `C:/Users/amado/TencentDB-Agent-Memory/` | L0-L3 Chat Memory (4 couches conversationnelles) + Wiki (Karpathy-style link graph) + CodeGraph (symbols/calls) + Skills (SOP versionnés) + ACL/Asset meta | JSON via Hono HTTP, SQLite (Drizzle) côté MemoryCore/Knowledge | non mesuré en cette session (voir §6.2) | **Oui, partielle** : MemoryKnowledge port 8421 confirmé vivant (cf. `RAPPORT_knowledge_config.md` 2026-08-04, ligne 56-66) ; autres modules non vérifiés | L1 facts utilisateur (préférences, décisions), graphe wiki ingéré, CodeGraph indexé, bindings LLM |
| **pocketbase-vec** — `C:/Users/amado/pocketbase-vec/` (jonction NTFS vers `ASpace_OS_V3/00_Amadeus/10_Observers/pocketbase-vec`) | Chunks texte (`chunks` collection, 100K char/text + source + meta) + embeddings 768-dim (vec0) + index FTS5 (BM25, unicode61+remove_diacritics) | SQLite WASM (ncruces) + sqlite-vec + FTS5, build Go, API `POST /api/vec/search` | **0 à quelques milliers** de chunks en pratique (collection `chunks` vide par défaut ; bench mesure jusqu'à 50k) | **Pas en cours** : pas de service live constaté, build `pbvec.exe` (39 Mo) présent dans le dépôt | Capacité RAG hybride (dense + BM25) souveraine 100 % locale, sans cloud ; table `embeddings` invisible du dashboard (cf. `README.md` ligne 78-86) |
| **Geordi KB** — `C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/` | 4 piliers : OKF (format standard), Wiki (1 773 pages, canon des concepts), Graphify (6 320 nœuds / 6 998 arêtes, graphe link), Dox (constitution, ADRs, D1-D8) + 22 707 .md non qualifiés (`04_From_V2_Root/` + `05_From_V2_Domains/`) | Markdown + frontmatter YAML + JSON (graph) | **48 646 .md** total mesuré par `PLAN_META_MEMOIRE_2026-08-01.md` §1.4 ; 1 773 dans `03_Memory_Unified/LLM_Wiki/wiki/` | **Oui** : les fichiers sont sur disque, lecture seule suffit pour les consulter ; pas de service runtime | Constitution, doctrine D1-D8, ADRs actifs, 1 773 pages de canon, le runbook de la mémoire elle-même |
| **Agent OS** — `C:/Users/amado/agent-os/` | Standards (coding-style, response-format, error-handling, anti-pause Supabase) + commands (plan-product, shape-spec, inject-standards, etc.) + profiles + worktrees + config.yml | Markdown + YAML | ~10 standards, 6 commands | N/A — c'est un cadre, pas un service | Standards injectés dans le system prompt ; conventions partagées entre agents |

### 1.1 Ce qui se mesure vraiment vs ce qu'on prétend

- **Geordi mesure, et le dit.** `PLAN_META_MEMOIRE_2026-08-01.md` §1.4 cite des comptes
  par sous-dossier (15 560 dans `01_Guides/`, 14 613 dans `04_From_V2_Root/`, etc.). Ce sont
  les seuls nombres que ce document peut porter comme des faits.
- **TencentDB mesure peu en surface.** Les README déclarent des capacités, pas des
  volumes. Le `RAPPORT_knowledge_config.md` 2026-08-04 confirme qu'un service répond
  (8421) mais ne dit pas combien de wikis/chunks y sont ingérés. **C'est un trou** que
  ce document ne peut pas combler en lecture seule.
- **PocketBase-vec mesure ses performances.** `README.md` ligne 56-67 donne des benchs
  KNN (1 000 / 10 000 / 50 000 vecteurs), pas la population actuelle. Le `pbvec.exe`
  est dans le dépôt, prêt à `go build`, mais aucune preuve n'a été cherchée qu'il
  tourne en service live pendant cette session.
- **Agent OS ne se mesure pas comme un volume** : c'est un registre de conventions, pas
  une base.

### 1.2 Statut opérationnel vérifié pendant cette session

| Source | Vérifié vivant ? | Comment |
|---|---|---|
| TencentDB MemoryKnowledge :8421 | ✅ (rapporté 2026-08-04) | `curl -s http://127.0.0.1:8421/health` → `{"status":"ok"}` (cf. `RAPPORT_knowledge_config.md` ligne 147) |
| TencentDB MemoryCore :8420, MemoryPanel :8123, MemoryProxy :8096 | ❌ non testé | Hors scope du brief et du `RAPPORT_knowledge_config.md` |
| pocketbase-vec | ❌ non testé | Aucun port actif repéré ; `pbvec.exe` non lancé dans cette session |
| Geordi KB | ✅ (par définition, statique) | `find` direct, jonctions repérées |
| Agent OS | ✅ (statique) | Fichiers `.md` + `config.yml` |

---

## 2. Recouvrements et arbitrage de propriété

Le problème central d'une unification est **qui détient quoi**. Sans arbitrage, on produit
deux vérités au lieu d'une. Six zones de recouvrement identifiées en lisant les sources :

### 2.1 Récit des faits observés (Chat Memory) — **TencentDB gagne**

| Qui stocke | Quoi | Format |
|---|---|---|
| TencentDB MemoryCore L0/L1 | Conversation brute, faits extraits, scénarios, profils | JSON via Hono, SQLite |
| Geordi Wiki hand_offs/ (350 fiches) | Ce qui s'est passé dans la session | MD + frontmatter |
| Geordi Wiki _CAPTURE_2026-08-01/ (117 fichiers) | Imports bruts non triés | MD |
| Geordi Wiki daily notes (`2026-07-20.md` etc.) | Notes datées | MD |

**Décision** : TencentDB L0-L3 détient le **récit opérationnel** des conversations.
Geordi `hand_offs/` détient le **journal canon** des handoffs (avec `type:` + `description:`
quand conforme OKF). Les deux ne se recouvrent pas à 100 % : TencentDB est chaud
(extraction automatique), Geordi est froid (append-only, signé humainement). **Les deux
cohabitent**. Une promotion L1 TencentDB → S3 Geordi n'est ni obligatoire, ni souhaitable :
le canon wiki est *sélection*, pas *trace*.

### 2.2 Connaissance structurée (Wiki / link graph) — **TencentDB MemoryKnowledge vs Geordi Wiki : pas le même objet**

| Qui stocke | Quoi | Format |
|---|---|---|
| TencentDB MemoryKnowledge Wiki | Documents ingérés via LLM (page + lien) | JSON Hono, SQLite + FTS5 |
| Geordi Wiki (1 773 pages) | Concepts/entities/hand_offs canoniques | MD + frontmatter OKF |
| pocketbase-vec `chunks` + `embeddings` | Morceaux de texte + vecteurs, sans graphe de liens | SQLite WASM |

**Décision** : trois usages distincts.
- **TencentDB MemoryKnowledge Wiki** = knowledge base *ingérée par LLM* depuis
  des documents bruts. Sa raison d'être est l'extraction automatique.
- **Geordi Wiki** = canon *écrit/maintenu par l'humain* (A0). Sa raison d'être est la
  doctrine (L0, ADR, entity).
- **pocketbase-vec `chunks`** = mémoire de retrieval *sans lien*, optimisée KNN/BM25.

Les trois se recouvrent quand on ingère le même document dans les trois. **Règle
d'arbitrage** : le contenu canonique (validé, signé) vit dans Geordi. Le contenu brut
ingéré vit dans TencentDB. Les chunks RAG vivent dans PocketBase. Aucune promotion
automatique entre les trois ; le pont est manuel ou assisté.

### 2.3 Code (call graph, impact) — **TencentDB CodeGraph gagne sur l'automatisme, pocketbase-vec ne couvre pas ce territoire**

| Qui stocke | Quoi | Format |
|---|---|---|
| TencentDB MemoryKnowledge CodeGraph | Symbols, fichiers, calls, impact paths, auto-sync | JSON Hono, SQLite |
| Geordi `04_From_V2_Root/` et `05_From_V2_Domains/` | Code source divers (22 707 .md, dont probablement du code) | MD |

**Décision** : TencentDB CodeGraph détient la **cartographie du code vivant** (celui
qu'on édite, qu'on re-sync). `04_From_V2_Root/`/`05_From_V2_Domains/` sont des **déversements
historiques** (cf. `PLAN_META_MEMOIRE` §1.3), pas une indexation live du code. À ne pas
confondre : un échantillonnage (étape 3 du plan adapté) dira si certains de ces fichiers
méritent une promotion vers TencentDB CodeGraph ou s'ils restent en archive.

### 2.4 Skills / SOP — **TencentDB MemoryCore gagne**

| Qui stocke | Quoi | Format |
|---|---|---|
| TencentDB MemoryCore Skill | Skills versionnés, ressources, triggers, ACLs | JSON Hono |
| Geordi Wiki `concepts/` | Concepts pédagogiques (16 pages, type=`concept`) | MD OKF |
| `06_Claude_Code_Bare/skills/` | Skills Claude Code (registry complet cité Dox ligne 37) | SKILL.md |
| `01_Guides/` (15 560 .md) | Guides premium (Geordi_YT-* et autres) | MD |

**Décision** : quatre familles distinctes.
- **TencentDB Skill** = SOP exécutables, versionnés, avec ACL et exécution tracée.
- **`06_Claude_Code_Bare/skills/`** = skills du harnais Claude Code local, déclenchés
  par slash-commandes.
- **Geordi `concepts/`** = pages *pédagogiques* (Karpathy-style link graph), pas
  exécutables.
- **`01_Guides/`** = corpus YouTube/ressources, canon de référence mais pas skill
  actif.

Les deux premiers (TencentDB Skill + Claude Code skills) **pourraient fusionner un jour**,
mais ce n'est pas le sujet du brief — et un pont automatique entre eux est dangereux :
les skills sont des outils, pas des documents.

### 2.5 Index de tout (méta) — **Geordi `00_Index/` + Agent OS standards/index.yml**

| Qui stocke | Quoi |
|---|---|
| Geordi `00_Index/` (7 fichiers) | Routage 5 branches (OKF/Wiki/Graphify/Dox/ROT), TAGS, RESOURCES_INDEX |
| Geordi `wiki/ROT.md` | Rot-rates S0-S4 |
| Geordi `wiki/index.md` (319 liens) | Index du wiki |
| Agent OS `standards/index.yml` | Index des standards (5 entrées) |
| Agent OS `commands/` | 6 commands (plan-product, shape-spec, etc.) |

**Décision** : Geordi `00_Index/` est l'**autoroute canon** vers les quatre piliers ;
Agent OS `standards/index.yml` est l'autoroute canon **vers les conventions d'écriture**.
Ils ne se recouvrent pas : l'un indexe *ce qu'on sait*, l'autre indexe *comment on écrit*.
**Pas de fusion** ; une cross-référence (étape §5.4) suffit.

### 2.6 ACL et identité — **TencentDB MemoryCore (User/Team/Agent/Task) vs Geordi TAGS.md Owner**

**Décision** : deux registres incompatibles cohabitent, et c'est explicite dans le
`PLAN_META_MEMOIRE` §4.2 (Doctor Who vs Star Trek vs A3 spec). **Tant que le propriétaire
n'a pas tranché (§6.3), aucune fusion possible**. Le présent document ne touche pas
à TAGS.md.

---

## 3. Couches unifiées

Une seule taxonomie qui absorbe les **4 couches Chat Memory** de TencentDB (L0-L3),
les **5 strates S0-S4** de Geordi, et les **2 artefacts vectoriels** de PocketBase
(`chunks` + `embeddings`). Pour chaque couche, six attributs : **quoi · qui écrit · qui
lit · durée · péremption · adresse physique**.

### 3.1 Taxonomie cible — sept couches

| # | Couche | Statut opérationnel | Équivalent TencentDB | Équivalent Geordi | Équivalent PocketBase |
|---|---|---|---|---|---|
| **U0** | **Identité / Lois** (toujours chargé) | Constitution, doctrines, invariants, owner | — (n/a) | S0 + Dox racine (`06_Claude_Code_Bare/CLAUDE.md`, `AGENTS.md`) | — |
| **U1** | **Trace opérationnelle chaude** (≤ 7 j, extraction auto) | Conversation brute, faits extraits, scénarios | L0 Conversation, L1 Atom, L2 Scenario | S1 hand_offs/` + `wiki/log.md` | — |
| **U2** | **Travail en cours** (≤ 7 j, sélection humaine) | Imports non triés, captures, fiches de travail | (peut recevoir L2 Scenario promu) | S2 `_CAPTURE_/`, `_INTAKE/`, projets/memory/ | (peut recevoir `chunks` fraîchement ingérés) |
| **U3** | **Profil & canon chaud** (injection system prompt) | Profils long-terme, persona, équipe | L3 Core / Persona | (pas d'équivalent direct) | — |
| **U4** | **Canon durable / ressource** (revue hebdo) | Pages de concept, ADR, entités | Wiki MemoryKnowledge (ingéré) | S3 L0/, concepts/, entities/, J01-J04, 01_Guides, 09_Life_OS | — |
| **U5** | **Retrieval souverain** (KNN + BM25 local) | Chunks texte + vecteurs, sans graphe | (peut indexer U4 si besoin) | — | `chunks` + `embeddings` + `chunks_fts` |
| **U6** | **Méta / index de tout** (par écriture) | Comment retrouver, rot, owners | — | S4 `00_Index/`, `wiki/index.md`, `wiki/ROT.md` | — |

### 3.2 Détail par couche

#### **U0 — Identité / Lois**
- **Quoi** : constitutions, AGENTS.md canon, ADRs actifs, D1-D8, Owner/Shelf registre.
- **Qui écrit** : A0 (humain), en append-only (D4 doctrine Geordi).
- **Qui lit** : tout agent au boot (cf. Geordi `CLAUDE.md` racine §1, ligne 25).
- **Durée** : lent (cycle 12WY).
- **Péremption** : revue + bump `revue_at:` ; sinon signal d'invariant oublié.
- **Adresse** :
  - `C:/Users/amado/ASpace_OS_V2/00_Amadeus/01_Identity_Core/CONSTITUTION.md`
  - `C:/Users/amado/ASpace_OS_V2/.../03_Resources_Geordi/06_Claude_Code_Bare/CLAUDE.md`
  - `C:/Users/amado/ASpace_OS_V2/.../03_Resources_Geordi/06_Claude_Code_Bare/AGENTS.md`

#### **U1 — Trace opérationnelle chaude**
- **Quoi** : conversations brutes (L0), faits (L1), scénarios (L2) — extraction automatique par pipeline async.
- **Qui écrit** : TencentDB MemoryCore (L0 write-back à chaque tour via MemoryProxy ;
  cf. `MemoryProxy/README.md` ligne 28-29). Geordi `hand_offs/` est signé humain, non automatique.
- **Qui lit** : MemoryProxy injecte L2/L3 directement dans le system prompt ; L0/L1 exposés
  en `<tdai_memory_tools>` (cf. `MemoryProxy/README.md` ligne 64-65).
- **Durée** : ≤ 7 j sans mouvement = signal (cf. ROT §S1).
- **Péremption** : compaction au seuil ; promotion vers U2 ou U4 selon règle des 3 (déjà
  documentée dans `ROT.md`).
- **Adresse** :
  - TencentDB : `~/.memory-tencentdb/memory-tdai` (cf. `MemoryCore/README.md` ligne 48) — non vérifié sur ce poste.
  - Geordi : `.../wiki/hand_offs/` (350 fiches), `.../wiki/log.md`, daily notes.

#### **U2 — Travail en cours**
- **Quoi** : imports bruts non triés, captures GTD, fiches de qualification.
- **Qui écrit** : A0 + agents d'ingest, sous règle Capture-avant-Clarify.
- **Qui lit** : A0 au tri GTD ; agents de qualification.
- **Durée** : ≤ 7 j sans mouvement = `_STALE_<date>` (cf. ROT §S2).
- **Péremption** : promotion vers U3/U4 par règle des 3, OU tag `_STALE_<date>` + route
  vers `04_From_V2_Root/` si hors scope.
- **Adresse** :
  - Geordi : `.../wiki/_CAPTURE_2026-08-01/`, `.../wiki/_INTAKE/`,
    `06_Claude_Code_Bare/projects/C--Users-amado/memory/` (35 fiches).
  - PocketBase : `chunks` fraîchement ingérés avant promotion U4/U5.

#### **U3 — Profil & canon chaud**
- **Quoi** : profils long-terme, persona d'équipe, cognition stable.
- **Qui écrit** : TencentDB MemoryCore (extraction L3 par async pipeline depuis L2).
- **Qui lit** : MemoryProxy injecte en system prompt à chaque tour (cf. `MemoryProxy/README.md`
  ligne 64-65, "Team / Global memory").
- **Durée** : lent (cycle 12WY aligné sur U0).
- **Péremption** : revue manuelle par A0 ; bump `revue_at:`.
- **Adresse** :
  - TencentDB : L3 Core/Persona dans `~/.memory-tencentdb/memory-tdai` (non vérifié).
- **Note** : **Geordi n'a pas d'équivalent direct.** C'est un trou de la taxonomie
  actuelle ; soit A0 admet que le profil chaud n'est *que* chez TencentDB, soit une
  strate U3-Geordi est créée. Tranché en §6.3.

#### **U4 — Canon durable / ressource**
- **Quoi** : concepts, ADR, entités, guides premium, Life Wheel.
- **Qui écrit** : A0 (avec règle des 3) ; LLM d'ingest TencentDB pour documents bruts.
- **Qui lit** : tout agent, à la demande.
- **Durée** : revue hebdo (7 j).
- **Péremption** : 2 revues manquées = flag pour re-tagging ; 90 j sans référence = candidat
  `_TRASH_<date>/`.
- **Adresse** :
  - Geordi : `.../wiki/L0/`, `concepts/`, `entities/`, `J01-J04/`, `01_Guides/`,
    `09_Life_OS/LD01-LD08/`, `02_Templates/`.
  - TencentDB : Wiki MemoryKnowledge (ingest depuis LLM).

#### **U5 — Retrieval souverain**
- **Quoi** : chunks texte + vecteurs 768-dim + index BM25, sans graphe de liens.
- **Qui écrit** : agents d'ingest (hooks PocketBase `bindChunkHooks`) ou script batch.
- **Qui lit** : agents via `POST /api/vec/search` (cf. `pocketbase-vec/search.go`).
- **Durée** : aligné sur la source (U2/U4) ; pas de rot propre.
- **Péremption** : delete cascade via `OnRecordAfterDeleteSuccess` (cf. `hooks.go` ligne 78).
- **Adresse** :
  - PocketBase : `chunks` collection + `embeddings` virtual table + `chunks_fts` virtual table.

#### **U6 — Méta / index de tout**
- **Quoi** : routage, rot, owners, RESOURCES_INDEX.
- **Qui écrit** : regen automatique (`bin/gen_wiki_index.py`), bump à chaque promotion.
- **Qui lit** : tout agent au boot (cf. Geordi `CLAUDE.md` §4 checklist).
- **Durée** : par écriture.
- **Péremption** : jamais (mtime + cohérence ligne).
- **Adresse** :
  - Geordi : `00_Index/`, `.../wiki/index.md`, `.../wiki/ROT.md`, `.../wiki/audits/`.
  - Agent OS : `standards/index.yml`.

### 3.3 Pourquoi 7 couches et pas 4 ou 5

- **Pourquoi pas 4** : réduire à 4 couches forcerait l'amalgame U1 (chaud) et U2 (froid).
  Or ils n'ont ni le même rot, ni le même auteur (auto vs humain), ni la même adresse.
- **Pourquoi pas 5** : amalgamer U3 (profil) avec U0 (identité) ou U4 (canon) masque la
  distinction *injection system prompt* (chaud) vs *lecture à la demande* (froid).
- **Pourquoi U5 est séparé de U4** : U5 a son propre moteur (vec0 + FTS5), son propre
  plafond de capacité (50-100k chunks, cf. `pocketbase-vec/README.md` ligne 69), et
  aucune API rule PocketBase (cf. `search.go` ligne 41-45) — il ne vit pas dans le
  même monde que U4.

### 3.4 Trois absences à signaler

- **Pas de U3-Geordi.** Le profil chaud n'a pas d'adresse dans Geordi. Voir §6.3.
- **Pas d'U0-TencentDB.** La Constitution n'est pas dupliquée chez TencentDB. Bonne
  chose : elle reste l'ancre humaine.
- **Pas d'U6-TencentDB.** Les routes MemoryKnowledge (`/v3/wiki/list` etc.) ne sont
  pas un *index de tout*, elles sont un *catalogue de ce qui est ingéré*. La nuance
  est dans le mot *tout*.

---

## 4. Rôle d'Agent OS — cadre, pas stockage

Ce qu'Agent OS *est*, lu dans son README et ses standards :

> Agent OS helps you shape better specs, keeps agents aligned in a lightweight system
> that fits how you already build. Core capabilities: Discover Standards, Deploy
> Standards, Shape Spec, Index Standards.
> — `agent-os/README.md` ligne 5-15

### 4.1 Ce qu'Agent OS peut porter (et pourquoi c'est légitime)

| Capacité | Pourquoi c'est son job | Limite |
|---|---|---|
| **Indexer les standards** (`standards/index.yml`) | C'est son cœur. 5 entrées aujourd'hui, extensible. | Ne sait pas indexer autre chose que des standards |
| **Injecter les standards au bon moment** (`/inject-standards`) | 3 scénarios : conversation, création skill, planification | Ne décide pas *quels* fichiers canoniques lire — il injecte *ses* standards |
| **Shaper un spec** (`/shape-spec`, `/plan-product`) | Force une structure répétable | Le spec vit ensuite où l'agent le dépose (Geordi, TencentDB, autre) |
| **Découvrir des standards depuis un codebase** (`/discover-standards`) | Pattern mining | Sortie = `.md` à ranger dans `standards/<cat>/` ; Agent OS ne les *éxécute* pas |

### 4.2 Ce qu'Agent OS ne peut PAS porter (et pourquoi)

| Capacité manquante | Pourquoi ça n'est pas son job | Qui doit le porter |
|---|---|---|
| **Stocker des faits, décisions, contexte** | Agent OS n'a pas de base de données ; ses fichiers sont des *conventions*, pas des *contenus*. | TencentDB MemoryCore (U1, U3) |
| **Indexer un graphe de liens** | Sa structure est `standards/<cat>/<file>.md`, plate, sans wiki-link, sans graph. | Geordi Wiki + Graphify |
| **Recherche vectorielle** | Aucun embedding, aucune API de retrieval. | pocketbase-vec (U5) |
| **Routing de questions vers la bonne source** | Pas d'algorithme de routage — `inject-standards` se base sur l'argument explicite de l'utilisateur. | Geordi `00_Index/INDEX_OF_INDEXES.md` + `CLAUDE.md` racine §3 |
| **Gérer la péremption (rot)** | Aucune notion de date de revue dans ses standards. | Geordi `wiki/ROT.md` |

### 4.3 Le rôle précis d'Agent OS dans l'unification

**Agent OS est le registre de conventions que les autres couches respectent quand elles
écrivent.** Concrètement, il porte :

1. **Les standards d'écriture** (`standards/`) — conventions de format, de nommage,
   d'erreur. Ces standards *citent* la taxonomie OKF v0.1 mais ne la dupliquent pas.
2. **Les commandes de façonnage** (`commands/agent-os/`) — `/shape-spec`,
   `/plan-product`, `/inject-standards`. Elles produisent des artefacts qui vont ensuite
   dans Geordi ou TencentDB.
3. **Le profil d'injection par défaut** (`config.yml`) — déclare quel héritage de
   standards applique à un agent donné.
4. **Le pont vers OKF v0.1** — Agent OS est *consommateur* d'OKF, pas *producteur*.
   Ses fichiers `.md` portent un frontmatter compatible mais ne sont pas eux-mêmes
   des bundles OKF.

**Agent OS n'est PAS :**
- une base de données ;
- un wiki ;
- un routeur de questions ;
- un graphe ;
- un moteur de retrieval ;
- un calendrier de péremption.

### 4.4 Cross-référence obligatoire entre Agent OS et Geordi

Une étape du §5 (§5.4) ajoute, dans `agent-os/standards/index.yml`, un champ `geordi_anchor`
pour chaque standard qui réfère une page canon de Geordi. Symétriquement, les pages
Geordi S3 (canon durable) qui définissent une convention portent un champ
`agent_os_standard: <cat>/<file>` dans leur frontmatter. **Aucun code, aucune migration —
juste deux champs YAML en plus, en append-only.**

---

## 5. Chemin par étapes réversibles

Chaque étape vaut seule : si on s'arrête après la deuxième, on doit être en meilleur
état qu'avant. Pas de grand soir. Toute étape qui déplace des fichiers est précédée
d'un `MANIFEST.json` (src → dst) ; déplacer, jamais supprimer.

### Étape 1 — **Audit vivant des services TencentDB**

- **Livrable** : un fichier `AUDIT_TENCENTDB_LIVE_2026-08-XX.md` à la racine de
  `ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/`.
- **Critère de fin** : pour chacun des 4 modules (MemoryCore :8420, MemoryKnowledge :8421,
  MemoryPanel :8123/5173, MemoryProxy :8096), une ligne : `port | running? | volumes
  mesurés | bindings actifs`. Vérifié par `curl -s http://127.0.0.1:<port>/health`.
- **Réversible** : aucune écriture, lecture seule.
- **Dépend de** : rien.
- **Pourquoi d'abord** : on ne peut pas arbitrer la propriété d'une source sans savoir
  si elle tourne et ce qu'elle contient. Ce trou est comblé avant toute autre décision.

### Étape 2 — **Audit vivant de pocketbase-vec**

- **Livrable** : `AUDIT_POCKETBASE_VEC_LIVE_2026-08-XX.md`, même chemin.
- **Critère de fin** : `pbvec.exe serve` lancé sur un port libre, `curl /api/vec/search`
  exécuté sur un terme de test, taille de `chunks` collection mesurée par SQL.
- **Réversible** : le service s'arrête par `Ctrl+C`. Aucune donnée écrite (les chunks
  sont vides par défaut).
- **Dépend de** : rien.
- **Pourquoi d'abord** : idem §1.

### Étape 3 — **MANIFEST de la cross-référence Agent OS ↔ Geordi**

- **Livrable** : `agent-os/memoire/MANIFEST_CROSSREF_AGENTOS_GEORDI.json`, fichier
  neuf créé dans le dossier `agent-os/memoire/` (le brief autorise ce dossier neuf).
- **Format** : `[{ "agent_os_standard": "<cat>/<file>", "geordi_anchor": "<wiki path>",
  "added": "<ISO date>", "reason": "<1 phrase>" }, ...]`.
- **Critère de fin** : ≥ 3 entrées (les 5 standards actuels × ceux qui réfèrent
  effectivement Geordi aujourd'hui — vérification rapide).
- **Réversible** : supprimer le fichier. Aucun déplacement.
- **Dépend de** : rien.
- **Pourquoi maintenant** : c'est l'étape qui crée le dossier neuf autorisé par le
  brief, sans rien casser.

### Étape 4 — **Patch additif Geordi (cross-référence inverse)**

- **Livrable** : patch append-only sur 3 pages S3 de Geordi, ajoutant le champ
  frontmatter `agent_os_standard: <cat>/<file>`.
- **Critère de fin** : 3 fichiers patchés, log dans `wiki/log.md`, diff vérifié.
- **Réversible** : revert via git, ou retirer la ligne ajoutée. Aucun fichier déplacé.
- **Dépend de** : étape 3 (au moins une entrée dans le MANIFEST).
- **Pourquoi maintenant** : le pont Agent OS ↔ Geordi est posé dans les deux sens.

### Étape 5 — **Documenter U3 (Profil chaud) — décision binaire**

- **Livrable** : section datée dans `00_Index/PLAN_META_MEMOIRE_2026-08-01.md`
  append-only (D4) OU nouvelle section dans `ARCHITECTURE_MEMOIRE_UNIFIEE.md`.
- **Critère de fin** : la question `U3 vit-il seulement chez TencentDB, ou faut-il
  créer une strate Geordi ?` reçoit une réponse par A0 (cf. §6.3).
- **Réversible** : c'est une décision, pas un déplacement.
- **Dépend de** : §6.3 résolu par A0.

### Étape 6 — **Pont manuel U4 → U5 (optionnel)**

- **Livrable** : script `tools/ingest_geordi_to_pocketbase.py` dans
  `agent-os/memoire/` (nouveau). Pas exécuté par cette architecture ; seulement décrit.
- **Critère de fin** : description du contrat (quelles pages U4 deviennent chunks, quelles
  métadonnées, quelle fréquence d'actualisation).
- **Réversible** : script jamais exécuté ; pas de fichiers touchés.
- **Dépend de** : décision A0 sur l'opportunité (cf. §6.4).

### Étape 7 — **Évaluation 90 jours**

- **Livrable** : `RAPPORT_REVUE_90J_2026-11-XX.md`, section datée dans le rapport jumeau.
- **Critère de fin** : pour chaque couche U0-U6, une note (1-5) sur adoption effective,
  taux de péremption observé, friction signalée. Décision : continuer, ajuster, abandonner.
- **Réversible** : c'est une évaluation, pas une mutation.
- **Dépend de** : étapes 1-4 exécutées et observées.

### 5.X Dépendances

```
1 ─► 2 (parallèles, indépendants)
3 ─► 4
5 ─► bloqué par §6.3 (décision A0)
6 ─► bloqué par §6.4 (décision A0)
7 ─► 1, 2, 3, 4 au minimum
```

---

## 6. Ce que je refuse de trancher

Quatre décisions restent pendantes, et ce document ne les tranche pas. La raison est
toujours la même : **manque d'autorité ou d'information pour décider en lecture seule**.

### 6.1 Quel service TencentDB reste-t-il vivant ?

**Statut** : non vérifié. Seul MemoryKnowledge :8421 est confirmé vivant par le
`RAPPORT_knowledge_config.md` 2026-08-04. Les trois autres modules peuvent être arrêtés
depuis — la session n'a pas testé les ports :8420, :8123, :8096.

**Question exacte à A0** : « MemoryCore (port 8420), MemoryPanel (8123) et MemoryProxy
(8096) tournent-ils encore ? Si oui, lequel est l'instance de référence ? Si non,
accepte-t-on que TencentDB-Agent-Memory, dans cet écosystème, se réduise à
MemoryKnowledge + un Wiki ingéré + un CodeGraph ? »

### 6.2 Que contient TencentDB MemoryKnowledge ?

**Statut** : 0 mesure pendant cette session. Le rapport du 2026-08-04 montre que
`/v3/wiki/list` répond `items=[]` (ligne 122-123), mais un appel plus tard aurait
pu trouver des wikis. Idem `/v3/code-graph/list` (ligne 124-129).

**Question exacte à A0** : « Avant de parler d'arbitrage de propriété U4, combien de
wikis sont ingérés dans MemoryKnowledge :8421 aujourd'hui, et de quels corpus ? »

### 6.3 U3 (Profil chaud) — TencentDB only ou doublon Geordi ?

**Statut** : aucune adresse Geordi pour U3 dans l'état mesuré. La couche U3 existe dans
la taxonomie TencentDB (L3 Core/Persona, cf. `MemoryCore/README.md` ligne 5), mais
Geordi n'a pas de strate équivalente. `hand_offs/` est S1 (court terme), pas U3.

**Question exacte à A0** : « Accepte-t-on que le profil chaud (persona d'équipe,
cognition stable) n'existe *que* chez TencentDB L3, ou faut-il créer une strate U3-Geordi
(équivalent d'un `entities/` étendu avec date de revue) ? »

**Note** : si A0 choisit l'option "TencentDB only", le présent document devient caduc
sur U3 et la couche U3 est *documentée comme externalisée*. Pas d'action.

### 6.4 Pont U4 → U5 (Geordi canon → PocketBase chunks) ?

**Statut** : optionnel. Aucune preuve dans cette session que les chunks PocketBase
contiennent quoi que ce soit d'utile. La capacité technique existe (768-dim aligné sur
Ollama `embeddinggemma:300m-qat-q8_0`).

**Question exacte à A0** : « Souhaite-t-on un pont qui ingère automatiquement les pages
Geordi S3 dans PocketBase U5, ou reste-t-on sur U5 = corpus séparé ingéré à la main ?
La première option double le travail de maintien ; la seconde préserve la séparation
propre mais demande à l'agent de choisir la source au moment de la requête. »

### 6.5 Trois vocabulaires d'Owner (TAGS.md §4.2)

**Statut** : déjà documenté par le `PLAN_META_MEMOIRE_2026-08-01.md` §4.2 comme
*recommandation à valider par A0, non appliquée*. Ce document ne le tranche pas non
plus — c'est hors scope de l'unification mémoire.

---

## 7. Ce que ce document ne fait pas

- ❌ **Ne touche pas** aux fichiers des quatre sources. Le seul écrit neuf autorisé
  est `agent-os/memoire/MANIFEST_CROSSREF_AGENTOS_GEORDI.json` (étape 3, dossier neuf).
- ❌ **Ne lance aucun service**, ne migre aucune donnée.
- ❌ **Ne pose aucun acte d'exécution**. Toutes les étapes §5 sont des *propositions* ;
  leur déclenchement est une décision A0/Rick, pas un automatisme.
- ❌ **N'installe aucune dépendance**, ne fait aucun `git commit`/`push`.
- ❌ **Ne contredit aucune décision tranchée du PLAN_META_MEMOIRE_2026-08-01.md** :
  la strate U3-Geordi (§6.3) reste pendante, pas tranchée ; le conflit Owner/Shelf
  (§6.5) reste hors scope.

---

## 8. Sources — fichiers réellement ouverts pendant cette session

- `C:/Users/amado/ASpace_OS_V2/.../03_Resources_Geordi/00_Index/PLAN_META_MEMOIRE_2026-08-01.md`
- `C:/Users/amado/ASpace_OS_V2/.../03_Resources_Geordi/00_Index/INDEX_OF_INDEXES.md`
- `C:/Users/amado/ASpace_OS_V2/.../03_Resources_Geordi/00_Index/OKF_INDEX.md`
- `C:/Users/amado/ASpace_OS_V2/.../03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/ROT.md`
- `C:/Users/amado/ASpace_OS_V2/.../03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/index.md` (premiers 100)
- `C:/Users/amado/ASpace_OS_V2/.../03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/graphify-out/GRAPH_REPORT.json`
- `C:/Users/amado/ASpace_OS_V2/.../03_Resources_Geordi/CLAUDE.md` (racine Geordi)
- `C:/Users/amado/ASpace_OS_V2/.../03_Resources_Geordi/06_Claude_Code_Bare/CLAUDE.md` (premiers 100)
- `C:/Users/amado/TencentDB-Agent-Memory/README.md`
- `C:/Users/amado/TencentDB-Agent-Memory/RAPPORT_knowledge_config.md`
- `C:/Users/amado/TencentDB-Agent-Memory/BRIEF_knowledge_config.md`
- `C:/Users/amado/TencentDB-Agent-Memory/CHANGELOG.md`
- `C:/Users/amado/TencentDB-Agent-Memory/MemoryCore/README.md`
- `C:/Users/amado/TencentDB-Agent-Memory/MemoryKnowledge/README.md`
- `C:/Users/amado/TencentDB-Agent-Memory/MemoryPanel/README.md`
- `C:/Users/amado/TencentDB-Agent-Memory/MemoryProxy/README.md`
- `C:/Users/amado/pocketbase-vec/README.md`
- `C:/Users/amado/pocketbase-vec/MANIFEST.json`
- `C:/Users/amado/pocketbase-vec/main.go`
- `C:/Users/amado/pocketbase-vec/search.go`
- `C:/Users/amado/pocketbase-vec/hooks.go`
- `C:/Users/amado/pocketbase-vec/embed.go`
- `C:/Users/amado/pocketbase-vec/migrations/1754280000_vec_embeddings.go`
- `C:/Users/amado/pocketbase-vec/migrations/1754290000_chunks_and_fts.go`
- `C:/Users/amado/pocketbase-vec/justfile`
- `C:/Users/amado/agent-os/README.md`
- `C:/Users/amado/agent-os/config.yml`
- `C:/Users/amado/agent-os/standards/index.yml`
- `C:/Users/amado/agent-os/standards/global/coding-style.md`
- `C:/Users/amado/agent-os/commands/agent-os/inject-standards.md`

Aucun de ces chemins ne contient de secret à motif `sk-`, `sbp_`, `vcp_`, `ghp_`,
JWT, clé PEM, ou `.env` non-exemple (cf. `pocketbase-vec/MANIFEST.json` ligne 25-29
pour le scan déjà effectué côté pbvec — je l'ai vérifié indépendamment et confirme :
aucune clé n'apparaît dans les fichiers que j'ai ouverts).

---

## 9. Historique (D4 append-only)

- **2026-08-06** — Création. Première architecture d'unification tenant compte des
  quatre sources effectivement sur disque, et non des promesses marketing. Sept
  couches U0-U6 ; cinq décisions pendantes ; sept étapes réversibles. Aucune
  exécution.
