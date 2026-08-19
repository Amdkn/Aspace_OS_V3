---
type: Concept
title: Méthode ↔ Vaisseau ↔ Rôle — mapping canonique 6 ships
description: Chaque méthode Life OS (Ikigai, Life Wheel, 12WY, PARA, GTD, DEAL) est incarnée par un vaisseau Star Trek avec un rôle canon — et chaque vaisseau a un ou plusieurs officiers A3.
tags: [mapping, vaisseau, methode, role, offcier, canon, ships-crew]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: life-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/README.md
    title: 20_Life_OS README — The Starships (Engines)
    last_modified: 2026-05-20
  - id: gatekeepers-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/README.md
    title: 00_Gatekeepers_Beth_Morty README — Operating Law
    last_modified: 2026-06-21
okf_version: "0.2"
---

# Méthode ↔ Vaisseau ↔ Rôle — mapping canonique 6 ships

Chaque méthode Life OS est incarnée par un vaisseau Star Trek avec un rôle canon, ses officiers A3, et son framework de référence. Le mapping est verrouillé canoniquement.

## Table canonique 6 ships

| Méthode | Vaisseau | Rôle canon | Officiers A3 |
|---|---|---|---|
| **Ikigai** | USS Orville | Identifier le "Pourquoi" — Meaning Engine | Ed (Craft/Profession), Kelly (Mission), Gordon (Passion), Claire (Vocation) + Isaac/Lamarr/Bortus/Alara/Klyden (5 Horizons) |
| **Life Wheel** | USS Discovery | Maintenir l'homéostasie — Balance Engine | Stamets (Mycelial Network / Connections LD05), Tilly (Calculations / Mind LD04) + 6 autres LD crew |
| **12 Week Year** | USS SNW | Impact trimestriel — Execution Engine | Pike (Vision), Una (Weekly Plan), M'Benga (Focus), Chapel (Metrics), Ortegas (Execution) |
| **PARA** | USS Enterprise | Architecture de l'information — Structure Engine | Picard (Strategy/Projects), Data (Memory/Archives), Spock (Areas), Geordi (Resources) |
| **GTD** | USS Cerritos | Task management — Chaos Engine | Mariner (Capture), Boimler (Clarify), Rutherford (Organize), Tendi (Review), Freeman (Engage) |
| **DEAL** | USS Protostar | Freedom from Toil — Liberation Engine | Dal (Define), Zero (Automate), Rok-Tahk (Eliminate), Gwyn (Liberate) |

## Doctrine Star Trek canon

> *"Beth is the filesystem conscience and veto. Morty is the terminal router and executor. Morty only acts from a complete Context Pack with Beth clearance."*
> — `20_Life_OS/README.md`

Et :

> *"The Law of Balance — Boldly go where no one has gone before."*
> — `20_Life_OS/README.md`

## Operating Law (gatekeepers)

> *"No L1 action is valid unless it can answer: 1. Which domain or framework is affected? 2. Which A2 ship owns the decision? 3. Which A3 crew member owns the next action? 4. Which evidence path proves the request? 5. Did Beth clear the execution?"*
> — `00_Gatekeepers_Beth_Morty/README.md`

## Pourquoi cette métaphore navires

La métaphore Star Trek n'est pas cosmétique. Elle impose trois invariants :

1. **Chaque méthode = un enginespécialisé** (Meaning / Balance / Execution / Structure / Chaos / Liberation).
2. **Chaque vaisseau a un équipage** (A3 crew narrow findings).
3. **Aucun vaisseau n'agit sans clearance du Command** (A1 Beth + A1 Morty).

## Rattachement couche / domaine

| Layer | Domaine |
|---|---|
| L1 Life OS | Human Experience, Executive Function, Life Wheel, 12WY, PARA, GTD, DEAL |
| L0 Kernel | Infra, serveurs, Syncthing, outils |
| L2 Buz | Cashflow, SOBs, clients, offres |

Life OS ne sort jamais de L1. Les work L2 (cashflow) restent nichés dans L1 (PARA + 12WY).

## Rattachement A1 ownership (D3 nuance close)

Beth et Morty ne sont **pas exclusifs** d'un sous-ensemble de ships. Le plan `fancy-hugging-bengio.md §3.5` simplifie en "responsabilité principale" :

- Beth = Ikigai + Life Wheel + DEAL (3 ships responsabilité principale)
- Morty = 12WY + PARA + GTD (3 ships responsabilité principale)

Mais le canon terrain (D4 close 2026-06-21) garde un veto **distribué** : Beth peut intervenir sur les 6 ships dès qu'une décision touche LD03/LD04. Morty route vers les 6 ships selon la matrice de routage canon.