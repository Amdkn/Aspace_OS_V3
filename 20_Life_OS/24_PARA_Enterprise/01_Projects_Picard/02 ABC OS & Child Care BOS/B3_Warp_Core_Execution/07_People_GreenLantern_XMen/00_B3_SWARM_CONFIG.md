---
id: B3_SWARM_CONFIG_ABC_CHILDCARE_PEOPLE
layer: L2-Business-Pulse-B3
project: abc-childcare-bos
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

# People B3 Swarm Config — X-Men (ABC OS + Child Care BOS — Phase 1 Stub)

This folder configures the **People** B3 swarm for the dual-entity
`abc-os-child-care-bos` project. Phase 1 = skeleton + topology declaration.
Roster detail and JTBD packets will be filled in subsequent phases.

> Note: this file supersedes the prior SHADOW_ACTIVE mirror (2026-05-27).
> Existing member sub-folders are preserved; only the swarm-config header
> is upgraded to the canonical B3 format.

## B2 / B3 Boundary

- **B2 = People** (Green Lantern, the B2 gatekeeper).
- **B3 = X-Men** (9 A3-active execution agents).
- B2 owns direction, DoD, acceptance, and proof review.
- B3 owns execution strategy, local unblocking, and delivery.

## ABC-Specific Anchors

- **Two distinct talent pools** — People must source / qualify /
  onboard BOTH:
  - **Formateurs agricoles** (ABC OS side) — agronomes, techniciens
    agricoles, ex-chambres-d'agriculture. Domain expertise + voice
    comfort + pedagogical skill.
  - **Childcare staff** (Child Care BOS side) — directeurs de crèche,
    EJE, auxiliaires de puériculture. Mandatory certifications,
    background checks, regulatory standing.
- **"Who Not How" (Sullivan)** — per book alignment, Sullivan maps
  to People primary, Ops secondary. The X-Men build the "who" for
  both entities.
- **Childcare background checks are non-negotiable** — People cannot
  place a childcare worker without Legal (G8) cleared vetting.
- **The mutant-school metaphor fits the dual entity** — integrating
  two very different talent populations (agronomes + puériculteurs)
  into a coherent workforce is the operational challenge.

## Squad Topology (9 X-Men)

The 9 X-Men map to 9 distinct execution roles inside the People domain:

| # | Agent | Execution Role (People) |
|---|-------|--------------------------|
| 1 | **Cyclops** (Scott Summers) | Discipline onboarding lead (dual-entity) |
| 2 | **Wolverine** (Logan) | Perf reviews (formateurs + childcare staff) |
| 3 | **Storm** (Ororo Munroe) | Leadership opérationnel across both entities |
| 4 | **Jean Grey** | Culture / résolution de conflits (rural vs urbain, agriculteur vs opérateur) |
| 5 | **Rogue** (Anna Marie) | Cross-training: transfert de capacités inter-agents (formateur → childcare-aware) |
| 6 | **Gambit** (Remy LeBeau) | Talent acquisition — charm offensive for agronomes + childcare pros |
| 7 | **Jubilee** | Junior mentorship / energy injection (newer A3s) |
| 8 | **Beast** (Hank McCoy) | Recrutement tech (VAPI voice trainers, NotebookLM curators) |
| 9 | **Nightcrawler** (Kurt Wagner) | Onboarding distribué (multi-CLI, multi-site childcare) |

> Note: Professor X is held at B2 (Green Lantern's domain) and not in
> the B3 execution roster, matching the canonical "Charles leads the
> school, X-Men execute the missions" pattern.
> Existing member folders (`01_Cyclops`, `02_Jean_Grey`, `03_Beast`,
> `04_Professor_X`) remain canonical and feed the Phase 2 promotion
> of `01_B3_AGENT_ROSTER.md`.

## Source Inspiration

Inspiration only — the squad is named after the **Marvel X-Men** core
9 roster. The "mutant school" metaphor maps directly to A'Space OS's
reality of integrating diverse agent capacities (CLIs, tools,
personas) into a coherent workforce. Architecture follows the same
B3 swarm patterns as `ceo-desktop`'s sibling config and `solaris`'s
mature config.

## Operating Rule (No-Babysitting)

- B3 does not ask B2 for every step.
- B3 asks B2 **only** on: missing authority, missing inputs, cross-domain
  conflict, or DoD ambiguity.
- B3 owns execution strategy. B2 owns acceptance. B1 owns direction.
- Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.
- B3 NEVER places a childcare worker who has not passed Legal (G8)
  vetting.

## Status

PHASE_1_STUB. Existing member sub-folders are preserved. Reference:
`../../../../ceo-desktop/_doctrine/B3_Warp_Core_Execution/07_People_GreenLantern_XMen/`
for the sibling structure this stub was adapted from.
