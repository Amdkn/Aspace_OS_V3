---
source: A0 Amadeus (jumeau numérique)
date: 2026-06-21
type: handoff
domain: cross
tags: [saas, cloud, mcp, baserow, affine, obsidian, plane, stabilisation]
---

# Handoff — 4 SaaS Cloud Activated (Vague 4 pivot A0 « PAR STABILITÉ »)

> **Date** : 2026-06-21
> **Auteur** : A0 Amadeus (Jumeau Numérique) — méta-orchestration
> **Statut** : LIVE pour 3/4, ready-LIVE pour Plane (CC restart A0 HITL)
> **Hash** : `saas_cloud_activated_2026-06-21_v4_pivot_stabilite`

## 1. Contexte — pivot A0 « PAR STABILITÉ »

### 1.1 Demande A0 verbatim

> « j'AI DECIDER PAR STABILITE D'ADOPTR LES VERSION CLOUD DU SUPABASE AUTANT QUE POUR IKIGAI ET LIFE WHHEL PAR SUPABASE POUR LE FOCUS DE MORTY LES A2 DE SNW sur Baserow Cloud, Obsidiant Cloud, Affine et Plane pour leurs version Cloud avant les Self Hosted »

### 1.2 Doctrine appliquée

- **A0 = board observer prérogative** (méta-orchestration, jamais B3 technicien)
- **Rick Sobriété kernel** activé 2026-06-21 (veto exercé NO-GO Affine + Beth NO-GO Plane → A0 override pour stabilité)
- **Test Key Pragma** : A0 a exposé les tokens dev en clair dans `.mcp.json` exprès pour discovery (pas de re-share demandé)
- **D1 verify-before-assert** : tous les status runtime capturés par appels MCP réels + 1 curl REST Plane API discovery

## 2. Mapping final 6 frameworks Life OS

