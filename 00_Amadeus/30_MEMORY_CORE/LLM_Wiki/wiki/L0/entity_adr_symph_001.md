---
name: adr-symph-001
type: ADR
namespace: SYMPH
status: RATIFIED
date: 2026-05-26
level: L0
canon_path: 10_Tech_OS/12_Blueprints/02-ADR/ADR-SYMPH-001_symphony-replaces-n8n.md
amends:
  - shadow_l0_spec_md
deprecates:
  - n8n
links:
  - entity_adr_symph_002
  - entity_adr_symph_003
  - entity_adr_heart_002
  - entity_adr_notion_001
  - entity_rick
source: LLM_Wiki_A0
domain: L0 Tech_OS / Entity
tags: [#wiki #hygiene #backfill]
---

# ADR-SYMPH-001 — Symphony Bus L0

Premier ADR du namespace `SYMPH`. Ratifie ce que `Shadow_L0/SPEC.md` préfigurait : Symphony est le **bus unique** L0, N8N est legacy.

## Points clés (6)
1. N8N marqué LEGACY ; archivage `Legacy_N8N_Workflows_2026-05-26/` au prochain ménage
2. Symphony = pattern (no runtime). Tick ephemeral + files + Task Scheduler.
3. Tick cycle canonique : WAKE→PROBE→DECIDE→EXECUTE→OBSERVE→LEARN→SIGNAL→SLEEP
4. Inter-agent messaging via JSON files outbox/inbox (no WS/gRPC/Redis)
5. Fallback chain quota-aware par Doctor (13/12/11)
6. 6 variants harness (détails ADR-SYMPH-002) ; standards injection + observabilité = ADR-SYMPH-003

## Backlinks
- [[entity_adr_symph_002]] — matrice variants
- [[entity_adr_symph_003]] — Agent OS = standards injection + pulse.log schema
- [[entity_adr_heart_002]] — instrumentation anti-panique
- [[entity_adr_notion_001]] — premier consommateur du bus

