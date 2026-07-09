---
id: ADR-LOOP-001
title: Canon du Loop A'Space — verification-first, done-check objectif, jamais d'auto-vérification
date: 2026-07-02
author: A0 jumeau numérique (Fable 5, CC)
status: PROPOSED
ratified: null (A0 ratify)
layer: L0 — Tech OS / Harness & Loops
preserves:
  - ADR-META-001 D1-D8 (verify-before-assert = le done-check est un D1 mécanisé)
  - ADR-SOBER-002 Anti-paperclip (hard stop obligatoire, coût raisonné)
  - mindsets/Morty_Mindset.md (FOCUS→REASON→ACT→OBSERVE→RE-EVALUATE→VERIFY→TRACK)
sister:
  - 03_Resources_Geordi/09_Life_OS/LD07_Creativity_Reno/2026-07-02_agent-loops-clearly-explained_nate-herk__GUIDE.md
  - 03_Resources_Geordi/09_Life_OS/LD07_Creativity_Reno/2026-07-02_wtf-is-loop-engineer_ai-jason__GUIDE.md
  - ~/.claude/plans/plan-meta-memoire-okf-wiki-graphify-dox.md §10 (1re application conforme)
  - ADR-LOOP-002 (queues + HITL) · ADR-LOOP-003 (orient + signals + wagers)
tags: [#ADR #loop #verification #done-check #maker-checker #posture-c]
---

# ADR-LOOP-001 — Canon du Loop A'Space

## Décision

Tout loop A'Space (=/goal, /loop, cron-réveil, workflow) est défini par le triplet **trigger + action + stop-condition**, exécuté en cycle **Reason → Act → Observe**, et n'est valide QUE si les 4 lois suivantes tiennent :

1. **Done-check objectif** : la stop-condition est mesurable (« itère jusqu'à X = Y »), jamais « until satisfied ». Si le critère est intrinsèquement subjectif → le rendre pseudo-objectif via rubrique + scorer dédié (loi 3).
2. **Hard stop** : cap d'itérations OU budget temps explicite, toujours. Un loop sans cap = paperclip.
3. **Jamais d'auto-vérification** : l'agent qui fait ne juge pas. La vérification passe par (a) une commande/test au résultat chiffré, ou (b) un **verifier read-only séparé** (pattern maker-checker), ou les deux.
4. **Log par itération** : 1 ligne trace (résultat + sortie du done-check) — un loop qui ne logge pas n'a pas eu lieu.

## Topologies canon (par ordre de sobriété)

**Solo loop** (défaut — 1 session + bon prompt) → **Maker-checker** (quand le scoring porte l'enjeu) → **Manager + helpers** (scope parallélisable seulement). On commence toujours au plus sobre.

## Loi de proportion (anti-hype)

**La majorité des tâches n'ont pas besoin de loop — elles ont besoin de vérification.** Le loop n'est justifié que si l'itération machine remplace une itération humaine réelle (courbe qualité/tentatives). Un loop ne vise pas 100 % de perfection : il rapproche massivement du but au premier tir. Sweet spot constaté : 35 min-2 h, ou « chunky loop » de nuit ; les runs de 12 h+ sont presque toujours du gaspillage.

## Conséquences

- Le §10 du plan Méta-Mémoire = 1re implémentation conforme (verify-commands chiffrées, cap 2 échecs, log par phase).
- Tout /goal existant sans done-check objectif est non-conforme → à amender à sa prochaine invocation (pas de sweep rétroactif).

## Rejeté

- Loops « until satisfied » (subjectif) · fleets 24/7 par défaut (le contexte Steinberger ≠ le nôtre) · auto-vérification par l'agent maker.
