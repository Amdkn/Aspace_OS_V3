---
source: A0_Amadeus (built artifact) + Product doctrine (Flash) + picard_audit_solaris + OFFER_GRANDSLAM
date: 2026-06-03
type: product_mvp_demo_boundary
domain: L2_Business / Product / Project 00 Agency as a Service / Mode Solaris
status: DRAFT_V1
tags: [#product #flash #mvp #demo #boundary #solaris #landing #saas_dashboard #nextjs #picard]
---

# 🟢 Product MVP & Demo Boundary — Solaris AaaS

> Companion to `JTBD-001_AAAS_MVP_DEMO_BOUNDARY.md`. Structures what is **built**, what the product **promises**,
> and the **boundary** between the marketing demo and the real deliverable (so we never sell what Ops/IT can't ship).
> Doctrine: Flash (ship fast, promise = deliverable), Built-to-Sell, S15/S20 (no over-promise).

## 1. What is actually built (real artifact)
- **Landing page** : Next.js 16 + React 19 + TypeScript app `01_solaris-aaas/`, committed to **`github.com/Amdkn/00-Solaris`** (commit `5d04494`).
  Sections : Hero · Hook · Paradigm · **Archetype** (les 4 archétypes d'agences) · Anatomy (SOA/SOC/SLA) · **MarginShield** (la douleur 80%) · Wheel (8 domaines) · Vault · FinalCTA · Footer. Diagrammes interactifs (DomainWheel, MarginShield, OrbitalDiagram, RoutingTerminal). Design 8/10, contenu 9/10 (audit Picard 2026-05-17).
- **État** : deployment-ready (dettes CRITICAL D01-D05 du prototype résolues par la migration Next.js + GitHub). Cible déploiement : Vercel (landing) | Dokploy (instance souveraine).

## 2. Promise ↔ Product fit (le contrat à tenir)
La landing **promet** (donc Ops/IT/Legal doivent pouvoir tenir) :
| Promesse landing | Doit être livré par | Garde-fou |
|---|---|---|
| **−80% de margin-bleed** / SLA 2-rounds | Ops SOP + SLA (Compute fixe) | Legal (claim à substantier, L24/L25) |
| 5× volume d'assets on-brand | le SaaS dashboard (Asset Librarian + Art Director) | Product MVP scope ci-dessous |
| Système propriétaire SOA/SOC/SLA | IT runtime + le Master SOC | ne pas vendre une démo comme du réel |
| Garantie 60j | — | Legal valide la clause (L25) |

## 3. La frontière MVP : landing (vend) ≠ dashboard SaaS (livre)
- **Landing = surface marketing/démo** (existe ✅) — convertit l'agence (hameçon Doctor Frame).
- **SaaS Dashboard = le produit réel** (à border / MVP suivant) : l'instance Solaris que l'agence *utilise* —
  les 4 couches Asset-First (SDD-007) : Mémoire des Assets (Librarian) · Validation (Art Director agent) ·
  Orchestration projet (Batman) · Croissance. **MVP minimal** = Couche 0+1 (versioning assets + pré-validation
  livrables sous SLA 2-rounds) — c'est le cœur qui tue le margin-bleed.
- **Boundary rule (Flash)** : on ne montre dans la démo que ce qui sera livrable au tier vendu ; pas de vaporware.

## 4. Dettes Product restantes (audit, post-migration)
- 🟠 **D09 backend form** : les CTA ("submit your url", "contact the factory") n'ont pas d'endpoint → pas de capture lead. **Bloquant business** (Growth ne peut pas collecter). → IT (runtime/API).
- 🟡 D12 tests · D14 TweaksPanel exclu du bundle prod · D13 OG/manifest.

## Prochains pas
1. Border le **MVP dashboard** (Couche 0+1 d'abord) — scope minimal qui prouve la promesse −80%.
2. Brancher le **form backend** (lead capture) — débloque Growth.
3. Valider promise↔deliverable avec Ops (SOP) + Legal (claims).

## Sources
- Artifact : `…/03_Product_Flash_Avengers/01_solaris-aaas/` + `picard_audit_solaris.md` + GitHub `Amdkn/00-Solaris`.
- Offre/ICP : `OFFER_GRANDSLAM_SOLARIS_CONTENT_FORGE.md` + `SOLARIS_ICP_MARKET_STUDY_2026.md`. Backbone : SDD-007.
