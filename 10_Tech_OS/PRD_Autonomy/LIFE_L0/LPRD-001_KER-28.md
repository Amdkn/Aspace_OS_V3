# LPRD-001: Doctor11/Amy/Rory/River persistent session contracts

**Mandate**: KER-28
**Layer**: L0
**Core**: LIFE
**Manager**: DOCTOR11
**Companion**: AMY (Spec)

## Objective
Restore durable Life Core operating sessions and capability contracts: Amy=Spec, Rory=Build, River=Spawn/Knowledge, Doctor11=Review/detach. No companion owns sovereign Kernel state.

## Details
Add the `session_binding` and `harness_capability` tables to `10_Tech_OS/kernel/schema.sql` if they do not exist.
Add a trigger `loi_life_core_binding_capability` to `10_Tech_OS/kernel/schema.sql` to enforce:
- Amy is bound only to `Spec`.
- Rory is bound only to `Build`.
- River is bound only to `Spawn` or `Knowledge`.
- Doctor11 is bound only to `Review` or `detach`.
- Companions (Amy, Rory, River) are restricted from binding to `L0` layer sovereign state, explicitly exempting Doctor11.

Create tests to verify these contracts in `10_Tech_OS/kernel/test_life_core_contracts.py`.

## Rules
- Stay inside this Companion role and Core.
- If requirements are materially ambiguous or need human interaction, STOP implementation and propose an ADR clarification for the Doctor/Rick review path.
- Preserve Kernel/WorkGraph authority boundaries.
- Run focused tests/build/audit relevant to changed files.
- Do not use destructive git cleanup/reset.
- Create/continue a PR with durable evidence.
