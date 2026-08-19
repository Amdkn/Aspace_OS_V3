---
type: Concept
title: Cycle 12WY — l'ascendeur de cadence (4 cycles / 12 Rocks / 48 sprints / 240 scrums)
description: Cadence canonique d'A'Space OS : 4 cycles 12 semaines (12WY-01 Fondations → 12WY-04 Souveraineté), 3 Rocks par cycle, 4 sprints par Rock, 5 scrums par sprint. Échelle ARR ×10 par cycle.
tags: [12WY, cadence, roadmap, cycle, rocks, sprints, scrums, picard, summers]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture_v2, at: 2026-08-19 }
sources:
  - id: ROADMAP_DEAL_12WY
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md
    title: ROADMAP D.E.A.L — 4 Cycles 12WY · 20/07/2026 → 20/07/2027
    last_modified: 2026-07-19
okf_version: "0.2"
---

# Cycle 12WY — l'ascendeur de cadence

## Énoncé

4 cycles de 12 semaines chacun. Chaque cycle = 3 Rocks (1 par mois). Chaque Rock = 4 sprints. Chaque sprint = 5 scrums. **Total annuel : 4 cycles · 12 Rocks · 48 sprints · 240 scrums.**

## Les 4 cycles (2026-07-20 → 2027-07-20)

| Cycle | Fenêtre W1-W12 | W13 review | Thème | Cible MRR fin de cycle |
|-------|----------------|------------|-------|------------------------|
| **12WY-01 Fondations** | 20/07 → 11/10/2026 | 12-18/10 | Durcissement infra + premiers clients | **10 clients · $10K MRR** |
| **12WY-02 Prototype GTM** | 19/10/2026 → 10/01/2027 | 11-17/01 | Attaque Strate B US (30 comptes cibles) | **100 clients · $100K MRR** |
| **12WY-03 Multi-Tenant** | 18/01 → 11/04/2027 | 12-18/04 | Expansion RLS + viralité fondateurs | **1 000 clients · $1M MRR** |
| **12WY-04 Souveraineté** | 19/04 → 11/07/2027 | 12-18/07 | Franchise + R&D locale (réinvestissement) | **×10 + IP propriétaire** |

Échelle **×10 par cycle**. Le milliard est l'asymptote H10 ; la trajectoire annuelle vit sur cette échelle.

## Cascade d'autorité

```
PICARD (A3)          1 vision/cycle    → décompose le cycle en 3 Rocks
   ▼
SUMMERS (B1)         1 Rock/mois       → traduit le Rock en directives par domaine
   ▼
8 B2 · 3T            4 Sprints/mois    → chaque manager tient le sprint de son domaine
   ▼
B3 SQUADS            5 Daily Scrums/sprint → exécution, receipts SQL
   ▲
UPLINK               5 scrums → 1 sprint review → 4 sprints → 1 Rock review
                     → 3 Rocks → 1 cycle review Picard → 4 cycles → bilan annuel
```

## Les 4 sprints-type du mois (8 B2 × Triptyque V4)

| Sprint | T1 — RH Agentique / Operation / Product | T2 — Growth / Sales / Finance | T3 — Legal / R&D / Uplink |
|--------|---------------------------------------|-----------------------------|----------------------------|
| **S1 Build** | staffer agents du Rock · SOP du mois | liste de cibles fraîche · script d'approche | conformité de l'offre · veille |
| **S2 Push** | automatiser le répétitif détecté en S1 | outreach volume plein · démos bookées | contrats types prêts |
| **S3 Close** | fiabiliser ce qui casse sous charge | closing · onboarding des signés | audit RLS/data des nouveaux clients |
| **S4 Harvest** | dette technique du mois purgée | métriques cohortes · NRR | uplink consolidé → dossier Rock suivant |

## Les 5 Daily Scrums

1. **Lire l'état** : requête SQL du domaine (pas de résumé narratif — le chiffre).
2. **1 action de conversion** : la tâche qui rapproche le MRR, en premier.
3. **1 action de système** : la tâche qui rend demain plus automatique.
4. **Receipt** : le delta SQL avant/après, loggé.
5. **Uplink 1 ligne** : au B2 du domaine. 5 lignes = matière du sprint review.

## Règle unique

**Chaque niveau ne remonte que du chiffré.** Un scrum sans receipt SQL n'existe pas. Un sprint sans delta MRR/pipeline n'existe pas. Un Rock sans métrique atteinte se re-scope au mois suivant — la cadence, elle, ne s'arrête jamais.
