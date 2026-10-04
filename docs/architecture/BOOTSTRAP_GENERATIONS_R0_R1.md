# Bootstrap Generations R0 → R1

Status: CANONICAL
Origin: #514
Program: #512 / Project V2 #8

## Principle

A bootstrap runtime may be highly active while constructing its successor, then become a quieter organ after the successor is operational.

This is **self-hosting maturation**, not failure or obsolescence.

```
R0 bootstrap organism
  ↓ builds / structures / certifies
R1 successor organism
  ↓ promoted by evidence
R0 transitions from active builder
  → REFERENCE
  → MONITOR
  → RECOVERY
  → PROVENANCE
  → DISPATCH_SUPPORT
  → RETIRED when safe
```

## Contract

```yaml
BootstrapGeneration:
  generation: R0|R1|R2
  builder_holon:
  built_runtime_ref:
  successor_ref:
  current_mode: BUILD_ACTIVE|REFERENCE|MONITOR|RECOVERY|PROVENANCE|DISPATCH_SUPPORT|RETIRED
  promotion_evidence: []
  rollback_ref:
  authority_scope:
  return_to:
```

## Invariants

1. Successor promotion requires evidence, not age.
2. R0 must not silently retain conflicting writer authority after promotion.
3. Demotion preserves history and rollback.
4. R0 and R1 may coexist for non-conflicting functions.
5. Institutional holon identity survives both generations.
6. A runtime that built the next runtime does not become the permanent identity of the institution.
7. A former builder may become an observability, provenance, dispatch, recovery or reference organ.

## A'Space application

A Solarpunk Kernel / CubeFarm bootstrap generation can begin as an active factory and later transition toward:
- Yaz monitoring;
- Graham provenance/replay;
- Nardole dispatch/reference;
- Donna recovery support;

while a newer certified organism performs active construction.

This pattern applies recursively to future A'Space generations.
