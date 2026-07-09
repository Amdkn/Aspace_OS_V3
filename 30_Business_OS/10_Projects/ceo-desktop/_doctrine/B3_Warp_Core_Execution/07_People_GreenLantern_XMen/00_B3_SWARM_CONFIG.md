---
id: B3_SWARM_CONFIG_CEO_DESKTOP_PEOPLE
layer: L2-Business-Pulse-B3
project: ceo-desktop
status: PHASE_1_STUB
created: 2026-06-07
updated: 2026-06-07
parent_jerry: J01_Jerry_Prime_LD01_Business
domain: People
b2_gatekeeper: Green_Lantern
squad: X_Men
topology_size: 9
source_inspiration: Marvel (X-Men — core 9 roster)
---

# People B3 Swarm Config — X-Men (CEO Desktop — Phase 1 Stub)

This folder configures the **People** B3 swarm for the `ceo-desktop` project.
Phase 1 = skeleton + topology declaration. Roster detail and JTBD packets
will be filled in subsequent phases.

## B2 / B3 Boundary

- **B2 = People** (Green Lantern, the B2 gatekeeper).
- **B3 = X-Men** (9 A3-active execution agents).
- B2 owns direction, DoD, acceptance, and proof review.
- B3 owns execution strategy, local unblocking, and delivery.

## Squad Topology (9 X-Men)

The 9 X-Men map to 9 distinct execution roles inside the People domain:

| # | Agent | Execution Role (People) |
|---|-------|--------------------------|
| 1 | **Cyclops** (Scott Summers) | Discipline onboarding (lead) |
| 2 | **Wolverine** (Logan) | Perf reviews |
| 3 | **Storm** (Ororo Munroe) | Leadership opérationnel |
| 4 | **Jean Grey** | Culture / résolution de conflits |
| 5 | **Rogue** (Anna Marie) | Cross-training: transfert de capacités inter-agents |
| 6 | **Gambit** (Remy LeBeau) | Talent acquisition (charm offensive) |
| 7 | **Jubilee** | Junior mentorship / energy injection |
| 8 | **Beast** (Hank McCoy) | Recrutement tech (nouveaux agents/outils) |
| 9 | **Nightcrawler** (Kurt Wagner) | Onboarding distribué (multi-CLI) |

> Note: Professor X is held at B2 (Green Lantern's domain) and not in the B3
> execution roster, matching the canonical "Charles leads the school, X-Men
> execute the missions" pattern.

## Source Inspiration

Inspiration only — the squad is named after the **Marvel X-Men** **core 9
roster**. The "mutant school" metaphor maps directly to A'Space OS's reality
of integrating diverse agent capacities (CLIs, tools, personas) into a
coherent workforce. Architecture follows the same B3 swarm patterns as
`solaris`'s mature config.

## Operating Rule (No-Babysitting)

- B3 does not ask B2 for every step.
- B3 asks B2 **only** on: missing authority, missing inputs, cross-domain
  conflict, or DoD ambiguity.
- B3 owns execution strategy. B2 owns acceptance. B1 owns direction.
- Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.

## Status

PHASE_1_STUB. No JTBDs or runtime agents yet. Reference:
`../../../../solaris/_doctrine/B3_Warp_Core_Execution/07_People_GreenLantern_XMen/`
for the mature template this stub will grow into.
