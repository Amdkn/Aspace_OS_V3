# FPRD-001 : [F0] Linear mandate → bounded PRD compiler

**Goal:** Create a deterministic script (`10_Tech_OS/kernel/prd_compiler.py`) to parse raw Linear mandate texts into structured, bounded Markdown PRDs without relying on LLMs.

**Scope:**
- Implement `prd_compiler.py` in `10_Tech_OS/kernel/`.
- Parse sections: Scope, Dependencies, Acceptance, Evidence, Exclusive Files.
- Hardcode Owner assignment: Primary Spec = Clara, Gatekeeper = Rick.
- Provide a unit test suite (`10_Tech_OS/kernel/test_prd_compiler.py`) ensuring owners are correct and sections are parsed.

**Dependencies:**
- Python standard library only (no external packages).

**Acceptance:**
- `prd_compiler.py` runs and outputs Markdown conforming to the bounded PRD structure.
- `test_prd_compiler.py` passes all tests.

**Evidence:**
- Test execution logs.

**Exclusive Files:**
- `10_Tech_OS/kernel/prd_compiler.py`
- `10_Tech_OS/kernel/test_prd_compiler.py`
