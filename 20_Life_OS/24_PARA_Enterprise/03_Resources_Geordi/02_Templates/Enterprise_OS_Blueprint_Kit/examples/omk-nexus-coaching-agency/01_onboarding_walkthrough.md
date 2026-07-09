---
type: example-onboarding-walkthrough
id: OMK_NEXUS_ONBOARDING_WALKTHROUGH
title: "OMK Nexus BOS - Onboarding Walkthrough (prospect/coach)"
status: RATIFIED
date: 2026-07-05T09:45:00-04:00
author: HA
sister: examples/omk-nexus-coaching-agency/README.md
append_only: true
---

# 01 - Onboarding Walkthrough

> Pas-a-pas pour un prospect/coach qui decouvre OMK Nexus BOS. Suivre ce walkthrough dans l'ordre.

## Step 0 - Tu es qui ?

Tu es soit :
- **(A) Fondateur d'un cabinet de coaching B2B premium** (5-50 clients actifs, $50k-$500k MRR)
- **(B) Directeur d'une agence de business development** (10-100 clients actifs, $100k-$1M MRR)

Dans les deux cas, tu as le meme probleme : **les couts fixes mensuels te mangent la marge**, et tu veux une architecture agentique qui :
- Reduit ces couts fixes de 80%+
- Automatise le pipeline d'acquisition par signaux (pas par spam)
- Livre une experience onboarding immediate (Quiz d'Acquisition self-serve)
- Garde le controle humain sur la relation client

## Step 1 - Découvrir l'architecture (15 min)

Ouvre `Enterprise_OS_Blueprint_Kit/BLUEPRINT.md` section 2-3 ("Architecture" et "The turn chokepoint"). C'est le plan de reference. Pour OMK Nexus BOS, on l'a override dans `specs/architecture_spec_omk_nexus.md`. Lis les 3 sections :

1. **Triptyque 1 (Backbone)** : People / IT / Ops - l'organisation qui construit
2. **Triptyque 2 (Front-End)** : Product / Growth / Sales - l'expansion commerciale
3. **Duo (Garde-Fous)** : Finance / Legal - la perennite du systeme

## Step 2 - Comprendre le pricing (10 min)

Ouvre `specs/cost_spec_omk_nexus.md`. Le point cle :
- **$1 000/mois par client premium**, cible 100 clients = $1.2M ARR
- **Marge nette > 90%** parce que le runtime est quasi-fixe via le Plan MiniMax 5.1B tokens / $50 + cache semantique local

Compare a Medvi : $1.8B ARR avec 2 employes (lui + son frere), mais chute FDA. OMK Nexus BOS evite la FDA en ciblant le B2B coaching au lieu du medical grand public.

## Step 3 - Lancer le Quiz d'Acquisition (15 min)

Ouvre `03_quiz_acquisition_integration.md` (dans ce dossier). C'est la demo live du tunnel de conversion OMK. Le prospect entre ses volumes d'activite, le systeme fait tourner une simulation en arriere-plan, et delivre instantanement une cartographie de pertes financieres ("Vous depensez $X en RH et tokens inutiles, voici votre plan de liberation").

## Step 4 - Voir l'AAARR Growth en action (20 min)

Ouvre `Enterprise_OS_Blueprint_Kit/prompts/aaarr_growth_signal_pack.md`. C'est le pack de 11 prompts pour le signal acquisition (le Tier 2 du Triptyque). Chaque prompt est scripte pour etre invoque par un agent Bedrock Haiku tier, qualifie le signal selon AAARR (Acquisition / Activation / Retention / Recommandation / Revenu), et pre-redige des sequences d'approche hyper-specifiques.

## Step 5 - Comprendre la securite (10 min)

Ouvre `specs/security_spec_omk_nexus.md`. La cle :
- **DLP-light 7 patterns** en Phase 1 (PII basique, credentials AWS/GitHub/Slack, PEM keys, credit cards, SSNs)
- **DLP complet Blueprint section 6** (9 patterns) en Phase 2 des le premier client signe
- **Write-once audit trail 7 ans** (S3 Object Lock governance mode)
- **EU AI Act awareness** mais pas SOC2 en Phase 1 (decale Phase 2)

## Step 6 - Evaluer l'effort d'implementation (15 min)

Ouvre `specs/build_plan_omk_nexus.md`. Le plan en 3 phases :

- **Phase 1 (semaine 1-2, cible 07/19)** : PoC structurel, specs livrees (CETTE LIVRAISON)
- **Phase 2 (semaine 3-6, cible 08/16)** : DLP-light deploye, 3 beta-coachs, Quiz live
- **Phase 3 (semaine 7-13, cible 09/07+)** : 100 clients actifs, DLP complet, EU AI Act documente

**Effort humain total** : 2-5 personnes sur 13 semaines, dont la moitie en parallele sur Phase 2-3.

## Step 7 - Prendre la decision

Si tu veux aller plus loin, dis a A0 :
- "GO pour Phase 2" -> on te presente les 3 beta-coachs early access (gated HITL A0)
- "GO pour deploiement AWS reel" -> on lance le compte `omk-nexus-bos-prod` (gated HITL A0)
- "GO pour DLP complet Supabase" -> on monte les 9 patterns Blueprint (gated HITL A0)

Si tu veux juste explorer, ce dossier est suffisant pour evaluer. Les specs sont des donnees concretes, pas du marketing.
