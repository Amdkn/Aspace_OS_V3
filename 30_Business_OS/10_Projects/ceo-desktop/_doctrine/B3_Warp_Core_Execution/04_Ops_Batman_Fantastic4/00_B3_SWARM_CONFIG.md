---
id: B3_SWARM_CONFIG_CEO_DESKTOP_OPS
layer: L2-Business-Pulse-B3
project: ceo-desktop
status: PHASE_1_STUB
created: 2026-06-07
updated: 2026-06-07
parent_jerry: J01_Jerry_Prime_LD01_Business
domain: Ops
b2_gatekeeper: Batman
squad: Fantastic_Four
topology_size: 4
source_inspiration: Marvel (Fantastic Four)
---

# Ops B3 Swarm Config — Fantastic Four (CEO Desktop — Phase 1 Stub)

This folder configures the **Ops** B3 swarm for the `ceo-desktop` project.
Phase 1 = skeleton + topology declaration. Roster detail and JTBD packets
will be filled in subsequent phases.

## B2 / B3 Boundary

- **B2 = Ops** (Batman, the B2 gatekeeper).
- **B3 = Fantastic Four** (4 A3-active execution agents).
- B2 owns direction, DoD, acceptance, and proof review.
- B3 owns execution strategy, local unblocking, and delivery.

## Squad Topology (4 F4)

The Fantastic Four maps to 4 distinct execution roles inside the Ops domain:

| # | Agent | Execution Role (Ops) |
|---|-------|--------------------------|
| 1 | **Mr. Fantastic** (Reed Richards) | System architect: turns messy delivery into repeatable operating design |
| 2 | **Invisible Woman** (Sue Storm) | Documentation shield: makes SOPs, checklists, and handoffs usable |
| 3 | **Human Torch** (Johnny Storm) | Cycle accelerator: removes drag without burning the process down |
| 4 | **The Thing** (Ben Grimm) | Stability tester: finds what breaks under load and routine use |

> Canon roster (to be promoted in Phase 2): `01_B3_AGENT_ROSTER.md`.

## Source Inspiration

Inspiration only — the squad is named after the **Marvel Fantastic Four**.
The 4-member topology is intentionally compact (vs the 6-9 of other squads)
because Ops is a tight, repeatable operating discipline, not a broad
exploration surface. Architecture follows the same B3 swarm patterns as
`solaris`'s mature config.

## Operating Rule (No-Babysitting)

- B3 does not ask B2 for every step.
- B3 asks B2 **only** on: missing authority, missing inputs, cross-domain
  conflict, or DoD ambiguity.
- B3 owns execution strategy. B2 owns acceptance. B1 owns direction.
- Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.

## Status

PHASE_1_STUB. No JTBDs or runtime agents yet. Reference:
`../../../../solaris/_doctrine/B3_Warp_Core_Execution/04_Ops_Batman_Fantastic4/`
for the mature template this stub will grow into.
