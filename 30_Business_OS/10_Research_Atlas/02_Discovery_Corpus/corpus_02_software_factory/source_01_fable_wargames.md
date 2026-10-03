# Discovery Packet 01: Fable 5 Wargames / Unknowns

## SourceClaim
Wargames function as executable simulation primitives to discover known unknowns, unknown knowns, and unknown unknowns before deploying high-risk autonomous agent operations.

## Supporting evidence
- Local Fable Wargame Kit (`fable_wargame_kit_source.zip`) containing `SUCCESS.md` (8 criteria for executable wargames) and `LEDGER.md` (OMK-C execution trace).
- Wargame structure requires expected observation, failure mode, counter-move, fork trigger, and `RECON NEEDED` flags.
- Validated on OMK-C Phase 3 SaaS Auth runbook (8/8 V-checks passed, gated HITL UI moves flagged).

## Contradictions / limits
- Wargaming simulates and discovers risks but cannot execute production state changes on its own.
- Blind execution requires complete pre-conditions; unhandled ambient state changes break static wargame scripts without active holon judgment.

## A'Space adaptation candidate
- Institutionalize Wargame as a simulation harness (`wargame.py`, `test_wargame_protocol.py`) in Tech OS Kernel to test holon decision loops before production dispatch.

## Anti-pattern / risk
- Treating wargames as rigid sequential checklists that strip S3 holons of situational adaptation or turn holons into script-followers.

## Impacted holons
- **Bill (S3 Research):** Synthesizes wargame patterns into research briefs.
- **Clara (S3 Design):** Integrates wargame gates into capability specifications.
- **Ryan (S3 Build):** Implements wargame harnesses and test suits.
- **River (S3 Flow):** Executes wargames prior to live effect dispatch.

## Candidate contract/ADR
- `ADR-312-WARGAME-SIMULATION-PRIMITIVE`: Mandates 8-criteria wargame simulation for high-risk autonomous missions.

## Required test/canary
- `10_Tech_OS/kernel/test_wargame_protocol.py` validating 8-criteria parsing and execution gating.

## Confidence
High (0.95)

## Provenance refs
- `20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Wargames/Fable_Wargame_Kit/fable_wargame_kit_source.zip`
- `50_Distillation/domaines/templates/concept-fable-wargame-kit-8-criteria.md`
- `30_Business_OS/00_Architecture/CONSTITUTION/FRACTAL_HOLON_CONTRACT.md`
