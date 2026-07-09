# ABC IT Transverse Systems Access OS

## Purpose
IT is the transverse systems gate for 02 ABC OS & Child Care BOS. It ensures every B2 domain and B3 execution swarm has the right tools, access, data boundaries, runtime rules, support paths, and rollback before work becomes operational.

## Operating Thesis
ABC needs IT to protect childcare-sensitive records, scheduling, communication, access, and incident visibility.

## Eight-Domain System Interface
| Domain | IT Surface | Required Proof |
| --- | --- | --- |
| Growth | Campaign tools, attribution, landing assets | Tool owner, tracking path, source of truth |
| Sales | CRM, offer docs, intake, follow-up | Pipeline owner, client data path, handoff record |
| Product | Build tools, package docs, QA evidence | Version owner, artifact storage, acceptance path |
| Ops | SOP tools, schedule, delivery records | Runtime owner, incident path, rollback path |
| IT | Systems, access, data, automation | Admin owner, boundary, support path |
| Finance | Billing, accounts, reports, approvals | Finance data boundary, export path, approval record |
| People | Rosters, capacity, training, permissions | Agent access, role map, onboarding/offboarding |
| Legal | Contracts, terms, compliance evidence | Legal storage, privacy boundary, audit trail |

## IT Control Loop
1. Read the active B1 priority, B2 gate, and B3 task.
2. Identify the tools, records, automations, data, and access needed.
3. Name the system owner and support owner.
4. Define source of truth, permission boundary, and data retention path.
5. Confirm automation and approval boundaries.
6. Confirm incident, rollback, and recovery path.
7. Route sensitive records through Legal/Finance/People/Ops when needed.
8. Emit the IT readiness decision before execution or launch.

## B2/B3 Integration
| Layer | IT Responsibility |
| --- | --- |
| B1 Summer Direction | Keep technology aligned to project priority |
| B2 Domain Owners | Define system needs and approval boundaries |
| B3 Execution Agents | Execute inside named runtime and access limits |
| People Transverse | Confirm agent ownership before permissions are granted |
| Ops Transverse | Confirm systems are launch-ready before delivery |
| Donna/DLQ | Quarantine unsafe, ownerless, or unclear system work |

## Readiness States
- SYSTEM_READY: tools, access, data path, support, and rollback are explicit.
- NEEDS_SYSTEM_OWNER: the work returns to B2/People because ownership or permissions are unclear.
- QUARANTINE: the work routes to Donna/DLQ because system, data, or access risk is unsafe.

## Project Constraint
No childcare-sensitive data or workflow may run without access control, record path, privacy boundary, and support escalation.

## IT Metrics
- Tools with named owners.
- Active workflows with runtime boundary.
- Access exceptions.
- Missing source-of-truth records.
- Incident and support queue age.
- Automations awaiting approval.