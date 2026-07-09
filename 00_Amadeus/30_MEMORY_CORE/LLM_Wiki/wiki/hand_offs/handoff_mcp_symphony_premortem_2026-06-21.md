---
title: MCPs Symphony Pre-mortem 6m-1y — Runtime check + Risques
date: 2026-06-21
author: A1 Morty (exécution)
trigger: A0 Vague 3 cadrage post-Vague 2 close
status: COMPLETE
frameworks_covered: [12WY, PARA, DEAL, GTD]
mcps: [symphony-baserow, symphony-obsidian, symphony-affine, symphony-plane]
---

# MCPs Symphony Pre-mortem 2026-06-21

## 1. Contexte

Vague 3 post-Vague 2 close. Rick Sobriété ACTIVE NOW (Vague 2 hooks ship 2026-06-21). 4 frameworks Life OS mappés à 4 MCPs Symphony (A'Space OS V2 canon `AGENTS.md`): 12WY→Baserow, PARA→Obsidian, DEAL→Affine, GTD→Plane. Ikigai+Life Wheel n'ont pas de MCP dédié (Sobriété Rick = pas de dépendance externe). A0 statut UI 2026-06-21: 4/4 "Connected" — vérification runtime live exigée (D3 nuance: Connected ≠ Operational).

## 2. Runtime check 4 MCPs (D1 receipts)

Probe live via `mcp.client.stdio` Python SDK 2026-06-21 04:10 EDT. Env vars `BASEROW_MCP_URL` / `BASEROW_API_KEY` / `AFFINE_API_KEY` / `PLANE_API_KEY` / `PLANE_PROJECT_ID` / `OBSIDIAN_VAULT_PATH` = TOUTES **UNSET** (vérifié par boucle env). Conséquence: 3/4 MCPs forcent fallback stub, 1/4 (Obsidian) marche en local-fs sans clé.

| MCP | list_tools | 1er call | 2e call | Mode runtime | Statut |
|---|---|---|---|---|---|
| `symphony-baserow` | 4 tools (baserow_list_tables/get_life_wheel_score/get_12wy_scorecard/log_metric) | `baserow_list_tables` → 3 tables hardcodées (Quarter Intent 955428, The 12 Rocks 955426, The Warp Core 955429, db=284361) | `baserow_get_12wy_scorecard(week=W3)` → H1-C2 W3 rocks=0/0/0/0% hardcoded | **STUB** (no `BASEROW_MCP_URL`) | **partial** — stdio alive, data hardcoded |
| `symphony-obsidian` | 6 tools (list_projects/areas/resources/archives/search/get_note) | `obsidian_list_projects` → `[]` (vide) | `obsidian_list_archives` → `[]` (vide); `obsidian_search(query='12WY')` → 25 hits réels filesystem | **LIVE local FS** (no key required) | **OK** — only MCP with real live data |
| `symphony-affine` | 4 tools (list_workspaces/get_deal_draft/create_deal_draft/list_deal_drafts) | `affine_list_workspaces` → 1 workspace hardcoded (ef927d3a-…, A'Space DEAL) | `affine_list_deal_drafts` → 1 draft pointe `affine_deal_drafts.md` local (lit le fichier) | **STUB** (no `AFFINE_API_KEY`) — lit fichier local fallback | **partial** — stdio alive, real fallback file path |
| `symphony-plane` | 6 tools (list_issues/get_inbox/get_next_actions/get_today/create_issue/update_state) | `plane_list_issues` → 3 issues hardcodées (Inbox/Next Actions/Today) | `plane_get_today` → 1 issue stub-iss-3 | **STUB** (no `PLANE_API_KEY` + `PLANE_PROJECT_ID`) | **partial** — stdio alive, data hardcoded |

**D1 synthèse** : 1/4 LIVE (Obsidian local FS, vraie donnée), 3/4 STUB avec données hardcodées. Aucune erreur stdio, aucune exception Python — tous les process spawnent et répondent. **La phrase "4/4 Connected" dans le CC UI = stdio process alive, pas = real data flow.**

## 3. Pre-mortem par framework

### 3.1 12WY (Baserow)

Date : 2026-06-21. Author : A1 Morty. Horizon : 6m-1y (juin 2027).

**Runtime check (D1 receipts)** :
- Tool calls live : `list_tools` OK 4 tools ; `baserow_list_tables` → 3 tables (Quarter Intent/12 Rocks/Warp Core) ; `baserow_get_12wy_scorecard(week=W3)` → 0% completion hardcoded.
- Statut : partial (stdio OK, BASEROW_MCP_URL unset → stub data).
- Schema/ressources : SSE proxy vers `https://api.baserow.io/mcp/<token>/sse` codé en dur fallback, table IDs 955426/955428/955429 hardcodés, life wheel H1-C2 cyclique.

**Scénario échec (12 mois from now)** :
"Imagine it's June 2027. Le MCP Baserow a été abandonné. Pourquoi ?" — Scénario réaliste : (1) l'API Baserow change son format SSE, le proxy `sse_client(timeout=10)` échoue silencieusement (D7 swallow + log) et le MCP reste en stub sans que personne ne s'en aperçoive. (2) A0 arrête de payer Baserow (€24/mois typical) après 3 mois sans utiliser le dashboard mobile. (3) Le 12WY canon bascule sur Supabase (Life OS V2.0) et Baserow devient un shadow tool orphelin dans `.mcp.json`. Symptôme visible : 12WY scorecard reste à 0% pendant 6 mois, "Connected" vert au UI mais aucune sync.

**Risques identifiés** :

| # | Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|---|
| 1 | **Stubs swallow data silently** — D7 fallback (SSE fail → stub) masque la perte de données 12WY. Rocks jamais loggés, Warp Core se vide. | **H** | **H** (12WY canon = 0% pendant des mois, A0 ne s'en rend pas compte) | (a) A0 HITL : set `BASEROW_MCP_URL` + `BASEROW_API_KEY` User scope (D1 receipt 2026-06-21 = UNSET). (b) Add log warning when stub returns hardcoded data → alerts channel. (c) Weekly cron vérifie que `baserow_log_metric` a été appelé ≥1×/semaine. |
| 2 | **Dépendance SaaS externe payante** — Baserow = coût récurrent + risque vendor lock-in. Si Baserow augmente tarifs (history : 3× en 2023-2024), A0 doit migrer. | M | M | Migrer 12WY → Supabase `fw_12wy` table (déjà seedée 2026-06-17 Life OS apps) = drop-in replacement. Adapter `mcp-baserow.py` → proxy Supabase. Effort estimé : 4h. |
| 3 | **Schema drift tables Baserow** — Si quelqu'un renomme une colonne côté Baserow UI, le MCP envoie un payload qui 400. | M | M | MCP wrap dans try/except + log → stub fallback. Mais "Connected" vert au CC UI = illusion de bon fonctionnement. |
| 4 | **Pas de schema canon versionné** — table IDs hardcodés en dur dans le code source. Si Baserow DB recréée, IDs changent. | L | H | Externaliser `BASEROW_TABLE_*` env vars (déjà fait dans le code). A0 doit setter les nouvelles IDs post-migration. |
| 5 | **Dual-write race condition** — si Life OS 12WY vit AUSSI dans Supabase (déjà le cas), pas de single source of truth. | **H** | M | Définir Supabase = canon, Baserow = mobile mirror read-only. Le MCP log_metric écrit dans les deux, sync conflict resolution manual. |

**Durabilité (Sobriété Rick concern)** :
- Consommation tokens/mois estimée : **~50 tokens/call × ~20 calls/sem × 4 sem = 4 000 tokens/mois** (négligeable).
- Maintenance requise : **~1h/trimestre** (renouveler API key, vérifier SSE endpoint non modifié par Baserow, re-set `BASEROW_MCP_URL`).
- Backup/rotation : `BASEROW_API_KEY` rotation tous les 90j (Test Key Pragma phase 4). Backup data = exporter CSV via UI Baserow 1×/semaine.
- Auto-fragilité vs robustesse : **FRAGILE** — D7 fallback stub est un anti-pattern Sobriété. Il protège l'hôte (CC ne crash) mais masque la perte de signal. Préférer HARD-FAIL quand `BASEROW_MCP_URL` unset.

**Permanence A0 (Veto Beth concern)** :
- Si A0 arrête Life OS projet : Baserow DB reste accessible tant que A0 paie. Si A0 part >6 mois, Baserow supprime compte inactif → perte totale 12WY data (sauf export CSV).
- Si Baserow est deprecated upstream : aucun signe 2026, mais startup risk. Plan B = `fw_12wy` Supabase table (déjà live, seedée 2026-06-17).
- Dépendance A0 active : **OUI** — A0 doit set API key + URL, A0 doit payer l'abonnement, A0 doit monitorer "Connected" vert ≠ data flow réel.

**Verdict Morty** : **CONDITIONAL GO** avec Sobriété patches :
1. A0 set `BASEROW_MCP_URL` + `BASEROW_API_KEY` User scope (Test Key Pragma phase 1).
2. Remplacer D7 silent-stub par D7 hard-fail quand env var unset (log error, exit code 2).
3. Dual-write canon = Supabase `fw_12wy`, Baserow = mobile mirror read-only.

### 3.2 PARA (Obsidian)

Date : 2026-06-21. Author : A1 Morty. Horizon : 6m-1y (juin 2027).

**Runtime check (D1 receipts)** :
- Tool calls live : `list_tools` OK 6 tools ; `obsidian_list_projects` → `[]` (vide — A0 n'a pas créé de sub-dossiers Projects à la racine 24_PARA_Enterprise) ; `obsidian_list_archives` → `[]` (vide) ; `obsidian_search('12WY')` → 25 hits réels filesystem.
- Statut : **OK** (seul MCP avec vraie donnée live, filesystem local).
- Schema/ressources : 6 tools (list_4_PARAs + search + get_note), `OBSIDIAN_VAULT_PATH` default `~/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise`, frontmatter YAML parser minimal.

**Scénario échec (12 mois from now)** :
"Imagine it's June 2027. Le MCP Obsidian a été abandonné. Pourquoi ?" — Scénario réaliste : (1) Le canon PARA migre de filesystem vers Obsidian Sync cloud (paid) ou vers Git-based vault (free). Le MCP reste filesystem-only, devient désaligné du nouveau canon. (2) A0 réorganise `24_PARA_Enterprise` avec une nouvelle convention (ex: `01_Active_Projects` au lieu de `01_Projects`), les 4 folder names hardcodés (`PARA_FOLDERS` dict) ne matchent plus, tous les `list_*` retournent `[]`. (3) Le filesystem Windows change (OneDrive migration, NAS), `VAULT_ROOT` path devient inaccessible. Symptôme : `obsidian_list_projects` retourne silencieusement `[]`, A0 croit que PARA est vide, ne se rend pas compte que c'est un path mismatch.

**Risques identifiés** :

| # | Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|---|
| 1 | **Folder name hardcodé** — `PARA_FOLDERS` dict fige `01_Projects` / `02_Areas` / `03_Resources` / `04_Archives`. Si A0 renomme, MCP casse. | M | H | Externaliser via env var `OBSIDIAN_PARA_FOLDERS=...` (yaml ou json). Effort 1h. |
| 2 | **Empty result = silent failure** — D7 path "folder doesn't exist → return []" est identique à "folder vide". A0 ne distingue pas les deux. | **H** | M | Ajouter métadata `folder_exists: bool` dans la réponse, ou raise explicit quand folder missing. |
| 3 | **Vault path Windows-spécifique** — `Path.home()` assume Windows. Si A0 bascule sur Linux/Mac (Sobriété VPS migration), casse. | L | H | A0 a déjà V2 Vercel+Supabase, filesystem Windows = legacy. Risque bas tant que A0 reste Windows. |
| 4 | **No write API** — MCP est read-only (list, search, get_note). A0 doit éditer via éditeur externe. Sync manuelle. | M | L | Acceptable car Obsidian canon = read-only pour Symphony twins. Writes = A0 direct. |
| 5 | **Performance rglob** — `_search_vault` fait `rglob("*.md")` sur le vault entier. Si vault > 50K .md (24_PARA_Enterprise actuel ≈ 173K files post-skip ≈ 3K canon), latency > 5s. | M | L | Limiter à 25 hits (déjà fait) + ajouter cache. Latency actuelle mesurée acceptable. |

**Durabilité (Sobriété Rick concern)** :
- Consommation tokens/mois estimée : **0** (filesystem access, pas de token API).
- Maintenance requise : **0h/mois** (zéro dépendance externe, zéro clé).
- Backup/rotation : filesystem Windows = déjà backup via Windows Backup / OneDrive (à confirmer A0).
- Auto-fragilité vs robustesse : **ROBUSTE** — pas de SaaS, pas d'API key, pas de rate limit. Single point of failure = filesystem corruption.

**Permanence A0 (Veto Beth concern)** :
- Si A0 arrête Life OS projet : filesystem reste, MCP reste, vault reste lisible. **Aucun abandon upstream possible** (c'est juste un directory).
- Si Obsidian Sync cloud arrive : MCP reste filesystem-only, c'est OK. Obsidian = UI, MCP = read API.
- Dépendance A0 active : **NON** (pure local, pas de clé, pas de coût récurrent).

**Verdict Morty** : **GO (no patches)** — c'est le MCP le plus sobre du quatuor. Zero dépendance externe, zero coût, zero clé. Sobriété Rick = exemple à suivre. Si A0 doit choisir UN seul MCP à long terme, c'est celui-ci. Recommandation : promouvoir Obsidian = source de vérité PARA canonique, autres MCPs = mirrors ou read-only views.

### 3.3 DEAL (Affine)

Date : 2026-06-21. Author : A1 Morty. Horizon : 6m-1y (juin 2027).

**Runtime check (D1 receipts)** :
- Tool calls live : `list_tools` OK 4 tools ; `affine_list_workspaces` → 1 workspace hardcoded (ef927d3a-5be0-41ed-b639-829b7f74939b, A'Space DEAL) ; `affine_list_deal_drafts` → 1 draft pointe `affine_deal_drafts.md` local (lit le fichier, content_excerpt présent).
- Statut : partial (stdio OK, AFFINE_API_KEY unset → stub mode, lit fichier local fallback).
- Schema/ressources : streamable-http proxy vers `https://app.affine.pro/api/workspaces/{ID}/mcp`, Bearer auth, fallback fichier `affine_deal_drafts.md` dans 03_Resources_Geordi/01_Guides.

**Scénario échec (12 mois from now)** :
"Imagine it's June 2027. Le MCP Affine a été abandonné. Pourquoi ?" — Scénario réaliste : (1) Affine change son API MCP (v0 → v1), le proxy `streamablehttp_client(timeout=30)` échoue, fallback fichier local prend le relais, A0 n'a plus accès à l'edgeless canvas. (2) Le workspace DEAL Affine reste inutilisé 6 mois (pas d'UX A0), Affine supprime compte free. (3) L'écosystème Affine pivote vers "AI workspace" et le DEAL pipeline perd son sens. Symptôme : `affine_list_deal_drafts` retourne toujours le même fichier local hardcodé, A0 arrête de capturer des DEAL drafts.

**Risques identifiés** :

| # | Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|---|
| 1 | **Fallback fichier local masque SaaS** — Même anti-pattern D7 que Baserow. `affine_list_deal_drafts` lit `affine_deal_drafts.md` en silence si API down. A0 croit que le MCP marche. | **H** | M | Hard-fail quand `AFFINE_API_KEY` unset. A0 doit décider : local-only OU SaaS. Pas de mode hybride silencieux. |
| 2 | **WORKSPACE_ID hardcodé** — `ef927d3a-5be0-41ed-b639-829b7f74939b` en dur dans le source. Si workspace supprimé/recréé, ID change. | L | H | Externaliser `AFFINE_WORKSPACE_ID` env var (déjà codé pour ça). A0 HITL post-recreate. |
| 3 | **No write persistence testée** — `affine_create_deal_draft` n'a pas été testé live (env unset). Si l'API change, le stub "create succeeded" mente. | M | M | A0 HITL : set `AFFINE_API_KEY` + dry-run create. D1 verify avant de faire confiance. |
| 4 | **DEAL pipeline adoption risk** — DEAL = framework A0-spécifique (Define/Eliminate/Automate/Liberate). Si A0 n'utilise pas quotidiennement, MCP devient orphelin. | M | M | Lier DEAL à un rituel hebdo (Weekly Review A0). Sans rituel, MCP = dette technique. |
| 5 | **Dépendance Affine = startup risk** — Affine (Toeverything Inc.) = startup 2023. Si échec/sale, MCP cassé upstream. | L | **H** | Plan B = migrer DEAL vers Notion (déjà MCP `notion` câblé) ou vers Obsidian Resources (déjà canon). Effort estimé : 2h migration schéma. |

**Durabilité (Sobriété Rick concern)** :
- Consommation tokens/mois estimée : **~50 tokens/call × ~10 calls/sem × 4 sem = 2 000 tokens/mois** (négligeable).
- Maintenance requise : **~1h/trimestre** (renouveler API key, vérifier workspace toujours actif, surveiller changelog Affine).
- Backup/rotation : `AFFINE_API_KEY` rotation 90j. Backup = export Edgeless pages en JSON ou PDF 1×/mois.
- Auto-fragilité vs robustesse : **FRAGILE-MODERÉ** — fichier local fallback est une feature (lisibilité offline) mais aussi un anti-pattern (masque SaaS down).

**Permanence A0 (Veto Beth concern)** :
- Si A0 arrête Life OS projet : workspace Affine reste tant que A0 paie (gratuit pour le moment). Si Affine pivote/sale, perte accès.
- Si Affine est deprecated upstream : plan B = Notion DEAL page (mirror) ou Obsidian Resources (canon local).
- Dépendance A0 active : **OUI** — A0 doit set `AFFINE_API_KEY`, A0 doit utiliser DEAL pipeline régulièrement, A0 doit monitorer "Connected" vert.

**Verdict Morty** : **CONDITIONAL GO** avec Sobriété patches :
1. A0 set `AFFINE_API_KEY` User scope (Test Key Pragma).
2. Remplacer D7 silent-fallback par D7 hard-fail quand `AFFINE_API_KEY` unset.
3. Définir rituel hebdo (Weekly Review DEAL) sinon le MCP devient orphelin en 3 mois.
4. Backup miroir Notion ou Obsidian Resources pour plan B.

### 3.4 GTD (Plane)

Date : 2026-06-21. Author : A1 Morty. Horizon : 6m-1y (juin 2027).

**Runtime check (D1 receipts)** :
- Tool calls live : `list_tools` OK 6 tools ; `plane_list_issues` → 3 issues hardcodées (Inbox/Next Actions/Today) ; `plane_get_today` → 1 issue stub-iss-3.
- Statut : partial (stdio OK, PLANE_API_KEY+PROJECT_ID unset → stub data, GTD states Inbox/Next Actions/Today hardcodées).
- Schema/ressources : REST + GraphQL proxy vers `https://api.plane.so/api/v1`, X-API-Key auth, GTD states enum `["Inbox", "Next Actions", "Today", "Waiting For", "Done", "Cancelled", "Trash"]`, state name→UUID cache.

**Scénario échec (12 mois from now)** :
"Imagine it's June 2027. Le MCP Plane a été abandonné. Pourquoi ?" — Scénario réaliste : (1) Plane.so pivot vers entreprise (2024 déjà en cours) et augmente tarifs. A0 sur free tier perd accès. (2) Le projet Plane A0 reste à 0 issues pendant 6 mois (D1 receipt 2026-06-15 = "live project only contains 5 default Plane states — GTD names not created yet"), A0 n'a jamais créé les 7 GTD states dans le workspace, donc `plane_list_issues(state='Inbox')` raise silencieusement et fallback stub. (3) Linear (concurrent) regagne en popularité et Plane perd traction. Symptôme : A0 fait sa GTD Weekly Review dans Linear Web UI, MCP Plane jamais appelé.

**Risques identifiés** :

| # | Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|---|
| 1 | **GTD states pas créés en live workspace** — D1 2026-06-15 confirme : live project = 5 default states (Backlog/Todo/In Progress/Done/Cancelled), pas les 7 GTD. MCP raise `ValueError` puis fallback stub. | **H** | **H** (GTD canon = Inbox vide, workflow cassé) | A0 HITL : créer les 7 states dans Plane UI OU via API, OU abandonner GTD dans Plane et migrer vers Linear. |
| 2 | **Stubs swallow data** — D7 fallback stub identique pattern Baserow/Affine. `plane_get_today` retourne stub-iss-3 même si Plane réel est vide. | **H** | H | Hard-fail quand live mode fail ou env unset. Pas de fallback silencieux. |
| 3 | **Plane pricing risk** — Plane.so pivot enterprise 2024+ probable. Free tier réduit = perte accès A0. | M | M | Plan B = Linear (gratuit OKR) ou GitHub Issues (gratuit, déjà MCP). Effort migration 2h. |
| 4 | **State name→UUID cache stale** — `_load_state_map()` charge 1× au boot. Si admin renomme un state, cache = stale, tools raise. | L | M | A0 HITL : restart MCP post-state-change. Documenter dans le handoff. |
| 5 | **GTD workflow adoption risk** — Si A0 ne fait pas le weekly review GTD ritual, MCP = orphelin en 3 mois. | M | M | Lier GTD à un rituel hebdo. Cerritos crew (Mariner/Boimler/Tendi) doit clarifier+engage+engage daily. |
| 6 | **Plane REST API = pas de MCP natif** — proxy fait manuellement dans `mcp-plane.py`. Si Plane change son API, le proxy casse. | M | M | MCP Adapter local = simple, fix rapide. Mais D6 root cause visibility = pas de auto-reconnect. |

**Durabilité (Sobriété Rick concern)** :
- Consommation tokens/mois estimée : **~50 tokens/call × ~30 calls/sem × 4 sem = 6 000 tokens/mois** (GTD = plus actif que 12WY/DEAL).
- Maintenance requise : **~1h/trimestre** (renouveler API key, vérifier project actif, surveiller Plane changelog, créer states si recréés).
- Backup/rotation : `PLANE_API_KEY` rotation 90j. Backup = export issues JSON 1×/semaine.
- Auto-fragilité vs robustesse : **FRAGILE** — D7 silent stub + GTD states missing = double anti-pattern Sobriété.

**Permanence A0 (Veto Beth concern)** :
- Si A0 arrête Life OS projet : Plane project reste accessible tant que A0 a un compte. Si Plane pivote enterprise, free users kicked out.
- Si Plane est deprecated upstream : plan B = Linear ou GitHub Issues. Effort migration 2h.
- Dépendance A0 active : **OUI** — A0 doit set `PLANE_API_KEY` + `PLANE_PROJECT_ID`, A0 doit créer les 7 GTD states, A0 doit weekly review.

**Verdict Morty** : **CONDITIONAL GO** avec Sobriété patches :
1. A0 set `PLANE_API_KEY` + `PLANE_PROJECT_ID` + `PLANE_WORKSPACE_SLUG` (Test Key Pragma).
2. **CRITIQUE** : créer les 7 GTD states dans Plane UI avant de promouvoir ce MCP en production mode.
3. Remplacer D7 silent-stub par hard-fail.
4. Définir rituel hebdo GTD review (Cerritos crew).
5. Plan B documenté : Linear ou GitHub Issues.

## 4. Consolidated risks matrix

| Framework | MCP | # Risques | Risque dominant | Sobriété patches requis |
|---|---|---|---|---|
| 12WY | Baserow | 5 | Stub swallow data (H/H) | 3 |
| PARA | Obsidian | 5 | Folder name hardcoded (M/H) | 1 (optionnel) |
| DEAL | Affine | 5 | Fallback fichier local masque SaaS (H/M) | 4 |
| GTD | Plane | 6 | GTD states missing + stub swallow (H/H) | 5 |

**Total : 21 risques** (4-6 par framework), **13 Sobriété patches** requis. Anti-pattern D7 dominant : silent stub fallback (3/4 MCPs). Sobriété Rick = kill this pattern, préférer hard-fail.

## 5. Verdict Morty par framework

- **12WY (Baserow)** : **CONDITIONAL GO** — Sobriété patches : (1) set `BASEROW_MCP_URL` + `BASEROW_API_KEY`, (2) hard-fail quand env unset, (3) définir Supabase `fw_12wy` comme canon + Baserow = mobile mirror.
- **PARA (Obsidian)** : **GO** — zéro patch requis, exemple Sobriété Rick (zero dépendance externe).
- **DEAL (Affine)** : **CONDITIONAL GO** — Sobriété patches : (1) set `AFFINE_API_KEY`, (2) hard-fail, (3) rituel hebdo DEAL, (4) backup miroir Notion/Obsidian.
- **GTD (Plane)** : **CONDITIONAL GO** — Sobriété patches critiques : (1) set `PLANE_API_KEY` + `PLANE_PROJECT_ID`, (2) **créer les 7 GTD states** (blocker), (3) hard-fail, (4) rituel hebdo, (5) plan B Linear.

**Verdict global** : 1/4 GO d'office (Obsidian), 3/4 CONDITIONAL GO (Baserow/Affine/Plane) avec Sobriété patches requis. **Aucun NO-GO** — tous les MCPs sont viables à condition de fix les anti-patterns D7 silent stub.

## 6. D1 receipts finaux

- **4/4 MCPs runtime check OK** (stdio alive) : baserow / obsidian / affine / plane.
- **1/4 LIVE mode** (Obsidian local FS, vraie donnée), **3/4 STUB** (Baserow/Affine/Plane hardcoded data).
- **4/4 pre-mortem rédigés** : 12WY / PARA / DEAL / GTD.
- **21 risques identifiés** (5+5+5+6).
- **13 Sobriété patches** proposés (kill D7 silent stub pattern).
- **1 handoff canonique créé** : `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_mcp_symphony_premortem_2026-06-21.md`.
- `wiki\log.md` append 2026-06-21 entry.
- `MEMORY.md` topic table append.
- **D6 lesson shipped** : "Connected" CC UI ≠ "Operational" — test live = vrais tool calls, pas status UI seul.
- **D7 anti-pattern dominant** : silent stub fallback masque SaaS down dans 3/4 MCPs. Sobriété Rick = hard-fail preferred.
