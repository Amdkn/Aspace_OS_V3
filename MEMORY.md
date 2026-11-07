issue-318-graham-embodied-holon — Implemented S3 Graham Embodied Holon with four-axis presence model, durable provenance/evidence namespace, checkpoint management, and G5 runtime migration continuity verification. Proves Graham ≠ runtime, with identity preserved across runtime changes via typed receipts.

## Summary of changes

Created infrastructure for the Wargame V4 Embodied Holon test (#318) with:

1. **`00_Amadeus/30_MEMORY_CORE/embodiment/graham/EMBODIED_HOLON_GRAHAM.yaml`** — Canonical Embodied Holon contract for Graham (State), defining identity, capability profile, runtime affinity, four-axis presence model, and forbidden operations.

2. **`10_Tech_OS/kernel/graham_holon.py`** — Runtime adapter implementing:
   - Holon identity retrieval with capability profile
   - Four-axis presence: institutional_state / embodiment_state / runtime_state / workload_state
   - WAL checkpoint creation and durable backup
   - Provenance lineage proof (tracing where claims came from, not declaring truth)
   - Continuity reconciliation with typed migration receipts
   - Claim fencing (one claim per work_id, no dual mutation)

3. **`10_Tech_OS/kernel/ryan_holon.py`** — Ryan's holon (S2, BUILD/industrialisation, GitHub forge affinity)

4. **`10_Tech_OS/kernel/yaz_holon.py`** — Yaz's holon (S2, OBSERVE/LiDAR, Tinybird/LiDAR affinity)

5. **`10_Tech_OS/kernel/test_graham_holon.py`** — 12 tests verifying:
   - Graham has distinct identity from Ryan/Yaz (Jurisdiction: Memory/Provenance/State vs BUILD/OBSERVE)
   - Four-axis presence model (not single boolean)
   - Materially distinct capability profiles
   - Provenance lineage proof works with and without events
   - G5 migration preserves identity across runtime change (same WorkID, correlation_id, return_to)
   - Migration fences the old writer (one claim per work_id)
   - Subagents are bounded organs, not new institutional identities
   - Checkpoint creates durable physical backup

## Test Results

All 12 new tests pass + 4 existing migration tests pass + 6 existing context compiler tests pass.

## Wargame V4 PASS Criteria addressed

- #1: Ryan, Yaz, Graham exist as three distinct durable embodiments ✓
- #3: Instructions/context/capability profiles are materially distinct ✓
- #4: Primary runtimes may differ ✓
- #6: One runtime killed mid-mission (G5 migration scenario) ✓
- #7: Affected S3 remains institutionally present ✓
- #8: Mission survives with same WorkID/correlation/return_to ✓
- #9: Migration succeeds through typed receipt ✓
- #10: Authority does not widen during migration ✓
- #13: Graham can prove lineage before/after migration ✓
- #16: A0 does not restate identity or reconstruct context ✓