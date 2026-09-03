---
title: "Summers Verse: ingestion Solaris (registre des sources + verifier) dans 00_Summers_Verse"
layer: L2
originator: wheel_consumer (cron metabolique)
source: 20_Life_OS/22_Wheel_Discovery/state.json
statut: FROZEN
date: 2026-09-03
---

## Irritant

Le bus Wheel Discovery (work 35) signale `LD01` GREEN, load low, route
`PROTOSTAR_DEAL` — Beth verte (beth_action: none). Ce signal n'avait aucun
consommateur : aucune traduction en work L2 de production de valeur.

## Résultat visé

Summers Verse: ingestion Solaris (registre des sources + verifier) dans 00_Summers_Verse

## Contraintes

- Passer par le portier `_INBOX/B1_Jerry_Summers/` -> `gate.py run` (L2).
- Pyramide L0 >= L1 > L2 : Beth a le veto, respecter `30_Business_OS/AGENTS.md`.
- Ne pas toucher `10_Tech_OS/kernel/` ni `20_Life_OS/`.

## Definition of Done

- [ ] `30_Business_OS/00_Summers_Verse/` contient le livrable cite dans
      l'objectif, avec un registre JSON lisible par `python -m json.tool` (rc=0).
- [ ] Un verifier executé (`python <verifier>.py`) retourne rc=0 et imprime
      au moins 1 critere OK.
- [ ] Le work uc.db correspondant porte une prediction pre-enregistree AVANT
      la premiere evidence (loi de prediction, schema.sql).
