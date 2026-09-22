# KPRD-020: Integrate Needle 3 capability adapter

## Scope
Integrate installed Cactus Needle 3 into IntelligenceRouter as native local capability interfaces. Prefer EXTRACT/ACT/EMBED and only expose DECIDE if evidence justifies it. Preserve fail-closed authority boundary. Add tests and runtime discovery.

## Owner
Rory

## Dependencies
Installed Cactus Needle 3 package.
IntelligenceRouter module in 10_Tech_OS/kernel/intelligence/intelligence_router.py

## Acceptance
- IntelligenceRouter supports EXTRACT, ACT, EMBED using Needle 3.
- DECIDE capability is fail-closed, meaning it is only exposed if explicit evidence (via the EvidenceLog) justifies it.
- Tests confirm these capability endpoints and authority boundary.
- No modifications to other layers or bounds.

## Evidence
Tests running and passing.
