---
type: Concept
title: Cinq patterns transversaux qui apparaissent dans plusieurs kits templates
description: Cinq patterns émergent indépendamment dans au moins 3 kits différents — agents-as-folder, kill switches, audit log append-only, three-layer memory, exfiltration guard. Preuve que ces patterns sont universels, pas idiosyncratiques à un kit.
tags: [patterns, cross-cutting, agents-as-folder, kill-switches, audit-log, three-layer-memory, exfiltration-guard, universality]
generated: { by: minimax-m3, at: 2026-08-19T20:15:00Z }
verified:
  - { by: process:cross_reference_5_patterns_4_kits, at: 2026-08-19T20:15:00Z }
sources:
  - id: claudeclaw-v3-blueprint
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/ClaudeClaw Mission Control Kit/CLAUDECLAW_V3_BLUEPRINT.md"
    title: "ClaudeClaw V3 — patterns canoniques (bridge / wrapper / brain + 4 ingrédients)"
    last_modified: 2026-05
  - id: enterprise-blueprint
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/BLUEPRINT.md"
    title: "Enterprise OS — 42 kill switches + write-once audit S3 Object Lock"
    last_modified: 2026-05
  - id: silver-platter-skill
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/The Perfect Agentic OS Kit/skill_assets/SKILL.md"
    title: "Silver-platter — agents-as-folder pattern"
    last_modified: 2026-05
  - id: full-agentic-21-patterns
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/FULL Agentic Patterns Kit/agentic-design-patterns-docs-main/agentic-design-patterns-docs-main/pattern-discussion"
    title: "FULL Agentic Patterns — 21 patterns canoniques"
    last_modified: 2026-05
  - id: memory-architect-skill
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Memory Architect Kit/SKILL.md"
    title: "Memory Architect — 7 couches + multi-signal retrieval"
    last_modified: 2026-05
okf_version: "0.2"
---

# Cinq patterns transversaux — la signature universelle des kits

## Énoncé

Cinq patterns émergent **indépendamment** dans au moins 3 kits différents. Cette convergence est la preuve qu'ils sont **universels** — pas idiosyncratiques à un seul auteur. Un distillateur qui les néglige perdrait l'information la plus réutilisable de cette vague.

## Les cinq patterns

### 1. **Agents-as-folder**

| Kit | Forme |
|---|---|
| ClaudeClaw Mission Control V3 | `agents/<id>/agent.yaml` + `agents/<id>/CLAUDE.md` |
| ClaudeClaw OS Blueprint V2 | identique (le V2 a été conservé par le V3) |
| The Perfect Agentic OS / silver-platter | sub-agent = « specialist staffer Claude routes questions to » |
| FULL Agentic Patterns | Multi-Agent Collaboration (verbatim dans `pattern-discussion/multi-agent-collaboration.md`) |

**Forme canonique** : un agent = un dossier avec deux fichiers (`agent.yaml` pour la config, `CLAUDE.md` pour la personnalité). Citation ClaudeClaw V3 : « An agent is just a folder with two files. »

### 2. **Kill switches (env var hot-reload)**

| Kit | Forme | Nombre |
|---|---|---|
| ClaudeClaw Mission Control V3 | 6 env vars, singleton hot-reload via `.env` mtime | 6 |
| ClaudeClaw OS Blueprint V2 | 6 env vars, vérifiés au boundary | 6 |
| Enterprise_OS_Blueprint | 42 switches Bedrock/Orchestrator/etc. | 42 |
| ClaudeClaw V2 | `EMERGENCY_KILL_PHRASE` string match (case-insensitive exact) | 1 (la totale) |

**Forme canonique** : un booléen par comportement dangereux, lisible à chaque boundary qui traverse ce comportement. Si l'env var ne peut être lue, le système refuse. **Fail-closed**.

### 3. **Audit log append-only**

