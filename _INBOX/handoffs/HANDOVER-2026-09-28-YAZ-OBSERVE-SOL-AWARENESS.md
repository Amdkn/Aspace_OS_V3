# HANDOVER — 2026-09-28 — YAZ / OBSERVE / SOL AGENT OS AWARENESS

## Resume contract

This handover continues the canonical nine-Companion mesh from:
- main commit `11880d10f68c64ac1ea5684bb142aa7e8b8ea362` / PR #186;
- `_INBOX/handoffs/HANDOVER-2026-09-28-NINE-PARALLEL-COMPANIONS.md`;
- GitHub Routing Board Discussion #185;
- IPBD intent `992e0f8f-cae3-4dd0-9bf4-ebc8887bc2f5` for LiDAR-style agentic proprioception.

Do not restart the LiDAR audit and do not redesign the nine-lane mesh.

## Current Yaz mission

Yaz is **OBSERVE**, a shared capability service for every Core and every Companion.

Yaz is not:
- the builder of defects it detects;
- the durable state owner;
- the Jev policy owner;
- a gatekeeper that blocks unrelated execution;
- a model-fingerprinting oracle.

Yaz is the nervous-system sensor that turns runtime trajectories into bounded evidence.

## Sol awareness correction

Current semantic world naming is:
- **Astra** — canonical A'Space OS V3 world / versioned system.
- **Sol** — Agent OS awareness and runtime world, including the desktop on `127.0.0.1:5555`.
- **Terra** — Life OS 2026 world.
- **Luna** — Business OS federation world.

Physical layout remains explicit:
- Astra repo: `C:/Users/amado/ASpace_OS_V3`.
- Agent OS parent: `C:/Users/amado/agent-os`.
- Astra navigation junction: `C:/Users/amado/ASpace_OS_V3/Agent_OS -> C:/Users/amado/agent-os`.

The junction is navigation, not Git ownership.

For backward compatibility, the old `worlds.Sol/Tera/Luna` keys remain readable. New readers must prefer `world_semantics.canonical`.

## Yaz responsibility stack

### SENSE
Observe native events from Codex, Antigravity, Claude Code, Hermes Agent, DeepSeek, Jules and other runtimes only when their native traces are actually observable.

Also observe Sol / Agent OS runtime surfaces where telemetry exists.

### NORMALIZE
Convert harness-specific events to a bounded semantic vocabulary without erasing:
- model identity/version;
- provider;
- harness/version;
- system-prompt fingerprint/version;
- reflex-policy version;
- tool-surface version.

### DIGEST
Expose a compact versioned Behavioral Digest, beginning with:
- `verified_after_final_edit`
- `inspect_before_edit`
- `test_after_edit_ratio`
- `temporary_failure_detected`
- `recovery_strategy_changed`
- `recovery_success`
- `spec_over_stale_test`
- `backtrack_rate`
- `repetition_rate`
- `unique_transition_fraction`
- `failed_execution_rate`
- `repository_outcome_ok`
- `trajectory_variance`
- `behavioral_drift_score`

Unknown/unobservable remains `null`, never fabricated `false`.

### BASELINE
Before attributing behavioral drift:
1. build same-harness rolling baselines;
2. compare policy-equivalent trajectories;
3. keep cross-harness distance separate from model substitution claims;
4. attribute prompt/tool/reflex-policy changes before escalating an identity anomaly.

### PROJECT
- Tinybird = disposable/reconstructible observability analytics.
- Graham/Supabase = durable evidence/replay state.
- Agent OS / Sol = human-visible awareness/runtime projection.
- GitHub = versioned adapter/contracts/evidence references.

## Collaboration routing

Yaz -> Ryan:
- build/runtime defect with reproducible trace;
- acceptance = patch/test evidence returned to originating Issue.

Yaz -> Graham:
- durable Evidence Packet;
- replay/idempotence need;
- acceptance = evidence/event IDs + replay query, no schema expansion by default.

Yaz -> Amy:
- Jev calibration/interface need;
- acceptance = typed observable interface, host policy still owns authority.

Yaz -> Clara:
- observability contract requires a new reusable capability/interface design.

Yaz -> Nardole:
- dependency, backpressure, return-to, ownership ambiguity after the observation is already bounded.

Yaz -> Bill:
- external research is required to interpret a novel signal.

Yaz -> Rory/River:
- project Life/GWS flow observability without taking over persistence or effects.

Rick is only for genuine cross-Core constitutional conflict.

## GitHub bus

Use Discussion #185 while the need is ambiguous.

When executable, use an Issue:
- label `handoff`;
- label `needs:<specialist>`;
- include ORIGIN / NEED / INPUTS / ACCEPTANCE / BOUNDARY / BLOCKING / RETURN TO;
- return evidence to the requester rather than making A0 the message bus.

## Wave-1 evidence

Wave-1 produced a Behavioral Digest/LiDAR canary with 5/5 tests and real Codex <-> Hermes cross-harness evidence.

Expected local evidence refs:
- `10_Tech_OS/observability/lidar/lidar_observability.py`
- `10_Tech_OS/observability/lidar/test_lidar_observability.py`
- `10_Tech_OS/observability/lidar/contracts/behavioral_digest.v1.schema.json`
- `10_Tech_OS/reports/yaz_lidar_cross_harness_20260928.json`
- `10_Tech_OS/reports/yaz_lidar_tinybird_20260928.ndjson`

These local artifacts must be reconciled into the Yaz identity worktree before code publication. Do not recreate them from memory if the local files are accessible.

## Next verifiable capability

1. Preserve/reconcile Wave-1 artifacts into `Amdkn/Yaz`.
2. Graham persists the Wave-1 Evidence Packet using existing evidence/event JSON surfaces.
3. Build same-harness rolling baselines.
4. Only then add Antigravity / Claude / Jules adapters from physically observed native trace formats.
5. Project the compact digest into Sol / Agent OS awareness and Tinybird analytics.
6. Produce a new handover with commit/PR/evidence refs.

## Boundary

No 958-field dump.
No new Supabase schema without evidence.
No silent world renaming that breaks legacy readers.
No model-substitution claim from behavioral distance alone.
No A0-mediated handoff when GitHub routing can carry it.
