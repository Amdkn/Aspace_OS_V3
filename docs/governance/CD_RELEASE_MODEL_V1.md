# A'Space CD & Release Model v1

Status: architecture contract; implementation varies per product

## Purpose

Separate integration truth from promotion truth.

CI answers:
> Can this mutation be accepted into the integrated codebase?

CD answers:
> Can this accepted version be promoted to this target, now, with known rollback?

Observability answers:
> What is actually running and behaving in that target?

## Release state machine

```
SOURCE_MUTATION
  -> CI_ACCEPTED
  -> MERGED
  -> RELEASE_CANDIDATE
  -> DEPLOYING
  -> DEPLOYED
  -> CANARY_VERIFIED
  -> PROMOTED
  -> RELEASED
```

Exceptional states:
`BLOCKED | FAILED | UNKNOWN | ROLLED_BACK`.

UNKNOWN must remain distinct from FAILED.

## ReleaseProfile

Before a product gets automated CD it should declare:

```yaml
ReleaseProfile:
  product_id:
  source_repo:
  artifact_kind:
  version_source:
  target_classes: []
  required_ci_checks: []
  deployment_adapter:
  migration_strategy:
  health_checks: []
  functional_canary:
  promotion_rule:
  rollback_strategy:
  evidence_sinks: []
  authority_owner:
```

No generic workflow should invent these values.

## Product-specific directions

### Tech OS / Solarpunk Kernel

Default goal:
PR -> CI -> bounded Kernel/runtime canary -> version/release.

A kernel release is not automatically a public deployment.
Machine/runtime promotion requires separate observed evidence.

### Agent OS

Expected pattern:
PR -> CI -> target-specific build -> localhost/staging or equivalent -> E2E -> release/deploy -> runtime observation.

Exact environments and deploy commands are intentionally not asserted here until its ReleaseProfile is accepted.

### Life OS

Expected pattern:
PR -> CI -> staging-equivalent -> E2E -> production-equivalent -> functional canary -> release evidence.

Exact targets remain product-owned.

### Business OS

Expected pattern:
PR -> CI/integration tests -> staged promotion -> business-domain canary -> production-equivalent -> evidence.

Business semantics and irreversible external effects remain Business-owned.

### CubeFarm

Expected pattern:
upstream/fork reconciliation -> PR -> build -> QA agents -> browser/runtime canary -> release.

CubeFarm remains a bounded factory/habitat consumer, not A'Space's universal release engine.

## GitHub primitives

Use:
- Actions for deterministic build/test/deploy steps;
- Environments for deployment targets and approvals when a product is ready;
- Releases/tags for immutable promoted versions;
- deployment records/statuses for promotion evidence;
- artifacts for build/test evidence;
- Issues only for failures that require executable follow-up.

## Promotion law

A merge does not authorize deployment by itself.

A promotion requires:
- accepted source version;
- target identity;
- authority to mutate that target;
- health/readback;
- bounded canary;
- rollback knowledge.

## Rollback law

Every consequential CD path must answer before promotion:
- what exact version/state can we return to?
- how is data/schema compatibility handled?
- which effect is reversible vs compensating-only?
- what evidence proves rollback completed?

## First implementation target

Do not automate all products at once.

Choose one product with:
- known build command;
- known target;
- known health check;
- low-cost rollback;
- existing CI.

Prove one full path:
`merge -> release candidate -> deploy -> canary -> promote -> rollback rehearsal -> evidence`.

Then reuse only the generic patterns that actually survived the canary.
