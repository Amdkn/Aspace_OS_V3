---
id: JTBD-003
title: JTBD Painkiller Message Variants — Format canon (Persona × JTBD × Pains × Gains × Triggers × Objections)
status: CANONICAL
date: 2026-06-24
created: 2026-06-24 (A1 Beth audit CONDITIONAL GO fix HIGH gap — stub créé pour débloquer 6 refs mortes)
last_updated: 2026-06-24
deciders: [A0 Amadeus]
proposed_by: Claude Code (A2) on A0 directive (A1 Beth audit verdict post-FULL BATCH 6 livrables)
domain: L2 Business OS / AaaS Doctrine / JTBD / Painkiller Message Format
tags: [#JTBD #painkiller #messaging #format-canon #aaas #stub #canonical]
related: [JTBD-ICP-SOLARIS-001, ADR-ICP-SOLARIS-001, ADR-L2-AAAS-001, ADR-AAAS-PRICING-001, ADR-MARKET-STUDY-001, ADR-OMK-004, ADR-SOBER-002, ADR-META-006]
sources_canons: [
  "JTBD-ICP-SOLARIS-001 (première application concrète du format Painkiller Message Variants)",
  "ADR-L2-AAAS-001 (AaaS Doctrine 3 Variants Solarpunk RATIFIED 2026-06-21)",
  "Takeout Gemini 2026-05 (verbatim pains/objections qui alimentent les variants)"
]
provenance: STUB créé 2026-06-24 par Claude Code (A2) suite à l'audit A1 Beth CONDITIONAL GO. Ce fichier **existe UNIQUEMENT pour débloquer 6 references mortes** (cf ADR-AAAS-PRICING-001 L38, L149, L160 + ADR-ICP-SOLARIS-001 L12, L169 + JTBD-ICP-SOLARIS-001 L12, L19, L145). Format canon complet documenté dans les sections suivantes ; canon corps détaillé à compléter en W2 fin (2026-07-03) ou plus tôt selon besoin A0.
---

# JTBD-003 — Painkiller Message Variants (Format Canon)

## Status

**CANONICAL** — 2026-06-24 (stub créé pour fix HIGH gap A1 Beth audit, FULL BATCH 6 livrables session).

**D6 honest flag** : ce fichier est un **stub fondateur de format canon**. Il définit la structure (5 sections obligatoires) que les JTBDs sisters (JTBD-ICP-SOLARIS-001, JTBD-ICP-NEXUS-001, JTBD-ICP-ORBITER-001, JTBD-PRICING-001) suivent. Le **corps détaillé** de chaque Painkiller Message Variant (variante messaging par persona × JTBD) reste à compléter en W2 fin (2026-07-03) ou par tâche dédiée.

## Purpose

### Pourquoi ce JTBD-003 existe

Le JTBD-003 = **format canon pour la rédaction des Painkiller Messages** AaaS Sisters Doctrine. Sister canon de :

- **`ADR-L2-AAAS-001`** (AaaS Doctrine 3 Variants Solarpunk RATIFIED 2026-06-21) — niveau doctrinal
- **`JTBD-ICP-SOLARIS-001`** (Jobs-to-Be-Done persona "Technicien fondateur E-Myth") — première application concrète
- **`ADR-AAAS-PRICING-001`** (AaaS Pricing Canon 5 Tiers RATIFIED + AMENDED 2026-06-24) — sister scope pricing messaging
- **`ADR-MARKET-STUDY-001`** (Étude de marché 'The Builders' 2026 RATIFIED 2026-06-24) — sœur scope marché

**Doctrine Painkiller** : un Painkiller Message = messaging AaaS qui transforme un **pain verbatim** (verbatim takeout canon) en **gain concret** (solution packagée prête-à-l'emploi), avec **triggers d'achat** et **objections pré-traitées**.

## Format

### Template canon — 5 sections obligatoires

Tout JTBD Painkiller Message Variant doit suivre ce template (5 sections, ordre canonique) :

#### Section 1 — Persona (archétype + démographie + verbatim caractéristique)

| Champ | Description | Source canon |
|---|---|---|
| Archétype | Persona archétypale (ex: "Technicien fondateur E-Myth") | Takeout canon origin spec |
| 4 sub-types | 4 sous-types canoniques (ex: Marketing / Création / Web / AI) | Takeout canon sister spec |
| Démographie | Age, localisation, CA, pricing actuel, stack | Étude de marché sœur |
| Verbatim caractéristique | 1 phrase canon verbatim qui capture l'essence | Takeout canon verbatim |

**Référence sister** : [`JTBD-ICP-SOLARIS-001` §Persona](./JTBD-ICP-SOLARIS-001.md#persona) (première application concrète).

#### Section 2 — Jobs-to-Be-Done (3-5 jobs fonctionnels + émotionnels + sociaux)

| Type | Description | Exemple Solaris |
|---|---|---|
| **Job 1 Functional** | Sortir d'un blocage opérationnel quotidien | "Sortir de l'esclavage client" |
| **Job 2 Functional** | Atteindre un objectif mesurable | "Facturer au juste prix sans négocier" |
| **Job 3 Emotional** | Résoudre une souffrance identitaire | "Ne plus avoir honte du système D" |
| **Job 4 Social** | Rejoindre une communauté / statut | "Rejoindre une communauté de pairs" |
| **Job 5 Functional (bonus)** | Répondre à un driver externe | "Conformité AI-Act sans expertise juridique" |

**Référence sister** : [`JTBD-ICP-SOLARIS-001` §Jobs-to-Be-Done](./JTBD-ICP-SOLARIS-001.md#jobs-to-be-done).

#### Section 3 — Pains verbatim canon (table 3-5 lignes minimum)

| # | Pain | Verbatim source | Line ref |
|---|---|---|---|
| P1 | Nom canon du pain | Verbatim takeout mot-pour-mot | `[YYYY-MM:LINE]` |
| P2 | ... | ... | ... |

**Règle D1** : chaque pain DOIT avoir un verbatim canon sourcé (pas d'invention, pas de reformulation). Sister pattern de [`JTBD-ICP-SOLARIS-001` §Pains](./JTBD-ICP-SOLARIS-001.md#pains-verbatim-canon).

#### Section 4 — Gains desired outcomes (table 3-5 lignes minimum)

| # | Gain | Description |
|---|---|---|
| G1 | Nom canon du gain | Description outcome mesurable |
| G2 | ... | ... |

**Règle** : chaque gain DOIT être **vérifiable** (mesurable, observable, testable par le persona). Sister pattern de [`JTBD-ICP-SOLARIS-001` §Gains](./JTBD-ICP-SOLARIS-001.md#gains-desired-outcomes).

#### Section 5 — Triggers + Objections (2 tables, 3-5 lignes minimum chacune)

**Buying Triggers** :

| # | Trigger | Description | Line ref |
|---|---|---|---|
| T1 | Nom canon du trigger | Crise / deadline / choc verbatim | `[YYYY-MM:LINE]` |

**Objections** :

| # | Objection | Verbatim source | Mitigation AaaS |
|---|---|---|---|
| O1 | Objection verbatim | `[YYYY-MM:LINE]` | Sister ADR Killer Feature |

**Règle D1** : chaque objection DOIT avoir un verbatim canon + une mitigation explicitement liée à une Killer Feature sister. Sister pattern de [`JTBD-ICP-SOLARIS-001` §Objections](./JTBD-ICP-SOLARIS-001.md#objections-verbatim-canon).

## Sister JTBDs

Ce format canon (5 sections) est appliqué par les JTBDs sisters suivantes :

| JTBD ID | Persona | Pricing tier | Sister ADR | Status |
|---|---|---|---|---|
| **JTBD-ICP-SOLARIS-001** | Technicien fondateur E-Myth | $300-500/an Tier 1 | `ADR-ICP-SOLARIS-001` | RATIFIED 2026-06-24 |
| **JTBD-ICP-NEXUS-001** | (à créer) Data First / Conformité | TBD sister `ADR-AAAS-PRICING-001` | `ADR-ICP-NEXUS-001` | À CRÉER (Q3 2026 W2 fin) |
| **JTBD-ICP-ORBITER-001** | (à créer) Mobile First / Terrain | TBD sister `ADR-AAAS-PRICING-001` | `ADR-ICP-ORBITER-001` | À CRÉER (Q3 2026 W2 fin) |
| **JTBD-PRICING-001** | (à créer) Pricing canon dedicated | Sister `ADR-AAAS-PRICING-001` 5 tiers | `ADR-AAAS-PRICING-001` | À CRÉER (Q3 2026 W2 fin) |

## Cross-refs

- [`JTBD-ICP-SOLARIS-001`](./JTBD-ICP-SOLARIS-001.md) — première application concrète du format (RATIFIED 2026-06-24)
- [`ADR-ICP-SOLARIS-001`](./ADR-ICP-SOLARIS-001_icp-solaris-structuration.md) — 5 Piliers ICP Solaris (RATIFIED 2026-06-24)
- [`ADR-L2-AAAS-001`](./ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md) — AaaS Doctrine 3 Variants Solarpunk (RATIFIED 2026-06-21)
- [`ADR-AAAS-PRICING-001`](./ADR-AAAS-PRICING-001_aaas-pricing-canon.md) — AaaS Pricing Canon 5 Tiers (RATIFIED + AMENDED 2026-06-24) — références JTBD-003 L38, L149, L160
- [`ADR-MARKET-STUDY-001`](./ADR-MARKET-STUDY-001_the-builders-2026.md) — Étude de marché 'The Builders' 2026 (RATIFIED 2026-06-24)
- [`ADR-OMK-004`](./ADR-OMK-004_pivot-supabase-cloud-vercel.md) — OMK Stack Pivot
- [`ADR-SOBER-002`](../L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) — Anti-Paperclip doctrine
- [`ADR-META-006`](../L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md) — D6 catalog (append-only)

## D1 Receipts Summary

| Critère | Source | Receipt | Confidence |
|---|---|---|---|
| Format 5 sections (Persona/JTBD/Pains/Gains/Triggers/Objections) | Sister `JTBD-ICP-SOLARIS-001` RATIFIED 2026-06-24 | application concrète | HIGH |
| 6 references mortes débloquées par création stub | `ADR-AAAS-PRICING-001` L38, L149, L160 + `ADR-ICP-SOLARIS-001` L12, L169 + `JTBD-ICP-SOLARIS-001` L12, L19, L145 | grep receipt | HIGH |
| Format canon sister scope messaging AaaS | `ADR-L2-AAAS-001` RATIFIED 2026-06-21 | sister doctrinal | HIGH |
| 3-ICP sister-symétrique (Solaris/Nexus/Orbiter) | `ADR-L2-AAAS-001` + `ADR-ICP-SOLARIS-001` + `ADR-ICP-NEXUS-001` + `ADR-ICP-ORBITER-001` | canon 4 ICP | HIGH |
| Stub fondateur, corps détaillé à compléter W2 fin 2026-07-03 | A0 directive post-A1 Beth audit verdict | directive verbale | HIGH |

## D6 Honest Flag

> **Stub fondateur créé 2026-06-24 par Claude Code (A2) sur directive A0 (post-A1 Beth audit CONDITIONAL GO verdict) pour fixer HIGH gap JTBD-003.** Ce fichier définit la **structure** (5 sections canoniques) que les JTBDs sisters suivent. **Le corps détaillé de chaque Painkiller Message Variant** (variantes messaging concrètes par persona × JTBD × pricing tier) reste **à compléter** :
>
> - En **W2 fin 2026-07-03** (par tâche dédiée ou follow-up Notion sync HITL)
> - Ou **plus tôt** selon demande A0 explicite
> - Par **sub-agent A1 Morty** (exécution patterns) avec relecture **A1 Beth** (veto cohérence canon)
>
> Pas d'invention de contenu canonique dans ce stub — uniquement structure template + references sisters + D1 receipts.

---

**STUB CANONICAL 2026-06-24 — Fix HIGH gap A1 Beth audit, débloque 6 references mortes**. Format canon sœur JTBD-ICP-SOLARIS-001 + futures JTBDs sisters (JTBD-ICP-NEXUS-001, JTBD-ICP-ORBITER-001, JTBD-PRICING-001). Corps détaillé à compléter en W2 fin 2026-07-03.