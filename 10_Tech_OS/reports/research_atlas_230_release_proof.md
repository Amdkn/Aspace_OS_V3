# Research Atlas v1 — Multi-Source Convergence & Promotion Proof

**Issue:** #230 (Resolves Epic #221 and Objective #220)
**Date:** 2026-10-02
**Agent:** Jules

## Objective Completion
This proof certifies that the **Bill Research Atlas** is a functional, multi-source R&D system capable of detecting converging technological families toward primitives A'Space does not yet possess.

The implementation in `30_Business_OS/10_Research_Atlas/03_Emergence_Radar/radar.py` satisfies all acceptance criteria without requiring any new architectural rebuild.

## Golden Proof Verification

### 1. One Discover AI source path & 2. One independent historical/user source path
Tested and verified in `test_multi_source_ingestion_and_deduplication`. The system ingests both a `Discover AI` report and an `independent` user source.

### 3. Both converge on shared canonical Paper identity
`resolve_identities()` correctly deduplicates citations into shared canonical IDs (e.g., `arxiv:1234.5678`), appending multi-source evidence to a single `canonical_map` entry rather than duplicating identity.

### 4. WATCH S1 & 5. PAPER S1 paths supported
The radar explicitly supports `watch_s1` and `paper_s1` ingestion pipelines via `ingest_watch_s1()` and `ingest_paper_s1()`, representing extracted citations identically on the canonical graph.

### 6. last30days S0 tests whether the lineage is accelerating now
Implemented in `check_temporal_acceleration()`. It compares the `timestamp` of each source citation against the current date (a 30-day window) and assigns an `acceleration_score`. Verified in `test_temporal_acceleration_and_promotion`.

### 7. Sources cluster into an evidence-backed ResearchLineage
Implemented in `build_lineages()`. Multi-source entries are grouped into `ResearchLineage` dataclass instances based on canonical identity and combined acceleration scores.

### 8. Lineage maps against CapabilityAtoms and emits CapabilityGap or promoted candidate
Implemented in `map_capabilities()`. A lineage requires multi-source validation (e.g., Discover AI + independent) and an acceleration score $\ge 0.5$ to become a `PromotedCandidate`. Otherwise, it emits a `CapabilityGap`. Verified in `test_temporal_acceleration_and_promotion`.

### 9. Graham preserves provenance and Clara receives only promoted candidate
Implemented in `generate_report()`. The final output JSON correctly separates:
- `clara_payload`: Strictly containing the promoted candidates.
- `graham_payload`: Containing the full provenance (all lineages and gaps) for memory and tracking.

## Acceptance Criteria Check
- [x] **Repeated citation across independent sources is signal, not duplicate:** Validated. Deduplicated via `canonical_map`.
- [x] **Citation graph expansion remains bounded:** Validated. Deep deep-ingest is delegated; the radar only acts on bounded extraction evidence.
- [x] **Promoted claim traceable to source evidence:** Validated. Output tracks evidence count and lineage IDs.
- [x] **Discover AI can be removed without collapse:** Validated in `test_architecture_robust_without_discover_ai`. WATCH S1 + PAPER S1 + Independent triggers promotion perfectly.
- [x] **Answers the core objective question:** By mapping emerging, high-acceleration lineages and emitting CapabilityGaps/PromotedCandidates, the system successfully answers which families are converging toward missing primitives.

## Artifacts
- **Evidence Pack:** `10_Tech_OS/reports/research_atlas_230_evidence.json`
- **Implementation:** `30_Business_OS/10_Research_Atlas/03_Emergence_Radar/radar.py`
- **Tests:** `30_Business_OS/10_Research_Atlas/03_Emergence_Radar/test_radar.py`

**Conclusion:** PASS. Closing #230, #221, #220.
