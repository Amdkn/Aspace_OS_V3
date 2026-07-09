# ABC B2 Cross-Domain Handoff Protocol

## Handoff Packet
Every B2 domain must hand Ops a compact packet before B3 execution:

```yaml
domain:
owner:
decision:
scope:
dependencies:
risks:
proof:
next_action:
deadline:
```

## Required Handoffs
| From | To Ops | Acceptance Standard |
| --- | --- | --- |
| People | Staffing and responsibility model | Named accountable owner and backup |
| IT | Tooling and records path | Access and storage are known |
| Product | Service scope | Deliverables and exclusions are explicit |
| Growth | Demand and promise | No unsupported claim enters delivery |
| Finance | Budget and unit economics | Costs and payment timing are visible |
| Legal | Compliance boundary | No childcare-sensitive action is unreviewed |

## Escalation
Ops escalates to Donna/DLQ when a packet is missing an owner, contains unresolved compliance risk, or asks B3 to execute without proof.

## Output
Ops emits one of three states:
- `GO`: B3 may execute.
- `CONDITIONAL`: B3 may execute only the named safe subset.
- `NO-GO`: work returns to the blocked B2 domain.
