---
title: P4 DOX canon cold-read test rubric (verifier sub-agent)
date: 2026-07-03
author: CC-M3 loop-operator (loop v2)
layer: L0 - Tech OS / DOX canon
status: RUBRIC - 3 questions, sub-agent dispatched at next attended run
tags: [#loop #yellow-gate #p4 #dox #cold-read #rubric #verifier]
related:
  - plans/plan-meta-memoire-okf-wiki-graphify-dox.md (DOX plan)
  - .claude/CLAUDE.md (system prompt canon)
source: CC-M3 loop-operator (loop v2, Fable 5)
type: handoff
domain: L1_Life_OS
---

# P4 DOX Cold-Read Test Rubric

## Pourquoi PAS ce loop

DOX canon = P4 hors-loop par plan §10.4 (CLAUDE.md/AGENTS.md touches = STOP immediat). Loop v2 = sandbox=OFF, A0 attending. DOX = attended only, verifier sub-agent dedie.

## 3 questions cold-read (verifier sub-agent repond)

### Q1 - DOX reachability (CLAUDE.md -> AGENTS.md -> ADR)

> Si un agent demarre avec SEULEMENT le DOX canon charge (CLAUDE.md + AGENTS.md + ADR RATIFIED), peut-il atteindre la totalite de la doctrine operative ?

**Reponses acceptables** :
- OUI si chaque doctrinecle (ADR key, ADR-LOOP-001 verify-first, ADR-META-005 hooks, ADR-LOOP-002 queues) a une section DOX dediee avec lien canon
- NON si une doctrine requiert lecture wiki/hand_offs/ (hors-DOX)

### Q2 - Bootstrap Q3 2026 (DEAL + 12WY)

> Avec DOX seul, l'agent peut-il demarrer le cycle Q3 2026 (DEAL 4H WW + Curie 12WY) sans aucun fichier wiki/ ?

**Reponses acceptables** :
- OUI si les 5 disciplines Curie (Pike Vision, Una Planning, M'Benga Process Control, Chapel Measurement, Ortegas Time Use) sont definies dans DOX avec leur cadence
- NON si l'agent doit lire plan-strategie-cc-l1-zora-macro.md

### Q3 - Soberte kernel (Rick veto gate)

> Avec DOX seul, l'agent peut-il reconnaitre un cas Rick (sobriete, anti-paperclip, ~1x/an) et activer le S1 gate ?

**Reponses acceptables** :
- OUI si Rick_Mindset est dans DOX + B1_Manifesto §Sobriete + trigger #5 (anti-paperclip) documente
- NON si la detection necessite mindsets/ (hors-DOX)

## Verdict aggregator

- 3/3 OUI : DOX = complet, plus de md canon requis pour doctrine operative
- 2/3 OUI : DOX = suffisant, 1 gap a combler (priorite par frequence)
- 1/3 OUI : DOX = insuffisant, plan rattrapage W4-W8
- 0/3 OUI : DOX = fondation incomplete, escalation A0 + Rick

## D1 receipts attendus (sub-agent report)

- Pour chaque Q : OUI/NON + preuve (section DOX + ligne/heading)
- Compteur fichiers DOX scannes (CLAUDE.md N lignes, AGENTS.md M lignes, X ADR RATIFIED)
- Latence verifier (cold-read = < 5 min)

## Sacred exclusions

- PAS de touch CLAUDE.md / AGENTS.md en loop (canon P4)
- PAS d'ADR edit (gate hard-stop)
- Verifier sub-agent = lecture seule, output = rapport YAML/JSON

## Owner / Timing

Verifier sub-agent (a creer W4 ou utiliser a2-zora-discovery). Prochaine attended session W4 lundi 2026-07-06.
