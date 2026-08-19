---
type: Concept
title: Famille WARMODE — 10 ADR postures (inversion freins/releases, portes, fenêtres)
description: La famille WARMODE (10 ADR) pose les postures opérationnelles : inversion freins/releases, portes over-freins, fenêtre Fable bypass, paperclip utile Kardashev conduction.
tags: [adr, warmode, posture, inversion, kardashev, paperclip]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-WARMODE-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L0_Tech_OS/ADR-WARMODE-001_posture-inversion-freins-releases.md"
    title: WARMODE 001 — Posture Inversion Freins/Releases
    last_modified: "2026-07-15"
  - id: ADR-WARMODE-002
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-WARMODE-002_portes-over-freins.md"
    title: WARMODE 002 — Portes over Freins
    last_modified: "2026-07-26"
  - id: ADR-WARMODE-004
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-WARMODE-004_paperclip-utile-kardashev-conduction.md"
    title: WARMODE 004 — Paperclip utile Kardashev Conduction
    last_modified: "2026-07-26"
okf_version: "0.2"
---

# Famille WARMODE — 10 ADR postures (inversion freins/releases, portes, fenêtres)

## Résumé

La famille **WARMODE** (10 ADR) pose les **postures opérationnelles** de l'organisation. Ces ADR renversent les postures classiques « tout bloqué par défaut » au profit de postures « portes ouvertes par défaut avec quelques verrous ciblés ».

## Les 10 ADR WARMODE

| ADR | Sujet | Date |
|---|---|---|
| `ADR-WARMODE-001` | Posture Inversion Freins/Releases | 2026-07-15 |
| `ADR-WARMODE-002` | Portes over Freins (première version) | 2026-07-26 |
| `ADR-WARMODE-002` (autre) | Portes over Freins — Beth seul veto | 2026-07-26 |
| `ADR-WARMODE-003` | Fenêtre Fable bypass Beth temporaire | 2026-07-26 |
| `ADR-WARMODE-004` | Paperclip utile Kardashev Conduction | 2026-07-26 |

Auxquels s'ajoutent 5 ADR WARMODE annexes (META_Organization/_TRASH_2026-07-26, non ratifiés).

## ADR-WARMODE-001 : l'inversion Freins/Releases

C'est l'ADR central de la famille. Il pose que pendant un cycle compressé, on **inverses** la posture classique :

> **Posture C traditionnelle (tout DISABLED/gated/PROPOSED par défaut)** — pour la durée d'un cycle compressé.

La posture par défaut devient « portes ouvertes », et les rares verrous sont nommés explicitement.

## ADR-WARMODE-002 : Portes over Freins — Beth seul veto

Deux versions de WARMODE-002 cohabitent :

1. La version générique `portes-over-freins.md`
2. La version spécifique `portes-over-freins-beth-seul-veto.md`

La deuxième précise que **Beth** (le gatekeeper humain) est le seul habilité à poser un veto dans cette posture. Tous les autres agents sont en mode "porte ouverte".

## ADR-WARMODE-004 : Paperclip utile Kardashev

C'est la doctrine Kardashev du paperclip : le risque paperclip (maximisation sans fin) est transformé en **utile Kardashev** (conduction vers la civilisation autonome). Doctrine ratifiée 2026-07-26.

## Statut vis-à-vis de V3

**canon** sur les 5 ADR principaux. Les 5 WARMODE annexes en `_TRASH_2026-07-26_pre_posture_pivot/` sont des drafts pré-pivot, **non ratifiés** — mais ils témoignent du débat doctrinal.

## Le verdict de cette distillation

**canon** pour les postures affirmées. **orphelin** pour les 5 drafts `_TRASH_2026-07-26_pre_posture_pivot` qui n'ont jamais été ratifiés (mais restent consultables pour mémoire).

## Liens

- Voir aussi : `concept-famille-meta.md` (les doctrines META)
- Voir aussi : `concept-famille-loop.md` (les cadences LOOP)