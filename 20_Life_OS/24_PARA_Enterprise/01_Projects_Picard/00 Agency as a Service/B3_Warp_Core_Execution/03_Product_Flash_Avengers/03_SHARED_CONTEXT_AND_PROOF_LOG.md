---
id: B3_SHARED_CONTEXT_AND_PROOF_LOG
layer: B3_SWARM_EXECUTION
surface: 00_Agency_aaS
domain: Product
status: SHADOW_ACTIVE
updated: 2026-05-27
---

# Shared Context And Proof Log

Use this as the common memory surface for the squad. It is not a chat transcript. It is the minimum state needed for another B3 to continue.

## Context Variables

`yaml
source_b2_rock: path-or-id
source_jtbd: path-or-id
current_goal: short measurable goal
active_member: member_name
peer_reviewed_by: member_name | null
artifact_paths:
  - path-or-link
proof_paths:
  - path-or-link
lead_indicator: measurable action
lag_indicator: measurable outcome
status: active | blocked | review_ready | accepted
`

## Proof Standard

A proof is valid when another agent can inspect it without trusting the author: file path, command output, screenshot, report, link, structured diff, metric, or explicit blocker note.

## Productive Disagreement

At least one peer should be allowed to disagree with the first solution when the JTBD affects cost, legal exposure, customer promise, release quality, or operational load. The disagreement must end in one of: accepted revision, rejected with reason, or B2 escalation.