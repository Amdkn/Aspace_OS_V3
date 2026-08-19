---
type: Concept
title: CEO-BENCH × SpecLoop — 18 composants d'exécution
description: 11 composants CEO-BENCH (Chen/Narasimhan/Liu, Princeton) + 7 composants SpecLoop (NTU/MediaTek) intégrés dans A'Space OS. Ce que les gagnants font : mémoire courte, forecast confronté, if-then dense, spend ciblé, info payée.
tags: [CEO-BENCH, SpecLoop, intégration, exécution, runbook, E.1-E.4]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture_v2, at: 2026-08-19 }
sources:
  - id: INTEGRATION_CEOBENCH
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/INTEGRATION_CEOBENCH_SPECLOOP.md
    title: Intégration complète CEO-BENCH × SpecLoop dans A'Space OS
    last_modified: 2026-07-19
okf_version: "0.2"
---

# CEO-BENCH × SpecLoop — 18 composants d'exécution

## Énoncé

Ce que le papier CEO-BENCH prouve : seuls Opus 4.8 ($27.8M) et GPT-5.5 ($21.3M) finissent au-dessus du $1M de départ ; la baseline **à règles fixes fait $15.7M** — la plupart des agents font faillite. Ce qui sépare les gagnants des morts tient en 4 axes mesurés (Fig. 12) : découverte d'info cachée (43 % d'allocation efficace vs 20 % random), **erreur de forecast cash à 4 semaines (8 % vs 179 %)**, lag de détection concurrent (1 semaine vs 2), **densité de "if" dans les mémos (8.6/semaine vs 2.6)**.

## 11 composants CEO-BENCH

| # | Composant | Intégration A'Space |
|---|-----------|------------------------|
| C1 | Refresh hebdo contexte + mémoire agent-editable | `memory_<domaine>.md` ≤150 l. réécrit en S4 |
| C2 | Mémo if-then (muscle des gagnants) | Format S4 Harvest : DÉCISION + SI signal ALORS réversion |
| C3 | Forecast cash J+28 chaque lundi | `forecast.md` — erreur > 50% = Rock mal compris |
| C4 | 19 tables SQL comme seule source d'état | 6 tables Supabase : ledger, subscriptions, pipeline, outreach_log, issues, experiments |
| C5 | Équation de cash quotidienne (Eq. 1) | Vue `daily_cash` — cash < 2 mois burn = mode préservation |
| C6 | Budget d'acquisition d'information | 10 conversations de découverte/mois, loggées `source='research'` |
| C7 | Spending ciblé (90 % vs 43 %) | 1 segment nommé par € /heure de dev |
| C8 | 8 catégories d'action = 8 B2 | WonderWoman/Superman/Flash/Batman/JohnJones/Cyborg/GreenLantern/transverse |
| C9 | Détection concurrent ≤ 1 semaine | 1 scrum/semaine Growth = veille signaux faibles |
| C10 | Turns/semaine et coût API comme métriques | Budget tokens/domaine loggé dans `ledger` |
| C11 | Monde non-stationnaire | Re-scope mensuel du Rock = feature, pas échec |

## 7 composants SpecLoop

| # | Composant | Intégration A'Space |
|---|-----------|------------------------|
| S1 | 3 rôles : Générateur / Reconstructeur / Vérificateur | Summers (B1) / B3 / query SQL |
| S2 | Information hiding (LE principe de design) | B3 Runbook SEUL, jamais de brief oral |
| S3 | Taxonomie d'erreurs E.1-E.4 | Routage mécanique des échecs |
| S4 | Contre-exemple > pass/fail | Uplink `[E-type] + cas concret + trace SQL` |
| S5 | Format de spec structuré | Runbook 1 page : Objectif / Entrées / Sorties / Procédure / Cadence / Notes |
| S6 | Budget de retry avant escalade | 1 FAIL = retry · 2 FAILs consécutifs = E.3 |
| S7 | Score de reconstruction = mesure de qualité | RR-Score = % scrums PASS sans demande de contexte |

## Taxonomie d'erreurs E.1-E.4

| Erreur | Équivalent business | Traitement | Qui répare |
|--------|---------------------|------------|------------|
| E.1 non-vérifiable | pas de métrique SQL observable | STOP — pas de dispatch | Picard |
| E.2 ne compile pas | script crashe, outreach ne part pas | retry local 3× | B2 |
| E.3 tourne mais mismatch | process s'exécute, métrique diverge | contre-exemple précis + amend Runbook | B1 (Summers/Gstack) |
| E.4 inconclusif | on ne sait pas si ça marche | reformuler la spec — ambiguïté = défaut de spec | B1 |

## Câblage dans la cadence

```
PICARD (cycle)      E.1 : aucune vision ne descend sans métrique SQL observable [S3]
   ▼
SUMMERS (Rock/mois) Runbook 1 page format S5 · forecast J+28 chaque lundi [C3]
   ▼                amende sur contre-exemple E.3 [S4] · re-scope mensuel = feature [C11]
8 B2 (4 sprints)    memory_<domaine>.md refresh hebdo [C1] · mémo if-then ≥5 [C2]
   ▼                E.2 réparé localement (3 retries) [S3/S6] · budget tokens loggé [C10]
   ▼                spending 90% ciblé par segment [C7] · veille concurrent 1 scrum/sem [C9]
B3 (5 scrums)       query SQL avant, delta SQL après [C4] · exécute depuis le Runbook SEUL [S2]
   ▲                uplink = [E-type + contre-exemple + ID SQL] [S4]
UPLINK              2 FAILs consécutifs = E.3 vers Summers [S6]
                    RR-Score du Runbook = % scrums PASS sans demande de contexte [S7]
```

## Base SQL réelle

6 tables, 4 vues (`daily_cash`, `mrr_by_segment`, `pipeline_by_stage`, `inference_cost_by_domain`), 1 règle : **un état non-requêtable n'existe pas** [C4/C5/C10].
