---
source: Claude Code A2 (CC-M3)
date: 2026-06-23
type: handoff
domain: L0
tags: [mcp, export, portability, snapshot, 1an, no-hard-delete]
---

# MCP Export Canon — 1an portabilité

> **Date** : 2026-06-23 (v1)
> **Auteur** : Claude Code (A2)
> **A0** : Amadeus (jumeau numérique)
> **Doctrine** : [ADR-META-006 D6 Catalog](../_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md) append-only · [ADR-SOBER-002 Anti-Paperclip](../_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) · D4 no-hard-delete · D7 portabilité first
> **Objectif** : snapshot lisible de TOUTES les configs MCP A0 + procedure restore cross-machine, garantissant résistance 1an à effondrement/cassure/extinction involontaire.

---

## 1. Préflight restore (D1 receipts vérifiables)

**Prérequis cross-machine** :
- OS : Windows 10/11 (paths absolus utilisent `C:/Users/<USER>/`)
- Node.js v24+ (vérifié `Node.js v24.12.0`)
- Python v3.14 (vérifié `C:/Python314/python.exe`)
- Bun v1.3+ (vérifié `C:/Users/amado/.bun/bin/bun.exe`)
- Claude Code CLI (vérifié `claude` accessible PATH)
- PowerShell 5+ (pour env var User scope)

**Restore order** : (1) install runtimes → (2) clone `~/.claude/` config tree → (3) set env vars User scope → (4) `npm install -g` packages requis → (5) append `.mcp.json` entries → (6) CC restart → (7) verify MCP panel.

---

## 2. Inventory MCP canon (12 MCPs actifs 2026-06-23)

### 2.1 HTTP zero-surface (P1 pattern — preferred)

| MCP | URL canon | Auth | Scope env vars |
|---|---|---|---|
| (future) ClickUp via HTTP | `https://mcp.clickup.com/mcp` | OAuth browser flow | (none — auto-handled) |

**Pattern P1** : zero subprocess, zero local state. **Si le vendor HTTPS reste up, MCP reste up.** Fallback : vendor outage = manual browser workflow.

### 2.2 npm stdio (P2 pattern — fallback fragile)

| MCP | Package npm global | Binary cmd | Env vars canon attendus |
|---|---|---|---|
| `airtable` | `@airtable-mcp-server@1.13.0` | `C:/Users/<USER>/AppData/Roaming/npm/airtable-mcp-server.cmd` | `AIRTABLE_API_KEY` (canonical) |
| `clickup` | `@clickup-mcp-server@1.12.0` | `C:/Users/<USER>/AppData/Roaming/npm/clickup-mcp-server.cmd` | `CLICKUP_API_TOKEN` |
| `desktop-commander` | `@wonderwhy-er/desktop-commander@0.2.42` | `C:/Users/<USER>/AppData/Roaming/npm/desktop-commander.cmd` | (none — binary direct) |

**Pattern P2** : subprocess + env var. **Restore** : `npm install -g <pkg>` + set env vars + `.mcp.json` entry.

### 2.3 bun self-contained (P3 pattern — flaky intermittent)

| MCP | Plugin | Runtime | State dir | Env vars |
|---|---|---|---|---|
| `telegram` | `telegram@0.0.6` (claude-plugins-official) | `bun` v1.3+ | `~/.claude/channels/telegram/` | `TELEGRAM_BOT_TOKEN`, `TELEGRAM_STATE_DIR` (optional) |

**Pattern P3** : bun runtime + grammy SDK + state dir local. **Restore** : bun install + state dir init + `/telegram:access` skill for pairing.

### 2.4 Vendor HTTPS (P4 pattern — auto-managed)

