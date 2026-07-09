---
id: B3_PEER_HANDOFFS
layer: B3_SWARM_EXECUTION
surface: 00_Summers_Verse
domain: IT
status: SHADOW_ACTIVE
updated: 2026-05-27
---

# Peer Unblocking And Handoffs

## Internal Handoff Contract

`yaml
handoff_id: B3-IT-PEER-YYYY-NN
from_agent: member_name
to_agent: member_name
reason: assumption_check | artifact_build | proof_review | blocker_resolution
context_variables:
  source_jtbd: path-or-id
  current_artifact: path-or-link
  known_constraints:
    - constraint
  missing_inputs:
    - input
expected_return:
  - artifact update
  - proof note
  - blocker cleared or escalated
`

## Allowed Peer Handoffs

- Research -> Build when enough context exists.
- Build -> Review when an artifact is testable.
- Review -> Research when evidence is thin.
- Any member -> Unblocker when progress stops.

## Escalate To B2 Only When

- The DoD is ambiguous.
- The required input does not exist.
- The task crosses another B2 domain gate.
- The swarm found a risk that changes acceptance.
- The only remaining action requires A0/B1 authority.