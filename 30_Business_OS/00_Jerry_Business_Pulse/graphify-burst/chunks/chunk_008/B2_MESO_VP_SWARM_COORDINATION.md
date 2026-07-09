---
id: B2_MESO_VP_SWARM_COORDINATION
layer: B2_MESO_COORDINATION
surface: 00_Agency_aaS
surface_kind: QuickAccess Mirror
status: SHADOW_ACTIVE
updated: 2026-05-27
---

# B2 Meso VP Swarm Coordination

The B2 VPs coordinate domain conflicts before asking B1 to decide. B1 gives North Star and vision; B2s negotiate meso-level execution tradeoffs.

## Coordination Pattern

- Product ↔ Ops: release quality versus repeatable delivery.
- Product ↔ IT: build ambition versus runtime/deployment boundaries.
- Growth ↔ Sales: attention generation versus qualified conversion.
- Finance ↔ Growth/Product: spend and pricing versus learning speed.
- Legal ↔ Sales/Growth/Product: claims, privacy, IP, and customer promise boundaries.
- People ↔ all domains: ownership, load, training, and continuity.

## B2 Peer Escalation Packet

`yaml
meso_issue_id: B2-MESO-YYYY-NN
requesting_domain: domain
peer_domain: domain
source_rock: path-or-id
conflict: short description
options:
  - option
  - option
recommended_tradeoff: short rationale
b1_escalation_needed: true | false
`

## Escalate To B1 Only When

- the tradeoff changes the North Star;
- two B2 domains cannot satisfy their DoD simultaneously;
- cost, legal, people load, or customer promise exceeds delegated authority;
- the project needs a strategic no.