| MCP | URL | Auth | Scope |
|---|---|---|---|
| `chrome-devtools` | (vendor) | auto | browser devtools |
| `context7` | (vendor npm cmd) | auto | library docs |
| `hostinger-dns` | (vendor HTTPS API) | Bearer | DNS records |
| `notion` | (vendor) | Bearer `ntn_*` | workspace Notion |
| `playwright` | (vendor npm cmd) | auto | browser E2E |
| `supabase` (×3 : AMD + omk + abc) | (vendor HTTPS API) | Bearer `sbp_*` | DB + storage + edge functions |
| `vercel` (×3 : AMD + omk + abc) | (vendor HTTPS API) | Bearer `vcp_*` | deployments + domains |
| `transcript-api` | Python MCP | Bearer `sk_*` | YouTube transcripts |
| `symphony-supabase/affine/baserow/obsidian/plane` | Python MCP twins | env-injected | ASpace OS internal |

**Pattern P4** : vendor-official HTTPS + auto-managed auth. **Restore** : vendor token rotation quarterly.

---

## 3. Env vars User scope — 12 MCP-related (snapshot 2026-06-23 22:50)

```powershell
# CLICKUP (D6 Entry #9 fixed 2026-06-23)
[Environment]::SetEnvironmentVariable("CLICKUP_API_TOKEN", "<value>", "User")
[Environment]::SetEnvironmentVariable("CLICKUP_API_KEY",   "<value>", "User")  # alias backward compat
[Environment]::SetEnvironmentVariable("CLICKUP_WORKSPACE_ID", "90141225938", "User")

# AIRTABLE (D6 Entries #10+#11 fixed 2026-06-23)
[Environment]::SetEnvironmentVariable("AIRTABLE_API_KEY", "<value>", "User")  # canonical
[Environment]::SetEnvironmentVariable("AIRTABLE_TOKEN",   "<value>", "User")  # alias
[Environment]::SetEnvironmentVariable("AIRTABLE_PAT",     "<pathRub_LEGACY_REVOKE>", "User")  # reliquat (D7 HITL)

# TELEGRAM
[Environment]::SetEnvironmentVariable("TELEGRAM_BOT_TOKEN", "8301764:AAFQ...", "User")

# TRANSCRIPT
[Environment]::SetEnvironmentVariable("TRANSCRIPT_API_KEY", "sk_Ajtx...", "User")

# HOSTINGER
[Environment]::SetEnvironmentVariable("HOSTINGER_API_TOKEN", "FU6xpXFU...", "User")

# VERCEL (×3 AMD + omk + abc)
[Environment]::SetEnvironmentVariable("VERCEL_TOKEN", "vcp_8BQJfQ...", "User")
[Environment]::SetEnvironmentVariable("VERCEL_TEAM_ID", "team_d3JjRK4f...", "User")

# SUPABASE (×3)
[Environment]::SetEnvironmentVariable("SUPABASE_ACCESS_TOKEN", "sbp_02db5fc8...", "User")
[Environment]::SetEnvironmentVariable("SUPABASE_LIFE_OS_URL", "https://hjweyhpmrxqsxfbibsnc.supabase.co", "User")
[Environment]::SetEnvironmentVariable("SUPABASE_LIFE_OS_ANON_KEY", "sb_publishable_...", "User")

# PLANE
[Environment]::SetEnvironmentVariable("PLANE_API_KEY", "plane_api_c6fb...", "User")
[Environment]::SetEnvironmentVariable("PLANE_WORKSPACE_SLUG", "aspace-core", "User")
[Environment]::SetEnvironmentVariable("PLANE_PROJECT_ID", "79df867c-06b5-4e61-b3f1-68aa886c39a3", "User")

# NOTION (embedded in .mcp.json OPENAPI_MCP_HEADERS)
```

**Restore procedure** : A0 manuel execute les `SetEnvironmentVariable` ci-dessus. **NE PAS hardcoder** les valeurs dans ce fichier (D4 no-hard-delete, D6 Test Key Pragma).

---

## 4. `.mcp.json` snapshot — 19 entries (2026-06-23 22:52)

