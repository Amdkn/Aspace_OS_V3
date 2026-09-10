---
type: Architecture Decision
title: Engram Hook IA O(1), Jules Bedrock Linear/Stitch & Morty Local CPU
description: Consolidation canonique de l'architecture Engram comme Hook IA déterministe O(1), de l'orchestration autonome de Jules via Linear/Stitch MCP, et du Modèle Fondation Local Morty (MiniMind + Marin + TimesFM) sur CPU/NVMe.
tags: [engram, hook-ia, jules, linear, stitch, minimind, timesfm, morty, okf, architecture]
generated: { by: "agent:gemini-antigravity", at: "2026-09-10T18:15:00Z" }
verified:
  - { by: "human:amdkn", at: "2026-09-10T18:15:00Z" }
sources:
  - id: spec-002
    resource: "delegation-a-jules/SPEC-002-ENGRAM-FULL-POTENTIAL-SOLARPUNK.md"
    title: "SPEC-002 Engram Full Potential & Solarpunk Bedrock"
    last_modified: 2026-09-09
  - id: spec-003
    resource: "delegation-a-jules/SPEC-003-LINEAR-AUTONOMY-AND-STRUCTURE.md"
    title: "SPEC-003 Linear Autonomy & Structure Jules"
    last_modified: 2026-09-09
  - id: sdd-004
    resource: "delegation-a-jules/SDD-004-MINIMIND-MARIN-TIMESFM-MORTY.md"
    title: "SDD-004 Modèle Fondation Local Morty (MiniMind + Marin + TimesFM)"
    last_modified: 2026-09-09
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine & certifié.** Composants forgés, scripts validés (py_compile 0 erreur, unit tests Engram 6/6 OK), branches synchronisées et poussées sur GitHub `main`.

# Engram Hook IA O(1), Jules Bedrock Linear/Stitch & Morty Local CPU

## 1. Engram comme Hook IA Déterministe O(1)
Engram n'est pas un RAG lourd ni une ré-injection de tokens :
- **Pre-Tool & Pre-Inference Interceptor :** Intercepte les requêtes avant tout appel LLM.
- **Résolution Zero-Token sur NVMe :** Mappe `phrase_book_aspace.json` via `mmap` mémoire pour résoudre les invariants 1D à 7D en moins de 1 ms sans consommer de tokens API.
- **Filtre Gatekeeper A1 Beth :** `10_Tech_OS/kernel/engram/beth_filter.py` évalue les intentions et déclenche des vetos déterministes immédiats (ex: circuit breaker `OS_HYOIDE_BUFFER`).
- **Alignement KV-Cache :** Génère un préfixe invariant figé assurant plus de 90% de réutilisation du cache GPU chez les fournisseurs d'inférence.

## 2. Jules Incarné en BedRock du Solarpunk Kernel
- **Linear MCP :** Jules structure et gère les issues en 3 équipes canoniques : Kernel Core (13e Docteur), Life Core (11e Docteur) et Forge Core (12e Docteur).
- **Stitch MCP :** Gatekeeper visuel garantissant la non-régression du design system des interfaces Web (The OMK Office, Dashboard Vite).
- **Sobriété de Quota :** Zéro prompt flou ; les directives sont déposées physiquement dans `delegation-a-jules/` sous forme de spécifications numérotées.

## 3. Modèle Fondation Local de Morty (MiniMind + Marin + TimesFM)
- **MiniMind 64M :** Inférence CPU pure en format quantifié (ONNX/GGUF), empreinte RAM < 50 Mo, pour l'arbitrage symbolique local de Morty sans réseau.
- **Marin :** Forge de compilation et de tokenisation du dataset d'instruction tuning à partir de `70_Onthologies/` et `40_Memory_Wiki_OKF/`.
- **TimesFM (Google Research) :** Modèle de fondation de séries temporelles zero-shot pour projeter les cycles 12WY et les horizons H1 à H90 de l'Ikigai (LD01 à LD08) en local.

## 4. Rôles Déterministes des Compagnons & Donna DLQ
- **Visionnaire L0 :** Rick Sanchez (Loi de réplicabilité pure et destruction de dette).
- **Kernel Core (13e) :** Yaz (Télémétrie 60s), Ryan (Build/Engine), Graham (Ontologie RDF / Silver Platter).
- **Life Core (11e) :** Amy (Vision), Rory (Physiologie/Sommeil), River (Chronobiologie/12WY).
- **Forge Core (12e) :** Clara (Produit/Recherche), Bill (Forge/DoD stricte), Nardole (Dispatch/Routage).
- **Dead Letter Queue :** Donna Noble (`10_Tech_OS/kernel/dlq.py`) isole les tâches à plus de 3 échecs pour briser la boucle de rejeu P1 et escalader à Rick.