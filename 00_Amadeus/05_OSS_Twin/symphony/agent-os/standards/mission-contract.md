---
title: Mission Contract (Symphony Payload v1.0)
---

> The **only** payload shape a Symphony tick may emit to a Hermes agent.
> Any deviation = tick refused at `before_dispatch` hook.

## Required fields (13)

```yaml
mission_contract_version: "1.0"     # MANDATORY — pinned
source_tool: airtable                # one of the 7 adapters
source_id: "<id>"                    # tracker-internal id
source_url: "<url>"                  # deep link
project: "<name>"                    # canonical project key
mission_type: client_pipeline_execution  # per-workflow enum
soa_domain: "Growth"                 # one of SOA01-SOA08
owner_b2: "Superman"                 # B2 DC manager for soa_domain
executor_b3: "Guardians"             # B3 Marvel squad for soa_domain
title: "<short>"                     # ≤ 80 chars
description: "<long>"                # ≤ 2000 chars
build_gate: "<text>"                 # PASS/BLOCKED definition
context_pack_url: "<url>"            # urn:aspace:rag:<id> or https://
forbidden_words: "<csv>"             # per-workflow lexique
sla:
  max_minutes: <int>                 # SDD-009 §2.3 axe temporel
  max_cost_usd: <float>              # axe financier
  max_retries: <int>                 # axe qualitatif
expected_proof: [list]               # see expected-proof.md
greenlight_required: true            # see writeback-policy.md
writeback_policy:                    # see writeback-policy.md
  external_write_requires_greenlight: true
  allowed_draft_outputs: [list]
```

## Validation

Zod schema at `before_dispatch` (symphony-base.spec.md §5.3.1) — missing
`soa_domain` or `build_gate` = exit 1, release claim. Per
`mission_contract_version` strict equality ("1.0"); future versions need
a new workflow_id.

## Why this exact shape

- 13 fields = the minimal "what + who + how long + what proof" tuple
- No free-form "notes" — everything parseable
- `source_id` + `source_url` = provenance, no broken refs after edits
- `sla` is a 3-axis object (not 3 flat fields) — enforces the SDD-009
  triade

## Cross-refs

- `candidate-record-rule.md` — what gets emitted
- `gate-decisions.md` — what `build_gate` describes
- `sla-triple.md` — SLA axes in depth
- `symphony-base.spec.md` §5.3 (WORKFLOW.md contract)
