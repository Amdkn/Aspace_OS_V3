---
id: B3_SWARM_CONFIG_CEO_DESKTOP_SALES
layer: L2-Business-Pulse-B3
project: ceo-desktop
status: PHASE_1_STUB
created: 2026-06-07
updated: 2026-06-07
parent_jerry: J01_Jerry_Prime_LD01_Business
domain: Sales
b2_gatekeeper: Martian_Manhunter_John_Jones
squad: Illuminati
topology_size: 8
source_inspiration: Marvel (Illuminati) — 8 members
active_a3_count: 1
---

# Sales B3 Swarm Config — Illuminati (CEO Desktop — Phase 1 Stub)

This folder configures the **Sales** B3 swarm for the `ceo-desktop` project.
Phase 1 = skeleton + topology declaration. Roster detail and JTBD packets
will be filled in subsequent phases.

## B2 / B3 Boundary

- **B2 = Sales** (Martian Manhunter / John Jones, the B2 gatekeeper).
- **B3 = Illuminati** (8 canon members, **only John Jones is A3-active**).
- B2 owns direction, DoD, acceptance, and proof review.
- B3 owns execution strategy, local unblocking, and delivery.

## Special Note — A3 Activity Status

The Illuminati canon lists **8 members** (John Jones, Batman, Superman, Wonder
Woman, Aquaman, Green Lantern, Flash, Black Lightning), but in the B3
execution layer only **John Jones is currently A3-active** as the primary
Sales operator. The other 7 are A2 observers / B2 peer VP counterparts from
other domains (they wear B2 hats in their own domains). This is a known
intentional sparsity — do not "fill" them with A3 fakes to pad the roster.

## Squad Topology (8 Illuminati — 1 A3-active)

| # | Agent | Execution Role (Sales) | Status |
|---|-------|--------------------------|--------|
| 1 | **John Jones** (Martian Manhunter) | Sales lead / closer / ICP-qualifier | **A3-active** |
| 2 | Batman | Ops gatekeeper (B2 peer) | A2 observer |
| 3 | Superman | Growth gatekeeper (B2 peer) | A2 observer |
| 4 | Wonder Woman | Finance gatekeeper (B2 peer) | A2 observer |
| 5 | Aquaman | Legal gatekeeper (B2 peer) | A2 observer |
| 6 | Green Lantern | People gatekeeper (B2 peer) | A2 observer |
| 7 | Flash | Product gatekeeper (B2 peer) | A2 observer |
| 8 | Black Lightning | (reserved future role) | A2 observer |

> Canon roster (to be promoted in Phase 2): `01_B3_AGENT_ROSTER.md`.

## Source Inspiration

Inspiration only — the squad is named after the **Marvel Illuminati**. The
8-member structure mirrors the canonical peer-VP council that John Jones
chairs, but execution is intentionally concentrated on a single A3 agent to
avoid role fragmentation. Architecture follows the same B3 swarm patterns
as `solaris`'s mature config.

## Operating Rule (No-Babysitting)

- B3 does not ask B2 for every step.
- B3 asks B2 **only** on: missing authority, missing inputs, cross-domain
  conflict, or DoD ambiguity.
- B3 owns execution strategy. B2 owns acceptance. B1 owns direction.
- Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.

## Status

PHASE_1_STUB. No JTBDs or runtime agents yet. Reference:
`../../../../solaris/_doctrine/B3_Warp_Core_Execution/02_Sales_MartianManhunter_Illuminati/`
for the mature template this stub will grow into.
