# KPRD-050: DecisionEvidence store + Engram exact-first bridge
## KER-42

**Context:** Before escalating to a learned System-1 model (like Morty MiniMind) for evaluation, the framework must store the execution evidence deterministically and attempt an exact-first lookup using the Engram Phrase Book.

**Requirements:**
1. Implement a `DecisionEvidence` store wrapper or logic that records the evidence reliably (no silent overwrite, preserve provenance).
2. Extend the `morty_engine.py` (or introduce a new bridge script) to perform an exact-first lookup using `EngramPhraseBook.resolve()` before executing the MiniMind fallback arbitration.
3. Tests must be included to prove the exact-first lookup handles deterministic cases without hitting the learned model, and that evidence is stored correctly.
4. Integrate this smoothly into the existing `morty_engine.py` arbitration flow or `uc.py` as appropriate.
5. Create an AUTO_CREATE_PR for the review. Do not expand scope.
