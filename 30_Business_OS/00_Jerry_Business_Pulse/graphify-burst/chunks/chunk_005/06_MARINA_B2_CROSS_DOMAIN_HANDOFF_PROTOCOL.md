# MARINA B2 Cross-Domain Handoff Protocol

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
| People | Crew, training, supervisor | No field work without crew owner |
| IT | Schedule, route, records | Job tracking is visible |
| Product | Cleaning package and quality bar | Scope and exclusions are explicit |
| Growth | Client promise and intake | Expectations match SOP |
| Finance | Quote, cost, margin, payment | Job economics are visible |
| Legal | Insurance, safety, terms | Liability boundary is checked |

## Escalation
Ops escalates to Donna/DLQ when crew capacity, safety, client promise, payment, or QA proof is missing.

## Output
Ops emits one of three states:
- `GO`: B3 may execute.
- `CONDITIONAL`: B3 may execute only the named safe subset.
- `NO-GO`: work returns to the blocked B2 domain.
