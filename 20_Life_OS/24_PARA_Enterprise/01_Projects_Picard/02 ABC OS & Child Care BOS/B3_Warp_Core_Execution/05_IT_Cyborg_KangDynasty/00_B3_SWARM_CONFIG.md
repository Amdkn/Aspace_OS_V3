---
id: B3_SWARM_CONFIG_ABC_CHILDCARE_IT
layer: L2-Business-Pulse-B3
project: abc-childcare-bos
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

# IT B3 Swarm Config — Kang Dynasty (ABC OS + Child Care BOS — Phase 1 Stub)

This folder configures the **IT** B3 swarm for the dual-entity
`abc-os-child-care-bos` project. Phase 1 = skeleton + topology declaration.
Roster detail and JTBD packets will be filled in subsequent phases.

> Note: this file supersedes the prior SHADOW_ACTIVE mirror (2026-05-27).
> Existing member sub-folders are preserved; only the swarm-config header
> is upgraded to the canonical B3 format.

## B2 / B3 Boundary

- **B2 = IT** (Cyborg, the B2 gatekeeper).
- **B3 = Kang Dynasty** (multiple Kang variants — each one a distinct
  execution role; not a fixed-N roster).
- B2 owns direction, DoD, acceptance, and proof review.
- B3 owns execution strategy, local unblocking, and delivery.

## ABC-Specific Anchors

- **VAPI integration is a first-class infra lane** — voice webhook
  routing, Gemini / Claude fallback orchestration, voice transcript
  storage, retry / failure handling. This is not a Product feature;
  it is IT plumbing.
- **Zod contracts are the source of truth** — every API boundary in
  the dual-entity system (formation data, agricultural metrics,
  childcare operator records, parent data) is validated by Zod
  schemas. IT owns the schema registry; Product/Finance/People
  consume the contracts.
- **NotebookLM as institutional memory** — formation transcripts,
  operator onboarding records, and childcare regulatory changes
  are stored in NotebookLM. IT owns the ingestion pipeline.
- **Symphony Router orchestration** — IT owns the routing infra
  that decides which LLM (Gemini vs Claude) handles which request,
  and how the VAPI voice surface connects to the formation back-end.
- **Two data sensitivities** — ABC OS (agricultural data) and
  Child Care BOS (child data, parent data) have very different
  regulatory exposure. IT must enforce this at infra level
  (encryption, retention, access control).

## Squad Topology (Kang Variants)

Unlike the fixed-N squads (6 Guardians, 9 Avengers, 4 F4…), the Kang
Dynasty is a **multi-variant topology**: each Kang variant represents
a distinct execution lane inside the IT domain. The number grows with
the project's infra surface, not with a fixed canon.

Canonical Kang variants for this project (to be expanded in Phase 2):

| Variant | Execution Role (IT) — ABC OS + Child Care BOS |
|---------|------------------------------------------------|
| **Kang Prime** | Infra core: VPS, DNS, Dokploy, orchestration (lead) |
| **Iron Lad** | Provisioning automatisé (Hostinger API) |
| **Scarlet Centurion** | Sécurité réseau / SSL-TLS / encryption-at-rest for child data |
| **Immortus** | Capacity planning / scaling anticipé (formation traffic peaks) |
| **Victor Timely** | CI/CD pipelines (Landing.html, voice webhook deploys) |
| **Rama-Tut** | Backup / Disaster Recovery (agricultural + childcare data) |
| **VAPI-Lane Kang** *(new)* | VAPI voice webhook integration + transcript pipeline |
| **Zod-Lane Kang** *(new)* | Zod schema registry + contract enforcement |
| **NotebookLM-Lane Kang** *(new)* | NotebookLM ingestion + retrieval pipeline |

> Roster is intentionally open-ended. Do not hard-cap the variant count.
> Existing member folders (`01_Kang_Prime`, `02_Immortus`, `03_Iron_Lad`,
> `04_Rama_Tut`) remain canonical.

## Source Inspiration

Inspiration only — the squad is named after the **Marvel Kang the
Conqueror** character, whose entire gimmick is **being multiple
variants across timelines**. This maps perfectly to IT's reality of
"same role, different infra env / different provider / different
timeline". Architecture follows the same B3 swarm patterns as
`ceo-desktop`'s sibling config and `solaris`'s mature config.

## Operating Rule (No-Babysitting)

- B3 does not ask B2 for every step.
- B3 asks B2 **only** on: missing authority, missing inputs, cross-domain
  conflict, or DoD ambiguity.
- B3 owns execution strategy. B2 owns acceptance. B1 owns direction.
- Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.
- B3 NEVER deploys a childcare-data-touching pipeline that bypasses
  Legal (G8) compliance review.

## Status

PHASE_1_STUB. Existing member sub-folders are preserved. Reference:
`../../../../ceo-desktop/_doctrine/B3_Warp_Core_Execution/05_IT_Cyborg_KangDynasty/`
for the sibling structure this stub was adapted from.
