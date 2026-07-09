---
id: B3_SWARM_CONFIG_CEO_DESKTOP_PRODUCT
layer: L2-Business-Pulse-B3
project: ceo-desktop
status: PHASE_1_STUB
created: 2026-06-07
updated: 2026-06-07
parent_jerry: J01_Jerry_Prime_LD01_Business
domain: Product
b2_gatekeeper: Flash
squad: Avengers
topology_size: 9
source_inspiration: Marvel Cinematic Universe (Avengers)
---

# Product B3 Swarm Config — Avengers (CEO Desktop — Phase 1 Stub)

This folder configures the **Product** B3 swarm for the `ceo-desktop` project.
Phase 1 = skeleton + topology declaration. Roster detail and JTBD packets
will be filled in subsequent phases.

## B2 / B3 Boundary

- **B2 = Product** (Flash, the B2 gatekeeper).
- **B3 = Avengers** (9 A3-active execution agents).
- B2 owns direction, DoD, acceptance, and proof review.
- B3 owns execution strategy, local unblocking, and delivery.

## Squad Topology (9 Avengers)

The 9 Avengers map to 9 distinct execution roles inside the Product domain:

| # | Agent | Execution Role (Product) |
|---|-------|--------------------------|
| 1 | **Tony Stark** (Iron Man) | Tech architecture / stack choice / debt management |
| 2 | **Steve Rogers** (Captain America) | Product vision / roadmap conviction (lead) |
| 3 | **Thor** | Power features / brute-force MVP when timing critical |
| 4 | **Bruce Banner** (Hulk) | Destructive QA / edge cases / stress testing |
| 5 | **Natasha Romanoff** (Black Widow) | Spec writing / rigorous user stories |
| 6 | **Clint Barton** (Hawkeye) | UX precision / feature-level sniper |
| 7 | **Wanda Maximoff** (Scarlet Witch) | Design system vision / brand coherence |
| 8 | **Vision** | Long-horizon product strategy / data integrity |
| 9 | **Sam Wilson** (Falcon) | Cross-team handoff / adoption & enablement |

> Canon roster (to be promoted in Phase 2): `01_B3_AGENT_ROSTER.md`.

## Source Inspiration

Inspiration only — the squad is named after the **Marvel Cinematic Universe**
**Avengers** core team (9 members including Sam Wilson). Naming is a
cognitive anchor, not a literal mapping. Architecture follows the same B3
swarm patterns as `solaris`'s mature config.

## Operating Rule (No-Babysitting)

- B3 does not ask B2 for every step.
- B3 asks B2 **only** on: missing authority, missing inputs, cross-domain
  conflict, or DoD ambiguity.
- B3 owns execution strategy. B2 owns acceptance. B1 owns direction.
- Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.

## Status

PHASE_1_STUB. No JTBDs or runtime agents yet. Reference:
`../../../../solaris/_doctrine/B3_Warp_Core_Execution/03_Product_Flash_Avengers/`
for the mature template this stub will grow into.
