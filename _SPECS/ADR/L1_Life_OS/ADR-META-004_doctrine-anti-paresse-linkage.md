---
id: ADR-META-004
title: Doctrine Anti-Paresse Linkage — D1-D8 Anchoring Across L0/L1/L2 ADRs
type: ADR (Architectural Decision Record)
status: PROPOSED (A0 sign-off 2026-06-15 via "go for all", à valider scope Templates mission 4)
date: 2026-06-15
author: A0 (Amadeus) via A2 (Claude Code) sub-agent
domain: L1 Life_OS / Meta-Cognition / Doctrine Linkage / Cross-Layer
tags: [#ADR #meta #anti-paresse #d1-d8 #linkage #cross-layer #doctrine]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-META-003]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, "all L0/L1/L2 ADRs"]
provenance: |
  Née 2026-06-15 de l'analyse mission 4 (PARA Geordi 02_Templates) : template Tilly
  `01_doctrine_anti_paresse_linkage` détecté. Doctrine à formaliser : chaque ADR L0/L1/L2 doit
  pointer `doctrine_anchors: [ADR-META-001, ...]` dans son frontmatter, et la lecture de tout ADR
  commence par vérifier que les anchors sont valid (pas deprecated, pas contradiction).
sign_off_a0: "A0 Amadeus — Go ADR-META-004 — 2026-06-15 (via 'go for all' session-level directive, scope à valider)"
sign_off_pending: false
ratification_log_2026-06-15: "A0 batch GO. D4 append-only. D7 = pas d'escalation additionnelle."
---

# ADR-META-004 — Doctrine Anti-Paresse Linkage

## Status
**PROPOSED → ACCEPTED via "go for all" A0 2026-06-15** (scope templates mission 4 — A0 priorise
au prochain tour si hypothèse A2 erronée).

## Context

1. **Mission 4 (2026-06-15)** : A2 a identifié template Tilly `01_doctrine_anti_paresse_linkage`
   dans `02_Templates/`. Doctrine à formaliser.
2. **ADR-META-001 (Anti-Paresse D1-D8)** est le **fondement** de tout ADR A'Space V2. Mais la
   plupart des ADRs drafts omettent le `doctrine_anchors` field en frontmatter, ou le mettent
   vaguement `[ADR-META-001, ADR-META-002, ...]` sans préciser quelle D-number est invoquée.
3. **Risque D4** : un ADR qui contredit une D-number existante passe inaperçu si pas de linkage
   explicite. Pattern D1 verify-before-assert = lire anchors avant de signer.

## Decision

**D1 — Frontmatter `doctrine_anchors` obligatoire** pour tout ADR A'Space V2 :
```yaml
doctrine_anchors: [ADR-META-001-D1, ADR-META-001-D4, ADR-META-002-D9, ...]
```
Chaque anchor précise la D-number invoquée (pas juste l'ADR-id). Permet audit mécanique.

**D2 — Audit pre-sign-off** : avant qu'A0 signe un ADR en `status: ACCEPTED`, A2 (ou A0 lui-même)
exécute le check :
- Pour chaque `doctrine_anchors`, lire l'ADR cité, vérifier la D-number existe.
- Vérifier que le présent ADR ne contredit aucune D-number citée.
- Si contradiction, escalader à A0 (D7 — pas d'auto-fix sur contradiction D-number).

**D3 — Append-only linkage updates** : si un ADR anchor change (ex. D-number D9 renommée D9.5),
l'ADR qui pointe cet anchor fait un append-only update (D4 no-self-contradiction). Pas de rewrite.

**D4 — Index croisé** : `_SPECS/ADR/INDEX.md` (à créer si absent) liste tous les ADRs + leurs
anchors. Lecture rapide "qui pointe quoi" sans grep.

**D5 — Lint hook pre-commit** (optionnel S+5) : un script PowerShell
`~/.claude/bin/adr-lint-anchors.ps1` valide que tout `doctrine_anchors` field référence des
ADR-ids existants. Bloque commit si anchor manquant ou typo.

## Consequences

- ✅ Tout ADR est auditable mécaniquement (D1 verify-before-assert à grande échelle).
- ✅ D4 no-self-contradiction détectable en pre-sign-off (avant ratification A0).
- ✅ Index croisé = retrieval rapide "qui pointe META-001 D4 ?".
- ⚠️ Coût initial : backfill `doctrine_anchors` field sur tous les ADRs existants (~15 ADRs
  canoniques, ~30 min A2 sub-agent).

## References

- `02_Templates` PARRA Geordi mission 4 (template source Tilly `01_doctrine_anti_paresse_linkage`).
- `ADR-META-001_anti-paresse-verify-before-assert.md` (anchor canonique D1-D8).
- `ADR-META-002_autonomy-by-design.md` (anchor D9-D12, sister).
- `ADR-META-003_model-agnostic-runtime-doctrine.md` (anchor D13, sister).
- `_SPECS/ADR/INDEX.md` (à créer, index croisé).
