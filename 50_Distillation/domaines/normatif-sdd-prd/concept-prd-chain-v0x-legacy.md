---
type: Concept
title: Chaîne PRD-V0.2.4 → PRD-V0.8.8 — les 44 PRD Legacy scellés
description: Les 44 Product Requirements Documents de la chaîne Legacy_V0.x (V0.2.4 → V0.8.8), distribués en miroir dans _SPECS/prds/ (45 avec antigravity-kit-fusion_PRD.md) et TOTAL_Spec/PRD/ (44), qui ferment la couche micro-applicative de chaque Framework App avant la migration V3.
tags: [prd, v0.x, legacy, uilayout, ikigaideep, paracomplete, 12wydisciplines, gtdcomplete, dealworkflow, environnement, zoracore, fleetgateway, memorystate, doctrinebeth, unificationnoyau, uxpicard, routagespockdata, pontsvivants, labospock, scannerflotte, fractalesummers, forgecreation, forgeliaison, forgeprincipes, pontirrigation, lifewheelautomatisée, refontetypologique, moteurexecution, nexustemporel, visionforge, goalforge, tacticforge, geneseroutage, visioncommand, goalcommand, loipersistance, triplecablage, omnicapture, engageview, migrationsouveraine, sasdecompression, pipelinedeal, nexuseconomique, radarfrictions, moteurrentabilite, pontexecutif, necropoledrones]
generated: { by: minimax-m3, at: 2026-08-19T14:40:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T14:40:00Z }
sources:
  - id: prd-root-specs
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Legacy_LifeOS_App_Specs_2026-05-22/_SPECS/prds/"
    title: Dossier _SPECS/prds/ (45 PRD dont antigravity-kit-fusion)
    last_modified: 2026-05-22
  - id: prd-root-total
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/PRD/"
    title: TOTAL_Spec/PRD/ (44 PRD V0.x — miroir partiel)
    last_modified: 2026-05-22
  - id: prd-v02-4-9-echantillon
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/PRD/PRD-V0.2.4_UILayout.md"
    title: PRD-V0.2.4 UI Layout (lu directement)
    last_modified: 2026-05-22
okf_version: "0.2"
---

# Chaîne PRD-V0.2.4 → PRD-V0.8.8 — les 44 PRD Legacy scellés

## Composition mesurée

44 PRD numérotés V0.2.4 → V0.8.8, plus 1 PRD orphelin
(`antigravity-kit-fusion_PRD.md` qui n'a pas de pendant dans TOTAL_Spec/PRD/).

| Plage | Phase | Couverture |
|---|---|---|
| **V0.2.4 → V0.2.9** (6 PRD) | UI Layout, Ikigai Deep, PARA Complete, 12WY Disciplines, GTD Complete, DEAL Workflow | chaque Framework App en profondeur |
| **V0.3.1 → V0.3.5** (5 PRD) | Environnement, Zora Core, Fleet Gateway, Memory State, Doctrine Beth | socle L1 |
| **V0.4.1 → V0.4.9** (9 PRD) | Unification Noyau, UX Picard, Routage Spock Data, Ponts Vivants, Labo Spock, Scanner Flotte, Fractale Summers, Forge Création, Forge Liaison | couche intermédiaire L0/L1/L2 |
| **V0.5.1 → V0.5.3** (3 PRD) | Forge Principes, Pont Irrigation, Life Wheel Automatisée | alignement V0.5 |
| **V0.6.1 → V0.6.9** (9 PRD) | Refonte Typologique, Moteur Exécution, Nexus Temporel, Vision Forge, Goal Forge, Tactic Forge, Genèse Routage, Vision Command, Goal Command | forges |
| **V0.7.1 → V0.7.4** (4 PRD) | Loi Persistance, Triple Câblage, OmniCapture, Engage View | couche tactique Cerritos |
| **V0.8.1 → V0.8.8** (8 PRD) | Migration Souveraine, Sas Décompression, Pipeline DEAL, Nexus Économique, Radar Frictions, Moteur Rentabilité, Pont Exécutif, Nécropole Drones | couche tardive Protostar |

## Verdict par bloc

- **superseded** (la majorité, ~38 PRD) — chaque Framework App a été
  réifiée en code React dans `coach-os/` et le PRD a cessé d'être la
  référence. Remplacés par le code source et par les concepts
  d'archives (ex. [[concept-sdd-v0-5-sovereign-constitution]]).
- **synthese-datee** (~6 PRD, ceux du V0.5/V0.6 qui ont une doctrine
  encore portée en V3) — leur **intention** reste valide (ex. V0.5.3
  Life Wheel Automatisée reste la cible du Compas), mais le détail
  d'implémentation est obsolète.
- **orphelin** : `antigravity-kit-fusion_PRD.md` (seul dans
  `_SPECS/prds/`, pas de miroir TOTAL_Spec) — voir
  [[concept-prd-orphelin-antigravity]].

## Convention de nommage

Le format `V0.X.Y` signifie **Version.Itération.Phase(alpha).Étape(num)**
selon l'auteur V0.2 (verbatim) :

> **Convention** : `V0.2.X.Y.Z` = Version.Itération.Phase(alpha).Étape(num)

Ce format **n'est plus utilisé** dans la chaîne numérotée SDD-000 →
SDD-010, qui adopte une numérotation plate. Voir
[[concept-sdd-chain-numbered]] pour la table de correspondance.

## Source du décompte

`find .../Legacy_LifeOS_App_Specs_2026-05-22/_SPECS/prds/` —
45 fichiers (44 numérotés V0.x + antigravity-kit-fusion).
Le miroir `TOTAL_Spec/PRD/` n'a que les 44 numérotés.

## Concepts liés

- [[concept-sdd-chain-v0x-legacy]] — la chaîne SDD correspondante.
- [[concept-prd-orphelin-antigravity]] — l'unique PRD sans miroir.
- [[concept-prd-v1-master-ingress]] — le saut V0 → V1 (PRD-V1.0).
