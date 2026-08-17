---
type: Concept
title: Cerritos GTD Pipeline
description: Chaîne de routage des idées — Mariner (capture) → Boimler (clarify) → Rutherford (organize) → Tendi (review) → Freeman (engage) — 5 acteurs canoniques couvrant le cycle GTD de Cerritos.
tags: [concept, gtd, cerritos, picard, routing, ideas, life-os]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraire_substrat_rdf, at: 2026-08-17T19:50:00Z }
  - { by: process:lecture_concepts_picard, at: 2026-08-17T21:00:00Z }
sources:
  - id: manifest-handoff-abc
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/02 ABC OS & Child Care BOS/CERRIROS_HANDOVER.md"
    title: Handover ABC — chaîne Jerry → Cerritos → Picard
    last_modified: 2026-05-21
  - id: cerritos-plane-manifest
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/Cerritos_Plane_Onboarding/MANIFEST.md"
    title: Cerritos × Plane Onboarding Manifest (status ACTIVE, 2026-06-22)
    last_modified: 2026-06-22
  - id: identity-canon-cerritos
    resource: "C:/Users/amado/ASpace_OS_V2/00_Amadeus/01_Identity_Core/AGENTS.md"
    title: Identity Core AGENTS.md l.126-129 (référencé)
    last_modified: 2026-07-15
okf_version: "0.2"
---

# Cerritos GTD Pipeline

## Définition

Pipeline de routage **GTD** (Getting Things Done) appliqué à toute idée
entrant dans A'Space OS. Cinq acteurs canoniques, inspirés de
l'équipage du USS Cerritos (Star Trek Lower Decks) :

| Étape | Acteur | Verbe |
|-------|--------|-------|
| 1 | **Mariner** | Capture — verbatim dans l'inbox |
| 2 | **Boimler** | Clarify — classer (actionable, multi-step, someday/maybe) |
| 3 | **Rutherford** | Organize — router vers Projects / Areas / Resources / Archives |
| 4 | **Tendi** | Review — vérifier non-drift, graduation candidate |
| 5 | **Freeman** | Engage — next action, schedule |

## Chaîne canonique

L'application aux projets clients suit la chaîne :

```
Jerry Prime (A1 vision)
    │
    ▼
Cerritos (GTD pipeline — idea triage and routing)
    │
    ▼
Picard / Summer's Verse (B1 — opens, decides, delegates)
    │
    ├──► B2 Managers (Rocks per domain)
    │        │
    │        ▼
    │    B3 Marvel Squads (execution)
    │
    └──► B3 Warp Core (Lead/Lag logs + artifact proofs)
```

**Cerritos est obligatoire.** Le handover ABC est non-équivoque : "Ideas
do NOT flow Jerry → Picard directly. Cerritos is the mandatory
intermediate. Jerry's role is criteria-setter, not receiver."

## SLA et règles

| Règle | Application |
|-------|-------------|
| **Inbox zéro en 4h** | Idées acquittées en 4h, jours ouvrés |
| **Routing SLA** | Toute idée routée à Picard en 48h |
| **Escalade inaction** | Si Picard inactif >72h → Jerry escalade B1 |
| **Détection pattern** | Tâche récurrente (3x) → délégation WHO, pas process HOW |
| **Child Care extra** | Idées compliance routées priorité haute (risque liability) |

## Application à un outil externe — Plane.so

Le projet `Cerritos_Plane_Onboarding` teste le mapping entre le pipeline
Cerritos et Plane.so (3 items backlog classés via les 5 stages canoniques) :

- **ASPAC-3** "Invite your team" → Projects/actions
- **ASPAC-6** "Use Cycles to time box tasks" → Projects/next-action W3
- **ASPAC-7** "Customize your settings" → Resources/someday-maybe W8+

**Anti-pattern D6 noté** : le Plane workspace live expose 5 default states
(Backlog, Todo, In Progress, Done, Cancelled) — les **states GTD
canoniques** (Inbox, Next Actions, Today, Waiting For, Done, Cancelled,
Trash) ne sont **pas créés**. C'est un follow-up noté dans `mcp-plane.py`
docstring ; A0 action requise (effort 2 min).

## Liens

- [[summers-verse-framework]] — la cible du routage
- [[cerritos-plane-onboarding]] — le test Plane.so
- [[picard-project-pattern]] — l'origine du rôle A3 Picard (Projects canon)

## Note de confiance

**Confirmé par machine.** La chaîne est lisible dans 4 handovers identiques
(ABC, RILCOT, Alikaly, Marina) et dans le manifest Cerritos × Plane.
L'anti-pattern D6 Plane est documenté dans le manifest Cerritos_Plane_Onboarding.
Aucune trace d'application Cerritos en dehors des handovers et du projet
Plane.

*Standing : pipeline défini, application limitée à 1 projet (Plane).*
