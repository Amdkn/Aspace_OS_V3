# HANDOVER — 2026-10-03 — GRAHAM TEMPORAL TRUTH SEMANTIC ACCEPTANCE v1.1

Parent: #448
Design merged previously: PR #449
Role: Graham / STATE · PROVENANCE · TEMPORAL TRUTH · CONTEXT

## Live-state correction

PR #449 was already merged before this semantic review began. This review therefore operates as a bounded post-merge correction, not as a redesign or rollback of Clara's architecture.

## Review result

The architecture is accepted.

Three semantic gaps had to be corrected before Ryan G0-G2 BUILD:

1. Claim identity / split-brain scope
   - CURRENT cannot be unique by subject alone.
   - Temporal truth must be keyed by at least subject + predicate + scope + source_authority.
   - GitHub, WorkGraph, runtime and Linear may all carry simultaneously current facts without being mutually contradictory.

2. Late-arriving historical evidence / Canon Resurrection
   - observed_at is the source-time of the fact.
   - recorded_at is when A'Space ingests it.
   - A late re-ingestion of an old observation must remain historical and cannot become current merely because it was recorded later.

3. Physiology freshness / scope
   - Physiology snapshots require explicit scope and validity boundary.
   - Provenance, freshness and epistemic state are separate.
   - STALE is freshness, not an epistemic truth value.

## Additional semantic laws

- CanonGraph records accepted interpretations under bounded authority; it is not itself a universal semantic authority.
- CanonTransition carries predicate, resolution_scope, and resulting canon head refs.
- Original TemporalClaims remain immutable; effective supersession is derived from transitions/query state rather than rewriting old claims.
- state_at / state_now operate on (subject, predicate, scope).
- ContextCapsule records source_cutoff_at so its world slice can be replayed.
- UNKNOWN remains local to the unresolved dimension.
- Provenance authenticates origin; it does not prove truth, freshness or cross-scope authority.

## Attack status

### Canon Resurrection
Semantic contract: PASS after correction.
A historical observation may be recorded later but keeps its original observed_at and cannot silently become CURRENT.

### Temporal Split-Brain
Semantic contract: PASS after correction.
Parallel CURRENT facts across different predicates/scopes/authorities are legal. The system must not invent a single global winner.

### Holon Runtime Migration
Semantic contract: PASS for G0 design boundary.
ContextCapsule carries replayable cutoff, canon slice, authority, evidence, contradictions, unknowns and return_to while containing no authoritative next_action.

## Ryan release boundary

Ryan is cleared to implement G0 -> G2 after this v1.1 correction merges and deterministic CI/schema validation passes.

Ryan must not:
- introduce latest-write-wins;
- mutate old TemporalClaims to mark them superseded;
- collapse provenance/freshness/epistemic state;
- infer OFFLINE from absence of WorkGraph claims/bindings;
- add a new database service before a demonstrated storage gap.

## Rory boundary

G3 still requires Rory's explicit typed reconciliation decision.
Graham may detect/qualify temporal contradiction but cannot silently decide semantic meaning outside its authority.

## No scope expansion

No Physiology v2.
No new scheduler.
No new SSOT.
No new cosmological plane.
No Supabase migration authorized by this review.
