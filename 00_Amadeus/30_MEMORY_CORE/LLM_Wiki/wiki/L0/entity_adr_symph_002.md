---
name: adr-symph-002
type: ADR
namespace: SYMPH
status: RATIFIED
date: 2026-05-26
level: L0
canon_path: 10_Tech_OS/12_Blueprints/02-ADR/ADR-SYMPH-002_symphony-variants-per-harness.md
extends: adr-symph-001
links:
  - entity_adr_symph_001
  - entity_adr_symph_003
  - entity_adr_heart_002
source: LLM_Wiki_A0
domain: L0 Tech_OS / Entity
tags: [#wiki #hygiene #backfill]
---

# ADR-SYMPH-002 — Variants Harness Symphony

Matrice 6 variants : 3 participants tick auto (`*_CLI`) + 3 consoles A0 (`*_IDE/_App/_Desktop`).

## Synthèse matrice

| Variant | Tick auto | Provider | Trust |
|---------|-----------|----------|-------|
| Claude_Code_CLI | ✓ | MiniMax | autonomy_scope |
| Codex_CLI | ✓ | OpenAI | autonomy_scope |
| Gemini_CLI | ✓ | Google | autonomy_scope |
| Antigravity_IDE | ✗ | Google | sandbox |
| Claude_Desktop_App | ✗ | Anthropic | sandbox |
| Codex_Desktop | ✗ | OpenAI | sandbox |

## Règle d'or
Seuls les `_CLI` participent au bus Symphony. Les autres sont des consoles A0 (lecture, génération assistée, jamais tick auto). Couvre le refus Anthropic d'autonomie unattended.

## Cas Marina (2026-05-25)
Quota Codex Desktop saturé en plein build Marina → confirmé : un crash console A0 **ne casse pas** Symphony (seuls les CLI sont participants tick).

## Complémentarité avec ADR-SYMPH-003
SYMPH-002 = **QUI** tick (quel harness, quelles permissions). SYMPH-003 = **COMMENT** le tick injecte les standards + écrit le pulse.log. Les deux sont complémentaires, pas redondants.

## Backlinks
- [[entity_adr_symph_001]] — bus parent
- [[entity_adr_symph_003]] — Agent OS = standards injection (le QUOI du tick, complémentaire du QUI)
- [[entity_adr_heart_002]] — gardes anti-panique

