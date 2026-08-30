# V3 Memory Doctrine — Pivot 2026-08-16

> **Statut** : PROPOSITION — append-only, à valider par l'utilisateur (loi 0).
> **Auteur** : agent pi (session post-compaction, M3), 2026-08-16

## 1. Constat

La `30_MEMORY_CORE/` d'A'Space OS V3 est une **erreur d'architecture**. Elle contient :

- `META_ONTOLOGIE.md` (24 KB) — la reconstitution des 3 couches
- `META_ONTOLOGIE.json` (57 KB) — données structurées
- `ONTOLOGIE_V1.md` + `ONTOLOGIE_V2.md` — itérations
- `BRIEF_META_ONTOLOGIE.md` + `BRIEF_CARTO_PARA.md` — briefs
- `sessions_md/` — sessions MD converties
- `lance_carto*.sh` (×4) — scripts de cartographie PARA
- `jsonl_vers_md.py` — convertisseur
- `journal_carto*.log` (×16) — logs

**Ce contenu est de la mémoire.** Il n'a rien à faire dans `00_Amadeus/`, qui est la racine d'**identité** (Identity Core). La mémoire canonique d'A'Space OS V2 est `Geordi/03_Resources_Geordi/`, pas un dossier V3 privé.

## 2. Doctrine

**La mémoire long terme d'A'Space OS canonique = OpenWiki + OKF 0.2 + DOX.**

| Couche | Outil | Rôle | Chemin |
|---|---|---|---|
| Format pivot | **OKF 0.2** | schema + 5 trust signals | Frontmatter de chaque wiki page |
| Mémoire long terme | **OpenWiki 0.2** | wiki engine (Karpathy LLM Wiki standardisé) | `~/.openwiki/wiki/` |
| Mémoire de travail | **DOX** (agent0ai) | self-doc AGENTS.md hierarchy | Racine V3 + 5 child |
| Source canonique Geordi | **Geordi V2** | ressources canoniques historiques | `ASpace_OS_V2/.../03_Resources_Geordi/` |
| Pont FTS5 / DIKW | **context-mode** | indexation locale + retrieval | FTS5 sqlite (`~/.pi/agent/...`) |

**Trace canonique** : `30_MEMORY_CORE/` doit **retourner** dans Geordi V2, en tant que ressources canoniques archivées.

## 3. Plan de migration (D4 append-only)

1. **Créer** `ASpace_OS_V2/03_Resources_Geordi/10_From_V3_Memory_Core/` (nouveau bucket `From_V3_Memory_Core`).
2. **Copier** (D4 : `cp`, pas `mv`) le contenu de `30_MEMORY_CORE/` vers `10_From_V3_Memory_Core/`.
3. **Reformater** en OKF 0.2 (frontmatter `type`, `title`, `description`, `tags`, `timestamp`, `sources`, `generated`, `verified`).
4. **Indexer** dans OpenWiki via un connecteur `git-repo` (avec patch pour maxBuffer) ou via context-mode FTS5.
5. **Déréférencer** `30_MEMORY_CORE/` de V3 : transformer en symlink ou en stub expliquant la migration.
6. **Append historique** dans `AGENTS.md` pi + V3.

## 4. Pourquoi cet ordre

1. **D4 append-only** : on n'efface pas, on ajoute. La copie est réversible.
2. **DIKW** : Data (META_ONTOLOGIE.md) → Information (OKF frontmatter) → Knowledge (Geordi + OpenWiki wiki) → Wisdom (DOX self-doc).
3. **Cohabitation pi/V3** : la mémoire vit à un seul endroit canonique (Geordi + OpenWiki), pas éparpillée entre 3 sources.

## 5. Risques identifiés

- **R1** : la copie peut dupliquer ~6 MB de fichiers. D4 : conserver le checksum et un MANIFEST.json.
- **R2** : OpenWiki TUI bloque en one-shot mode. D7 : pas de bloquer, faire en mode message direct.
- **R3** : connecteur git-repo cassé (maxBuffer). D7 : workaround via mini-repo git dédié ou via context-mode FTS5.
- **R4** : la mémoire V3 contient des **sessions_md** qui sont des transcriptions. **D1 verify-before-assert** : ce contenu est-il canonique ou volatile ? Si volatile, le verser dans Geordi `transcripts_raw/` (le bucket `_transcripts_raw` existe déjà).

## 6. Statut actuel (2026-08-16)

- ✅ Constat posé (cette doctrine)
- ✅ OpenWiki 0.2 installé et configuré (`~/.openwiki/.env` + `connectors/git-repo/config.json` + `onboarding.json`)
- ✅ Wiki OpenWiki générée (quickstart.md, _plan.md, openwiki/index.md)
- ✅ DOX tree initialisé (root V3 + 5 child AGENTS.md)
- ✅ Context-mode FTS5 : 19 docs indexés, 458 events, 33 files tracked
- ⏳ Bug git-repo connector maxBuffer sur Geordi (non-git) en cours de contournement
- ⏳ 5 cibles `.claude/` à indexer (sessions, projects, plans, channels, skills)
- ⏳ Migration `30_MEMORY_CORE/` → Geordi `10_From_V3_Memory_Core/` (à valider)

## 7. Cross-references

- Root V3 AGENTS.md : ../../AGENTS.md
- OpenWiki : ~/.openwiki/wiki/quickstart.md
- Geordi canon : ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/
- DOX child : ./AGENTS.md
- Historique pi : ~/.pi/agent/AGENTS.md §9
