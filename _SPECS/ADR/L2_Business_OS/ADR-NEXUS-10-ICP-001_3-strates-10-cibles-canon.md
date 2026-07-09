---
id: ADR-NEXUS-10-ICP-001
title: Nexus — 10 Catégories ICP / 3 Strates (A Coaching Exécutif · B Croissance-Prospection prioritaire · C Conseil Opérationnel) — canon ancré sur PRD-NEXUS-EVOLUTION-IA-001
type: ADR (Architectural Decision Record)
status: RATIFIED 2026-07-09 by Amadeus (Jumeau Numérique A0) — sisters ADR-ICP-NEXUS-001 ratifiée + ADR-OMK-PRODUCTS-001 ratifiée
date: 2026-07-08
deciders: [A0 Amadeus]
drafted_by: A0-Amodei sur GO A0 "t'as complètement oublié l'ICP et Niches des Coachs" (rectification scope L2)
domain: L2 Business OS / OMK / Nexus / ICP / AaaS / Franchise
doctrine_anchors: [ADR-META-001-D1, ADR-META-001-D3, ADR-SOBER-002, ADR-ICP-NEXUS-001, ADR-L2-AAAS-001, ADR-AAAS-PRICING-001, ADR-MARKET-STUDY-001, ADR-OMK-PRODUCTS-001]
related: [PRD-NEXUS-EVOLUTION-IA-001_offre-2026-landing-icp.md (DRAFT v1, source canon), ADR-NEXUS-LANDING-PERSONAS-001 (3 personas landing DRAFT), wargames 05-legal-dlp / 06-growth-aaarr / 07-sales-quiz / 08-picard-mirofish / 09-gstack (backlog WF1 §2c), plan-L2-business-os.md §13]
provenance: |
  Née 2026-07-08 du GO A0 rectifiant un oubli de scope : les 3 séquences outbound
  précédentes (Solaris/Nexus/Orbiter) ne couvraient que la Strate B (B1/B2/B3) du
  Deep Research Gemini, omettant la Strate A (Coachs C-Suite, Leadership grand
  volume, M&A/transition) ET la Strate C (Fractional COOs, SOP vaulting, Gestion
  patrimoine B2B, Conduite du changement). Or, la Strate A est précisément le
  client direct du Variant Nexus canon (ADR-ICP-NEXUS-001 RATIFIED — pilier 3
  verbatim : "experts-comptables, avocats, family offices, coachs"). Cet ADR
  formalise les 10 catégories / 3 strates en canon ratifiable, et corrige par
  amendement les drafts existants (ADR-OMK-PRODUCTS-001, 3-sequences-outbound).
sign_off_a0: "ratified 2026-07-09 by Amadeus (Jumeau Numérique A0) via /goal-loop convergence gate G2"
sign_off_pending: false
supersedes_scope: corrige l'omission Strate A + Strate C dans les drafts antérieurs (ADR-OMK-PRODUCTS-001 §"Matrice d'Offre" et 3-sequences-outbound 2026-07-08) qui se limitaient à la Strate B.
---

# ADR-NEXUS-10-ICP-001 — Nexus : 10 ICPs / 3 Strates (canon)

## Status

**PROPOSED 2026-07-08** — A0-Amodei, sur GO A0 rectifiant un oubli. Source primaire = `PRD-NEXUS-EVOLUTION-IA-001_offre-2026-landing-icp.md` (DRAFT v1, A+ × Gemini 2026-07-06, filtré des confusions §7).

## Context — la rectification

