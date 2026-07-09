---
source: LLM_Wiki_A0
date: 2026-05-11
type: concept
domain: Tech_OS / L0_Kernel / SDD_Canon
tags: [#concept #SDD #System_Design #Architecture_Documents #Blueprint #Aspace_Core]
---

# Concept: SDD (System Design Documents)

> SDD = Le design system de A'Space OS. Chaque SDD est une spécification technique archivée en Markdown, versionnée via TARDIS Protocol.

Les **SDD** sont les documents de conception architecturale pour L0 Tech OS. Ils constituent la **couche design** entre la décision (ADR) et l'exécution (Blueprint code).

---

## Position dans la hiérarchie documentaire

```
AGENTS.md         (canon — qui sont les agents)
    ↓
ADR              (décision — qu'est-ce qui a été décidé)
    ↓
SDD              (design — comment c'est conçu)
    ↓
Blueprint        (exécution — code/spreadsheets)
```

**Règle absolue:** Pas de code sans spec. Pas de spec sans ADR. Pas d'ADR sans ancrage dans AGENTS.md.

---

## Les 10 SDDs actuels (VPS canon)

| SDD | Titre | Guardian | Status |
|-----|-------|---------|--------|
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

---

## Format SDD

Chaque SDD contient:

```markdown
# SDD-XXX — Titre

## Historique (version, date, auteur, ADRs liés)
## Contexte (pourquoi cette décision)
## Décision (ce qui a été conçu)
## Conséquences (impact sur L0/L1/L2)
## Implémentation (liens vers blueprints)
## Checkpoints (TARDIS Protocol entries)
```

---

## SDD vs ADR vs PRD vs SDD

| Document | Type | Granularité | Guardian | Immuable? |
|----------|------|------------|---------|-----------|
| **ADR** | Décision | Haute (système) | Rick | Oui (nouveaux ADRs) |
| **SDD** | Design | Moyenne (module) | Rick + A2 | Oui (TARDIS) |
| **PRD** | Requirement | Moyenne (feature) | A2 Manager | Oui (versioning) |
| **PRD** | Requirement | Fine (ticket) | A3 Nano Squad | Non (1-day tasks) |

---

## SDD Canon Location

```
VPS: /srv/aspace/10_FORGE/12_Blueprints/01-SDD/
Local: A'Space_OS_V2/10_Tech_OS/12_Blueprints/01-SDD/
LLM Wiki raw: LLM_Wiki/raw/sdd/
```

Les SDDs sont copiés du VPS vers local via SCP (2026-05-11) puis ingérés dans le LLM Wiki.

---

## Inbounds

- [[sources/source_sdd-blueprints]] — Ingest de tous les SDDs (source)
- [[concept_adr]] — ADRs governs le process SDD (134 refs dans les SDDs)
- [[entity_rick]] — Rick est le guardian canonical des SDDs

---

*Last updated: 2026-05-11*
*Source: [[sources/source_sdd-blueprints]]*