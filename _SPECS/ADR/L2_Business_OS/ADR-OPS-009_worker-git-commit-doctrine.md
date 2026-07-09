---
id: ADR-OPS-009
title: Worker Git Commit Doctrine — A3 commits between features, D4-git-workflow
status: ACCEPTED
level: L2
level_name: Business_OS
date: 2026-06-22
author: A3 sub-agent (handoff youtube_ingest_2026-06-22)
supersedes: null
extends:
  - ADR-META-001 D4 (no-amnesia append-only)
  - .claude/rules/git-workflow.md (conventional commits format)
source: Luke Alvoeiro, Factory — "Multi-Agent Systems That Ship for Days" (AI Engineer channel, 2026-06-22)
---

# ADR-OPS-009 — Worker Git Commit Doctrine

## Contexte

Luke Alvoeiro (Factory) : "When a feature is assigned to a worker, that worker has clean context, no accumulated baggage, no degraded attention. The worker reads its spec. It implements the feature and then **commits by Git** allowing the next worker to inherit a clean slate and a working code base."

Pattern clé : chaque A3 worker commit après **chaque feature complétée**, pas en fin de mission. Bénéfices :
- Next worker hérite d'un code base working (pas de merge hell mid-mission).
- Handoff structurel = git history = diff review-able par A1/A2.
- Rollback granulaire (revert 1 feature sans casser la mission).
- Validation post-commit = scrutiny validator peut checker le commit diff.

**Problème A'Space** : aujourd'hui, beaucoup de missions A'Space accumulent le travail et ne commitent qu'en fin de mission (pattern "batch commit"). Conséquences observées :
- D6 root cause : merge conflicts mid-mission si 2 A3 touchent même fichier.
- Validation post-commit impossible (tout est dans 1 mega-commit).
- Rollback granulaire impossible (revert 1 feature = revert tout).

## Décision

**A3 twins commit after each feature complete, pas en fin de mission.**

**Règle opérationnelle** :
1. A3 reçoit 1 feature du validation contract (per ADR-LIFE-013).
2. A3 implémente la feature.
3. **A3 commit immédiatement** après feature verte (tests + lint + type-check pass).
4. Format commit = conventional commits (per `.claude/rules/git-workflow.md`) :
   - `<type>: <description>` — types : feat, fix, refactor, docs, test, chore, perf, ci.
   - Body optionnel : référence à validation contract (assertion ID), référence à handoff.
5. A3 passe au worker suivant via handoff structuré (per Factory pattern).
6. Validators peuvent paralleliser code review sur les commits (read-only operation, per ADR-LIFE-014).

**Exceptions** :
- **Documentation-only changes** : peuvent batcher (git history pollution = bruit, pas signal).
- **Sub-feature incremental** : si feature = > 10 commits logiques, A3 peut grouper (mais commit groups = 1 logical feature, pas 1 mega-commit mission).
- **Hotfix emergency** : A1 Beth/Morty peut autoriser batch commit pour incidents critiques (mais justification obligatoire dans outbox E2).

**Attribution** : désactivée globalement via `~/.claude/settings.json` (per `.claude/rules/git-workflow.md`). Pas de `Co-Authored-By` Claude dans commits.

## Conséquences

**Positives** :
- Code base working à chaque commit (next worker hérite clean slate, per Factory).
- Code review granulaire (validators peuvent reviewer commit-by-commit, parallel read-only).
- Rollback granulaire (revert 1 feature = safe).
- Git history = audit trail canon (D4 append-only appliqué au source code).
- Handoff structured ↔ git diff = double validation (handoff documente WHAT, git commit documente HOW).

**Négatives** :
- Commit overhead ↑ (A3 doit formatter commit message + push = ~30s per feature). Acceptable vs merge hell risk.
- Risque de commits "WIP" si A3 push trop tôt (mitigation : validation contract assertions = definition of done).

## Alternatives considérées

1. **Batch commit fin de mission** : rejeté — viole D4 no-amnesia + Factory pattern (merge hell mid-mission).
2. **Squash commits fin de mission** : considéré — utile pour release finale, mais perte de granularité handoff. Mitigé : squash UNIQUEMENT au release tag, pas en dev.
3. **Auto-commit par hook PostToolUse** : rejeté — trop magique, A3 doit rester accountable de ses commits (D7).

## Références

- **Source canon** : `wiki/hand_offs/youtube_ingest_2026-06-22/youtube_ingestion_handoff_2026-06-22.md` §4
- **Video** : https://youtu.be/ow1we5PzK-o?si=gjZCWKaytC21sRDo
- **Git workflow rule** : `.claude/rules/git-workflow.md`
- **ADR-META-001 D4** : `_SPECS/ADR/L0_Kernel_OS/ADR-META-001_anti-paresse-verify-before-assert.md` (no-amnesia append-only)
- **ADR-LIFE-014** : Serial-first parallel opt-in (validators parallel code review = read-only).