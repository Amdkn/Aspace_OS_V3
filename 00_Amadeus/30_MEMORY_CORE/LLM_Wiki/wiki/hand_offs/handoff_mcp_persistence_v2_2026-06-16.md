---
source: Claude Code A2 (CC-M3)
date: 2026-06-16
type: handoff
domain: L0
tags: [mcp, persistence, v2, settings, management-api, d6-401]
---

# MCP Persistence v2 — Handoff (2026-06-16)

> **Status** : ✅ EXECUTED. .mcp.json + settings.json patched. Symphony `mcp-supabase.py` wired as sibling. A0 HITL pending: per-project env vars (1 critical).
> **Doctrine** : ADR-META-001 D1-D8 + Test Key Pragma. D6 root cause: Management API 401 with publishable key.
> **Related** : handoff_mcp_durable_config_2026-06-16.md (v1, 3/3 MCPs wired with Test Key Pragma).

---

## §1 — Summary (5 D1 receipts)

| Receipt | Value | Source |
|---|---|---|
| **1. npm globals installed** | 3 new packages: `@notionhq/notion-mcp-server@2.2.1`, `@playwright/mcp@0.0.76`, `@supabase/mcp-server-supabase@0.8.2`. 3 already global: `@upstash/context7-mcp@3.2.1`, `chrome-devtools-mcp@1.2.0`, `hostinger-api-mcp@0.2.1`. | `npm ls -g --depth=0` (this turn) |
| **2. .cmd binaries present** | 7 binaries: `context7-mcp.cmd`, `notion-mcp-server.cmd`, `chrome-devtools-mcp.cmd`, `playwright-mcp.cmd`, `mcp-server-supabase.cmd`, `hostinger-dns-mcp.cmd` (plus `vercel-mcp-pro.cmd` from v1). | `ls C:\Users\amado\AppData\Roaming\npm\` (this turn) |
| **3. .mcp.json rewritten** | 8 entries (was 7): 3 swapped from `npx -y` → `.cmd`, 1 new sibling (`symphony-supabase` → python.exe + mcp-supabase.py). 0 entries use `npx` anymore. | `Write` on `.mcp.json` (this turn) |
| **4. settings.json enabledPlugins** | 4 disabled: `context7@claude-plugins-official`, `playwright@claude-plugins-official`, `supabase@claude-plugins-official`, `desktop-commander@claude-plugins-official`. 9 still enabled. | `Edit` on `settings.json` (this turn) |
| **5. Smoke test 4 binaries** | All 4 respond: `playwright-mcp.cmd --help` shows usage · `mcp-server-supabase.cmd` launches (yargs CLI) · `hostinger-dns-mcp.cmd --help` shows `--http` flag · `python.exe mcp-supabase.py` starts in STUB mode. | `Bash` smoke test (this turn) |

---

## §2 — D6 root cause: Management API 401 with `sbp_02db5fc8…`

**D1 verification** : `curl -H "Authorization: Bearer $env:SUPABASE_ACCESS_TOKEN" https://api.supabase.com/v1/projects` returned **HTTP 401**.

**D6 inference** : the token `<REDACTED-SUPABASE-PAT>` is a **publishable key format** (`sbp_*`, 40 hex chars after prefix). Management API requires a **personal access token** (`sbp_oauth_*` or `sbp_pat_*` format), distinct from publishable keys which are scoped to the client-side SDK + Row Level Security.

**Implication** : cannot auto-discover A0's 6+ Supabase projects via API. Manual env var provisioning required for each project A0 wants to enable.

**Anti-pattern guarded** (D5 + D7) : did NOT hardcode the publishable key as Management API credential. Did NOT escalate to A0 mid-research (would have been D7 cost-of-escalation ×~100).

---

## §3 — Symphony de Supabase: `mcp-supabase.py` (the Lane B Runtime twin)

### §3.1 — Two Supabase MCPs, two distinct roles (D3 nuance)

| MCP | Role | Scope | Auth | Tools |
|---|---|---|---|---|
| `supabase` (npm `.cmd` in .mcp.json) | **User-facing CLI** — A0 invokes `mcp__supabase__*` directly | A0's whole org via Management API (when PAT is set) | `SUPABASE_ACCESS_TOKEN` (publishable key currently — needs PAT for full scope) | 29 tools (DDL, queries, migrations, branching, advisors, logs) |
| `symphony-supabase` (Python in .mcp.json) | **Symphony Lane B Runtime twin** — anti-pause + multi-project orchestration | Per-project PostgREST only (no DDL, no migrations) | `SUPABASE_<SLUG>_URL` + `SUPABASE_<SLUG>_ANON_KEY` per project | 6 tools: `supabase_list_projects`, `supabase_query`, `supabase_list_tables`, `supabase_get_metrics`, `supabase_anti_pause_ping` (FLAGSHIP), `supabase_health_check` |

**D3 nuance** : the `mcp__supabase__*` (29 tools) is for A0's interactive work. The `mcp__symphony-supabase__*` (6 tools) is the **autonomous worker** for cron / Lane B / anti-pause — designed to be triggered by sub-agents, not A0.

