---
type: Concept
title: GTD 5 Stages Capture→Clarify→Organize→Review→Engage — Cerritos
description: Pipeline canonique Getting Things Done d'USS Cerritos Holo Deck. 5 stages × 5 A3 crew, sur Plane.so comme outil Shadow L1.
tags: [gtd, cerritos, capture, clarify, organize, review, engage, plane]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: cerritos-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md
    title: A2 Holo Deck Cerritos Spec
    last_modified: 2026-05-20
  - id: cerritos-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/25_GTD_Cerritos/README.md
    title: 25_GTD_Cerritos README
    last_modified: 2026-06-21
  - id: rutherford-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/25_GTD_Cerritos/03_Organize_Rutherford/A3_Rutherford_Organize_Spec.md
    title: A3 Rutherford Spec — D3 nuance critique
    last_modified: 2026-05-20
okf_version: "0.2"
---

# GTD 5 Stages Capture→Clarify→Organize→Review→Engage — Cerritos

GTD est le framework **chaos-to-action** d'A'Space OS, géré par USS Cerritos (Holo Deck) via Plane.so comme outil Shadow L1. Cinq stages, chacun avec un A3 crew canon.

## Matrice canon 5 stages × 5 A3 twins

| Stage GTD | A3 twin | Stage canon | state.json stage | D3 nuance |
|---|---|---|---|---|
| 1. Capture | **Mariner** | `Capture` | `captured` | raw_input_preview (80 chars) + sha256 hash, `next_step: "A3:Boimler"` |
| 2. Clarify | **Boimler** | `Clarify` | `clarified` | para_bucket assigné + tag (`@next`/`@waiting`/`@someday`/`@archive`) |
| 3. Organize | **Rutherford** | `Organize` | `organized` | **D3 nuance détectée** : `fancy-hugging-bengio.md §15.1` identifie **Tendi = Organize** ; canon local actif garde **Rutherford = Organize** (résolu 2026-05-20) |
| 4. Review | **Tendi** | `Review` | `reviewed` | **D3 nuance détectée** : `fancy-hugging-bengio.md §15.1` identifie **Rutherford = Reflect** ; canon local actif garde **Tendi = Review** |
| 5. Engage | **Freeman** | `Engage` | `engaged` | Freeman = `next_step` actionnable + drift_flag si context drifté, dispatch vers A1 Morty |

## Workflow canon (D1 receipt = plan §3.3)

```
A0 intention (court terme / exécution)
  ↓
[A1 Morty] ← filtre focus (budget tokens, priorité cycle, scope)
  ↓
[A2 Cerritos GTD] ← workflow 5 stages canon
  ├─ Mariner (Capture)     → state.json: "captured"
  ├─ Boimler (Clarify)     → state.json: "clarified" + tag
  ├─ Rutherford (Organize) → state.json: "organized" + bucket PARA
  ├─ Tendi (Review)        → state.json: "reviewed" + drift check
  └─ Freeman (Engage)      → state.json: "engaged" + next_action
```

## Position dans le triptyque MORTY

GTD (Cerritos Holodeck) = **bus horizontal** qui boucle les 2 triptyques (MORTY 12WY⊃PARA⊃DEAL + BETH Ikigai⊃Life Wheel⊃Muse) vers B1 Fractal. Position canon : **A1 Morty Focus → A2 USS Cerritos → A3 5 Airlock**.

## Acceptance Criteria canon

- Every actionable item has a verb and an owner.
- Every multi-step item is escalated to Project or Rock.
- Every blocked item names the missing input.
- No empty heartbeat or task churn is created.

## Sortie Cerritos

```yaml
ship: CERRITOS
a2: Holo Deck
framework: GTD
stage: capture|clarify|organize|review|engage
decision: next_action|project|resource|someday|trash|blocked
route_to: MORTY|ENTERPRISE|SNW|PROTOSTAR|BETH
proof:
  - C:\...
```

## D3 nuance critique (Rutherford = Organize)

`fancy-hugging-bengio.md §3.2` (table canon A3 twins) mappe initialement **Tendi = Organize** (avec **Rutherford = Reflect**). Le canon actif local (résolu 2026-05-20 par A0 sur SDD-008) garde **Rutherford = Organize + Tendi = Review**. Cette spec est alignée avec le canon twin `A2_HoloDeck_Cerritos_Spec.twin.md` ligne 41.

Recommandation D7 close : ne PAS escalader A0 pour réécrire §3.2 du plan — le terrain canon local + twin canon sont cohérents et D4 append-only.