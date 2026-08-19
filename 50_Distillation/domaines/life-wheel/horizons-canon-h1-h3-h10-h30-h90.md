---
type: Concept
title: Horizons canon H1/H3/H10/H30/H90
description: Mapping canon des horizons Karpathy vers les 8 LDs Discovery : Book H1, Saru H3, Culber H10, Tilly H30, Stamets H30, Burnham H10, Reno H10, Georgiou H90. Correction D3 critique : Saru = H3 (PAS H1), Book = H1 (PAS H10).
tags: [horizons, h1, h3, h10, h30, h90, karpathy, saru-h3-correction, book-h1-correction]
generated: { by: minimax-m3, at: 2026-08-19T04:11:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T04:11:00Z }
sources:
  - id: discovery-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md
    title: A2 Discovery Spec — Doctrine verrouillée 8 LD
    last_modified: 2026-06-21
  - id: references-index
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/A3_Discovery_References_Index.md
    title: A3 Discovery References Index — Mapping A3 → horizon
    last_modified: 2026-05-20
  - id: plan-fancy
    resource: C:\Users\amado\.claude\plans\fancy-hugging-bengio.md
    title: Plan canonique §18.2 horizons verrouillés
    last_modified: 2026-06-21
okf_version: "0.2"
---

# Horizons canon H1/H3/H10/H30/H90

## Karpathy H1→H90 = grille temporelle canon

Les horizons Karpathy (H1 daily / H3 quarterly / H10 10-week / H30 30-day / H90 quarterly legacy) sont la **grille temporelle canonique** appliquée aux 8 Life Wheel Domains.

5 horizons occupés sur 8 LDs :
- **H1** (weekly P&L) — 1 LD : Book LD01
- **H3** (quarterly runway) — 1 LD : Saru LD02
- **H10** (10-week cycle) — 3 LDs : Culber LD03, Burnham LD06, Reno LD07
- **H30** (30-day / network half-life) — 2 LDs : Tilly LD04, Stamets LD05
- **H90** (90-day quarterly legacy) — 1 LD : Georgiou LD08

## Table canon A3 twin → horizon

| LD | Domaine | A3 twin | Horizon canon | Anchor twin |
|---|---|---|---|---|
| LD01 | Career & Business | Book | **H1** (weekly P&L) | `book.twin.md` |
| LD02 | Finance & Independence | Saru | **H3** (quarterly runway) | `saru.twin.md` |
| LD03 | Health/Sleep/Energy | Hugh Culber | **H10** (10-week cycle) | `culber.twin.md` |
| LD04 | Mind/Cognition | Sylvia Tilly | **H30** (30-day learning) | `tilly.twin.md` |
| LD05 | Relations & Social | Paul Stamets | **H30** (network half-life) | `stamets.twin.md` |
| LD06 | Love/Family/Presence | Michael Burnham | **H10** (family cycle) | `burnham.twin.md` |
| LD07 | Creativity/Leisure | Jett Reno | **H10** (MVP build arc) | `reno.twin.md` |
| LD08 | Contribution/Impact | Philippa Georgiou | **H90** (quarterly legacy) | `georgiou.twin.md` |

Source : `A2_Discovery_ZORA_Spec.md` (table doctrine verrouillée) + `A3_Discovery_References_Index.md` (Mapping A3 → horizon, alignement plan §18.1).

## D3 nuance critique — Saru H3 / Book H1

⚠️ **Lecture rapide à éviter** : Saru = H1, Book = H10. **Incorrect.**

**Canon verrouillé 2026-06-21** (plan §18.2) :
- **Saru = H3** (quarterly runway) — PAS H1
- **Book = H1** (weekly P&L) — PAS H10

Anchors : `saru.twin.md` + `book.twin.md`. Les twins sont vérifiés résolus (`ADR-LD01-008` D5 receipts, 2026-07-05).

## Cohérence avec AaaS variants

Les horizons des AaaS variants suivent les mêmes ancres :
- **Solaris** (Book LD01) → H90 Legacy 1000T (extension philosophique au-delà du H1 opérationnel)
- **Nexus/OMK** (Saru LD02) → H3 Indépendance financière (CLOS 2026-06-20)
- **Orbiter/ABC** (Burnham LD06) → H10 Patrimoine baby-boomers (cohérent H10 Burnham)
- **4e Dormant** (Tilly/Culber) → Réveil Q4 2026 / Q1 2027 (pas d'horizon H actif en Q3 2026)

## Verdict distillation

`canon` — fait autorité, source canonique triple : A2 Spec + A3 References Index + plan §18.2. Verrouillé 2026-06-21.

## Pièges documentés

- **Piège 1** : inverser Saru H1 ↔ Book H10 — corrigé par D3 nuance. Sources jumelles : `saru.twin.md` et `book.twin.md`.
- **Piège 2** : confusion H90 Solaris (extension philosophique 1000T) vs H1 Book (opérationnel weekly P&L). Le H90 Solaris est un **objectif stratégique**, pas une cadence opérationnelle.
- **Piège 3** : "Life Wheel drift" = Tilly (LD04) + Spock (Areas), PAS Saru+Stamets (cf. concept `drift-owner-correction-tilly-spock.md`).