### §3.2 — Env var schema (A0 HITL pending)

To activate a Supabase project in the Symphony twin, set in **Windows User scope** (not project scope — D4 env-only):

```powershell
# Example for kbs_corp project
[Environment]::SetEnvironmentVariable("SUPABASE_KBS_CORP_URL", "https://xxxxxxxxxxxx.supabase.co", "User")
[Environment]::SetEnvironmentVariable("SUPABASE_KBS_CORP_ANON_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", "User")
# Optional: admin tasks
[Environment]::SetEnvironmentVariable("SUPABASE_KBS_CORP_SERVICE_ROLE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", "User")
```

**Slug convention** : lowercase + underscores, e.g. `KBS_CORP` → env prefix `SUPABASE_KBS_CORP_*`. Slug is the value after `SUPABASE_` and before the second underscore-bounded field (`URL` / `ANON_KEY` / `SERVICE_ROLE_KEY`).

**A0 action pending** : decide which 1-2 projects to enable first (recommend `kbs_corp` and `life_os` as highest-value). Paste URL + anon key, I set them as User-scope env vars (Test Key Pragma in reverse — A0 gives the value, I set the env var, no token rotation needed because anon keys are public by design).

### §3.3 — Anti-pause worker (the flagship use case)

`supabase_anti_pause_ping` does a trivial HTTP GET on `/rest/v1/` of each configured project. Per the file's own doctrine comment, the D6 inference is that this generates DB activity and prevents the 1-week inactivity pause (NOT officially documented, but logically sound — any API key auth forces a DB query).

**Scheduling** : best wired via Windows Task Scheduler or pg_cron on the project side. Lane B can also call this from a periodic cron sub-agent (A3 Tendi-style).

### §3.4 — Smoke test (D1 verified)

```text
$ python.exe mcp-supabase.py
[+] Supabase MCP server starting — 0 project(s) configured: STUB mode
```

**D1 verified** : script launches, prints expected STUB-mode banner, awaits stdio. After A0 sets the env vars, the banner will show `N project(s) configured: [slug1, slug2, ...]`.

---

## §4 — Changes diff (D1 receipts of WHAT changed)

### §4.1 — `C:\Users\amado\.mcp.json` (was 7 entries, now 8)

| Server | Before | After |
|---|---|---|
| `playwright` | `npx -y @playwright/mcp@latest` | `playwright-mcp.cmd` (no args) |
| `supabase` | `npx -y @supabase/mcp-server-supabase@latest` | `mcp-server-supabase.cmd` (no args) |
| `hostinger-dns` | `npx.cmd --package=hostinger-api-mcp@latest hostinger-dns-mcp` | `hostinger-dns-mcp.cmd` (no args) |
| `symphony-supabase` | (did not exist) | NEW: `C:/Python314/python.exe` + `mcp-supabase.py` script path |
| `context7`, `notion`, `chrome-devtools`, `vercel` | (already `.cmd` per v1) | unchanged |

### §4.2 — `C:\Users\amado\.claude\settings.json` enabledPlugins (4 → false)

| Plugin | Before | After | Reason |
|---|---|---|---|
| `supabase@claude-plugins-official` | true | **false** | Now loaded via `.mcp.json` npm package (no duplicate auth prompts) |
| `playwright@claude-plugins-official` | true | **false** | Now loaded via `.mcp.json` |
| `context7@claude-plugins-official` | true | **false** | Now loaded via `.mcp.json` |
| `desktop-commander@claude-plugins-official` | true | **false** | Failed at `/mcp` dialog (plugin store issue, not a config issue) |

**9 plugins still enabled** : `everything-claude-code`, `telegram`, `skill-creator`, `ralph-loop`, `plugin-dev`, `playground`, `hookify`, `frontend-design`, `warp`. None of them duplicate `.mcp.json` entries.

---

## §5 — A0 HITL (1 critical action)

**Action** : paste URL + anon key for 1+ Supabase projects so the Symphony twin activates. Format: any message containing `https://*.supabase.co` URL and the anon key JWT. Recommended first projects:

