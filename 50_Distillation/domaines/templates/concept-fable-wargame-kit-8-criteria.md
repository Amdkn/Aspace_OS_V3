---
type: Concept
title: fable-wargame-kit — les 8 critères d'un wargame qui passe + un exemple OMK-C réel
description: Kit de 15 fichiers qui pose 8 critères pour qu'un plan de bataille soit exécutable blind + un LEDGER.md prouvant son utilisation par A'Space V2 (mission Runbook C SaaS Auth OMK-C phase C, 2026-07-15).
tags: [templates, fable-wargame, success-criteria, ledger, omk, runbook-c, trace]
generated: { by: minimax-m3, at: 2026-08-19T19:55:00Z }
verified:
  - { by: process:lecture_fable_wargame_integral_et_ledger_omk_c, at: 2026-08-19T19:55:00Z }
sources:
  - id: wargame-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/fable-wargame-kit/README.md"
    title: "Fable Wargame Kit — README"
    last_modified: 2026-05
  - id: wargame-success
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/fable-wargame-kit/fable-last-week/SUCCESS.md"
    title: "Fable Wargame — 8 critères de validation"
    last_modified: 2026-05
  - id: wargame-ledger
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/fable-wargame-kit/fable-last-week/LEDGER.md"
    title: "Fable Wargame — LEDGER (mission Runbook C SaaS Auth OMK-C, 2026-07-15)"
    last_modified: 2026-07-15
  - id: wargame-tasks-listing
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/fable-wargame-kit/fable-last-week/tasks"
    title: "10 missions (01-website, 02-copy, 03-localai, 04-tax, 05-offer, 06-chatbot, 07-bugs, 08-model, 09-competitors, 10-automation)"
    last_modified: 2026-05
  - id: wargame-laundry-list-pdf
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/fable-wargame-kit/The Laundry List.pdf"
    title: "10 wargame orders visuels"
    last_modified: 2026-05
okf_version: "0.2"
---

# fable-wargame-kit — 8 critères + un exemple OMK-C réel

## Périmètre

15 fichiers : README racine + `fable-last-week/` (SUCCESS.md, LEDGER.md, 10 missions, wargames/) + The Laundry List.pdf.

## Verdict global

**`synthese-datee`** — daté sur le contexte (Fable 5 leaving July 7), canon sur les 8 critères.

**Daté sur :** la phrase « Fable 5 leaves subscriptions on July 7 and moves to usage credits » — événement daté, et la CTA vers la communauté Skool (`https://www.skool.com/earlyaidopters/about`) qui n'est pas le canal A'Space.

**Canon sur :** les **8 critères** d'un wargame qui passe. C'est le cœur réutilisable du kit, applicable à toute doctrine ou opération.

## Les 8 critères (verbatim de `SUCCESS.md`)

1. **Every move states its expected observation** — exactly what you should see if the move worked.
2. **Every move carries its most likely failure** — the cause that failure signals, and the counter-move.
3. **Every fork has a trigger** — if you observe X, take route B. No judgment calls left to the executor.
4. **Every assumption recon could not settle** is marked `RECON NEEDED` with the exact check that settles it.
5. **Abort conditions exist** — the moments to stop and flag rather than improvise.
6. **Verification is spelled out** — which runs the executor performs, when, and what pass looks like for each.
7. **It has survived a red-team pass** — the doc records the attack that failed against it, and the patch born from the attack that did not.
8. **It is executable blind** — a mid-tier model could run the mission end to end without asking a single question.

Ce 8ᵉ critère est remarquable : il impose que le plan soit **exécutable par un agent médiocre sans intervention humaine**. C'est une discipline opérationnelle extrêmement exigeante, et c'est la raison d'être du kit.

## Trace dans V3 — l'exemple OMK-C

Le `LEDGER.md` documente **une mission réelle** menée par A'Space, datée 2026-07-15 :

> **Mission : Runbook C SaaS Auth — Picard Phase 3 R-OMK-C**

Métadonnées verbatim :
- **Location** : `C:/Users/amado/agent-os/worktrees/picard-OMK-C-phase-C/`
- **Runbook source** : `ASpace_OS_V2/30_Business_OS/10_Projects/omk/_doctrine/runbooks/runbook-C-saas-auth.md` (269 l., 14 292 B)
- **Chart source** : `ASpace_OS_V2/30_Business_OS/10_Projects/omk/_doctrine/chartes/phase_c_saas_auth.md` (52 l.)
- **B3 squad** : Mr. Fantastic (AuthProvider lead) + Ikaris AI-Act (Pilier 5 lead) + Kang Prime (JWT hook Cloud)

**Moves executed (M1 + M3 + M5 — all SAFE)** :
- M1 : PII audit grep 0 hits + shipped `src/lib/redact.ts` (156 l., sha256 `0073b12e6494ae0b1513eb728e4d28d3ef03bd5ef4d822d7afaa2e987941ecb5`)
- M3 : `grep -rn "Admin User" src/` → 0 hits (DoD-1 ✅) ; `npm run lint` → 0 errors in `src/auth/` + `src/lib/redact.ts`
- M5 : wiki/log.md pulse + LEDGER entry

**Moves STOPPED — A0 HITL pending (M2 + M4)** :
- M2 : JWT hook Cloud re-provision — manual UI step (Supabase Cloud Dashboard) → A0 HITL gated
- M4 : Vercel Authentication OFF × project `omk-saas-os` — manual UI step → A0 HITL gated

**Self-grade vs SUCCESS-ASPACE 12 pts** :
- V1-V8 vérifications passent (8/8 V-checks)
- D6 honesty : 4 gaps flagged, score 9/12 SUCCESS-ASPACE équivalent
- Les 3 erreurs ProductView.tsx sont hors scope Phase C — flaggés pour Phase D charter

C'est la **preuve** que ce kit a été **utilisé** comme cadre opérationnel sur OMK-C. Verdict : `canon` sur la trace (LEDGER), `synthese-datee` sur le kit lui-même.

## Les 10 missions du kit

Chaque mission dans `tasks/01-website.md` à `10-automation.md` est un brief fill-in-the-blank pour un wargame dans un domaine :

| Mission | Domaine |
|---|---|
| 01-website | site web |
| 02-copy | rédaction |
| 03-localai | LLM local |
| 04-tax | fiscalité |
| 05-offer | offre commerciale |
| 06-chatbot | agent conversationnel |
| 07-bugs | debug |
| 08-model | choix de modèle |
| 09-competitors | analyse concurrentielle |
| 10-automation | automatisation |

Ces missions ne sont **pas utilisées** directement dans V3 (qui a son propre backlog OMK), mais le **format** est réutilisable.

## Concepts liés

- [[concept-fable-mindset-12-principles]] — le Mindset est la philosophie, le Wargame est la mise en pratique
- [[concept-kits-utilisation-trace]] — ce kit est l'un des rares à avoir laissé une trace vérifiable
