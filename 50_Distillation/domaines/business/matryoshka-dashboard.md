---
type: Concept
title: Matryoshka Dashboard — la couche qui se déplie à la bonne cadence
description: Le Dashboard du CEO est une Matriochka : Life Wheel > Business Wheel > Domain Wheel > Rock Wheel. La couche juste se déplie pour A0 à la bonne cadence, pas toutes les couches en même temps.
tags: [matryoshka, dashboard, adr-infra-003, life-wheel, business-wheel]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: SUMMERS_VERSE_MANIFEST
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/SUMMERS_VERSE_MANIFEST.md"
    title: Summer's Verse Manifest — CEO's Desktop
    last_modified: "2026-06-07"
  - id: README_CEO_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/README.md"
    title: README — CEO's Desktop
    last_modified: "2026-06-07"
  - id: MANIFEST_CEO_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/MANIFEST.md"
    title: Manifest — ceo-desktop
    last_modified: "2026-07-13"
  - id: ADR-INFRA-003
    resource: "30_Business_OS/10_Projects/ceo-desktop/CLAUDE.md (référencé)"
    title: ADR-INFRA-003 — CEO Dashboard Matryoshka
    last_modified: "2026-06-07"
okf_version: "0.2"
---

# Matryoshka Dashboard — la couche qui se déplie à la bonne cadence

> **Une seule chose à retenir.** Le CEO's Desktop n'affiche pas tout à A0 tout le temps ; il **déplie la couche juste** selon la cadence du SOB consulté.

## Énoncé canonique

> Matryoshka principle (ADR-INFRA-003): the Life Wheel holds the Business Wheel, the Business Wheel holds the Domain Wheels, the Domain Wheels hold the Rock Wheels. The CEO's Desktop surfaces the right layer to A0 at the right cadence. (`SUMMERS_VERSE_MANIFEST.md`)

## La pile (extérieure → intérieure)

| Couche                | Contenu                              | Cadence d'affichage typique     |
|-----------------------|--------------------------------------|--------------------------------|
| **Life Wheel**        | La vie entière d'A0                  | quotidien (intention)          |
| **Business Wheel**    | Les 8 SOB + cadences                 | hebdomadaire à mensuel          |
| **Domain Wheel**      | Un SOB particulier (Growth, Sales, IT, …) | selon cadence du SOB      |
| **Rock Wheel**        | Les Rocks actifs d'un SOB            | quotidien pendant le 12WY      |

## Pourquoi cette structure

- **Anti-bruit.** A0 lit son desktop en moins de 90 secondes (cible Phase 2). Voir les 8 cadences empilées en permanence serait illisible.
- **Cadence = profondeur.** Un SOB à cadence quotidienne (Cyborg/IT) déplie ses Rocks au quotidien ; un SOB à cadence trimestrielle (Aquaman/Legal) déplie ses Rocks moins souvent mais sur la même profondeur.
- **Le desktop surfaces drift; it does not fix it.** La règle est répétée verbatim dans `01_NORTH_STAR_1Y_3Y_10Y.md` : A0 fixes the drift, the desktop surfaces it.

## Ce que ce n'est pas

- Pas un dashboard avec 23 tuiles empilées. C'est une **navigation** entre couches, pas une vue unique.
- Pas un outil de reporting RH. Le Rock Wheel ne montre pas les heures des gens ; il montre les Rocks eux-mêmes.
- Pas une métaphore. La pile est l'architecture réelle de la couche `apps/` Phase 2 (qui n'est pas encore bâtie en Phase 1).

## Conséquence opérationnelle

Toute feature desktop qui ne se déplie pas sur **une seule** couche viole le principe. Un dashboard qui mélange Rocks de 8 SOB en permanence (sans sélection) est un anti-pattern : il rend l'utilisateur sourd à la cadence propre de chaque domaine.
