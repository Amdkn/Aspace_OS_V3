---
type: Concept
title: Orchestration des 13 Scheduled Tasks Antigravity — Tech OS, Gouvernance & Cores
description: Architecture, fréquences cron et protocoles d'exécution des 13 tâches planifiées autonomes réparties sur les agents de V3 (Rick, Yas, Ryan, Graham, Donna, Nardole, Bill, Clara, Amy, Rory, River).
tags: [scheduler, cron, tasks, tech-os, antigravity, automation, governance]
generated: { by: gemini-antigravity, at: 2026-09-07T13:36:30Z }
verified:
  - { by: human:amdkn, at: 2026-09-07T13:36:30Z }
sources:
  - id: scheduled-tasks-manifest
    resource: "10_Tech_OS/scheduler/scheduled_tasks_manifest.json"
    author: human:amdkn
    last_modified: 2026-09-07
okf_version: "0.2"
---

# Orchestration des 13 Scheduled Tasks Antigravity (V3)

## 1. Vue d'Ensemble

L'autonomie opérationnelle d'**A'Space OS V3** repose sur des routines de surveillance, d'auto-nettoyage et de consolidation continues.
Les 13 tâches planifiées couvrent l'intégralité des 4 piliers transversaux et des 3 OS applicatifs. Elles sont enregistrées comme processus récurrents autonomes (`schedule`) dans Antigravity et consignées dans [`10_Tech_OS/scheduler/scheduled_tasks_manifest.json`](file:///c:/Users/amado/ASpace_OS_V3/10_Tech_OS/scheduler/scheduled_tasks_manifest.json).

---

## 2. Répartition par Couche & Agent

| ID | Tâche | Agent | Fréquence (Cron) | Domaine | Objectif d'Invariance |
|---|---|---|---|---|---|
| **T-01** | DLQ & Stale Leases Reaper | `companion_donna_dlq` | `*/15 7-23 * * *` | L0 Baux | Aucun verrou orphelin dans `uc.db` > 15 min. |
| **T-02** | Replication & Law L0 Check | `s1_rick` | `0 2 * * 0` | L0 Dark Factory | Preuve hebdomadaire d'auto-réplication sans humain. |
| **T-03** | Heartbeat Ecosystem Scan | `companion_yas_observatory` | `*/30 8-23 * * *` | L0 Kernel | Port 5555 HTTP 200, RAM Chokidar, verrou audio TTS. |
| **T-04** | CI/CD Build & TypeScript | `companion_ryan_builder` | `0 4 * * *` | L0 Kernel | Compilation à zéro faute (`tsc --noEmit`), logs rotatifs. |
| **T-05** | Semantica Nightly Consolidation | `companion_graham_memory` | `0 3 * * *` | 70_Onthologies | Consolidation RDF quotidienne vers Semantica (1 681+ nœuds). |
| **T-06** | Weekly Distillation Gatekeeper | `companion_graham_memory` | `0 5 * * 0` | 50_Distillation | Règle d'or 1 : sas de distillation hebdomadaire certifié. |
| **T-07** | Wiki Lint & OKF Compliance | `companion_graham_memory` | `0 9 * * 0` | 40_Memory | Zéro dette d'obscurité, frontmatters OKF 0.2 valides. |
| **T-08** | Kanban Balancing & Watchdog | `companion_nardole_dispatch` | `*/20 8-20 * * 1-5` | L2 Business | Zéro ticket orphelin > 5 min, équilibrage des baux. |
| **T-09** | Weak Signals & SOB Scan | `companion_bill_discovery` | `0 7 * * 1-5` | L2 Business | Veille matinale arXiv, dépôts GitHub et signaux SOB. |
| **T-10** | Offer & SOPs Freshness Audit | `companion_clara_product_forge` | `0 10 * * 5` | L2 Business | Contrôle de délivrabilité des blueprints $100M et franchise 72h. |
| **T-11** | Energy Alignment & UI Sync | `companion_amy_interface` | `0 8,14,20 * * *` | L1 Life | Synchronisation jauge vitale Beth $\leftrightarrow$ console Port 5555. |
| **T-12** | Database Integrity Audit | `companion_rory_backend` | `0 6 * * *` | L1 Life | Audit de santé SQLite (`uc.db`) et politiques RLS Supabase. |
| **T-13** | n8n Bus & Webhooks Health | `companion_river_workflows` | `*/30 * * * *` | L1 Life | Disponibilité 24/7 des webhooks entrants et flux n8n. |

---

## 3. Comportement en Cas d'Échec

Chaque Scheduled Task applique le protocole d'escalade :
1. **Échec ponctuel :** Enregistrement de l'anomalie dans `10_Tech_OS/reports/`.
2. **Échec persistant (3 occurrences) :** Routage vers `companion_donna_dlq` qui qualifie la cause racine.
3. **Anomalie critique structurelle :** Escalade immédiate vers `s1_rick` et notification vocale claire via le démon TTS Denise.
