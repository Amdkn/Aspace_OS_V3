---
type: handover
title: Clara Machine Fabric to Ryan Build
description: Durable Clara-to-Ryan handover for Machine Fabric mission 194 and build cell 197.
generated: 2026-09-28
okf_version: 1.0
---

# HANDOVER — 2026-09-28 — CLARA MACHINE FABRIC → RYAN BUILD

Mission: #194
Completed cell: #196 Clara / DESIGN
Input: Bill #195 + PR #199
Return-to: Ryan #197

## Decision

AMF is not DC2 and not a DesktopCommanderMCP fork.

AMF owns:
`typed capability -> policy -> operation_id -> precondition -> effect -> durable receipt -> replay/compensation`.

Upstreams are adapters behind that law.

## Durable design artifacts

- `10_Tech_OS/machine_fabric/FACTORY_BLUEPRINT.json`
- `10_Tech_OS/machine_fabric/contracts/MACHINE_FABRIC_CONTRACTS.schema.json`
- `10_Tech_OS/machine_fabric/design/DESIGN_CONTRACT.md`
- `10_Tech_OS/machine_fabric/mvp/RYAN_BUILD_PACKET.md`

The design maps onto the fractal FactoryBlueprint/CapabilityNeed/EscalationPacket contracts from PR #187 without creating a parallel ontology.

## Accepted architecture

### Daemon/service
Owns ledger, operation identity, jobs/leases, policy, receipts, capability registry, health and transports.

### Signed-in user worker
Owns interactive-session capabilities: UIA/accessibility, Native Messaging presence, clipboard, pointer/keyboard and other session-bound adapters.

### Browser authority
Separate grants for tabs, DOM read, DOM action, network inspection, debugger/runtime evaluation and performance trace. Debugger is privileged and deny-by-default.

### Remote
Loopback by default.
Tailscale Serve = private v0 canary.
Headscale/WireGuard = later sovereignty certification.

## Ryan is unblocked

Ryan #197 may start **M0 immediately**.

M0 is deliberately smaller than the full provisional #197 list:
- loopback daemon;
- SQLite ledger;
- unified policy;
- capability registry;
- `machine.fs.read`;
- bounded reversible `machine.fs.write`;
- durable receipts;
- restart recovery;
- health.

Fundamental canary:
`mutation -> crash/restart -> replay same operation_id -> zero duplicate mutation`.

M1 worker/Chrome and M2 private remote are follow-on mission cells, not blockers to M0 closure.

## Mandatory M0 proof

1. one mutation effect only;
2. replay same operation_id returns/reconciles receipt;
3. same operation_id + different fingerprint is denied;
4. out-of-scope path denied;
5. shell/path path cannot bypass authority;
6. compensation operation has its own linked receipt.

## Cross-capability handoff

- Yaz: duplicate-prevention, latency, failure/health metrics.
- Graham: receipt/provenance + manifest/policy version.
- Rory: no false online, no double claim, authority drift.
- Nardole: route/retry/backpressure and return-to.
- Amy: health/approval/receipt presentation.
- Donna: unknown-effect/DLQ causal recovery.
- Rick/Doctor13: only authority expansion or semantic policy conflict.

## Stop conditions

Ryan must emit CapabilityNeed/EscalationPacket rather than widening scope if operation effect truth, replay safety or authority cannot be established.

Evidence closes M0; Chrome/remote breadth does not.
