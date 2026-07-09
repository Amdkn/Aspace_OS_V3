# JTBD-002 AAAS Transverse People Agent Governance Gate

## Job
When Agency as a Service prepares any B2 or B3 action across the eight domains, People must verify that the right agents are assigned, accountable, capable, and connected to a proof path.

## Trigger
Use this gate before:
- creating a new B3 execution task;
- moving work between B2 domains;
- launching a cross-domain initiative;
- changing owner, scope, or deadline;
- escalating to Ops, Legal, Finance, or Donna/DLQ.

## Output
A dated People governance decision:
- ASSIGNED
- NEEDS_OWNER
- DLQ

## Readiness Checks
| Check | Question |
| --- | --- |
| B2 owner | Who owns the domain decision? |
| B3 agent | Who executes the concrete task? |
| Decision rights | Can this owner decide or approve? |
| Capacity | Can the agent execute now without overload? |
| Dependencies | Which domains must respond? |
| Proof | What artifact proves completion? |
| Escalation | Where does the task go if blocked? |
| Ops link | Does this need Ops Transverse Gate before launch? |

## Guardrail
No B3 task may run without a named B2 owner, named B3 agent, proof path, and escalation route.

## Proof
Attach the command packet, roster update, handoff note, and final People decision.