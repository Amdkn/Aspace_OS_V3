---
type: example-overview
id: OMK_NEXUS_COACHING_AGENCY
title: "OMK Nexus BOS - Tier T1 Coaching B2B PoC"
status: RATIFIED
date: 2026-07-05T09:45:00-04:00
author: HA (A3 Picard in PARA, projets owner H10)
refines: examples/{solo-consultant,northgate-law,riverside-clinic}/ (intouches)
sister: ADR-LD01-011_omk_nexus_bos_poc_initiation
append_only: true
tier: T1
niche: BUSINESS_COACHING_AND_DEV_AGENCIES
---

# OMK Nexus BOS - Tier T1 Coaching B2B PoC

> **Cas d'usage** : Cabinet de Coaching Premium / Agence de Business Development cible 100 clients premium a $1k/mois = $1.2M ARR.
>
> Parallele canon : `solo-consultant/` (T0), `northgate-law/` (T1, notre tier), `riverside-clinic/` (T2).

## Quick context

Tu es le fondateur d'un cabinet de coaching B2B premium OU d'une agence de business development. Tu as 5-50 clients actifs, une equipe de 2-10 personnes, des couts operationnels eleves (Otter.ai, Lemlist, HubSpot, Notion, Calendly), et tu veux :
- Reduire les couts fixes mensuels (objectif : marge > 90%)
- Automatiser le pipeline d'acquisition (sans spammer, par signaux)
- Offrir une experience onboarding immediate (Quiz d'Acquisition en self-serve)
- Garder le controle de la relation client (pas de FDA, pas de HIPAA, juste EU AI Act awareness)

**OMK Nexus BOS** est le systeme qui fait ca. Ce cas d'usage est Tier T1 (entre solo et clinic) parce que tu geres des PII confidentielles mais pas regulees.

## Files dans ce dossier (append-only, ordre de lecture)

1. **`README.md`** (ce fichier) - vue d'ensemble, contexte, navigation
2. **`01_onboarding_walkthrough.md`** - pas-a-pas prospect/coach : de la decouverte a la premiere session
3. **`02_first_session_runbook.md`** - runbook 90 min : quiz acquisition -> analyse AAARR -> cartographie pertes -> plan de liberation
4. **`03_quiz_acquisition_integration.md`** - integration Quiz d'Acquisition Medvi a l'Agentic Dashboard

## Liens canon

- **Specs** : `Enterprise_OS_Blueprint_Kit/specs/{system,architecture,security,cost,agent,build_plan}_spec_omk_nexus.md` (6 overrides)
- **Prompts AAARR Growth** : `Enterprise_OS_Blueprint_Kit/prompts/aaarr_growth_signal_pack.md` (11 prompts)
- **Architecture parent** : `Enterprise_OS_Blueprint_Kit/BLUEPRINT.md` (Mark Kashef, canonique, intouche)
- **Trace doctrine** : `ASpace_OS_V2/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/30_decisions/ADR-LD01-011_omk_nexus_bos_poc_initiation.md`

## Tier mapping

| Tier | Cas canon | Niche | Equipe | Compliance |
|---|---|---|---|---|
| T0 | solo-consultant | Coaching solo / consulting | 1 personne | aucune |
| **T1** | **omk-nexus-coaching-agency** (CE CAS) | **B2B coaching agencies** | **2-10 personnes** | **EU AI Act awareness** |
| T1 | northgate-law | Cabinet d'avocats | 2-10 personnes | Legal privilege |
| T2 | riverside-clinic | Clinique sante | 10-50 personnes | HIPAA |

## Cible chiffree (per Gemini Deep Research 2026-07-05)

- **Forfait client** : $1 000/mois par client premium
- **Volume cible** : 100 clients = $1.2M ARR
- **Marge nette** : > 90% (runtime quasi-fixe via Plan MiniMax 5.1B tokens / $50)
- **Equipe PoC** : 2-5 personnes (A0 + Abdaty + 1-3 beta-coachs Phase 2)
- **Horizon** : Q3 2026 (12WY 06/15 -> 09/07) pour Phase 1-3

## Anti-patterns (suite de ADR-LD01-011)

- Ne JAMAIS deployer en AWS reel avant Phase 2 validee (gated HITL A0)
- Ne JAMAIS recruter beta-coachs avant PoC specs validees (gated HITL A0)
- Ne JAMAIS deployer le DLP complet Supabase avant premier client signe (Phase 2 -> 3)
- Ne JAMAIS utiliser Opus tier (cout trop eleve, value-add incertain Phase 1)
- Ne JAMAIS muter les fichiers canon Enterprise_OS_Blueprint_Kit/BLUEPRINT.md
