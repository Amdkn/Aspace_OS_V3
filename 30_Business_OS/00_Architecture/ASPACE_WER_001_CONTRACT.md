---
spec_id: WER-001
spec_type: A-SPEC
version: 1.0.0
status: ACCEPTED
owner: Amdkn
origin_objective: 272
consumers: [WorkflowEngine, ReceiptAdapter]
repositories: [Amdkn/Aspace_OS_V3]
product_surfaces: [Business OS, Factory]
bounded_contexts: [Workflow, Reliability]
capabilities: [workflow.transition, effect.record]
authority: [BUSINESS, ARCHITECTURE]
state_owners: [WorkflowEngine]
evidence_required: [Receipt Persistence, Idempotency Simulation]
---

# [A-SPEC][WER-001] Workflow, event, effect, receipt & recovery contracts

## 1. Canonical Terminology
- **EffectReceipt**: Cryptographic or deterministic proof that a mutation occurred. HTTP 200 is not a business effect.
- **UNKNOWN**: State where a capability was invoked but the effect cannot be determined without an out-of-band check. UNKNOWN must never be blindly replayed.
- **Compensation**: The business or technical action required to reverse a partial or unintended effect.

## 2. Invariants
- HTTP 200 ≠ business effect proven.
- UNKNOWN ≠ FAILED.
- UNKNOWN is never blindly replayed.
- Human-in-the-loop is a first-class state (e.g., `REQUIRES_HUMAN`).

## 3. Authority Boundaries
Transitions are owned by the specific workflow domain. Workflow Engine enforces transition validity based on state machine boundaries.

## 4. Inputs / Outputs
- **Input**: Transition command or External Event.
- **Output**: `EffectReceipt`.

## 5. State Ownership
Business state is owned by domain aggregates. Workflow execution state is owned by the Workflow Engine.

## 6. Commands / Queries / Events
- `Command(Transition)` -> Evaluates -> Produces `EffectReceipt` -> Emits `Event(TransitionCompleted)`.

## 7. Effects and Receipts
Every completed external mutation MUST yield an `EffectReceipt` (see `WER_001.schema.json`).

## 8. Failure / UNKNOWN Behavior
If a transition yields UNKNOWN, it transitions to a `REQUIRES_HUMAN` or `NEEDS_RECONCILIATION` state rather than retrying. FAILED states can be retried if `retry_safe` is true.

## 9. Migration and Versioning
Workflows are versioned. Active transitions on old workflows continue on their original version unless explicitly migrated.

## 10. Implementation Consumers
- Python Workflow Engine implementations.
- Database/ledger projections.

## 11. Contract Tests
Tests must simulate:
- Duplicate webhook/retry.
- One forced external failure without double mutation or fabricated completion.

## 12. Release Evidence
Receipt simulation must pass `test_wer_engine.py` proving no double execution on retry of non-idempotent operation.
