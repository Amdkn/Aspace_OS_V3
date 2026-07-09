---
id: B3_SWARM_CONFIG_ABC_CHILDCARE_LEGAL
layer: L2-Business-Pulse-B3
project: abc-childcare-bos
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

# Legal B3 Swarm Config — Eternals (ABC OS + Child Care BOS — Phase 1 Stub)

This folder configures the **Legal** B3 swarm for the dual-entity
`abc-os-child-care-bos` project. Phase 1 = skeleton + topology declaration.
Roster detail and JTBD packets will be filled in subsequent phases.

> Note: this file supersedes the prior SHADOW_ACTIVE mirror (2026-05-27).
> Existing member sub-folders are preserved; only the swarm-config header
> is upgraded to the canonical B3 format.

## B2 / B3 Boundary

- **B2 = Legal** (Aquaman, the B2 gatekeeper).
- **B3 = Eternals** (9 A3-active execution agents).
- B2 owns direction, DoD, acceptance, and proof review.
- B3 owns execution strategy, local unblocking, and delivery.

## ABC-Specific Anchors

- **The single highest-stakes domain in the project.** Per
  SUMMERS_VERSE_MANIFEST, "Childcare = high liability, strong
  regulations. Every offer must pass compliance review before
  launch." The Eternals are the gate, not a checkpoint.
- **Agricultural data protection** (ABC OS side):
  - RGPD / CNIL compliance on agriculteur personal data.
  - VAPI voice transcript retention rules.
  - Agricultural business data confidentiality (yield, financials).
  - Contract templates for formation services (CGV, CGA).
- **Childcare licensing / regulatory** (Child Care BOS side):
  - PMI / DREETS / CAF regulatory framework.
  - Child data protection (enhanced RGPD, parental consent,
    data minimization, retention).
  - Staff background check / certification validation.
  - Operator licensing templates (France, EU expansion later).
  - Incident reporting SOPs and regulatory notification protocols.
- **Compliance gate = structural** — Legal is consulted BEFORE any
  B3 squad ships work touching childcare operations, child data,
  formation contracts, or VAPI voice retention.

## Squad Topology (9 Eternals)

The 9 Eternals map to 9 distinct execution roles inside the Legal domain:

| # | Agent | Execution Role (Legal) |
|---|-------|--------------------------|
| 1 | **Ikaris** | Lead / vision juridique long-terme (10y licensable framework) |
| 2 | **Sersi** | Adaptabilité juridictionnelle (FR / EU / US; agricultural + childcare) |
| 3 | **Thena** | Litigation / archives (incident response, regulatory disputes) |
| 4 | **Kingo** | Public-facing / CGV (formation, childcare operator contracts) |
| 5 | **Druig** | Négociation de clauses (formation, VAPI data processing) |
| 6 | **Gilgamesh** | Enforce des clauses (childcare operator non-compliance) |
| 7 | **Ajak** | Résolution amiable (parent complaints, operator disputes) |
| 8 | **Phastos** | Templates de contrats (formation, childcare, VAPI DPA) |
| 9 | **Makkari** | Vélocité signature (DocuSign < 24h) for operator contracts |

> Existing member folders (`01_Ikaris`, `02_Ajak`, `03_Phastos`,
> `04_Thena`) remain canonical and feed the Phase 2 promotion of
> `01_B3_AGENT_ROSTER.md`.

## Source Inspiration

Inspiration only — the squad is named after the **Marvel Eternals**.
The "ancient, long-horizon, post-human" vibe maps to Legal's reality
of dealing with contracts whose consequences play out over years, not
sprints. Architecture follows the same B3 swarm patterns as
`ceo-desktop`'s sibling config and `solaris`'s mature config.

## Operating Rule (No-Babysitting)

- B3 does not ask B2 for every step.
- B3 asks B2 **only** on: missing authority, missing inputs, cross-domain
  conflict, or DoD ambiguity.
- B3 owns execution strategy. B2 owns acceptance. B1 owns direction.
- Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.
- B3 Legal is the **GATE** for Child Care BOS compliance — not a
  post-hoc reviewer. Every childcare-touching artifact must pass
  before launch.

## Status

PHASE_1_STUB. Existing member sub-folders are preserved. Reference:
`../../../../ceo-desktop/_doctrine/B3_Warp_Core_Execution/08_Legal_Aquaman_Eternals/`
for the sibling structure this stub was adapted from.
