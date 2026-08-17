---
type: Concept
title: Triptyque V4 (T1, T2, T3)
description: Structure en 3 axes du projet OMK — T1 People+Ops+Product (build), T2 Growth+Sales+Finance (sell), T3 Legal+R&D (govern + innovate). Chaque triptyque = 1 Ownerbook + 3 chartes + 3 runbooks par Rock.
tags: [concept, triptyque, t1, t2, t3, omk, w40, v4]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraire_substrat_rdf, at: 2026-08-17T19:50:00Z }
  - { by: process:lecture_concepts_picard, at: 2026-08-17T21:00:00Z }
sources:
  - id: ownerbook-T1
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/ownerbooks/ownerbook_T1_people_ops_product.md"
    title: Ownerbook T1 People/Ops/Product (Rock B1-1, 2026-07-15)
    last_modified: 2026-07-15
  - id: ownerbook-T2
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/ownerbooks/ownerbook_T2_growth_sales_finance.md"
    title: Ownerbook T2 Growth/Sales/Finance (Rock B1-2, 2026-07-15)
    last_modified: 2026-07-15
  - id: ownerbook-T3
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/ownerbooks/ownerbook_T3_legal_rd.md"
    title: Ownerbook T3 Legal/R&D (Rock B1-3, 2026-07-15)
    last_modified: 2026-07-15
okf_version: "0.2"
---

# Triptyque V4 (T1, T2, T3)

## Définition

Structure en **3 axes** du projet OMK Business OS, où chaque axe est un
**triptyque** (3 B2 captain + 3 B3 squad + 1 mission). Origine : W40 §2
(151 lignes, 12/12 grade, verbatim A+ daté 2026-07-15). Trois triptyques
couvrent l'ensemble de l'OS Business :

| Triptyque | Mission | B2 owners | B3 squads |
|-----------|---------|-----------|-----------|
| **T1** | RH Agentique + SOP & Skills + Agency as a Service | GreenLantern / Batman / Flash | X-Men / Fantastic4 / Avengers |
| **T2** | AAARR + 100M Offers + 1-Person/1-Billion Company | Superman / JohnJones / WonderWoman | Guardians of the Galaxy / Illuminati / Thunderbolts |
| **T3** | 365 Conformité + Amélioration par Innovation de Découverte externe | Aquaman / Cyborg | Eternals / Kang Dynasty |

## Anatomie d'un triptyque

Chaque triptyque = **1 Ownerbook** + **3 chartes** (Mission + DoD + Squad
Dispatch) par Rock + **3 runbooks** (M1-M2, M3-M4, M5-M6) par Rock. Cadence
de production : **Phase 1 BMad** (chartes WHAT) puis **Phase 2 Gstack**
(runbooks HOW).

```
T1 (Rock B1-1)
├── ownerbook_T1_people_ops_product.md
├── chartes_cycle_2/
│   ├── chart_T1_people_b2b_saas_playbook.md
│   ├── chart_T1_people_hr_ops.md
│   ├── chart_T1_people_onboarding.md
│   ├── chart_T1_ops_perf_metrics.md
│   ├── chart_T1_ops_runbook_v1.md
│   ├── chart_T1_ops_sop_canon.md
│   ├── chart_T1_product_prd_template.md
│   ├── chart_T1_product_roadmap.md
│   └── chart_T1_product_spec_loop.md
└── runbooks/ (à venir, format sister T2/T3)
    ├── runbook_T1_people_ops_product_m1_m2.md
    ├── runbook_T1_people_ops_product_m3_m4.md
    └── runbook_T1_people_ops_product_m5_m6.md
```

## Charges utiles par triptyque

**T1** charge les 53 B3 agents en profiles documentés, SOP canon
(tool → skill), Product spec-loop output. Sans T1, T2 n'a rien à vendre
et T3 pas de backbone compliance.

**T2** charge le AAARR funnel (Superman), 100M Offers Hormozi
(JohnJones), et 1-Person/1-Billion unit economics (WonderWoman). C'est
**le seul triptyque qui génère du revenu** — mais il consomme T1 et
s'appuie sur T3.

**T3** porte 365 Conformité (Aquaman H90 legal review) + R&D External
Discovery (Cyborg, ex-IT absorbé à L0 Rick). US market pivot
(2026-07-15) : AI Bill of Rights OSTP 2022 + Colorado AI Act 2026, **pas**
EU AI-Act 2026-08-02 primary driver.

## Anti-patterns et aborts

Chaque triptyque porte ses propres Abort-A/B/C/D :
- **T1 Abort-D** : drift USD pricing back to EUR → STOP, re-read
  `ADR-AAAS-PRICING-001` Hypothèse A
- **T2 Abort-?:** CAC ≤ 1/3 LTV per WonderWoman Saru H3 quarterly
- **T3 Abort-A** : 365 Conformité gate skipped (US compliance clause
  missing) → STOP, B2 Aquaman HALT
- **T3 Abort-C** : IT infra work re-introduced in T3 (L0 sovereignty
  violated) → STOP, B3 Kang Prime return to L0

## Doctrine Spec-Loop

A0 = **IA spec-lock, no manual UI gate**. Documenté W40 §2. Chaque
DoD-3 / DoD-4 des Ownerbooks porte cette contrainte. C'est le pendant
positif des Abort-C (UI manuelle = violation).

## Liens

- [[omk-business-os]] — le projet qui porte la structure
- [[fifty-three-b3-agent-roster]] — la squad 53 agents
- [[eight-domain-avengers-wheel]] — les 8 B2 captains
- [[picard-project-pattern]] — l'origine du format

## Note de confiance

**Confirmé par machine.** 3 Ownerbooks lus, 24 chartes cycle 2 lus
(via substrat), W40 §2 référencé. Cohérence Ownerbook ↔ Charter lisible
par énumération.

*Standing : structure Triptyque V4 définie et déployée pour OMK Q3 2026.*
