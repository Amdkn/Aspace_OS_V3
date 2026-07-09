---
id: B1_DIRECTION_INDEX
layer: B1_DIRECTION
status: SHADOW_ACTIVE
updated: 2026-05-26
---

# Jerry Area Direction - LD01 Business

This folder is the B1 direction cockpit. It exists so Jerry or Summer can pass strategy to B2 managers without forcing B3 technicians to infer intent from scattered notes.

## Operating Rule

B1 owns direction and packet structure. B2 owns domain Definition of Done and gates. B3 owns execution, proof, Lead indicators, Lag indicators, and blocker reports.

## Files

1. 01_NORTH_STAR_1Y_3Y_10Y.md - 1-year, 3-year, and 10-year direction.
2. 02_12WY_COMMAND_CYCLES.md - four 12WY command cycles and seasonal responsibility.
3. 03_DECISION_CHARTER.md - decision rights, vetoes, escalation, and output packet.
4. 04_B2_HANDOFF_QUEUE.md - B1-to-B2 queue for Rocks, gates, and domain requests.
5. 05_B2_DEFINITION_OF_DONE_SPEC.md - B2 DoD packet structure and acceptance contract.
6. 06_B3_JOBS_TO_BE_DONE_SPEC.md - B3 JTBD packet structure and proof contract.

## Handoff Path

1. B1 writes or updates direction here.
2. B1 creates a B2 request in 04_B2_HANDOFF_QUEUE.md.
3. B2 converts the request into DoD packets using 05_B2_DEFINITION_OF_DONE_SPEC.md.
4. B2 creates B3 jobs using 06_B3_JOBS_TO_BE_DONE_SPEC.md.
5. B3 executes only the defined jobs and returns proof.
6. B2 updates gates; B1 reviews direction drift.

## Stop Conditions

- No B2 work without a B1 handoff queue item.
- No B3 work without a B2 DoD or JTBD source.
- No Product-only release can become Business Done without the B2 gate matrix.