---
name: multi-loop-karpathy
description: Multi-agent Karpathy auto-research loop — spawns 8 sub-agents in parallel per iteration, persists to canon via state.json, schedules via /routine for cycle duration. Replaces /loop native CC (7-day bound) with CronCreate + ScheduleWakeup for 12WY cycles.
---

# /multi-loop-karpathy — A0 Multi-Iteration Research Loop

> **Skill Symphony Multi-Workflow** — invocable par A0 Amadeus via `/multi-loop-karpathy <topic> [<cadence>] [<duration>]`.
>
> **Complément de** : `/loop` natif CC (borné 7 jours, session-scoped). `/multi-loop-karpathy` étend à multi-iteration cycle-aware via Karpathy auto-research pattern + Symphony twin.

## Différence vs /loop natif CC

| Aspect | `/loop` natif | `/multi-loop-karpathy` |
|---|---|---|
| Durée max | 7 jours (auto-expire) | Cycle 12WY = 84 jours (ou plus) |
| Agents | 1 (Main Agent repeat) | 8+ sub-agents // par itération |
| State | Session memory | `state.json` persistant + `log.md` canon |
| Karpathy pattern | ❌ absent | ✅ Capture → Process → Persist → Loop |
| Cron anchor | absent | CronCreate ou ScheduleWakeup |
| A1 routing | linear | Morty → Cerritos Mariner + SNW Ortegas |

## Workflow canonique (5 steps)

### Turn 1 — Air Lock Clarification

`/multi-loop-karpathy` demande à A0 :
1. **Topic recherche** : quel sujet à itérer ? (e.g. "Life-OS-2026 V2.0 readiness")
2. **Cadence** : daily / weekly / monthly
3. **Duration** : cycle 12WY = 84 jours (W1-W12) ou custom
4. **Stop condition** : quand arrêter la boucle ? (e.g. "ship BETA V2.0" ou "GO detection")

### Turn 2 — Route A1 Morty → A2 Cerritos + SNW

**Capture phase** : A2 Cerritos Holodeck → A3 Mariner (capture inbox permanent)
**Execution phase** : A2 SNW Curie → A3 Ortegas (daily standup / real-test-after-edit discipline)

### Turn 3 — Spawn Karpathy Loop = 8 sub-agents // par itération

**Pattern Phase 2 canon** (`symphony-phase2-batch` SKILL.md) :
- 1 sub-agent re-twin A1+A2
- 6 sub-agents A3 twins (1/ship)
- 1 sub-agent MCPs (4 servers)
- 1 sub-agent bridges (6 wirings)

Karpathy 4-step appliqué à chaque itération :
1. **Capture** : sub-agents lisent source canon (handoff/ADR/transcript/data MCP)
2. **Process** : appliquent Agent OS standard (api/response-format + global/coding-style) + ADR-META-001 D1-D8
3. **Persist** : écrivent dans `state.json` + `log.md` canon (D4 append-only)
4. **Loop** : `next_step` pointe vers prochaine itération tant que `stop_condition` non remplie

### Turn 4 — Cron anchor (remplace /loop 7-day bound)

`/multi-loop-karpathy` configure :
- `CronCreate` (persistent, bornée cycle 12WY) **OU**
- `ScheduleWakeup` (in-session, bornée session CC)

Bornes typiques :
- **Daily iterations** : cron `0 8 * * *` (8h chaque jour)
- **Weekly iterations** : cron `0 8 * * 1` (lundi 8h)
- **Cycle 12WY** : cron custom (12 invocations sur 84 jours)

### Turn 5 — Loop detection + GO trigger

Si `state.json.stop_condition` = OK :
- Retourne `<DONE>` au Main Agent
- TTS SAPI Hortense : "Recherche terminée. Objectif atteint."

Sinon :
- Cron relance nouvelle itération
- Sub-agents re-spawnent
- Loop continue jusqu'à GO

## Doctrine ancrage

- **D1 verify-before-assert** : state.json.stop_condition lu + vérifié avant `<DONE>`
- **D2 research-first** : canon lu AVANT spawn sub-agents
- **D4 no-self-contradiction** : log.md append-only, state.json versionné
- **D7 cost-of-escalation** : 8 sub-agents // par itération × N itérations = ROI exponentiel
- **D8 cross-agent** : Claude + Codex + Gemini respectent matrice

## Fichiers canon liés

- `C:\Users\amado\.claude\commands\routine.md` — orchestrateur 3-tiers (utilisé par /multi-loop-karpathy)
- `C:\Users\amado\.claude\skills\symphony-phase2-batch\SKILL.md` — Phase 2 = 8 sub-agents // precedent
- `C:\Users\amado\.claude\skills\symphony-fabuleux-discipline\SKILL.md` — doctrine
- `C:\Users\amado\.claude\rules\fable-autor-research-loop-symphony-agentos.md` — Karpathy doctrine
- `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L1_Life_OS\ADR-MEMO-000_auto-research-karpathy-loop-claude-code_DRAFT.md` — ADR Karpathy loop
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_a0_divinity_arsenal_2026-06-20.md` — A0 doctrine

## Usage

```
/multi-loop-karpathy <topic> [<cadence>] [<duration>]
```

Exemples :
- `/multi-loop-karpathy "Life-OS-2026 V2.0 readiness" weekly 84d`
- `/multi-loop-karpathy "Saru 1000T Anti-paperclip check" daily 30d`
- `/multi-loop-karpathy "Symphony twin runtime status" daily 7d`