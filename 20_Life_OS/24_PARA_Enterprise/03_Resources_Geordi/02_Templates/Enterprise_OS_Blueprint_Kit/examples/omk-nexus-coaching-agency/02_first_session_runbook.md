---
type: example-first-session-runbook
id: OMK_NEXUS_FIRST_SESSION_RUNBOOK
title: "OMK Nexus BOS - First Session Runbook (90 min)"
status: RATIFIED
date: 2026-07-05T09:45:00-04:00
author: HA
sister: examples/omk-nexus-coaching-agency/01_onboarding_walkthrough.md
append_only: true
---

# 02 - First Session Runbook (90 minutes)

> Runbook pour la premiere session live entre A0 et un prospect OMK Nexus BOS. Sequence en 5 etapes, duree totale 90 min.

## Pre-requis (avant la session)

1. Le prospect a lu `01_onboarding_walkthrough.md` (15-20 min de son cote)
2. A0 a prepare un Quiz d'Acquisition customise pour le prospect (secteur, taille d'equipe, MRR)
3. Les 3 beta-coachs early access sont identifiees (Phase 2) ou en cours de selection

## Etape 1 - Decouverte (15 min, A0 lead)

Objectif : comprendre le contexte prospect, pas pitcher OMK.

Questions a poser :
- Quel est votre secteur precis (coaching d'affaires / agence BD / autre) ?
- Quelle est votre taille d'equipe actuelle et votre MRR ?
- Quels outils vous coute le plus cher en mensuel (Otter.ai / Lemlist / HubSpot / Notion) ?
- Quelle est votre plus grande frustration operationnelle aujourd'hui ?
- Avez-vous deja tente l'automatisation par IA ? Si oui, qu'est-ce qui a foire ?

A0 prend des notes dans `wiki/log.md` (trace canon).

## Etape 2 - Quiz d'Acquisition live (20 min, prospect lead)

Le prospect ouvre le Quiz d'Acquisition dans l'Agentic Dashboard (simulation). Il entre ses volumes d'activite reels :
- Nombre d'appels de vente / semaine
- Nombre de transcripts analyses / mois
- Nombre de prospects contacts / semaine
- Nombre d'onboardings clients / mois
- Outils payants actuels + couts mensuels
- Taille de l'equipe (sales + ops + produit)

Le systeme fait tourner une simulation en arriere-plan (per Gemini T2 Sales : Sonnet tier) et delivre en ~30 secondes une **cartographie de pertes financieres** structuree en 4 axes :
1. **Couts fixes mensuels** (Otter, Lemlist, HubSpot, Notion, Calendly) -> projection d'economie avec OMK
2. **Couts variables token cloud** -> projection avec Plan MiniMax forfait
3. **Couts RH maintenance** (admin SOP, reporting) -> projection avec Triptyque 1 People/IT/Ops
4. **Couts d'acquisition** (Lemlist email blast inefficace) -> projection avec AAARR signal

Output : **"Vous depensez $X en RH et tokens inutiles, voici votre plan de liberation"** (closing par preuve ROI).

## Etape 3 - Analyse AAARR (25 min, A0 lead)

A0 montre le pack de 11 prompts AAARR (`prompts/aaarr_growth_signal_pack.md`) et explique comment le systeme qualifie les signaux automatiquement :

- **Acquisition** : 2 prompts qui scrapent Apollo (embauches directeurs commerciaux), Reddit (discussions goulots), LinkedIn Sales Navigator (signaux chauds)
- **Activation** : 3 prompts qui scoringent les signaux (>= 0.7 = qualified) et pre-redigent des sequences d'approche hyper-specifiques
- **Retention** : 2 prompts de nurture sequence (emails valeur, check-ins periodiques)
- **Recommandation** : 2 prompts de referral loop (coachs qui referent d'autres coachs)
- **Revenu** : 2 prompts de closing (Quiz -> Demo -> Retainer)

A0 lance 1-2 prompts en live sur un signal reel pour montrer la qualite du scoring.

## Etape 4 - Architecture & Securite (15 min, A0 lead)

A0 montre les 6 specs overrides (`specs/*.md`) et explique les points cles :
- Tier T1 (entre solo et law firm)
- DLP-light 7 patterns Phase 1, 9 patterns Phase 2
- Write-once audit 7 ans
- MiniMax plan forfaitaire (cout marginal par client < $5)
- Loop engineering rattachee : H10 input Picard, H1 aggregator Book, daily Squad B3

Objectif : le prospect comprend qu'il n'y a pas de pieges (pas HIPAA, pas FDA, EU AI Act aware, write-once audit).

## Etape 5 - Closing & Next Steps (15 min)

A0 propose 2 paths au prospect :

**Path A - Beta-coach early access (Phase 2)** :
- Le prospect devient 1 des 3 beta-coachs (gated HITL A0)
- Acces au Quiz d'Acquisition live + AAARR Growth pack
- 0$ pendant 60 jours (Phase 2), puis $1k/mois si signe
- Feedback loop hebdo avec A0

**Path B - Wait for Phase 3** :
- Le prospect attend la sortie officielle Phase 3 (cible 09/07+)
- Acces self-serve via le Quiz d'Acquisition public
- $1k/mois des le premier mois

A0 laisse le prospect choisir, prend RDV dans 7 jours pour follow-up.

## Post-session

A0 append un episode dans `calendar.md` (LD01_Business_Book/99_meta/calendar.md) avec :
- Timestamp de la session
- Nom du prospect + secteur
- Path choisi (A ou B)
- Score de l'opportunite (1-5)
- Next action (RDV follow-up, beta-coach candidate, etc.)

A0 met aussi a jour le `<proj>/MANIFEST.md` du projet OMK Nexus BOS avec le nouveau prospect en pipeline.

## Anti-patterns (a eviter pendant la session)

- Ne JAMAIS promettre de features non specifiees dans les 6 overrides
- Ne JAMAIS garantir un ROI chiffre precis (les projections sont des estimations, pas des garanties)
- Ne JAMAIS presser le prospect pour signer dans la session (laisser 7 jours de reflexion)
- Ne JAMAIS mentionner Medvi par nom (le prospect peut connaitre ou pas, mais on ne s'en vante pas)
- Ne JAMAIS promettre le DLP complet Phase 2 avant qu'il soit deploye