| Kit | Forme |
|---|---|
| ClaudeClaw Mission Control V3 | SQLite `audit_log` table, 90-day retention, periodic prune |
| ClaudeClaw OS Blueprint V2 | SQLite `audit_log` table, typed action categories (message, command, delegation, unlock, lock, kill, blocked) |
| Enterprise_OS_Blueprint | DynamoDB chaud + S3 Object Lock (governance mode, 7-year hold) froid |
| Fable Mindset | n/a explicite, mais `analyze_discipline.py` logge les actions |

**Forme canonique** : append-only, indexé par `ts`, retention bornée, **chaque action qui change l'état écrit une ligne**. Enterprise va plus loin (write-once S3 Object Lock) — pattern « dual-write » : copie chaude requêtable + copie froide inaltérable.

### 4. **Three-layer memory (FTS5 + embeddings + salience)**

| Kit | Forme |
|---|---|
| ClaudeClaw Mission Control V3 (Pack 06) | FTS5 + Gemini embeddings + salience + decay + pinning |
| ClaudeClaw OS Blueprint V2 (Memory v2) | gemini-3-flash-preview extraction + 768-dim embeddings + importance + salience + supersession + relevance feedback |
| Memory Architect Kit (Tier 3) | semantic search + keyword + entity linking (multi-signal rank fusion) |
| FULL Agentic Patterns (Memory Management) | pattern canonique |

**Forme canonique** : trois couches (keyword search + vector similarity + importance/salience scoring), combinées via rank fusion. Citation Memory Architect Kit : « ~7,000 tokens vs 25,000 for brute force. Same accuracy. »

### 5. **Exfiltration guard (regex scan avant transmission)**

| Kit | Forme | Patterns |
|---|---|---|
| ClaudeClaw V3 (Pack 07) | scan avant Telegram/Slack/Discord/email/file write | 15+ regex |
| ClaudeClaw V2 (Pack 5) | scan avant outbound, base64 + URL-encoded variants | 15+ |
| Enterprise_OS_Blueprint | DLP 9 patterns : 7 block + 2 warn | 9 |

**Forme canonique** : avant chaque sortie (Telegram, Slack, email, file write, log), scan pour API keys / private keys / tokens / credit cards / SSNs. Si match, block + audit. Le pattern « base64-encoded et URL-encoded variants » est universel.

## Pourquoi cette transversalité compte

Si un seul kit avait proposé un de ces patterns, on pourrait douter de sa valeur. **Le fait que 3+ kits les proposent indépendamment** est un signal de **maturité du domaine** : ces patterns sont l'état de l'art pour un agent OS en 2026, et tout distillateur qui construit un nouveau système doit les adopter.

## Trace dans A'Space V3

| Pattern | Adopté en V3 ? |
|---|---|
| Agents-as-folder | **partiellement** — V3 utilise `00_Amadeus/01_Identity_Core/agents/` mais avec une structure différente (fichiers `L1_A0_*.md` plats, pas `agent.yaml + CLAUDE.md`). |
| Kill switches | **partiellement** — D4 (append-only), D6 (no-self-contradiction), D7 (stale-mandate) sont des doctrines verrouillées, mais pas des env vars hot-reload à la ClaudeClaw. |
| Audit log | **non-adopté** — pas de table `audit_log` SQLite. Les `RAPPORT_*.md` sont des artefacts narratifs, pas structurés. |
| Three-layer memory | **adopté en V3** — `40_Memory_Wiki_OKF/` est un index OKF v0.2 sur disque + mémoire de session. Pas de FTS5/embeddings. Tier 1-2 du modèle, pas Tier 3. |
| Exfiltration guard | **non-adopté** — pas de scan regex sur les outputs. Risque ouvert. |

## Concepts liés

- [[concept-claudeclaw-mission-control-kit]] — le kit qui implémente les 5 patterns le plus complètement
- [[concept-enterprise-os-blueprint-kit]] — la variante AWS-cloud des 5 patterns
- [[concept-memory-architect-7-layers]] — l'archétype du pattern 4
