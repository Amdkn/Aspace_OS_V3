---
type: Ontology
title: Verbes — Autorité — qui commande
description: Les prédicats de la famille « autorite » réellement attestés dans les triplets du corpus.
tags: [ontologie, verbes, autorite, rdf]
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

# Autorité — qui commande

**7 prédicats** de cette famille, attestés dans les triplets du corpus.

> **Extrait, jamais inventé.** `ONTOLOGIE_V1` a échoué en proposant
> un verbe `sert` « qui manquait » — il ne manquait pas. Ce fichier
> est régénéré par `scripts/extraire_verbes.py` : un verbe absent
> du corpus n'y entre pas, même s'il serait utile.

| Verbe | Occurrences |
|---|---:|
| `governs` | 97 |
| `hasVetoOver` | 35 |
| `stewards` | 34 |
| `escalates` | 24 |
| `vetoes` | 4 |
| `forbids` | 1 |
| `mandates` | 1 |

## Comment vérifier

```bash
python C:/Users/amado/ASpace_OS_V3/scripts/extraire_verbes.py
```
