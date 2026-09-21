# FPRD-001 FOR-4

Brief: Build the deterministic Linear mandate to PRD compiler `prd_compiler.py` in 10_Tech_OS/kernel/.

Requirements:
- Parses raw Linear mandate texts into structured, bounded Markdown PRDs.
- Must extract or default: Scope, Owner, Dependencies, Acceptance, Evidence, Exclusive Files.
- Explicit assignment: Clara as Primary Spec, Rick as Gatekeeper (no LLMs).
- Output must conform exactly to these markdown sections.
- Unit tests needed (`test_prd_compiler.py`) demonstrating valid mapping.

Do not alter authority contracts or unrelated domains.
