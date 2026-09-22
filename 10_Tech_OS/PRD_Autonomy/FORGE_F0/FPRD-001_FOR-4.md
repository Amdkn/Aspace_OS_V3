# FPRD-001: Linear mandate → bounded PRD compiler

**Issue:** FOR-4
**Title:** Implement `prd_compiler.py` for deterministic PRD generation

## Scope
Develop a Python script `10_Tech_OS/kernel/prd_compiler.py` that reads a raw "Linear mandate" text file and deterministically generates a bounded Markdown PRD.

The script must extract or deduce the following sections from the raw text:
- **Scope:** The main objective.
- **Owner:** Assign ownership.
- **Dependencies:** Any dependencies mentioned or inferred.
- **Acceptance:** Acceptance criteria for the PRD.
- **Evidence:** How the implementation will be verified.
- **Exclusive Files:** The files this feature is allowed to touch.

If Owner/Gatekeeper are not specified, automatically assign:
- Primary Spec: Clara
- Mechanism Gatekeeper: Rick

The output must be a well-structured Markdown file.

## Requirements
- Python 3.
- No LLM dependency (deterministic regex/parsing only).
- Output must strictly follow the required headers.
- Input is plain text or basic Markdown.
- Must include a CLI interface (e.g., `python3 prd_compiler.py --input raw.md --output prd.md`).

## Test Evidence
- Provide a unit test file `10_Tech_OS/kernel/test_prd_compiler.py` that verifies the parsing logic and default assignments.
