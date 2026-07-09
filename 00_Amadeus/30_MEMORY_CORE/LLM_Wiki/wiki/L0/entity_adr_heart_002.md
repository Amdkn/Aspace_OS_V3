---
name: adr-heart-002
type: ADR
namespace: HEART
status: RATIFIED
date: 2026-05-26
level: L0
canon_path: 10_Tech_OS/12_Blueprints/02-ADR/ADR-HEART-002_heartbeat-anti-panique-openclaw-paperclip.md
anchors:
  - sdd-001
  - shadow_l0_heartbeat_protocol_md
amends:
  - shadow_l0_spec_md
links:
  - entity_adr_symph_001
  - entity_adr_symph_002
  - entity_openharness
  - entity_rick
source: LLM_Wiki_A0
domain: L0 Tech_OS / Entity
tags: [#wiki #hygiene #backfill]
---

# ADR-HEART-002 — Heartbeat Anti-Panique + Réintroduction Gated OpenClaw/Paperclip

Mappe les 8 paniques SDD-001 (4 Framework + 4 Kernel) sur les 8 phases du tick cycle Symphony. Amende `Shadow_L0/SPEC.md` qui interdisait nu OpenClaw/Paperclip — désormais autorisés **sous conditions strictes**.

## 7 décisions

1. **D1** — Matrice gardes anti-panique par phase tick (WAKE adresse Type 1, EXECUTE adresse K1/K2…)
2. **D2** — Read-After-Write systémique pour tout write critique (`Write-AndVerify` helper)
3. **D3** — OpenClaw gated par 4 conditions C1-C4 (DM timeout, health, Donna DLQ, heartbeat)
4. **D4** — Paperclip gated par 4 conditions P1-P4 (AGENTS.md, budget, mémoire procédurale, Donna)
5. **D5** — 3 modes mesh : `lean` (défaut) / `bridged` (OpenClaw ON) / `full` (les deux)
6. **D6** — Donna DLQ refondue file-based (pas WS) — anti-Type 4
7. **D7** — Watchdog Yaz sweep 5min always (vérifie ticks, donna_dlq, conditions modes)

## Mode initial
**lean** — OpenClaw + Paperclip OFF. Pas d'escalade avant Phase 1 Notion Solaris verrouillée.

## Backlinks
- [[entity_adr_symph_001]] — bus parent
- [[entity_openharness]] — Rick A1 incarnation (compatible mode lean)

