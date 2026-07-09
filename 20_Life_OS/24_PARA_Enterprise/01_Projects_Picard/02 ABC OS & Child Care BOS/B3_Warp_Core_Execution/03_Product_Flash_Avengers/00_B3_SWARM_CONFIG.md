---
id: B3_SWARM_CONFIG_ABC_CHILDCARE_PRODUCT
layer: L2-Business-Pulse-B3
project: abc-childcare-bos
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

# Product B3 Swarm Config — Avengers (ABC OS + Child Care BOS — Phase 1 Stub)

This folder configures the **Product** B3 swarm for the dual-entity
`abc-os-child-care-bos` project. Phase 1 = skeleton + topology declaration.
Roster detail and JTBD packets will be filled in subsequent phases.

> Note: this file supersedes the prior SHADOW_ACTIVE mirror (2026-05-27).
> Existing member sub-folders are preserved; only the swarm-config header
> is upgraded to the canonical B3 format.

## B2 / B3 Boundary

- **B2 = Product** (Flash, the B2 gatekeeper).
- **B3 = Avengers** (9 A3-active execution agents).
- B2 owns direction, DoD, acceptance, and proof review.
- B3 owns execution strategy, local unblocking, and delivery.

## ABC-Specific Anchors

- **The VAPI formation interface lives here.** The Product Avengers
  own the in-product voice UX — the formation flow that turns a
  agriculteur's question into a measurable outcome. This is the
  *core* product surface for ABC OS, not a feature on the side.
- **`Landing.html` is the prototype entry point.** The web landing
  page is the canonical pre-product surface that funnels prospects
  into the VAPI formation. The Avengers treat it as a first-class
  artifact (design, copy, conversion).
- **AI-first, voice-as-channel** — the product is formation, not
  voice. Every squad member must defend the boundary: do not let
  voice UX creep become the product.
- **Symphony Router + Zod** — the Avengers consume Symphony Router
  for orchestration and Zod for contract validation. IT owns the
  infra, Product owns the user-facing surface.
- **Dual-entity awareness** — Avengers serve BOTH the ABC formation
  product AND the Child Care BOS compliance / ops product. Same
  Avengers squad, different JTBD packets per entity.

## Squad Topology (9 Avengers)

The 9 Avengers map to 9 distinct execution roles inside the Product domain,
adapted to the dual ABC + Child Care reality:

| # | Agent | Execution Role (Product) |
|---|-------|--------------------------|
| 1 | **Tony Stark** (Iron Man) | Tech architecture / stack choice / debt management; owns VAPI / Gemini / Claude / Zod boundaries |
| 2 | **Steve Rogers** (Captain America) | Product vision / roadmap conviction; defends formation-as-product vs voice-as-product |
| 3 | **Thor** | Power features / brute-force MVP when timing critical (e.g. Landing.html v1) |
| 4 | **Bruce Banner** (Hulk) | Destructive QA / edge cases / stress testing on voice + formation flows |
| 5 | **Natasha Romanoff** (Black Widow) | Spec writing / rigorous user stories in FR |
| 6 | **Clint Barton** (Hawkeye) | UX precision / feature-level sniper on the voice funnel |
| 7 | **Wanda Maximoff** (Scarlet Witch) | Design system vision / brand coherence across Landing.html + VAPI surface |
| 8 | **Vision** | Long-horizon product strategy / data integrity (agricultural data) |
| 9 | **Sam Wilson** (Falcon) | Cross-team handoff / adoption & enablement (childcare operators on boarding) |

> Existing member folders (`01_Captain_America`, `02_Iron_Man`, `03_Thor`,
> `04_Black_Widow`) remain canonical and feed the Phase 2 promotion of
> `01_B3_AGENT_ROSTER.md`.

## Source Inspiration

Inspiration only — the squad is named after the **Marvel Cinematic
Universe Avengers** core team (9 members including Sam Wilson). Naming
is a cognitive anchor, not a literal mapping. Architecture follows the
same B3 swarm patterns as `ceo-desktop`'s sibling config and `solaris`'s
mature config.

## Operating Rule (No-Babysitting)

- B3 does not ask B2 for every step.
- B3 asks B2 **only** on: missing authority, missing inputs, cross-domain
  conflict, or DoD ambiguity.
- B3 owns execution strategy. B2 owns acceptance. B1 owns direction.
- Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.
- B3 NEVER ships a feature that bypasses Legal review (G8) — especially
  on the Child Care BOS side (licensing, child data protection).

## Status

PHASE_1_STUB. Existing member sub-folders are preserved. Reference:
`../../../../ceo-desktop/_doctrine/B3_Warp_Core_Execution/03_Product_Flash_Avengers/`
for the sibling structure this stub was adapted from.
