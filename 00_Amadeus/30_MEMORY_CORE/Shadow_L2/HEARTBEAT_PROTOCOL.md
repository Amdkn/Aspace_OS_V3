---
source: Shadow_L2
date: 2026-05-19
type: doctrine
status: DRAFT_ACTIVE
domain: Shadow_L2 / Heartbeat / Business_Pulse / Symphony
inherits: ../Shadow_L0/HEARTBEAT_PROTOCOL.md
anchors:
  - Shadow_L0/HEARTBEAT_PROTOCOL.md
  - LLM_Wiki/wiki/concepts/concept_shadow_l1_l2_heartbeat_symphony.md
  - Shadow_L2/02_god-mode-cli-stack-20260516.md
tags: [#Heartbeat, #ShadowL2, #BusinessPulse, #ClaudeCode, #MiniMax, #Symphony, #Production]
---

# HEARTBEAT_PROTOCOL — Shadow L2 (Business Pulse)

> Hérite de `Shadow_L0/HEARTBEAT_PROTOCOL.md`. Spécialise pour la couche
> **Business Pulse** : production, growth, finance, delivery, operations.
>
> Orchestrateur principal : **Claude Code CLI on MiniMax Token Plan**.
> Cadence agressive : **5 min 24/7** (MiniMax request budget rend ça viable).

## 1. Mission de Shadow L2

Shadow L2 = pouls **Business Pulse Fractal (Marvel/DC Squads)** :

| Squad | Domaine surveillé |
|---|---|
| 01 GreenLantern / X-Men | People, RH, contracts |
| 02 Cyborg / Kang Dynasty | IT, infra prod, MCP, deployments |
| 03 Batman / Fantastic Four | Ops, delivery, incidents |
| 04 Flash / Avengers | Product, app health, release |
| 05 Superman / Guardians | Growth, leads, marketing, content |
| 06 Wonder Woman / Thunderbolts | Finance, margin, cost/burn |
| 07 Aquaman / Eternals | Legal, compliance |
| 08 John Jones / Illuminati | Sales, pipeline, CRM |

Shadow L2 **alerte sur les déviations business** : production down, lead pipeline drift, margin shield breach, incident.

## 2. Pourquoi Claude Code sur MiniMax orchestre L2

| Critère | Justification |
|---|---|
| Request budget MiniMax | Ticks 5 min × 288/jour = ~8.5k ticks/mois — viable seulement avec Token Plan |
| Anthropic policy | Anthropic refuse unattended Claude SDK. MiniMax backbone = workaround légal documenté |
| Reasoning | Détection signaux faibles (margin drift subtil, lead archetype shift) |
| Skill ecosystem | `/airtable-enrich`, `/security-scan`, `/code-review`, `/quality-gate` directement accessibles |
| Tool surface | `gh`, `vercel`, `supabase`, `hostinger`, `airtable`, `clickup`, `notion` MCPs disponibles |
| Fallback | MiniMax 429 → Gemini CLI (Forge 12th Doctor default) |

## 3. Cadence Cible

| Tempo | Valeur | Trigger |
|---|---|---|
| Production health | `every 5m always` | Task Scheduler 24/7 |
| Lead pipeline | `every 30m work-hours` | Mon-Fri 08:00-20:00 |
| Margin shield | `every 6h` | Round-robin |
| Incident watch | `every 5m always` | Couplé prod health |
| Stall timeout | `8 min` | Tick L2 court par design |
| Context compact | `> 60%` | L2 charge contextuelle bornée par tick |

**Active hours = 24/7** pour production health + incident watch. Les autres checks suivent business hours.

## 4. No-Empty-Heartbeat Rule (renforcée L2)

Un tick L2 5min/24/7 = risque #1 de bruit. Conditions obligatoires :

1. Au moins une source L2 prouvée joignable (`200` sur health endpoint connu)
2. `tasks:` block avec un check dû à ce tick (round-robin par interval)
3. Pas dans cooldown post-alerte (30 min après alerte → tick silencieux sur même anomaly_id)
4. Run précédent non bloqué `in-progress`

Sinon → `HEARTBEAT_OK` sans appel CLI (économie tokens critique à cette cadence).

## 5. Readiness Gates (état au 2026-05-19)

| Gate | État | Bloqueur |
|---|---|---|
| Capsule Claude_Code_CLI L2 existe | ✅ (créé) | — |
| HEARTBEAT.md L2 avec tasks | ✅ (créé) | — |
| MiniMax key valide | ✅ | — |
| Vercel API token | ⏳ à confirmer | — |
| Supabase MCP up | ✅ | — |
| Hostinger MCP | ✅ | — |
| Airtable MCP A'Space | ✅ | — |
| ClickUp MCP | ✅ | — |
| First supervised run | ❌ pending | A0 validation |
| Task Scheduler entries | ❌ disabled | Attente supervised |

## 6. Surfaces Observées (PROBE L2)

```yaml
surfaces:
  production_apps:
    - solaris.kalybana.com (health endpoint, supabase)
    - omkservices.com (vercel deployment)
    - marinacleaning.* (delivery client)
    - alykaly-os.* (internal)
    method: HTTP GET /health or root 200 check
    cadence: 5m

  airtable_marketing:
    base_ids: <vars AIRTABLE_*_BASE>
    watched: 1-Raw → 2-Enrichi pipeline state
    cadence: 30m

  clickup_workspace:
    team_id: <CLICKUP_TEAM_ID>
    watched: pipeline tasks, overdue, blockers
    cadence: 30m

  hostinger_vps:
    method: MCP VPS_getVirtualMachinesV1
    watched: VPS up, CPU/mem metrics
    cadence: 15m

  vercel_deployments:
    method: MCP list_deployments
    watched: failed builds last 24h
    cadence: 10m

  supabase_logs:
    method: MCP get_logs + get_advisors
    cadence: 1h

  cost_burn:
    sources:
      - MiniMax dashboard (manual digest weekly)
      - Anthropic console (if used)
      - Vercel usage
      - Hostinger billing
    cadence: 6h
```

## 7. Anomaly Catalog L2

| ID | Condition | Severity | Action |
|---|---|---|---|
| `L2-A01` | Production app health != 200 | H1 (CRITICAL) | Alert A0 immédiat + pulse.log + A0_inbox |
| `L2-A02` | Vercel deployment failed last 1h | H10 | Anomaly digest + suggest rollback |
| `L2-A03` | Hostinger VPS CPU > 85% sustained 15m | H10 | Alert + metrics snapshot |
| `L2-A04` | Hostinger VPS disk > 90% | H10 | Alert + cleanup suggestion |
| `L2-A05` | Airtable Raw queue > 100 leads non-enrichis 24h | H30 | Suggest `/airtable-enrich` batch |
| `L2-A06` | ClickUp overdue tasks > 10 | H30 | Digest A0_inbox |
| `L2-A07` | Supabase advisor flags security issue | H1 | Alert immédiat + capture advisor output |
| `L2-A08` | Supabase logs error rate spike (>5x baseline) | H10 | Alert + log excerpt |
| `L2-A09` | MiniMax quota < 10% remaining | H10 | Alert A0, suggest temporary Opus switch |
| `L2-A10` | Cost burn > threshold (defined per service) | H30 | Margin shield digest |
| `L2-A11` | Incident persistant > 30 min (même anomaly_id) | H1 | Escalate, suggest mission card |

## 8. Severity → Cooldown Mapping

| Severity | Cooldown post-alerte | Rationale |
|---|---|---|
| H1 (CRITICAL) | 5 min | Re-check vite, mais pas spam |
| H10 | 30 min | |
| H30 | 2h | |
| H90 | 24h | |

Cooldown stocké dans `memory/cooldown.json` (anomaly_id → expiry_ts).

## 9. Autonomy Scope L2

```yaml
autonomy_scope:
  - http-get-health-endpoints
  - mcp-read-vercel
  - mcp-read-supabase
  - mcp-read-hostinger
  - mcp-read-airtable
  - mcp-read-clickup
  - airtable-write-with-dry-run     # /airtable-enrich pattern OK
  - a0-inbox-write
  - skill-invoke (read-only skills only: /quality-gate, /security-scan, /code-review)
  - mission-card-draft-for-squads   # propose to relevant Squad inbox

requires_signoff:
  - airtable-write-without-dry-run
  - clickup-write
  - notion-write
  - vercel-deploy
  - hostinger-mutate                # any non-read MCP call
  - supabase-mutate
  - prod-rollback
  - dns-change

forbidden:
  - log-secret-value
  - delete-without-trash
  - dns-write-without-snapshot
  - cross-layer-execute-l1          # L2 propose to L1, never execute L1
  - bypass-margin-shield-alerts
```

## 10. Fallback Chain L2 (renforcé production-tier)

| Failure | Fallback |
|---|---|
| MiniMax 429 | → Gemini CLI (12th Doctor preferred fallback) |
| MiniMax token plan epuise | → Gemini CLI ; if also 429 → Codex CLI 5-turn cap |
| Production health endpoint timeout | Retry 3× exponential ; if still down → H1 alert |
| MCP server disconnect | Log + skip surface ; alert if > 1h |
| Both Claude+Gemini quota down | Codex CLI dernier recours, alerts only (no analysis) |
| Cooldown table corruption | Reset cooldown.json, log warning |

## 11. Output Surfaces L2

| Output | Destination | Format |
|---|---|---|
| H1 alert | `A0_inbox/CRITICAL-YYYY-MM-DD-HHMM.md` | One file per H1, atomic |
| H10/H30 digest | `A0_inbox/anomalies-YYYY-MM-DD.md` | Append, max 1 file/day |
| Margin shield report | `A0_inbox/margin-shield-YYYY-MM-DD.md` | Daily summary if drift |
| Cross-layer L1 proposal | `Shadow_L1/agents/Claude_Code_CLI/memory/inbox/` | Mission card |
| Squad mission card | `30_Business_OS/0X_<Squad>/inbox/` (à créer) | Mission card |
| Pulse signal | `memory/pulse.log` | `ISO_TS \| signal \| surface \| anomaly_id \| severity \| duration_ms` |
| Wiki concept | `LLM_Wiki/wiki/concepts/` | Si pattern cristallisé |

## 12. Anti-Patterns L2-Specific

1. **Tick 5 min consommant des tokens à vide** — toujours respecter no-empty-rule + cooldown
2. **Auto-rollback prod** — toujours signoff A0
3. **Re-alerter chaque tick sur même anomaly** — cooldown obligatoire
4. **Décider à la place du Squad** — L2 propose mission card, Squad exécute
5. **Logger secrets MCP / tokens** — variable names only
6. **Cross-layer L2→L1 sans mission card** — toujours via inbox L1
7. **DNS / prod-deploy sans snapshot** — Hostinger DNS toujours snapshot avant change
8. **Margin shield silencieux** — burn > seuil DOIT alerter, jamais swallow
9. **Re-derive surface state à chaque tick** — utiliser cache pulse.log + cooldown

## 13. Activation Procedure

1. Set `MINIMAX_API_KEY`, `ANTHROPIC_BASE_URL=https://api.minimax.io/anthropic`
2. Confirmer MCPs vercel/supabase/hostinger/airtable/clickup `200` ping
3. Run `heartbeat-tick-l2.ps1 --supervised --once`
4. A0 inspecte outbox + pulse.log + cooldown.json
5. Si OK → activer Task Scheduler `ASpace-Heartbeat-L2-Claude-MiniMax-5min`
6. Surveiller 24h en mode supervised (alertes H1 = SMS/notif si configuré)
7. Bascule autonomous après 12h pulse non-spam

## 14. Cross-refs

- `../Shadow_L0/HEARTBEAT_PROTOCOL.md`
- `../Shadow_L1/HEARTBEAT_PROTOCOL.md`
- `./SPEC.md`
- `./WORKFLOW.md`
- `./HEARTBEAT.md`
- `./agents/Claude_Code_CLI/Heartbeat.md`
- `./02_god-mode-cli-stack-20260516.md`
- `LLM_Wiki/wiki/concepts/concept_shadow_l1_l2_heartbeat_symphony.md`

## 15. Inbounds

- `./SPEC.md`
- `./WORKFLOW.md`
- `./HEARTBEAT.md`
- `./agents/Claude_Code_CLI/Heartbeat.md`
- `~/.claude/bin/heartbeat-tick-l2.ps1` (à scaffolder)
