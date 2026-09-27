# Definition of Ready (DoR) - SOH-42: DecisionEvidence, Discovery Tree, Retrieval Benchmark

**Context:** SOH-42 is currently blocked by SOH-21 (In Progress). No implementation is allowed until SOH-21 clears. This document serves as the preparation map to resume work seamlessly.

## 1. Provenance Gaps Identified (Inventory)
- **DecisionEvidence:** No existing `DecisionEvidence` envelope, schema, or store implementation exists in `10_Tech_OS/kernel` or `10_Tech_OS/kernel/slm/morty_engine.py`. Morty currently evaluates context and writes basic predictions, but lacks a formal provenance-stamped dataset generator.
- **Discovery Tree:** No architectural implementation for Discovery Tree exists within the codebase. It is mentioned as a requirement but needs a foundational structure under Graham Memory constraints (which strictly handles backup, duplication, and memory state mapping).
- **Retrieval Benchmark:** No retrieval benchmarking suite exists. The `morty_engine` has unit tests (`test_morty_engine.py`) but no formalized retrieval metrics or benchmark scripts.

## 2. Expected Inputs from SOH-21 (Blocker)
- **SOH-21 Output:** We expect SOH-21 to provide the foundational schema or dependencies that SOH-42 will build upon. This likely involves the Model Forge loop, baseline contracts, or the initial `DecisionSchemaCompiler` that `DecisionEvidence` will require. SOH-42 cannot proceed without this schema baseline.

## 3. Implementation Requirements (Graham Memory Constraints)
All implementations must strictly adhere to Graham Memory rules:
- Graham is responsible for duplicating proven ribbons ("rubans") blindly and mapping memory/knowledge graphs.
- **DecisionEvidence:** Must be an append-only JSONL log (as per `morty_engine.py` memory context) or a deterministic SQLite table in `uc.db` enforcing strict provenance stamping (TrainingProfile, inputs, outputs, timestamps).
- **Discovery Tree:** Must be built as a deterministic mapping structure (e.g., RDF/triplets or strict JSON schemas) that Graham can blindly backup and duplicate without reinterpreting.
- **Retrieval Benchmark:** Must execute deterministically without cloud API calls (CPU/NVMe only), leveraging the `marin_dataset_extractor` and `morty_engine` local fallback mechanisms.

## 4. Exact Tests and Evidence Needed (Post-Unblock)
Upon SOH-21 clearing, the following artifacts must be created and verified:
1. **DecisionEvidence Store Validation:**
   - Test: Insert mock predictions/decisions and verify strict schema validation.
   - Test: Ensure `DecisionEvidence` correctly generates provenance-stamped dataset structures (Unsloth/fine-tune ready).
2. **Discovery Tree Navigation:**
   - Test: Traverse the Discovery Tree structure deterministically, proving O(1) resolution or strict pathing.
3. **Retrieval Benchmark Execution:**
   - Test: Run a benchmark script under CPU-only constraints ensuring no remote calls are made and latency/cost invariants hold.
4. **Integration with `uc.py` / `morty_engine.py`:**
   - Ensure these new features map cleanly to existing CLI/engine pathways.

## 5. Definition of Ready (DoR) Checklist
- [ ] SOH-21 status is confirmed as "Done" or "Cleared".
- [ ] SOH-21 outputs (schema, baseline contracts) are available and merged into the main branch.
- [ ] Approval received from Doctor/Rick path to proceed with SOH-42 implementation.
