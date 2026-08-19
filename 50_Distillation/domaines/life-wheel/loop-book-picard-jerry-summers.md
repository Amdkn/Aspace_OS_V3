---
type: Concept
title: Loop Engineering Book→Picard→Jerry→Summers (L2 cross-link)
description: Triangle L2 Business OS — Book (H1 aggregator) supervise Picard (H10 projects), Jerry (B1 Lighting), Summers (B1 Verse). Cadence matrix H10/H1/Daily. ADR-LD01-008 ratifié 2026-07-05, War Mode actif. Book = aggregator (PAS coach direct).
tags: [loop-engineering, adr-ld01-008, picard-h10, jerry-lighting, summers-verse, book-aggregator, war-mode]
generated: { by: minimax-m3, at: 2026-08-19T04:17:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T04:17:00Z }
sources:
  - id: adr-ld01-008
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/30_decisions/ADR-LD01-008_coaching-loop-picard-jerry-summers.md
    title: ADR-LD01-008 — Loop Engineering (ACCEPTED 2026-07-05)
    last_modified: 2026-07-05
  - id: book-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/A3_Book_LD01_Spec.md
    title: A3 Book Spec — aggregator role
    last_modified: 2026-05-20
okf_version: "0.2"
---

# Loop Engineering Book→Picard→Jerry→Summers (L2 cross-link)

## Énoncé canon

Le **triangle Picard × Jerry × Summers**, orchestré par **Book**, forme la tri-direction **L2 Business OS**. Source : `ADR-LD01-008` (ACCEPTED 2026-07-05, War Mode actif).

## Les 4 personnages

| Personnage | Rôle | Horizon | Output canon |
|---|---|---|---|
| **Picard** | USS Enterprise / PARA Projects owner | **H10** (10-week sprint, sister cadence 12WY-Q3-2026) | `<proj>/MANIFEST.md` |
| **Jerry** | B1 Direction macro / Lighting keeper ("keep lights on") | weekly | 4 indicators `lights_*` |
| **Summers** | B1 Direction micro / Verse / quick access | weekly | Prose hebdo du quadrant |
| **Book** | A3 LD01 aggregator | **H1** weekly P&L | Fiche P&L hebdo |

Source : `ADR-LD01-008` D1 lignes 60-64.

## Cadence matrix (3 ticks imbriqués)

```
H10 (10-week sprint) ── Picard tick ──→ <proj>/MANIFEST.md (append-only)
    ↓
H1 (weekly P&L) ── Book tick ──→ Fiche P&L hebdo (append-only)
    ↓
Daily (H0.04 standup) ── Squad B3 ──→ 1 tâche + 1 output + 1 lesson (CARDIA-TDD)
```

À chaque tour, l'épisode est append dans `99_meta/calendar.md` (D4 append-only). Le calendar devient le **log canonique de la boucle**.

## Book = aggregator (PAS coach direct)

Verbatim canon (`A3_Book_LD01_Spec.md` §Boundaries + `ADR-LD01-008` D2) :

> *"Book does not decide business strategy alone. Book does not create Rocks or mutate Baserow. If LD01 consumes more than safe bandwidth, Book escalates to Discovery and Beth."*

Séquence canon du tour H1 :
1. Lit le tick H10 de Picard → `<proj>/MANIFEST.md`.
2. Lit Jerry Pulse → 4 indicateurs "keep lights on".
3. Lit Summers Verse → la ligne narrative du quadrant.
4. Produit la fiche P&L hebdo.
5. Append un épisode-mémoire dans `99_meta/calendar.md`.
6. Escalade à Discovery + Beth si `load_signal = critical` OU `business_coherence = extractive`.

## 4 indicateurs Lighting (Jerry expose)

Subset LD01-coaching déclaré dans `ADR-LD01-008` D3 :
- `lights_project_count` (int) — projets Picard actifs dans la fenêtre H10.
- `lights_load_signal` (enum) — agrégé sur les 8 LDxx par Book.
- `lights_business_coherence` (enum) — sortie Book H1.
- `lights_calendar_dernier_episode` (timestamp ISO 8601) — delta vs tick H1 précédent.

Mise à jour : H1 par Book / H10 par Picard / daily par Squad.

## Anti-patterns (D4)

- ❌ Réécrire la boucle en TypeScript avant que la doctrine soit validée 4+ semaines (YAGNI).
- ❌ Imposer la cadence H1 à Picard (H10 reste son rythme canon).
- ❌ Faire de Book un coach direct (rôle = aggregator).
- ❌ Auto-activer une cron sur cette boucle (Posture C + ADR-WARMODE-001).

## Verdict distillation

`canon` — fait autorité. Source unique : `ADR-LD01-008` (ACCEPTED 2026-07-05, A0 GO tracé dans citadel). War Mode actif, append-only local, réversible par suppression du seul fichier ADR.

## Pièges documentés

- **Piège 1** : Book transformé en coach direct. **Viole canon** — Book = aggregator.
- **Piège 2** : Picard H10 forcé en cadence H1. **Viole canon** — Picard garde son rythme H10.
- **Piège 3** : matérialisation runtime Lighting (Postgres `l2_mesh` view, webhook, fichier canon) sans HITL A0. **D6 YAGNI** — déclarée seulement.
- **Piège 4** : mutation des twins Discovery/Enterprise/Protostar depuis cet ADR. **D4 append-only** — pointeur seul.
