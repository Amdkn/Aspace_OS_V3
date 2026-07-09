---
name: plane-12wy-cycle
version: 1.0
created: 2026-06-07
phase: DECIDE + EXECUTE
tracker: Plane
actor: SNW captain (Pike) + Asha/Freeman crews
---

# 07 — Plane 12-Weeks Year Cycle

> **Plane** est la source de vérité **tactique** de Life OS. Il porte le cycle
> 12 Weeks Year (12WY) — 12 semaines de focus intense avec 3-5 objectifs
> hard-commit.

## Cycle 12 Weeks Year (canon)

```
Semaine 0  ────  Semaine 1-11  ────  Semaine 12
(Planning)       (Execution)          (Review)
   │                 │                   │
   ▼                 ▼                   ▼
3-5 goals       Weekly review        Scorecard
Weekly OKRs     + Daily 90min        + Reset
```

| Phase | Semaine | Activité | Crew A3 principal |
|---|---|---|---|
| **Planning** | S0 | Définir 3-5 goals SMART | Pike (captain) + Asha |
| **Execution** | S1-S11 | Daily 90min, weekly review | Freeman + crews SNW |
| **Review** | S12 | Scorecard, retrospective, reset | Pike + Tilly (LD04) |

## Plane.so schema (cycles + issues)

### Cycle
```
[ID] [Name] [StartDate] [EndDate] [Goals] [Scorecard] [Status]
```

### Issue (1 per goal/sous-tâche)
```
[ID] [CycleID] [Title] [Description] [Assignee] [State] [Priority]
[T-Shirt Size] [StartDate] [DueDate] [PulseTickID]
```

**States** : `Backlog` → `Todo` → `In Progress` → `Done` → `Verified`
**Priority** : `Urgent` (P1) · `High` (P2) · `Medium` (P3) · `Low` (P4)

## Hand-off SNW → autres vaisseaux

| Besoin | Routage vers | Format |
|---|---|---|
| Knowledge graph (leçons de la semaine) | Enterprise (PARA) | Issue Plane + `[[obsidian:lesson-X]]` |
| Health check (intensity trop haute) | LD03 Culber | Issue avec `tag: health-alert` |
| Tâche clarifiée | Cerritos (GTD) | Issue `state=Clarify` routée |
| Goal 12WY | Orville (Ikigai pilier concerné) | Cycle Plane lié à pilier Ikigai |

## Daily 90min (canon)

Chaque jour, Freeman (crew A3 SNW) ouvre **un slot 90min** non-négociable :
- 0-10 min : review issues Plane
- 10-80 min : execution goal #1 du jour
- 80-90 min : log dans `pulse.log` (phase EXECUTE)

**Anti-pattern** : 90min scindé en multiples sessions → perte de flow.

## Weekly review (chaque dimanche)

| Step | Crew A3 | Durée |
|---|---|---|
| 1. Score vs goals | Pike | 15 min |
| 2. Issues Done / Verified | Freeman | 15 min |
| 3. Leçons dans Obsidian | Enterprise | 20 min |
| 4. Reset semaine prochaine | Pike | 10 min |
| Total | — | 60 min |

## Anti-patterns

- ❌ Goal 12WY sans `T-Shirt Size` (rend capacity planning impossible)
- ❌ Issue sans `PulseTickID` (rend OBSERVE aveugle)
- ❌ SNW crew qui crée un cycle < 12 semaines (viole canon 12WY)
- ❌ 12WY captain qui omet le scorecard S12 (rend l'apprentissage nul)

## Source canonique

- `20_Life_OS/` SNW (12 Weeks Year canon)
- Frame : 12WY (Moran & Lennington)
- Pattern : LD04 (Cognition/Tilly) — corrélation intensité ↔ santé cognitive
