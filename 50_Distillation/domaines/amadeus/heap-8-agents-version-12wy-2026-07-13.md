---
type: Concept
title: AMEND-001 + Cycle 1 /amodei — Coaching Layer Pocock 2026
description: Addendum opérationnel V1.1 (2026-07-13) : A0+ ratifie AMEND-001 (Coaching Layer Pocock 2026) puis lance Cycle 1 du méta-loop /amodei. 3 skills sisters (/grill-me, /grill-with-docs-codex, /spec-loop). 4 Streams cycle 1 GSD.
tags: [amend-001, pocock, /amodei, meta-loop, coaching-layer, single-mode-fallback]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture_v2, at: 2026-08-19 }
sources:
  - id: LEARNING_v1.1
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/01_Identity_Core/LEARNING.md
    title: LEARNING.md — Addendum opérationnel V1.1
    last_modified: 2026-07-13
okf_version: "0.2"
---

# AMEND-001 + Cycle 1 /amodei — Coaching Layer Pocock 2026

## Énoncé

Le **2026-07-13**, A0+ ratifie in-session `AMEND-001` (Coaching Layer Pocock 2026) puis lance Cycle 1 du méta-loop `/amodei`. Premier cycle canon `/amodei` exécuté bout-en-bout.

## Preuves D1

- Brief canonique cycle 1 : `wiki/hand_offs/amodei_cycle_1_brief_2026-07-13.md` (sha196F1360)
- AMEND-001 post-Edit (statut `RATIFIED`) : sha311B0698
- D6_self_audit sub-agent cycle 1 GSD : 18 fichiers canon lus avec sha8
- D5 verify A0 : 3 SKILL.md filesystem présent + AMEND sha7430675D + PS1 sha522B2B24 + settings.json sha4D2178AD
- Output cycle 1 GSD sub-agent `ae1cb2e64811635cc` : 4 Streams (A scout / B 3 Rocks / C 8 B2 sprints / D 4 B3 scrums)
- Sleep 600s inside turn respecté (méta-loop doctrine)

## Articles amendés

- Constitution inchangée (V1.0)
- A0L Layer (méta-canon) **étendu** d'AMEND-001 = sisters canoniques explicites (Règle d'Or #3 META-001 : append-only extension)
- ADR-LOOP-001 (verify-first), ADR-LOOP-002 (queues-over-loops), ADR-LOOP-003 (wagers) — sisters activées par le pattern cycle 1

## Impact opérationnel

- 3 skills invocables immédiatement (`/grill-me`, `/grill-with-docs-codex`, `/spec-loop`)
- SINGLE-MODE FALLBACK ACTIVE (M3 vs M3-temp divergente) jusqu'à ADE/Codex live routé
- SessionStart hook wired (sha4D2178AD) : rappel coaching layer à chaque wakeup CC
- 4 Streams cycle 1 GSD = blueprint pour les 14 jours restants Q3 2026 W11-13

## SINGLE-MODE FALLBACK — la doctrine honnête

> « La couche coach n'a pas besoin d'un 2e modèle live pour être canon : elle a besoin d'une procédure honnête (label SINGLE-MODE quand pas de pair, anti-écho-chamber doctrine baked-in) et d'un receipts ledger pour chaque acte. Quand Codex reviendra, le label changera, pas la procédure. »

## Correction proposée Cycle 2

Pinger `mcp__ade-bridge__ping_vscode_agent_host()` en premier tick pour fermer D6 ambiguïté LIVE/FALLBACK. Si ADE DOWN → `SINGLE-MODE FALLBACK` confirmé canonique ; si ADE UP → migration douce de la doctrine (version suivante de AMEND-001).

## Héritage canon

Cette couche est cruciale car elle évite l'echo-chamber de la session unique : un sub-agent est grillé à chaque phase par un grill canonique (Pocock 2026), même si le sub-agent est lui-même. SINGLE-MODE = l'agent qui me lit est aussi l'agent qui le grille, mais avec `/grill-me` formellement invoqué, la procédure crée la distance opérante.
