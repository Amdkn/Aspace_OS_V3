---
type: Concept
title: Famille L2 Business OS — 80 ADR structurés, batchs de ratification 2026-07-15
description: La famille L2 Business OS (80 ADR sous _SPECS/ADR/L2_Business_OS/) est la plus formelle. La majorité a été ratifiée en batch les 2026-07-15 et 2026-07-16.
tags: [adr, l2, business-os, batch-ratification]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-CANON-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-CANON-001_roster-source-of-truth.md"
    title: L2 Roster Source of Truth (8 B2 × 53 B3)
    last_modified: "2026-07-15"
  - id: ADR-L2-TRIPTYQUE-V4-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-TRIPTYQUE-V4-001_business-triptyques-v4-enterprise-os_RATIFIED_2026-07-15.md"
    title: L2 Triptyques V4 Enterprise OS (batch sibling 2/7)
    last_modified: "2026-07-15"
  - id: ADR-L2-MULTIVERSE-CD-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-MULTIVERSE-CD-001_multiverse-cd-verse_RATIFIED_2026-07-15.md"
    title: L2 Multiverse CD-Verse (batch sibling 6/7)
    last_modified: "2026-07-15"
  - id: ADR-L2-PAPERCLIPAI-004
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-004_paperclip-calibration-doctrine_RATIFIED_2026-07-16.md"
    title: L2 Paperclip Calibration (batch 2026-07-16)
    last_modified: "2026-07-16"
okf_version: "0.2"
---

# Famille L2 Business OS — 80 ADR structurés, batchs de ratification 2026-07-15

## Résumé

La famille **L2 Business OS** est la **plus nombreuse et la plus formelle**. 80 ADR vivent dans `_SPECS/ADR/L2_Business_OS/`. La majorité a été ratifiée en **batch** lors des sessions « SUPER-MAN DE JERRY » des 2026-07-15 (7 sibling ADR) et « anti-sabotage » du 2026-07-16 (PaperclipAI-001 à 004).

## Le format L2

Le frontmatter L2 est le plus riche observé :

```yaml
---
id: ADR-L2-MULTIVERSE-CD-001
title: "Multiverse CD-Verse Layer ..."
status: RATIFIED
date: 2026-07-15
ratified_by: A0 Amadeus (airlock clos 2026-07-15 — batch verdict Enterprise OS SUPER-MAN DE JERRY session, sibling 6/7)
proposed_by: A2 (Claude Code via /superpowers:brainstorming) on A0 directive session brainstorm
domain: L2 Business OS / Multiverse DC-Verse / 8 B2 heroes / Functional layer
related: [ADR-L2-TRIPTYQUE-V4-001, ADR-CANON-001, ...]
sources_canons: [...]
tags: [...]
provenance: |
  Née 2026-07-15 d'une session brainstorm ...
---
```

Champs remarquables :

- `ratified_by` : nom de l'autorité + contexte de la session (A0 + airlock clos)
- `proposed_by` : A2 (Claude Code) le plus souvent, parfois Codex (A2 antérieur)
- `related: [...]` : liste d'ADR siblings ou antérieurs
- `sources_canons: [...]` : sources ayant nourri la décision
- `provenance: |` : paragraphe markdown narratif sur l'origine de la décision
- `supersedes: ...` : remplace tel ADR (souvent NONE — D4 append-only)
- `extends: ...` / `amends: ...` : chaîne d'amendements

## Le batch 2026-07-15 (7 sibling ADR)

La session « Enterprise OS SUPER-MAN DE JERRY » a ratifié en un seul airlock 7 ADR :

| # | ADR | Sujet |
|---|---|---|
| 1/7 | `ADR-AAAS-PRICING-001-AMEND-003` | Tier 5 Enterprise OS Coach-Deployer ($1500/mo) |
| 2/7 | `ADR-L2-TRIPTYQUE-V4-001` | Triptyques V4 Enterprise OS |
| 3/7 | `JTBD-ICP-NEXUS-001` | JTBD Expert Méthodique |
| 4/7 | `JTBD-Enterprise-OS-Coach-001` | JTBD Coach Premium |
| 5/7 | `JTBD-Enterprise-OS-CEO-001` | JTBD CEO Series B |
| 6/7 | `ADR-L2-MULTIVERSE-CD-001` | Multiverse CD-Verse Functional Layer |
| 7/7 | `ADR-L2-NAMING-CONVENTION-001` | Naming Convention session canon |

Ces 7 ADR partagent le même contexte de ratification : `batch verdict Enterprise OS SUPER-MAN DE JERRY session, sibling N/7`.

## Le batch 2026-07-16 (4 ADR PaperclipAI)

La session « anti-sabotage » du 2026-07-16 a ratifié 4 ADR sur la doctrine paperclip :

- `ADR-L2-PAPERCLIPAI-001_governance-mirror-doctrine.md`
- `ADR-L2-PAPERCLIPAI-002_anti-paperclip-irony-doctrine.md`
- `ADR-L2-PAPERCLIPAI-003_paperclip-delegation-not-creation-doctrine.md`
- `ADR-L2-PAPERCLIPAI-004_paperclip-calibration-doctrine_RATIFIED_2026-07-16.md` (le seul avec `RATIFIED` dans le nom)

L'ADR-004 est un amend des 3 autres (D4 append-only). Il carve-out explicitement les routine tasks de l'anti-paperclip, suite à un incident économique A0 ($50 → $20 downgrade token plan).

## Statut vis-à-vis de V3

**canon** sur 75+ ADR ; **synthese-datee** sur quelques ADR pointus (ex : `ADR-OMK-004` qui a partiellement supersedé `ADR-OMK-001`). Aucun L2 n'est complètement obsolète.

## Le verdict de cette distillation

**canon**. La famille L2 reste la source de vérité sur l'architecture business. Aucun L2 n'est à supprimer ; certains sont à amender (AMEND pattern).

## Liens

- Voir aussi : `concept-amend-pattern.md` (les AMEND)
- Voir aussi : `concept-supersedes-partial.md` (les supersedes partiels)
- Voir aussi : `concept-batches-ratification.md` (les sessions de batch)