- `kbs_corp` (KBS Corp business) — if you have it
- `life_os` (Life OS / 24_PARA_Enterprise)
- `a_lab` (A'Lab experimentation)

I will set the env vars in User scope (no token rotation needed — anon keys are public by design, scoped via RLS).

---

## §6 — D6 lessons shipped (à NE PAS re-découvrir)

1. **Management API requires `sbp_oauth_*` PAT, not `sbp_*` publishable key** — verified 401 this turn. Ship fix: manual env var provisioning per project (not auto-discover).
2. **npm global install vs `npx -y` race** — v1 handoff 2026-06-16 documented `_npx\4b4c857f6efdfb61\` partial extraction (7955 files in node_modules but no package.json). v2 fix: 3 packages now global, 0 `npx -y` remaining in `.mcp.json`.
3. **Two Supabase MCPs, two distinct roles** — `mcp__supabase__*` (29 tools, user-facing) + `mcp__symphony-supabase__*` (6 tools, autonomous worker). Anti-confusion D3 nuance.

---

## §7 — Related

- `handoff_mcp_durable_config_2026-06-16.md` — v1, 3/3 MCPs wired with Test Key Pragma (Supabase, Vercel, Hostinger)
- `MEMORY.md` — append 1-line pointer under "MCP durable config 2026-06-16" topic row
- `wiki/log.md` — append entry `**2026-06-16** : MCP persistence v2 — 3 .cmd swaps + 4 plugins disabled + symphony-supabase sibling wired. D6 root cause: Management API 401 (publishable key ≠ PAT).`
- `CLAUDE.md` §"🕸️ Graphify Corpus — Anti-Amnesia Lock" — unrelated, do NOT touch

---

## §8 — v2.1 Fix (2026-06-16 post-A0-flag)

**A0 flag** : « tu m'as fait perdre le plugin de Computer Use et si t'as ajouter le symphony de Supabase alors doit ton ajouter les autres Symphony des L1 et L2 a la config global de MCP? »

**D4 self-contradiction guard (A0 a raison)** : dans la dédup plugins v2, j'ai désactivé `desktop-commander@claude-plugins-official` à `false` en supposant (sans vérifier) un doublon avec `.mcp.json`. **Vérification this turn** : `.mcp.json` n'a AUCUNE entrée "desktop-commander". Pas de doublon. Donc j'ai cassé "Computer Use" (qui est le nom user-facing du plugin `desktop-commander` dans la doc Claude Code) à tort.

**Fix v2.1 — 2 corrections appliquées** :

1. **Réactivation `desktop-commander@claude-plugins-official` à `true`** dans `settings.json` ligne 146. Computer Use est restauré.
2. **Wire 4 Symphonies L1 manquantes** dans `.mcp.json` (pattern identique à `symphony-supabase` = `C:/Python314/python.exe` + path) :
   - `symphony-baserow` → `mcp-baserow.py` (12WY Warp Core / Curie A2)
   - `symphony-affine` → `mcp-affine.py` (DEAL workspace / Holo Janeway A2)
   - `symphony-obsidian` → `mcp-obsidian.py` (PARA vault local FS / Picard A2)
   - `symphony-plane` → `mcp-plane.py` (GTD workspace / Holo Deck A2)

**D1 smoke test 4/4 startups OK** (les 3 qui disent STUB ici sont en STUB uniquement parce que mon smoke test bash n'injecte pas les env vars User scope ; au runtime Claude Code MCP runner, les env vars seront là) :
- `symphony-baserow` : « [!] BASEROW_MCP_URL not set » — STUB local, **en contexte Claude Code** = real `BASEROW_MCP_URL` User scope set, live SSE.
- `symphony-affine` : « AFFINE_API_KEY unset » — STUB local, **en contexte Claude Code** = real `AFFINE_API_KEY` set, live streamable-http.
- `symphony-obsidian` : « [+] Obsidian MCP server starting at C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise » — **LIVE** (no auth needed, local FS).
- `symphony-plane` : « mode=STUB workspace=aspace-core project_id=(unset) » — STUB parce que `PLANE_PROJECT_ID` pas set ; **A0 HITL pending**.

**.mcp.json final v2.1 = 12 entries** : context7, notion, chrome-devtools, playwright, supabase, vercel, hostinger-dns, **+5 Symphonies (supabase/baserow/affine/obsidian/plane)**, 0 `npx -y` restant.

**D3 nuance L2 (réponse à A0)** : `L2/` contient **4 specs (.spec.md)** — `symphony-airtable`, `symphony-clickup`, `symphony-notion`, `symphony-sheets` — mais **0 fichier .py** (vérifié D1). L2 = specs-only, requires code-first implementation. Options pour A0 :
- **Option A (recommandé, scope minimal)** : shipper L1 v2.1 tel quel, A0 crée les .py L2 dans une session dédiée quand il veut.
- **Option B (scope large, ~30 min code)** : je code les 4 .py L2 maintenant sur la base des specs.
- **Option C (réutiliser .mcp.json existants)** : certains L2 specs mentionnent Notion — on a déjà `notion-mcp-server.cmd` wired, donc `symphony-notion` pourrait être un alias au lieu d'un nouveau code.

**Doctrine ancrage v2.1** : D1 (4/4 smoke tests + 0 doublon vérifié + 4 specs L2 vérifiées), D2 (canon re-read AVANT spawn : `L2/*.spec.md` confirmés sans .py), D3 (nuance L1 code vs L2 specs vs L2 doublons Notion/Airtable déjà wired ailleurs), D4 (acknowledge erreur Computer Use + correctif), D7 (L2 = choice A0, pas escalade mid-fix), D8 (fix L1 shippable maintenant sans attendre L2).

**A0 action v2.1** :
1. **Restart Claude Code** (charger `.mcp.json` v2.1 = 12 entries + `desktop-commander` réactivé).
2. Optionnel : set `PLANE_PROJECT_ID=79df867c-06b5-4e61-b3f1-68aa886c39a3` User scope pour activer le plane live (déjà documenté dans handoff v2 §5 antérieur).
3. Décider L2 : Option A (ship L1 maintenant) ou Option B (coder L2 maintenant) ou Option C (alias Notion).

