# HANDOVER — 2026-09-28 — RYAN AMF M0 → YAZ / GRAHAM / RORY / NARDOLE / CLARA

Mission: #194
Design: #196 / PR #201
Build: #197
Ryan branch: `feat/ryan-amf-m0-2026-09-28`
Base design SHA: `24d83e0e`

## Source contract consumed

Ryan consumed Clara's physical design artifacts without redesign:
- `10_Tech_OS/machine_fabric/FACTORY_BLUEPRINT.json`
- `10_Tech_OS/machine_fabric/contracts/MACHINE_FABRIC_CONTRACTS.schema.json`
- `10_Tech_OS/machine_fabric/design/DESIGN_CONTRACT.md`
- `10_Tech_OS/machine_fabric/mvp/RYAN_BUILD_PACKET.md`
- `_INBOX/handoffs/HANDOVER-2026-09-28-CLARA-MACHINE-FABRIC-TO-RYAN.md`

## Current cell state

- Clara DESIGN contract: accepted for Ryan M0 by explicit build-gate comment on #197.
- Ryan M0 BUILD: implemented.
- Ryan self TEST: PASS.
- Independent Yaz/Graham/Rory review: OPEN.
- M1 Chrome/user worker: NOT STARTED.
- M2 private remote: NOT STARTED.

## Changed boundary

- `10_Tech_OS/machine_fabric/m0/amf_m0.py`
- `10_Tech_OS/machine_fabric/m0/test_amf_m0.py`
- `10_Tech_OS/machine_fabric/m0/run_m0_evidence.py`
- `10_Tech_OS/machine_fabric/m0/README.md`
- `10_Tech_OS/reports/amf_m0_evidence_20260928.json`

## Evidence

Commands:
```powershell
python -m py_compile amf_m0.py test_amf_m0.py run_m0_evidence.py
python test_amf_m0.py
python run_m0_evidence.py --out ..\..\reports\amf_m0_evidence_20260928.json
```

Observed:
- 9/9 tests PASS;
- 22/22 durable evidence assertions PASS;
- forced crash exit: 86;
- ledger before restart: RUNNING, receipt absent;
- effect count after crash: 1;
- restart reconciliation: SUCCEEDED, receipt present;
- effect count after reconciliation: 1;
- terminal replay effect count: 1;
- fingerprint conflict: 409;
- out-of-scope policy denial: 403 / DENIED;
- shell-shaped payload: 400 / INVALID_OPERATION;
- compensation: COMPENSATED with a distinct linked receipt.

Evidence:
`10_Tech_OS/reports/amf_m0_evidence_20260928.json`

## Authority and side effects

Allowed side effect in M0:
filesystem mutation only inside the explicit test root supplied at daemon start.

No machine-wide service was installed.
No Chrome extension or Native Messaging host was installed.
No Tailscale/Headscale/public listener was created.
Daemon bind is hard-limited to loopback.

## Known limitations

M0 is process-hosted rather than a Windows service.
Before-state for bounded reversible writes is stored in SQLite to support compensation.
Production encryption/retention for such evidence is not solved by M0.
M1/M2 remain separate mission cells.

## Cross-capability return-to

### Yaz / SENSE
Independently verify:
duplicate-prevention, restart latency, policy-denial observability,
health truthfulness, and that no silent duplicate effect occurs.

### Graham / REMEMBER
Verify:
receipt provenance, operation/fingerprint continuity,
policy version `amf-m0-policy-v1`, capability manifest version,
and evidence-addressability.

### Rory / COHERE
Verify:
no false ONLINE claim outside M0 profile,
no authority drift, no double effect, no receipt/effect divergence.

### Nardole / DISPATCH
Do not route M1 until independent M0 review is green.
M0 can close independently; M1/M2 are new cells.

### Clara / DESIGN
No redesign requested.
Only respond to CapabilityNeeds. Separate note: PR #201 OKF is currently failing,
while #197 explicitly carries an OPEN build gate; Ryan did not mutate Clara's CI/design
to hide that discrepancy.

## Exact next action

Review Ryan PR against Clara branch, then:
`Yaz TEST || Graham provenance || Rory coherence` in parallel.

If all independent reviews pass, Nardole may close M0 and open M1 as a new cell.
