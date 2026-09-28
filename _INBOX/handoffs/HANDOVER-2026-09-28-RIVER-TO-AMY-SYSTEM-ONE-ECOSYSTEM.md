# HANDOVER — 2026-09-28 — RIVER → AMY / BILL / CLARA — SYSTEM-ONE ECOSYSTEM CORRECTION

## Origin / continuity
- Active IPBD: `16c4a90f-5934-4843-9e24-484f57d617e2`.
- Existing R&D issue: GitHub `#125 [BRD-003][BILL] Evidence-Preserving Reducer with local SLM`, which already says to evaluate Needle/Laya.
- River canary historical provenance: `Amdkn/River@3c21acda`.
- Main fractal-mesh provenance: `origin/main@11880d10` / PR #186.
- Reconciled River commit: `16253806918cbd1e30427d49dd033293b2205116`, built directly on `main@11880d10` with the six exact River blobs preserved.
- Rollback branch: `backup/River-pre-reconcile-20260928` -> prior head `416f813683179a86b874cd56b24521caba5a2724`.
- `HANDOVER-2026-09-28-NINE-PARALLEL-COMPANIONS.md` supersedes the six-session handover and transfers Jev platform/interface stewardship from River to Amy.

## Verifiable result of this correction cell
Machine-readable evidence:
`10_Tech_OS/kernel/evidence/system_one_ecosystem_scan_20260928.json`.

The prior River benchmark proved the typed contract but under-scanned the ecosystem. Corrected taxonomy:

### MODEL / decision-engine peers
Jev, Laya, Kev, CLM, GLiNER2.5-Decide, Tev1, Decider, NanoJev and Jev-Omni are current decision-engine/model candidates to classify. They are not equally mature and do not all cover the same primitives.

### RUNTIME / serving fabric
Decis is not a model. It is a self-hosted multi-engine server that can expose engines such as Laya/Kev behind a Jev-compatible `/v1/systemone` contract.

### SDK / schema / integration
- System One Connector: MCP/provider connector for typed evaluation.
- `zod-jev`: integration layer. Zod validates structural shape; Jev supplies probabilistic semantic judgment. It is not a replacement model.

### USE-CASE / benchmark
- `laya-needle`: Needle-derived RAG passage filtering with Laya replacing hosted Jev.
- Needle/Needle3 should be treated as consumer/experimental reconstruction evidence unless a concrete peer model implementation is identified.

## Design correction
Do not encode provider identity into `HostPolicy`.
Amy's interface should depend on a provider-neutral contract:
`state + typed questions -> typed answers/probabilities + provenance`.

Deterministic host policy retains thresholds, authority and all side effects.

## Benchmark contract to carry forward
For true model/provider candidates, use the same BehavioralDigest + Choice/Score/Noul fixtures and measure:
- final action accuracy;
- Noul Brier;
- Score MAE;
- calibration/ECE;
- p50/p95 latency;
- memory/runtime cost;
- primitive coverage;
- `/v1/systemone` compatibility;
- option-order stability;
- offline/self-host capability.

Needle and Zod belong in integration/use-case tests, not the model leaderboard.

## CapabilityNeeds / exact next owners
### BILL / RESEARCH
Continue existing GitHub #125; expand Needle/Laya discovery into a source-backed System-One provider matrix. Do not create a duplicate issue.

### AMY / INTERFACE
Adopt River's proven canary as provenance, then define the stable provider-neutral interface and at least Jev + one open/local adapter candidate.

### CLARA / DESIGN-FORGE
Compile acceptance/construction rules for provider interchangeability, fail-closed escalation and evidence return.

### RYAN / BUILD
Implement only after Amy/Clara bound the interface. Reuse the same benchmark harness.

### RIVER / FLOW
Consume the resulting interface. River no longer owns Jev platform/interface design.

## Authority / evidence
- No hosted Jev/Laya/Kev call was made in this correction cell.
- External benchmark/latency figures remain source claims until replayed inside A'Space.
- No irreversible side effect may ever be granted solely by model confidence.
- River branch reconciliation is complete; no branch divergence blocker remains.

## Next action
Amy/Bill/Clara resume from this handover + GitHub #125 + reconciled River branch without asking A0 to rebuild the ecosystem.
