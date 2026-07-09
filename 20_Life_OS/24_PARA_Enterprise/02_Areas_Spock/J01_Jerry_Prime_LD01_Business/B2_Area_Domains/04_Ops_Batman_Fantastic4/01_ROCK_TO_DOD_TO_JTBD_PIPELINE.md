---
id: B2_AREA_ROCK_TO_DOD_TO_JTBD_PIPELINE
layer: B2_AREA_SUPERVISION
surface: Jerry Area J01 LD01 Business
domain: Ops
status: SHADOW_ACTIVE
updated: 2026-05-27
---

# Rock -> DoD -> JTBD Pipeline

B2 converts Jerry B1 area vision into execution-ready swarm work without collapsing into babysitting.

## Pipeline

1. Read B1 area handoff queue.
2. Name one macro domain Rock.
3. Define the Definition of Done.
4. Create acceptance criteria and evidence requirements.
5. Split the Rock into B3 Jobs to be Done.
6. Let the B3 swarm execute autonomously.
7. Review artifacts against the DoD.
8. Update the B2 area gate matrix and report to B1.

## B2 Rock Packet

`yaml
rock_id: J01-B2-OPS-YYYY-NN
domain: Ops
b2_owner: Batman
source_b1_handoff: path-or-id
rock_statement: "As Ops, achieve [measurable macro outcome] so that [portfolio reason]."
status: proposed | active | blocked | review | done
definition_of_done:
  - measurable outcome
  - artifact proof
  - business impact proof
  - risk boundary cleared
acceptance_criteria:
  - criterion_1
  - criterion_2
  - criterion_3
lead_indicators:
  - controllable behavior metric
lag_indicators:
  - outcome metric
b3_jobs:
  - jtbd_id
  - jtbd_id
review_cadence: daily | weekly | per-milestone
`

## Anti-Bottleneck Rule

If B2 must answer more than one clarification before B3 can start, the JTBD is too vague. Rewrite the job, not the swarm.