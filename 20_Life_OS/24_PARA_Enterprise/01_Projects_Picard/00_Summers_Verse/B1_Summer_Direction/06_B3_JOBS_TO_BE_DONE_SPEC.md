---
id: B1_B3_JOBS_TO_BE_DONE_SPEC_00_SUMMERS_VERSE
layer: L2_Business_Pulse
kind: Template
status: SHADOW_ACTIVE
date: 2026-05-26
---

# B3 Jobs To Be Done Spec - 00_Summers_Verse

B1 defines the structure of work. B2 converts DoD into jobs. B3 executes jobs and returns proof.

## B3 JTBD Packet

`yaml
jtbd_id: ""
date: "2026-05-26"
scope: "00_Summers_Verse"
source_b2_dod: ""
b2_domain: "Growth|Sales|Product|Ops|IT|Finance|People|Legal"
owner_b3: ""
job_statement: "When ___, B3 must ___, so that ___."
input_artifacts:
  - path: ""
expected_output_artifacts:
  - path: ""
commands_or_actions:
  - ""
proof_required:
  - ""
lead_indicator: ""
lag_indicator: ""
timebox: ""
status: "TODO|IN_PROGRESS|BLOCKED|DONE"
blocker: ""
`

## JTBD Rules

A B3 job must be:

- artifact-producing;
- small enough to verify;
- tied to one B2 DoD;
- measurable by one Lead indicator and one Lag indicator when possible;
- blocked explicitly when inputs are missing.

## B3 Does Not

- invent strategy;
- redefine the B2 Definition of Done;
- bypass Finance, Legal, Ops, IT, Sales, Growth, or People gates;
- mark a project Business Done;
- hide missing proof behind narrative.

## Proof Contract

Every completed B3 job must return:

`yaml
job_id: ""
status: "DONE|BLOCKED"
changed_files:
  - ""
commands_run:
  - ""
proof_paths:
  - ""
remaining_risk:
  - ""
next_b2_review_needed: true
`

## Handoff Back To B2

B3 returns proof to B2. B2 decides whether the DoD is satisfied. B1 decides whether the direction can advance.