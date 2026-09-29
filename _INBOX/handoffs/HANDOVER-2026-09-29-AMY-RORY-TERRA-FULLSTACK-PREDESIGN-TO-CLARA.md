# HANDOVER — 2026-09-29 — AMY + RORY → CLARA — TERRA FULL-STACK PREDESIGN

## Coordination
GitHub #243
`[LIFE-OS][TERRA][FULLSTACK][PREDESIGN] Maturity + Code-to-API convergence`

## Inputs
Amy:
`b4e56e7e73b1d68680b5758aafa8e156045299d1`

Rory:
`5f9ff47e3c14770413a9147012d84e17eb7736de`

Canonical Clara input:
`10_Tech_OS/reports/clara_input_terra_fullstack_api_unification_20260929.md`

## Maturity
Terra = **M3 Integrated Platform, pre-convergence**.

Do not interpret M3 as “unfinished UI”.
The product surface is broad and functional; the blocker is contract convergence.

## P0 design problems
- duplicate :3001 Business bridge implementations;
- duplicate browser clients;
- broken CLI/Linear endpoint assumptions;
- local outbox schema != Supabase schema;
- IndexedDB outbox migration not certified;
- absent migration RPC;
- Blackboard not activated/certified;
- B3 type contracts drifted;
- startup launcher points at legacy clone;
- release gate is not cross-platform.

## Clara mission
Turn existing Terra code into one coherent API/service architecture while preserving:
- React UI;
- local-first UX;
- Supabase RLS;
- event contracts;
- Blackboard concepts;
- MCP;
- CLI.

## Required output
Do not hand to Ryan until these are bounded:
1. canonical API runtime;
2. domain/application service layer;
3. endpoint retirement map;
4. persistence ownership matrix;
5. local/cloud concurrency + tombstone protocol;
6. DB migrations;
7. Blackboard role;
8. adapter/auth boundaries;
9. B3 canonical types;
10. runtime identity/startup;
11. cross-platform evidence gate;
12. reversible build waves.

Do not re-audit from scratch.
