---
type: Concept
title: SDD — System Design Documents (couche design)
description: La couche design entre la décision (ADR) et l'exécution (Blueprint code). 10 SDDs canon pour L0 Tech OS, versionnés via TARDIS Protocol. Pas de code sans spec ; pas de spec sans ADR ; pas d'ADR sans ancrage AGENTS.md.
tags: [sdd, system-design, architecture, blueprint, l0, tardis]
generated: { by: minimax-m3, at: 2026-08-17T20:48:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T20:48:00Z }
sources:
  - id: concept-sdd
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_sdd.md"
    title: "Concept: SDD (System Design Documents)"
    last_modified: 2026-05-11
  - id: concept-adr
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_adr.md"
    title: "Concept: ADR (Architecture Decision Records)"
    last_modified: 2026-05-10
  - id: synthesis-fin-gestation
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/syntheses/synthesis_fin-gestation-strategique.md"
    title: "Synthesis: La Fin de la Gestation Stratégique (2026-05-08)"
    last_modified: 2026-05-10
okf_version: "0.2"
---

# SDD — System Design Documents (couche design)

> SDD = le design system de A'Space OS. Chaque SDD est une spécification technique archivée
> en Markdown, versionnée via TARDIS Protocol.

## 1. Hiérarchie documentaire

```
AGENTS.md         (canon — qui sont les agents)
    ↓
ADR              (décision — qu'est-ce qui a été décidé)
    ↓
SDD              (design — comment c'est conçu)
    ↓
Blueprint        (exécution — code/spreadsheets)
```

**Règle absolue** : pas de code sans spec ; pas de spec sans ADR ; pas d'ADR sans ancrage dans AGENTS.md.

## 2. Les 10 SDDs canoniques (état mai 2026)

| SDD | Titre | Guardian | Status |
|---|---|---|---|
| SDD-000 | Constitution du Rick's Verse | Rick | ✅ Canon |
| SDD-000b | Agent Bootstrap | Rick | ✅ Canon |
| SDD-000c | A'Space Core (Jumeau Numérique) | Rick | ✅ Canon |
| SDD-001 | Solarpunk Kernel Core L0.3 | Rick | ✅ Canon |
| SDD-002 | A1 Rick Harness | Rick | ✅ Canon |
| SDD-003 | TARDIS Protocol (A2/A3 Onboarding) | Rick | ✅ Canon |
| SDD-004 | Rick's Verse Governance | Rick | ✅ Canon |
| SDD-005 | Life OS L1 Integration | Beth/Morty | ✅ Canon |
| SDD-006 | Business Pulse L2 | Jerry/Summer | ✅ Canon |
| SDD-007 | SOB Factory ICP Variants | Rick | ✅ Canon |

## 3. Format SDD

```markdown
# SDD-XXX — Titre

## Historique (version, date, auteur, ADRs liés)
## Contexte (pourquoi cette décision)
## Décision (ce qui a été conçu)
## Conséquences (impact sur L0/L1/L2)
## Implémentation (liens vers blueprints)
## Checkpoints (TARDIS Protocol entries)
```

## 4. SDD vs ADR vs PRD

| Document | Type | Granularité | Guardian | Immuable ? |
|---|---|---|---|---|
| **ADR** | Décision | Haute (système) | Rick | Oui (nouveaux ADRs) |
| **SDD** | Design | Moyenne (module) | Rick + A2 | Oui (TARDIS) |
| **PRD** | Requirement | Fine (ticket) | A3 Nano Squad | Non (1-day tasks) |

## 5. SDD canon location

```
VPS:    /srv/aspace/10_FORGE/12_Blueprints/01-SDD/
Local:  10_Tech_OS/12_Blueprints/01-SDD/
Wiki raw: LLM_Wiki/raw/sdd/
```

Les SDDs sont copiés du VPS vers local via SCP, puis ingérés dans le LLM Wiki.

## 6. Statut Constitution v1.0

L'article 5 de la Constitution A'SPACE (2026-07-12) rétrograde les ADRs et SDDs en
**jurisprudence consultative**. Les SDDs restent de bons réflexes d'ingénierie
(documentation avant code), mais cessent d'être bloquants. La règle hiérarchique
« pas de code sans spec » survit comme **habitude**, plus comme **loi**.

## Liens entrants

- `adr-immutability-ricks-law.md` — l'amont (décision)
- `constitution-aspace-v1.md` — Article 5 rétrograde SDDs en jurisprudence
- `compounding-knowledge-wiki.md` — les SDDs alimentent le wiki (sources canon)
