---
type: Concept
title: Familles à un seul ADR — où la décision n'a pas fait école
description: Plusieurs familles ne comptent qu'un seul ADR : AGKIT-001, A0L-COACH-AMEND-001, A0L-META-001, A11Y-001, AGENT-BENCH-SCHEMA-001, RH-META-GOUVERNANCE-001, RH-META-GOUVERNANCE-001 (3 drafts). Une famille à 1 ADR est un signal, pas une famille.
tags: [adr, familles-mono, signal, decision-isolee]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: AGKIT-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/ADR/ADR-AGKIT-001_Industrial_Fusion.md"
    title: AGKIT 001 Industrial Fusion (mono)
    last_modified: "2026-06-15"
  - id: RH-META-GOUVERNANCE-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-RH-META-GOUVERNANCE-001-canonical-v3_RATIFIED_2026-07-26.md"
    title: RH META Gouvernance 001 canonical v3 RATIFIED
    last_modified: "2026-07-26"
okf_version: "0.2"
---

# Familles à un seul ADR — où la décision n'a pas fait école

## Résumé

Une famille à **un seul ADR** n'est pas une famille, c'est une **occurrence**. Le brief vague 2 signale ces cas : la décision n'a pas fait école.

## Les occurrences repérées

Liste non exhaustive des familles mono-ADR vues dans le corpus :

| Famille | ADR | Statut |
|---|---|---|
| AGKIT | `ADR-AGKIT-001_Industrial_Fusion.md` | RATIFIED (V0) |
| A0L | `ADR-A0-L-META-001_4e-layer-jumeau-grilling.md` + `ADR-A0-L-COACH-AMEND-001_couche-coach-pocock-2026-amelioration-jumeau.md` | RATIFIED (Identity_OS) |
| A11Y | `ADR-A11Y-001_wcag-2-2-aa.md` | RATIFIED (L2) |
| AGENT-BENCH-SCHEMA | `ADR-AGENT-BENCH-SCHEMA-001_agent-bench-sql-canonique_PROPOSED.md` | PROPOSED (DRAFTS) |
| RH-META-GOUVERNANCE | `ADR-RH-META-GOUVERNANCE-001-canonical-v3_RATIFIED_2026-07-26.md` + drafts v2 et v1 | RATIFIED (avec chaîne AMEND) |
| AGENTIC | `ADR-AGENTIC-001_l2-agentic-commerce-nanosquad-coordination.md` | RATIFIED |
| ARCH | `ADR-ARCH-002_dual-kanban-multica-vibekanban_PROPOSED.md` | PROPOSED |
| CANON | `ADR-CANON-001_roster-source-of-truth.md` + `ADR-CANON-002_RHA-Workflow_W20-M5.md` | RATIFIED |
| CONSENSUS | `ADR-CONSENSUS-002_emergency-shutdown-protocol-llm-orchestration.md` | PROPOSED |
| EXTRA-PPR | `ADR-EXTRA-PPR-001_preventive-construction-doctrine.md` | RATIFIED |
| HARNESS | `ADR-HARNESS-001_harness-persona-decoupling.md` + `ADR-HARNESS-REVERSIBILITY-KERNEL-001_harness-staffing-reversibility.md` | RATIFIED |
| HERMES | `ADR-HERMES-001_nous-desktop-native-workspace-remote.md` | RATIFIED (Kernel) |
| MULTIPAGE | `ADR-MULTIPAGE-001_wireframe-sitemap.md` | RATIFIED |
| NET | `ADR-NET-001_Hebergement-Multi-Couche.md` | RATIFIED |

## Le signal d'une décision isolée

Quand une famille n'a qu'un seul ADR, c'est un signal :

1. **La décision n'a pas fait tåche d'huile** : aucun ADR sibling ne la complète, ne l'amende, ne la réfute.
2. **Le domaine n'a pas été réinvesti** : aucune nouvelle décision n'a été nécessaire dans le voisinage.
3. **La ratification est peut-être prématurée** : le RATIFIED a été posé avant que la pratique ne valide la décision.

Aucun de ces signaux n'est nécessairement négatif. Une décision stable peut fort bien n'avoir qu'un ADR. Mais c'est **un indicateur à observer** dans le temps.

## Les exceptions notables

- **`AGKIT`** : Industrial Fusion est un cas où la décision a peut-être été absorbée par un autre ADR (à vérifier).
- **`RH-META-GOUVERNANCE`** : la chaîne v1 → v2 → v3 montre que la famille **évolue**, ce n'est pas une famille mono, c'est une famille en croissance.
- **`CANON`** : 2 ADR (Roster + RHA-Workflow). Ce n'est pas mono.
- **`HARNESS`** : 2 ADR. Pas mono.

## Statut vis-à-vis de V3

**orphelin** pour la plupart. **canon** pour ceux qui sont stables et actifs (A11Y, NET).

## Le verdict de cette distillation

**mixte**. Une famille mono n'est pas un problème, c'est un indicateur de santé du domaine. À observer.

## Liens

- Voir aussi : `concept-amend-pattern.md` (l'évolution des familles)
- Voir aussi : `concept-adr-format.md` (le format)