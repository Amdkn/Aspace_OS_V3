---
type: Concept
title: Architecture Graph-Native et Context Graphs (Semantica AGI)
description: Métamodèle d'infrastructure combinant graphes sémantiques, contextes dynamiques d'exécution et traçabilité causale pour agents IA explicables.
tags: [architecture, ontologie, semantica, graph-native, context-graph, provenance]
generated: { by: gemini-antigravity, at: 2026-09-07T08:50:00Z }
verified:
  - { by: process:distill_gate, at: 2026-09-07T08:48:58Z }
sources:
  - id: semantica-repo
    resource: "https://github.com/semantica-agi/semantica"
    title: "Semantica AGI — Graph-Native Infrastructure"
    last_modified: 2026-09-07
okf_version: "0.2"
---

# Architecture Graph-Native et Context Graphs (Semantica)

## 1. Problème Résolu
Les architectures agentiques classiques s'appuient sur un contexte textuel éphémère ou sur un retrieval vectoriel probabiliste, conduisant à des hallucinations, des dérives de raisonnement et une incapacité à certifier ou auditer les causes d'une décision.

## 2. Invariants Techniques Semantica
1. **Dualité Graphe de Connaissance / Graphe de Contexte :**
   - **Knowledge Graph (KG) :** Ontologie métier stable, règles de gouvernance et taxonomies formelles (l'équivalent de `70_Onthologies/`).
   - **Context Graph (CG) :** Graphe dynamique des entités, sessions, baux et agents actifs en mémoire de travail à l'instant $t$.
2. **Auditabilité Causale & Provenance :**
   - Chaque action d'agent doit être reliée par un arc typé à l'assertion ontologique qui l'autorise et à la trace d'observation qui l'a déclenchée.
3. **Moteurs de Raisonnement Hybrides :**
   - Le LLM n'invente pas la structure : il opère une traversée et une projection sur le sous-graphe sémantique pertinent.

## 3. Application Transversale à A'Space OS V3
- **Vers 70_Onthologies/ :** Intégration du métamodèle de prédicats de causalité (`causesAction`, `justifiedBy`, `trackedInSession`).
- **Vers 10_Tech_OS/kernel/ :** Observabilité sur SQLite / graphe pour tracer les baux d'agents (`uc.db`) sous forme de nœuds de contexte.
