---
type: Concept
title: Citadel Architecture — 3 ICP + 3 engines + 1 Kadreec
description: Architecture AaaS pivot 2026-06-21 : 3 ICP (Solaris/Nexus/Orbiter) × 3 engines (ICP-driven / Sales-Enablement / Zero-PII) × 1 Kadreec. Chaque ICP est ratifié par un ADR-ICP dédié.
tags: [citadel, 3-ICP, 3-engines, kadreec, sales-enablement, zero-PII]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture_v2, at: 2026-08-19 }
sources:
  - id: PRODUCT_v2
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/sob/PRODUCT.md
    title: PRODUCT.md
    last_modified: 2026-07-20
  - id: ROADMAP_DEAL_12WY
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md
    title: ROADMAP D.E.A.L
    last_modified: 2026-07-19
okf_version: "0.2"
---

# Citadel Architecture — 3 ICP + 3 engines + 1 Kadreec

## Énoncé

L'architecture AaaS pivote en 2026-06-21 vers une **Citadel** structurée en 3 ICP × 3 engines × 1 Kadreec. Chaque ICP est ratifié par un ADR-ICP dédié.

## Les 3 ICP

| ICP | Persona | Niche | Pricing | ADR |
|-----|---------|-------|---------|-----|
| **Solaris** | Flux / Image | Outreach automation | $XX/instance | ADR-ICP-SOLARIS-001 |
| **Nexus** | Donnée froide / Conformité | Coach premium / Citadelle | $1 000/mois | ADR-ICP-NEXUS-001 |
| **Orbiter** | Terrain | Sales-Enablement | $XX/instance | ADR-ICP-ORBITER-001 |

## Les 3 engines

| Engine | Couche A'Space | Fonction |
|--------|----------------|----------|
| **ICP-driven** | Sirius (3-ICP canon) | Pilote l'orientation par ICP |
| **Sales-Enablement** | Orbiter | Pipeline qualifié, relances autonomes |
| **Zero-PII** | Nexus | Instance privée, RGPD, audit en 1 query |

## Le Kadreec

Le **Kadreec** est l'orchestrateur unique qui coordonne les 3 engines. C'est l'équivalent Citadel du **Coach OS** (couche L1) : il arbitre, dispatch, vérifie.

## Cycle 2 — Prototype GTM

Le Rock R1 du 12WY-02 cible **30 comptes Strate B US attaqués, 3 variants nichés live** :
- **Solaris Outbound** (Solaris engine)
- **Nexus Conformité** (Nexus engine, Zero-PII)
- **Orbiter Sales-Enablement** (Orbiter engine)

Pipeline ≥ 30 comptes stage-aware.

## Pricing canon

Grille 5 tiers (ADR-AAAS-PRICING-001 RATIFIED) : $300-500/an intro → Tier 5 $50K MRR.
Le spearhead coach entre par la baseline 1000$/mois (Nexus), l'expansion multi-tenant vient au Cycle 3.

## Convergences

- **Pattern DEAL** : Definition (cible ICP) → Elimination (rejet explicite des niches régulées) → Automation (3 engines) → Liberation (Kadreec arbitre).
- **Pattern Vessels** : Solaris = Orville (flux), Nexus = Discovery (vision), Orbiter = SNW (execution).
- **Pattern Heka** : la parole crée le réel. Le Kadreec prononce l'orientation, les 3 engines matérialisent.

## Anti-pattern

- Mélanger les ICP (un client Solaris ne paie pas Nexus — prix différents)
- Lancer les 3 engines simultanément (chaque engine a son backlog Kadreec)
- Confondre Citadel (architecture) et Kadreec (orchestrateur) — ils sont distincts

## Canon futur

Le pivot 2026-06-21 a sélectionné Kadreec comme arbitre central. ADR-OMK-001/002/003 documentent l'orchestration. La cadence 12WY-02 mesure le succès de chaque triplet (ICP × engine × niche).
