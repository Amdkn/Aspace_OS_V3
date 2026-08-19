---
type: Concept
title: Collisions SDD-009 et SDD-010 — deux numéros, deux conflits
description: Les collisions internes de la chaîne numérotée : SDD-009_dashboard-governance vs SDD-009_shadow-L2-business-os, et SDD-010_meta-cloture vs SDD-010_UPDATED_shadow-L0-IA. Deux paires, deux causes différentes.
tags: [sdd, collision, sdd-009, sdd-010, dashboard, shadow, meta-cloture, ambiguite]
generated: { by: minimax-m3, at: 2026-08-19T15:45:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T15:45:00Z }
sources:
  - id: sdd-009-dashboard-direct
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-009_dashboard-governance.md"
    title: SDD-009 Dashboard de Gouvernance d'Infrastructure (lu)
    last_modified: 2026-06-04
  - id: sdd-009-shadow-direct
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-009_shadow-L2-business-os.md"
    title: SDD-009 Shadow L2 Business OS (lu — 2026-05-13)
    last_modified: 2026-05-13
  - id: sdd-010-meta-direct
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-010_meta-cloture-scope-13eme-semaine.md"
    title: SDD-010 Meta Clôture Scope (lu — 2026-05-13)
    last_modified: 2026-05-13
  - id: sdd-010-updated-direct
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-010_meta-cloture-scope-13eme-semaine_UPDATED_shadow-L0-IA.md"
    title: SDD-010 UPDATED Shadow L0-IA (lu)
    last_modified: 2026-07-13
okf_version: "0.2"
---

# Collisions SDD-009 et SDD-010 — deux numéros, deux conflits

## Le constat

Deux paires de collisions dans la chaîne numérotée vivante
(`05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/`) :

### Paire SDD-009

| Document | Statut | Date |
|---|---|---|
| `SDD-009_dashboard-governance.md` | **PLANNED** (jamais exécuté) | 2026-06-04 |
| `SDD-009_shadow-L2-business-os.md` | **RATIFIÉ** (9ème SDD de la pyramide A'Space OS V0) | 2026-05-13 |

### Paire SDD-010

| Document | Statut | Date |
|---|---|---|
| `SDD-010_meta-cloture-scope-13eme-semaine.md` | **RATIFIÉ** (10ème et dernier SDD du scope A'Space OS V0) | 2026-05-13 |
| `SDD-010_meta-cloture-scope-13eme-semaine_UPDATED_shadow-L0-IA.md` | **UPDATED** (mise à jour post-wargames W33-W42) | 2026-07-13 |

## Verdict

| Document | Verdict |
|---|---|
| SDD-009 Dashboard | `synthese-datee` — PLANNED jamais exécuté, mais statut conservé pour traçabilité |
| SDD-009 Shadow L2 | `canon` — RATIFIÉ, porte la matrice 3×8 (Airtable/ClickUp/Notion × 8 domaines) |
| SDD-010 Meta Clôture | `canon` — RATIFIÉ, pose la doctrine de la 13e semaine |
| SDD-010 UPDATED Shadow L0-IA | `synthese-datee` — mise à jour post-wargames, le suffixe `_UPDATED_shadow-L0-IA` est lui-même l'aveu de la collision |

## Causes différentes

### SDD-009 : collision entre domaines disjoints

Les deux SDD-009 traitent de domaines disjoints :

- `dashboard-governance` → **L0 Tech OS** (gouvernance infrastructure)
- `shadow-L2-business-os` → **L2 Business Pulse** (matrice 3×8)

La collision vient probablement du fait que la numérotation
décimale plate (000 → 010) n'a pas de critère de routing par couche.
C'est un **symptôme** de la numérotation plate.

### SDD-010 : collision chronologique interne

Les deux SDD-010 sont **le même document à deux moments** :

- 2026-05-13 : version ratifiée d'origine (la doctrine de la 13e
  semaine).
- 2026-07-13 : version UPDATED post-wargames W33-W42 (ajout du
  Shadow L0-IA dans le scope).

Le suffixe `_UPDATED_shadow-L0-IA` est l'**aveu explicite** que
l'auteur a renommé le fichier pour signaler la mise à jour, **sans
changer le numéro**. C'est une collision volontaire — pas un
conflit.

## Source du décompte

`find .../05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/` →
17 fichiers. Décompte :

- 1 × SDD-000
- 1 × SDD-000b
- 1 × SDD-000c
- 1 × SDD-001
- 1 × SDD-002
- 1 × SDD-003
- 1 × SDD-004
- 1 × SDD-005
- 1 × SDD-006
- 1 × SDD-007
- 1 × SDD-008
- **2 × SDD-009** (collision)
- 1 × SDD-010
- **2 × SDD-010 UPDATED** (collision)

## Concepts liés

- [[concept-sdd-006-collision]] — la collision SDD-006 (entre
  deux arborescences).
- [[concept-sdd-renaming-no-content]] — le renommage sans mise à
  jour du contenu.
