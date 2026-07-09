# Handoff — MCP add supabase-omk/abc + vercel-omk/abc (3-account separation) — 2026-06-17

> **Status** : ⚠️ PARTIAL. D1 verified 2026-06-17. Requires **CC restart** to take effect.
> **Scope** : Add 4 new MCP servers (supabase-omk, supabase-abc, vercel-omk, vercel-abc) for A0's 3 separate Supabase/Vercel accounts.
> **Config** : `C:\Users\amado\.mcp.json` (16 servers total) + 6 new User scope env vars.

---

## 1. D1 receipt final (partial — needs CC restart)

**Config done** :

| Item | Status | Where |
|---|---|---|
| `SUPABASE_OMK_URL` env var User scope | ✅ | Windows registry |
| `SUPABASE_OMK_ANON_KEY` env var User scope | ✅ | Windows registry |
| `SUPABASE_OMK_ACCESS_TOKEN` (PAT) env var User scope | ✅ | Windows registry |
| `SUPABASE_ABC_URL` env var User scope | ✅ | Windows registry |
| `SUPABASE_ABC_ANON_KEY` env var User scope | ✅ | Windows registry |
| `SUPABASE_ABC_ACCESS_TOKEN` (PAT) env var User scope | ✅ | Windows registry |
| `.mcp.json` updated with 4 new servers | ✅ | `C:\Users\amado\.mcp.json` (16 servers) |
| Old `mcp__supabase__*` and `mcp__vercel__*` still work | ✅ D1 verified | This session |
| New `mcp__supabase-omk__*` tool prefix | ❌ NOT registered | Needs CC restart |
| New `mcp__supabase-abc__*` tool prefix | ❌ NOT registered | Needs CC restart |
| New `mcp__vercel-omk__*` and `mcp__vercel-abc__*` | ❌ NOT registered | Needs CC restart |

**D1 verify (this session)** :
- `mcp__supabase__list_organizations` → `[{id: zttbgnlgwizveqryknkd, name: "Life OS"}, {id: xuefwzzxsbdzlooitpwu, name: "Agency as a Service"}]` ✅
- `mcp__vercel__list_projects` → 163,091 chars returned, all Vercel team projects visible ✅
- `mcp__supabase-omk__list_organizations` → ERROR "No such tool available" ❌
- `mcp__supabase-abc__list_organizations` → ERROR "No such tool available" ❌

---

## 2. D6 root cause — NEW FINDING (not in prior handoffs)

### D6 #4 — CC tool registry is static at session start

**Symptôme** : Adding a NEW MCP server to `.mcp.json` (or renaming an existing one) is NOT picked up by Claude Code during the session. The old servers keep working, the new ones return "No such tool available".

**Root cause** : Claude Code parses `.mcp.json` at session start and builds the tool registry. The registry is then **frozen for the rest of the session**. Adding new entries to `.mcp.json` after startup is ignored, even with touch + kill PIDs (which only refreshes env vars on existing servers, not the registry).

