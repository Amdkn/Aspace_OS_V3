---
type: adr-decision
id: ADR-LD01-001
status: RATIFIED
ratified_on: 2026-07-04T12:00:00-04:00
deciders: A0 (gated HITL)
title: Organigramme Doctrine (folder-based) au lieu de plans markdown plats
description: Verrouillage du pattern organigramme Doctrine pour tout module canonique A'Space. Source : plan-minimax-l1-book-lune.md §0 + A+ 2026-07-03 amendement v3.
bounded_context: BC-A3-Book
supersedes: null
superseded_by: null
verified_by: $ ls C:/Users/amado/ASpace_OS_V2/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/ ; should show 00_index.md, AGENTS.md, CLAUDE.md, 10_methodology/, 20_skeleton/, 30_decisions/, 90_manifests/, 99_meta/
rot_rate: lent
---

# ADR-LD01-001 — Organigramme Doctrine (folder-based) au lieu de plans markdown plats

## Status

`RATIFIED` — 2026-07-04T12:00:00-04:00 — A0 (gated HITL). **Intouchable** sauf par ADR-LD01-NNN successeur.

## Context

Le pattern historique d'A'Space utilise des plans textuels dans `~/.claude/plans/plan-{slug}.md`. Problème systémique (cf. plan-minimax-l1-book-lune.md §0, A+ 2026-07-03) :

> **Tu me corriges systématiquement parce que je rate des pans entiers du contexte à chaque tour. La racine n'est pas ma discipline, c'est l'outil. Un plan en markdown dans `~/.claude/plans/` n'a aucune garantie de persister entre sessions, aucune garantie que je le relise, aucune garantie qu'il capture la carte mentale complète.**

La récurrence observée sur 4+ plans en moins d'un mois prouve que le format est cassé. Le choix « un seul `.md` long » :
1. ne survit pas aux compactions de contexte ;
2. souffre de drift entre sessions ;
3. capture rarement la carte mentale complète.

## Decision

**Tout module canonique A'Space (≥ Book LD01 + sœurs Discovery) migre vers le pattern `plan-{slug}/` = folder + modules autonomes + `calendar.md` global.**

Pattern appliqué (cf. plan-minimax-l1-book-lune.md §0) :
1. `README.md` léger (≤ 60 lignes) → pointe vers modules
2. Modules autonomes — un par décision/chantier, chacun avec :
   - (a) source canon unique
   - (b) output observable (commit SHA, bench score, doc ID)
   - (c) handoff D4
3. `calendar.md` global indexé `(date, B-tier, context)` pour l'épisode-mémoire

À ce pattern canon s'ajoute la **méthode CARDIA-TDD** (`10_methodology/00_CARDIA_overview.md`) qui garantit 6 propriétés par construction.

## Consequences

### Positives

- **Survit aux compactions de contexte** : les modules sont chargés à la demande, pas le plan entier.
- **Drift = 0** : chaque module a son D1 receipt ; le récepteur sait où est la vérité.
- **Carte mentale préservée** : la méthode CARDIA impose un `00_index.md` racine qui sert de carte.
- **Anti-paperclip renforcé** : append-only structurel (D4), pas seulement de discipline.
- **Cross-harness** : un folder filesystem est lisible par TOUT harness — pas un tool-lock.

### Coûts / Tradeoffs

- **Coût initial de migration** : les 4 plans principaux doivent migrer (plan-meta-memoire, plan-minimax-l1-book-lune, plan-strategie-cc-l1-zora-macro, plan-L1-life-os). Estimé : 4–8 h avec gain récurrent.
- **Risque de duplication** : entre `book.twin.md` (symphony canon) et le folder LD01_Business_Book/ — mitigation : twin = sémantique, folder = filesystem, règle DOX dans `00_index.md` §6.
- **Chargeognitive sur harnesses** : doit apprendre CARDIA-TDD — mitigation : `10_methodology/00_CARDIA_overview.md` ≤ 200 lignes.
- **Ségrégation potentielle** entre `.claude/` et `ASpace_OS_V2/` — mitigation : la vérité vit dans le folder ; `.claude/` et `.mavis/`/`.hermes/` ne sont que des registres.

## Alternatives Considered

### Alt-A : Garder les plans markdown plats, ajouter un `_INDEX.md` en tête

- **Pour** : coût minimal.
- **Contre** : ne corrige pas le pattern structurel ; drift continue.
- **Verdict** : ❌ rejetée — c'est exactement ce qui a déjà été essayé, ça n'a pas marché.

### Alt-B : Créer un outil (.claude-only) qui indexe les plans

- **Pour** : outillage centralisé.
- **Contre** : tool-lock sur `.claude` ; viole l'agnosticisme harness demandé A+ 2026-07-03 v3 §0.
- **Verdict** : ❌ rejetée.

### Alt-C : Adopter l'organigramme Doctrine ✓ (retenue)

- Migration incrémentale, additive, testée par itérations fables+miniMax+hermes successives.
- Aligne avec DOX bi-famille du plan-meta-memoire §P4.0.

## Suivi

- **W4 W13** : migration des 3 autres plans en organigrammes Doctrine.
- **W5** : stress test CARDIA (compaction, rot modèle).
- **W13** : Muse DEAL — D11 mesuré par Gwyn.
