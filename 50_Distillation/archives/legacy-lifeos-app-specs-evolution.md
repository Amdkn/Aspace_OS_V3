---
type: Project
title: Legacy LifeOS App Specs — l'évolution V0.2 → V0.6 (jusqu'au 2026-05-22)
description: Le dossier `Legacy_LifeOS_App_Specs_2026-05-22/` archive les spécifications des apps Life OS en versions V0.2 à V0.6 (Micro → EngineRoom → EnterpriseComputer → SovereignConstitution → TemporalEngine), une chaîne de SDD, ADRs, DDD, PRDs et CONTRACTS close au 2026-05-22.
tags: [legacy, lifeos, sdd, adr, ddd, prd, v0.2, v0.3, v0.4, v0.5, v0.6, micro, engine-room, enterprise-computer, sovereign-constitution, temporal-engine, 2026-05-22]
generated: { by: minimax-m3, at: 2026-08-17T23:10:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-17T23:10:00Z }
sources:
  - id: legacy-specs-root
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Legacy_LifeOS_App_Specs_2026-05-22/_SPECS/"
    title: Dossier _SPECS legacy (198 fichiers .md)
    last_modified: 2026-05-22
  - id: legacy-totalspec
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Legacy_LifeOS_App_Specs_2026-05-22/TOTAL_Spec/"
    title: Dossier TOTAL_Spec (177 fichiers .md)
    last_modified: 2026-05-22
  - id: sdd-v05
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Legacy_LifeOS_App_Specs_2026-05-22/_SPECS/SDD-V0.5_SovereignConstitution.md"
    title: SDD V0.5 Sovereign Constitution (lu directement)
    last_modified: 2026-05-22
  - id: substrat
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat/04_Archives_Data.jsonl"
    title: Substrat d'extraction — 750 fichiers legacy, 338 440 mots mesurés
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Legacy LifeOS App Specs — l'évolution V0.2 → V0.6

## Périmètre mesuré

Le dossier `Legacy_LifeOS_App_Specs_2026-05-22/` (date d'archivage :
2026-05-22) contient :

- **750 fichiers `.md`** mesurés par le substrat d'extraction
- **338 440 mots** au total
- Structure interne à **deux répliques** :
  - `_SPECS/` (198 fichiers) — la lignée SDD verticale
  - `TOTAL_Spec/` (177 fichiers) — ADR/DDD/PRD/CONTRACTS
  - `20_Life_OS/24_PARA_Enterprise/` (375 fichiers) — un sous-arbre PARA
    imbriqué (signe d'un archivage qui a copié un instantané complet de
    la zone 20_Life_OS, pas seulement les specs)

C'est **2,7 % du seau 04_Archives_Data** en nombre de fichiers, mais
**3,4 % en volume de mots**.

## La chaîne SDD V0.2 → V0.6 (extraits du substrat)

Lue directement dans `_SPECS/`, la chaîne est :

| Version | Nom de code | Phase | Couche |
|---|---|---|---|
| V0.2 | Micro | fondation | socle minimal |
| V0.3 | EngineRoom | phase 1 | moteur de base |
| V0.4 | EnterpriseComputer | phase 1 | ordinateur d'entreprise |
| V0.4-Phase2 | TacticalOrchestration | phase 2 | orchestration tactique |
| V0.4-Phase3 | SummersFractal | phase 3 | fractal Summer's Verse |
| **V0.5** | **SovereignConstitution** | pivot | **Livre des Lois** |
| V0.6 | TemporalEngine | phase 1 | moteur temporel |
| V0.6-Phase2 | TimeForges | phase 2 | forges du temps |
| V0.6-Phase3 | CentralCommand | phase 3 | commande centrale |

L'évolution **V0.4 → V0.5 → V0.6** marque le pivot du **« mockup visuel »**
vers le **« Livre des Lois »** : Ikigai et Life Wheel cessent d'être des
illustrations pour devenir des principes immuables.

## Verbatim du pivot V0.5 (SovereignConstitution)