| A1 Gatekeeper | A2 Ship | Framework | A3 Spécialiste | SaaS cible | Status runtime |
|---|---|---|---|---|---|
| A1 Beth (Veto) | USS Orville | Ikigai 9 | Ed/Kelly/Gordon/Klyden | **Supabase Cloud** | ✅ LIVE (Sobriété+++) |
| A1 Beth (Veto) | USS Discovery | Life Wheel 8 LD01-LD08 | Book/Saru/Burnham | **Supabase Cloud** | ✅ LIVE (Sobriété+++) |
| A1 Beth (Veto) | USS Protostar | DEAL Muse 4H | Dal/Rok-Tahk/Zero/Gwyn | **Affine Cloud** | ✅ LIVE edgeless |
| A1 Morty (Focus) | USS SNW Curie | 12WY 5 disciplines | Pike/Una/Chapel/M'Benga/Ortegas | **Baserow Cloud** | ✅ LIVE SSE (DB 284361) |
| A1 Morty (Focus) | USS Enterprise Computer | PARA 4 | Picard/Spock/Geordi/**Data** | **Obsidian Local FS** | ⚠️ LOCAL (D3 nuance) |
| A1 Morty (Focus) | USS Cerritos Holo Deck | GTD 5 | Mariner/Boimler/Tendi/Freeman/Rutherford | **Plane Cloud** | ⏳ LIVE ready (CC restart) |

## 3. D1 receipts runtime — 4 SaaS MCPs

### 3.1 Baserow Cloud (12WY) — ✅ LIVE SSE

**Mode** : SSE proxy via `BASEROW_MCP_URL` (pas REST legacy).
**Env vars User scope** :
- `BASEROW_API_KEY` = `ewFGHw9klIsE...` (32 chars)
- `BASEROW_MCP_URL` = `https://api....` (63 chars)
- `BASEROW_DATABASE_ID` = `<EMPTY>` (non requis en SSE mode)

**Runtime receipt** (`mcp__symphony-basero w__baserow_list_tables`) :
```json
[
  {"id": "955428", "name": "Quarter Intent", "database_id": "284361", "purpose": "Quarterly vision per A'Space layer (L0/L1/L2)"},
  {"id": "955426", "name": "The 12 Rocks", "database_id": "284361", "purpose": "Quarterly concrete objectives (12 max)"},
  {"id": "955429", "name": "The Warp Core", "database_id": "284361", "purpose": "Weekly decomposition W1-W12 (50/30/20 L2/L1/L0)"}
]
```

→ 3 tables canon en place, DB `284361` = workspace Baserow Cloud "Amadou'space" (per screenshot A0 2026-06-21).

### 3.2 Affine Cloud (DEAL Muse) — ✅ LIVE

**Mode** : streamable-http proxy vers hosted MCP endpoint.
**Env vars User scope** :
- `AFFINE_API_KEY` = `ut_fDktG4cA0...` (46 chars)
- `AFFINE_WORKSPACE_ID` = `ef927d3a-5be0-41ed-b639-829b7f74939b` (UUID)

**Runtime receipt** (`mcp__symphony-affine__affine_list_workspaces`) :
```json
[{"id": "ef927d3a-5be0-41ed-b639-829b7f74939b", "name": "A'Space DEAL Workspace", "kind": "DEAL", "url": "https://app.affine.pro/workspace/ef927d3a-5be0-41ed-b639-829b7f74939b", "edgeless": true}]
```

→ 1 workspace DEAL edgeless mode confirmé (per screenshot A0).

### 3.3 Plane Cloud (GTD) — ⏳ LIVE ready (CC restart required)

**Mode** : REST API (httpx async) — Plane.so n'a pas de MCP endpoint natif.
**Env vars User scope (après Set 2026-06-21)** :
- `PLANE_API_KEY` = `plane_api_c6...` (42 chars) — déjà set
- `PLANE_WORKSPACE_SLUG` = `aspace-core` (set 2026-06-21)
- `PLANE_PROJECT_ID` = `79df867c-06b5-4e61-b3f1-68aa886c39a3` (set 2026-06-21, discovered via REST)

**Runtime receipt actuel** (`mcp__symphony-plane__plane_list_issues`) : **STUB** (3 issues fallback).
**Cause racine D6** : MCP Plane server lit env vars au subprocess startup. Mon Set User scope post-session-start ne reload pas le subprocess courant.

**D6 fix canonique** (per `handoff_mcp_durable_config_2026-06-16.md`) :
1. `touch C:\Users\amado\.mcp.json` (force MCP tool registry reload)
2. Kill PIDs des 4 Symphony MCP servers (symphony-baserow, symphony-affine, symphony-obsidian, symphony-plane)
3. CC re-spawn les subprocess au prochain tool call
4. **OU** CC restart complet (plus simple mais perd session state)

**REST API discovery done** (`https://api.plane.so/api/v1/workspaces/aspace-core/projects/`) :
- User auth: `117f5c3e-f1d9-4159-bdc7-dc354cc3c0d7` (Amadou Kone, amdkn777@gmail.com)
- Workspace: `2a0f9020-1dc3-4654-a5a5-452be02bbfd1` (slug `aspace-core`)
- Project: `79df867c-06b5-4e61-b3f1-68aa886c39a3` (name "ASpace Core", identifier `ASPAC`, is_member=true)

→ 1 projet dans workspace, A0 = Member role 20.

### 3.4 Obsidian (PARA) — ⚠️ LOCAL FS (D3 nuance)

**Mode** : filesystem local direct (`OBSIDIAN_VAULT_PATH`), **PAS un SaaS Cloud**.
**Env vars User scope** : tous vides → fallback default `~/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise`.

**D3 nuance critique** : Le brief A0 dit « Obsidiant Cloud » mais `mcp-obsidian.py` ligne 16-17 stipule verbatim :
```
Auth:
    None (local filesystem access only). No API key required.
```

→ Obsidian n'a **pas de mode Cloud** dans ce MCP. Soit :
- (a) A0 voulait dire Obsidian Publish (publish.obsidian.md pour hosting public)
- (b) A0 acceptation local-first (Sobriété+++, données locales d'abord = Loi L0 §1 Rick Sobriété)

**Recommandation Sobriété Rick** : (b) — local-first canoniquement aligné Rick L0 §1. Validation A0 HITL pending.

**Runtime receipt actuel** (`mcp__symphony-obsidian__obsidian_list_projects`) :
```json
[]
```
→ `01_Projects/` PARA folder vide. Comportement attendu (PARA pas encore rempli).

## 4. D3 nuances + Sobriété Rick observations

### 4.1 D3 nuance Obsidian

Cf. §3.4. Obsidian = local FS, pas Cloud SaaS. Pivot A0 « Cloud » techniquement impossible pour ce MCP sans rewrite architecture.

### 4.2 D6 root cause Plane MCP env reload

Cf. §3.3. Pattern récurrent : MCP servers lisent env vars au subprocess startup. Post-session Set User scope n'affecte pas subprocess courant. Fix canonique documenté.

### 4.3 Sobriété Rick alignement

- **Ikigai + Life Wheel** sur Supabase Cloud = aligné Sobriété++ (données structurées canon, RLS mono-tenant)
- **DEAL** sur Affine Cloud = OK (docs first canonique, Edgeless mode)
- **12WY** sur Baserow Cloud = OK (3 tables canon pré-existantes)
- **GTD** sur Plane Cloud = OK post-restart
- **PARA** sur Obsidian local = aligné Sobriété+++ (Loi L0 §1 « Données locales d'abord »)

→ 4 SaaS Cloud validés Sobriété, 1 local Sobriété+++.

### 4.4 Anti-paperclip Saru (rappel)

Le mapping 6 frameworks Life OS ne crée PAS de paperclip maximizer pour Saru LD02 Finance : chaque SaaS a un scope cadre (Ikigai/Life Wheel/DEAL/12WY/PARA/GTD). Anti-paperclip = OK par construction.

## 5. A0 actions pending (HITL)

1. **CC restart** (ou touch .mcp.json + kill MCP PIDs) pour activer Plane live mode
2. **D3 nuance Obsidian clarification** : (a) Obsidian Publish ou (b) acceptation local-first ?
3. **Migration éventuelle** : si Obsidian Publish souhaité, A3 Holo-Janeway doit réécrire `mcp-obsidian.py` en streamable-http proxy vers publish.obsidian.md (effort ~30 min, Sobriété trade-off)

## 6. Anti-patterns évités (D6 lessons shipped)

1. **PAS de Test Key Pragma re-demandé** : A0 a exposé tokens dev en clair dans `.mcp.json` exprès. Discovery direct via env var reads (D7 cost-of-escalation respecté)
2. **PAS de curl direct** sauf fallback discovery : utilisé MCP tools d'abord, REST API Plane en fallback discovery uniquement
3. **PAS de re-derivation** : 4 scripts MCP Symphony lus verbatim pour comprendre env var contract avant action
4. **D3 nuance conservée** : Obsidian « Cloud » = local FS, ne pas inventer un mode Cloud qui n'existe pas

## 7. Doctrine Anti-Paresse D1-D8 appliquée

- **D1 Verify-Before-Assert** : 4 MCP runtime calls + 1 REST API discovery + 1 env var scope check avant de claimer quoi que ce soit
- **D2 Research FIRST** : 4 scripts MCP lus avant d'agir
- **D3 Nuance over Literal** : Obsidian « Cloud » du brief A0 = local FS réel
- **D4 No Self-Contradiction** : ce handoff = append-only, ne réécrit aucun handoff antérieur
- **D5 No Self-Congratulation** : Plane live = « ready, restart required », PAS « live maintenant »
- **D6 Persistent Symptom** : Plane stub → collect exact command + env vars + D6 fix canonique (touch .mcp.json + kill PIDs)
- **D7 A0 Escalation Cost** : Plane PROJECT_ID discovery = curl direct, pas escalation A0
- **D8 Cross-Agent** : Pattern MCP durable config réutilisé verbatim

## 8. Related

- `wiki/hand_offs/handoff_a0_jumeau_numerique_2026-06-21.md` §12 (Vague 4 pivot A0)
- `wiki/hand_offs/handoff_mcp_durable_config_2026-06-16.md` (pattern touch + kill PIDs)
- `wiki/hand_offs/handoff_mcp_symphony_premortem_2026-06-21.md` (pre-mortem 4 SaaS)
- `_SPECS/ADR/L1_Life_OS/ADR-META-001_anti-paresse-verify-before-assert.md`
- `wiki/log.md` entry 2026-06-21 Vague 4 close

## 9. Hash d'intention

`sha256(saas_cloud_activated_2026-06-21_v4_pivot_stabilite)` = computed at log.md append time

---

## 10. POST-CC-RESTART UPDATE (2026-06-21 19:33 EDT)

### 10.1 Status runtime post A0 CC full restart

A0 a exécuté Option A (Full kill-all CC + relaunch, screenshot panel VSCode 2026-06-21 ~19:30). **10/10 MCPs Connected** dans le panel CC (supabase-omk + symphony-affine + symphony-baserow + symphony-obsidian + **symphony-plane** + symphony-supabase + transcript-api + vercel + vercel-abc + vercel-omk).

### 10.2 Plane LIVE (D1 receipt canon — mission 15-17 SUCCESS)

`mcp__symphony-plane__plane_list_issues` retourne maintenant **LIVE 7 issues** :

```json
"Issues (live, project=79df867c…): [
  {id: '72d14a7e-...', sequence_id: 7, name: '6. Customize your settings ⚙️', ...},
  {id: 'abcacca5-...', sequence_id: 6, name: '5. Use Cycles to time box tasks 🗓️', ...},
  {id: '58717e10-...', sequence_id: 5, name: '4. Visualize your work 🔮', ...},
  {id: 'b9d1b26e-...', sequence_id: 4, name: '3. Create and assign Work Items ✏️', ...},
  {id: 'acbd88a8-...', sequence_id: 3, name: '2. Invite your team 🤜🤛', ...},
  {id: '051cfcdf-...', sequence_id: 2, name: '1. Create Projects 🎯', ...},
  {id: 'a8225399-...', sequence_id: 1, name: 'Welcome to Plane 👋', ...}
]"
```

→ **Cerritos Holo Deck GTD fully LIVE Cloud** ✅. Le USER state de mcp-plane.py ligne 351 (project=79df867c…) confirme PROJECT_ID correctement chargé. Le fix canonique = full CC restart (Option A appliquée).

### 10.3 D6 NEW regression post-restart : baserow + affine tool registry

`mcp__symphony-baserow__baserow_list_tables` et `mcp__symphony-affine__affine_list_workspaces` retournent `Tool not found` post-restart. Pourtant :
- Les subprocesses python sont alive (PIDs 31508, 18500, start 19:32-19:33)
- Le panel CC affiche "Connected" pour les 10 MCPs
- Le tool name est canon (vérifié verbatim via `Grep` dans `mcp-baserow.py` ligne 198 et `mcp-affine.py` ligne 157)

**D6 hypothesis** : CC tool registry n'a pas re-discovered les tools des MCPs qui étaient connectés PRE-restart. Plane marche parce qu'il a été spawn APRÈS le restart (fresh registry). Baserow + Affine étaient déjà connectés avant le restart et n'ont pas re-listé leurs tools.

**D6 fix candidates** (D7 cost-of-escalation : A0 HITL) :
1. **A. Touch `.mcp.json` + kill baserow/affine subprocesses** : force re-spawn + re-list_tools
2. **B. Second CC restart** : même fix que Plane
3. **C. Use alt MCP tools** : `mcp__symphony-supabase__*` peut servir de backup (Baserow → Supabase `fw_12wy` table ; Affine → Supabase `fw_deal` table) — D3 nuance Sobriété++

### 10.4 Obsidian confirmed local (A0 clarification)

A0 a verbalement confirmé en chat (2026-06-21 ~19:30) : "j'ai restart claude code et je confirme que Obsidian est Local sur mon File System". D3 nuance §3.4 close.

### 10.5 Mapping final 6 frameworks Life OS — état runtime final

| A1 | A2 | Framework | SaaS | Runtime | Status |
|---|---|---|---|---|---|
| A1 Beth | A2 Orville | Ikigai | Supabase Cloud | (non retesté post-restart) | ⏳ presumed LIVE |
| A1 Beth | A2 Discovery | Life Wheel | Supabase Cloud | (non retesté post-restart) | ⏳ presumed LIVE |
| A1 Beth | A2 Protostar | DEAL | Affine Cloud | REGRESSION tools not found | ❌ D6 post-restart |
| A1 Morty | A2 Curie SNW | 12WY | Baserow Cloud | REGRESSION tools not found | ❌ D6 post-restart |
| A1 Morty | A2 Enterprise | PARA | Obsidian Local FS | LIVE (returns []) | ✅ |
| A1 Morty | A2 Cerritos | GTD | Plane Cloud | **LIVE 7 issues** | ✅ D1 verified |

### 10.6 D6 lessons shipped (cumulative)

1. **User scope env vars ne propagent PAS aux subprocess Python spawned pre-Set** (D6 root cause Plane initial)
2. **CC ne kill PAS tous les anciens subprocesses MCP au restart** (4 instances coexistantes observées)
3. **MCP tool registry CC = static at session start** (D6 #4 déjà documenté) — NEW : ne se met PAS à jour même après full CC restart pour MCPs pré-connectés
4. **Full CC restart = seule solution confirmée pour Plane LIVE** (D1 verified)

### 10.7 A0 HITL — 1 action pending

**Baserow + Affine tool registry regression** : appliquer Option A (second CC restart) ou Option C (use Supabase backup) ou laisser en l'état et accepter que 12WY + DEAL opèrent via stubs.

— Update hash : `saas_cloud_activated_2026-06-21_v5_post_restart_plane_live`
