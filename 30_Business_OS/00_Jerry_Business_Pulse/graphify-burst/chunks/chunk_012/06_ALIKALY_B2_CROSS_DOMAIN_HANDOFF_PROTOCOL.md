# ALIKALY B2 Cross-Domain Handoff Protocol

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
| People | Authority and stakeholder map | Decision owner is explicit |
| IT | Records and access path | Documents are controlled |
| Product | Entity purpose | Scope is explicit |
| Growth | External communication boundary | No unsupported public claim |
| Finance | Tax/account/budget path | Financial action is traceable |
| Legal | Filing and agreement path | No legal action is guessed |

## Escalation
Ops escalates to Donna/DLQ when legal certainty is missing, authority is unclear, finance/tax proof is absent, or a J03 dependency is unresolved.

## Output
Ops emits one of three states:
- `GO`: B3 may execute.
- `CONDITIONAL`: B3 may execute only the named safe subset.
- `NO-GO`: work returns to the blocked B2 domain.
