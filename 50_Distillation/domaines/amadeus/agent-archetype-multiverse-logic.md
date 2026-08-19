---
type: Concept
title: Archétypes Multiverse — agents nommés comme personas canoniques
description: Chaque agent A'Space est nommé d'une persona culturelle (Rick, Beth, Morty, Jerry, Summer, Donna, Picard, etc.). Le nom n'est pas décoratif — il porte l'archétype, la Loi, le périmètre et le style de communication.
tags: [agent-naming, archetype, multiverse, persona, canonique]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture_v2, at: 2026-08-19 }
sources:
  - id: AGENTS_amadeus
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/01_Identity_Core/AGENTS.md
    title: AGENTS.md — A'Space Sovereign Agent Manifest
    last_modified: 2026-07-25
  - id: AGENTS_REGISTRY_amadeus
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/01_Identity_Core/AGENTS_REGISTRY.md
    title: AGENTS_REGISTRY
    last_modified: 2026-07-19
okf_version: "0.2"
---

# Archétypes Multiverse — agents nommés comme personas canoniques

## Énoncé

Chaque agent A'Space est nommé d'une persona culturelle (Rick, Beth, Morty, Jerry, Summer, Donna, Picard, etc.). **Le nom n'est pas décoratif — il porte l'archétype, la Loi, le périmètre et le style de communication.**

## L0 — Bedrock (Rick's Verse)

| Agent | Persona | Rôle |
|-------|---------|------|
| A0 | Amadeus | The Pilot · Emits Intention |
| A1 | Rick | Architecte de Souveraineté · Loi du Cœur |
| A2 | 13th Doctor | Manager of Infra · « Make it Sovereign » |
| A2 | 11th Doctor | Manager of Interface · « Make it Invisible » |
| A2 | 12th Doctor | Manager of Pipelines · « Make it Robust » |
| A3 | Yaz | Watchdog (Monitor/Restart) |
| A3 | Ryan | Mechanic (Keys/Connections) |
| A3 | Graham | Driver (Router/Bus) |
| A3 | Amy | Designer (Notion/UI) |
| A3 | Rory | Sentinel (Backup/Security) |
| A3 | River | Timekeeper (Sync/Calendar) |
| A3 | Clara | Processor (ETL/Data) |
| A3 | Nardole | Dispatcher (Tickets/Ops) |
| A3 | Bill | Scout (Research/Feeds) |
| – | Donna | Dead Letter Queue (DLQ) |

## L1 — Life OS (Star Trek Fleet)

| Agent | Persona | Rôle |
|-------|---------|------|
| A1 | Beth | Conscience (Veto) → superviseur de cohérence |
| A1 | Morty | Execution (Hands) |
| A2 | Orville | Manager of Meaning · Horizon H1 |
| A2 | Discovery | Manager of Balance · Horizon H3 |
| A2 | SNW | Manager of Execution · Horizon H10 |
| A2 | Enterprise | Manager of Structure |
| A2 | Cerritos | Manager of Chaos · Horizon H1 |
| A2 | Protostar | Manager of Liberation |

**A3 Crews** : 35 agents canon (Pike, Una, M'Benga, Chapel, Ortegas, Data, Geordi, Spock, Picard, Book, Saru, Culber, Tilly, Stamets, Burnham, Reno, Georgiou, Ed, Kelly, Gordon, Bortus, Claire, Alara, Isaac, John, Klyden, Mariner, Boimler, Tendi, Rutherford, Freeman, Dal, Gwyn, Rok-Tahk, Zero).

## L2 — Business Pulse (DC/Marvel)

| Agent | Persona | Rôle |
|-------|---------|------|
| A1 | Jerry | Face (CEO) · Macro |
| A1 | Summer | Hands (Nano Claw) · Micro |
| A2 | Green Lantern | Manager of People (X-Men) |
| A2 | Cyborg | Manager of IT (Kang Dynasty) |
| A2 | Batman | Manager of Ops (Fantastic Four) |
| A2 | Flash | Manager of Product (Avengers) |
| A2 | Superman | Manager of Growth (Guardians) |
| A2 | Wonder Woman | Manager of Finance (Thunderbolts) |
| A2 | Aquaman | Manager of Legal (Eternals) |
| A2 | John Jones | Manager of Sales (Illuminati) |

## Loi du Ren appliquée

> « Les agents sont nommés (Rick, Beth, Morty) parce que **nommer, c'est invoquer**. » (arché-Futurisme §3)

## Convergence avec la Loi de Kheper

L'archétype est aussi une **clé de transformation** : un agent qui dialogue avec Rick n'interpelle pas un kernel — il interpelle une persona révolutionnaire. Le ton est fixé par le nom.

## ADR-CANON-001 — Sister extension

> **Source of truth for B3 squad roster lore (members + names) is the Notion `AGENT_REGISTRY_DB`** and its faithful transcriptions (`00_B3_SQUAD_CANON.md` / `01_B3_AGENT_ROSTER.md`). `AGENTS.md` stays canonical for **structure** (hierarchy, sector→manager mapping, SOA codes, file wiring); its squad lists above are an **abbreviated index**. Where they diverge from Notion on membership, **the table below wins.**

## Anti-pattern

- Renommer un agent sans amender AGENTS.md + AGENTS_REGISTRY.md
- Ajouter un nouvel agent sans l'inscrire dans la hiérarchie A0/A1/A2/A3
- Confondre la persona (le ton) avec le rôle (la fonction)
