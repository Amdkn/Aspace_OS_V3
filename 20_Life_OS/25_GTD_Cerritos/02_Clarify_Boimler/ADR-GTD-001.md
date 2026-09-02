---
id: ADR-GTD-001
title: ADR-GTD-001 — canon 5 stages Cerritos
status: accepted
date: 2026-09-02
deciders:
  - amdkn (Amadou Kone, architecte A'Space OS V3)
  - Rory Build (constructeur A, L1 Life Core — rédaction)
reviewers:
  - 11e Docteur (L1 Life Core — détachement)
source: 20_Life_OS/25_GTD_Cerritos/01_Inbox_Mariner/inbox.md (item 1)
gap: "gap #10 du plan fancy-hugging-bengio (§15.2, row 10)"
---

# ADR-GTD-001 — Canon 5 stages Cerritos

## Context

Le framework GTD d'A'Space OS V3 est porté par l'A2 Holo Deck à bord de l'USS
Cerritos (`20_Life_OS/25_GTD_Cerritos/`). Sa description de fait existe depuis
des mois, mais aucun Architecture Decision Record ne l'a formellement actée :

- `20_Life_OS/25_GTD_Cerritos/README.md` décrit la matrice canon 5 stages × 5
  A3 twins (Mariner=Capture, Boimler=Clarify, Rutherford=Organize, Tendi=Review,
  Freeman=Engage) et le workflow canon du plan
  `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` (§3.5, §3.7, §15.1, §15.2).
- `20_Life_OS/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md` fixe les
  responsabilités du Holo Deck : capture d'entrées brutes, clarification
  d'actionnabilité, organisation des next actions, revue hebdomadaire, routage
  des packets d'engagement vers Morty. Sa section Crew porte la même matrice
  et note explicitement le conflit canon SDD-008 (Tendi/Rutherford inversés),
  résolu en faveur du terrain local le 2026-05-20 (canon actif).
- `20_Life_OS/25_GTD_Cerritos/01_Inbox_Mariner/inbox.md` (item 1, capture du
  2026-09-02) porte la demande : créer ADR-GTD-001 pour figer le canon 5 stages
  Cerritos — gap #10 du plan fancy-hugging-bengio.

Sans cet ADR, toute session qui reprend le framework doit reconstituer la
matrice depuis trois fichiers dispersés, et le conflit SDD-008 peut être
relancé indéfiniment au lieu d'être clos par une décision formelle.

## Decision

L'A2 Holo Deck Cerritos adopte le canon suivant, effectif immédiatement :

### 1. Les cinq stages GTD canon

| # | Stage | State bus | Sortie canon |
|---|---|---|---|
| 1 | `capture` | `captured` | raw_input_preview (80 chars) + sha256 hash |
| 2 | `clarify` | `clarified` | bucket PARA + tag (`@next`/`@waiting`/`@someday`/`@archive`) |
| 3 | `organize` | `organized` | bucket PARA assigné, route + destination Airlock |
| 4 | `review` | `reviewed` | stale/blocked/repeated check + drift check |
| 5 | `engage` | `engaged` | `next_step` actionnable + drift_flag, dispatch A1 Morty |

### 2. Les cinq A3 twins Cerritos, un par stage

| Twin | Stage | Dossier |
|---|---|---|
| **Mariner** | Capture | `01_Inbox_Mariner/` |
| **Boimler** | Clarify | `02_Clarify_Boimler/` |
| **Rutherford** | Organize | `03_Organize_Rutherford/` |
| **Tendi** | Review | `04_Review_Tendi/` |
| **Freeman** | Engage | `05_Engage_Freeman/` |

Ce mapping **prévaut** sur `fancy-hugging-bengio.md §15.1` (qui mappait
Tendi=Organize / Rutherford=Reflect) et sur `SDD-008`. Le conflit est clos :
la résolution du 2026-05-20, confirmée par `A2_HoloDeck_Cerritos_Spec.md`
(sections Crew et A3 Findings Contract), devient la décision formelle. Toute
inversion future exige un nouvel ADR, pas une réécriture silencieuse.

### 3. Bus d'état

Chaque transition de stage écrit dans
`00_Amadeus/40_SYMPHONY_BUS/state.json` (schema state-bus.v1, pattern §3.7 du
plan). Machine à états sémantique, pas d'UI visuelle.

### 4. Frontières inchangées

- Cerritos possède les next actions, pas la stratégie de vie.
- Plane.so reste la surface Shadow ; toute mutation distante exige un scope
  API vérifié (statut `NEEDS_CONTEXT7` tant que non vérifié).
- Escalades : projet → Enterprise (PARA), rock/tactique → SNW (12WY),
  overload → Beth (veto HALT).

## Consequences

1. **Qui capture / qui clarifie** : toute nouvelle entrée brute va dans
   `01_Inbox_Mariner/inbox.md` (1 ligne = 1 raw input, source citée, sinon
   `hypothesis`). Mariner ne clarifie jamais ; le cochage de l'item 1 de
   l'inbox appartient à Boimler en Clarify, hors de ce ruban. Le prochain
   owner de tout item ouvert est `A3:Boimler` (ou Beth si escalade).
2. **Cohérence documentaire verrouillée** : les fichiers `README.md` et
   `A2_HoloDeck_Cerritos_Spec.md` cessent d'être des descriptions de fait
   dispersées ; cet ADR devient la référence formelle qu'ils pointent. Un
   désaccord futur entre eux se résout par amendement de cet ADR.
3. **Escalades définies** : un item plus grand qu'une next action (plus
   d'une session ou d'une semaine) est escaladé à Enterprise (projet PARA) ou
   SNW (rock 12WY) ; un overload déclenche un signal Beth, dont le veto HALT
   rouge fige toute accélération L2.
4. **Conflit canon clos** : le mapping Tendi/Rutherford inversé du plan
   (§15.1) ne peut plus être relancé comme hypothèse ouverte — il est tranché
   ici, append-only (D4).
5. **Implementations dérivées** : `state_writer.py` (state-bus.v1, inbox
   item 2) et toute vérification du scope API Plane (item 3) doivent se
   conformer à la matrice ci-dessus.
