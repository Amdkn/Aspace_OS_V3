---
type: Architecture audit
title: "A'Space V3 runtime vivance audit"
description: Source-grounded map of why the V3 runtime has viable primitives but no continuously executing, self-recovering and reproducing control loop.
tags: [aspace-v3, runtime, autonomy, kernel, replication]
generated: { by: verdent-gpt-5.6-sol, at: 2026-08-30T09:45:00-04:00 }
verified:
  - { by: verdent-gpt-5.6-sol, at: 2026-08-30T09:45:00-04:00 }
sources:
  - id: kernel
    resource: "10_Tech_OS/kernel/"
    title: "V3 kernel implementation"
    last_modified: 2026-08-03
  - id: production-state
    resource: "10_Tech_OS/kernel/uc.db"
    title: "Observed production queue state"
    last_modified: 2026-08-03
  - id: full-audit
    resource: "40_Memory_Wiki_OKF/architecture/audit-vivance-aspace-v3-2026-08-30.md"
    title: "Full causal audit and recovery order"
    last_modified: 2026-08-30
okf_version: "0.2"
---

# Runtime status

A'Space V3 has a small queue protocol and several active infrastructure
components, but it does not currently have a detached process that closes the
whole runtime loop.

The kernel can complete a manually driven path:

`submit → claim → predict → attest → review → done`.

The repository does not contain an active universal constructor. The reference
worker explicitly substitutes a short sleep for construction. At audit time,
no process was running the gate, lease reaper, worker, reviewer, prediction
scorer or Paperclip bridge. The production database had not received an event
since 2026-08-03.

# Broken interfaces

## Tape to queue

`gate.py` validates a minimal tape when invoked. `uc.py submit`, however,
accepts work without a tape and `work.tape_id` is nullable. The gate is a
convention rather than a mandatory boundary.

## Prediction to execution

The SQL trigger requires a prediction before `review` or `done`. It cannot
require a prediction before execution because work has no authoritative
`started_at`. A test successfully wrote evidence before creating the
prediction and still reached `done`.

## Evidence to detachment

Evidence is stored as untyped event payloads. Any caller can attest any
criterion. The direct `done` command does not require complete evidence,
artifact identity, claim ownership, a distinct reviewer or a scored
prediction.

## Failure to retry

An untargeted worker claim selects only `pending` work. Failed work can be
reclaimed only by a targeted claim. The normal autonomous path therefore
cannot raise `attempts` to the DLQ threshold.

## Queue to constructor

`harness.py` wraps leases and transitions but does not dispatch a tape to a
real execution backend. The repository has tools and agent registries, not a
live adapter contract joining capability, workspace, tape, artifact and
evidence.

## Boot to runtime

The scheduled WSL wake task targets a nonexistent `Ubuntu` distribution while
the installed distribution is `Ubuntu-24.04`. The latter has no V3 systemd
units. The WSL guardian keeps the VM alive but does not start V3.

The external A0 script is not a replacement: it is outside the repository,
targets a V2 Coach OS path, runs for a bounded four or twelve hours, and does
not reference `uc.db`, the tape directory or V3 bridges.

# Split control plane

State is distributed across SQLite, Multica, Paperclip, Buzz, the external A0
runtime and a proposed WSL mission-control chain. There is no reconciliation
protocol or single terminal state.

Observed state on 2026-08-30:

- SQLite: 11 work items, last event 2026-08-03, two expired claims;
- Multica: 57 agents, all idle;
- Multica: 220 issues, last update 2026-08-12;
- Paperclip bridge: endpoint unreachable;
- AgentGateway and the corpus API: listening;
- V3 controller processes: none.

This distinction matters: infrastructure availability is not autonomous
agency.

# Minimal recovery architecture

Use `uc.db` as the sole authority until one closed loop works. A single
boot-managed supervisor should:

1. ingest complete tapes;
2. reap leases;
3. dispatch eligible work to one real constructor adapter;
4. invoke an independent reviewer;
5. score terminal predictions;
6. schedule retries or DLQ transitions;
7. create descendants only after verified success.

The schema should enforce mandatory tapes, explicit transitions, claim tokens,
prediction time before execution start, typed evidence, distinct reviewer
identity and terminal scoring.

The first vivance certificate is not a large roster. It is one cold-boot test
where a worker is killed, the lease expires, another worker completes the real
artifact, the reviewer detaches it, the prediction is scored and a descendant
passes a canary without operator input.

The detailed evidence, loophole reproductions, causal hierarchy and repair
order are in
[`40_Memory_Wiki_OKF/architecture/audit-vivance-aspace-v3-2026-08-30.md`](../../../40_Memory_Wiki_OKF/architecture/audit-vivance-aspace-v3-2026-08-30.md).
