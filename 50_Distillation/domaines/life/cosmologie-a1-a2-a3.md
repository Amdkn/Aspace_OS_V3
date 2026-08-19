---
type: Concept
title: Cosmologie A1/A2/A3 — hiérarchie systémique Life OS
description: Trois étages d'agents — A1 gatekeepers (Beth + Morty), A2 ships framework, A3 crew domain. Chaque niveau compile ; ne décide jamais à la place du niveau au-dessus.
tags: [cosmologie, a1-a2-a3, gatekeepers, ships, crew, hierarchy, life-os]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: beth-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md
    title: A1 Beth Spec
    last_modified: 2026-05-20
  - id: morty-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md
    title: A1 Morty Spec
    last_modified: 2026-05-20
  - id: discovery-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md
    title: A2 Discovery Spec
    last_modified: 2026-05-20
  - id: cerritos-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md
    title: A2 Holo Deck Cerritos Spec
    last_modified: 2026-05-20
okf_version: "0.2"
---

# Cosmologie A1/A2/A3 — hiérarchie systémique Life OS

Life OS orchestre 6 frameworks selon une hiérarchie à trois étages. Chaque niveau compile les findings du niveau au-dessous ; aucun A3 ne compile un rapport final, aucun A1 ne touche au terminal sans gate explicite.

## A1 — Gatekeepers (2 agents)

| Agent | Rôle | Sortie | Outils |
|---|---|---|---|
| Beth | Conscience, veto, PRD-L1 authority | 5 états (GREEN/ORANGE/RED/HALT_LD03/HALT_LD04) | Filesystem + canon SDD |
| Morty | Terminal executor, Context Pack gate, routing | Routage vers les 6 ships, écrit dans state.json | Shadow L1 (Baserow, Obsidian, Plane, Affine, Symphony) |

## A2 — Framework ships (6 ships)

| Ship | Framework | Outil Shadow |
|---|---|---|
| USS Orville | Ikigai (4 Pillars × 5 Horizons) | Obsidian / notes |
| USS Discovery | Life Wheel / ZORA (LD01-LD08) | Baserow `LD00 ZORA` |
| USS SNW / Curie | 12 Week Year (5 disciplines) | Baserow `12WY Warp Core` |
| USS Enterprise / Picard | PARA (Projects/Areas/Resources/Archives) | Obsidian PARA |
| USS Cerritos / Holo Deck | GTD (5 stages) | Plane |
| USS Protostar / Holo Janeway | DEAL (D/E/A/L) | Affine |

## A3 — Domain crew

Chaque A2 ship possède un équipage de 4 à 9 agents qui produisent des findings narrow :

- **Orville** : 9 crew = 4 Pillars (Ed Mercer Profession, Kelly Grayson Mission, Gordon Malloy Passion, Claire Finn Vocation) + 5 Horizons (Isaac H1, John Lamarr H3, Bortus H10, Alara Kitan H30, Klyden H90).
- **Discovery** : 8 crew = Book LD01, Saru LD02, Culber LD03, Tilly LD04, Stamets LD05, Burnham LD06, Reno LD07, Georgiou LD08.
- **SNW** : 5 disciples = Pike Vision, Una Planning, M'Benga Focus, Chapel Metrics, Ortegas Execution.
- **Cerritos** : 5 stages = Mariner Capture, Boimler Clarify, Rutherford Organize, Tendi Review, Freeman Engage.
- **Protostar** : 4 stages = Dal Define, Rok-Tahk Eliminate, Zero Automate, Gwyn Liberate.
- **Enterprise** : 4 rôles = Picard Projects, Spock Areas, Geordi Resources, Data Archives.

## Règle de compilation (canon A2 verbatim)

> *"The A3 domain officers never compile final Discovery reports. They provide LD01-LD08 findings; Discovery/ZORA synthesizes the Life Wheel state and sends the result to Beth or Morty."*
> — `A2_Discovery_ZORA_Spec.md` ligne 66

Cette règle vaut pour **tous** les ships : un A3 ne publie jamais de décision. Seul l'A2 compile ; seul l'A1 décide ou route.

## Anti-paperclip Saru 1000T — 3 garde-fous canon

Le risque le plus nommé dans le corpus : un A3 LD02 Saru mal routé peut paperclip le système sur un objectif 1000T extractif. Trois garde-fous canon verrouillés :

1. **Boundary A3 Saru spec** : "Saru coordinates with Book but does not override LD01 strategy."
2. **AREA_STANDARD P1 Work ON not IN** : Saru ne déclenche B1 review que si ≥2 B2 domains en conflit (scarcity seule ne suffit pas).
3. **Musk pivot = agency over utopia** : Saru DOIT évaluer "augmente-t-elle agency A0 ou attend salvation externe ?"

Le SpaceX IPO 85.7B Greenshoe est l'anti-pattern ingéré — étude de cas dans `_etudes_cas/2026-06-15_spacex-ipo-greenshoe-85-7b.md`.