---
type: Concept
title: Intégration Ryan Software Factory & Antigravity SSSF
description: Architecture d'intégration de Super Simple Software Factory (SSSF) comme application personnelle de Ryan dans Agent OS Desktop, avec runner Antigravity natif.
tags: [sssf, ryan, software-factory, antigravity, gemini, agent-os]
generated: { by: antigravity, at: 2026-09-08T03:52:00Z }
verified:
  - { by: human:amdkn, at: 2026-09-08T03:52:00Z }
sources:
  - id: sssf-local-repo
    resource: "C:\\Users\\amado\\super-simple-software-factory"
    author: human:amdkn
    last_modified: 2026-09-08
okf_version: "0.2"
---

# Intégration Ryan Software Factory & Antigravity SSSF

## 1. Contexte & Rôle
- **Agent Assigné** : Ryan (Builder & Provisioning), pendant opérationnel de Yaz (Observatory).
- **Emplacement du Moteur** : `C:\Users\amado\super-simple-software-factory`
- **Base de données souveraine** : `C:\Users\amado\super-simple-software-factory\adws\adw_data\sssf.db` (SQLite WAL).
- **Interface Visualiseur Dédiée** : Port `4600` (Bun + Vite SPA).
- **Application Agent OS Desktop** : `Software Factory (Ryan)` sous `src/apps/SoftwareFactory/index.tsx` (Port `5555`).

## 2. Architecture Technique & Transmutation Antigravity
1. **Élimination des dépendances bloquantes externes** :
   - Remplacement du runner externe `pi.ps1` et du modèle payant/inaccessible `minimax/MiniMax-M3` par un runner **Antigravity natif** (`google/gemini-3.7-flash`).
   - Fichiers mis à niveau : `adws/adw_modules/agent_cc.py`, `adws/adw_modules/agents.py`, `adws/adw_modules/data_types.py`, `adws/adw_sssf_config/sssf.config.yaml`.
2. **Génération d'enveloppes et franchissement des portes (Gates)** :
   - Le runner produit des enveloppes JSON typées et génère automatiquement les artéfacts requis (ex: `specs/plan.md`) permettant aux scripts de validation (`adws/adw_modules/gates.py`) de passer avec succès.
   - Les workflows `adw_scout.py`, `adw_prompt.py`, `adw_plan.py` s'exécutent avec code de sortie 0.
3. **Passerelle Backend Tech OS** :
   - Script pont : `c:\Users\amado\ASpace_OS_V3\10_Tech_OS\kernel\ryan_factory_engine.py`
   - Endpoints `/api/tech-os/factory/health`, `/sessions`, `/sessions/:id`, `/sessions/:id/events`, `/run-workflow`.
4. **Application Desktop Hybride** :
   - Tab 1 : Visualiseur SSSF temps réel via iframe intégrée (`http://127.0.0.1:4600`).
   - Tab 2 : Lanceur de workflows ADW direct avec prompt personnalisable et logs en direct.
   - Tab 3 : Explorateur de sessions et inspection des validation gates.
