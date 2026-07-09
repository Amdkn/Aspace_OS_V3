---
id: B1_DIRECTION_INDEX_CEOS_DESKTOP
layer: B1_DIRECTION
status: PHASE_1_SKELETON
created: 2026-06-07
parent_jerry: J01_Jerry_Prime_LD01_Business
project_slug: ceo-desktop
---

# B1 Direction — CEO's Desktop

This folder is the B1 direction cockpit for the **CEO's Desktop** project. It exists so Jerry/Summer can pass command-center strategy to B2 domain managers without forcing B3 technicians to infer intent from scattered notes.

See `../SUMMERS_VERSE_MANIFEST.md` for the 1Y/3Y/10Y frame.

## Operating Rule

B1 owns direction and packet structure. B2 owns domain Definition of Done and gates for the 8 SOB. B3 owns execution, proof, Lead indicators, Lag indicators, and blocker reports for the 8 squads.

The CEO's Desktop is unique in that **B1 is A0 itself** — Amadeus is the CEO. B2 managers report up to the desktop; the desktop is the surface A0 uses to consume their reports.

## Files

1. `01_NORTH_STAR_1Y_3Y_10Y.md` — 1-year, 3-year, and 10-year command-center direction.
2. `02_12WY_COMMAND_CYCLES.md` — 12-Week Year command cycles and seasonal responsibility.
3. `03_DECISION_CHARTER.md` — decision rights, vetoes, escalation, and output packet schema.
4. `04_B2_HANDOFF_QUEUE.md` — B1-to-B2 queue for the 8 SOB domains (currently all PENDING).

## Handoff Path

1. B1 (A0) writes or updates direction here.
2. B1 creates a B2 request in `04_B2_HANDOFF_QUEUE.md` for any of the 8 SOB domains.
3. B2 converts the request into a DoD packet (Phase 2 — not yet built).
4. B2 creates B3 jobs via the JTBD spec (Phase 2 — not yet built).
5. B3 executes only the defined jobs and returns proof.
6. B2 updates gates; B1 reviews direction drift.

## Stop Conditions

- No B2 work without a B1 handoff queue item.
- No B3 work without a B2 DoD or JTBD source.
- No domain decision is final without a decision-charter entry.
- The desktop cannot bypass Beth/Morty safety — it surfaces risk, it does not hide it.

## Phase 1 Scope (Now)

This Phase 1 skeleton contains only the 4 B1 files above. Phase 2 (B2 DoD + B3 JTBD specs, decision log, retrospective ledger) is queued in `04_B2_HANDOFF_QUEUE.md` as PENDING.
