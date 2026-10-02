# A-SPEC CCS-001: Business Capability Contracts + CQE

```yaml
spec_id: CCS-001
spec_type: CCS
version: "1.0"
status: ACCEPTED
owner: Business OS
origin_objective: "#272"
consumers:
  - Office
  - Operations
  - Mobile
repositories:
  - Aspace_OS_V3
product_surfaces:
  - Public
  - Operations
  - Edge
bounded_contexts:
  - Business Operations
  - Customer Service
capabilities:
  - customer.intake
  - case.progress.read
  - document.request.create
  - booking.create
authority: business:write, business:read
state_owners: Tenant
evidence_required: true
migration_from: legacy-crud
supersedes: ""
```

## 1. Intent

This specification defines the canonical structure of a Business Capability Contract. It separates the **business meaning** (intent, inputs, authority, side effects) from the **transport or projection** (React, HTTP, Mobile, CLI, MCP).

Generic CRUD is NOT the canonical business language. All capabilities must be typed as Command, Query, or Event (CQE):
- **Query** = asks for state, no business mutation.
- **Command** = expresses intended mutation.
- **Event** = observed fact that already happened.

## 2. Contract Structure

Each capability contract must comply with `contracts/business.capability.v1.schema.json` and define:
- `capability_id` + `version`
- `domain_owner`
- `intent`
- `effect_class` (COMMAND, QUERY, EVENT)
- `input_schema` and `output_schema`
- `preconditions`
- `authority`
- `deterministic_validation`
- `side_effects`
- `idempotency`
- `compensation`
- `evidence_required`
- `supported_surfaces` (adapters/projections)

## 3. Initial Capability Vocabulary

The following capabilities have been defined to prove that Office, Operations, and Mobile can share one contract with multiple projections:

1. **`customer.intake`**: Record a new customer lead or intake form.
2. **`booking.create`**: Create a new booking/appointment.
3. **`case.progress.read`**: Read the current progress status of a case.
4. **`document.request.create`**: Create a new document request for a customer.

## 4. Verification

The contracts are automatically verified by `contracts/test_business_contracts.py` ensuring they all adhere to the same schema and provide support for multiple projection surfaces.
