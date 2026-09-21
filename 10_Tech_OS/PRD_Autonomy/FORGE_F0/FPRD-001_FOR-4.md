# FPRD-001: Linear Mandate -> Bounded PRD Compiler

## Context
We need a deterministic compiler (`10_Tech_OS/kernel/prd_compiler.py`) to parse raw Linear mandate texts into structured, bounded Markdown PRDs.

## Requirements
* Parse raw Linear mandate texts (e.g. Markdown or plain text containing sections).
* Enforce the inclusion of specific sections: Scope, Owner, Dependencies, Acceptance, Evidence, and Exclusive Files.
* Automatically assign "Clara" as Primary Spec and "Rick" as Gatekeeper without relying on LLMs.
* Output should be a structured Markdown file.
* Create a test file `10_Tech_OS/kernel/test_prd_compiler.py` to ensure it works correctly.

## Instructions
1. Create `10_Tech_OS/kernel/prd_compiler.py` with the compiler logic.
2. Create `10_Tech_OS/kernel/test_prd_compiler.py` for unit tests.
3. Ensure it runs via pytest.
