---
id: B2_DC_DIRECTION_COUNCIL_WORKFLOW
layer: B2_MESO_COORDINATION
surface: 05_Marina
surface_kind: QuickAccess Mirror
status: SHADOW_ACTIVE
updated: 2026-05-27
context7_evidence: /openai/swarm
---

# B2 DC Direction Council Workflow

This is the VP swarm for the 8 Business domains. It receives B1 mandates, resolves meso tradeoffs, and keeps B1 out of operational churn.

## Council Members

- Superman - Growth
- Martian Manhunter / John Jones - Sales
- Flash - Product
- Batman - Ops
- Cyborg - IT
- Wonder Woman - Finance
- Green Lantern - People
- Aquaman - Legal

## Council Routine

1. Intake B1 mandate or B2 peer issue.
2. Identify impacted domains.
3. Each impacted B2 states its DoD, blocker, and non-negotiable boundary.
4. Council selects one of three modes:
   - parallel: domains can act independently.
   - handoff: one domain must finish before another starts.
   - 
egotiation: two or more DoDs conflict and need a tradeoff.
5. B2s create or update Rocks and DoD packets.
6. B2s dispatch B3 JTBD packets.
7. Council logs the meso decision.
8. Escalate to B1 only when authority or North Star changes are required.

## Meso Decision Packet

`yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B1-B2-MANDATE-YYYY-NN
mode: parallel | handoff | negotiation
impacted_domains:
  - domain
tradeoff: short statement
decision: accepted | blocked | escalate_to_B1
proof_expected:
  - B2 gate update
  - B3 proof path
next_review: date-or-cycle
`

## Escalation Rule

Escalate to B1 only if the council cannot preserve the 8-domain wheel while staying inside current North Star, cycle priority, authority, and risk appetite.