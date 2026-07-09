---
type: spec-override
id: SPEC_OMK_COST
title: "COST_SPEC OMK Nexus BOS - MiniMax plan forfaitaire + cost cap fail-closed"
status: RATIFIED
date: 2026-07-05T09:45:00-04:00
author: HA
refines: specs/COST_SPEC.md (template canon)
sister: ADR-LD01-011 D2
---

# COST_SPEC - OMK Nexus BOS (override MiniMax plan forfaitaire)

> Override du template canon. Logique **cost arbitrage** = MiniMax plan fixe + inference locale, pas de variable cost runaway.

## Sources de cout (Phase 1 PoC)

| Source | Type | Mensuel | Comment |
|---|---|---|---|
| AWS Bedrock (Haiku tier) | Variable | ~$30/mois | 11 prompts AAARR x ~2k tokens each x 100 clients x 4 semaines |
| AWS Bedrock (Sonnet tier) | Variable | ~$80/mois | Quiz d'Acquisition outputs x 100 clients x 1 fois/mois |
| AWS S3 + DynamoDB + KMS | Fixe | ~$50/mois | Tier standard, pas scale |
| AWS Fargate orchestrator | Fixe | ~$30/mois | 1 task running 24/7 |
| AWS CloudWatch + SNS alarms | Fixe | ~$10/mois | Monitoring minimal |
| **Sous-total AWS** | Mixte | **~$200/mois** | Tier T1 standard |
| **Plan MiniMax 5.1B tokens** | **Fixe** | **$50/mois** | Forfait, pas de variable cost |
| Local inference (Ollama Llama 3) | Marginal | ~$0 | Open-source, hardware existant |
| Local storage + SQLite cache | Marginal | ~$0 | Storage existant |
| **Sous-total runtime** | Mixte | **$50-250/mois** selon charge | |
| **TOTAL Phase 1 PoC** | Mixte | **~$250-450/mois** | sous le plafond Tier T1 $500 |

## Pricing OMK Nexus BOS cote client (per Gemini analyse)

- **Forfait de base** : $1 000/mois par client premium
- **Cible** : 100 clients premium = $1.2M ARR
- **Marge nette cible** : > 90% (car les couts runtime sont quasi-fixes via MiniMax forfait)
- **Cout marginal par client supplementaire** : < $5/mois (cache semantique local reutilise)

## Cost cap fail-closed (per Blueprint section 3)

- **Daily cap** : $20/jour (AWS Budget + kill switch automatique)
- **Monthly cap** : $500/mois (AWS Budget + alerte admin)
- **Behavior on cap** : kill switch Bedrock calls, fall back to local-only Ollama
- **Behavior on cap computation failure** : **fail-closed** = stop rather than run (per Blueprint)

## Token economics (MiniMax 5.1B tokens / $50)

- **Total tokens/mois** : 5,100,000,000 (5.1B)
- **Cout par token** : $0.0000000098 (~1 nanocent)
- **Usage estime 100 clients** :
  - AAARR prompts : 100 clients x 11 prompts x 2k tokens = 2.2M tokens (0.04% du quota)
  - Quiz d'Acquisition : 100 clients x 5k tokens = 500k tokens (0.01% du quota)
  - Total : ~2.7M tokens = **0.05% du forfait** = legumes
- **Headroom** : 99.95% du forfait pour iterations futures, beta-coachs early access, scale-up

## Jevons paradox mitigation

Le paradoxe de Jevons : a mesure que les prix baissent, la consommation augmente. OMK Nexus mitige par :

1. **Cache semantique local SQLite/OPFS** : prompts AAARR reutilises sur signaux similaires = 0 token cloud (per Gemini T1 IT)
2. **Tier Haiku pour les passes low-stakes** (signal qualification) : ~10x moins cher que Sonnet
3. **Tier Sonnet pour l'output final uniquement** (validation, Quiz d'Acquisition) : pas pour la generation bulk
4. **Tier Opus jamais utilise** en Phase 1 (cout trop eleve)
5. **Local inference Ollama** pour fallback no-outside-vendor et pour les passes privees (PII clients)

## ROI client (per Gemini analyse)

- **Watchgang** (Matthew Gallager) : faillite avec 60 salaries, ARR <$10M
- **Medvi** : $1.8B ARR avec 2 employes (lui + son frere), mais chute FDA
- **OMK Nexus BOS** : $1.2M ARR cible avec 2-5 personnes, marge > 90%, niche coaching B2B sans risque FDA

## Open questions Phase 2

- Bedrock vs local pour les **transcripts d'appels** (Phase 2 si clients B2B signent)
- EU AI Act compliance : cout estime ~$2k/mois (documentation + audit) Phase 2
- DLP complet Supabase : cout estime ~$50/mois (9 patterns + audit) Phase 2
