---
source: A0_Amadeus + Ops doctrine (Batman) + OFFER_GRANDSLAM + SDD-007 Asset-First
date: 2026-06-03
type: delivery_sop
domain: L2_Business / Ops / Project 00 Agency as a Service / Mode Solaris
status: DRAFT_V1
tags: [#ops #batman #delivery #sop #solaris #zero_jerry #sla #genesis_sprint #picard]
---

# ⚙️ Delivery SOP — Solaris AaaS (zero-Jerry)

> Companion to `JTBD-001_AAAS_DELIVERY_SOP.md`. The repeatable delivery that lets Sales sell the **result**, not
> the hours (S5/S6). North Star Ops : **livraison reproductible, livrée par le mesh d'agents** (objectif flagship
> "$10K MRR sans dépendance Jerry sur la livraison"). Doctrine : Batman (SOP/repeatability), E-Myth (work ON not IN).

## 1. Les 2 SOP (un par tier de la value ladder)

### SOP-A — Content Forge (premium, high-touch)
1. **Genesis Sprint (setup)** : install de l'instance Solaris client (≤10j hyp.) — provisioning (IT), config des 4 couches Asset-First, ingestion brand-context (RAG), calibrage du SLA 2-rounds.
2. **Run** : pipeline **Brief → Concept → Production → Validation (Art Director agent) → Livraison**, révisions plafonnées **2 rounds** (le SLA). Asset Librarian versionne/nomme/dé-doublonne.
3. **Boucle** : feedback hebdo (cas client documenté), expand/share-of-wallet.

### SOP-B — Solaris Lite (self-service, low-touch)
1. **Onboarding self-service** (~0 humain) : signup → instance Lite auto-provisionnée → ingestion brand-context guidée.
2. **Run** : même pipeline, SLA simplifié, Compute plafonné. Support async (People PE23).

## 2. Le principe zero-Jerry (E-Myth + People PE25)
Chaque étape qui peut être faite par un agent (Librarian, Art Director, orchestration Batman) **doit** l'être —
l'humain dirige (création/relation client), le mesh exécute. Le Genesis Sprint lui-même se systématise vers un
template reproductible (moins de touch à chaque client). Buy-back du temps fondateur = le mesh.

## 3. Deployment Ops (le produit lui-même)
- **CI/CD** : GitHub `Amdkn/00-Solaris` → build Next.js → déploiement Vercel (landing) | **Dokploy bare-metal** (instance souveraine — l'angle AAA). (Cf. IT runtime boundary.)
- **Gate de livraison (Batman)** : aucune promesse publique ne scale avant que la SOP de livraison du tier soit prouvée (le "Ops launch gate" du VOC).

## 4. Dettes / dépendances
- ⏳ Le **MVP dashboard** (Product) doit exister pour que SOP-A/B soient exécutables au-delà de la landing.
- ⏳ **Mesurer le temps réel** d'un Genesis Sprint + d'un cycle de révision (pour le SLA + le COGS Finance).
- Révisions >2 rounds = exception facturée (boundary Finance/Legal).

## Prochains pas
1. Détailler SOP-A étape par étape en SOP exécutable (checklist + owners agents).
2. Chiffrer le temps/Compute par étape → alimente Finance (COGS) + le SLA.
3. Définir le Ops launch gate (critères PASS) avant scale acquisition.

## Sources
- Asset-First 4 couches : SDD-007 §3.2. Offre/SLA : `OFFER_GRANDSLAM_SOLARIS_CONTENT_FORGE.md`.
- Doctrine Ops : `04_Ops_Batman_Fantastic4/03_BATMAN_OPS_PRINCIPLES.md`. Modèle marge : `…/06_Finance/AAAS_PRICE_MARGIN_MODEL_SOLARIS.md`.
