---
type: build_packet
title: Ryan Build Packet AMF MVP v0.1
description: Accepted bounded build packet for Ryan to implement the Machine Fabric MVP.
generated: 2026-09-28
okf_version: 1.0
---

# Ryan Build Packet — AMF MVP v0.1

Parent: #194 · Design: #196 · Build: #197

## Accepted boundary

Ryan may start now.

Do **not** build the complete Desktop Commander replacement. First prove the execution invariant with the smallest useful vertical slice.

### M0 — durable mutation kernel — REQUIRED FIRST

Build:
1. local Windows daemon bound to loopback;
2. SQLite operation ledger;
3. operation schema + fingerprint;
4. unified policy hook;
5. capability registry;
6. one read capability;
7. one reversible mutation capability: `machine.fs.write` on an explicitly allowed test directory;
8. durable Receipt API;
9. restart recovery logic;
10. health endpoint.

Fundamental acceptance:
`mutation -> daemon crash/restart -> replay same operation_id -> zero duplicate mutation`.

Concrete canary:
- create a test file or append a uniquely fingerprinted record once;
- force daemon termination after effect boundary;
- restart;
- submit exactly the same operation_id/fingerprint;
- result returns prior/reconciled receipt;
- file/effect count remains exactly 1.

Also prove:
- same operation_id + different fingerprint => rejected;
- out-of-scope path => DENIED receipt;
- shell/path canonicalization cannot bypass allowed root;
- a reversible write has an explicit compensation operation with separate receipt.

### M1 — user worker + Chrome presence — SECOND

Only after M0 is green.

Build:
- signed-in user worker heartbeat/registration;
- capability lease/fencing token;
- Chrome MV3 extension;
- Native Messaging host;
- list-tabs read capability;
- one deterministic DOM/accessibility action with receipt;
- extension/service-worker reconnect canary.

Must prove:
- daemon alive + worker dead => DEGRADED;
- reconnect does not double-claim a job;
- same browser operation_id survives Native Messaging reconnect;
- DOM action yields postcondition evidence + durable receipt.

Do **not** add debugger/CDP action to M1. Only expose manifest entry as unavailable/privileged unless separately authorized.

### M2 — private remote transport — THIRD

After M0/M1.

Use Tailscale Serve as the first private canary over the same loopback daemon.

Must prove:
- remote reconnect retains operation identity;
- ACL/transport identity does not bypass capability policy;
- no public bind;
- vendor quota is not part of local execution semantics.

Headscale/WireGuard is research/certification later, not M2 acceptance.

## Implementation freedom

Ryan chooses language/framework unless it breaks:
- durable SQLite semantics;
- Windows service/user-worker boundary;
- typed contracts;
- idempotent recovery tests;
- adapter isolation.

Reuse compatible upstream code only with license/provenance recorded. Do not copy hosted Remote Desktop Commander internals.

## Evidence required in Ryan PR

- architecture tree;
- exact test commands;
- M0 crash/restart/replay transcript;
- SQLite ledger rows before/after replay;
- duplicate count assertion;
- policy denial proof;
- compensation proof;
- M1 worker health transition proof when implemented;
- Chrome reconnect proof when implemented;
- M2 private transport proof when implemented;
- latency and failure metrics;
- known limitations;
- rollback/removal procedure;
- handovers to Yaz/Rory/Amy/Graham/Nardole.

## Stop conditions

Stop and emit CapabilityNeed/EscalationPacket instead of widening scope if:
- Windows service boundary requires authority not granted;
- receipt cannot establish effect truth;
- operation replay class is ambiguous;
- debugger/CDP becomes necessary for M0/M1;
- remote transport requires public exposure;
- an upstream adapter can only work by bypassing unified policy.

## Completion

M0 can close independently. M1/M2 are subsequent cells, not reasons to hold M0 hostage.
