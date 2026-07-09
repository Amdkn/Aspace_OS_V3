---
id: B3_SWARM_CONFIG_CEO_DESKTOP_IT
layer: L2-Business-Pulse-B3
project: ceo-desktop
status: PHASE_1_STUB
created: 2026-06-07
updated: 2026-06-07
parent_jerry: J01_Jerry_Prime_LD01_Business
domain: IT
b2_gatekeeper: Cyborg
squad: Kang_Dynasty
topology_size: multi_variant
source_inspiration: Marvel (Kang the Conqueror — multiple variants)
---

# IT B3 Swarm Config — Kang Dynasty (CEO Desktop — Phase 1 Stub)

This folder configures the **IT** B3 swarm for the `ceo-desktop` project.
Phase 1 = skeleton + topology declaration. Roster detail and JTBD packets
will be filled in subsequent phases.

## B2 / B3 Boundary

- **B2 = IT** (Cyborg, the B2 gatekeeper).
- **B3 = Kang Dynasty** (multiple Kang variants — each one a distinct
  execution role; not a fixed-N roster).
- B2 owns direction, DoD, acceptance, and proof review.
- B3 owns execution strategy, local unblocking, and delivery.

## Squad Topology (Kang Variants)

Unlike the fixed-N squads (6 Guardians, 9 Avengers, 4 F4…), the Kang Dynasty
is a **multi-variant topology**: each Kang variant represents a distinct
execution lane inside the IT domain. The number grows with the project's
infra surface, not with a fixed canon.

Canonical Kang variants (to be expanded in Phase 2):

| Variant | Execution Role (IT) |
|---------|----------------------|
| **Kang Prime** | Infra core: VPS, DNS, Dokploy, orchestration (lead) |
| **Iron Lad** | Provisioning automatisé (Hostinger API) |
| **Scarlet Centurion** | Sécurité réseau / SSL-TLS |
| **Immortus** | Capacity planning / scaling anticipé |
| **Victor Timely** | CI/CD pipelines |
| **Rama-Tut** | Backup / Disaster Recovery |

> Roster is intentionally open-ended. Do not hard-cap the variant count.

## Source Inspiration

Inspiration only — the squad is named after the **Marvel Kang the Conqueror**
character, whose entire gimmick is **being multiple variants across
timelines**. This maps perfectly to IT's reality of "same role, different
infra env / different provider / different timeline". Architecture follows
the same B3 swarm patterns as `solaris`'s mature config.

## Operating Rule (No-Babysitting)

- B3 does not ask B2 for every step.
- B3 asks B2 **only** on: missing authority, missing inputs, cross-domain
  conflict, or DoD ambiguity.
- B3 owns execution strategy. B2 owns acceptance. B1 owns direction.
- Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.

## Status

PHASE_1_STUB. No JTBDs or runtime agents yet. Reference:
`../../../../solaris/_doctrine/B3_Warp_Core_Execution/05_IT_Cyborg_KangDynasty/`
for the mature template this stub will grow into.
