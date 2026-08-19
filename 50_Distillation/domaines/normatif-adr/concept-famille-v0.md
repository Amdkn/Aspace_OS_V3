---
type: Concept
title: Famille V0 — 46 ADR de phase, format "build phase" non formel
description: La famille V0 (ADR-V0.1 à ADR-V0.8.8) documente les phases de construction du Life OS V0. Le format est court, sans frontmatter, sans statut — différent des L2.
tags: [adr, v0, life-os, phase-build, format-non-formel]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-V0.1
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/ADR/ADR-V0.1_Rilcot.md"
    title: V0.1 — Rilcot (le tout premier)
    last_modified: "2026-05-15"
  - id: ADR-V0.4.5
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/ADR/ADR-V0.4.5_LaboSpock.md"
    title: V0.4.5 — UX Spock Laboratoire Areas
    last_modified: "2026-05-25"
  - id: ADR-V0.8.8
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/ADR/ADR-V0.8.8_NecropoleDrones.md"
    title: V0.8.8 — Nécropole Drones (dernier de la série)
    last_modified: "2026-06-15"
okf_version: "0.2"
---

# Famille V0 — 46 ADR de phase, format "build phase" non formel

## Résumé

La famille **V0** regroupe 46 ADR identifiés par le préfixe `ADR-V0.X.Y_<topic>.md`. C'est la famille la plus nombreuse. Leur format diffère des L2 : ce ne sont pas des ADR « classiques » avec frontmatter et statut, mais des **notes de phase de construction** du Life OS V0 (les itérations 0.1 à 0.8.8).

## Le format V0

Un ADR V0 typique contient :

- un titre `# ADR-V0.X.Y — <sujet>`
- un sous-titre `> **Phase** : V0.X.Y`
- une section `## Décision : <la décision>`
- un tableau `### Plan DDD Tabulé` avec colonnes `Étape | Fichier | Description | Gate`

**Pas de frontmatter YAML.** Pas de `status:`. Pas de `supersedes:`. Pas de `related:`. C'est une décision exécutée, pas un acte de gouvernance.

## Localisation source

Source canonique : `04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/ADR/`. Le dossier `_Life-OS-2026-clone/` est le **clone de travail** qui contient les originaux.

Exemples :

- `ADR-V0.4.5_LaboSpock.md` — `> **Phase** : V0.4.5 / ## Décision : Pillar Dashboard en Overlay Local`
- `ADR-V0.4.6_ScannerFlotte.md` — `> **Phase** : V0.4.6 / ## Décision : CSS Pure pour les Visualisations`
- `ADR-V0.8.8_NecropoleDrones.md` — dernier de la série (vérification par comptage)

## Les phases observées

| Phase | Sujets typiques |
|---|---|
| V0.1 à V0.2.9 | UI Layout, Ikigai, PARA, 12WY, GTD, DEAL |
| V0.3.x | Environnement, ZoraCore, FleetGateway, MemoryState, DoctrineBeth |
| V0.4.x | UnificationNoyau, UXPicard, RoutageSpockData, PontsVivants, LaboSpock, ScannerFlotte, FractaleSummers, ForgeCreation, ForgeLiaison |
| V0.5.x | ForgePrincipes, PontIrrigation, LifeWheelAutomatisée |
| V0.6.x | RefonteTypologique, MoteurExecution, NexusTemporel, VisionForge, GoalForge, TacticForge, GeneseRoutage, VisionCommand, GoalCommand |
| V0.7.x | LoiPersistance, TripleCablage, OmniCapture, EngageView |
| V0.8.x | MigrationSouveraine, SasDecompression, PipelineDEAL, NexusEconomique, RadarFrictions, MoteurRentabilite, PontExecutif, NecropoleDrones |

## Statut vis-à-vis de V3

**synthese-datee**. Les ADR V0 documentent la **trajectoire** du Life OS V0 → V3. Ils restent la **seule source** pour comprendre pourquoi une décision précise a été prise à un moment précis (ex : pourquoi CSS pur plutôt que Chart.js — réponse dans V0.4.6). En V3, ces décisions sont absorbées par le code et les Blueprints `12_Blueprints/02-ADR/`, mais **sans la justification originelle**.

Le point obsolète : la numérotation V0.X.Y n'a plus cours en V3 (les phases sont devenues des couches : L0 Tech, L1 Life, L2 Business). Le contenu reste utile, la nomenclature est caduque.

## Le verdict de cette distillation

**synthese-datee**. La famille V0 reste la meilleure source sur 44 de ses 46 ADR (la justification originelle d'une décision UI/UX). La nomenclature V0.X.Y est obsolète ; le contenu est canonique.

## Liens

- Voir aussi : `concept-famille-ld01.md` (la famille qui succède à V0 dans LD01)
- Voir aussi : `concept-famille-fwk.md` (FWK 011 à 020 = les frameworks canoniques)