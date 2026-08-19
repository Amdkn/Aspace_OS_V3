---
type: Concept
title: FULL Agentic Patterns Kit — 21 patterns agentic universels (clone upstream)
description: Kit de 66 fichiers = un clone du dépôt langchain-ai/agentic-design-patterns-docs qui documente 21 patterns agentic standards en 3 formats (mermaid + ascii + discussion). Référencé par CLAUDE.md comme « n'est PAS la mémoire ».
tags: [templates, agentic-patterns, langchain, upstream-clone, mermaid, ascii, 21-patterns]
generated: { by: minimax-m3, at: 2026-08-19T20:10:00Z }
verified:
  - { by: process:lecture_full_agentic_et_verification_clone_amont, at: 2026-08-19T20:10:00Z }
sources:
  - id: full-agentic-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/FULL Agentic Patterns Kit/agentic-design-patterns-docs-main/agentic-design-patterns-docs-main/README.md"
    title: "Agentic Design Patterns Documentation — README upstream"
    last_modified: 2026-05
  - id: full-agentic-pattern-multi-agent-discussion
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/FULL Agentic Patterns Kit/agentic-design-patterns-docs-main/agentic-design-patterns-docs-main/pattern-discussion/multi-agent-collaboration.md"
    title: "Pattern discussion — Multi-Agent Collaboration (verbatim)"
    last_modified: 2026-05
  - id: full-agentic-clone-warning-canon
    resource: "C:/Users/amado/CLAUDE.md"
    title: "CLAUDE.md utilisateur — « n'est PAS la mémoire, c'est un clone du dépôt amont langchain-ai/openwiki »"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# FULL Agentic Patterns Kit — clone upstream + 21 patterns universels

## Périmètre

66 fichiers : 1 `.gitignore` + 1 README + **21 patterns × 3 formats** (mermaid + ascii + discussion) + un README principal.

| Format | Count | Fichiers par pattern |
|---|---|---|
| **mermaid-diagrams/** | 21 | `<pattern>.mmd` |
| **ascii-art/** | 21 | `<pattern>.txt` |
| **pattern-discussion/** | 21 | `<pattern>.md` (~75-150 lignes chacun) |

Les 21 patterns sont décrits dans `README.md` :

**Core Patterns** (5) : Prompt Chaining, Routing, Parallelization, Reflection, Tool Use.
**Advanced Patterns** (5) : Planning, Multi-Agent Collaboration, Memory Management, Learning and Adaptation, Model Context Protocol.
**System Patterns** (5) : Goal Setting and Monitoring, Exception Handling and Recovery, Human-in-the-Loop, Knowledge Retrieval (RAG), Inter-Agent Communication.
**Optimization Patterns** (4) : Resource-Aware Optimization, Reasoning Techniques, Guardrails/Safety Patterns, Evaluation and Monitoring.
**Strategic Patterns** (2) : Prioritization, Exploration and Discovery.

Total : 5 + 5 + 5 + 4 + 2 = 21 patterns.

## Verdict global

**`synthese-datee`** — clone upstream daté par nature, mais 21 patterns eux-mêmes canoniques.

## Pourquoi `synthese-datee` plutôt que `orphelin`

Le CLAUDE.md utilisateur (`C:\Users\amado\CLAUDE.md`) note explicitement :

> **`ASpace_OS_V3\openwiki\` n'est PAS la mémoire** (correction du 2026-08-17).
> C'est un clone du dépôt amont `langchain-ai/openwiki` — l'outil qui *génère*
> des wikis. Il a son propre `.git`, il est invisible depuis le statut du dépôt
> parent, et son unique remote ne nous appartient pas.

Cette note vise `openwiki/`, pas explicitement `FULL Agentic Patterns Kit`. Mais le **mécanisme est le même** : un clone GitHub upstream n'est pas une ressource A'Space, c'est un snapshot à un instant t.

Cependant, **contrairement à openwiki/**, ce clone **est dans `02_Templates/`** et **est utilisé comme référentiel de design**. Le contenu (les 21 patterns) est canonique et universellement applicable. Donc :
- Le **contenant** (le clone GitHub) est orphelin/daté.
- Le **contenu** (les 21 patterns) est canonique.

Verdict **`synthese-datee`** — daté sur la fraîcheur du snapshot, canon sur les patterns.

## Les patterns les plus applicables à A'Space V3

| Pattern | Application V3 |
|---|---|
| **Routing** | A0 dispatcher → capitaines par domaine (L1/L2/L3) |
| **Parallelization** | sub-agents en parallèle (fan-out dans `agentgateway`) |
| **Reflection** | post-task review (`RAPPORT_*.md` après chaque passe) |
| **Tool Use** | MCP tools + Bash + Read/Write (canonique) |
| **Planning** | BRIEF canonique avant toute exécution |
| **Memory Management** | `40_Memory_Wiki_OKF/` (OKF v0.2) |
| **Model Context Protocol** | MCP servers (`agentgateway` expose 16) |
| **Goal Setting and Monitoring** | D4-D8 doctrines + success_signal canon |
| **Exception Handling and Recovery** | kill switches + D7 stale-mandate (cf. vague B1) |
| **Human-in-the-Loop** | D7 silent mode + A0 HITL gates |
| **Knowledge Retrieval (RAG)** | non-utilisé en V3 (pas de RAG actuel) |
| **Inter-Agent Communication** | non-standardisé en V3 (Hive Mind serait le candidat) |
| **Resource-Aware Optimization** | Quota Anthropic, hiérarchie de délégation (cf. CLAUDE.md §1) |
| **Reasoning Techniques** | thinking blocks, effortLevel xhigh (Ultracode) |
| **Guardrails/Safety Patterns** | 42 kill switches Enterprise / 6 kill switches ClaudeClaw |
| **Evaluation and Monitoring** | `_loop/RAPPORT_b*.md` (vague B1) |
| **Prioritization** | 8-domain Business OS routing |
| **Exploration and Discovery** | R&D squad (Cyborg + Beast) |

→ A'Space V3 utilise **~14 des 21 patterns** d'une manière ou d'une autre, sans l'avoir formalisé comme tel.

## Concepts liés

- [[concept-five-cross-cutting-patterns]] — les patterns qui reviennent dans plusieurs kits
- [[concept-kits-utilisation-trace]] — la trace indirecte via les patterns
