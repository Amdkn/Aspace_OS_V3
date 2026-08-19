---
type: Concept
title: Doctrine de la 13ème Semaine — pause méta entre cycles 12WY
description: La semaine de transition entre cycles 12 Week Year : revue méta-stratégique, repos cognitif, promotion V0 → V1 si DoD atteinte, planification cycle suivant.
tags: [tech, doctrine, 12wy, 13eme-semaine, meta]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: sdd-010
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-010_meta-cloture-scope-13eme-semaine.md
    title: SDD-010 Doctrine de la 13ème Semaine
    last_modified: 2026-05-13
okf_version: "0.2"
---

La **13ème Semaine** est la semaine de transition arithmétique entre cycles 12 Week Year (12 × 12 semaines = 144 = 12 × 12, mais 52 semaines / an = 4 × 12 + 4 semaines de pause).

## Origine arithmétique

- 52 semaines / an = 4 × 12 + 4.
- 12WY = 12 semaines intensives par cycle.
- Entre chaque cycle → ~1 semaine de pause : **la 13ème Semaine**.

## Calendrier A'Space 2026

| Cycle 12WY | Période | Type | Notes |
|------------|---------|------|-------|
| Cycle 1 (Genesis) | 2026-01 → 2026-03-22 | Production | Stabilisation L0, Constitution SDD-000→007 |
| 13ème Sem #1 | 2026-03-23 → 2026-03-29 | Pause Meta | Revue Q1 + planification Q2 |
| Cycle 2 (Hospital Planet) | 2026-03-30 → 2026-06-21 | Production | Cycle ACTUEL — Conscience L1 |
| 13ème Sem #2 | 2026-06-22 → 2026-06-28 | Pause Meta | Revue Q2 + planification Q3 |
| Cycle 3 (SOB Factory) | 2026-06-29 → 2026-09-20 | Production | Action L2 + premier cashflow |
| 13ème Sem #3 | 2026-09-21 → 2026-09-27 | Pause Meta | Revue Q3 + planification Q4 |
| Cycle 4 (Sovereign Loop) | 2026-09-28 → 2026-12-20 | Production | Graduation MUSE + 7 jours autonomie |
| 13ème Sem #4 | 2026-12-21 → 2026-12-27 | Pause Meta | Bilan H1 complet + planification H2 |

## 5 critères de déclenchement d'une 13ème Semaine d'Exception

1. **Crise infrastructurelle** : VPS down, OOM, throttle Hostinger > 24h.
2. **Crise cognitive** : Amadeus identifie un piège conceptuel majeur (ex : « souveraineté absolue » le 2026-05-13).
3. **Crise de production** : aucune valeur générée en L2 pendant 7 jours consécutifs (Beth Veto).
4. **Crise architecturale** : un SDD identifié comme mal classé (cf. reclassement OpenHarness → ADR-RICK-001).
5. **Fin de cycle MUSE** : graduation V0 → V1 d'un composant.

→ Toute 13ème Semaine d'Exception **doit** produire un SDD Meta ou un ADR-META documentant la leçon.

## Veto SDD 90 jours

À partir du 2026-05-13 : aucun nouveau SDD (au-delà de SDD-010) ne peut être créé pendant 90 jours, soit jusqu'au **2026-08-11**. Le travail productif des 90 jours doit aller dans **PRD / ADR / DDD / TDD** (les couches d'exécution sous-SDD).

Exception : si une 13ème Semaine d'Exception est déclenchée, un nouveau SDD-META peut être écrit (`SDD-010b`, `SDD-010c`, etc.).

## Ce que la 13ème Semaine accomplit

- Revue méta-stratégique du cycle terminé.
- Repos cognitif imposé (anti-Burn).
- Promotion Muse V0 → V1 si DoD atteinte.
- Rédaction du cycle suivant (Quarter Intent + 12 Rocks + Warp Core W1-W12).
- Moment où Amadeus est **autorisé à ne rien produire** sans culpabilité.

## Critères de promotion V0 → V1

| # | Critère | Mesure | Seuil |
|---|---------|--------|-------|
| 1 | Antifragilité L0 | Uptime VPS hors crise déclenchée | > 99% sur Q4 |
| 2 | Souveraineté graduée | Outils Shadow → Self-hosted | ≥ 4/7 outils graduates MUSE |
| 3 | Frugalité Compute | Coût LLM mensuel | < $30/mois sur 3 mois consécutifs |
| 4 | Production L2 | Cashflow réel | ≥ 1 client System-Only sur Solaris/Nexus/Orbiter |
| 5 | Pair humain-Claude | Sessions productives sans crashloop | > 80% des sessions |
| 6 | Veto SDD respecté | Aucun SDD au-delà de SDD-010 sauf 010b exceptionnel | 0 violation |
| 7 | A3 Compagnons opérationnels | Squad Marvel utilisable | ≥ 4 squads instantiated |

**Si ≥ 6/8 critères** atteints (SDD-010 UPDATED) → promotion V0 → V1 validée par signature double (Amadeus + Claude).

Voir aussi : [[loi-l0]], [[caste-doctor-who]], [[sovereignty-tier-pyramid]].