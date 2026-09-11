---
type: Concept
title: Co-Évolution Modèle-Harnais, Harness-of-Harness & Exécution Multi-Jours
description: Architecture de co-évolution entre politiques neuronales et harnais logiciels runtime, intégrant Harness-of-Harness (HoH), HELIX, Task-CoEvolve, Terminal-Universe et veRL pour l'autonomie multi-jours de V3.
tags: [co-evolution, harness, hoh, helix, terminal-universe, verl, rsi, tech-os]
generated: { by: gemini-antigravity, at: 2026-09-07T10:08:00Z }
verified:
  - { by: human:amdkn, at: 2026-09-07T10:08:00Z }
sources:
  - id: arxiv-2609-01481
    resource: "Harness-of-Harness: Multi-Day Autonomous Software Development (arXiv:2609.01481)"
    author: Haoyang Yan et al.
  - id: arxiv-2608-13951
    resource: "HELIX: Model-Harness Co-evolution for Recursive Self-Improvement (arXiv:2608.13951)"
    author: arXiv:2608.13951
  - id: arxiv-2609-04148
    resource: "Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments (arXiv:2609.04148)"
    author: arXiv:2609.04148
  - id: arxiv-2409-19256
    resource: "HybridFlow / veRL: Flexible and Efficient RLHF Framework"
    author: Sheng Shen et al.
okf_version: "0.2"
---

# Co-Évolution Modèle-Harnais & Exécution Multi-Jours (V3)

## 1. Le Changement de Paradigme : Du Modèle Seul au Système Harnaché

Jusqu'alors, l'amélioration des agents reposait quasi-exclusivement sur la puissance intrinsèque du modèle (taille des paramètres, contexte). Les découvertes de septembre 2026 démontrent que **le harnais d'exécution (outils, baux, boucles de rétroaction, gestion de l'état)** est aussi critique que le modèle lui-même :

$$ \text{Performance Système} = \mathcal{F}(\text{Politique LLM} \otimes \text{Harnais Runtime}) $$

Dans **A'Space OS V3**, le harnais est incarné par :
- Le noyau d'orchestration SQLite (`10_Tech_OS/kernel/uc.db`).
- Le gestionnaire de baux temporels et de détachement (Loi du bail, Loi de détachement).
- Les subagents spécialisés (`doctor_13_kernel`, `companion_ryan_builder`, etc.).

---

## 2. Les Piliers Techniques de la Co-Évolution

### A. Harness-of-Harness (HoH - arXiv:2609.01481)
Permet des cycles de développement logiciel autonome s'étalant sur plusieurs jours consécutifs sans intervention humaine grâce à :
1. **Planification continue par étapes réversibles.**
2. **Validation empirique ancrée sur preuves (*evidence-grounded testing*).**
3. **Ré-ancrage périodique de l'état :** purge des bruits de logs intermédiaires pour préserver la fenêtre de contexte.

### B. HELIX & Task-CoEvolve (arXiv:2608.13951 & arXiv:2608.20169)
- **Co-évolution conjointe :** L'agent réécrit et optimise le code de son propre harnais (scripts de build, wrappers d'outils, parsers) à mesure qu'il résout des tâches.
- **Sélection adaptative des tâches de validation :** Évite de surcharger le runtime en sélectionnant dynamiquement les tests critiques d'invariance.

### C. Terminal-Universe (arXiv:2609.04148)
Convertit les trajectoires d'agents terminaux en bacs à sable ré-exécutables et vérifiables. Permet à Ryan Builder et au 13e Docteur de rejouer des scénarios de panne ou de déploiement à froid en environnement isolé.

### D. veRL / HybridFlow (arXiv:2409.19256)
Orchestre les dataflows asynchrones entre agents acteurs, critiques et modèles de récompense. Utilisé dans V3 pour calibrer le scoring prédictif de `uc.db` et alimenter le benchmark `ceo-bench`.

---

## 3. Implémentation Opérationnelle dans Tech OS

1. **Ryan (Builder) :** Intègre le patron HoH pour la maintenance continue et l'instanciation à froid des conteneurs sans blocage synchrone.
2. **Yas (Observatory) :** Surveille la santé du harnais (détection des boucles infinies de co-évolution).
3. **Donna DLQ :** Reçoit toute trajectoire en échec pour analyse de cause racine et enrichissement du jeu de validation.
