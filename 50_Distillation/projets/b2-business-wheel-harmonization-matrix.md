---
type: Concept
title: B2 Business Wheel Harmonization Matrix
description: Matrice 8-domaines transverses GROWTH/SALES/PRODUCT/OPS/IT/FINANCE/PEOPLE/LEGAL — chacun avec un gate READY/NEEDS/BLOCKED à franchir avant qu'une motion devienne publique, contractuelle ou data-bearing.
tags: [concept, b2, matrice, gates, transverse, harmonization, eight-domain]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraire_substrat_rdf, at: 2026-08-17T19:50:00Z }
  - { by: process:lecture_concepts_picard, at: 2026-08-17T21:00:00Z }
sources:
  - id: matrix-abc
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/02 ABC OS & Child Care BOS/B2_Business_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md"
    title: Matrix ABC (status SHADOW_ACTIVE, 2026-06-02)
    last_modified: 2026-06-02
  - id: matrix-rilcot
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/03_RILCOT_Members_Space_OS/B2_Business_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md"
    title: Matrix RILCOT (status SHADOW_ACTIVE, 2026-06-02)
    last_modified: 2026-06-02
  - id: matrix-alikaly
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/04 Alikaly Bana Holding to LLC/B2_Business_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md"
    title: Matrix Alikaly (status SHADOW_ACTIVE, 2026-06-02)
    last_modified: 2026-06-02
  - id: matrix-marina
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/05 marina Cleaning BOS & SOP/B2_Business_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md"
    title: Matrix Marina (status SHADOW_ACTIVE, 2026-06-02)
    last_modified: 2026-06-02
okf_version: "0.2"
---

# B2 Business Wheel Harmonization Matrix

## Définition

Matrice qui **prévient qu'un domaine fort en masque un faible**. Présente
dans les 4 projets Summer's Verse (ABC, RILCOT, Alikaly, Marina) — 4
fichiers identiques à 30 mots près, status **SHADOW_ACTIVE** au
2026-06-02. Le `surface` varie (`02_ABC_OS`, `03_RILCOT`, `04_Alikaly`,
`05_Marina`), le contenu est une copie.

## Structure — deux niveaux

### 1. Paire-checks (début de matrice)

| Paire | Question | Escalade si unresolved |
|-------|----------|------------------------|
| Growth + Sales | Attention devient-elle opportunité qualifiée ? | B2 Council |
| Sales + Ops | Les promesses sont-elles livrables repeatedly ? | B2 Council |
| Product + Ops | L'artefact est-il opérationnellement supportable ? | B2 Council |
| Product + IT | Le produit run, deploy, recover, access ? | B2 Council |
| Finance + Growth | Le spend est-il justifié par learning/traction ? | B2 Council |
| Finance + Product | Build cost protège-t-il margin ? | B2 Council |
| Legal + Growth | Les claims sont safe ? | B2 Council |
| Legal + Product | IP/privacy/terms boundaries sont-ils clairs ? | B2 Council |
| People + All | Ownership et load sont sustainable ? | B2 Council ou B1 si structurel |

### 2. Transverse gates (par domaine)

Chaque B2 owner porte un **gate** que toute motion doit franchir avant
de devenir publique, contractuelle, ou data-bearing. Le gate émet
trois signaux : **READY** / **NEEDS_xxx** / **BLOCKED_xxx**.

| Domaine | Owner | Question pivot | Émet |
|---------|-------|----------------|------|
| **Ops/Transverse** | Batman | Phase livraison, owner, risque, rollback, date review | `LAUNCH_READY` |
| **People** | GreenLantern | B2 owner nommé, B3 agent nommé, decision rights, capacity, proof path, escalation | `ASSIGNED` / `NEEDS_OWNER` / `DLQ` |
| **IT** | Cyborg | System owner, access boundary, source of truth, data boundary, automation, rollback | `SYSTEM_READY` / `NEEDS_SYSTEM_OWNER` / `QUARANTINE` |
| **Growth** | Superman | VOC evidence, ICP narrow, promise boundary, measurement, budget, owner, claim-safe | `GROWTH_READY` / `NEEDS_SIGNAL` / `BLOCKED_PROMISE` |
| **Legal** | Aquaman | Claim boundary, data/privacy, IP/deliverable, terms/liability, authority, escalation | `LEGAL_READY` / `NEEDS_REVIEW` / `BLOCKED_RISK` |
| **Finance** | WonderWoman | Price/budget, cost model, margin/cash, refund, approval, leakage | `FINANCE_READY` / `NEEDS_MODEL` / `BLOCKED_LEAKAGE` |
| **Sales** | Martian Manhunter | Diagnostic, scope, delivery feasible, price/terms approved, handoff | `SALES_READY` / `NEEDS_QUALIFICATION` / `BLOCKED_COMMITMENT` |
| **Product** | Flash | Scope explicit, exclusions, acceptance, runtime/economics, ownership/legal | `PRODUCT_READY` / `NEEDS_SCOPE` / `BLOCKED_DELIVERY` |

## Règle de blocage

**Ops Transverse Gate** est le dernier verrou. Un projet entier est
**BLOCKED** si Ops ne peut pas nommer : phase livraison, owner, risque,
rollback, date review. Domaines individuels peuvent être `CONDITIONAL`,
mais l'ensemble ne lance pas sans Ops.

**Contrainte spécifique ABC** : "Childcare work cannot launch unless
compliance, people load, and field delivery procedures are explicit."

## Red flag combinations

- Product green, Ops/IT red → **do not launch**
- Growth green, Sales red → validate offer avant scaling attention
- Sales green, Ops/People red → delivery load risk
- Finance red et Growth/Product green → slow down or reprice
- Legal red avec public-facing work → **hold claims and launch**

## Trois statuts, trois lectures

Le frontmatter `status: SHADOW_ACTIVE` est intéressant. Le commentaire
canonique du projet 01-omk-business-os utilise le terme **`STATUS`**
différemment : `READY / DRAFT_V1 / REVIEW_READY / GRADUATED / PHASE_1_STUB
/ SHADOW_ACTIVE`. La matrice est **SHADOW_ACTIVE** parce qu'elle est
**définie mais pas exécutée** — c'est le pendant de GRADUATED : la
matrice est l'armature de gating, mais aucun gate READY/BLOCKED émis
n'est tracé dans le corpus.

## Liens

- [[eight-domain-avengers-wheel]] — les 8 domaines qui portent les gates
- [[summers-verse-framework]] — la trame B1/B2/B3 qui consume les gates
- [[picard-project-pattern]] — l'audit qui précède les gates
- [[abc-os-child-care-bos]] / [[rilcot-members-space-os]] / [[alikaly-bana-holding-llc]] / [[marina-cleaning-bos-sop]] — les 4 projets où la matrice est dupliquée

## Note de confiance

**Confirmé par machine.** 4 fichiers identiques à 30 mots près. Le
frontmatter SHADOW_ACTIVE est cohérent et n'est pas en contradiction
avec le GRADUATED des manifests — c'est un statut différent (matrice
définie vs projet structuré).

*Standing : matrice définie dans 4 projets, aucun gate READY/BLOCKED émis tracé.*
