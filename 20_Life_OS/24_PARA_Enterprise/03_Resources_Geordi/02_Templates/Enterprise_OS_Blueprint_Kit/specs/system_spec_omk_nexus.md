---
type: spec-override
id: SPEC_OMK_SYSTEM
title: "SYSTEM_SPEC OMK Nexus BOS - Tier T1, niche coaching B2B"
status: RATIFIED
date: 2026-07-05T09:45:00-04:00
author: HA (A3 Picard in PARA, projets owner H10)
refines: specs/SYSTEM_SPEC.md (template canon, intouchable)
sister: ADR-LD01-011_omk_nexus_bos_poc_initiation
append_only: true
---

# SYSTEM_SPEC - OMK Nexus BOS (override Tier T1)

> Override fill-in du template canon `specs/SYSTEM_SPEC.md` (intouche). Ce fichier est cree en append-only dans le Blueprint Kit par ADR-LD01-011.

## Identity
- Account id: `omk-nexus-bos-prod` (single AWS account, omk-nexus AWS Organization)
- Region: `us-east-1` (primary), `eu-west-1` (secondary pour EU AI Act)
- Owner: Amadeus Kone (A0) + Abdaty (ingenieur, A3 Spock-areas)
- Recommended deploy tier: **standard** (= T1, entre hobby et pro)

## Data
- What data will this handle: **Donnees PII de clients coachés** (noms, emails LinkedIn, transcripts d'appels, playbooks internes des agences), **transcripts de ventes** (Zoom/Gong), **scraping signals publics** (Apollo, Reddit, LinkedIn Sales Navigator)
- Sensitivity: **confidential** (pas regule HIPAA, mais EU AI Act awareness)
- Any of it not yours to hand over: **Oui** - PII clients = donnees proprietaires du coach, pas d'export cloud sans consentement explicite
- Retention needs: **7 ans** pour audit trail (write-once S3 Object Lock per Blueprint section 6), **2 ans** pour transcripts operationnels, **90 jours** pour caches semantiques

## Jurisdiction and industry
- Jurisdiction(s): **France (primary), EU (secondary), US (pour clients transfrontaliers)**
- Industry: **Business Coaching / Business Development Services** (B2B SaaS services, pas medical)
- Rules that brings: **EU AI Act (transparency, human oversight), RGPD, pas HIPAA, pas FDA**. SOC2 decale Phase 2.

## Surfaces
- [x] Telegram (bot pour A0 + beta-coachs en early access)
- [x] Slack (pour les clients B2B agences, en option Phase 2)
- [x] Web dashboard (Agentic Dashboard - simulation du Quiz d'Acquisition)
- [ ] Email, [ ] SMS - hors scope PoC

## Models
- Allowed: **Claude Opus 4** (hard parts, validation finale), **Sonnet 4** (execution), **Haiku** (premier jet + formatage), **Open models local** (Llama 3 / Qwen 2.5 via Ollama) pour fallback no-outside-vendor
- Barred from sending prompts to any outside vendor: **Oui pour les PII clients** (Bedrock in-account obligatoire), **Non pour les scrapes publics** (modeles externes toleres en pre-traitement, resultat anonymise in-account ensuite)

## Team and roles
- People: **3-5 personnes au PoC** (A0 + Abdaty + 1-3 beta-coachs early access Phase 2)
- Roles needed: **viewer** (coachs clients, read-only sur leur data), **analyst** (beta-coachs avances), **operator** (A0 + Abdaty), **admin** (A0 seul), **owner** (A0, single point of veto per A1 Beth canon)

## Tools you're replacing
- Otter.ai / Gong (transcription manuelle appels -> auto via Bedrock)
- Notion SOPs (statiques -> Skills Agentiques executables en .md per Gemini T1 Ops)
- Lemlist / Instantly (email outreach -> AAARR signal prompts)
- HubSpot CRM basique (contacts -> DynamoDB L1 cognition table)
- Calendly (booking -> surface Telegram integree)

## Budget
- Monthly ceiling: **$500/mois infra + $50/mois Plan MiniMax forfait** = $550/mois fixe
- Daily cap target: **$20/jour** (fail-closed cost cap per Blueprint section 3)

## Non-negotiables
- **Zero fuite PII client hors compte AWS** (DLP-light subset 7 patterns minimum)
- **Write-once audit trail 7 ans** (S3 Object Lock governance mode)
- **A1 Beth = seul veto humain** (per ADR-WARMODE-002, pas automatisable)
- **MiniMax plan forfaitaire** uniquement (pas de variable cost runaway)

## Open questions
- DLP complet Supabase section 6 Blueprint : **declenche Phase 2** au premier client signe (gated HITL A0)
- Bedrock access en compte AWS neuf : Phase 2 (SOPF etait template solo, pas OMK)
- Beta-coachs early access : **3 noms Phase 2** (gated HITL A0), hors scope PoC specs
- Compliance EU AI Act : **documente Phase 2**, pas bloquant PoC
