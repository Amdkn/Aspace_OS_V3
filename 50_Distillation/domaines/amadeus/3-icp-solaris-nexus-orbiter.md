---
type: Concept
title: Architecture 3-ICP — Solaris / Nexus / Orbiter
description: 3 variants de l'AaaS positionnés sur des niches disjointes. Solaris = flux/image, Nexus = donnée froide/conformité, Orbiter = terrain. Pilotés chacun par un ADR-ICP dédié.
tags: [3-ICP, AaaS, Solaris, Nexus, Orbiter, ADR-ICP, niches]
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

# Architecture 3-ICP — Solaris / Nexus / Orbiter

## Énoncé

L'architecture AaaS A'Space est structurée en **3 variants ICP** positionnés sur des niches **disjointes** :

| Variant | Niches | Caractérisation |
|---------|--------|-----------------|
| **Solaris** | flux / image | Outbound — Solaris Outbound |
| **Nexus** | donnée froide, critique, confidentielle | Conformité — Nexus Conformité |
| **Orbiter** | terrain | Sales-Enablement — Orbiter Terrain |

## Cycle 2 — Prototype GTM

Le Rock R1 du 12WY-02 cible **30 comptes Strate B US attaqués, 3 variants nichés live** :
- **Solaris Outbound**
- **Nexus Conformité**
- **Orbiter Sales-Enablement**

Métrique : pipeline ≥ 30 comptes stage-aware.

## Pourquoi 3

1. **Risk-spread** — un variant qui pivote ne tue pas le reste
2. **Specificity** — chaque ICP a sa propre verticale, son propre funnel, son propre pricing
3. **Compounding** — la team apprend 3 postures de vente simultanément

## Solarplexus (terme convergent)

Le takeout 2026-05 mentionne « **Solaris OS** » comme « produit AaaS flagship, sister ADR-ICP-SOLARIS-001 RATIFIED 2026-06-24 ». Solaris OS est probablement l'ancien nom de Solaris (variant flux/image) avant le rename final en 3-ICP.

## Notes de cohérence

- **Nexus** = OMK Nexus (pilier 4, ADR-ICP-NEXUS-001 RATIFIED 2026-06-24)
- **ADRs scope** : `ADR-ICP-SOLARIS-001`, `ADR-ICP-NEXUS-001`, `ADR-ICP-ORBITER-001`
- **Clone de la doctrine AaaS** : ADR-L2-AAAS-001
- **Clone de la niche Nexus** : ADR-NEXUS-NICHE-001
- **Clone du pricing** : ADR-AAAS-PRICING-001 (5 tiers canon)

## Anti-pattern

Créer un 4ᵉ variant. Chaque variant coûte 3 Rocks d'observation par cycle. La cadence 12WY ne tolère pas l'éparpillement.
