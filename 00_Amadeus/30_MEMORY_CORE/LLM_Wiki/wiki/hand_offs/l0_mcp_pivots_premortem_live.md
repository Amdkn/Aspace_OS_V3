---
target: L0 MCP pivots (Supabase × 3 / Vercel × 3 / Airtable × 2 / ClickUp × 2)
date: 2026-06-28
author: A0 jumeau numérique (Opus)
sister_canon:
  - ADR-L0-META-ORCH-001 (Hermes meta-orchestrator RATIFIED 2026-06-27)
  - ADR-META-006 D6 catalog (post-mortem inventory)
  - .claude/mindsets/Rick_Mindset.md (S1 sobriety)
premortem_run: P2.4b — 2026-06-28 (1er run, gate POST P2 GO A0)
auto_refresh: re-invoked on any F1-F15 trigger event
---

# L0 MCP Pivots — Premortem Live

## Scope
4 MCP pivots totalisent **10 serveurs** actifs dans `.mcp.json` (5 721 bytes, dernière modif 2026-06-23) :
- **Supabase** × 3 : `supabase` · `supabase-omk` · `supabase-abc`
- **Vercel** × 3 : `vercel` · `vercel-omk` · `vercel-abc`
- **Airtable** × 2 : `airtable` · `plugin_airtable_airtable`
- **ClickUp** × 2 : `clickup` · `2c79bb4b-...-clickup`

## D1 State Map (2026-06-28)

| Surface | claimed_state | actual_state | gap |
|---|---|---|---|
| `.mcp.json` | 10 serveurs enregistrés | ✅ 10 serveurs (D1 grep vérifié) | none |
| `.claude/settings.json` plugins | `airtable@claude-plugins-official: true` | ✅ | none |
| `.claude/settings.json` plugins | `supabase@claude-plugins-official: false` | D6 #1 catalogué (post-CC-restart 2026-06-23) | documented, gated A0 |
| `.cmd` binaries (F3) | présents dans PATH npm global | ✅ `vercel-mcp-pro.cmd` + `airtable-mcp-server.cmd` + `clickup-mcp-server.cmd` (D1 vérifié via `where`) | none |
| SessionStart digest | `✓ Connected` × 20+ | ✅ per SessionStart:compact | none |
| Hooks | `posttooluse-test-after-edit.ps1` (code-files only) | ✅ log-only (Rick-vetoed hard-block) | none |
| Watchdog MCP-dédié | absent | ❌ | F4 (A0_GO_REQUIRED) |

## F1-F15 Status (auto-verified 2026-06-28)

### ✅ OK (no remediation)
- **F7** auto-execution chain : aucun cron B1 sur ces MCP, Posture C respectée
- **F9** self-replication : pas de boucle auto-spawn détectée
- **F13** capability vs activation : 10 serveurs Connected = pas dormant
- **F14** gates pending >30j : D6 #1 entrée 5 jours, sous seuil
- **F15** dead handoff : 10 handoffs historiques, aucun "dead" récent

### SAFE_LOG_ONLY (executed + flagged, 4 actions)
- **F3** binary missing : 3/3 `.cmd` MCP vérifiés présents dans `~/AppData/Roaming/npm/` ✅
- **F8** prompt injection : MCP stdio = surface input → note canon `Rick_Mindset.md` §Anti-paperclip
- **F10** snapshot : `.mcp.json` versionné via backup manuel (D6 #5 lesson) — note canon
- **F12** orphan risk : 3 serveurs par cible (multi-instance) — note D6 catalog (token instance peut mourir isolément)

### A0_GO_REQUIRED (queued, NOT executed — 4 actions)
- **F2** plugin `supabase@claude-plugins-official: false` — activer ou laisser off ? (D6 #1 décision)
- **F4** watchdog MCP-dédié : pas de cron capturant `✗ Failed` MCP runtime
- **F6** heartbeat connexion `l0-watchdog-scrape` skill aux 4 MCP — skill existe, pas wired
- **F11** rollback script MCP — pas de procédure de restauration `.mcp.json` en cas de corruption

## Cron activity log
- `OWNER mode: no parent seq=21` (digest SessionStart, OWNER loop inactif)
- Aucun cron A1→B1 sur ces MCP (Posture C respectée)

## Pending A0 actions
Voir `l0_mcp_pivots_premortem_pending_actions.md` (live queue).

## Sister canon links
- [ADR-L0-META-ORCH-001](../_SPECS/ADR/L0_Tech_OS/ADR-L0-META-ORCH-001_hermes-meta-orchestrator.md) — Hermes méta-orchestrateur runtime
- [Rick_Mindset.md](../../../../../../.claude/mindsets/Rick_Mindset.md) — S1 sobriety + anti-paperclip
- [ADR-META-006 D6 catalog](../_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md) — entrée #1 airtable/clickup post-CC-restart 2026-06-23

## Next run
Re-invoquer `/premortem-fill l0-mcp-pivots` après tout trigger F1-F15 (nouvelle entrée D6, plugin toggle, MCP ✗ Failed, cron creation).
