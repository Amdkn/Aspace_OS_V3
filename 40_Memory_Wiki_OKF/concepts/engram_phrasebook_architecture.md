---
type: concept
title: "Architecture Engram Phrase Book et Gatekeepers A1 (Zero-Token Overhead)"
description: "Découplage déterministe entre calcul actif et mémoire ontologique statique via tables NVMe mmap inspirées de Qwen Engram, Marin et MiniMind"
tags:
  - architecture
  - engram
  - zero-token
  - mmap
  - gatekeeper
  - life-os
  - tech-os
generated: "2026-09-09"
verified:
  by: "human:amdkn"
  date: "2026-09-09"
sources:
  - "http://www.youtube.com/watch?v=IH8XmxiwliQ (Codacus - Local Frontier Models Analysis)"
  - "c:\\Users\\amado\\ASpace_OS_V3\\10_Tech_OS\\kernel\\engram\\phrase_book_aspace.json"
  - "c:\\Users\\amado\\ASpace_OS_V3\\10_Tech_OS\\kernel\\engram\\engram_loader.py"
okf_version: "0.2"
---

# Architecture Engram Phrase Book & Gatekeepers A1 (Zero-Token Overhead)

> **Principe Cardinal :** Cesser d'injecter des milliers de tokens de règles, de Lore et de schémas ontologiques dans chaque fenêtre de contexte. Le cerveau actif calcule le raisonnement ; la mémoire ontologique immuable réside sur le SSD NVMe et est résolue en $O(1)$ par memory mapping (`mmap`).

---

## 1. Fondements Cybernétiques & Matériels

L'analyse empirique de Codacus sur les modèles frontières locaux (177B tournant sur RTX 3060 12 Go) démontre la rupture entre calcul tensoriel et lecture de table :
- **Modèle conventionnel :** Chaque mot ou concept récurrent consomme des couches d'attention et des mégaoctets de VRAM/RAM.
- **Modèle Engram Phrase Book :** Les n-grams récurrents (*"LD01"*, *"Definition of Done"*, *"13e Docteur"*) sont résolus directement dans une table d'indexation NVMe sans activation de couches d'inférence.

---

## 2. Implémentation A'Space OS V3

1. **Substrat Déterministe (`10_Tech_OS/kernel/engram/`) :**
   - `phrase_book_aspace.json` : Répertoire canonique des entités 1D à 7D (LD01-LD08, Triades des 11e, 12e et 13e Docteurs, Invariants SSSF).
   - `engram_loader.py` : Moteur de résolution instantané exploitant `mmap` en mode lecture seule (`ACCESS_READ`).
2. **Front de Capture A1 (Gatekeepers Beth & Morty) :**
   - **Beth (Gouvernance 5D/6D) :** Valide la conformité sémantique et la non-dilution de la trajectoire d'A0.
   - **Morty (Substrat 3D/4D) :** Pilote la résolution déterministe hors-cloud et le cadencement sans calcul lourd.

---

## 3. Impact Économique & Performance

- **Token overhead d'initialisation :** 0 token payé aux APIs cloud pour réexpliquer le système.
- **Empreinte RAM :** Proche de 0 Mo additionnels grâce au paging virtuel du kernel OS.
- **Résolution :** < 1 milliseconde par intention.
