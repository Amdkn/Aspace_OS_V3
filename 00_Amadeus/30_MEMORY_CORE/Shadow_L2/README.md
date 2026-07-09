---
source: A0_MEMORY_CORE
date: 2026-05-19
type: shadow-l2-index
status: ACTIVE
domain: Shadow_L2 / Business_Pulse / Symphony
tags: [#ShadowL2, #BusinessPulse, #ClaudeCode, #MiniMax, #Symphony, #Production]
---

# Shadow L2

Shadow L2 = **couche pouls Business Pulse Fractal** (Marvel/DC Squads).
Orchestrée par Claude Code CLI on MiniMax Token Plan, cadence agressive 5 min 24/7.

## Source De Verite

| Fichier | Role |
|---------|------|
| `README.md` | Index Shadow L2 (ce fichier) |
| `HEARTBEAT_PROTOCOL.md` | **Doctrine pulse L2 (Symphony adapted)** — héritage de Shadow_L0 |
| `SPEC.md` | Spec mesh Shadow L2, acceptance criteria |
| `WORKFLOW.md` | Mission lifecycle L2 + Squad routing map |
| `HEARTBEAT.md` | `tasks:` block lu par `heartbeat-tick-l2.ps1` |
| `agents/Claude_Code_CLI/Heartbeat.md` | Capsule orchestrateur (MiniMax, 5min cadence) |
| `agents/Claude_Code_CLI/Agent.md` | Identité cross-Squad (Jerry/Summer) |
| `agents/Claude_Code_CLI/Tools.md` | Surface capability L2 (MCPs full) |
| `agents/Claude_Code_CLI/memory/cooldown.json` | Anti-spam state (anomaly_id → expiry) |
| `A0_inbox/` | CRITICAL alerts (H1 atomiques) + digests quotidiens |
| `00_picard-phase-1-summary-20260517.md` | Historique Picard phase 1 |
| `01_mcp-shadow-l2-config-20260516.md` | Config MCP L2 (source de vérité) |
| `02_god-mode-cli-stack-20260516.md` | Stack CLI A'Space (concept parent) |
| `03..06_migration-reports-*.md` | Rapports migration apps (Solaris, OMK, Marina, Alykaly) |

## Cadence Cible

| Surface | Tempo | Active hours |
|---|---|---|
| Production health | 5 min | 24/7 |
| Incident persistence | 5 min | 24/7 |
| Supabase advisors | 1 h | 24/7 |
| Vercel build failures | 10 min | 24/7 |
| Hostinger VPS pressure | 15 min | 24/7 |
| Airtable raw queue | 30 min | 08:00-20:00 |
| ClickUp overdue | 30 min | 08:00-20:00 |
| MiniMax quota | 1 h | 24/7 |
| Margin shield | 6 h | 24/7 |

## Principe

Shadow L2 ne décide pas. Il alerte + propose mission cards Squad.
Tout mutate (deploy/DNS/PATCH) requiert signoff A0.

## État Actuel (2026-05-19)

| Composant | État |
|---|---|
| Structure fichiers | ✅ créée |
| `heartbeat-tick-l2.ps1` | ⏳ à scaffolder |
| Task Scheduler `ASpace-Heartbeat-L2-5min` | ❌ disabled (attendu) |
| Premier supervised run | ❌ pending validation A0 |
| `phase_enabled` dans HEARTBEAT.md | `false` |

## A Lire Avant Action

1. `../Shadow_L0/HEARTBEAT_PROTOCOL.md` (doctrine mère)
2. `./HEARTBEAT_PROTOCOL.md` (spécialisation L2)
3. `./HEARTBEAT.md` (tasks block)
4. `./agents/Claude_Code_CLI/Heartbeat.md` (capsule)
5. `LLM_Wiki/wiki/concepts/concept_shadow_l1_l2_heartbeat_symphony.md`

## Cross-refs

- `../Shadow_L0/` (canonical pulse doctrine)
- `../Shadow_L1/` (Life OS pulse — distinct couche)
- `LLM_Wiki/wiki/concepts/concept_god_mode_cli_stack.md`
