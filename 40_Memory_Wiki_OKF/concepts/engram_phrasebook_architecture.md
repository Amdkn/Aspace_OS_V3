---
type: Architecture Concept
title: Engram Phrasebook & Gatekeeper A1 Beth
description: Moteur résolveur Engram zero-RAM O(1) sur SSD NVMe et filtre de garde déterministe A1 Beth pour A'Space OS V3.
tags: [engram, phrasebook, gatekeeper, beth, okf]
generated: { by: "agent:bill-potts", at: "2026-09-09T10:00:00Z" }
verified:
  - { by: "human:amdkn", at: "2026-09-09T10:00:00Z" }
sources:
  - id: sdd-001
    resource: "delegation-a-jules/SDD-001-ASPACE-STRUCTURE-AND-12TH-DOCTOR.md"
    title: "SDD-001 Structure & 12th Doctor"
    last_modified: 2026-09-09
  - id: prd-a1
    resource: "delegation-a-jules/PRD-A1-ENGRAM-PHRASEBOOK.md"
    title: "PRD-A1 Engram Phrasebook"
    last_modified: 2026-09-09
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine & revu.** Code source compilé (py_compile 0 erreur) et 6 tests unitaires passés à 100%.

# Engram Phrasebook & Gatekeeper A1 Beth

## 1. Description & Objectif Cybernétique
L'architecture **Engram Phrasebook** a pour but d'éliminer l'overhead de tokens lors de l'injection répétitive des invariants, règles et lore d'A'Space OS V3. Les ontologies et invariants sont stockés dans une lookup table `10_Tech_OS/kernel/engram/phrase_book_aspace.json` mappée en mémoire (`mmap`) via `engram_loader.py`.

Le composant **BethFilter** (`10_Tech_OS/kernel/engram/beth_filter.py`) agit comme le Gatekeeper A1. Il intercepte chaque intention entrante avant sa transmission aux agents A2/A3 pour valider les règles et exercer un veto immédiat en cas de circuit breaker (ex. `OS_HYOIDE_BUFFER`).

## 2. Composants Forgés
- **Lookup Table :** `10_Tech_OS/kernel/engram/phrase_book_aspace.json` (mappings 1D-7D, LD01-LD08, Docteurs, DoD).
- **Moteur Résolveur :** `10_Tech_OS/kernel/engram/engram_loader.py` (résolution $O(1)$ par `mmap`).
- **Filtre Gatekeeper A1 :** `10_Tech_OS/kernel/engram/beth_filter.py` (évaluation déterministe & veto).
- **Suite de Tests :** `10_Tech_OS/kernel/engram/test_engram.py` (6 unit tests passing).

## 3. Câblage Inter-Composants (Dispatch Nardole)
- **Tech OS Kernel :** Interception des événements dans `10_Tech_OS/kernel/`.
- **Life OS A1 Gatekeepers :** Alignement déterministe avec Beth (`20_Life_OS/00_Gatekeepers_Beth_Morty/`).
