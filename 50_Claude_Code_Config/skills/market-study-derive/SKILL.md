---
name: market-study-derive
description: Automates derivation of AaaS Market Study Canon from Takeout Gemini conversations + Notion pages + ADR canon. Outputs ADR-MARKET-STUDY-NNN sister draft + JTBD-MARKET-NNN sister + wiki hand_off backup. Use when A0 asks "structure market study", "extract TAM/SAM/SOM", "find killer feature", or to formalize a market study after discovery that no ADR/handoff canon exists.
version: 1.0.0
created: 2026-06-24
author: Claude Code (A2) on A0 directive
related: [ADR-MARKET-STUDY-001, ADR-ICP-SOLARIS-001, ADR-ICP-NEXUS-001, ADR-ICP-ORBITER-001, ADR-L2-AAAS-001, ADR-AAAS-PRICING-001, ADR-META-006, ADR-SOBER-002, ADR-ICP-NEXUS-001]
---

# /market-study-derive — AaaS Market Study Canon Derivation Skill

> **Doctrine ancrage** : [ADR-MARKET-STUDY-001 RATIFIED 2026-06-24](../../ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-MARKET-STUDY-001_the-builders-2026.md) · [ADR-META-001 D6 root-cause first](../../rules/ecc/agents.md) · [ADR-SOBER-002 Anti-Paperclip](../../ASpace_OS_V2/_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) · [ADR-META-006 D6 catalog](../../ASpace_OS_V2/_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md) · D7 anti-effondrement canon · D4 no-hard-delete

## What this skill does

Given **A0 demand** ("structure market study", "extract TAM/SAM/SOM", "find killer feature", "canonize étude de marché", etc.), this skill:

1. **Scans 3 canon sources** for market study content:
   - **Takeout Gemini conversations** (year-month .md files in `00_Amadeus/30_MEMORY_CORE/Gemini_Takeout_2026/`)
   - **Notion pages** (live pages: Squad 02 Sales, Market Research, etc.)
   - **Existing ADR canon** (`_SPECS/ADR/L2_Business_OS/` for sister scope)
2. **Extracts 4 sections canon** (D2 research FIRST):
   - **La Mutation** — marché en transition
   - **L'Offre E-Myth** — agencies/web E-Myth = 80% des acteurs
   - **Services Hybrides** — mix SaaS + services + AI agents
   - **Les 3 Modèles** — pricing canon Solo/Standard/Groupe
3. **D1 verifies** : locate verbatim quotes with line refs `[YYYY-MM:NNNNN]` + 2 tables (Pricing + KPIs) + Killer Feature verdict + driver légal
4. **D6 root cause** : identify Killer Feature (4 mécanismes pack Agentic Governance sister `ADR-L2-AAAS-001` + `ADR-ICP-SOLARIS-001` Pilier 5) + driver légal (AI-Act, RGPD, secret pro, etc.)
5. **Generates 3 outputs** :
   - `ADR-MARKET-STUDY-NNN_<name>.md` (canon ADR draft)
   - `JTBD-MARKET-NNN_<name>.md` (canon JTBD draft sister scope, sister JTBD-ICP-SOLARIS-001 pattern)
   - `wiki/hand_offs/market_study_<DATE>.md` (backup canon D7 anti-effondrement)

## When to invoke

A0 says any of:
- "structure market study", "extract market study", "canonize étude de marché"
- "extract TAM", "extract SAM", "extract SOM"
- "find killer feature", "extract killer feature from takeout"
- "extract market trends", "extract market segments"
- "create ADR market study", "create ADR étude de marché"

## Use when

- **D7 anti-effondrement** : aucun ADR/JTBD/handoff canon market study formalisé
- **Takeout sleeping canon** : Takeout Gemini contient souvent 500-1500 lignes structurées non extraites
- **Notion draft vs canon** : Notion live contient études de marché non ratifiées
- **Cross-cuts 3 sources** : takeout + Notion + ADR canon
- **Killer Feature identification** : 4 mécanismes pack Agentic Governance = différentiation canon AaaS
- **Driver légal urgency** : AI-Act août 2026 = window Q2-Q3 2026 critique

## Workflow

### Step 1 — Anchor extraction (D2 research FIRST)

