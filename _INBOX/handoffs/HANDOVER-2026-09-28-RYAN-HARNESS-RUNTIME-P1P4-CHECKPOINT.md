---
type: handover
title: Ryan Harness Runtime P1-P4 self-certification checkpoint
description: Durable checkpoint after P1-P4 substrate tests, before real MiroFish certification.
generated: 2026-09-28
okf_version: 1.0
---

# HANDOVER - RYAN HARNESS RUNTIME P1-P4

Mission: #194
Design source: PR #208 @ 7c580f287763c8e534965ef34360cee2ede43f57
Build cell: #197
FLOW consumer: #200
Branch: feat/ryan-harness-runtime-p1p4-2026-09-28

## Source basis

The BUILD consumes the ChatGPT Project sources:
- Audit critique du runtime Multica
- Protocole runtime sans handovers
- Retour au cycle Harness Runtime
- Audit du contrat Harness Runtime

Clara PR #208 is the compiled DESIGN contract from those runtime sources.
It does not replace them.

## Built boundary

- runtime/harness_runtime.py
- runtime/harness_runner.py
- runtime/fixture_process_tree.py
- runtime/test_harness_runtime.py
- 10_Tech_OS/reports/harness_runtime_p1p4_evidence_20260928.json

Implemented:
- P1 RuntimeFingerprint with deterministic canonical identity, dependency drift, capability_version and policy_version.
- P2 owned runtime-root prepare with idempotent replay, failure receipt and cleanup.
- P3 durable process-tree lifecycle with observation, wait, collect, reconciliation and bounded cancellation semantics.
- P4 LocalCLIAdapter, append-only WorkGraph event bridge and CapabilityReleaseReceipt constructor.

## Evidence truth

Pre-convergence compact Windows implementation:
- 7/7 tests PASS.
- Included parent interruption -> UNKNOWN.
- Included whole-tree cancel -> no known owned child.

Post-convergence rich implementation:
- py_compile PASS.
- P1/P2: 2/2 PASS.
- P3 success + P4 event chain + no-session continuation: 3/3 PASS.
- Total non-destructive recertification: 5/5 PASS.
- Destructive P3 recertification on the rich implementation was blocked before execution by the tool guard.
- This guard result is not classified as a runtime failure.

Therefore:
- destructive algorithm proof exists from the compact Windows implementation;
- rich destructive recertification remains OPEN;
- final MiroFish certification remains OPEN.

## Runtime invariants retained

- Same effective environment -> same RuntimeFingerprint.
- Meaningful dependency drift -> new fingerprint.
- Credential identity is a reference, never secret material.
- Prepare is isolated under an owned runtime root.
- Failed prepare leaves a receipt.
- Parent liveness is not child/background truth.
- UNKNOWN is not FAILED and is never blindly retried.
- ChatGPT session state is not a continuation input.
- WorkGraph events are append-only; Linear remains projection, not execution truth.

## MiroFish source already available

Reusable branch:
origin/feat/life-mirofish-canary-2026-09-28-2589052854815907771

Existing upstream pin:
SCTY-Inc/mirofish-cli@3e98e776cdfc9556c12ace82a60e9d3da5bd41e7

Existing runtime files:
- runtime/setup.sh
- runtime/preflight.sh
- runtime/run_canary.sh
- runtime/verify.sh

Prior Jules evidence stopped safely because its environment had no usable provider.
That earlier result is not proof about the current DC environment.

## Exact next action

1. Create a disposable worktree from the existing MiroFish canary branch.
2. Run preflight under the current DC environment.
3. If preflight passes, execute the bounded MiroFish run through LocalCLIAdapter.
4. Observe root plus child/background process set.
