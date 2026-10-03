# Discovery Packet 08: Super Simple Software Factory / Agents + Code

## SourceClaim
Minimalistic agentic software factories succeed by combining simple code scripts with small, highly-specialized agent prompts rather than monolithic frameworks.

## Supporting evidence
- `30_Business_OS/09_Blueprints/agentic-os/transcriptions/02-graphify.txt` (Lightweight knowledge graphs speeding up code execution).
- `10_Tech_OS/kernel/uc.py` (Simple, modular micro-agent executions in A'Space Kernel).

## Contradictions / limits
- Overly simplistic script-agent combinations fail when complex cross-domain dependencies require structured state management and formal contracts.

## A'Space adaptation candidate
- Maintain lightweight, modular runtime scripts (`uc.py`, `harness.py`) that S3 holons invoke as instruments rather than heavy, opaque frameworks.

## Anti-pattern / risk
- Substituting simplistic scripts for rich holon cognition, leading to brittle task execution when unexpected errors occur.

## Impacted holons
- **Ryan (S3 Build):** Crafts simple, reusable script instruments.
- **Nardole (S3 Dispatch):** Routes tasks efficiently through minimal execution paths.

## Candidate contract/ADR
- `ADR-312-MODULAR-INSTRUMENT-DESIGN`: Mandates simple, single-responsibility code instruments for holon usage.

## Required test/canary
- `10_Tech_OS/kernel/test_uc_workgraph.py` verifying lightweight modular task execution.

## Confidence
High (0.93)

## Provenance refs
- `30_Business_OS/09_Blueprints/agentic-os/transcriptions/02-graphify.txt`
- `10_Tech_OS/kernel/uc.py`
