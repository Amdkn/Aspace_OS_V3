# Ryan Build Packet — Harness Runtime P1-P4

Parent: #194
Design: #196
Build: #197
FLOW consumer: #200

## Goal

Build the smallest substrate that lets Ryan publish a reusable capability and leave the execution path.

Do not implement a new scheduler.
Do not encode Companion names as runtime identity.
Do not require ChatGPT sessions or handover markdown for continuation.

The target consumer is River/FLOW.
The first certification canary is the existing MiroFish incident.

## P1 — Runtime inspect/fingerprint

Implement typed:
runtime.inspect
harness.inspect

Return RuntimeFingerprint matching the Clara schema.
Acceptance:
- deterministic canonical JSON;
- same effective environment => same fingerprint;
- meaningful drift => new fingerprint;
- inspect performs no global install;
- fingerprint binds capability_version + policy_version;
- credential identity is referenced, never secret material.

Include process-group identity when execution already exists.

## P2 — Isolated prepare

Implement:
runtime.prepare
harness.prepare

Preparation must be scoped to an owned runtime root, venv or container.

Acceptance:
- replay same prepare is idempotent;
- dependency/lock provenance recorded;
- failure leaves receipt;
- bounded cleanup/compensation exists;
- no silent global Python/Node/PATH/proxy mutation;
- P1 exposes drift after prepare.
## P3 — Process-tree lifecycle

Implement:
harness.launch
harness.resume
harness.observe
harness.wait
harness.cancel
harness.collect
harness.reconcile

Execution is owned by process group/job, not parent PID.

Acceptance:
- durable operation_id/execution_id;
- root + child/background inventory;
- heartbeat/stale detection;
- cancellation kills complete owned tree;
- timeout cannot leave untracked owned children;
- restart reconcile reports effect YES/NO/UNKNOWN;
- UNKNOWN never retries blindly.
## P4 — Adapter + continuation substrate

Implement generic adapter protocol for provider harnesses.

Minimum one real adapter needed for certification.
MiroFish may use the runtime/provider already proven by River preflight.

Implement machine objects:
CapabilityReleaseReceipt
DispatchEnvelope
HarnessExecutionRequest
HarnessExecutionReceipt
ReconcileDecision
ContinuationEnvelope

Ryan only produces CapabilityReleaseReceipt for publication.
Ryan does not manually deliver each future execution to River.

The runtime must expose enough event/receipt data for Nardole and Rory to operate without reading a handover.
## WorkGraph integration

Reuse current work_id and append-only event table.

Add event writers/readers for:
capability_release
dispatch_envelope
harness_execution_requested
runtime_prepared
harness_execution_started
harness_observed
harness_execution_receipt
rory_reconcile_decision
continuation_routed
continuation_resolved

Do not mutate Linear as execution truth.

If schema migration is needed, keep it minimal and backwards-compatible.
Prefer existing claim/lease/session_binding tables over a second lease model.
## First canary

1. Publish Harness Runtime capability version.
2. Nardole routes a READY MiroFish cell to River.
3. River issues HarnessExecutionRequest.
4. Runtime inspect/prepare passes.
5. Launch one bounded MiroFish run.
6. Ensure a child/background process is visible.
7. Force root/parent interruption.
8. Reconcile process tree and artifacts.
9. Emit HarnessExecutionReceipt.
10. Rory returns ReconcileDecision.
11. Nardole returns ContinuationEnvelope.

No manual handover is allowed between steps 1-11.
## Evidence

Ryan PR must include:
- contract validation tests;
- fingerprint drift fixtures;
- idempotent prepare proof;
- child/background enumeration proof;
- whole-tree cancel proof;
- forced interruption transcript;
- no orphan owned child after cancel/timeout;
- HarnessExecutionReceipt fixture;
- CapabilityReleaseReceipt publication proof;
- event-chain readback from WorkGraph;
- rollback/removal instructions.

Independent verification:
Yaz = lifecycle/orphan/latency/health.
Graham = provenance/version binding.
Rory = reconciliation invariants.
Nardole = dispatch/return correctness.

Chrome M1 and private remote M2 remain out of scope.
