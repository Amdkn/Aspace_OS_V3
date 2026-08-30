---
type: Ontology
title: Verbes — Routage — où ça va
description: Les prédicats de la famille « routage » réellement attestés dans les triplets du corpus.
tags: [ontologie, verbes, routage, rdf]
generated: { by: scripts/extraire_verbes.py, at: 2026-08-30 }
verified:
  - { by: scripts/extraire_verbes.py, at: 2026-08-30 }
sources:
  - id: ontologie-v2
    resource: 00_Amadeus/30_MEMORY_CORE/ONTOLOGIE_V2.md
    title: §3 — les quatre familles de verbes
    last_modified: 2026-08-30
  - id: triplets
    resource: 70_Onthologies/**/*.ttl
    title: Les prédicats mesurés (85 distincts)
    last_modified: 2026-08-30
okf_version: "0.2"
---

# Routage — où ça va

**11 prédicats** de cette famille, attestés dans les triplets du corpus.

> **Extrait, jamais inventé.** `ONTOLOGIE_V1` a échoué en proposant
> un verbe `sert` « qui manquait » — il ne manquait pas. Ce fichier
> est régénéré par `scripts/extraire_verbes.py` : un verbe absent
> du corpus n'y entre pas, même s'il serait utile.

| Verbe | Occurrences |
|---|---:|
| `covers` | 74 |
| `routes` | 42 |
| `handledBy` | 40 |
| `cites` | 20 |
| `directs` | 5 |
| `targets` | 4 |
| `orchestrates` | 2 |
| `handlesBy` | 1 |
| `triggers` | 1 |
| `dispatches` | 1 |
| `handles` | 1 |

## Comment vérifier

```bash
python C:/Users/amado/ASpace_OS_V3/scripts/extraire_verbes.py
```
