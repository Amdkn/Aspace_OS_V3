---
type: Decision
title: ADR — Heartbeat Daemon 15 Min, Plancher Jules >= 3 & Préservation Quotas Antigravity
description: Arbitrage canonique fixant le rythme d'auto-relance à 15 minutes, le maintien d'au moins 3 sessions Jules concurrentes, et la déportation stricte du calcul sur Jules Pro pour préserver le quota hebdomadaire Antigravity.
tags: [decision, jules, heartbeat, quotas, antigravity, aspace-os-v3, okf]
generated: { by: gemini-3.6-flash, at: 2026-09-10T21:38:00Z }
verified:
  - { by: human:amdkn, at: 2026-09-10T21:37:45Z }
sources:
  - id: direct-user-directive-20260910
    resource: "Directive souveraine Amadou Kone — Heartbeat 15m, plancher 3 sessions Jules, zéro gâchis quotas Antigravity"
    author: human:amdkn
    last_modified: 2026-09-10
okf_version: "0.2"
---

# ADR — Heartbeat Daemon 15 Min & Plancher Concurrence Jules >= 3

## 1. Contexte & Problématique
Amadou Kone a défini un plan Google AI Pro sur Antigravity nécessitant une gestion rigoureuse des quotas hebdomadaires. Parallèlement, l'opérateur dispose de 100 sessions quotidiennes sur Jules Pro (Google Labs) qui doivent être exploitées à pleine capacité sans laisser le système inactif.

## 2. Décision Canonique

1. **Fréquence du Heartbeat Autonome (15 Minutes) :**
   - Le heartbeat est configuré à `CronExpression: "*/15 * * * *"` (`IsDaemon: true`).
   - Fin des réveils rapprochés à 5 minutes pour éliminer toute consommation superflue de tokens de contexte.

2. **Plancher Strict de Concurrence Jules (>= 3 Sessions Simultanées) :**
   - Le cluster Jules doit maintenir en permanence au minimum **3 sessions actives concurrentes** (`IN_PROGRESS`).
   - Règle de déclenchement : Dès qu'une session se termine et que l'effectif tombe sous le seuil de 3, l'orchestrateur Antigravity lance immédiatement la session suivante à partir de `delegation-a-jules/` ou des besoins émergents du système.

3. **Préservation Stricte des Quotas Antigravity (Mode Full Délégation) :**
   - Antigravity agit exclusivement comme **Chef d'Orchestre minimaliste** : il rédige les PRDs, dispatche les sessions, vérifie les tests unitaires et fusionne les PRs.
   - 100% de la volumétrie de code, des refactors et de l'implémentation lourde est déportée sur Jules Pro.

## 3. Conséquences & Vérification
- Préservation de la jauge hebdomadaire Antigravity.
- Débit soutenu de production asynchrone sur GitHub.
- Traçabilité append-only systématique dans les `AGENTS.md` locaux et `uc.db`.
