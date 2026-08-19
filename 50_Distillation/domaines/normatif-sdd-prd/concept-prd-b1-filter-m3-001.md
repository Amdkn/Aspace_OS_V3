---
type: Concept
title: PRD-B1-FILTER-M3-001 — Délégation filtre B1 (M3)
description: PRD qui pose le filtre B1 de délégation vers M3 (MiniMax M3) — la gate opérationnelle qui distingue ce qui peut être délégué (par M3 en arrière-plan) de ce qui doit rester en session A1/A2 active. Économie de quotas + cohérence de boucle.
tags: [prd, b1-filter, m3, delegation, quotas, economie, boucle, gate]
generated: { by: minimax-m3, at: 2026-08-19T15:20:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T15:20:00Z }
sources:
  - id: prd-b1-filter-direct
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/PRD/PRD-B1-FILTER-M3-001_delegation-filtre-b1.md"
    title: PRD-B1-FILTER-M3-001 (lu — délégation filtre B1)
    last_modified: 2026-07-12
okf_version: "0.2"
---

# PRD-B1-FILTER-M3-001 — Délégation filtre B1 (M3)

## Périmètre

Le PRD pose la **gate opérationnelle** qui distingue ce qui peut
être délégué à **M3 (MiniMax M3)** en arrière-plan de ce qui doit
rester en **session A1/A2 active** :

- **Délégable à M3** : scans de corpus, lints, migrations, comptages,
  réécritures en masse, audits, toute tâche dépassant ~20 appels
  d'outils ou traitant > 200 fichiers.
- **Resté en session A1/A2** : décisions, arbitrages, vérification
  du travail délégué, tâches courtes < 5 appels d'outils.

## Trois invariants

1. **Économie de quotas** — les modèles Anthropic sont la ressource
   rare. M3 ne consomme pas ces quotas. Donc le travail long est
   défléchi vers M3 par défaut.
2. **Vérification obligatoire** — un agent délégué n'est jamais cru
   sur parole. Sa sortie se vérifie (par capture, mesure, ou lecture
   directe).
3. **Cohérence de boucle** — la délégation respecte la hiérarchie
   A0/A1/A2/A3. M3 n'invoque pas A2, et un A2 ne délègue pas à A1.

## Verdict

**canon** — le filtre B1 est l'un des rares PRD post-Constitution v1.0
(2026-07-12) qui pose une doctrine d'**économie opérationnelle**, pas
une doctrine d'architecture. Sa valeur va croissante avec le coût
des quotas.

## Source du décompte

`find .../04_From_V2_Root/_SPECS/PRD/` → 4 fichiers (3 numérotés
B1/INDEX/NEXUS + 1 `.bak` miroir de PORTFOLIO pré-M6).

## Concepts liés

- [[concept-prd-nexus-evolution-ia-001]] — l'offre commerciale qui
  exploite ce filtre.
- [[concept-prd-portfolio-b1-franchise]] — l'index portfolio qui
  contient les 3 PRD canon (B1-FILTER, NEXUS, PORTFOLIO).
