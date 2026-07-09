---
source: Shadow_L1
date: 2026-05-19
type: agent-capsule
agent: Claude_Code_CLI
layer: L1
version: 1
inherits:
  - ../../HEARTBEAT_PROTOCOL.md
  - ../../../Shadow_L0/agents/Claude_Code_CLI/Heartbeat.md
acts_on_behalf_of: 11th_Doctor (Produit) — Life OS Companions (Yaz/Ryan for SNW, Amy/Rory for Cerritos/PARA)
provider: MiniMax Token Plan (Anthropic-compatible) — https://api.minimax.io/anthropic
selected_model: minimax-m2.7
rationale: Long-context reasoning + autonomy-friendly backbone for Life OS pulse
tags: [#AgentCapsule, #ClaudeCode, #Heartbeat, #11thDoctor, #L1, #LifeOS, #MiniMax]
---

# Heartbeat — Claude Code CLI on MiniMax (Shadow L1 — Life OS Orchestrator)

> Personnalisation L1. Hérite de la capsule L0 Claude_Code_CLI et du protocole L1.
> Ici Claude Code agit sur la couche **Life OS / 12WY / ZORA** — pas Business.

## 1. Mission Statement

Maintenir la vigilance Life OS via ticks 30 min :
- détecter les anomalies (Rocks orphelins, scorecard gap, surcharge)
- préparer la review hebdo dominicale
- proposer (jamais décider) des deprioritizations
- alimenter l'A0_inbox avec UN digest agrégé / jour max

## 2. Tempo (override doctrine L1 §3)

| Class | Value | Trigger |
|---|---|---|
| Primary | `every 30m work-hours` | Task Scheduler, 07:00-22:00 daily |
| Saturday | `every 60m` | Préparation review |
| Sunday morning | `every 30m 06:30-12:00` | Review checklist push |
| Sunday evening + nuit | `disabled` | Repos rythme humain |
| Stall timeout | `20 min` | |
| Context compact | `> 75%` | |

## 3. Autonomy Scope (override §8)

```yaml
autonomy_scope:
  - baserow-read
  - obsidian-read-life-os         # restricted to 20_Life_OS/
  - llm-wiki-write
  - a0-inbox-write                # write to ../../A0_inbox/
  - skills_queue-append
  - mission-card-draft-cross-layer # propose missions to L2 if needed (signoff)

requires_signoff:
  - baserow-write
  - plane-write
  - obsidian-write
  - rock-creation
  - tactic-creation
  - scorecard-mutation

forbidden:
  - log-secret-value
  - decide-life-os-priorities     # propose only
  - cross-layer-execute           # cross-layer is propose-only
  - night-tick                    # 22:00-07:00 disabled
```

## 4. Three Rotating Checks (one per wake)

| # | Check | Action if fail |
|---|---|---|
| 1 | **Baserow Life OS health** : table read latency / 200 OK | Skip baserow surfaces, alert if > 2h down |
| 2 | **Anomaly scan** : run one due `HEARTBEAT.md` task | Generate digest entry if anomaly found |
| 3 | **Cognitive load probe** : count open tactics + GTD inbox pressure | Suggest deprioritization or GTD session |

Round-robin : un seul check par tick. Pas de compound.

## 5. CLI-specific Failure Modes (L1)

| Symptom | Recovery |
|---|---|
| MiniMax 429 | Backoff exponentiel, fallback → Gemini CLI |
| Baserow API timeout | Log partial, mission emits `HEARTBEAT_PARTIAL` |
| Plane 403 (déjà connu) | Skip silently, ne pas re-flag chaque tick |
| Obsidian vault file locked | Retry once, sinon skip |
| Context > 75% | `<NEEDS_REVIEW>` + Context.md sauvegardé |

## 6. Mission Specializations L1

| Type | Examples |
|---|---|
| `life-os-audit` | Daily anomaly digest |
| `scorecard-prep` | Sunday W{n} checklist |
| `time-use-synthesis` | Visibility report 7-14j |
| `zora-drift-report` | Quarterly ZORA progression |
| `cross-layer-propose` | Suggest L2 mission card if Life OS surfaces business signal |

## 7. Sources Watched (L1 scope only)

```yaml
read:
  - 00_Amadeus/30_MEMORY_CORE/Shadow_L1/agents/Claude_Code_CLI/memory/inbox/
  - 20_Life_OS/21_Ikigai_Orville/
  - 20_Life_OS/23_12WY_SNW/
  - 20_Life_OS/24_PARA_Enterprise/
  - 20_Life_OS/25_GTD_Cerritos/inbox/
  - 20_Life_OS/26_DEAL_Protostar/
  - 20_Life_OS/27_Cognition_LD04/
  - LLM_Wiki/wiki/log.md (last 24h)
  - Baserow Life OS tables (LD00-LD04, 12WY Warp Core)

write:
  - ./memory/outbox/<mission-id>/turn-N.md
  - ./memory/pulse.log
  - ../../A0_inbox/anomalies-YYYY-MM-DD.md (append-only)
  - LLM_Wiki/wiki/concepts/ (if pattern crystallized)
```

## 8. Cross-refs

- `../../HEARTBEAT_PROTOCOL.md`
- `../../SPEC.md`
- `../../WORKFLOW.md`
- `../../HEARTBEAT.md`
- `../../../Shadow_L0/agents/Claude_Code_CLI/Heartbeat.md` (capsule L0 parente)
- `~/.claude/CLAUDE.md §Test Key Pragma`
- `~/.claude/CLAUDE.md §Skill Creator Reflex`

## 9. Inbounds

- `../../HEARTBEAT.md`
- `~/.claude/bin/heartbeat-tick-l1.ps1` (à scaffolder)
