---
id: ADR-LIFE-013
title: Validation Contract Pattern — A1 Beth/Morty sign before any A2 work
status: RATIFIED
level: L1
level_name: Life_OS
date: 2026-06-22
author: A3 sub-agent (handoff youtube_ingest_2026-06-22)
supersedes: null
extends:
  - handoff_a0_divinity_arsenal_2026-06-20.md (A1 Gatekeepers doctrine)
  - ADR-META-005_hooks-automation.md (Vague 2 hooks, Sobriété scope)
source: Luke Alvoeiro, Factory — "Multi-Agent Systems That Ship for Days" (AI Engineer channel, 2026-06-22)
---

# ADR-LIFE-013 — Validation Contract Pattern

## Contexte

Luke Alvoeiro (Factory) : "Validation Contract est écrit pendant planning, **avant tout code**, et définit correctness indépendamment de l'implémentation." Pour projets complexes = centaines d'assertions. Chaque feature = 1+ assertions à satisfaire. **Somme des features = toutes assertions couvertes.**

Le problème qu'il adresse : tests écrits après implémentation ne catchent pas les bugs, ils confirment les décisions ("Tests written after implementation don't catch bugs. They confirm decisions. If you rely on validation like that your system will eventually drift.").

**Problème A'Space** : aujourd'hui, A2 reçoit une intention A0 et dispatch directement aux A3 twins. Aucun contrat formel n'est signé entre A0/A1 et A2/A3. Conséquence : A3 peut dériver (scope creep, misinterpretation), et A1 Beth/Morty ne peuvent bloquer qu'au post-mortem (validation trop tardive).

## Décision

**Aucun A2 work ne commence sans validation contract signé par A1 Gatekeeper (Beth ou Morty selon domaine).**

**Template validation contract** (5 sections obligatoires) :
1. **Input** : quelles données/intentions A0 fournit, format attendu.
2. **Output** : quels livrables A2/A3 doivent produire, format + acceptance criteria mesurables.
3. **Risk** : quels échecs sont acceptables (rollback plan), quels échecs sont bloquants (hard-stop).
4. **Rollback** : comment annuler proprement si drift détecté (D4 append-only → `_TRASH_<date>/`).
5. **Criteria** : assertions vérifiables (≥ 3 par feature, idéalement 5-10 pour projets complexes, comme Factory).

**Workflow obligatoire** :
1. A0 émet intention (méta-langage).
2. **A1 Beth ou Morty produit + signe le validation contract** avant tout dispatch A2.
3. A2 orchestre selon le contract (ne peut pas dévier hors scope sans nouveau contract).
4. A3 twins exécutent features ; chaque feature complétée doit matcher ≥ 1 assertion du contract.
5. A1 revalide à chaque milestone boundary (Factory pattern).

**Authority A1** : A1 Beth/Morty peuvent bloquer/refuser un A2 work si contract incomplet ou assertions insuffisantes. D7 cost-of-escalation : refuser est moins coûteux qu'exécuter sans contrat.

## Conséquences

**Positives** :
- Drift ↓ (A3 sait exactement quoi shipper, pas d'ambiguïté).
- A1 visibility ↑ (cadrage avant exécution, pas après).
- Anti-bitter-lesson (Factory) : structure permet d'utiliser open-weight models sans perte qualité.
- Compound return (Factory) : codebase plus clean qu'avant (chaque mission = net positive).

**Négatives** :
- Upfront cost ↑ (A1 doit investir 10-20% du temps en contract avant A2 work — c'est du **strategic programming** vs **tactical**, validé par Pocock).
- Risque d'over-spec (YAGNI — assertions inutiles ralentissent sans valeur).
- A1 gatekeeping bottleneck si volume missions ↑ (mitigation : A1 peut déléguer validation à A2 Discovery Zora pour contrats sub-L1).

## Alternatives considérées

1. **A2 self-contract** : rejeté — viole doctrine A1 Gatekeepers (A1 = authority L1, A2 = orchestrateur).
2. **Post-hoc validation seulement** : rejeté — c'est exactement le pattern que Luke critique ("tests after implementation confirm decisions, don't catch bugs").
3. **Contract optionnel pour sub-L1 work** : considéré — risque de drift. Gardé **uniquement pour validations A2→A3 sub-L1 sub-30min** (exempté si A1 signe exemption explicite dans outbox E2).

## Références

- **Source canon** : `wiki/hand_offs/youtube_ingest_2026-06-22/youtube_ingestion_handoff_2026-06-22.md` §4
- **Video** : https://youtu.be/ow1we5PzK-o?si=gjZCWKaytC21sRDo
- **A0 Divinity Arsenal** : `wiki/hand_offs/handoff_a0_divinity_arsenal_2026-06-20.md` (A1 Beth+Morty doctrine)
- **ADR-META-005** : `_SPECS/ADR/L1_Life_OS/ADR-META-005_hooks-automation.md` (Sobriété hooks)
- **Pocock Strategic Programming** : `03_Resources_Geordi/01_Guides/02_Ops/2026-06-19_matt-pocock-harness-engineering-agentic-workflow.md`