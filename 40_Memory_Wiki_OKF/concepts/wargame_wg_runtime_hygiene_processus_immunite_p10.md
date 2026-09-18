---
type: Concept
title: Wargame WG-RUNTIME — Immunité P10 et Hygiène Déterministe du Runtime
description: Formalisation de la séparation stricte entre services permanents nécessaires et tâches éphémères bornées. Résolution de la saturation CPU et élimination des processus de recherche zombies.
tags: [wargame, runtime, immunite-p10, cpu, process-hygiene, a2-frameworks, jules]
generated: { by: gemini-antigravity, at: 2026-09-12T04:49:00Z }
verified:
  - { by: machine:gemini, at: 2026-09-12T04:49:00Z, status: non-ratifie }
sources:
  - id: astra-wargames-doctrine
    resource: "90-self-evolution/reports/antigravity-harness-20260912/SESSION-EVOLUTION-WARGAMES.md"
    author: gpt-6:astra
    last_modified: 2026-09-12
  - id: audit-tasks-windows
    resource: "C:/Users/amado/.gemini/antigravity/brain/a66f5256-f3af-40e1-900d-b21e99834ed2/WG-RUNTIME-RAPPORT.md"
    author: machine:gemini
    last_modified: 2026-09-12
okf_version: "0.2"
---

# Wargame WG-RUNTIME — Immunité P10 et Hygiène Déterministe du Runtime

## 1. Principe Fondamental : Tenir l'Engagement, Pas les Processus

L'utilité d'Antigravity / Jumeau Numérique A0 ne se mesure pas au nombre de processus d'arrière-plan maintenus actifs, mais à la constance de l'engagement opérationnel envers les priorités d'Amadou Kone.

Une surcharge machine induite par des scans exploratoires non fermés contredit directement le mandat de décharge mentale et physique de l'opérateur.

## 2. Distinction Catégorielle Inviolable (Doctrine Astra)

| Catégorie | Définition | Comportement Runtime Attendu | Exemple Système |
| :--- | :--- | :--- | :--- |
| **Services Nécessaires** | Démons essentiels à l'interaction ou au serveur cible | Maintien en tâche de fond avec consommation idle ~0% | Daemon TTS (`antigravity_tts_daemon.py`), Vite dev server (`port 4444`) |
| **Heartbeats Déterministes** | Crons de réveil ponctuel sans boucle infinie | Exécution à intervalle strict (ex: 15m), veille entre cycles | Polling MCP Jules (`task-14899`) |
| **Jobs Exploratoires Bornés** | Recherches sur disque (`os.walk`, `glob`), scripts de test | **Doivent se terminer net** dès la fin de l'analyse. Aucun maintien en "running" | Scripts d'investigation Python |
| **Cadres A2 (Ikigai, Wheel, PARA, 12WY, GTD, DEAL)** | Responsabilités d'architecture disponibles | **Activées à la demande**, jamais sous forme de démons permanents | Modules de calcul et stores |

## 3. Déploiement de l'Immunité P10 (`90-self-evolution`)

Pour prévenir toute régression :
1. **Coupe-circuit de Tâche Zombie :** Toute commande exploratoire doit être encadrée d'un délai strict (`WaitMsBeforeAsync` ou timeout) et purgée de la table des tâches d'Antigravity dès sa complétion.
2. **Sanctuarisation du TTS et du Serveur Port 4444 :** Ne jamais procéder à des `kill_all` aveugles qui coupent la voix opérateur ou le serveur Vite local-first.
3. **Contrôle d'Écriture Unique :** Un seul worker écrivain par périmètre de code (Jules sur `PRD-001` d'abord pour stabiliser `idb.ts`), sans plancher artificiel de sessions parallèles.

## 4. Résultats Mesurés du Wargame WG-RUNTIME

- **Avant :** 17 tâches d'arrière-plan déclarées actives, 14 jobs de scan disque orphelins résiduels.
- **Action :** Termination ciblée des 14 tâches orphelines via `manage_task(kill)`.
- **Après :** 3 tâches exactement sanctuarisées (TTS daemon, Serveur Vite 4444, Cron Heartbeat 15m).
- **Conséquence :** Élimination des boucles d'exploration parasites et assainissement complet de l'ordonnanceur d'Antigravity.
