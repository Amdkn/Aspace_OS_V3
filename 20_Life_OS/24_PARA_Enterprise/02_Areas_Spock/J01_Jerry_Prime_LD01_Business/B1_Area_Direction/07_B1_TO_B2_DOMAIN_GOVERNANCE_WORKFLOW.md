---
id: B1_B2_DOMAIN_GOVERNANCE_WORKFLOW
layer: B1_DIRECTION_TO_B2_MESO
surface: J01_Jerry_Prime_LD01_Business
surface_kind: Jerry Area
status: SHADOW_ACTIVE
updated: 2026-05-27
context7_evidence: /openai/swarm
---

# B1 -> B2 Domain Governance Workflow

B1 does not manage every B2 task. B1 protects the North Star, reads the balance of the 8-domain Business Wheel, and gives clear domain mandates. The B2 DC direction swarm coordinates the domain-level execution.

## 8-Domain Business Wheel

1. Growth - market attention and learning loop.
2. Sales - trust, qualification, offer fit, and conversion path.
3. Product - user value and release artifact.
4. Ops - repeatable delivery and SOP readiness.
5. IT - runtime, access, deployment, and backups.
6. Finance - cost, pricing, margin, billing, and burn control.
7. People - ownership, load, training, and continuity.
8. Legal - claims, privacy, IP, terms, and exposure.

## Workflow

1. B1 reads North Star and current 12WY cycle.
2. B1 scans the 8-domain wheel for imbalance: empty domain, overloaded domain, blocked gate, missing proof, or Product-only drift.
3. B1 writes one domain mandate per affected B2, not a step-by-step plan.
4. B2s negotiate meso tradeoffs through ../B2_Area_Domains/B2_MESO_VP_SWARM_COORDINATION.md.
5. B2 converts mandates into Rocks, DoD, and B3 JTBD packets.
6. B3 swarms execute and unblock internally.
7. B2 returns gate status to B1.
8. B1 updates direction only when the North Star, risk appetite, or strategic priority changes.

## B1 Domain Mandate Packet

`yaml
mandate_id: B1-B2-MANDATE-YYYY-NN
source_north_star: 01_NORTH_STAR_1Y_3Y_10Y.md
cycle: C1 | C2 | C3 | C4
affected_domains:
  - Growth | Sales | Product | Ops | IT | Finance | People | Legal
imbalance_type: empty_domain | overloaded_domain | blocked_gate | product_only_drift | cross_domain_conflict | missing_proof
strategic_intent: "What must become true for the business wheel to rebalance."
constraints:
  - constraint
success_signal:
  - measurable signal
b2_expected_response:
  - Rock proposal
  - DoD packet
  - meso tradeoff packet if needed
b1_decision_needed: false
`

## B1 Intervention Threshold

B1 intervenes only when:

- two or more B2 domains cannot resolve a meso conflict;
- the North Star or cycle priority must change;
- risk appetite changes;
- a domain asks for authority outside its mandate;
- the 8-domain wheel becomes structurally imbalanced.

Otherwise B2 owns coordination and B3 owns execution.