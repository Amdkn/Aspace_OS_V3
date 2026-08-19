---
type: Concept
title: Famille META — 8 ADR doctrines (anti-paresse, autonomie, modèle-agnostique, hooks)
description: La famille META (8 ADR) pose les doctrines méthodologiques : anti-paresse verify-before-assert, autonomie by design, modèle-agnostique runtime, hooks automation, d6 root causes catalog.
tags: [adr, meta, doctrine, anti-paresse, autonomie, hooks]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-META-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/META_Organization/ADR-META-001_anti-paresse-verify-before-assert.md"
    title: META 001 — Anti-Paresse verify-before-assert
    last_modified: "2026-07-15"
  - id: ADR-META-002
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/META_Organization/ADR-META-002_autonomy-by-design.md"
    title: META 002 — Autonomie by design
    last_modified: "2026-07-15"
  - id: ADR-META-006
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/META_Organization/ADR-META-006_d6-root-causes-catalog.md"
    title: META 006 — D6 Root Causes Catalog
    last_modified: "2026-07-26"
okf_version: "0.2"
---

# Famille META — 8 ADR doctrines (anti-paresse, autonomie, modèle-agnostique, hooks)

## Résumé

La famille **META** (8 ADR) pose les **doctrines méthodologiques** qui s'appliquent transversalement aux autres familles. Ce sont les méta-règles que tous les autres ADR citent dans leur champ `doctrine_anchors`.

## Les 8 ADR META

| ADR | Sujet |
|---|---|
| `ADR-META-001` | Anti-Paresse verify-before-assert |
| `ADR-META-002` | Autonomie by design |
| `ADR-META-003` | Modèle-Agnostique Runtime Doctrine |
| `ADR-META-004` | Doctrine Anti-Paresse Linkage |
| `ADR-META-005` | Hooks Automation |
| `ADR-META-006` | D6 Root Causes Catalog (deux versions : root causes + droid whispering) |
| `ADR-META-006` (autre) | Droid Whispering Doctrine |

**Note** : ADR-META-006 apparaît deux fois, l'une pour le catalogue root causes, l'autre pour le droid whispering. **Collision de numérotation.**

## ADR-META-001 : Anti-Paresse verify-before-assert

Le document de référence méthodologique. Ses D1-D8 sont citées par la majorité des ADR L2 :

- **D1** : verify-before-assert — ne jamais affirmer un fait non vérifié
- **D2** : research FIRST — lire avant d'écrire
- **D3** : sources vérifiables — chaque assertion doit pouvoir être ramenée à un chemin
- **D4** : append-only — ne pas réécrire, amender
- **D5-D8** : autres disciplines anti-paresse

Ce document est **le plus cité** du corpus. Il apparaît comme `doctrine_anchor` dans pratiquement tous les ADR L2 ratifiés en juillet 2026.

## ADR-META-002 : Autonomie by design

L'autonomie des agents est un principe cardinal. Toute décision qui retire de l'autonomie à un agent (ex : forcer une validation HITL sur une décision routinière) doit être justifiée.

## ADR-META-006 : D6 Root Causes Catalog

Le catalogue D6 des root causes est la base de la culture post-mortem A'Space. Chaque incident est classé selon ce catalogue (over-fire, désengagement, scope creep, etc.).

## Statut vis-à-vis de V3

**canon** sur tous les 8 ADR. Aucune dépréciation.

## Le verdict de cette distillation

**canon**. La famille META est **le** socle doctrinal transversal. Aucune distillation ne doit la rendre obsolète.

## Liens

- Voir aussi : `concept-famille-warmode.md` (les postures WARMODE)
- Voir aussi : `concept-famille-loop.md` (les cadences LOOP)