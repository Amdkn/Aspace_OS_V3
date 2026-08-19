---
type: Concept
title: AaaS Doctrine — 3 ICP variants, 1 prototype de franchise
description: La doctrine AaaS (Agency as a Service) installe une seule usine logicielle (P2 Meta Factory) configurée en 3 variants d'ICP — Solaris (Visuel), Nexus (Donnée/Conformité), Orbiter (Enterprise). 5 tiers de pricing, franchise Built-to-Sell.
tags: [aaas, 3-icp, solaris, nexus, orbiter, pricing, built-to-sell, meta-factory]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: 7-sequences-franchise-2026-07-08
    resource: "30_Business_OS/02_Meta_Factory/outbound/7-sequences-franchise-2026-07-08.md"
    title: 7 Séquences Outbound OMK — 3 Strates × 10 ICPs (Franchise-First)
    last_modified: "2026-07-08"
  - id: 3-sequences-franchise-2026-07-08
    resource: "30_Business_OS/02_Meta_Factory/outbound/3-sequences-franchise-2026-07-08.md"
    title: 3 Séquences Outbound OMK — Pitch Franchise-First
    last_modified: "2026-07-08"
  - id: ADR-L2-AAAS-001
    resource: "30_Business_OS/02_Meta_Factory/outbound/3-sequences-franchise-2026-07-08.md (référencé)"
    title: ADR-L2-AAAS-001 — AaaS Doctrine
    last_modified: "2026-06-21"
okf_version: "0.2"
---

# AaaS Doctrine — 3 ICP variants, 1 prototype de franchise

> **Une seule chose à retenir.** P2 Meta Factory est **une seule usine logicielle** configurée en **3 variants d'ICP** (Solaris, Nexus, Orbiter) sur **5 tiers de pricing** (T1-T5). Le pivot doctrinal : on vend la franchise Built-to-Sell, pas la tuyauterie.

## Énoncé canonique (P2 Meta Factory)

> 3 Variants distincts, 1 prototype de franchise (D1) : P2 Meta Factory = la même usine configurée différemment. La cohérence du discours est l'anti-pitch-dégénéré. (`3-sequences-franchise-2026-07-08.md` § "3 séquences, ce qui est commun")

## Les 3 ICP variants

| ICP      | Profil canon                                              | Tier d'entrée        | Tier haut de gamme |
|----------|-----------------------------------------------------------|----------------------|--------------------|
| **Solaris** | Visual First / DAM — persona designer premium 5-25K   | T1 PME Solo Founder ($300-500/an) | T3 PME Groupe ($4-5K/an) |
| **Nexus**   | Data-First / Expert Knowledge — expert méthodique + conformité (avocats, experts-comptables, family offices, cliniques) | T4 Nexus Pro ($30-50K/an) | T4-T5 (T5 Orbiter Enterprise pour gros dossiers) |
| **Orbiter** | Enterprise — cabinets d'enablement à $100K+             | T4 Nexus Pro          | T5 Orbiter Enterprise ($100K-250K/an) |

## Les 5 tiers canoniques (ADR-AAAS-PRICING-001, 2026-06-24)

| Tier                | Prix/an          | Cible                                       |
|---------------------|------------------|---------------------------------------------|
| T1 PME Solo Founder | $300-500         | Solo sans track record                      |
| T2 PME Solo Standard| $500-1000        | Solo installé                               |
| T3 PME Groupe       | $4 000-5 000     | Cabinet multi-partners (10+ clients)        |
| T4 Nexus Pro        | $30 000-50 000   | Grand compte, conformité, multi-tenant      |
| T5 Orbiter Enterprise| $100 000-250 000 | Tier enterprise, IP-as-software              |

**Extension multi-tenant** : isolation RLS par tenant à **$150/tenant/mois** (à confirmer pricing canon — flaggé en attente).

## Ce qui ne change jamais (D4 — invariants)

1. **Aucune mention du coût API.** Jamais. C'est une preuve technique, pas le pitch.
2. **Le Pitch = la propriété intellectuelle du client, softwarelisée.** Toujours, sans exception. L'OS ne remplace pas le coach/l'agence/le COO — il softwarelise ce qu'ils vendaient en heures.
3. **Tier canon ancré** sur `ADR-AAAS-PRICING-001` (D1 receipts).
4. **POC 30 jours, install < 10 jours** = AIDA-Action.
5. **3 Variants distincts, 1 prototype de franchise** (D1) — cohérence du discours.
6. **Liens canon présents** : `ADR-OMK-PRODUCTS-001`, `ADR-NEXUS-10-ICP-001`, sister Solaris/Orbiter.
7. **Filtre §7 PRD strict** : pas de pitch local-first 0,01$ (différé 2027), pas de chiffres non sourcés, pas de features inventées, pas de dissolution du veto Beth.

## Pourquoi cette doctrine

- **Anti-illusion de token-cost.** Un prospect qui négocie sur les tokens se positionne comme acheteur d'utilitaire, pas comme acquéreur de franchise. La doctrine refuse cette conversion (`7-sequences-franchise-2026-07-08.md` §A1 "Aucune mention du coût API").
- **Built-to-Sell comme test.** Si le client ne peut pas revendre l'OS, ce n'est pas un T3-T5 — c'est un T1-T2 « chasseur de rabais » (`7-sequences-franchise-2026-07-08.md` § "Doctrine commune").
- **Matière noire sémantique = capital.** « La matière noire sémantique accumulée par les agences leaders devient leur actif le plus difficile à répliquer — et paradoxalement le plus exposé à la disruption LLM cloud. » Le pitch transforme cette exposition en valeur de revente.

## Ce que ce n'est pas

- Pas une marketplace d'OS. P2 Meta Factory est une usine, pas un annuaire.
- Pas une tarification au token. Les tiers sont forfaitaires, ancrés sur l'ICP, pas sur l'usage API.
- Pas un pitch utilitaire. Le rêve (Built-to-Sell) prime sur la preuve (déterminisme Mirofish).

## Conséquence opérationnelle

Un prospect qui demande le coût API **est filtré** : soit on le relit ensemble, soit on l'écarte (T3-T5 ROI > T1-T2 « chasseur de rabais »). Le filtre est non-négociable.
