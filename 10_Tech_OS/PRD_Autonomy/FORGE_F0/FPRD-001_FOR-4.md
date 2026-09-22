# FPRD-001: Linear Mandate Compiler

Compile a raw text mandate (from Linear) into a bounded, markdown-formatted Product Requirements Document (PRD).

**Scope:**
Build `10_Tech_OS/kernel/prd_compiler.py` and its test `10_Tech_OS/kernel/test_prd_compiler.py`.
The script should read a plain text mandate from standard input (or a file) and output a Markdown string containing standard headers: Scope, Owner, Dependencies, Acceptance, Evidence, Exclusive Files.

**Owner:** Clara Spec (Primary), Rick (Gatekeeper)

**Dependencies:** Standard library only (no LLM).

**Acceptance:**
1. A function or CLI that accepts a raw string and outputs a structured Markdown PRD.
2. The output MUST contain the literal headers: `## Scope`, `## Owner`, `## Dependencies`, `## Acceptance`, `## Evidence`, `## Exclusive Files`.
3. If the owner is missing in the raw text, it defaults to: `Clara (Primary Spec) / Rick (Gatekeeper)`.
4. It must not use LLMs or external APIs (pure regex/string parsing is fine, as long as it handles a simple unstructured or semi-structured block).

**Evidence:**
A test suite `10_Tech_OS/kernel/test_prd_compiler.py` demonstrating deterministic mapping.

**Exclusive Files:**
- `10_Tech_OS/kernel/prd_compiler.py`
- `10_Tech_OS/kernel/test_prd_compiler.py`