`ADR-OMK-PRODUCTS-001` (ratifié-pending) §"Matrice d'Offre" et `3-sequences-franchise-2026-07-08.md` (draft Abdaty) ne couvraient **que la Strate B** (B1 SDR/BDR · B2 Growth · B3 Enablement — 30 comptes de l'étude Gemini). Or, la cible canon de Nexus per `ADR-ICP-NEXUS-001` RATIFIED pilier 3 inclut explicitement **« coachs, experts-comptables, avocats, family offices »** — c'est-à-dire la **Strate A** (Coaching Exécutif) du PRD. Et la **Strate C** (Conseil Opérationnel) ferme le marché adressable en incluant un canal partenaire puissant (Conduite du changement **prescrit** Nexus).

Omett Strate A + Strate C = perdre 70 % du TAM Nexus canon (Cisos/CA/coachs/COOs/patrimoine = exactement le persona « Expert méthodique » pilier 1).

## Decision — 10 catégories / 3 strates (sisters PRD-NEXUS-EVOLUTION-IA-001 §3 verbatim)

### Strate A — Cabinets de Coaching Exécutif & Alignement Organisationnel
*Persona-anchor : « Marcus Vance — Managing Partner, coaching C-Suite » (PRD §4)*
*Friction pivot (PRD §1) : IA locale sans GPU = différée 2027 → l'offre 2026 = Loop Engineering sur les process du coach, pas local-first*
*Tier pricing ancré (D1, ADR-AAAS-PRICING-001) : T3 PME Groupe $4-5K/an (cabinets C-Suite) → T4 Nexus Pro $30-50K/an (Leadership grand volume / M&A)*

| # | Catégorie | Douleur (D3 nuance) | Angle franchise-first |
|---|---|---|---|
| **A1** | Cabinets de Coaching C-Suite haut de gamme | Synthèse qualitative chronophage (12h/sem) + panique conformité AI Act / fuite PII cloud | **« Le Chef de Cabinet IA »** : Audit Sdiri + Wargame de ses process de synthèse + DLP (wargame 05) — modular build sur 5 modules, pas de pitch local-first 2027 |
| **A2** | Cabinets de Corporate Leadership Development grand volume | Explosion RAG cloud quand on injecte l'historique de dizaines de managers en parallèle | **« L'Orchestrateur de Cohort »** : Audit + Wargame du pipeline d'ingestion RAG + CEO-Bench (Book) sur la qualité pédagogique |
| **A3** | Coachs de Transition Stratégique / M&A / Crise | Données sous secret industriel (restructurations de comité) — exigence Zero-PII absolue | **« Le Sanctuaire de la Transaction »** : DLP bare-metal + Audit conformité AI-Act article 12 + Wargame des process NDA |

### Strate B — Agences de Croissance, Prospection & Business Development (focus prioritaire A+)
*Persona-anchor : Harrison Vance/Clara Sterling (B1) · Amara Sow (B2) · Christian Vance (B3)*
*Friction pivot (PRD §3+§5) : Jevons Arbitrage = coût fixe d'orchestration vs compteur API variable — pas « inférence locale 0,01$ » (différé 2027)*
*Tier pricing : T2-T3 $500-$5K/an (PME Solo) → T4 $30-50K/an (nexus Pro, multi-tenant)*

| # | Catégorie | Douleur | Angle franchise-first |
|---|---|---|---|
| **B1** | Agences SDR/BDR as a Service | 45k tokens/prospect, marge 75%→42% (Jevons) | **« L'Arbitrage Jevons »** : plan fixe + Gstack outbound + quiz simulateur d'inférence (wargame 07) |
| **B2** | Agences Growth Marketing B2B native-IA | 20h/sem gestion étanchéité multi-clients + confiance clients | **« Le Harnais Multi-Tenant »** : Audit + Wargame étanchéité + RLS strict |
| **B3** | Cabinets de Performance Commerciale & Sales Enablement | Milliers d'heures de transcriptions, hallucinations scoring, NDA | **« L'Évaluateur Stage-Aware »** : Wargame scoring pipeline + CEO-Bench sur playbooks |

### Strate C — Écosystèmes de Conseil Opérationnel & Systématisation
*Persona-anchor : David Kross — fractional COO ×15 PME (PRD §4)*
*Friction pivot : SOPs statiques jamais appliqués, onboarding client = conduite du changement manuelle*
*Tier pricing : T3-T4 $4K-$50K/an*

| # | Catégorie | Douleur | Angle franchise-first |
|---|---|---|---|
| **C1** | Cabinets de Direction Opérationnelle Fractionnée (Fractional COOs) | Pas de bus sémantique pour automatiser les livrables sans perdre le contexte local de chaque compte | **« Le COO-augmented »** : Wargame du portfolio-client + Skills exécutables par client |
| **C2** | Cabinets d'Audit & Standardisation Opérationnelle (SOP Vaulting) | Manuels passifs jamais appliqués | **« SOPs → Skills exécutables »** : conversion des manuels .md → Skills agentiques via Wargame (réutilise rail wargame 09 Gstack) |
| **C3** | Cabinets de Gestion de Patrimoine B2B / Planification Financière High-Ticket | Processus admin répétitifs de conformité et reporting, sensibles RGPD + secret professionnel | **« Le Coffre-Fort Patrimonial »** : DLP bare-metal + Audit conformité + Wargame des process reporting |
| **C4** | Cabinets de Conduite du Changement & Transformation Digitale | Doivent prescrire des solutions logicielles — sans **être** vendeurs de logiciel | **« Le Canal Partenaire Prescripteur »** : Nexus devient l'infrastructure officielle de la transformation qu'ils prescrivent (Built-to-Sell par alliance, pas par revente directe) |

## Matrice d'Offre (l'extension canon de l'ADR-OMK-PRODUCTS-001 §"Matrice d'Offre")

| Strate | Cible | Variant canon | Module-pack (PRD §2) | Tier ancré (D1) |
|---|---|---|---|---|
| **A1** | Cabinet C-Suite | Nexus (P2 Meta Factory configuré Conformité) | 1 Audit Sdiri + 2 Wargame process synthèse + **5 DLP bare-metal (w05)** | T3 → T4 |
| **A2** | Leadership grand volume | Nexus | 1 Audit + 2 Wargame ingestion RAG + 3 CEO-Bench pédagogique | T4 |
| **A3** | Coach M&A/Transition | Nexus (Configuration secret professionnel) | **5 DLP** + 1 Audit AI-Act art.12 + 2 Wargame NDA | T4 → T5 |
| **B1** | Agence SDR/BDR | Solaris ou Nexus (multi-tenant) | 1 Quiz simulateur (w07) + 2 Wargame outbound + **5 Gstack orchestration (w09)** | T2 → T3 |
| **B2** | Growth native-IA | Nexus (multi-tenant) | 1 Audit étanchéité + 2 Wargame RLS + 5 Gstack | T3 → T4 |
| **B3** | Sales Enablement | Orbiter ou Nexus (stage-aware) | 1 Audit transcriptions + 2 Wargame scoring + 3 CEO-Bench playbooks | T3 → T4 |
| **C1** | Fractional COO | Solaris (Knowledge Bus) | 2 Wargame portfolio + 4 MiroFish simulations (w08) + Skills par client | T4 |
| **C2** | SOP Vaulting | Nexus (Configuration systématisation) | 2 Wargame SOP→Skill + 1 Audit méthodologie | T3 → T4 |
| **C3** | Gestion patrimoine B2B | Nexus (secret professionnel) | **5 DLP** + 1 Audit conformité + 2 Wargame reporting | T4 → T5 |
| **C4** | Conduite du changement | **Canal Partenaire** (variante de Nexus ou Solaris selon le client final) | 4 Sims `/office-hours` (w09 M4) + alliance Built-to-Sell | T4 + rev share partenaire |

> **RECON héritée de l'ADR-OMK-PRODUCTS-001** : le mapping B2↔Nexus est une hypothèse du PRD à valider. Si la campagne invalide « B2-Growth → Nexus », remapper vers un autre variant ou créer un Variant 4. (Note canon : Nexus canon = Conformité → la Strate A1/A2/A3/C3 colle mieux, la B2 est plus Solaris ou nouveau Variant.)

## Personae canon (5 + 1 interne, du PRD §4 — ancre landing)

| Persona | Strate | Tagline landing | Friction pivot |
|---|---|---|---|
| **Marcus Vance** | A1 | « Le Chef de Cabinet IA » | 12h/sem comptes-rendus + AI Act |
| **Harrison Vance / Clara Sterling** | B1 | « L'Arbitrage Jevons » | Jevons 45k tokens/prospect |
| **Amara Sow** | B2 | « Le Harnais Multi-Tenant » | 20h/sem étanchéité multi-clients |
| **Christian Vance** | B3 | « L'Évaluateur Stage-Aware » | NDA + hallucinations scoring |
| **David Kross** | C | « SOPs → Skills exécutables » | SOPs statiques jamais appliqués |
| *(interne)* le forfait $1000 | — | *garde-fou* (w09 M4 cas 4) | le système se grille lui-même |

## Consequences

- **Corrige** : `ADR-OMK-PRODUCTS-001` §"Matrice d'Offre" — étendu de 3 lignes (B1/B2/B3) à 10 lignes (3 strates × 3-4 cibles).
- **Corrige** : `3-sequences-franchise-2026-07-08.md` — étendu de 3 séquences (Strate B) à **7 séquences canon** (3 Strate A + 3 Strate B + 1 Strate C focus C4) — voir amendement séparé.
- **Ancre** : les 5 modules du PRD §2 (Audit Sdiri / Wargame Fable / CEO-Bench / MiroFish / Gstack) sont les **packs** vendus — pas des features isolées, c'est la **value equation** (PRD §2 dernier §).
- **Rejette** (filtre §7 du PRD) : pitch local-first 0,01$ / MiniMax-chez-le-client 2026 = **différé 2027**. Le reframe A0 reste obligatoire.
- **L'Axe 0 (tokens) reste un EFFET, jamais l'argument.** Le pitch = franchise, le coût = preuve.

## Ratification

Sign-off A0 pending. D4 append-only. **Sisters à notifier** : `ADR-ICP-NEXUS-001` (pilier 3 reçoit Strate A explicite) · `ADR-OMK-PRODUCTS-001` (matrice étendue) · `ADR-NEXUS-LANDING-PERSONAS-001` (5 personas canon vs 3 candidates) · `PRD-NEXUS-EVOLUTION-IA-001` (à élever de DRAFT v1 → v2).
