---
type: Concept
title: Trace d'utilisation des 9 kits — 2 ont laissé une marque vérifiable, 7 sont des moules de référence
description: Sur les 9 kits templates de V2, 2 ont laissé une trace concrète (Fable Wargame via LEDGER OMK-C, ClaudeClaw via héritage de patterns). 5 sont des moules de référence non-deployés, 2 sont des orphelins (PDF certification, clone upstream).
tags: [kits, utilisation, trace, ledger, omk, mold-status]
generated: { by: minimax-m3, at: 2026-08-19T20:20:00Z }
verified:
  - { by: process:inventaire_trace_par_kit, at: 2026-08-19T20:20:00Z }
sources:
  - id: wargame-ledger
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/fable-wargame-kit/fable-last-week/LEDGER.md"
    title: "Fable Wargame — LEDGER (mission OMK-C réelle, 2026-07-15)"
    last_modified: 2026-07-15
  - id: os-audit-skill-canon
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/os-audit-SKILL.md"
    title: "OS Audit — skill canonique A'Space (écrit par l'utilisateur)"
    last_modified: 2026-08
  - id: claude-plugins-guide
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/claude-plugins-guide_2026-07-25.md"
    title: "5 plugins Claude Code — guide A'Space (B1-filtered Green Lantern)"
    last_modified: 2026-07-25
okf_version: "0.2"
---

# Trace d'utilisation des 9 kits templates

## Énoncé

Le brief de la vague 2 pose la question :

> Pour chaque kit : de quoi est-il le moule, quelles contraintes impose-t-il, et **a-t-il été utilisé** ? Un kit dont aucun artefact du corpus ne porte la marque est un moule mort — c'est une information, dis-la.

Cette vague a fait l'inventaire. Sur les 9 kits (+ 2 fichiers racine + 1 PDF orphelin) :

## Tableau de trace

| # | Kit | Trace dans V3 | Verdict |
|---|---|---|---|
| 1 | **Claude Certified Architect Study Guide** (1 PDF) | aucune, jamais cité | `orphelin` |
| 2 | **ClaudeClaw Mission Control Kit** (13 MD + PDF + memory/) | aucune directe, mais **5 patterns** adoptés via héritage conceptuel (cf. [[concept-five-cross-cutting-patterns]]) | `synthese-datee` |
| 3 | **ClaudeClaw OS Blueprint Kit V2** (5 MD + PDF) | aucune — superseded par V3 | `superseded` (par V3) |
| 4 | **Enterprise_OS_Blueprint_Kit** (53 fichiers) | aucune — pas d'AWS dans V3 | `synthese-datee` (moule de référence non-deployé) |
| 5 | **Fable Mindset** (10 fichiers + scripts Python + PDF) | aucune directe, mais le **PostToolUse hook** (prompt 6 de `PROMPTS.md`) est applicable à plusieurs projets V3 | `synthese-datee` |
| 6 | **fable-wargame-kit** (15 fichiers) | **OUI** — `LEDGER.md` documente la mission Runbook C SaaS Auth OMK-C phase C (2026-07-15) | `synthese-datee` |
| 7 | **FULL Agentic Patterns Kit** (66 fichiers = clone upstream) | aucune directe, mais ~14 des 21 patterns sont utilisés en V3 sans formalisation | `synthese-datee` (clone daté, contenu canonique) |
| 8 | **Memory Architect Kit** (SKILL.md + PDF) | aucune directe, mais le **modèle 7 couches** est conceptuellement applicable (A'Space V3 utilise déjà Identity + Critical Context + Long-term Knowledge) | `synthese-datee` |
| 9 | **The Perfect Agentic OS Kit** (31 fichiers) | aucune directe, mais le **format de skill** silver-platter est un archétype | `synthese-datee` |

## Fichiers racine (hors kits)

| Fichier | Trace dans V3 | Verdict |
|---|---|---|
| `os-audit-SKILL.md` | **OUI** — skill canonique, exécuté sur `C:\Users\amado\.claude\skills\os-audit\SKILL.md` (le fichier source de vérité) | `canon` |
| `claude-plugins-guide_2026-07-25.md` | **OUI** — écrit par l'utilisateur (A+), B1-filtered Green Lantern, ratifié pour 5 plugins | `canon` |
| `claude-plugins-summary.pdf` | aucune, source du guide ci-dessus | `orphelin` |
| `os-audit-SKILL.md - Google Docs.pdf` | aucune, copie PDF de `os-audit-SKILL.md` | `orphelin` (doublon) |
| `Second Brain - Principles and Starter Prompts.pdf` | aucune | `orphelin` |
| `The AI Consultant Playbook for 2026.pdf` | aucune | `orphelin` |
| `fable-5-extreme-use-cases-guide.pdf` | aucune | `synthese-datee` (sister de Fable Mindset, daté) |

## Synthèse

- **Sur 9 kits**, 2 ont une trace vérifiable dans V3 :
  - **fable-wargame-kit** : LEDGER OMK-C (mission réelle datée 2026-07-15, hashes sha256, V-checks 8/8).
  - **ClaudeClaw Mission Control Kit** : héritage conceptuel (5 patterns transversaux, aucun déploiement direct).

- **2 fichiers racine** sont des artefacts canoniques d'A'Space (pas des kits tiers) :
  - `os-audit-SKILL.md` : skill A'Space exécutable, mirroré sur le filesystem global.
  - `claude-plugins-guide_2026-07-25.md` : document A'Space ratifié par A+.

- **4 fichiers racine + 1 kit (Claude Certified Architect Study Guide)** sont des orphelins : aucun rattachement au corpus, aucun usage observé.

- **Aucun kit n'est « canon » sans réserve** — tous sont soit datés sur les références, soit superseded, soit orphelins. Le **canon** dans cette vague est partagé entre :
  - Les patterns transversaux ([[concept-five-cross-cutting-patterns]]),
  - Le format de skill silver-platter ([[concept-perfect-agentic-silver-platter]]),
  - Les 8 critères de wargame ([[concept-fable-wargame-kit-8-criteria]]),
  - Les 7 couches de mémoire ([[concept-memory-architect-7-layers]]).

## Concepts liés

- [[concept-template-as-moule]] — le méta-concept qui justifie ce verdict
