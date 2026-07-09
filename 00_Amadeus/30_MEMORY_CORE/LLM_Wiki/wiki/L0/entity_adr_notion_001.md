---
name: adr-notion-001
type: ADR
namespace: NOTION
status: RATIFIED
date: 2026-05-26
level: L2
canon_path: 30_Business_OS/09_Blueprints/02-ADR/ADR-NOTION-001_back-office-solaris-template.md
workspace: Business Pulse ∞ AMADEUS
depends_on:
  - adr-fwk-022
  - adr-fs-001
blocks_on:
  - adr-symph-001
links:
  - entity_adr_fwk_022
  - entity_adr_fs_001
  - entity_amadeus
  - entity_picard_summers_verse
source: LLM_Wiki_A0
domain: L0 Tech_OS / Entity
tags: [#wiki #hygiene #backfill]
---

# ADR-NOTION-001 — Notion Back Office : Solaris Template

Premier ADR du namespace `NOTION`. Pose la structuration du workspace `Business Pulse ∞ AMADEUS` avec **Solaris** comme prototype canonique et **template clonable** vers les 5 autres projets Picard.

## Décisions clés (8)

1. D1 — Workspace unique (pas de multi-workspace)
2. D2 — Solaris = TEMPLATE_VERSION 1.0
3. D3 — Architecture 5 sections par projet (HQ, SOPs TVR, Hall Agents, Produits, Légal)
4. D4 — MASTER_SOP_DB schema immuable 14 propriétés
5. D5 — 8 portails domaines alignés PARA J01 Marvel/DC
6. D6 — Pipeline Airtable→Notion→ClickUp, bus Symphony
7. D7 — Cuisine (Notion) vs Salle (Next.js+Supabase) — client final ne voit jamais Notion
8. D8 — Template versioning pour clonage projets puis franchises

## Backlinks
- [[entity_adr_fwk_022]] — alignement Marvel/DC (parent)
- [[entity_adr_fs_001]] — junctions short-path (parent infra)
- ADR-SYMPH-001 (à venir, dépendance) — bus orchestration sync Notion↔Supabase

