# Discovery Packet 04: AI-Native Full SDLC Workshop

## SourceClaim
An AI-native software development lifecycle integrates requirements discovery, architectural design, automated implementation, and continuous testing into unified feedback loops.

## Supporting evidence
- `30_Business_OS/09_Blueprints/agentic-os/transcriptions/05-cinq-couches.txt` (5-layer architecture plumbing: infrastructure, context, memory, routing, interface).
- End-to-end SDLC workflows spanning intent distillation to automated PR submission.

## Contradictions / limits
- SDLC workshops typically promote linear assembly lines, whereas complex holonic systems require recursive, non-linear delegation and lateral peer-to-peer alignment.

## A'Space adaptation candidate
- Structure the SDLC into explicit holon stewardship domains: Clara (Design/PRD), Ryan (Build/Code), River (Flow/Release), Yaz (Observe/Audit), and Graham (Memory/Knowledge).

## Anti-pattern / risk
- Forcing a rigid linear waterfall that prevents River from giving immediate flow feedback to Clara or Ryan during execution.

## Impacted holons
- **Clara (S3 Design):** Specs SDLC contracts.
- **Ryan (S3 Build):** Executes software build steps.
- **River (S3 Flow):** Orchestrates lifecycle transitions.
- **Graham (S3 Memory):** Persists domain artifacts across lifecycle phases.

## Candidate contract/ADR
- `ADR-312-HOLONIC-SDLC-ORCHESTRATION`: Governs non-linear SDLC transitions across Companion holons.

## Required test/canary
- `10_Tech_OS/kernel/test_uc_workgraph.py` verifying multi-phase workgraph execution.

## Confidence
High (0.90)

## Provenance refs
- `30_Business_OS/09_Blueprints/agentic-os/transcriptions/05-cinq-couches.txt`
- `30_Business_OS/00_Architecture/CONSTITUTION/FRACTAL_HOLON_CONTRACT.md`
