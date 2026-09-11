---
type: Decision
title: "Delegation Jules — Moteur Local SLM Morty & Ingestion Marin CPU"
description: "Brief physique et mandatement de Jules pour l'implémentation du moteur local Morty (MiniMind + TimesFM) et de l'extracteur de dataset Marin."
tags: [jules, delegation, morty, slm, minimind, marin, timesfm, cpu, okf]
generated: { by: "agent:gemini-antigravity", at: "2026-09-11T00:45:00Z" }
verified:
  - { by: "human:amdkn", at: "2026-09-11T00:45:00Z" }
sources:
  - id: sdd-004
    resource: "delegation-a-jules/SDD-004-MINIMIND-MARIN-TIMESFM-MORTY.md"
    author: human:amdkn
    last_modified: 2026-09-09
  - id: prd-morty
    resource: "delegation-a-jules/PRD-MORTY-LOCAL-ENGINE.md"
    author: antigravity
    last_modified: 2026-09-11
okf_version: "0.2"
---

# Délégation Jules — Moteur Local SLM Morty & Ingestion Marin CPU

## 1. Contexte & Découplage Cloud
- **Objectif** : Zéro dépendance API cloud pour les arbitrages et la prévision de chronobiologie (H1-H90).
- **Architecture** : Triade MiniMind 64M (symbolique) + Marin (alignement déterministe) + TimesFM (séries temporelles) tournant à froid sur CPU NVMe (< 150 Mo RAM).
- **Repository Cible** : `Amdkn/Aspace_OS_V3`.

## 2. Actions Réalisées par Antigravity (Chef d'Orchestre)
1. Rédaction et versionnage du brief formel `delegation-a-jules/PRD-MORTY-LOCAL-ENGINE.md` appuyé sur `SDD-004-MINIMIND-MARIN-TIMESFM-MORTY.md`.
2. Push sur GitHub `main` (commit `3f0b9c87`).
3. Validation de l'absence de tâches pendantes dans `uc.db` (105 done, 0 pending, 0 claimed).
4. Câblage amont de `BethFilter` sur `gate.py` et `controleur.py` pour sécuriser l'admission avant dispatch.

## 3. Spécifications Déléguées à Jules
- **Module d'Extraction Marin** : `10_Tech_OS/kernel/slm/marin_dataset_extractor.py` pour compiler les fiches OKF (`40_Memory_Wiki_OKF/concepts/`) et les triplets RDF (`70_Onthologies/triplets/`) en paires d'instruction tuning sans dépendance lourde.
- **Moteur d'Inférence Local** : `10_Tech_OS/kernel/slm/morty_engine.py` exposant `predict_horizon()` et `evaluate_decision()` avec fallback CPU.
- **Suite de Tests Déterministe** : `10_Tech_OS/kernel/slm/test_morty_engine.py` (0 erreur `python -m py_compile` et 100% tests passés).
