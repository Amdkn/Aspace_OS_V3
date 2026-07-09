---
id: B2_B3_SWARM_SUPERVISION_PROTOCOL
layer: B2_DOMAIN_SUPERVISION
project: 01-omk-business-os
domain: IT
status: SHADOW_ACTIVE
updated: 2026-05-27
---

# B3 Swarm Supervision Protocol

The IT B2 does not babysit the Kang Dynasty swarm. It creates a bounded game board, then reviews proof.

## Autonomy Contract

B3 agents are free to:

- choose the execution sequence;
- inspect constraints and propose workarounds;
- use local tools and approved project surfaces;
- produce better artifacts than the initial request imagined;
- stop and declare a blocker when the DoD cannot be satisfied honestly.

B3 agents are not free to:

- change the Rock;
- change the Definition of Done;
- bypass Legal, Finance, Ops, IT, or People gates;
- commit private keys, credentials, or sensitive values;
- mark their own work as Business Done without B2 review.

## JTBD Packet

`yaml
jtbd_id: B3-IT-YYYY-NN
source_rock_id: B2-IT-YYYY-NN
assigned_swarm: Kang Dynasty
job_statement: "When [situation], produce [artifact/outcome], so that [DoD progress]."
freedom_of_execution:
  allowed: "B3 chooses tactics, tools, and sequence."
  forbidden: "B3 cannot redefine Rock, DoD, or cross-domain gates."
input_artifacts:
  - path-or-link
expected_output_artifacts:
  - path-or-link
proof_required:
  - command/log/screenshot/report/link
lead_indicator: measurable action
lag_indicator: measurable outcome
blocker_protocol: "Return BLOCKED with missing input, failed assumption, and next B2 decision needed."
`

## Review Loop

1. B3 posts artifact and proof.
2. B2 checks proof against DoD.
3. B2 returns one of: ccepted, evise, locked, scalate_to_B1.
4. B2 updates the B2 gate matrix.

## Donna Safety Exit

If the swarm loops, fabricates proof, or keeps asking for permission instead of executing inside the contract, route the case to Donna/DLQ for safety review.