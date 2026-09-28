# HANDOVER — 2026-09-28 — Nardole DISPATCH / R&D AI-Native SDLC Mesh — Wave 1

## Mission identity
- mission_id: `MISSION-RND-AI-SDLC-2026-09-28-01`
- origin_intent: `7f653c67-3eb0-4615-8b2a-13edaf830c8c`
- supporting_intent: `bfa06dd2-6da1-4b12-9eed-ea3a4070131c`
- origin: A0 request + Bill/Ryan peer-session launchers + Fractal Mission Topology
- return_bus: GitHub Discussion #185 — A'Space Agent Capability Mesh
- topology: MESH / parallel + reentrant cells
- policy: capability != pipeline step; evidence closes cells

## Current routing map
| cell_id | capability | owner | mode | machine state | outcome |
|---|---|---|---|---|---|
| NAR-00 | DISPATCH | Nardole | reentrant | pending until durable binding exists | route cells, receipts, backpressure, reopen/recovery |
| GRA-01 | REMEMBER | Graham | parallel | READY | bounded recall + canonical ingestion-surface provenance |
| BIL-01 | DISCOVER | Bill | parallel/swarm | READY | sourced Discovery Packet for Software Factory / Multi-Agent Orchestration / AI-Native SDLC |
| CLA-01 | DESIGN | Clara | reentrant/mesh | READY | compile candidate topology/FactoryBlueprint from evidence without waiting for global research closure |
| RYA-01 | BUILD | Ryan | parallel | WAITING_CANONICAL_SURFACE | reuse existing transcript/WATCH/yt-dlp/ffmpeg primitives; build smallest replayable adapter |
| YAZ-01 | OBSERVE | Yaz | parallel | WAITING_EVIDENCE | Behavioral Digest + execution/recovery evidence over the ingestion path |

## Non-pipeline routes
- Graham <-> Bill: recall/provenance and source claims reinforce each other; neither waits for the other to finish globally.
- Graham + Bill -> Clara: Clara may consume partial stable packets and re-enter as new evidence arrives.
- Ryan runs in parallel on the bounded adapter surface; only the canonical ingestion-surface location is unresolved.
- Yaz attaches to Ryan/Bill execution evidence as soon as events exist; verification is not a terminal gate.
- All cells return receipts to Nardole + Discussion #185.
- Monitor/Learn may reopen the smallest affected cell without restarting the mission.
## CapabilityNeeds
### NEED-RND-01-GRAHAM-RECALL
Find the canonical WATCH/transcript-api/previous-ingestion surfaces and return exact paths/refs, prior evidence, known failures and reuse constraints. Blocking only for duplicate-code avoidance; not a global mission blocker.

### NEED-RND-02-BILL-DISCOVERY
Produce at least one sourced Discovery Packet: source metadata, transcript/paper/repo refs, claims, novelty, contradictions, questions and candidate implications. No implementation dispatch by Bill.

### NEED-RND-03-RYAN-BUILD
Continue from commit `2633185a`. Build only after locating/reusing the existing ingestion surface. Acceptance: replayable source URL entrypoint, deterministic metadata, transcript retrieval, optional keyframes, Discovery Packet output, evidence manifest, dry-run + fixture test, reversible commit.

### NEED-RND-04-CLARA-DESIGN
Consume partial stable evidence and compile the smallest FactoryBlueprint / mission pattern required. No fixed Bill -> Clara -> Ryan chain. Return accepted interface/acceptance deltas to Nardole and Ryan.

### NEED-RND-05-YAZ-OBSERVE
Define and collect trajectory evidence for ingest/replay/retry: inspect-before-edit, test-after-edit, temporary failure, recovery strategy, recovery success, repetition/backtrack, repository outcome. Return Behavioral Digest, not raw telemetry flood.

## Return contracts
Every return must contain: mission_id, cell_id, evidence refs, changed artifacts/commit if any, unresolved CapabilityNeeds, retry/reopen condition, next owner. Discussion #185 is the shared human-visible rendezvous; Supabase WorkGraph remains machine state.

## Dispatch / lease / backpressure law
- No `claimed` state without a real lease and fresh binding.
- No active binding is currently asserted for these ChatGPT peer sessions.
- One identity worktree owns its mutations; the dirty shared root is read-only for this mission.
- A new mutation cell waits if its target worktree/repo boundary is already dirty for unrelated work.
- Retry reuses the same cell/work identity; do not create a replacement ticket/session merely because one attempt failed.
- Two bounded deterministic retries maximum for a recoverable technical failure, then route a causal packet to Donna/RECOVER.
- Semantic/authority conflict escalates to the relevant Doctor only after local mesh resolution fails; Rick only for unresolved cross-Core/constitutional conflict.
## World routing
- Astra = A'Space V3 / design, contracts, shared mission evidence.
- Sol = Agent OS runtime/interface; Desktop 127.0.0.1:5555. If a mutation belongs to Sol, PR it in the Sol repo, not Astra.
- Terra = Life OS 2026 consumer world.
- Luna = Business / The OMK Office federation; member repos keep independent Git history.
- Junctions/symlinks are navigation only, never Git ownership.

## Evidence already recovered
- Discussion #185: existing Routing Board + Wave-1 convergence snapshot.
- PR #187 OPEN/MERGEABLE, head `30ff6202`: Council + fractal mission runtime; contracts exist in Agy worktree, not root main.
- PR #189 OPEN/MERGEABLE, head `682a5d2f`: Astra/Sol/Terra/Luna federation.
- Ryan Wave-0 commit `2633185a`: R&D ingestion discovery checkpoint; yt-dlp/ffmpeg present; canonical WATCH/transcript adapter still to locate.
- Supabase: no active claims; all 13 recorded bindings are completed; DLQ empty.
- Existing WorkGraph rows are historical waiting/governance-failed rows; none represents this new mission yet.
- No Bill mission handover was visible at this checkpoint.

## Known divergence
Root `ASPACE_WORKSPACE_REGISTRY.json` is still dated 2026-09-27 and carries the superseded Sol/Tera/Luna world naming. PR #189 contains the Astra/Sol/Terra/Luna correction. Do not mutate the dirty root to “fix” it from this lane.

## Next owners
1. Graham + Bill in parallel.
2. Ryan continues bounded canonical-surface discovery/build; not blocked on Bill global completion.
3. Clara re-enters on first stable packet/interface decision.
4. Yaz attaches to first executable/evidence-bearing run.
5. Nardole reconciles returns, opens/reopens only the smallest necessary cell, and routes recoverable failures to Donna.

## Next Nardole action
Publish this mission topology to Discussion #185, materialize non-claimed WorkGraph cells with the same mission/cell IDs, attach receipts/evidence, then remain the return-to owner.
