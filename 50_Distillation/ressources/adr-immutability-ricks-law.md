---
type: Concept
title: ADR — Architecture Decision Records (Rick's Law)
description: Le canon juridique de Rick. Une décision architecturale immuable : créée une fois, jamais réécrite. Toute évolution → un nouvel ADR. Différent des SDD (design) et PRDs (requirement).
tags: [adr, rick, immutability, decision-record, governance, l0]
generated: { by: minimax-m3, at: 2026-08-17T20:45:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T20:45:00Z }
sources:
  - id: concept-adr
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_adr.md"
    title: "Concept: ADR (Architecture Decision Records)"
    last_modified: 2026-05-10
  - id: concept-sdd
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_sdd.md"
    title: "Concept: SDD (System Design Documents)"
    last_modified: 2026-05-11
  - id: adr-fs-001-entity
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/entities/entity_adr_fs_001.md"
    title: "ADR-FS-001 — Junction-Based Aliasing"
    last_modified: 2026-05-22
  - id: adr-fwk-021-entity
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/entities/entity_adr_fwk_021.md"
    title: "ADR-FWK-021 — Canon Tripartite des Blueprints"
    last_modified: 2026-05-22
okf_version: "0.2"
---

# ADR — Architecture Decision Records (Rick's Law)

> Le canon juridique de Rick. Créé une fois, jamais réécrit.

Un ADR est l'enregistrement d'une **décision architecturale** — le *pourquoi*, pas le *quoi*.
Les ADRs sont le mécanisme par lequel Rick governance le Tech OS.

## 1. Format Standard

```markdown
# ADR-XXX: Titre de la Décision

## Status
Accepted | Deprecated | Superseded

## Context
Contexte de la décision (problème, contraintes)

## Decision
Ce qui a été décidé

## Consequences
- ✅ Positif: ...
- ❌ Négatif: ...
```

## 2. Règles absolues (Rick's Law)

1. **Immuabilité** : un ADR créé n'est jamais réécrit.
2. **Nouveaux ADRs** : une nouvelle décision → un nouvel ADR (jamais de rewrite).
3. **Canon first** : toute anomalie → nouvelle ADR, pas modification.
4. **Ancrage** : tout ADR doit être ancrée dans `AGENTS.md`.

## 3. Namespaces

Les ADRs sont rangés par namespace :

- **ADR** (générique) : Rick Law (ADR-001..007 historiques)
- **FS** (filesystem) : `ADR-FS-001` Junction-Based Aliasing
- **FWK** (framework) : `ADR-FWK-021` Canon Tripartite des Blueprints
- **HEART-**, **INFRA-**, **NOTION-**, **SYMPH-**, **CANON-**, **META-** : namespaces thématiques

Convention immuable : `<TYPE>-<NAMESPACE>-<NNN>_<kebab-case>.md`.

## 4. ADR Actifs Connus (extrait historique pré-Constitution)

| ID | Sujet | Règle clé |
|---|---|---|
| **ADR-001** | OpenClaw Position | `03_OpenClaw_Body` = config only, jamais clone |
| **ADR-002** | Portabilité Multiverse | `ASPACE_ROOT` env var — pas de chemins hardcodés |
| **ADR-003** | agents_registry.json | Mapping Canon ↔ Runtime ↔ Config |
| **ADR-006** | Windows Watchdog | Native PS persistence over Docker |
| **ADR-007** | **Paradigm Shift V2** | Trust Zone `C:\Users\amado` — **ADR fondateur** |
| **ADR-FS-001** | Junction-Based Aliasing | PARA/Enterprise = SSOT, exposition via junctions NTFS, jamais copies |
| **ADR-FWK-021** | Canon Tripartite des Blueprints | 3 canons isomorphes L0/L1/L2 (12_Blueprints) |
| **ADR-CANON-001** | Roster source-of-truth | Notion AGENT_REGISTRY_DB prime ; AGENTS.md = index |

## 5. ADR vs SDD vs PRD

| Document | Type | Granularité | Guardian | Immuable ? |
|---|---|---|---|---|
| **ADR** | Décision | Haute (système) | Rick | Oui (nouveaux ADRs) |
| **SDD** | Design | Moyenne (module) | Rick + A2 | Oui (TARDIS) |
| **PRD** | Requirement | Fine (ticket) | A3 Nano Squad | Non (1-day tasks) |

## 6. Constitution A'SPACE — Article 5 et statut des ADRs

**Article 5** : tous les ADRs antérieurs sont rétrogradés en **mémoire consultative**.
Leur contenu reste (D4 sur le contenu) ; leur statut de loi est aboli.
Toute règle non re-déclarée par A+ à chaque cycle 12WY expire.

**Conséquence pratique** : un ADR pré-2026-07-12 reste un bon réflexe (D1-D8 = habitudes
professionnelles) mais **ne bloque plus** une action. Bloquer devient anticonstitutionnel
(Article 6).

## Liens entrants

- `constitution-aspace-v1.md` — Article 5 rétrograde les ADRs en jurisprudence
- `sovereignty-3-niveaux.md` — niveau 2 (code) = ADRs immuables
- `ntfs-junction-aliasing.md` — la matérialisation filesystem (ADR-FS-001)
