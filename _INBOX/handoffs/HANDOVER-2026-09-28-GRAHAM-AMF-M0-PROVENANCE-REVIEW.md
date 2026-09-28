# HANDOVER — 2026-09-28 — GRAHAM AMF M0 PROVENANCE REVIEW

Mission: GitHub #194 A'Space Machine Fabric
Design: #196 / PR #201
Build: #197 / PR #202
Reviewed head: `6edbdded5c91a40899d4ea211be22d79169c9842`
Capability: Graham / REMEMBER · STATE · REPLAY

## Result

Ryan BUILD and self-test remain PASS.
Independent Graham execution reproduced `9/9 tests PASS` on the Ryan worktree with bytecode writes disabled.
Crash/restart/replay semantics inspected in code preserve the proven no-double-effect behavior.
Unknown or unmatched postcondition during RUNNING reconciliation goes to `DLQ` with `blind replay forbidden`.
Compensation is a distinct operation and the original receipt receives the compensation operation reference.

## Provenance finding

Policy provenance is durable: ledger and receipt preserve `amf-m0-policy-v1`.
Capability manifest provenance is not durable.
The live registry declares `machine.fs.write version=0.1.0`, but receipt, operation ledger and semantic fingerprint do not bind that version.
Therefore a future manifest revision could not be distinguished from 0.1.0 using the historical receipt alone.

## Classification

Graham certification: **BLOCKED only on capability-version provenance**.
Ryan BUILD PASS is not revoked.
M0 crash/replay canary is not revoked.
M1/M2 remain HOLD.
M0 must not be called SHIPPED until the smallest provenance gap is closed.

## CapabilityNeed

`CAPNEED-20260928-AMF-M0-CAPABILITY-VERSION-PROVENANCE`

Requested route:
1. Clara DESIGN chooses the minimal receipt/ledger provenance contract.
2. Ryan BUILD applies only that bounded patch and tests it.
3. Graham reruns receipt/replay provenance certification.
4. Rory may continue coherence review in parallel; no need to wait for this design micro-cell.
5. Nardole converges Yaz + Graham + Rory receipts before closing M0.

## Evidence

- PR #202 head above.
- Clara contract: `MACHINE_FABRIC_CONTRACTS.schema.json`.
- Ryan evidence: `10_Tech_OS/reports/amf_m0_evidence_20260928.json`.
- Independent local run: 9/9 tests PASS.
- Independent provenance canary: receipt has policy_version but `receipt_has_capability_version=false`.
- Code path inspected: `_receipt`, operations ledger, `_reconcile_running`, `_link_compensation`.

## Authority / side effects

No Ryan or Clara source code was modified.
No M0 state was promoted.
No claim/session binding was fabricated.
Only Graham handover + CapabilityNeed are added in the Graham worktree.

## Return-to

Clara → contract delta.
Ryan → bounded implementation/test.
Graham → recertify.
Nardole → close/reopen smallest cell after all independent receipts.
