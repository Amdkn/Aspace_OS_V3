---
name: pricing-canon-derive
description: Automates derivation of AaaS Pricing Canon from 4 sources (A0 working memory + CC session archives + YouTube transcripts + Notion draft). Outputs ADR-AAAS-PRICING-NNN sister draft + JTBD-PRICING-NNN sister + wiki hand_off backup. Use when A0 asks "structure pricing canon", "derive pricing tiers", "fix pricing hallucination", or to formalize pricing after discovery that no ADR/JTBD/handoff pricing canon exists.
version: 1.0.0
created: 2026-06-24
author: Claude Code (A2) on A0 directive
related: [ADR-AAAS-PRICING-001, ADR-L2-AAAS-001, ADR-META-006, ADR-SOBER-002]
---

# /pricing-canon-derive — AaaS Pricing Canon Derivation Skill

> **Doctrine ancrage** : [ADR-AAAS-PRICING-001 RATIFIED 2026-06-24](../../ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md) · [ADR-META-001 D6 root-cause first](../../rules/ecc/agents.md) · [ADR-SOBER-002 Anti-Paperclip](../../ASpace_OS_V2/_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) · D7 anti-effondrement canon · D4 no-hard-delete

## What this skill does

Given **A0 demand** ("derive pricing canon", "fix pricing hallucination", "formalize pricing tiers", etc.), this skill:

1. **Scans 4 canon sources** for pricing content:
   - **A0 working memory** (questions, directives, JTBD contexts)
   - **CC session archives** (787 MB jsonl: 517 files live + archives)
   - **YouTube transcripts** (vidéos référencées par A0 dans sessions)
   - **Notion draft pages** (Squad 02 Sales ACV, etc.)
2. **Extracts anchors** (5-grams discriminants, prix, services, segments)
3. **Cross-validates 4 sources** (D6 root cause = aucune source unique fiable)
4. **Generates 3 outputs**:
   - `ADR-AAAS-PRICING-NNN_sister.md` (canon ADR draft)
   - `JTBD-PRICING-NNN_sister.md` (canon JTBD draft)
   - `wiki/hand_offs/pricing_canon_<DATE>.md` (backup canon)

## When to invoke

A0 says any of:
- "derive pricing canon", "structure pricing canon", "formalize pricing tiers"
- "fix pricing hallucination" (Notion draft != memory A0)
- "extract pricing from session archive"
- "match YouTube transcript for pricing"
- "create ADR pricing"

## Use when

- **D7 anti-effondrement** : aucun ADR/JTBD/handoff canon pricing formalisé
- **A0 memory > canon écrit** : A0 a des souvenirs précis que sessions CC n'ont pas
- **Notion draft vs canon** : Notion live contient ACV non ratifié
- **Cross-cuts 4 sources** : memory + sessions + vidéos + Notion

## Workflow

### Step 1 — Anchor extraction (D2 research FIRST)

```bash
# Ask A0 for transcription YouTube or pricing keywords
# Then extract discriminants:
python scripts/extract_anchors.py \
  --source "youtube_transcript.txt" \
  --keywords "tizi teachizi 4000 an 49 99 trust mrr" \
  --output anchors.json
```

### Step 2 — Canon sources scan (D1 verify)

```bash
# Scan 4 sources for matching pricing content
python scripts/scan_sources.py \
  --anchors anchors.json \
  --live "C:/Users/amado/.claude/projects/C--Users-amado/" \
  --archive16 "C:/Users/amado/.claude/_ARCHIVE_2026-06-16_sessions/" \
  --archive6 "C:/Users/amado/.claude/session-data/_TRASH/2026-06-06_cleanup/" \
  --notion "https://api.notion.com/v1/search" \
  --output sources_matched.json
```

### Step 3 — Canon derivation (D6 root cause)

```bash
# Cross-validate 4 sources, extract convergent pricing
python scripts/derive_canon.py \
  --sources sources_matched.json \
  --memory "A0 memory: $300/mois OU $5000/an" \
  --output ADR_AAAS_PRICING_DRAFT.md
```

### Step 4 — Output 3 deliverables

1. `_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-NNN_<name>.md` (ADR canon draft)
2. `_doctrine/B3_Warp_Core_Execution/01_Growth_Superman_Guardians/JTBD-PRICING-NNN.md` (JTBD draft)
3. `wiki/hand_offs/pricing_canon_<DATE>.md` (backup canon D7 anti-effondrement)

## Anti-patterns (D6 Lessons shipped)

1. ❌ **Notion draft = canon ratifié** : Notion live contient souvent ACV non ratifié (A0 hallucination cascade)
2. ❌ **Session CC = pricing canon** : 249 compactions par session en moyenne = détails perdus
3. ❌ **A0 memory négligée** : A0 memory souvent PLUS précise que canon écrit (D6 nuance)
4. ❌ **Skip JTBD-PRICING** : JTBD pricing sister manquant = canon incomplet
5. ❌ **Skip wiki backup** : D7 anti-effondrement raté si Notion down

## Examples (D1 receipts from 2026-06-24)

### Example 1 — Session `589ac9db` L713

```
User message L713 (11,301 chars):
"je vais te donnée la Transcription brute d'une video a analyser
 avant d'appliquer l'accuponcture de suppression d'un 0 dans les prix
 pour mettre 5000 a 500 meme si je ne sais pas encore si c'est par mois
 ou par ans ou à l'inscription...
J'ai fait 10 SaaS B2B & B2C : Voici ce que PERSONNE ne te dit:"
```

### Example 2 — Archive 16 juin subagent

```
"$5K MRR baseline Year 1, scaling to $500K by Year 10"
```

### Example 3 — A0 memory

```
"tarification de $300/ mois ou par Ans ou 5000 par Ans"
"ne soit pas rigide sur ses Donnee car mes souvenir sont plus precis"
```

### Example 4 — Notion Squad 02 Sales

```
"ACV moyen : Solaris ≥ 5k€ · Nexus ≥ 15k€ · Orbiter ≥ 50k€"
(DRAFT non ratifié — A0 dit hallucination)
```

## ROI

| Action | Manuel | Avec skill | Gain |
|---|---|---|---|
| Scan 517 .jsonl pour pricing | ~30 min | ~30 sec | **-98%** |
| Extract anchors discriminants | ~10 min | ~10 sec | **-98%** |
| Cross-validate 4 sources | ~20 min | ~1 min | **-95%** |
| Generate ADR + JTBD + wiki | ~2h | ~5 min | **-96%** |
| **Total** | **~3h** | **~7 min** | **-96%** |

## Sister canon references

- [ADR-AAAS-PRICING-001 RATIFIED 2026-06-24](../../ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md)
- [wiki/hand_offs/youtube_10saas_b2b_b2c_canon_2026-06-24.md](../../ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/youtube_10saas_b2b_b2c_canon_2026-06-24.md)
- [ADR-L2-AAAS-001 AaaS Doctrine 3 Variants](../../ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md)
- [ADR-META-006 D6 Catalog](../../ASpace_OS_V2/_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md)

## Scripts

- `scripts/extract_anchors.py` — D2 anchor extraction (5-grams discriminants)
- `scripts/scan_sources.py` — D1 scan 4 sources (CC sessions + Notion + YouTube)
- `scripts/derive_canon.py` — D6 cross-validation + ADR/JTBD/wiki generation

## Status

**v1.0.0 ACTIVE** — créée 2026-06-24 sur Option 3 du A0 directive batch (Option 1+2+3).
