---
id: ADR-LOOP-002
title: Queues over Loops — backlog pioché, HITL poussé vers la droite, sandbox AFK obligatoire
date: 2026-07-02
author: A0 jumeau numérique (Fable 5, CC)
status: PROPOSED
ratified: null (A0 ratify)
layer: L0 — Tech OS / Harness & Loops
preserves:
  - Donna DLQ (L0 canon — la queue des échecs est déjà notre pattern)
  - mindsets/B1_Manifesto.md §Sobriety + Posture C (zéro checkpoint retiré sans HITL A0)
  - ADR-META-001 D5 (pas d'auto-congratulation : review du système producteur)
sister:
  - 03_Resources_Geordi/09_Life_OS/LD07_Creativity_Reno/2026-07-02_pocock-agentic-engineering-workflow_david-ondrej__GUIDE.md
  - ~/.claude/plans/plan-meta-memoire-okf-wiki-graphify-dox.md P6-E3 (sandbox gated)
  - ADR-LOOP-001 (canon loop) · ADR-LOOP-003 (orient + signals)
tags: [#ADR #queue #backlog #hitl #sandbox #afk #review-the-system]
---

# ADR-LOOP-002 — Queues over Loops

## Décision

1. **Le modèle mental canon = la queue, pas la boucle infinie.** Le travail agentique A'Space est un backlog d'items typés (issue, signal, ticket) que des agents AFK **piochent sur trigger** (label, événement, cron) — jamais une boucle qui tourne pour tourner. Un item sort de la queue quand son livrable est mergé/validé, ou part en Donna DLQ après échecs répétés.
2. **HITL rightward, jamais HITL-zéro** : les checkpoints humains se poussent progressivement vers la droite (bug → exploration auto → fix auto → review auto → il reste le clic A0), MAIS chaque retrait de checkpoint = décision A0 explicite (Posture C). Question de contrôle permanente : *« qui review l'IA qui décide qu'on peut ne pas reviewer ? »* → **on review aussi le SYSTÈME producteur** : échantillonnage périodique des items auto-validés.
3. **Sandbox obligatoire pour tout agent AFK** : aucun agent hors-session ne tourne hors isolation (worktree/container/VM). Un agent AFK non-sandboxé peut détruire le home ou exfiltrer les env vars — risque kernel, veto Rick.
4. **Review enrichie, pas review subie** : le producteur AFK attache la preuve à son livrable (sortie chiffrée du done-check, screenshot, vidéo de walkthrough) — l'humain review en 1 lecture, pas en 1 session de debug.

## Rationale

Le développement a toujours été une queue (backlog → nœuds qui piochent → merge). Le « loop infini unique » ne matche ni les équipes ni notre doctrine : Donna DLQ, stop-conditions §10.4, pattern label→dispatch. Ce que le marché appelle « loops » est, dans 80 % des cas, des **agents AFK sur queue** — nommer correctement évite de construire la mauvaise chose.

## Conséquences

- Les crons P5 (Méta-Mémoire) et les Scheduled futurs (automatisation CC/HA/MC avant montée Shadow) se spécifient comme **consommateurs de queue** avec type d'item + condition de sortie + destination DLQ.
- Audit minimaliste candidat (gated Rick) : le reset Pocock — contexte nu, puis re-superposer uniquement les procédures choisies (notre surface 145 commandes × 130 skills = bloat probable).

## Rejeté

- Boucle infinie « ralph-style » comme défaut (reste un outil ponctuel, pas une architecture) · retrait de checkpoint implicite · agent AFK sur le FS réel non isolé.