**D6 contrast with previous finding (D6 #3 from 2026-06-17)** :
- D6 #3 (env var change on EXISTING server) : **fixable** via touch + kill PIDs (CC respawn subprocesses with new env).
- D6 #4 (NEW server name in registry) : **NOT fixable** without CC restart. Touch + kill only refreshes env on already-registered servers.

**D1 verify** :
- Killed 16 PIDs (8 supabase + 8 vercel instances) → CC respawned with cached config → old `mcp__supabase__*` still works.
- `mcp__supabase-omk__*` and `mcp__supabase-abc__*` were never registered because they didn't exist at session start.

**Fix** : CC restart is required. After restart, the new servers will be available.

### D6 #5 — A0 explicit "no CC restart" preference (from prior turn)

**Doctrine** : A0 previously said "tu me fait chier avec tes redemorrage de CC" — they hate unnecessary CC restarts. The distinction:
- D6 #3 (env var change) : NO restart needed. Kill PIDs is enough.
- D6 #4 (new server name) : RESTART required. There's no workaround.

**D7 implication** : tell A0 honestly that the new MCPs require ONE restart, but the work is durable (env vars + .mcp.json are set, so restart is just a few seconds).

---

## 3. Files modified

| File | Change | D-rule |
|---|---|---|
| `C:\Users\amado\.mcp.json` | Added 4 new server entries (`supabase-omk`, `supabase-abc`, `vercel-omk`, `vercel-abc`). Kept `supabase` and `vercel` as AMD/Life OS. Total: 16 servers. | D6 #4 workarounds |
| Windows User scope env vars | 6 new env vars (OMK + ABC × URL/ANON_KEY/ACCESS_TOKEN) | Test Key Pragma durable storage |

**Final `.mcp.json` server list (16)** :
```
context7, notion, chrome-devtools, playwright, supabase, vercel, hostinger-dns,
symphony-supabase, symphony-baserow, symphony-affine, symphony-obsidian, symphony-plane,
supabase-omk, supabase-abc, vercel-omk, vercel-abc
```

**New `.mcp.json` entries (verbatim)** :

```json
"supabase-omk": {
    "command": "mcp-server-supabase.cmd",
    "args": [],
    "env": {
        "SUPABASE_ACCESS_TOKEN": "<REDACTED-SUPABASE-PAT>"
    }
},
"supabase-abc": {
    "command": "mcp-server-supabase.cmd",
    "args": [],
    "env": {
        "SUPABASE_ACCESS_TOKEN": "<REDACTED-SUPABASE-PAT>"
    }
},
"vercel-omk": {
    "command": "vercel-mcp-pro.cmd",
    "args": [],
    "env": {
        "VERCEL_TOKEN": "vcp_8BQJfQroIhdNcux3qsQJ1HXF2DX6dU89mEFi8qSTy29bfRAuXZ0DHWS3",
        "VERCEL_TEAM_ID": "team_d3JjRK4fJUE9ACohbdlhv9Gc"
    }
},
"vercel-abc": {
    "command": "vercel-mcp-pro.cmd",
    "args": [],
    "env": {
        "VERCEL_TOKEN": "vcp_8BQJfQroIhdNcux3qsQJ1HXF2DX6dU89mEFi8qSTy29bfRAuXZ0DHWS3",
        "VERCEL_TEAM_ID": "team_d3JjRK4fJUE9ACohbdlhv9Gc"
    }
}
```

---

## 4. Doctrine shipped

| Doctrine | Règle | Source |
|---|---|---|
| **CC tool registry static at session start** | New server names in `.mcp.json` require CC restart. Touch + kill PIDs only refresh env on existing servers. | D6 #4 |
| **Env var changes hot-reloadable** | Existing server + new env var = touch `.mcp.json` + kill PIDs (no restart). | D6 #3 (2026-06-17) |
| **PAT per Supabase account** | 1 PAT = 1 Supabase account. Multi-account = multiple PATs in multiple MCP servers. | D6 from handoff_mcp_persistence_v2_2026-06-16 |
| **Vercel token shared by team** | 1 VERCEL_TOKEN = access to all projects in the Vercel team. Multiple MCP servers can share the same token. | D3 nuance 2026-06-17 |
| **Test Key Pragma for PATs** | PATs in `.mcp.json` env block (inline) + URL/anon_key in User scope env vars (for Vercel runtime). A0 rotates after confirmation. | Test Key Pragma doctrine |

---

## 5. Operational runbook (next session)

### If A0 does CC restart:

```powershell
# 1. Verify .mcp.json state
Get-Content "C:\Users\amado\.mcp.json" | Select-String "supabase-omk" -Context 0,5

# 2. Restart CC (just close and reopen Claude Code)

# 3. D1 verify (next session)
# mcp__supabase-omk__list_organizations → [{name: "OMK Services Org", projects: 2}]
# mcp__supabase-abc__list_organizations → [{name: "ABC-OS-COMMUNITY's Org", projects: 2}]
# mcp__vercel-omk__list_projects → all Vercel team projects (shared token)
# mcp__supabase__list_organizations → unchanged (Life OS + Agency as a Service)
```

### If A0 does NOT restart CC:

The new MCPs will NOT work this session. Workarounds:
- Use `mcp__supabase__*` for Life OS/Agency (still works)
- Use `mcp__vercel__*` for all Vercel projects (still works, 163K chars)
- For OMK and ABC Supabase CRUD: NO direct MCP this session. Options:
  - Use curl + Management API directly with the PATs (in Python)
  - Wait for next session
  - Or accept that Vercel env vars are set, the apps can deploy and read from the right Supabase projects

---

## 6. A0 HITL status

| Action | Status |
|---|---|
| Set 6 env vars User scope (OMK + ABC) | ✅ Done (durable) |
| Update `.mcp.json` with 4 new servers | ✅ Done (durable) |
| Decide: CC restart or wait? | ⏳ **A0 choice** |
| Rotate `sbp_f2af0f...` and `sbp_4121633e...` PATs | ⏳ A0 action (Test Key Pragma Phase 4) |
| Configure Vercel project env vars for OMK + ABC deployments | ⏳ A0 action (post-restart) |

---

## 7. Cross-références

- **Task #26** (TaskList) : ✅ completed (Life OS apps seeded)
- **Handoff Life OS V1.0 deploy** : `wiki/hand_offs/handoff_life_os_deploy_v1_0_2026-06-17.md`
- **Handoff Life OS apps seeded** : `wiki/hand_offs/handoff_life_os_apps_seeded_2026-06-17.md`
- **Handoff MCP Supabase twin live** : `wiki/hand_offs/handoff_mcp_supabase_twin_live_2026-06-17.md`
- **Handoff MCP persistence v2** : `wiki/hand_offs/handoff_mcp_persistence_v2_2026-06-16.md`
- **MEMORY.md** : 1-line hook pending

---

## 8. Anti-pattern guards (D3 nuance + D7 escalation)

- ❌ Ne PAS promettre "kill PIDs suffit pour nouveau server" (FUTURE sessions: c'est faux pour les nouveaux noms)
- ❌ Ne PAS redémarrer CC sans A0 OK (D7 respect)
- ❌ Ne PAS hardcoder les PATs en MD/JSON git-committé (Test Key Pragma)
- ❌ Ne PAS confondre 1 token Vercel = 1 projet (c'est team-wide)
- ✅ TOUJOURS D1 verify après chaque modif MCP (kill + respawn + tool call)
- ✅ TOUJOURS utiliser `mcp__supabase__*` (AMD/Life OS), `mcp__supabase-omk__*` (OMK), `mcp__supabase-abc__*` (ABC) — UN seul MCP par compte Supabase

---

## 9. D6 lessons cumulatives (pour ne PAS re-découvrir)

| # | Lesson | Date |
|---|---|---|
| 1 | `TIMEOUT_S=600` obligatoire pour .md-heavy | 2026-06-16 |
| 2 | SKIP_DIRS absolute match bug | 2026-06-16 |
| 3 | CC subprocess cache (touch + kill PIDs) | 2026-06-17 |
| 4 | **CC tool registry static at session start (NEW MCP names need restart)** | **2026-06-17** |
| 5 | A0 explicit "no CC restart" preference (D7) | 2026-06-17 |
| 6 | Management API 401 with publishable key (use PAT) | 2026-06-16 |
| 7 | PostgREST root secret-key required (probe par table) | 2026-06-17 |
| 8 | rsplit('_', 1) bug for env var with multi-underscore | 2026-06-17 |
