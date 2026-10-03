# Discovery Packet 02: Best AI Coding Configuration / Autonomy Levels

## SourceClaim
Optimal agentic coding performance requires decoupling model capabilities into explicit autonomy levels with distinct tool access, jurisdiction bounds, and approval gates.

## Supporting evidence
- `30_Business_OS/09_Blueprints/agentic-os/transcriptions/03-fable5-agentic-os.txt` (Fable 5 5-level agentic OS taxonomy).
- Multi-tier agent configurations allowing autonomous read/recon while gating state modifications behind explicit policy rules.

## Contradictions / limits
- Pure autonomy level frameworks often mistake hierarchy level (S1 vs S3) for capability level or intelligence level, leading to dumbing down S3 workers.

## A'Space adaptation candidate
- Map autonomy levels to jurisdiction scopes (S1 local file read/edit vs S2 component refactor vs S3 system architecture), maintaining full cognitive completeness at all levels.

## Anti-pattern / risk
- Assigning low-tier models to S3 roles and treating them as "dumb workers", violating #311 Fractal Holon Constitution.

## Impacted holons
- **Ryan (S3 Build):** Configures autonomy bounds for build harnesses.
- **Yaz (S3 Observe):** Monitors drift across execution levels.
- **Rory (S3 Interface):** Renders autonomy boundaries in user dashboards.

## Candidate contract/ADR
- `ADR-312-AUTONOMY-JURISDICTION-MAPPING`: Defines cognitive completeness across variable autonomy bounds.

## Required test/canary
- `10_Tech_OS/kernel/test_mission_continuity.py` testing bounded mission execution without loss of holon identity.

## Confidence
High (0.90)

## Provenance refs
- `30_Business_OS/09_Blueprints/agentic-os/transcriptions/03-fable5-agentic-os.txt`
- `30_Business_OS/00_Architecture/CONSTITUTION/FRACTAL_HOLON_CONTRACT.md`
