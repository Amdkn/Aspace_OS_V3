---
name: symphony-pilot-runtime
description: Phase 2 Runtime dispatcher — polls Plane PROJECT_ID `79df867c-06b5-4e61-b3f1-68aa886c39a3` for Today issues, routes via A1/A2/A3 canon matrix (12 items Q3 2026), spawns A3 sub-agents, appends state.json (state-bus.v1) + wiki/log.md. Wires /multi-routines-12wy → Plane durable dispatch.
---

# /symphony-pilot-runtime — A0 Phase 2 Runtime

> **Doctrine ancrage** : ADR-META-001 D1-D8 (Verify, Research, Nuance, No-Contradiction, Proof, Root-cause, Cost-of-Escalation, Cross-agent) + ADR-SOBER-002 (Anti-MAXIMIZER, KISS ≤80 lignes runtime, **stdlib only — 0 pip install requis**).

## Usage

```bash
python "C:/Users/amado/.claude/skills/symphony-pilot-runtime/symphony_pilot_runtime.py" --once --dry-run
python "C:/Users/amado/.claude/skills/symphony-pilot-runtime/symphony_pilot_runtime.py" --poll-interval=1800
```

## Prérequis

- `PLANE_API_TOKEN` env var User scope (D8 — Test Key Pragma)
- `claude` CLI accessible (CC subprocess)
- **stdlib only** (json/os/subprocess/sys/time/urllib/pathlib) — **0 pip install requis** (D6 root cause fix : SKILL.md initiale disait httpx mais runtime = stdlib only)

## Fixes crash silencieux (Goal 2026-06-23)

1. **state-bus.v2 JSONL append-only** : `wiki/state.jsonl` au lieu de `state.json` (OVERWRITE → APPEND). Chaque tick = 1 ligne JSON. Tick counter in-memory monotonique.
2. **heartbeat.jsonl sibling** : cross-check file pour détecter drift.
3. **log.md timestamp ISO 8601 unique** : chaque entry préfixée `[YYYY-MM-DDTHH:MM:SS+ZZ]`.
4. **stderr verbose logging** : subprocess errors loggés même si exit code != 0 (D1 receipts).
5. **Stop hook TTS SAPI Hortense** wired dans `~/.claude/settings.json` (Stop event → beep + speak).

## Livrables

- `state.json` atomic append (state-bus.v1) à chaque tick
- `wiki/log.md` 1-line entry par issue dispatché
- Drift flag si sub-agent fail (D6 root-cause, pas de retry aveugle)

## Sister skills

- `/multi-routines-12wy` (12 items Q3 2026 canon matrix)
- `/multi-goal` (8 sub-agents // par outcome)
- `/multi-loop-karpathy` (Capture→Process→Persist→Loop, extends /loop au-delà 7j)