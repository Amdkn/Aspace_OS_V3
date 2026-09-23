---
type: Architecture Concept
title: Truthful dispatch ownership and zero-work supervisor
description: Deterministic ownership gates before Jules dispatch and Linear projection.
tags: [workgraph, orchestration, ownership, convergence]
generated: { by: "agent:codex-work", at: "2026-09-23T11:08:00Z" }
verified: []
sources:
  - id: work-181-evidence
    resource: "10_Tech_OS/reports/convergence_181_evidence.json"
    title: "20 focused tests and real supervisor preflight"
    last_modified: 2026-09-23
okf_version: "0.2"
---

# Ownership before projection

A Linear issue resolves to exactly one canonical WorkGraph work_id. Dispatch requires
an eligible pending item, satisfied dependencies, no live owner or open binding, then
an atomic claim via uc.py. A durable attempt precedes the network request; ambiguity
must be reconciled before retry. Session creation alone never proves execution:
In Progress requires an unexpired matching claim, an active binding and a fresh
IN_PROGRESS observation from the same provider session.

Occupied companion lanes cannot receive unrelated work. An empty Jules supervisor
cycle reads WorkGraph locally and exits before Orca or an LLM is invoked.

Machine evidence: 20 focused tests pass, including competing claims, expired leases,
wrong/queued sessions and closed bindings. Live empty supervisor cycle skipped.
Independent review pending at authoring; this does not certify full Kernel autonomy.

Final delta: an OS file lock serializes fleet ticks across processes. Final focused suite: 21/21 PASS; evidence v2 supersedes the initial 20-test snapshot.


Closure verification 2026-09-23: Hermes independent review PASS, all four reviewed file hashes unchanged, focused suite rerun 21/21 PASS. See convergence_181_acceptance.json. No full Kernel autonomy claim.
