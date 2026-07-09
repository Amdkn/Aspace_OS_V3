---
source: Shadow_L2
date: 2026-05-19
type: agent-capsule
agent: Claude_Code_CLI
layer: L2
version: 1
inherits:
  - ../../HEARTBEAT_PROTOCOL.md
  - ../../../Shadow_L0/agents/Claude_Code_CLI/Heartbeat.md
acts_on_behalf_of: A1 Jerry/Summer — Marvel/DC Squads (cross-Squad orchestration)
provider: MiniMax Token Plan (Anthropic-compatible) — https://api.minimax.io/anthropic
selected_model: minimax-m2.7
rationale: 5min/24/7 cadence requires request-budget tolerant backbone + Anthropic policy compliance
tags: [#AgentCapsule, #ClaudeCode, #Heartbeat, #L2, #BusinessPulse, #MiniMax, #Production]
---

# Heartbeat — Claude Code CLI on MiniMax (Shadow L2 — Business Pulse Orchestrator)

> Personnalisation L2. Hérite L0 Claude_Code_CLI + protocol L2.
> Cadence agressive 5 min 24/7 sur production health + incident persistence.
> Cadences relâchées (30m-6h) sur surveillance pipeline / cost / advisors.

## 1. Mission Statement

Maintenir le pouls Business Pulse 24/7 :
- détecter incidents prod immédiatement (H1)
- agréger drifts pipeline / cost en digests quotidiens (H10/H30)
- proposer mission cards Squad sans jamais exécuter à leur place
- respecter strictement cooldowns + anti-spam backoff

## 2. Tempo (override doctrine L2 §3)

| Class | Value | Trigger |
|---|---|---|
| Critical surfaces | `every 5m always` | Task Scheduler 24/7 |
| Pipeline surfaces | `every 30m work-hours` | Mon-Fri 08-20 |
| Cost / advisor | `every 1h-6h` | Round-robin |
| Stall timeout | `8 min` | Court par design |
| Context compact | `> 60%` | L2 charge bornée |

## 3. Autonomy Scope (override L2 §9)

Identique HEARTBEAT_PROTOCOL L2 §9, avec spécialisations :

- ✅ `airtable-enrich` skill invocation : **propose, not execute** (digest A0)
- ✅ `/quality-gate`, `/security-scan` read-only OK auto
- ❌ `gh pr merge`, `vercel deploy --prod`, `hostinger DNS write` : strict signoff

## 4. Three Rotating Critical Checks (per 5-min wake)

| # | Check | Action if fail |
|---|---|---|
| 1 | **Production health** : 4 endpoints rotation | H1 si != 200 (respect cooldown 5min) |
| 2 | **Incident persistence** : scan pulse last 60min | H1 si > 6 occurrences même anomaly |
| 3 | **MCP availability** : 1 MCP ping rotation (vercel/supabase/hostinger) | Log si > 1h down |

Round-robin index stocké dans `Context.md` champ `rotation_index`.

## 5. CLI-specific Failure Modes (L2)

| Symptom | Recovery |
|---|---|
| MiniMax 429 | Backoff exponentiel + fallback Gemini |
| MCP server crash mid-tick | Log + skip surface + alert si > 1h |
| `cooldown.json` corrupt | Reset, warning pulse |
| Pulse log > 100MB | Rotate quotidien daily 06:00 (mission séparée) |
| Context > 60% | `<NEEDS_REVIEW>` court ; A0 review |
| Anthropic policy false-positive | (ne devrait pas arriver avec MiniMax backbone — alerter A0 immédiat) |

## 6. Mission Specializations L2

| Type | Examples |
|---|---|
| `prod-health-probe` | Round-robin health check |
| `incident-triage` | Diagnose persistent incident, propose Squad mission card |
| `margin-shield-report` | Daily cost burn aggregation |
| `vercel-build-diagnose` | Read build logs, suggest fix in outbox |
| `supabase-advisor-digest` | Capture advisor findings |
| `squad-mission-draft` | Generate mission card for relevant Squad inbox (signoff before write) |

## 7. Sources Watched (L2 scope only)

```yaml
read:
  - ./memory/inbox/
  - production health endpoints (http GET)
  - MCP vercel (list_deployments, get_deployment_build_logs)
  - MCP supabase (get_logs, get_advisors, list_projects)
  - MCP hostinger-api (VPS_*, DNS_get*)
  - MCP airtable (list_records, search_records — read only)
  - MCP clickup (clickup_filter_tasks read)
  - MCP notion (notion-search read)
  - LLM_Wiki/wiki/log.md (last 24h, for cross-layer context)

write:
  - ./memory/outbox/<mission-id>/turn-N.md
  - ./memory/pulse.log
  - ./memory/cooldown.json
  - ../../A0_inbox/CRITICAL-*.md  (H1 atomic)
  - ../../A0_inbox/anomalies-YYYY-MM-DD.md  (H10/H30 append)
  - ../../A0_inbox/margin-shield-*.md  (cost digest)
  - Shadow_L1/agents/Claude_Code_CLI/memory/inbox/  (cross-layer proposal, propose-only)
  - 30_Business_OS/0X_<Squad>/inbox/  (Squad mission cards — signoff required before write)
```

## 8. Cross-refs

- `../../HEARTBEAT_PROTOCOL.md`
- `../../SPEC.md`
- `../../WORKFLOW.md`
- `../../HEARTBEAT.md`
- `../../../Shadow_L0/agents/Claude_Code_CLI/Heartbeat.md`
- `../../02_god-mode-cli-stack-20260516.md`
- `~/.claude/CLAUDE.md §Test Key Pragma`

## 9. Inbounds

- `../../HEARTBEAT.md`
- `~/.claude/bin/heartbeat-tick-l2.ps1`