> **« L'Ikigai et la Life Wheel doivent cesser d'être des mockups visuels
> pour devenir le Livre des Lois de The Watcher. Si la machine automatise
> sans principe, elle prend le contrôle. »**
>
> — `_SPECS/SDD-V0.5_SovereignConstitution.md` §1

Trois décisions architecturales majeures du V0.5 :

1. **Le Veto des Conteneurs (Anti-Pattern)** — les 8 Domaines de la Life
   Wheel et les Axes de l'Ikigai sont **figés**. Le bouton `+ New` ne
   crée jamais une nouvelle catégorie, seulement un nœud de contenu à
   l'intérieur.
2. **Migration vers IndexedDB** — remplacement strict du middleware
   `persist` (`localStorage`) dans `fw-ikigai.store.ts` et
   `fw-wheel.store.ts` par le système `ld-router.ts`.
3. **Le Pont Top-Down / Bottom-Up** — un `Project` gagne des pointeurs
   optionnels `ikigaiVisionId` et `wheelAmbitionId`.

## Vocabulaire d'agents dans les specs legacy

Important : les specs legacy utilisent un **vocabulaire d'agents
différent** de la version actuelle :

| Legacy (avant 2026-05-22) | Actuel (2026-08-17) |
|---|---|
| A'0 = GravityClaw | A0 = Amadeus (l'utilisateur) |
| A'1 = Rick | A1 = Beth |
| A'2 = Doctors | A2 = Picard / Spock / Geordi / Data |
| A3 = Gemini CLI / IronClaw | A3 = Data (Archives) |

Ce **décalage** est un signal que le vocabulaire a été refondu entre
mai et août 2026 — un projet RDF doit choisir quel vocabulaire porte
l'URI canonique.

## Composition du TOTAL_Spec (par sous-dossier)

| Sous-dossier | Fichiers | Nature |
|---|---|---|
| `ADR/` | 62 | Architecture Decision Records |
| `DDD/` | 56 | Domain-Driven Design docs |
| `PRD/` | 44 | Product Requirements Documents |
| `SDD/` | 14 | Spec-Driven Development (noyau V0.x) |
| `CONTRACTS/` | 1 | Contrats inter-modules |
| TOTAL | 177 | |

## Composition du _SPECS (par sous-dossier)

| Sous-dossier | Fichiers | Nature |
|---|---|---|
| `ADR/` | 64 | ADRs (doublons partiels avec TOTAL_Spec) |
| `DDD/` | 61 | DDDs (doublons partiels) |
| `prds/` | 45 | PRDs (lowercase, dossier distinct de TOTAL_Spec/PRD) |
| `wishlists/` | 7 | Idées non triées |
| `02_V1_PRD/` | 3 | PRD V1 historique |
| `SDD-V0.2` à `SDD-V0.6-Phase3` | 9 | La chaîne SDD elle-même |
| `CONTRACTS.md` | 1 | Contrats inter-modules |
| TOTAL mesuré | ~192 | |
| `_INBOX/` | ~5 (non compté) | staging |

## Doublons et fragmentation

`_SPECS/` et `TOTAL_Spec/` **ne sont pas des synonymes** :
- `_SPECS/` porte la **lignée verticale** (SDD V0.2 → V0.6 + companions)
- `TOTAL_Spec/` porte le **portrait horizontal** (ADR + DDD + PRD par
  domaine, snapshot à un instant t)

Les **doublons ADR/DDD** entre les deux sont des **artefacts** : le
même document a été classé deux fois selon deux taxonomies.

## Le sceau « Approuvé »

Le SDD-V0.5.1 porte le statut **« Approuvé »** dans son frontmatter
littéral. C'est un signal de **clôture de version** : la V0.5 a été
gelée comme référence avant la migration vers la V0.6.

## Concepts liés

- [[sdd-sovereign-constitution-v05]] — l'analyse détaillée du pivot V0.5.
- [[data-role-a3-archives-officer]] — l'officier qui a scellé l'archive le 2026-05-22.
- [[archive-v3-structure-snapshot-2026-08-02]] — un autre grand versement dans ce même seau.
