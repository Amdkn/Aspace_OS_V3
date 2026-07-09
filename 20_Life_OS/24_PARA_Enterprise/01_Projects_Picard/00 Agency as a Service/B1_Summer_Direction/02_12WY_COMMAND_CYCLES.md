---
id: B1_12WY_COMMAND_CYCLES_00_AGENCY_AAS
layer: L2_Business_Pulse
kind: SummerProject
status: SHADOW_ACTIVE
date: 2026-05-26
---

# 12WY Command Cycles - 00_Agency_aaS

## Cycle C1 - Direction Lock

Goal: convert vague ambition into a bounded operating direction.

Gate:

- North Star filled;
- active mode selected or marked NEEDS_MODE_LOCK;
- B2 handoff queue seeded;
- Product-only risk acknowledged.

## Cycle C2 - Domain Activation

Goal: make the 8 B2 domains real enough to block or enable Product.

Gate:

- Growth, Sales, Product, Ops, IT, Finance, People, Legal each has a named concern;
- Ops and IT have reviewed runtime feasibility;
- Finance and Legal have reviewed exposure;
- People has named owner/load risk.

## Cycle C3 - Execution Proof

Goal: turn B2 direction into B3 execution artifacts.

Gate:

- B3 evidence log exists;
- at least one tactic has artifact proof;
- build, SOP, or operational proof is linked;
- blocked items are not hidden.

## Cycle C4 - Graduation Or Archive

Goal: decide whether the system graduates, loops, pauses, or archives.

Gate:

- B2 matrix complete;
- B3 Lead/Lag logs summarized;
- Data archive packet prepared if closing;
- Jerry/Picard register updated.

## Weekly Review Prompt

`	ext
What did B1 decide, what did B2 accept, what did B3 prove, and what remains unsafe to scale?
`
"@
   = @"
---
id: B1_DECISION_CHARTER_00_AGENCY_AAS
layer: L2_Business_Pulse
kind: SummerProject
status: SHADOW_ACTIVE
date: 2026-05-26
---

# B1 Decision Charter - 00_Agency_aaS

## Decision Rights

B1 may decide:

- project or area direction;
- mode hypothesis: Solaris, Nexus, Orbiter, or mixed;
- which B2 domain receives the next handoff;
- whether Product stays prototype-only;
- whether a decision needs Beth, Morty, Jerry, Picard, or A0.

B1 may not:

- execute B3 work;
- bypass B2 gates;
- mark Business Done from Product Done;
- mutate provider/API/MCP/CLI config without explicit evidence and signoff;
- hide unresolved Finance, Legal, Ops, IT, or People risk.

## Output Packet

`yaml
decision_id: ""
date: "2026-05-26"
scope: "00_Agency_aaS"
question: ""
options:
  - ""
recommendation: ""
risk_if_wrong: ""
reversibility: "high|medium|low"
beth_status: "GREEN|ORANGE|HALT"
b2_owner: "Growth|Sales|Product|Ops|IT|Finance|People|Legal"
b3_artifact_required: true
proof_path: ""
next_review: ""
`

## Escalation

- HALT if Beth/Morty safety is red.
- Escalate to Jerry when the decision affects Area standards.
- Escalate to Picard when the decision changes project status.
- Escalate to A0 when the decision changes identity, budget, legal exposure, or direction.