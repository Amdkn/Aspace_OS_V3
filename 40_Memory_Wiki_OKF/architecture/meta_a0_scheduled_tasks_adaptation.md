---
type: Concept
title: Méta-Tâche T-00 A0 Amadeus — Optimisation & Adaptation Contextuelle Hebdomadaire
description: Spécification de la méta-tâche souveraine T-00 (A0 Amadeus) garantissant l'adaptation contextuelle dynamique (Windows/WSL/VPS), l'alignement ontologique Semantica et la préservation de l'architecture légère sans Docker pour n8n (.py -> flux visuels).
tags: [meta-task, amadeus, scheduler, context-adaptation, wsl, vps, n8n-lightweight, onthology]
generated: { by: gemini-antigravity, at: 2026-09-07T14:19:00Z }
verified:
  - { by: human:amdkn, at: 2026-09-07T14:19:00Z }
sources:
  - id: meta-a0-worker
    resource: "10_Tech_OS/scheduler/meta_a0_adaptation_worker.py"
    author: human:amdkn
    last_modified: 2026-09-07
okf_version: "0.2"
---

# Méta-Tâche T-00 A0 Amadeus : Optimisation & Adaptation Contextuelle

## 1. Raison d'Être

Dans un système cybernétique multi-niveaux tel qu'**A'Space OS V3**, des tâches planifiées statiques figées dans le code courent le risque de désynchronisation face à deux forces majeures :
1. **Les mutations d'infrastructure hôte :** Bascule de travail entre l'environnement **Windows Natif** (développement local, desktop apps), **WSL (aspace-l0)** et **VPS distant (aspace-vps)** via SSH/Tailscale.
2. **L'évolution continue du graphe de connaissances :** Nouveaux concepts ajoutés dans `70_Onthologies/`, sessions distillées et enrichissement du modèle sémantique (1 681 nœuds).

La tâche méta **`T-00`** opère au niveau **A0 (Amadeus)** chaque dimanche à 01h00 (avant les consolidations de Graham et les purges de Donna) pour assurer une syntonie parfaite.

---

## 2. Les Trois Piliers d'Adaptation de T-00

### Pilier 1 : Détection Hôte & Translation de Chemins (Windows / WSL / VPS)
- Détecte dynamiquement l'environnement d'exécution hôte (`platform.system()`, variables WSL, socket SSH).
- Adapte dynamiquement les baux SQLite (`uc.db`) et les chemins de fichiers (ex: `C:\Users\amado\...` $\leftrightarrow$ `/mnt/c/Users/amado/...` $\leftrightarrow$ `/home/amadeus/...`).
- Assure qu'aucun worker ne s'arrête en erreur pour une discordance de slash ou d'interpréteur (`pwsh` vs `bash`).

### Pilier 2 : Alignement Ontologique Vivant (Semantica AGI)
- Vérifie que chaque Scheduled Task programmée dans `config/sidecars` correspond à une intention et une capacité répertoriées dans `semantica_knowledge_graph.json`.
- Si Amadou Kone crée une nouvelle franchise Business OS ou un nouveau rituel Life OS, T-00 propose ou ajuste automatiquement la routine associée.

### Pilier 3 : Préservation des Subtilités d'Agent OS — Le Cas N8N Léger sans Docker
- **Doctrine de Sobriété V3 :** Le n8n d'Amadou Kone n'est **PAS** une instance Docker lourde (qui consommerait plus de 800 Mo de RAM et imposerait des daemons de virtualisation superflus).
- **Fabrication Native Légère :** C'est un **orchestrateur visuel souverain** qui lit et convertit directement les scripts Python opérationnels (`.py`) et les baux `uc.db` en **workflows et graphes visuels temps réel** dans la console Agent OS (Application `RiverWorkflows` sur le Port 5555).
- T-00 protège rigoureusement ce pattern contre toute tentative d'injection d'une pile Docker lourde non autorisée.

---

## 3. Livrables & Points d'Entrée

- **Sidecar Natif Antigravity :** `C:\Users\amado\.gemini\config\sidecars\t-00-meta-a0-amadeus-adaptation\sidecar.json`.
- **Worker Python d'Exécution :** [`10_Tech_OS/scheduler/meta_a0_adaptation_worker.py`](file:///c:/Users/amado/ASpace_OS_V3/10_Tech_OS/scheduler/meta_a0_adaptation_worker.py).
- **Rapport d'Audit Généré :** `10_Tech_OS/reports/meta_a0_adaptation_report.json`.