```json
{
    "mcpServers": {
        "context7":        { "command": "context7-mcp.cmd",        "args": [] },
        "notion":          { "command": "notion-mcp-server.cmd",   "args": [], "env": { "OPENAPI_MCP_HEADERS": "..." } },
        "chrome-devtools": { "command": "chrome-devtools-mcp.cmd", "args": ["--no-usage-statistics","--no-performance-crux"], "env": { "CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS": "1" } },
        "playwright":      { "command": "playwright-mcp.cmd",      "args": [] },
        "supabase":        { "command": "mcp-server-supabase.cmd", "args": [], "env": { "SUPABASE_ACCESS_TOKEN": "${env:SUPABASE_ACCESS_TOKEN}" } },
        "vercel":          { "command": "vercel-mcp-pro.cmd",      "args": [], "env": { "VERCEL_TOKEN": "${env:VERCEL_TOKEN}", "VERCEL_TEAM_ID": "${env:VERCEL_TEAM_ID}" } },
        "hostinger-dns":   { "command": "hostinger-dns-mcp.cmd",  "args": [], "env": { "HOSTINGER_API_TOKEN": "${env:HOSTINGER_API_TOKEN}" } },
        "symphony-supabase": { "command": "C:/Python314/python.exe", "args": ["C:/Users/<USER>/ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony/L1/lane_B_runtime/04_mcps/mcp-supabase.py"], "env": { "SUPABASE_LIFE_OS_URL": "${env:SUPABASE_LIFE_OS_URL}", "SUPABASE_LIFE_OS_ANON_KEY": "${env:SUPABASE_LIFE_OS_ANON_KEY}" } },
        "symphony-baserow":  { "command": "C:/Python314/python.exe", "args": ["..."] },
        "symphony-affine":   { "command": "C:/Python314/python.exe", "args": ["..."] },
        "symphony-obsidian": { "command": "C:/Python314/python.exe", "args": ["..."] },
        "symphony-plane":    { "command": "C:/Python314/python.exe", "args": ["..."], "env": { "PLANE_API_KEY": "${env:PLANE_API_KEY}", "PLANE_BASE_URL": "https://api.plane.so/api/v1", "PLANE_WORKSPACE_SLUG": "${env:PLANE_WORKSPACE_SLUG}", "PLANE_PROJECT_ID": "${env:PLANE_PROJECT_ID}" } },
        "supabase-omk":    { "command": "mcp-server-supabase.cmd", "args": [], "env": { "SUPABASE_ACCESS_TOKEN": "sbp_f2af..." } },
        "supabase-abc":    { "command": "mcp-server-supabase.cmd", "args": [], "env": { "SUPABASE_ACCESS_TOKEN": "sbp_4121..." } },
        "vercel-omk":      { "command": "vercel-mcp-pro.cmd", "args": [], "env": { "VERCEL_TOKEN": "vcp_4z4b...", "VERCEL_TEAM_ID": "team_FORM..." } },
        "vercel-abc":      { "command": "vercel-mcp-pro.cmd", "args": [], "env": { "VERCEL_TOKEN": "vcp_4cys...", "VERCEL_TEAM_ID": "team_728D..." } },
        "transcript-api":  { "command": "C:/Python314/python.exe", "args": ["-u", ".../mcp-transcript-api.py"], "env": { "TRANSCRIPT_API_KEY": "${env:TRANSCRIPT_API_KEY}" } },
        "airtable":        { "command": "airtable-mcp-server.cmd", "args": [], "env": { "AIRTABLE_API_KEY": "${env:AIRTABLE_API_KEY}", "AIRTABLE_TOKEN": "${env:AIRTABLE_TOKEN}", "AIRTABLE_PAT": "${env:AIRTABLE_PAT}" } },
        "clickup":         { "command": "clickup-mcp-server.cmd", "args": [], "env": { "CLICKUP_API_TOKEN": "${env:CLICKUP_API_TOKEN}", "CLICKUP_API_KEY": "${env:CLICKUP_API_KEY}", "CLICKUP_WORKSPACE_ID": "${env:CLICKUP_WORKSPACE_ID}" } }
    }
}
```

