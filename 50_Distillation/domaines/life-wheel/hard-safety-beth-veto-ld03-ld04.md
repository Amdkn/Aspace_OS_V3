---
type: Concept
title: HARD SAFETY — doctrine Beth veto LD03 LD04
description: Doctrine canon de sécurité — LD03 RED = Beth veto automatic avant routing Morty. LD04 = STOP authority si Culber RED. Seuils chiffrés SDD-005 : LD03_minimum=4.0, LD04_minimum=3.5. Cascade LD03→LD04 vérifiée à chaque Sunday Uplink.
tags: [hard-safety, beth-veto, ld03-ld04-cascade, sdd-005, halt-states, primary-gravity]
generated: { by: minimax-m3, at: 2026-08-19T04:10:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T04:10:00Z }
sources:
  - id: sdd-005
    resource: ASpace_OS_V2/10_Tech_OS/12_Blueprints/01-SDD/SDD-005_life-os-l1-integration.md
    title: SDD-005 Life OS L1 Integration (seuils Beth)
    last_modified: 2026-05-20
  - id: beth-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md
    title: A1 Beth Spec (5 états dont HALT_LD03 / HALT_LD04)
    last_modified: 2026-05-20
  - id: culber-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD03_Health_Culber/A3_Culber_LD03_Spec.md
    title: A3 Culber Spec (HARD SAFETY doctrine)
    last_modified: 2026-05-20
  - id: tilly-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD04_Cognition_Tilly/A3_Tilly_LD04_Spec.md
    title: A3 Tilly Spec (STOP authority)
    last_modified: 2026-05-20
okf_version: "0.2"
---

# HARD SAFETY — doctrine Beth veto LD03 LD04

## Énoncé canon

Deux domaines de la Life Wheel portent une **règle dure** : LD03 (Health/Sleep/Energy) et LD04 (Mind/Cognition). Leur dégradation déclenche un **veto Beth automatic** — c'est la seule règle qui prime sur la cadence A2/A3.

Verbatim canon (plan §18.1, ligne 73 du tableau canon) :
- LD03 : *"HARD SAFETY : RED = Beth veto automatic"*
- LD04 : *"HARD SAFETY : STOP authority"*

## Seuils chiffrés (SDD-005)

```yaml
beth_thresholds:
  LD03_minimum: 4.0
  LD04_minimum: 3.5
  multi_domain_alert: 3
```

- LD03 < 4.0 → état `HALT_LD03` automatic.
- LD04 < 3.5 → état `HALT_LD04` automatic.
- ≥3 LD en alerte → escalade A0 (multi_domain_alert).

Source : `SDD-005_life-os-l1-integration.md` + `A1_Beth_Spec.md` ligne 49 (5 états).

## 5 états Beth mutuellement exclusifs

| État | Sens | Action Morty |
|---|---|---|
| `GREEN` | Evidence présente, santé OK, priorité cohérente | Execute within Context Pack |
| `ORANGE` | Utile mais incomplet ou risqué | Draft only, ask for missing proof |
| `RED` | Health/cognition/priority violation | **Halt execution** |
| `HALT_LD03` | Health/sleep constraint triggered | **Stop L0/L2 acceleration** |
| `HALT_LD04` | Cognitive overload triggered | **Reduce scope, start GTD/PARA cleanup** |

Source : `A1_Beth_Spec.md` lignes 41-50.

## Cascade LD03 → LD04 (primary gravity)

Verbatim canon (A3_Culber_LD03_Spec.md) :
> *"LD03 is primary gravity: when it degrades, L4 cognition degrades in cascade."*

Donc :
- LD03 RED → `HALT_LD03` + Beth veto + **cascading Tilly/LD04**.
- LD04 RED → STOP authority Tilly (cross-check Culber obligatoire) + **PAS exécution sans recovery signal**.

Cascade vérifiée à chaque **Sunday Uplink** (revue hebdomadaire ritualisée, seul moment toléré pour escalader à A0).

## Boundaries Beth (anti-patterns canon)

Source `A1_Beth_Spec.md` §"Anti-Patterns Beth Blocks" :
- ❌ Morty exécute sans `beth_clearance`.
- ❌ A3 Life OS appelle directement L0 technicians (doit passer par Agent Portal / River boundary).
- ❌ L2 business work bypasse PARA et 12WY.
- ❌ Plus d'un cycle 12WY actif en compétition pour la même attention humaine.
- ❌ Health ou cognition traitée comme "later".
- ❌ Tool devient system of record sans documented handoff path.

## Veto distribué (D4 nuance 2026-06-21)

Beth a un **veto distribué** sur les 6 A2 ships (Orville, Discovery, SNW, Enterprise, Cerritos, Protostar), pas seulement Ikigai+Life Wheel+DEAL comme une lecture rapide du plan §3.5 pourrait le suggérer.

Morty a un **routage distribué** sur les 6 ships selon matrice `fancy-hugging-bengio.md §3.6`.

## Verdict distillation

`canon` — fait autorité. Triple source : SDD-005 (seuils chiffrés) + Beth Spec (5 états) + Culber/Tilly specs (HARD SAFETY doctrine). Verrouillé depuis 2026-05-20.

## Pièges documentés

- **Piège 1** : un cycle 12WY Q3 2026 qui tombe sur un ship hors responsabilité principale d'un A1 reste valide — Beth/Morty interviennent quand même via veto/routing. Priorité de cycle = responsabilité principale.
- **Piège 2** : ne pas escalader A0 quotidiennement. A0 board observer = milestones H30/H90 seulement.
- **Piège 3** : sans seuils chiffrés, Beth ne peut pas répondre en <5 minutes. Avec seuils, Beth rejette mécaniquement et escalade seulement les cas ambigus.
