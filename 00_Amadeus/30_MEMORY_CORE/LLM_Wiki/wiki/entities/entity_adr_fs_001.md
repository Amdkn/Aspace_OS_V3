---
name: adr-fs-001
type: ADR
namespace: FS
status: RATIFIED
date: 2026-05-22
level: L0
canon_path: 10_Tech_OS/12_Blueprints/02-ADR/ADR-FS-001_junction-based-aliasing.md
links:
  - entity_adr_fwk_021
  - entity_amadeus
source: LLM_Wiki_A0
domain: L0 Tech_OS / Entity
tags: [#wiki #hygiene #backfill]
---

# ADR-FS-001 — Junction-Based Aliasing for Short-Path Agent Operability

Première décision du namespace `FS` (Filesystem). Établit que :

1. PARA/Enterprise est **Source de Vérité** unique pour Projects/Areas/Resources/Archives
2. Business OS expose ces données via **NTFS Junctions** (jamais copies)
3. Trois couches d'aliasing : sentinelles racine `_\`, drives subst (`B:`, `P:`), junctions sectorielles
4. Interdictions : `robocopy /MIR` 2-way, `mklink /D` non justifié, junction vers `node_modules`

Audit initial : 4 junctions existantes, 1 corrigée (`alykaly-front` self-ref → PARA Next.js réel).

## Backlinks
- [[entity_adr_fwk_021]] — parent doctrinal (canon Blueprints)
- [[entity_rick]] — owner L0