**Restore** : copier ce JSON dans `~/.mcp.json` (root home, PAS `~/.claude/.mcp.json` qui n'existe pas). Remplacer `<USER>` par le nom Windows user cible.

---

## 5. Plugin cache fixes (P2 pattern override)

### 5.1 Desktop Commander `.mcp.json` (D6 Entry P2 fix 2026-06-23)

**Chemin** : `C:/Users/<USER>/.claude/plugins/cache/claude-plugins-official/desktop-commander/<VERSION>/.mcp.json`

**Contenu canon** :
```json
{
    "mcpServers": {
        "desktop-commander": {
            "command": "C:/Users/<USER>/AppData/Roaming/npm/desktop-commander.cmd",
            "args": []
        }
    }
}
```

**Note** : ce fichier n'est PAS upstream (git marketplace ignore). Il sera écrasé à chaque mise à jour plugin. **D7 workaround** : re-créer après update, OU migrer vers entry direct dans `~/.mcp.json`.

---

## 6. Backups horodatés (D4 no-hard-delete)

**`_TRASH_2026-06-23_clickup_rename/`** (3 fichiers, 16.3 KB total) :
- `.mcp.json.before_clickup_token_rename.bak` (5379 bytes) — pre-ClickUp env var fix
- `.mcp.json.before_airtable_token_fix.bak` (5445 bytes) — pre-Airtable TOKEN addition
- `.mcp.json.before_airtable_api_key_fix.bak` (5505 bytes) — pre-Airtable API_KEY canonical

**D4 doctrine** : backups jamais supprimés. Retraits → `_TRASH_<date>/`.

---

## 7. Test Key Pragma — procedure restore A0 (D6 doctrine)

A0 partage clés API inline en chat avec intention claire ("teste ça") :
1. Phase 1 : A0 colles PAT/refresh token dans le chat CC
2. Phase 2 : Agent `[Environment]::SetEnvironmentVariable(...)` User scope
3. Phase 3 : Test `curl` / CLI direct, capture proof (ID, count, status)
4. Phase 4 : A0 revoke + recreate dans service après confirmation
5. Phase 5 : A0 colles nouvelle clé en chat OU script masked SecureString

**Anti-patterns interdits** : refuser tester / supprimer env var sans A0 GO / pusher A0 vers UI Desktop / hardcoder clé.

---

## 8. Sister canon references (D4 cross-link)

| Document | Rôle |
|---|---|
| `wiki/hand_offs/premortem_plugin_durability_2026-06-23.md` | Pre-mortem 7 modes failure × 4 MCPs (Airtable/DC/Telegram/ClickUp) |
| `_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md` | D6 catalog append-only (11 entries 2026-06-23) |
| `_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md` | Anti-Paperclip doctrine |
| `_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` | AaaS sister (Airtable = first AaaS variant) |
| `wiki/hand_offs/handoff_mcp_persistence_v2_2026-06-16.md` | MCP wiring D6 lessons |
| `wiki/hand_offs/handoff_mcp_durable_config_2026-06-16.md` | MCP durability receipts |
| `wiki/hand_offs/handoff_mcp_transcript_api_restart_2026-06-21.md` | Transcript-API restart pattern |

---

## 9. Invariants 1an vérifiables (D1 receipts)

| Invariant | Source vérifiée |
|---|---|
| Backup `.mcp.json` (3 fichiers horodatés) | `~/.claude/_TRASH_2026-06-23_clickup_rename/` |
| Env vars User scope durables cross-session | `[Environment]::SetEnvironmentVariable(..., 'User')` PowerShell receipts |
| Plugin manifests immutable | `~/.claude/plugins/installed_plugins.json` symlink-stable |
| Pre-mortem canon immutable D4 | `wiki/hand_offs/premortem_plugin_durability_2026-06-23.md` v2 |
| D6 catalog append-only | 11 entries vérifiées 2026-06-23 |
| Skill candidate canon | `/mcp-envvar-auditor` (action #5 pre-mortem v2) |

**Résistance 1an minimum garantie par** :
1. Backups horodatés (D4)
2. Env vars User scope (Windows registry-backed, durable)
3. Pre-mortem canon (forward-looking risk)
4. D6 catalog (lessons shipped append-only)
5. Cross-machine restore procedure documentée (§1-5)

---

**D4 append-only** : v1 créé 2026-06-23. Updates → v2 avec ref cross-link. Retraits → `_TRASH_2026-06-23_mcp_export/`.
