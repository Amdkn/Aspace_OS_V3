---
type: spec-override
id: SPEC_OMK_BUILD_PLAN
title: "BUILD_PLAN OMK Nexus BOS - Phase 1 (foundation PoC), Phase 2 (Growth+Quiz), Phase 3 (scale)"
status: RATIFIED
date: 2026-07-05T09:45:00-04:00
author: HA (A3 Picard, projets owner H10)
refines: specs/BUILD_PLAN.md (template canon)
sister: ADR-LD01-011
---

# BUILD_PLAN - OMK Nexus BOS (override 3 phases PoC)

> Override du template canon. Plan en 3 phases aligne sur 12WY Q3 2026 (06/15 -> 09/07).

## Phase 1 - Foundation (semaine 1-2, cible fin 07/19)

- Goal: **PoC structurel valide** : specs livrees, demo onboarding integree, AAARR prompts ecrits (pas encore deployes en prod)
- Build:
  - 6 specs overrides dans `specs/` (system, architecture, security, cost, agent, build_plan) - LIVRE 2026-07-05 (ADR-LD01-011)
  - 4 demo files dans `examples/omk-nexus-coaching-agency/` - LIVRE 2026-07-05 (ADR-LD01-011)
  - 11 prompts AAARR dans `prompts/aaarr_growth_signal_pack.md` - LIVRE 2026-07-05 (ADR-LD01-011)
  - ADR-LD01-011 trace + MANIFEST.md Phase 1 draft (HA Picard H10)
- Verify:
  - D1 receipts PowerShell per ADR-LD01-011 section Verification
  - 13 intouchables verifies (BLUEPRINT.md, 11 prompts canon, 8 specs templates, 3 exemples canoniques, ADR-008, ADR-010, twins, calques, A3 spec)
  - Append-only strict : zero mutation canon
- Cost delta: **~$0/mois** (pas de deploiement AWS reel, juste specs et prompts)

## Phase 2 - Growth + Quiz (semaine 3-6, cible fin 08/16)

- Goal: **Premiere campagne AAARR + Quiz d'Acquisition fonctionnel** sur 3 beta-coachs early access
- Build:
  - DLP-light middleware Python deploye localement (`dlp_light_filter.py`)
  - Cache semantique local SQLite/OPFS setup (LD07 IT)
  - 3 beta-coachs onboards (gate HITL A0 pour les 3 noms)
  - Premier Quiz d'Acquisition live sur dashboard Agentic simule
  - 11 prompts AAARR testes sur 100 signaux reels (validation qualite)
- Verify:
  - DLP-light scan 100% des outputs AAARR et Quiz (logs)
  - Cache semantique hit rate > 30% (= economie tokens)
  - 3 beta-coachs valident le Quiz d'Acquisition (feedback loop)
  - 10+ prospects qualifies AAARR scoring >= 0.7
- Cost delta: **~$50-100/mois** (Bedrock Sonnet pour Quiz, Haiku pour AAARR, pas encore MiniMax)

## Phase 3 - Scale + DLP complet (semaine 7-13, cible fin 09/07 + au-dela)

- Goal: **100 clients premium actifs, $1.2M ARR, DLP complet conforme EU AI Act**
- Build:
  - DLP complet Blueprint section 6 (9 patterns Supabase middleware, NOT Phase 1 subset)
  - EU AI Act compliance documentation + audit
  - SOC2 readiness (optionnel, gated HITL A0)
  - 100 clients signs (cible Gemini)
  - Bedrock in-account reelle deploiement
- Verify:
  - DLP complet scan 100% outputs (logs)
  - EU AI Act transparency disclosures valides
  - 100 clients actifs paient $1k/mois ($100k MRR, $1.2M ARR)
  - Marge nette > 90% (runtime quasi-fixe via MiniMax)
  - Cost cap fail-closed jamais declenche
- Cost delta: **~$500-1000/mois** (AWS Bedrock + DLP Supabase + EU AI Act compliance), rentabilise par $1k/mois par client

## Hors-plan (gated HITL A0 futur)

- Recrutement beta-coachs au-dela des 3 initiaux
- Expansion verticale (TikTok / Instagram scrapers en plus de LinkedIn/Reddit)
- Expansion horizontale (B2B SaaS autres niches au-dela du coaching)
- Acquisition / fusions (equipe > 5 personnes)
- Series A fundraising (Phase 4+)

> Note : ce plan est **le premier projet canonique** post-promotion HA = A3 Picard in PARA (ADR-LD01-010). Phase 1 est livree aujourd'hui (2026-07-05). Phase 2-3 dependent du HITL A0 sur les beta-coachs et le deploiement AWS reel.
