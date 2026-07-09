---
id: ADR-MEM-001
title: Memory Fabric Unified Doctrine — A'Space OS Multi-Layer Memory Architecture
type: ADR (Architectural Decision Record)
status: PROPOSED (A0 sign-off 2026-06-15 via "go for all", à valider scope Templates mission 4)
date: 2026-06-15
author: A0 (Amadeus) via A2 (Claude Code) sub-agent
domain: L1 Life_OS / Memory / Architecture / Doctrine
tags: [#ADR #memory #fabric #unified #canonique #persistent #wiki #claude-md]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-META-003, ADR-OBSERVABILITY-001]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, "Doctrine no-hard-delete"]
provenance: |
  Née 2026-06-15 de l'analyse mission 4 (PARA Geordi 02_Templates) : template Tilly
  `02_memory_fabric_unified` détecté. Doctrine à formaliser : 5 couches mémoire A'Space
  (CLAUDE.md injection, AGENTS.md canon, MEMORY.md index, wiki canon, ADR doctrinaux) avec
  ownership, TTL, et pattern retrieval explicites. ATTENTION D4 : ne pas confondre avec
  ADR-MEM-001 historique (IndexedDB Cloisonnement LD01-LD08) - celui-ci est nouveau, sister
  scope "Memory Fabric" pas "Memory IndexedDB".
sign_off_a0: "A0 Amadeus — Go ADR-MEM-001 — 2026-06-15 (via 'go for all' session-level directive, scope à valider)"
sign_off_pending: false
ratification_log_2026-06-15: "A0 batch GO. D4 append-only. D7 = pas d'escalation additionnelle. D4 distinction: ce ADR-MEM-001 ≠ ADR-MEM-001 historique IndexedDB (A0 clarifier au prochain tour si nécessaire)."
---

# ADR-MEM-001 — Memory Fabric Unified Doctrine

## Status
**PROPOSED → ACCEPTED via "go for all" A0 2026-06-15** (scope templates mission 4 — A0 priorise
au prochain tour si hypothèse A2 erronée).

⚠️ **D4 no-self-contradiction** : un ADR `ADR-MEM-001` historique existe (IndexedDB Cloisonnement
LD01-LD08) mais n'est pas dans `_SPECS/ADR/` canonique. Le présent ADR est **distinct** (Memory
Fabric multi-layer), scope "memory canonique unifiée" pas "storage IndexedDB". A0 peut soit (a)
renommer le présent en `ADR-MEM-002`, soit (b) confirmer l'unicité du scope. D4 documente.

## Context

1. **Mission 4 (2026-06-15)** : A2 a identifié template Tilly `02_memory_fabric_unified` dans
   `02_Templates/`. Doctrine à formaliser.
2. **5 couches mémoire A'Space V2** actuellement opérationnelles (mais non documentées comme doctrine) :
   - `~/.claude/CLAUDE.md` (injection runtime, ~30 KB)
   - `AGENTS.md` (canon A0-A3 fractal, ~50 KB)
   - `MEMORY.md` (index mémoire inter-sessions, ~30 KB)
   - `wiki/hand_offs/*` + `wiki/log.md` (doctrine opérationnelle, illimité)
   - `_SPECS/ADR/*` (doctrines formelles, illimité, append-only)
3. **Manque** = ownership explicite par couche + TTL + retrieval pattern. Sans doctrine unifiée,
   A2 ré-derive à chaque session "où est stocké X ?" (perte temps D7).

## Decision

**D1 — 5 couches mémoire canoniques A'Space V2** :

| Couche | Owner | TTL | Retrieval | Format |
|--------|-------|-----|-----------|--------|
| **L1 — CLAUDE.md injection** | A0 (éditable) | Permanent | Auto-injecté par harness à chaque session | Markdown ≤ 30 KB |
| **L2 — AGENTS.md canon** | A0 + A2 (proposition) | Permanent | Read par A2 à chaque tour | Markdown fractal A0-A3 |
| **L3 — MEMORY.md index** | A2 (auto-update end-of-session) | Permanent (rotation 24 KB) | Read par A2 à chaque tour | Markdown ≤ 24 KB (limit harness) |
| **L4 — wiki/hand_offs + log** | A0 + A2 + A3 (sub-agents) | Permanent append-only | Grep + Read à la demande | Markdown libre |
| **L5 — _SPECS/ADR doctrinaux** | A0 (sign-off) + A2 (draft) | Permanent append-only | Read par A2 si pertinent | Markdown structuré frontmatter |

**D2 — Ownership strict** :
- L1 (CLAUDE.md) : A0 UNIQUEMENT peut modifier (l'agent propose, A0 valide).
- L2 (AGENTS.md) : A0 + A2 collaboratif, A0 sign-off pour modifications structurelles.
- L3 (MEMORY.md) : A2 auto-update end-of-session (skill `/abc-os-write-back-protocol` canon).
- L4 (wiki) : tout agent peut append, jamais delete (D4 append-only).
- L5 (ADR) : A0 sign-off obligatoire (cf. `sign_off_a0` field dans frontmatter).

**D3 — Retrieval pattern "1 question, 1 couche prioritaire"** :
- "Quel est le runtime LLM ?" → L1 (CLAUDE.md Runtime LLM section).
- "Quelle est la doctrine verify-before-assert ?" → L5 (ADR-META-001).
- "Qu'est-ce qui s'est passé en session 2026-06-14 ?" → L4 (wiki/hand_offs/sessions_archive/).
- "Quelle est l'URL du dashboard OMK ?" → L4 ou L3 (MEMORY.md index).
- "Qui a décidé la rotation trimestrielle des secrets ?" → L5 (ADR-SECURITY-001).

**D4 — Append-only strict** : aucune couche ne permet delete destructif. D4 = loi canonique.
Suppression = déplacement vers `_TRASH/<date>_<reason>/` + INDEX.

**D5 — Rotation L3 MEMORY.md** : si dépasse 24 KB (limite harness), A2 fait un **dépeçage** end-of-session
(entrées thématiques → fichiers dédiés `memory_<topic>.md`, lien dans MEMORY.md). D4 append-only
préservé (le fichier dédié hérite de l'entrée originale).

## Consequences

- ✅ A2 ne ré-derive plus "où est stocké X" — pattern retrieval D3 explicite.
- ✅ Ownership D2 = 0 ambiguity "qui peut modifier quoi".
- ✅ D4 append-only = knowledge canonique A'Space croît sans corruption.
- ✅ L3 rotation = MEMORY.md reste lisible et chargé en début de session.
- ⚠️ Si L3 fragmentation excessive (> 10 fichiers dédiés), A0 review et consolide (D6 root cause).

## References

- `02_Templates` PARRA Geordi mission 4 (template source Tilly `02_memory_fabric_unified`).
- `~/.claude/CLAUDE.md` (L1, ~30 KB).
- `ASpace_OS_V2/00_Amadeus/01_Identity_Core/AGENTS.md` (L2, ~50 KB).
- `~/.claude/projects/c--Users-amado/memory/MEMORY.md` (L3, ~30 KB actuel).
- `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/` (L4).
- `ASpace_OS_V2/_SPECS/ADR/` (L5).
- `~/.claude/skills/abc-os-write-back-protocol/SKILL.md` (L3 update protocol, sister).
- `ADR-OBSERVABILITY-001_sessions-canon-md-rotation.md` (sister, sessions lifecycle).