```bash
# Ask A0 for market study scope (TAM/SAM/SOM, segment cible, géographie)
# Then extract discriminants:
python scripts/extract_sections.py \
  --source "C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/Gemini_Takeout_2026/2026-05_conversations.md" \
  --sections "Mutation,E-Myth,Hybrides,Modeles" \
  --keywords "étude de marché,TAM,SAM,SOM,killer feature,AI-Act,mutation,E-Myth,services hybrides" \
  --output sections_anchors.json
```

### Step 2 — Canon sources scan (D1 verify)

```bash
# Scan 3 sources for matching market study content
python scripts/scan_market_sources.py \
  --sections sections_anchors.json \
  --takeout "C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/Gemini_Takeout_2026/" \
  --notion "https://api.notion.com/v1/search" \
  --adr_canon "C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/" \
  --output sources_matched.json
```

### Step 3 — Killer Feature root cause (D6)

```bash
# Identify Killer Feature (4 mécanismes Agentic Governance canon)
# + driver légal (AI-Act/RGPD/secret pro)
python scripts/derive_killer_feature.py \
  --sources sources_matched.json \
  --killer_feature_pattern "Action Space Bounding|Sandboxing|HITL Dynamique|Traçabilité AI-Act|Zero-PII|God.?s Eye|Palantir Constructif" \
  --driver_legal_pattern "AI Act|RGPD|HIPAA|secret professionnel|84 Trilliards|domination hyper-locale" \
  --output killer_feature_verdict.json
```

### Step 4 — Output 3 deliverables (canonisation)

1. `_SPECS/ADR/L2_Business_OS/ADR-MARKET-STUDY-NNN_<name>.md` (ADR canon draft — sister `ADR-MARKET-STUDY-001` pattern)
2. `_SPECS/ADR/L2_Business_OS/JTBD-MARKET-NNN_<name>.md` (JTBD draft — sister `JTBD-ICP-SOLARIS-001` pattern)
3. `wiki/hand_offs/market_study_<DATE>.md` (backup canon D7 anti-effondrement)

## 4 Sections canon (D2 research anchors)

| # | Section canon | Anchor keywords (FR+EN) | D2 regex pattern |
|---|---|---|---|
| 1 | **La Mutation** | "mutation", "transition digitale", "transformation digitale", "marché en mutation" | `(?i)(mutation|transition digitale|transformation digitale|marché en transition)` |
| 2 | **L'Offre E-Myth** | "E-Myth", "agence E-Myth", "technicien fondateur", "80% des agences" | `(?i)(E-Myth|technicien fondateur|80% des agences|agence E-Myth)` |
| 3 | **Services Hybrides** | "services hybrides", "mix SaaS services", "AI agents commodité", "conformité by design" | `(?i)(services hybrides|mix SaaS services|AI agents commodité|conformité by design)` |
| 4 | **Les 3 Modèles** | "3 modèles", "Solo Founder", "Standard", "Groupe", "pricing canon" | `(?i)(3 modèles|Solo Founder|Standard|Groupe|pricing canon)` |

## Killer Feature canon (4 mécanismes Agentic Governance)

**Source canon** : Sister `ADR-ICP-SOLARIS-001` Pilier 5 (Action Space Bounding + Sandboxing + HITL Dynamique + Traçabilité AI-Act).

**Détection D6** : grep takeout pour le pattern 4 mécanismes + scoring par densité d'occurrences.

## Anti-patterns (D6 Lessons shipped 2026-06-24)

1. ❌ **Skip D1 receipts** : toute section canon doit avoir au moins 1 verbatim line ref `[YYYY-MM:NNNNN]`
2. ❌ **Confondre brief et output** (D6 lesson 2026-06-24) : brief = demande A0, output = 3 deliverables canon
3. ❌ **Halluciner TAM sans source** : TAM/SAM/SOM doivent être verbatim takeout ou sister ADR canon, JAMAIS inventés
4. ❌ **Skip JTBD-MARKET sister** : JTBD canon sister manquant = canon incomplet
5. ❌ **Skip wiki backup** : D7 anti-effondrement raté si Takeout down (D6 no-hard-delete respecté mais extract perdu)
6. ❌ **Sauter driver légal** : AI-Act / RGPD / secret pro = urgence canonisation = Killer Feature justification
7. ❌ **Killer Feature 1 mécanisme** : pack Agentic Governance = 4 mécanismes canon, pas 1 feature isolée
8. ❌ **Pricing canon absent** : toute étude de marché doit avoir 1 section pricing (sister `ADR-AAAS-PRICING-001`)

