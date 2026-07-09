# RILCOT B2 Cross-Domain Handoff Protocol

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
| People | Host/moderator/follow-up ownership | No ritual lacks an owner |
| IT | Member-space tooling | Access and support path are clear |
| Product | Member experience scope | Value promise and quality bar are explicit |
| Growth | Activation and retention motion | Funnel steps are operational |
| Finance | Membership economics | Revenue and recurring costs are visible |
| Legal | Community rules and privacy | Boundary is documented |

## Escalation
Ops escalates to Donna/DLQ when the member experience has no owner, no cadence, no feedback loop, or unresolved legal/privacy risk.

## Output
Ops emits one of three states:
- `GO`: B3 may execute.
- `CONDITIONAL`: B3 may execute only the named safe subset.
- `NO-GO`: work returns to the blocked B2 domain.
