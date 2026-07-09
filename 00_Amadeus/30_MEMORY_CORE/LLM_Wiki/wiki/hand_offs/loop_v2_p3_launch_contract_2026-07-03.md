---
title: P3 Graphify re-sync launch contract (next attended run)
date: 2026-07-03
author: CC-M3 loop-operator (loop v2)
layer: L0 - Tech OS / Graphify corpus
status: CONTRACT - sandbox=ON, A0 attendu, prochaine session
tags: [#loop #yellow-gate #p3 #graphify #launch-contract #sandbox-on]
blast_radius: 252 MB corpus (master + 49 junctions)
related:
  - skills/graphify-swarm-burst/SKILL.md
  - .claude/memory/wiki/ (junction LLM_Wiki canon)
source: CC-M3 loop-operator (loop v2, Fable 5)
type: handoff
domain: L0_Tech_OS
---

# P3 Graphify re-sync - Launch Contract (attended only)

## Pourquoi PAS ce loop

Loop v2 = sandbox=OFF, A0 attending, scope = Red/Green/White. P3 = sandbox=ON requis (D6: graphify master merge = 252 MB, blast radius eleve, race conditions Windows).

D6 lessons shipped (CLAUDE.md Graphify block) : TIMEOUT_S=600, SKIP_DIRS absolut bug, WSL bash broken, race condition chunk flush, community field int cast.

## Pre-req A0 (avant prochaine attended run)

1. **Sandbox = ON** (ADR-LOOP-002 loi 3 stricte)
2. **A0 HITL present** (pas AFK)
3. **Cible = 1-3 app subsets** (PAS full corpus 252 MB blast) :
   - Option A : `.claude/` (self canon, scoped graphify)
   - Option B : `agent-os/` (Brian Casel Builder Methods, ~40 MB)
   - Option C : `.hermes/` (runtime, ~30 MB)
4. **INCREMENTAL=1** (D2: ne pas tout re-graphifier, juste le delta depuis dernier marker)
5. **TIMEOUT_S=600** (D6 #1, .md-heavy)

## Commande ready-to-paste

```bash
APPS=".claude" INCREMENTAL=1 TIMEOUT_S=600 PYTHONIOENCODING=utf-8 "C:/Python314/python.exe"   "C:/Users/amado/.claude/skills/graphify-swarm-burst/scripts/graphify_swarm.py"
```

Suivi de :

```bash
PYTHONIOENCODING=utf-8 "C:/Python314/python.exe"   "C:/Users/amado/.claude/skills/graphify-swarm-burst/scripts/graphify_master_merge.py"
```

## Verifie post-run

- `app-.claude/graph.json` mis a jour
- Master merge : nodes/edges deltas raisonables (<10% du master)
- Pas de rc=1 chunks partiels (D6 #6 = log warning + continue)
- `.graphify_semantic_marker` timestamp frais

## Owner / Timing

A0 + CC-M3. Prochaine attended session (W4 lundi 2026-07-06 ideal).
