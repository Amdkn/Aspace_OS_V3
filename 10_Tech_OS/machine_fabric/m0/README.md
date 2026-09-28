# A'Space Machine Fabric — M0 Durable Mutation Kernel

Status: Ryan BUILD self-acceptance PASS. Independent review remains open.

## Boundary

M0 implements only the bounded Clara contract from PR #201 / issue #197:

- loopback-only HTTP daemon;
- SQLite operation ledger;
- canonical operation fingerprint;
- unified pre-execution policy;
- capability registry;
- `machine.fs.read`;
- reversible `machine.fs.write` (`write_text`, `append_text`, `compensate`);
- durable receipts;
- restart reconciliation;
- capability-scoped health.

M0 does **not** include Chrome, UIA, process control, Windows service installation,
Tailscale/Headscale, or public network exposure.

## Architecture tree

```
m0/
  amf_m0.py            operation engine + loopback HTTP daemon
  test_amf_m0.py       unit/integration/restart tests
  run_m0_evidence.py   durable acceptance evidence generator
```

Durable acceptance evidence:
`10_Tech_OS/reports/amf_m0_evidence_20260928.json`.

## Invariant

`typed capability -> policy -> operation_id -> precondition -> effect -> durable receipt -> replay/compensation`

A write becomes `RUNNING` with a durable effect plan before the external effect.
If the daemon dies after the effect but before the receipt, restart reconciliation
checks the expected postcondition. It never blindly repeats an unknown mutation.

## Exact verification commands

From `10_Tech_OS/machine_fabric/m0`:

```powershell
python -m py_compile amf_m0.py test_amf_m0.py run_m0_evidence.py
python test_amf_m0.py
python run_m0_evidence.py --out ..\..\reports\amf_m0_evidence_20260928.json
```

Observed on 2026-09-28: 9/9 tests PASS and 22/22 evidence assertions PASS.

## Fundamental canary

`mutation -> forced process exit 86 -> restart -> replay same operation_id -> zero duplicate mutation`

The evidence captures:
- ledger before restart: `RUNNING`, no receipt;
- effect count after crash: 1;
- ledger after restart: `SUCCEEDED`, durable receipt;
- effect count after reconciliation: 1;
- effect count after terminal replay: 1.

## Authority proofs

- same operation_id + different fingerprint -> HTTP 409 conflict;
- path outside explicit root -> DENIED / HTTP 403;
- unexpected shell-shaped payload -> INVALID_OPERATION / HTTP 400;
- loopback server constructor rejects `0.0.0.0`;
- compensation is a separate operation and receipt linked from the original.

## Health

M0 reports:
- daemon: `UP`;
- worker: `NOT_REQUIRED`;
- transport: `LOCAL`;
- aggregate: `ONLINE` for the M0 local-filesystem profile only.

It must not be interpreted as browser/UI/remote readiness.

## Known limitations

The M0 daemon is process-hosted, not yet installed as a Windows service.
Reversible before-state is stored in the local SQLite effect plan for bounded test-root
writes; production retention/encryption policy is a later design concern.
M1 and M2 remain separate cells.

## Rollback

Stop the loopback daemon, delete its SQLite ledger/test root, and revert the Ryan M0
commits. M0 installs no machine-wide service, browser extension, or public listener.
