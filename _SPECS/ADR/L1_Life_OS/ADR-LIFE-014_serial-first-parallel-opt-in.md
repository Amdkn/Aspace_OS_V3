---
id: ADR-LIFE-014
title: Serial-First, Parallel Opt-in — D7 reinforcement anti-swarm premature
status: RATIFIED
level: L1
level_name: Life_OS
date: 2026-06-22
author: A3 sub-agent (handoff youtube_ingest_2026-06-22)
supersedes: null
extends:
  - ADR-META-001_anti-paresse-verify-before-assert.md (D7 cost-of-escalation)
source: Luke Alvoeiro, Factory — "Multi-Agent Systems That Ship for Days" (AI Engineer channel, 2026-06-22)
---

# ADR-LIFE-014 — Serial-First, Parallel Opt-in

## Contexte

Luke Alvoeiro (Factory) a testé parallelism classique sur missions software dev : **ça ne marche pas**. Citation directe : "Agents conflict. They step on each other's changes. They duplicate work. They make inconsistent architectural decisions. And so the coordination overhead ends up eating up the speed gains all the while you're burning tokens."

Solution Factory : **sérial par défaut**. 1 worker OU validator à la fois. Parallel **uniquement** sur read-only operations :
- Search through code base
- Research APIs
- Code review (validators peuvent paralleliser entre eux sur features différentes du même milestone)

**Tradeoff Factory** : "Slower on paper, but error rate drops dramatically, and when you have tasks that run for many days, this correctness compounds."

**Problème A'Space** : ADR-META-001 D7 (cost-of-escalation) mandate que l'escalation A0 est ~100× le coût original. Mais aucune règle ne discipline **quand paralleliser A3 twins**. Risque observé : swarm premature = 35 A3 spawned simultanément = overhead coordination + drift + tokens brûlés.

## Décision

**Default = sériel. Parallel = opt-in sur read-only only.**

**Règle opérationnelle** :
1. Un seul A3 worker actif par workstream à un moment T.
2. Un seul A2 orchestrateur actif par workstream à un moment T.
3. Parallel autorisé **uniquement** sur opérations read-only vérifiables (D1 receipts obligatoires) :
   - Pas de shared mutable state.
   - Pas de shared resource (API rate-limited, single-writer file, etc.).
   - Pas de décision architecturale (ces décisions = sériées, validées par A1).
4. Validators peuvent paralleliser entre eux **sur des features différentes** du même milestone (read-only check : feature N+1 ne dépend pas de feature N).

**D1 verification obligatoire avant parallel** :
- Inventorier shared state, shared resource, décision architecturale.
- Si ≥ 1 yes → sériel obligatoire.
- Si 0 yes → log justification dans handoff + parallel OK.

**Escalation A0** : si A2 détecte que sérial bloque throughput critique (D7 cost-of-escalation = 100×), A2 peut remonter à A1 Beth/Morty pour exemption (mais pas avant).

## Conséquences

**Positives** :
- Erreur rate ↓ drastiquement (Factory D1 receipts : "validation never succeeds on first go" en parallel, mais sérial first-pass success ↑).
- Token economy ↑ (pas de coordination overhead = moins de re-derivation).
- Correctness compounds sur missions multi-jours (12WY cycle 12 semaines → validé).
- D7 cost-of-escalation renforcé (parallel premature = escalation A0 massive).

**Négatives** :
- Throughput ↓ apparent (1 worker vs 10 simultanés). Mitigé par : (a) missions multi-jours où correctness > speed, (b) Factory 5 engineers × 6 workstreams = 30 workstreams effective via serial + targeted parallel.
- A2 doit apprendre à dire "sériel" même quand A0 push pour "fast parallel" (YAGNI speed).

## Alternatives considérées

1. **Parallel by default, serial opt-in** : rejeté — c'est exactement le pattern Factory a testé et qui ne marche pas (D6 root cause : coordination overhead eats speed gains).
2. **Auto-detect parallelisable ops** : considéré — faisable (AST analysis des A3 calls), mais coûteux en meta-cognition A2. Rejeté pour Q3 2026 (YAGNI).
3. **Parallel par nombre d'A3 twins disponibles** : rejeté — confond disponibilité et compatibilité. Anti-pattern D7.

## Références

- **Source canon** : `wiki/hand_offs/youtube_ingest_2026-06-22/youtube_ingestion_handoff_2026-06-22.md` §4
- **Video** : https://youtu.be/ow1we5PzK-o?si=gjZCWKaytC21sRDo
- **ADR-META-001 D7** : `_SPECS/ADR/L0_Kernel_OS/ADR-META-001_anti-paresse-verify-before-assert.md`
- **Anti-paresse doctrine** : D1 verify, D7 cost-of-escalation.
- **D6 root cause #44** : swarm `rc=1` partial → log warning + continue (déjà shippé).