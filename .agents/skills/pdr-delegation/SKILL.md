---
name: pdr-delegation
description: Compile intent/issues into the smallest executable PDR and route it without mandatory document cascades.
---
# PDR Delegation
Required: PDR-ID; Origin; Category; Outcome; Specialist; repo/files boundary; dependencies; acceptance checks; evidence; rollback boundary; Jules-fit; Return-to.
Categories: BUILD | REPAIR | TEST | INTEGRATE | MIGRATE | AUDIT | BENCHMARK | CONTRACT.
If work is bounded/reversible, PDR is enough. Add ADR/PRD/TDD only when risk truly requires it.
If one outcome needs multiple phases/patterns/capabilities, compile a Mission Topology with `python scripts/council_mission.py`; its cells may each produce or consume bounded PDRs.
Never send a vague outcome to Jules.
