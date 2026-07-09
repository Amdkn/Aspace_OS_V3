---
title: SOA Domain Routing
---

> Per the 8 SOA sectors (L2 Business OS), every Symphony tick routes
> through exactly one B2 (manager) + one B3 (squad). The orchestrator
> is ALWAYS the first worker.

## Canonical mapping (L2 Shadow Business)

| SOA Domain | B2 Owner (DC) | B3 Squad (Marvel) | Hermes primary | Support workers |
|---|---|---|---|---|
| **Growth** (SOA05) | Superman | Guardians of the Galaxy | orchestrator | researcher, strategist |
| **Sales** (SOA08) | John Jones | Illuminati | orchestrator | strategist, reviewer |
| **Finance** (SOA06) | Wonder Woman | Thunderbolts | orchestrator | reviewer |
| **Ops** (SOA03) | Batman | Fantastic Four | orchestrator | ops-watch |
| **Product** (SOA04) | Flash | Avengers | orchestrator | builder, qa, reviewer |
| **IT** (SOA02) | Cyborg | Kang Dynasty | orchestrator | builder, qa, reviewer |
| **People** (SOA01) | Green Lantern | X-Men | orchestrator | strategist |
| **Legal** (SOA07) | Aquaman | Eternals | orchestrator | reviewer |

## Rules

1. **Orchestrator first** — every tick, no exceptions
2. **B2 / B3 are not human** — they're the routing keys. The actual
   human is A0 (validation finale, greenlight)
3. **Cross-domain** — if a record touches 2+ domains, the orchestrator
   picks the **primary** and `cross_refs: []` lists the others
4. **Out-of-slot** — Ops/Product/IT/People/Legal records in an
   Airtable-L2 workflow → recommend a ClickUp task instead of running
   directly. See `WORKFLOW.solaris-clickup-ops.md` for the inverse

## Anti-patterns

- ❌ Routing "Growth" record to "Batman" (Ops B2) — mismatch
- ❌ Skipping orchestrator (calling researcher directly) — no triage
- ❌ Two B3 squads for the same record — split the mission, don't merge
- ❌ Hardcoding the B2/B3 in the prompt — let the routing table decide

## Cross-refs

- `mission-contract.md` — `soa_domain` + `owner_b2` + `executor_b3` fields
- `gate-decisions.md` — when to escalate
- `entity_symphony_router.md` (wiki) — B1 Symphony Router concept
