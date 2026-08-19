---
type: Concept
title: Famille OMK — 9 ADR OMK Dashboard, pivot Dokploy → Vercel
description: La famille OMK (9 ADR) documente l'architecture du OMK Dashboard (Vite 6 + React 19 + TS 5.8 + Tailwind v4). Le pivot Dokploy → Vercel du 2026-06-19 a partiellement supersedé l'architecture initiale.
tags: [adr, omk, dashboard, dokploy, vercel, pivot]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-OMK-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-OMK-001_dual-product-dashboard-multitenant_RATIFIED.md"
    title: OMK 001 Dual-Product (Dokploy, RATIFIED puis AMENDED)
    last_modified: "2026-06-11"
  - id: ADR-OMK-004
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-OMK-004_pivot-supabase-cloud-vercel.md"
    title: OMK 004 Pivot Supabase Cloud + Vercel
    last_modified: "2026-06-19"
  - id: ADR-OMK-005
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-OMK-005_tenant-isolation-guard.md"
    title: OMK 005 Tenant Isolation Guard
    last_modified: "2026-07-26"
  - id: ADR-OMK-NEXUS-TRANSFORM-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-OMK-NEXUS-TRANSFORM-001_omk-to-nexus-pivot.md"
    title: OMK Nexus Transform (OMK → Nexus)
    last_modified: "2026-07-26"
okf_version: "0.2"
---

# Famille OMK — 9 ADR OMK Dashboard, pivot Dokploy → Vercel

## Résumé

La famille **OMK** (9 ADR) documente l'architecture du **OMK Dashboard** (`apps/dashboard/`) — un codebase Vite 6 + React 19 + TS 5.8 + Tailwind v4 qui sert deux produits (internal + SaaS) puis, après pivot, un seul produit SaaS sur Vercel.

## Les 9 ADR OMK

| ADR | Sujet | Statut |
|---|---|---|
| `ADR-OMK-001` | Dual-Product Deployment (Dokploy) | RATIFIED 2026-06-11, AMENDED 2026-06-19 |
| `ADR-OMK-002` | PG Roles Provisioning | RATIFIED |
| `ADR-OMK-003` | MCP Supabase aspace | en rédaction |
| `ADR-OMK-004` | Pivot Supabase Cloud + Vercel | RATIFIED 2026-06-19 |
| `ADR-OMK-005` | Tenant Isolation Guard | en validation |
| `ADR-OMK-MULTICA-001` | Mission Control Multica replaces Plane | RATIFIED |
| `ADR-OMK-NEXUS-TRANSFORM-001` | OMK → Nexus pivot | RATIFIED |
| `ADR-OMK-PRODUCTS-001` | OMK 3 products vertical franchise | RATIFIED |
| `ADR-OMK-NEXUS-TRANSFORM-001` | (doublon — voir collisions) | |

## Le pivot 2026-06-19

`ADR-OMK-004` (RATIFIED 2026-06-19 par A0) **supersede partiellement** :

- `ADR-OMK-001` §Deploy D1-D4 (Dokploy → Vercel)
- `ADR-SUPABASE-001` §Hosting (self-host VPS → Supabase Cloud)

Et **amende** `ADR-OMK-001` §runtime : single-mode SaaS only (`VITE_APP_MODE=saas`), le mode `internal` est retiré (Condition A = A1 LOCKED).

C'est l'exemple type du **supersedes partiel** : `ADR-OMK-001` reste canonique pour son §runtime amendé, mais son §Deploy est mort. La règle canon est `D4 append-only` : on n'efface pas, on annote.

## La transformation OMK → Nexus

`ADR-OMK-NEXUS-TRANSFORM-001` marque la transformation du produit OMK en produit Nexus. OMK n'est plus un produit, c'est une marque interne de la plateforme Nexus.

## Les collisions

`ADR-OMK-NEXUS-TRANSFORM-001` apparaît **deux fois** dans le corpus. Aucun mécanisme de dédoublonnage n'a été trouvé.

## Statut vis-à-vis de V3

- **ADR-OMK-001** : **synthese-datee**. §Deploy mort, §runtime amendé. La copie `_TRASH/superseded/` est la trace historique.
- **ADR-OMK-004** : **canon**. Le pivot est la référence actuelle.
- **ADR-OMK-005** : **canon** (en cours de validation finale).
- **ADR-OMK-NEXUS-TRANSFORM-001** : **canon**.

## Le verdict de cette distillation

**mixte**. La famille OMK illustre le mieux le pattern append-only : un pivot complet sans réécriture du corps de l'ADR originel.

## Liens

- Voir aussi : `concept-supersedes-partial.md` (les supersedes partiels)
- Voir aussi : `concept-amend-pattern.md` (le pattern AMEND)
- Voir aussi : `concept-famille-l2-business.md` (le contexte L2)