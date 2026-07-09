---
id: B1_DECISION_CHARTER_CEOS_DESKTOP
layer: L2_Business_Pulse
kind: CEO_Command_Center
status: PHASE_1_SKELETON
created: 2026-06-07
parent_jerry: J01_Jerry_Prime_LD01_Business
project_slug: ceo-desktop
---

# Decision Charter — CEO's Desktop

> Stub. To be ratified in Cycle C1 of the 12WY cadence.

## Decision Rights (Draft)

B1 (A0) may decide:

- the 1Y/3Y/10Y direction of the CEO's Desktop;
- which SOB domain receives the next handoff;
- whether a domain is moved from PENDING → ACCEPTED → BLOCKED in the handoff queue;
- whether the desktop stays shadow-active, activates, or pauses;
- whether a decision needs Beth, Morty, Jerry, Picard, or a 4-boundary gate (IT, Finance, Legal, People).

B1 (A0) may not:

- execute B3 work directly;
- bypass B2 DoD gates;
- mark a SOB domain as Business Done from Product Done alone;
- mutate provider/API/MCP/CLI config without explicit evidence and signoff;
- hide unresolved IT, Finance, Legal, or People risk.

## Output Packet (Draft Schema)

```yaml
decision_id: ""
date: "2026-06-07"
scope: "ceo-desktop"
question: ""
options:
  - ""
recommendation: ""
risk_if_wrong: ""
reversibility: "high|medium|low"
boundary_gates:
  it: "GREEN|ORANGE|HALT|NA"
  finance: "GREEN|ORANGE|HALT|NA"
  legal: "GREEN|ORANGE|HALT|NA"
  people: "GREEN|ORANGE|HALT|NA"
beth_morty_status: "GREEN|ORANGE|HALT"
b2_owner: "Growth|Sales|Product|Ops|IT|Finance|People|Legal"
b3_artifact_required: true
proof_path: ""
next_review: ""
```

## Escalation

- **HALT** if Beth/Morty safety is red, or if any of the 4 boundary gates is HALT.
- **Escalate to Jerry** when the decision affects an Area standard or the Life Wheel balance.
- **Escalate to Picard** when the decision changes a project status (shadow → active → paused → archived).
- **Escalate to A0** (self) when the decision changes identity, budget, legal exposure, or the 1Y/3Y/10Y direction itself.

## Phase 1 Action

The first decision-charter entry will be logged when C1 (Direction Lock) closes — ratifying the North Star, the 12WY cadence, and this charter itself.
