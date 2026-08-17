---
type: Project
title: OMK Business OS
description: OS SaaS interne OMK — 53 agents B3 et 8 capitaines B2, structure Triptyque V4 (T1 People+Ops+Product, T2 Growth+Sales+Finance, T3 Legal+R&D), pivot marché US, status ACTIVE 2026-07-15.
tags: [projet, saas, agency-as-service, us-market, triptyque, bridge, w40]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraire_substrat_rdf, at: 2026-08-17T19:50:00Z }
  - { by: process:lecture_concepts_picard, at: 2026-08-17T21:00:00Z }
sources:
  - id: runbook-D
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/runbooks/runbook-D-repositories.md"
    title: Runbook D — Phase D Repositories (M1-M6, 2026-07-15)
    last_modified: 2026-07-15
  - id: runbook-C
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/runbooks/runbook-C-saas-auth.md"
    title: Runbook C — Phase C SaaS Auth (M1-M5, 2026-07-15)
    last_modified: 2026-07-15
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
  - id: chartes-cycle-2
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/chartes_cycle_2/"
    title: 24 chartes T1-T3 (2026-07-15)
    last_modified: 2026-07-15
okf_version: "0.2"
---

# OMK Business OS

## Synthèse

**OMK Business OS** — projet SaaS interne de l'OS Business : 53 agents B3
organisés en 8 capitaines B2, structurés en **Triptyque V4** (T1, T2, T3)
avec un pivot explicite vers le **marché US** (Coach premium B2B $7.5-25K
ACV + Enterprise mid-market). Status **ACTIVE** au 2026-07-15, doctrines
verrouillées D4 (append-only) et D6 (no-self-contradiction). Suite vivante
du projet dans le dépôt `coach-os` (hors-périmètre de cette distillation).

## Trois questions — ce qu'il visait, ce qui a été livré, ce qui ne l'a pas été

**Ce qu'il visait.** Construire un SaaS **agency-as-a-service** où le
livrable n'est pas un outil — c'est un squad de 53 agents B3 déployés
contre les besoins client. Mission par triptyque :
- **T1** (RH Agentique + SOP & Skills + Agency as a Service) — B2 GreenLantern
  + Batman + Flash, B3 X-Men + Fantastic4 + Avengers
- **T2** (AAARR + 100M Offers + 1-Person/1-Billion Company) — B2 Superman +
  JohnJones + WonderWoman, B3 Guardians of the Galaxy + Illuminati + Thunderbolts
- **T3** (365 Conformité + R&D External Discovery) — B2 Aquaman + Cyborg,
  B3 Eternals + Kang Dynasty

**Ce qui a été livré.** 137 fichiers .md, datés majoritairement 2026-07-15
(snapshot récent cohérent). La structure de production suit un cycle
**Phase 1 BMad → Phase 2 Gstack** par triptyque : 3 chartes (Mission + DoD +
Squad Dispatch) puis 3 runbooks (M1-M2, M3-M4, M5-M6) par Rock. Runbook D
(date 2026-07-15) adresse Phase D Référentiels : 11/14 views live branche
sprint 2026-06-20, héritage `lib/constants.ts` à éradiquer, ADR-CRUD-VIEWS
manquant à créer. Runbook C adresse Phase C SaaS Auth : AuthProvider,
useOrg(), JWT hook Cloud via Supabase. 24 chartes cycle 2 (T1-T3) couvrent
les sous-domaines (PRD, SOP canon, billing Stripe, ABM LinkedIn, AI Bill
of Rights, etc.).

**Ce qui ne l'a pas été.** Différence structurelle avec les 4 projets
Summer's Verse : ici, **l'exécution est documentée au niveau runbook**,
avec critères DoD-Una 3 critères et V1-V8 verification runs. La
contrepartie : les **commandes canoniques** (Posture C HITL gated, A0 HITL
flag `enable_picard_runbook_X.flag`) sont déclarées mais pas vérifiées —
Gap-6 du Runbook D le reconnaît. L'ADR-CRUD-VIEWS est **PROPOSED**, jamais
RATIFIED. Le pivot marché US (2026-07-15) invalide les références EUR
historiques sans nettoyer le canon antérieur.

## Doctrine — D4, D6, Spec-Loop

Trois verrous doctrinaux structurent l'écriture des chartes et runbooks :
- **D4 append-only** : aucune ligne canon existante n'est modifiée ;
  toute évolution est un append daté.
- **D6 no-self-contradiction** : un runbook qui détecte une contradiction
  avec un chart ou un AGENTS.md prend la source la plus récente comme
  hypothèse et dénonce la stale. Runbook D applique ce principe contre
  son propre chart Phase D, jugé stale.
- **Spec-Loop** (Polivaev 2026) : le gate A0 = IA spec-lock, pas un
  checkpoint UI humain. Documenté dans W40 §2 — référence externe.

## Liens

- [[triptyque-v4-t1-t2-t3]] — la structure T1/T2/T3
- [[fifty-three-b3-agent-roster]] — la squad 53 agents
- [[eight-domain-avengers-wheel]] — la roue 8-domaines
- [[picard-project-pattern]] — l'origine des chartes/runbooks
- [[b2-business-wheel-harmonization-matrix]] — la matrice 8-domaines transverses

## Note de confiance

**Confirmé par machine.** Le status ACTIVE est lisible dans le frontmatter
du README B3. La structure Triptyque est cohérente à travers les 3
ownerbooks et 24 chartes. La doctrine D4/D6 est appliquée de manière
vérifiable dans le wording des runbooks (M0 honest reality check, etc.).

*Standing : ACTIVE, doctrines verrouillées, exécution couvrant Phase C + D.*
