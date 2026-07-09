---
source: LLM_Wiki_A0
date: 2026-05-17
type: concept
domain: A0_Sovereign / Agentic_Patterns
tags: [#Autonomous_Loop #Research #Compounding #AutoResearch #Shadow_L0]
---

# Concept — Autonomous Research Loop

## Definition

An **autonomous research loop** is the agentic pattern where :

1. A **frozen reference** (physics / canon / spec) ensures comparability between runs.
2. An **agent-mutable surface** (code / config / patches) is the hypothesis space.
3. A **human-curated direction** (intent / program.md / ADR) sets the research grant.
4. A **bounded experiment cost** (5-min training run / 12WY week / single PR) normalizes the unit of iteration.
5. A **measurable proxy of progress** (eval-loss / lint score / throughput) decides keep-or-discard.
6. The agent **chains many cheap trials** instead of relying on one expensive insight.

## Origin

[[source_karpathy-autoresearch|Karpathy's AutoResearch repo]] is the canonical minimal embodiment. The 3-file split (`prepare.py` / `train.py` / `program.md`) maps cleanly to the 3-actor split (canon-keeper / executor / pilot).

## A'Space Incarnations

| Loop scope | Frozen reference | Agent-mutable | Human direction | Cost unit | Progress proxy |
|---|---|---|---|---|---|
| A'Space code | AGENTS.md + ADRs | Shadow L0 mesh edits | A0 Intention (3-Turn) | 1 PR / 1 patch | wiki lint score |
| LLM Wiki growth | Schema rules | Wiki pages | New source ingest | 1 ingest pass | broken-link count |
| Shadow L1 ops | Plane/Baserow schemas | Payloads | A0 priority list | 1 work-item | auth-OK / data-flow |
| Shadow L2 connectors | API contracts | CLI wrappers | God Mode CLI doctrine | 1 `printing-press generate` | CLI test pass |
| 12WY weekly cycle | Annual GTD/PARA goals | Daily tasks | A0 weekly intent | 1 week (50/30/20) | scorecard delta |

## Critical Failure Modes

| Failure | Symptom | Mitigation |
|---|---|---|
| **Reward hacking** | Agent gaming the proxy (e.g. memorizing eval set) | Multi-metric reward + adversarial val splits |
| **Local optima** | Greedy keep/discard converges nearest hill | Inject exploration pressure via `program.md` updates |
| **Single-loss tyranny** | Optimizing 1 dimension breaks others | Add complementary objectives (interpretability, robustness) |
| **Frozen reference rot** | Canon drifts un-versioned | TARDIS Protocol — versioned, not overwritten |
| **Human bottleneck** | A0 becomes the rate limiter on `program.md` | Symphony router pre-shapes A0 ask into structured intents |

## Cross-Refs

- [[source_karpathy-autoresearch]] — Canonical source.
- [[entity_autoresearch]] — Entity for the repo.
- [[entity_shadow_l0_executor_mesh]] — A'Space's mesh implementation.
- [[source_llm-wiki-pattern]] — Sibling pattern (memory loop, not research loop).
- [[concept_compounding_knowledge]] — Why both loops compound.
- [[concept_e-myth]] — Visionary/Manager/Technician maps to pilot/canon-keeper/executor.

## Inbounds

- [[source_karpathy-autoresearch]]
- [[entity_autoresearch]]