## Examples (D1 receipts from 2026-06-24)

### Example 1 — Étude de marché 'The Builders' 2026 (1,354 lignes structurées)

```
Source : Takeout Gemini 2026-05 L155547-156900
Titre verbatim L155547 : "ÉTUDE DE MARCHÉ 'THE BUILDERS' : AGENCES WEB ET AUTOMATISATION 2026"
TAM verbatim L155599 : "136,1 Mds$ marché intégrateurs système"
4 sections canon : Mutation + E-Myth + Hybrides + 3 Modèles
Killer Feature L156796-156844 : "Agentic Governance 4 mécanismes"
Driver légal L155599 : "AI Act application totale août 2026"
```

### Example 2 — Nexus Family Offices 84 Trilliards (verbatim L19500)

```
Source : Takeout Gemini 2026-05 L19500-19580
TAM verbatim L19500 : "le transfert de 84 Trilliards d'euros (le plus grand transfert de richesse de l'histoire de l'humanité)"
Secteur : Family Offices / Cabinets juridiques / Experts-comptables
Killer Feature Nexus : Zero-PII Bare-Metal (5 mécanismes vs Solaris 4)
Driver légal : secret professionnel + RGPD + AI-Act
```

### Example 3 — Orbiter Bilawal Sidhu God's Eye View (verbatim L19620)

```
Source : Takeout Gemini 2026-05 L19620-19751
Inspiration UX verbatim L19620 : "Bilawal Sidhu God's Eye View (qui traque les navires dans le détroit d'Ormuz)"
Différenciation L19635 : "Palantir Constructif vs Palantir Force Brute centralisée"
Killer Feature Orbiter : God's Eye View + Ant-Man Route Optimizer + Vision Dispatcher + Quicksilver SMS + Songbird Billing (5 mécanismes terrain)
Driver légal : domination hyper-locale + zones blanches 4G
```

## ROI

| Action | Manuel | Avec skill | Gain |
|---|---|---|---|
| Scan Takeout Gemini pour étude de marché (1,354 lignes) | ~45 min | ~45 sec | **-98%** |
| Extract 4 sections canon + 2 tables + Killer Feature | ~30 min | ~30 sec | **-98%** |
| Cross-validate 3 sources (takeout + Notion + ADR canon) | ~30 min | ~1 min | **-95%** |
| Generate ADR + JTBD + wiki backup | ~3h | ~10 min | **-94%** |
| **Total** | **~4.5h** | **~13 min** | **-95%** |

## Sister canon references

- [ADR-MARKET-STUDY-001 RATIFIED 2026-06-24 — Étude de marché 'The Builders' 2026](../../ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-MARKET-STUDY-001_the-builders-2026.md)
- [ADR-ICP-SOLARIS-001 RATIFIED 2026-06-24 — ICP Solaris 5 Piliers](../../ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-ICP-SOLARIS-001_icp-solaris-structuration.md)
- [ADR-ICP-NEXUS-001 RATIFIED 2026-06-24 — ICP Nexus 5 Piliers](../../ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-ICP-NEXUS-001_icp-nexus-structuration.md)
- [ADR-ICP-ORBITER-001 RATIFIED 2026-06-24 — ICP Orbiter 5 Piliers](../../ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-ICP-ORBITER-001_icp-orbiter-structuration.md)
- [ADR-L2-AAAS-001 AaaS Doctrine 3 Variants](../../ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md)
- [ADR-AAAS-PRICING-001 RATIFIED+AMENDED 2026-06-24 Pricing Canon](../../ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md)
- [ADR-META-006 D6 Catalog](../../ASpace_OS_V2/_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md)
- [Sister skill `/pricing-canon-derive` v1.0.0 ACTIVE 2026-06-24](../../skills/pricing-canon-derive/SKILL.md)

## Scripts

- `scripts/extract_sections.py` — D2 anchor extraction (4 sections canon : Mutation / E-Myth / Services Hybrides / 3 Modèles)
- `scripts/derive_killer_feature.py` — D6 root cause for the 4 mécanismes Agentic Governance + driver légal

## Status

**v1.0.0 ACTIVE** — créée 2026-06-24 sur Option 3 du A0 directive batch (Option 1 ADR + Option 2 JTBD + Option 3 skill). Sister de `/pricing-canon-derive` créée même jour, même pattern.