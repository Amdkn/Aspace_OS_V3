---
type: Concept
title: 3-Turn BMad Air Lock — protocole de clarification
description: Protocole obligatoire avant tout artefact (SDD, PRD, ADR, DDD) ou code. 3 tours : Clarification (questions), Organisation (proposition), Veto Review (GO/NO GO A0). Translucide : la consultation est une condition d'alignement, pas une gate.
tags: [bmad, air-lock, 3-turn, clarification, veto, alignment]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture_v2, at: 2026-08-19 }
sources:
  - id: AGENTS_amadeus
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/01_Identity_Core/AGENTS.md
    title: AGENTS.md — A'Space Sovereign Agent Manifest
    last_modified: 2026-07-25
okf_version: "0.2"
---

# 3-Turn BMad Air Lock — protocole de clarification

## Énoncé

**Global Doctrine for all Agents (A0, A1, A2, A3)** — Before any agent generates an artifact (SDD, PRD, ADR, DDD) or writes code, a strict 3-Turn interaction with the Commanditaire (Amadeus) is mandatory.

## Les 3 tours

### Tour 1 — Clarification (Air Lock)

- **Goal** : Understand the true intent.
- **Action** : The agent explicitly asks questions directly related to the user's initial input or capture. No decisions are made, no artifacts are drafted.

### Tour 2 — Organisation & Proposition

- **Goal** : Innovate and structure the approach.
- **Action** : The agent proposes a strategy to transcend the specs. It outlines how the tools and environments (Meta A'Space Web OS) will be optimized to fulfill the clarified intent.

### Tour 3 — Veto Review

- **Goal** : Final authorization.
- **Action** : The agent presents the proposed direction for an explicit « Veto » or « Go » from A0. Only after a « Go » can artifact generation or coding begin.

## Tension avec la Constitution v1.0

**Article 6** — _le blocage est le seul acte interdit_. Aucun agent ne peut créer de gate, flag bloquant, queue HITL obligatoire, ou mécanisme d'arrêt.

**Le 3-Turn BMad n'est PAS une gate dans ce sens** : ce n'est pas un blocage, c'est une **clarification**. La distinction est subtile mais canonique :

- **Gate** = BLOQUE l'agent, même si tout est clair
- **Clarification** = ALIGNÉ sur l'intention avant de produire

Post-Constitution v1.0, le 3-Turn BMad reste un **signal consultatif** que l'agent lit, pèse, et applique si l'intention est ambiguë. Si l'intention est limpide, l'agent ship sans les 3 tours.

## Article 4bis (V2.0-canon) et BMad

Le 3-Turn BMad est implicitement borné par V2.0-canon : si A+ a explicitement demandé un livrable canon, les 3 tours ne sont pas un obstacle — c'est un filtre. Si A+ n'a pas demandé, l'agent n'a pas à produire, et donc n'a pas à consulter.

## Kardeec Gap

Le protocole est strictement orienté **Commanditaire → Agent**. Quand l'agent prend l'initiative (auto-amélioration Article 4), il n'y a pas de Commanditaire à consulter — il y a le canon à vérifier.

## Anti-pattern

- Produire un ADR sans avoir posé de questions sur l'intention
- Sauter directement à l'implémentation parce que la demande « semble claire »
- Considérer BMad comme une gate formelle (le 3e tour est un GO, pas un visa)
