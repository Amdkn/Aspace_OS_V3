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

Current HEAD recertification:
- py_compile PASS.
- Full Windows suite: **7/7 PASS in 13.822s**.
- P1 fingerprint determinism/drift PASS.
- P2 idempotent prepare/failure receipt/cleanup PASS.
- P3 parent interruption -> UNKNOWN -> retry_safe=false PASS.
- P3 whole-tree cancel PASS.
- P3 success/artifact/effect=YES PASS.
- P4 CapabilityRelease constructor + append-only WorkGraph event chain PASS.
- No ChatGPT session state required PASS.
- Post-test targeted sweep: **0 owned fixture/harness_runner processes lingering**.
- Python 3.14 emitted ResourceWarning for detached Popen handles; this is recorded as implementation hygiene, not an orphan-process failure.

Therefore:
- P1-P4 substrate self-certification is PASS;
- final real MiroFish certification remains OPEN;
- no final CapabilityReleaseReceipt is published until that real canary closes.

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

## MiroFish real preflight status

Disposable worktree created:
C:\Users\amado\orca\workspaces\ASpace_OS_V3\MiroFishCanaryRyan

Reusable branch:
origin/feat/life-mirofish-canary-2026-09-28-2589052854815907771

Pinned upstream:
SCTY-Inc/mirofish-cli@3e98e776cdfc9556c12ace82a60e9d3da5bd41e7

Current WSL environment:
- Python 3.12.3
- claude executable present
- codex executable present
- no global Python/Node/PATH/proxy mutation performed

Observed real bootstrap defects:
1. The canary shell scripts checkout with CRLF; WSL initially reports bash\\r.
2. After local line-ending normalization, preflight correctly reports the isolated venv missing.
3. Official setup creates the venv and installs hatchling/hatch-vcs/uv, then uv editable install fails in build isolation on an invalid Wheel-Version dependency.
4. No-build-isolation exposes an undeclared build dependency: editables.
5. After adding editables only inside the disposable venv, the no-deps MiroFish entrypoint builds.
6. mirofish doctor then fails at import with ModuleNotFoundError: dotenv.
7. Upstream provider values are claude-cli/codex-cli, while this machine exposes claude/codex; any alias must remain runtime-local.
8. Upstream uv.lock resolves sentence-transformers -> torch 2.11.0 plus Linux CUDA/CUDNN/NCCL/CUSPARSE/TRITON packages, so a naive full install is not accepted as the minimal certification path.

Interpretation:
- P1-P4 substrate self-certification remains PASS.
- MiroFish full certification remains OPEN.
- The current blocker is an adapter/bootstrap defect, not a Harness Runtime failure.
- No final CapabilityReleaseReceipt has been published.
- No synthetic HarnessExecutionReceipt may be emitted.

## Exact next action

1. Keep the disposable MiroFish worktree as the certification source.
2. Add a lean isolated dependency/provider profile in Ryan's adapter boundary.
3. Preserve the upstream pin and runtime-local provider aliasing.
4. Obtain a real bounded MiroFish launch without global environment mutation.
5. Observe root plus child/background process set.
6. Reconcile report/verdict.json as YES / NO / UNKNOWN.
7. Emit the real HarnessExecutionReceipt.
8. Route the receipt to Rory; UNKNOWN routes Donna and never blind retry.
9. Only after Rory/Nardole closure publish the final CapabilityReleaseReceipt.

## Return-to

Yaz: lifecycle/orphan/latency/health.
Graham: fingerprint/provenance/version binding.
Rory: reconciliation from machine state + receipt.
Nardole: dispatch/return routing without handover dependency.
River: consume only the typed runtime receipt/event chain.
Donna: UNKNOWN recovery.
Clara: DESIGN gap only; ordinary bootstrap defects stay in Ryan BUILD.

## Rollback

Delete the disposable MiroFish worktree/runtime cache and revert Ryan adapter changes.
No machine-global installation or configuration change is required for rollback.
