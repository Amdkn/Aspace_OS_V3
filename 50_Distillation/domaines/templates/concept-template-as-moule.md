---
type: Concept
title: Un template est un moule, pas une doctrine
description: Cette distinction commande la distillation des 9 kits templates de V2 — un kit impose des contraintes à ce qui en sort, il ne dicte pas le contenu.
tags: [templates, kits, distillation, canon, datation, moule, doctrine]
generated: { by: minimax-m3, at: 2026-08-19T19:30:00Z }
verified:
  - { by: process:lecture_9_kits_v2, at: 2026-08-19T19:30:00Z }
sources:
  - id: brief-vague2-templates
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/BRIEF_templates.md"
    title: "Brief vague 2 — distillation Templates (9 kits)"
    last_modified: 2026-08-19
  - id: rapport-normatif-sdd-prd-vague2
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/RAPPORT_normatif-sdd-prd.md"
    title: "Rapport parallèle vague 2 — distillation SDD/PRD"
    last_modified: 2026-08-19
  - id: claudeclaw-v3-blueprint-the-thesis
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/ClaudeClaw Mission Control Kit/CLAUDECLAW_V3_BLUEPRINT.md"
    title: "Hive Mind Blueprint (ClaudeClaw V3)"
    last_modified: 2026-05
okf_version: "0.2"
---

# Un template est un moule, pas une doctrine

## Énoncé

Un **template** (kit) est un dispositif qui **impose une forme** à ce qui en sort.
Une **doctrine** (SDD, ADR, canon) est un dispositif qui **impose un contenu** à ce qui le lit.

Cette distinction commande la distillation V2 → V3 :

- Pour une doctrine (SDD-006, ADR-SOBER-002, ADR-META-001), la question est : « est-elle encore vraie ? »
- Pour un template (Enterprise_OS_Blueprint_Kit, ClaudeClaw Mission Control Kit), la question est : **« a-t-il été utilisé, et que reste-t-il valide de sa forme ? »**

## Pourquoi cette distinction est essentielle

Le brief de la vague 2 Templates l'énonce ainsi :

> Un template n'est pas une doctrine : c'est un **moule**. La question utile
> n'est donc pas « qu'est-ce qu'il dit » mais **« qu'est-ce qu'il impose à ce
> qui en sort »**.

Les 9 kits V2 de `02_Templates/` (ClaudeClaw Mission Control, Enterprise_OS_Blueprint, Fable Mindset, fable-wargame, FULL Agentic Patterns, Memory Architect, The Perfect Agentic OS, ClaudeClaw OS Blueprint V2, Claude Certified Architect Study Guide) sont tous des **moules** : ils contiennent des prompts, des scripts, des structures de fichiers, des diagrammes, des checklists. Aucun n'est une doctrine qu'on cite comme autoritative.

## Conséquences pour la classification

Pour chaque document issu d'un kit, on ne demande pas « est-il canon ? » mais :

1. **De quoi est-il le moule ?** Quel type d'artefact en sort (skill, agent, infra, doctrine, brief) ?
2. **Quelles contraintes impose-t-il ?** Quelles structures, quels champs, quels formats ?
3. **A-t-il été utilisé ?** Si oui, les artefacts du corpus V3 portent-ils la marque du moule ?

Un kit dont aucun artefact du corpus ne porte la marque est un **moule mort** —
c'est une information qu'il faut consigner, pas une faute à corriger.

## Critères de verdict (rappel)

| Verdict | Sens |
|---|---|
| `canon` | fait toujours autorité, rien à signaler |
| `synthese-datee` | dépassé sur un point précis, valable sur le reste — lequel et lequel |
| `superseded` | remplacé en entier, par quoi (jamais sans successeur nommé) |
| `orphelin` | ne se rattache à rien, statut indéterminable |

Le moule d'un kit peut être **canon sur sa forme** (toujours applicable) tout en étant **daté sur ses références** (modèles cités, prix, providers). C'est le verdict `synthese-datee` typique.

## Concepts liés

- [[concept-kits-utilisation-trace]] — quels kits ont laissé des traces, lesquels sont des moules morts
- [[concept-five-cross-cutting-patterns]] — 5 patterns qui reviennent dans plusieurs moules
