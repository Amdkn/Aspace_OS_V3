# MARINA B2/B3 Agent Command Protocol

## Command Packet
Every cross-domain task must have this packet before B3 execution:

`yaml
project: Marina Cleaning BOS & SOP
b1_priority:
b2_domain:
b2_owner:
b3_agent:
job_to_be_done:
decision_rights:
capacity_check:
dependencies:
proof_required:
escalation_path:
status:
`

## Assignment Rules
| Rule | Standard |
| --- | --- |
| One owner | Every domain decision has exactly one accountable B2 owner |
| One executor | Every JTBD has exactly one accountable B3 agent |
| One proof path | Every task names its artifact, log, or acceptance proof |
| One escalation | Every risky task names where it goes when blocked |
| Capacity visible | People rejects assignments that overload an agent without backup |

## Cross-Domain Handoff
People validates the human/agent side of the handoff before Ops validates execution readiness.

| Handoff Type | People Must Confirm |
| --- | --- |
| B1 to B2 | Priority, authority, and domain owner |
| B2 to B2 | Sender, receiver, dependency, decision needed |
| B2 to B3 | Executor, output, proof, deadline |
| B3 to B2 | Artifact, evidence, acceptance request |
| B3 to Ops | Delivery owner, SOP owner, blocker owner |
| Any to Donna/DLQ | Failure reason and recovery owner |

## Refusal Conditions
People blocks B3 work when:
- no B2 owner is named;
- no B3 agent is named;
- decision rights are unclear;
- capacity is unknown;
- proof is vague;
- the work touches Legal, Finance, childcare, field delivery, or entity governance without escalation clarity.

## Output
People emits one of three states:
- ASSIGNED: B3 can execute.
- NEEDS_OWNER: return to B1/B2 for ownership.
- DLQ: route to Donna because the work is unsafe, blocked, or ownerless.