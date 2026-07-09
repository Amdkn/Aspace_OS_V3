---
id: B3_SWARM_CONFIG_CEO_DESKTOP_LEGAL
layer: L2-Business-Pulse-B3
project: ceo-desktop
status: PHASE_1_STUB
created: 2026-06-07
updated: 2026-06-07
parent_jerry: J01_Jerry_Prime_LD01_Business
domain: Legal
b2_gatekeeper: Aquaman
squad: Eternals
topology_size: 9
source_inspiration: Marvel (Eternals)
---

# Legal B3 Swarm Config — Eternals (CEO Desktop — Phase 1 Stub)

This folder configures the **Legal** B3 swarm for the `ceo-desktop` project.
Phase 1 = skeleton + topology declaration. Roster detail and JTBD packets
will be filled in subsequent phases.

## B2 / B3 Boundary

- **B2 = Legal** (Aquaman, the B2 gatekeeper).
- **B3 = Eternals** (9 A3-active execution agents).
- B2 owns direction, DoD, acceptance, and proof review.
- B3 owns execution strategy, local unblocking, and delivery.

## Squad Topology (9 Eternals)

The 9 Eternals map to 9 distinct execution roles inside the Legal domain:

| # | Agent | Execution Role (Legal) |
|---|-------|--------------------------|
| 1 | **Ikaris** | Lead / vision juridique long-terme |
| 2 | **Sersi** | Adaptabilité juridictionnelle (FR / EU / US) |
| 3 | **Thena** | Litigation / archives |
| 4 | **Kingo** | Public-facing / CGV |
| 5 | **Druig** | Négociation de clauses |
| 6 | **Gilgamesh** | Enforce des clauses |
| 7 | **Ajak** | Résolution amiable |
| 8 | **Phastos** | Templates de contrats |
| 9 | **Makkari** | Vélocité signature (DocuSign < 24h) |

> Canon roster (to be promoted in Phase 2): `01_B3_AGENT_ROSTER.md`.

## Source Inspiration

Inspiration only — the squad is named after the **Marvel Eternals**. The
"ancient, long-horizon, post-human" vibe maps to Legal's reality of dealing
with contracts whose consequences play out over years, not sprints.
Architecture follows the same B3 swarm patterns as `solaris`'s mature
config.

## Operating Rule (No-Babysitting)

- B3 does not ask B2 for every step.
- B3 asks B2 **only** on: missing authority, missing inputs, cross-domain
  conflict, or DoD ambiguity.
- B3 owns execution strategy. B2 owns acceptance. B1 owns direction.
- Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.

## Status

PHASE_1_STUB. No JTBDs or runtime agents yet. Reference:
`../../../../solaris/_doctrine/B3_Warp_Core_Execution/08_Legal_Aquaman_Eternals/`
for the mature template this stub will grow into.
