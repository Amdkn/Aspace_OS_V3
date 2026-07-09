---
id: ADR-OMK-PRODUCTS-001
title: OMK 3 Produits — Ligne Verticale de Franchise (BOS Harness → Meta Factory White-Label → R&D Souverain), variants ICP nichés dans P2
type: ADR (Architectural Decision Record)
status: RATIFIED 2026-07-09 by Amadeus (Jumeau Numérique A0) — sisters ADR-L2-AAAS-001 + ADR-ICP-{SOLARIS,NEXUS,ORBITER}-001 + ADR-AAAS-PRICING-001 + ADR-MARKET-STUDY-001
date: 2026-07-08
deciders: [A0 Amadeus (Jumeau Numérique)]
drafted_by: A0-Amodei (Murderbot méta-coach) — sur GO A0 (AskUserQuestion : "Ligne verticale + variants dans P2" + "Canon ADR + matrice d'offre")
domain: L2 Business OS / OMK / AaaS / $100M Offer / STP / AIDA / AAARR / Franchise Prototype
tags: [#ADR #omk #aaas #franchise #100M-offer #stp #aida #aaarr #dark-factory #gstack #white-label #meta-factory #jepa #dspark #anti-token-first #built-to-sell #picard #book #summers #jerry]
doctrine_anchors: [ADR-META-001-D1, ADR-META-001-D3, ADR-SOBER-002, ADR-CANON-001, ADR-L2-AAAS-001, ADR-WARMODE-002]
related: [ADR-ICP-SOLARIS-001, ADR-ICP-NEXUS-001, ADR-ICP-ORBITER-001, ADR-AAAS-PRICING-001, ADR-MARKET-STUDY-001_the-builders-2026, "wargames/03-wf2-book-ceo-bench.md", "wargames/28-runpane...decorrele.md", "sim Mirofish wf3_sim_runner.py", "Gstack skills (gstack-cso/gstack-ship/gstack-autoplan)"]
provenance: |
  Née 2026-07-08 du constat A0 : "Deep Research de Gemini n'a pas la vision complète de L2."
  L'étude de marché GTM US de Gemini (30 comptes B1/B2/B3) pitche OMK comme un UTILITAIRE
  d'optimisation de coût (Arbitrage de Jevons, réduction tokens, RLS/PostgreSQL) — la
  "soute technique" — au lieu de l'OS d'entreprise souverain qui industrialise une agence
  artisanale en franchise revendable (Built to Sell). Gemini lui-même s'est auto-corrigé
  (reframe 3 Variants) mais restait sur l'axe ICP. A0 a ajouté un 3e axe : la LIGNE PRODUIT
  (P1 BOS / P2 White-Label / P3 R&D). Cet ADR résout la confusion des trois "3" + la collision
  de nommage "Nexus" (variant vs produit).
sign_off_a0: "ratified 2026-07-09 by Amadeus (Jumeau Numérique A0) via /goal-loop convergence gate G1"
sign_off_pending: false
---

# ADR-OMK-PRODUCTS-001 — OMK 3 Produits : Ligne Verticale de Franchise

## Status

**PROPOSED 2026-07-08** — draft A0-Amodei sur GO A0. Ratification A0 pending (D1 pricing $ à confirmer depuis ADR-AAAS-PRICING-001 ; reformulation des 3 séquences outbound = livrable suivant).

## Context — le piège "token-first" et la confusion des trois "3"

### C1 — Le symptôme (D1, source : étude Gemini partagée CE run)
Le GTM de Gemini vend l'**Axe 0** (la tuyauterie) : « –90 % de facture API », « Arbitrage de Jevons », « RLS PostgreSQL ». Danger nommé par A0 : un prospect (ex. Harrison Vance / Leadium B1) **négocie le forfait à la baisse** ou **attend l'effondrement des prix LLM 2027**. Un OS souverain vendu comme économie de coût est un utilitaire jetable.

### C2 — La cause : trois axes distincts écrasés en un seul
| Axe | Définition | Le "3" | Statut canon |
|---|---|---|---|
| **1 — MARCHÉ** (la douleur) | À qui on vend | B1 SDR/BDR · B2 Growth · B3 Enablement | Cibles Gemini (30 comptes) |
| **2 — VARIANT / ICP** (la face produit) | Comment le produit se présente | Solaris 🎨 Visual/DAM · **Nexus ⚖️ Data/Conformité** · Orbiter 🏗️ Mobile/Terrain | **RATIFIÉ** (ADR-ICP-*) |
| **3 — LIGNE PRODUIT** (business model) | Le degré de maturité/audience | P1 BOS · P2 White-Label · P3 R&D | **Cet ADR** |

Gemini colle Axe 1 = Axe 2 (B1→Solaris…) comme un fait acquis (c'est une **hypothèse à tester**, pas du canon) et ignore l'Axe 3.

### C3 — La collision de nommage
« **Nexus** » désigne à la fois (a) le **VARIANT** Data/Conformité (ADR-ICP-NEXUS-001 ratifié) et (b) le **PRODUIT** white-label ("OMK Nexus Business OS" chez Gemini). Deux référents sous un mot → War Room confuse.

## Decision

### D1 — La ligne verticale de franchise (Axe 3), variants nichés dans P2
OMK est **une seule ligne produit à 3 étages de maturité**, pas 3 produits parallèles ni une matrice 3×3 :

- **P1 — OMK BOS (le Harness d'exécution L2, INTERNE).** L'usine : Dark Factory Gstack en Loop Engineering, **déterminisme structuré par les Simulations Mirofish (`wf3_sim_runner.py`) + les Wargames CEO-Bench (W03)**. C'est le moteur qui produit le travail. Non vendu tel quel — c'est la machine derrière le rideau. Gate anti-paperclip = airlock Beth (B1-réplication = ≥3 Mirofish SOUTENABLE, W28/W29). Sister : ADR-WARMODE-002.
- **P2 — OMK Meta Factory (le White-Label, EXTERNE).** *(nom proposé — résout la collision C3 ; « Nexus » reste le VARIANT.)* Le produit vendu aux **coachs & agences** : P1 packagé en franchise-par-conception. **C'est ICI que vivent les 3 Variants** (Solaris/Nexus/Orbiter) comme 3 configurations d'une même usine. L'agence cliente achète une **usine logicielle à haute marge, revendable** (Built to Sell), pas des tokens.
- **P3 — OMK R&D Souverain (la frontière).** AaaS local souverain : intégration Wargames + SOP dans le **réentraînement DSpark / Recursivemas / Skill-to-JEPA world models** (optimisation IA open-source). Alimente P1/P2 en capacités ; horizon H90+.

```
P1 BOS (moteur interne)  ──packagé──▶  P2 Meta Factory (white-label agences)  ──configuré en──▶  Solaris | Nexus | Orbiter
       ▲                                                                                                    │
       └────────────────── P3 R&D souverain (DSpark/JEPA) nourrit le moteur ◀───────────────────────────────┘
Prototype de Franchise : P1 réplique P2 à l'identique → N clients = N usines franchisées, attention A0 plate.
```

### D2 — Le reframe doctrinal : franchise-first, jamais token-first
Le Jevons / RLS / cache sémantique local = **preuve technique** (la carrosserie), **jamais le pitch** (le désir). Le pitch = *« transforme ton agence de main-d'œuvre en usine logicielle souveraine, scalable et revendable »*. La réduction de coût est un **effet**, pas l'offre.

### D3 — Alignement $100M Offer / STP / AIDA / AAARR
- **$100M Offer (Hormozi)** s'applique à l'**Axe 3** : P2 Meta Factory = l'offre irrésistible (dream outcome = agence → plateforme revendable ; perceived likelihood = déterminisme Mirofish/CEO-Bench ; time delay = POC 30j / install <10j ; effort = clé-en-main Docker).
- **STP** : Segmentation = Axe 1 (B1/B2/B3) · Targeting = les 30 comptes · Positioning = Axe 2 (variant par ICP).
- **AIDA** : Attention = déclencheurs 2026 (recrutements Prompt Eng, stack Gong/Clay) · Interest = franchise vs main-d'œuvre · Desire = Built-to-Sell + souveraineté data · Action = POC 30j.
- **AAARR** : Acquisition (scraping signaux) → Activation (install <10j) → Rétention (**gravité des données** = matière noire sémantique locale, attrition ≈ 0) → Referral (affiliation certifiée Clay/Rev-Arch) → Revenue (forfait récurrent + $150/tenant/mois isolé RLS — *chiffres à confirmer ADR-AAAS-PRICING-001*).
- **Croissance exponentielle déterministe** = le **Prototype de Franchise** (D1) : le déterminisme vient des sims Mirofish + wargames CEO-Bench, pas d'un pari commercial.

## Matrice d'Offre (le livrable réutilisable)

### Vue compacte (3 strates × 3-4 cibles) — la matrice canon, ancre `ADR-NEXUS-10-ICP-001`

> Pour le détail complet (10 cibles / 3 strates / 5 personae), sister canon : [`ADR-NEXUS-10-ICP-001`](./ADR-NEXUS-10-ICP-001_3-strates-10-cibles-canon.md) (RATIFIED 2026-07-08). Cette section résume.

| Strate | Cible canon | Variant P2 | Module-pack (PRD §2) | Tier ancré (D1, ADR-AAAS-PRICING-001) | Tagline franchise-first |
|---|---|---|---|---|---|
| **A1** | Cabinet Coaching C-Suite | Nexus (Conformité) | 1 Audit Sdiri + 2 Wargame process synthèse + **5 DLP** (w05) | T3-T4 ($4K-$50K/an) | « Le Chef de Cabinet IA » |
| **A2** | Leadership Development grand volume | Nexus | 1 Audit + 2 Wargame RAG + 3 CEO-Bench | T4 | « L'Orchestrateur de Cohort » |
| **A3** | Coach M&A / Transition | Nexus (secret professionnel) | **5 DLP** + 1 Audit AI-Act art.12 + 2 Wargame NDA | T4-T5 ($30K-$250K/an) | « Le Sanctuaire de la Transaction » |
| **B1** | Agence SDR/BDR as a Service | Solaris ou Nexus multi-tenant | 1 Quiz simulateur (w07) + 2 Wargame outbound + **5 Gstack** (w09) | T2-T3 | « L'Arbitrage Jevons » |
| **B2** | Growth Marketing native-IA | Nexus *(hypothèse à valider) | 1 Audit étanchéité + 2 Wargame RLS + 5 Gstack | T3-T4 | « Le Harnais Multi-Tenant » |
| **B3** | Sales Enablement | Orbiter ou Nexus stage-aware | 1 Audit transcriptions + 2 Wargame scoring + 3 CEO-Bench | T3-T4 | « L'Évaluateur Stage-Aware » |
| **C1** | Fractional COO ×15 PME | Solaris (Knowledge Bus) | 2 Wargame portfolio + **4 MiroFish** (w08) + Skills/client | T4 | « Le COO-augmented » |
| **C2** | SOP Vaulting | Nexus systématisation | 2 Wargame SOP→Skill + 1 Audit | T3-T4 | « SOPs → Skills exécutables » |
| **C3** | Gestion Patrimoine B2B | Nexus (secret professionnel) | **5 DLP** + 1 Audit conformité + 2 Wargame reporting | T4-T5 | « Le Coffre-Fort Patrimonial » |
| **C4** | Conduite du changement | **Canal Partenaire** (prescripteur) | 4 Sims `/office-hours` (w09 M4) + alliance Built-to-Sell | T4 + rev share | « L'Infrastructure Officielle de la Transformation » |

### RECON héritée (D1, non re-théorisée)
- **B2↔Nexus** = hypothèse Gemini reprise par défaut. Le canon `ADR-ICP-NEXUS-001` (RATIFIED) positionne Nexus sur Conformité → la **Strate A** (A1/A2/A3) et **C3** collent mieux, **B2** (Growth) est plus *Solaris* ou nouveau Variant. À trancher en campagne, pas gravé comme acquis.
- **Variant 4 possible** : si Solaris (Visual) + Nexus (Data) + Orbiter (Mobile) ne couvrent pas B2, créer un variant `Helios` ou `Amplify` (Growth/Marketing natif) — ADR à créer.

> ⚠️ Ce qui suit est l'**ancienne matrice 3-lignes** (Strate B uniquement) que le PRD canon et l'ADR-OMK-PRODUCTS-001 §D1-amendement ont étendue. Conservée pour traçabilité D4 (pas de suppression, append-only).

### Archive — matrice 3-lignes initiale (2026-07-08, avant amendement Strate A + C)
| Sous-niche (Axe 1) | Variant (Axe 2) | Ce que Gemini vend (friction) | Ce qu'OMK livre (valeur franchise) |
|---|---|---|---|
| **B1 Outbound** (Leadium, Whistle, SalesPipe) | **Solaris** 🎨 | Élimination des appels API d'enrichissement | **L'usine d'outreach autonome à forfait fixe** |
| **B2 Growth** (MeghRoop, Avenue Z, NoGood) | **Nexus** ⚖️ | RLS PostgreSQL anti-mélange payloads | **Le hub multi-tenant souverain** |
| **B3 Enablement** (Force Mgmt, Winning by Design, Challenger) | **Orbiter** 🏗️ | Équation vectorielle locale sous Docker | **L'usine d'audit qui logicielise la méthodo dans le CRM** |

## Consequences

**Positif** : (1) sort du piège utilitaire → pricing tenu, pas négocié. (2) Un seul produit à faire mûrir (P1→P2), pas 9 cellules à maintenir. (3) « Nexus » désambiguïsé. (4) Le déterminisme de croissance est *ancré* (Mirofish + CEO-Bench), pas promis.

**À faire (non fait ici, pas caché)** :
- **Renommage P2** : « OMK Meta Factory » = proposition ; A0 tranche (veto possible).
- **Front-end** : P2 = App Vercel + Supabase + structuration Agents (« Prérequis Post SaaS-pocalypse ») — chantier séparé.
- **Reformulation des 3 séquences outbound** (Solaris/Nexus/Orbiter, jargon tokens → Franchise/Scalabilité) pour le meeting Abdaty mercredi — **livrable immédiat suivant**.
- **Pricing $** : ancrer les montants exacts depuis ADR-AAAS-PRICING-001 (5 tiers) — non recopiés ici (D1, pas de chiffre inventé).
- **Front P3** : DSpark/JEPA/Recursivemas = R&D, pas GTM court-terme.

## Ratification
Sign-off A0 pending. D4 append-only. Sisters à notifier : ADR-L2-AAAS-001, ADR-ICP-*, ADR-AAAS-PRICING-001, ADR-MARKET-STUDY-001.
