# JTBD-002 MARINA Transverse IT Systems Gate

## Job
When 05 Marina Cleaning BOS & SOP prepares any B2 or B3 action across the eight domains, IT must verify the systems, access, data, automation, support, and rollback boundary before execution or launch.

## Trigger
Use this gate before:
- creating or changing a tool, account, automation, repository, or data store;
- launching a B3 workflow that touches records or client/member/entity/job data;
- granting permissions to any B2 owner or B3 agent;
- moving work to Ops launch readiness;
- changing source of truth, support, or rollback path.

## Output
A dated IT readiness decision:
- SYSTEM_READY
- NEEDS_SYSTEM_OWNER
- QUARANTINE

## Readiness Checks
| Check | Question |
| --- | --- |
| System owner | Who owns the tool/runtime? |
| Access owner | Who approves and revokes permissions? |
| Source of truth | Where does the canonical record live? |
| Data boundary | What data is touched and how is it protected? |
| Automation boundary | What can run automatically and what needs approval? |
| Support path | Where does failure go? |
| Rollback path | How is the change paused, reverted, or quarantined? |
| People/Ops link | Are agent ownership and launch readiness aligned? |

## Guardrail
No field job may launch without schedule/route system, job record, photo/QA path, access owner, and support escalation.

## Proof
Attach the systems packet, access map, runtime boundary, support path, rollback path, and final IT decision.