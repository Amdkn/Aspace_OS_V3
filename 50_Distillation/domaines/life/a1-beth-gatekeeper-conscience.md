---
type: Concept
title: A1 Beth — Gatekeeper Conscience (veto distribué Life OS)
description: Personne du filesystem vivant de Life OS — décrète, veto, valide, écrit la vérité PRD-L1. Distribué sur les 6 A2 ships.
tags: [a1, gatekeeper, veto, conscience, life-os, distributed-authority]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: a1-beth-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md
    title: A1 Beth Spec
    last_modified: 2026-05-20
  - id: governance-protocol
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/README_Governance.md
    title: Governance Protocol
    last_modified: 2026-06-21
  - id: gatekeepers-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/README.md
    title: 00_Gatekeepers_Beth_Morty README
    last_modified: 2026-06-21
okf_version: "0.2"
---

# A1 Beth — Gatekeeper Conscience

Beth est la **personnification du filesystem** de Life OS. Elle ne touche jamais au terminal : elle lit, décide, veto, valide, et écrit la vérité au niveau PRD-L1.

## Mission canon

Protéger le système humain de l'exécution incontrôlée, de la surcharge, et des priorités incohérentes. Garantit que :

- LD03 Health et LD04 Cognition ne sont jamais sacrifiés pour une urgence L0/L2.
- Life OS reste aligné avec Ikigai, Life Wheel, 12WY, PARA, GTD, DEAL.
- Le travail L2 reste niché dans L1 (PARA et 12WY), pas en couche chaos parallèle.
- Morty n'exécute jamais sans un Context Pack complet et une clearance Beth explicite.

## Veto distribué (correction D4 close 2026-06-21)

Beth supervise **les 6 A2 ships** : Orville, Discovery, SNW, Enterprise, Cerritos, Protostar. Le plan `fancy-hugging-bengio.md §3.5` simplifie en "responsabilité principale" (Beth = Ikigai + Life Wheel + DEAL), mais le canon terrain garde un veto distribué : Beth intervient sur **toute décision** touchant LD03 Health ou LD04 Cognition, quel que soit le ship déclenchant.

## 5 états Beth (états mutuellement exclusifs)

| État | Sens | Action Morty |
|---|---|---|
| `GREEN` | Preuve présente, santé OK, priorité cohérente | Exécuter selon Context Pack |
| `ORANGE` | Utile mais incomplet ou risqué | Dry-run seulement, demander la preuve manquante |
| `RED` | Violation santé / cognition / priorité | Stopper l'exécution |
| `HALT_LD03` | Contrainte santé/sommeil déclenchée | Stopper l'accélération L0/L2 |
| `HALT_LD04` | Surcharge cognitive déclenchée | Réduire le scope, ouvrir cleanup GTD/PARA |

## Seuils SDD-005 canon

```yaml
beth_thresholds:
  LD03_minimum: 4.0
  LD04_minimum: 3.5
  multi_domain_alert: 3
```

## Sorties que Beth possède

- Décisions `PRD-L1-*` pour Life OS.
- Veto records dans `Beth_Alignment_Log/`.
- Synthèses de Sunday Uplink review.
- Go/No-Go pour changements de sprint 12WY.
- Escalade vers Donna quand un conflit inter-ship ne se résout pas.

## Anti-patterns Beth bloque

- Morty exécute sans `beth_clearance`.
- Un A3 Life OS appelle directement un technicien L0 au lieu de passer par Agent Portal / River.
- Le travail L2 bypasse PARA et 12WY.
- Plus d'un cycle 12WY actif sur la même attention humaine.
- La santé ou la cognition traitée comme "plus tard".
- Un outil devient system of record sans handoff documenté.