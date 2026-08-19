---
type: Concept
title: Canon Tripartite des Blueprints — B1 → B2 → B3
description: Le canon ADR-FWK-021 qui définit la structure de tout blueprint (SDD, ADR, PRD, DDD) : B1 = direction, B2 = DoD domaine, B3 = JTBD à exécuter. Toujours, sans exception.
tags: [adr-fwk-021, canon-tripartite, blueprint, b1-b2-b3, sdd, adr, prd, ddd]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: SUMMERS_VERSE_MANIFEST
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/SUMMERS_VERSE_MANIFEST.md"
    title: Summer's Verse Manifest — CEO's Desktop
    last_modified: "2026-06-07"
  - id: CLAUDE_CEO_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/CLAUDE.md"
    title: CLAUDE.md — CEO's Desktop
    last_modified: "2026-06-07"
  - id: ADR-FWK-021
    resource: "30_Business_OS/10_Projects/ceo-desktop/CLAUDE.md (référencé)"
    title: ADR-FWK-021 — Canon Tripartite des Blueprints
    last_modified: "2026-06-07"
okf_version: "0.2"
---

# Canon Tripartite des Blueprints — B1 → B2 → B3

> **Une seule chose à retenir.** Tout blueprint (SDD, ADR, PRD, DDD) suit la triade **B1 → B2 → B3**. Pas de B3 sans B2 DoD, pas de B2 sans B1 direction, pas de B1 sans preuve de B0 (le besoin).

## Énoncé canonique

> Canon Tripartite des Blueprints (ADR-FWK-021): B1 direction → B2 domain DoD → B3 jobs to be done, with explicit handoffs and proof paths. (`SUMMERS_VERSE_MANIFEST.md`, `CLAUDE.md`)

## La triade appliquée aux types de documents

Le dépôt `04_Business_Domains/09_Blueprints/` matérialise la triade via 4 sous-dossiers, un par type :

| Type    | Couche dominante | Question répondu                  | Exemple vide observé      |
|---------|------------------|------------------------------------|---------------------------|
| `01-SDD`| B1 (direction)   | « Quel système veut-on, et pourquoi ? » | dossier vide de `.md`     |
| `02-ADR`| B1 (décision)    | « Quelle décision d'architecture prend-on, et avec quelles contraintes ? » | 4 ADRs top-level dans `09_Blueprints/02-ADR/` |
| `03-PRD`| B2 (DoD)         | « Quelles sont les DoD, les features, les specs ? » | dossier vide de `.md` |
| `04-DDD`| B3 (JTBD)        | « Quel travail concret, par quel squad, avec quelle preuve ? » | dossier vide de `.md` |

## Pourquoi cette triade

- **Pas de dérive vers le bas.** Un B2 qui commence à écrire du B3 (du tactique) casse la triade ; un B1 qui commence à exécuter casse la triade. Le canon empêche la substitution.
- **Hand-offs explicites.** Chaque transition B1→B2 ou B2→B3 est tracée (`B2_HANDOFF_QUEUE.md`, JTBD packets). Un handoff sans handoff doc n'existe pas.
- **Proof paths requis.** Le B3 ne prouve pas à B1 directement ; il prouve à B2, qui valide à son tour et reporte à B1. C'est l'anti-babysitting appliqué au papier.

## Observation sur le corpus

Les 5 fichiers top-level de `09_Blueprints/` sont :
- `02-ADR/ADR-CK-FREE-001_clickup-free-constraints.md` (RATIFIÉ)
- `02-ADR/ADR-ID-001_identifiants-universels.md` (RATIFIÉ)
- `02-ADR/ADR-MESH-L2-001_tri-plateforme-doctrine.md` (RATIFIÉ)
- `02-ADR/ADR-NOTION-001_back-office-solaris-template.md` (RATIFIÉ)
- `03-ONBOARDING/client-onboarding-kit-v1.md` (template canonique)

Les dossiers `01-SDD/`, `03-PRD/`, `04-DDD/` à l'intérieur de `04_Business_Domains/09_Blueprints/` sont **vides** de `.md`. La triade est anticipée par la structure, mais les B2/B3/B4 formels n'ont pas encore été publiés — signe que le canon est posé en attente d'activation.

## Anti-patterns

- **SDD qui ressemble à un PRD** (le « quel système » glisse vers « comment »).
- **ADR qui ressemble à un DDD** (la « décision » devient un « script »).
- **DDD qui décide une direction** (le « job à faire » devient un « changement de cap »).

## Conséquence opérationnelle

Un blueprint qui n'identifie pas sa couche (B1, B2 ou B3) **n'est pas un blueprint canon** — c'est un brouillon. Sa ratification est bloquée tant que la couche n'est pas nommée explicitement.
