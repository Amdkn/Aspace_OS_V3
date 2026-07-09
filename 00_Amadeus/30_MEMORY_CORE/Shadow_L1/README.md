---
source: A0_MEMORY_CORE
date: 2026-05-17
type: shadow-l1-index
status: ACTIVE
domain: Shadow_L1 / Baserow / Plane / Symphony
tags: [#ShadowL1, #Baserow, #Plane, #Symphony, #GeminiCLI, #ClaudeCode]
---

# Shadow L1

Shadow L1 est la couche de handoff pour les outils operationnels Life OS / Business Ops:

- Baserow comme source structurée lisible.
- Plane comme cible de work-items.
- Symphony comme routeur conceptuel entre source, decomposition et execution.

Ce dossier est fait pour que Gemini CLI et Claude Code CLI puissent reprendre la configuration Baserow/Plane sans lire l'archive Hermes comme source active.

## Source De Verite

| Fichier | Role |
|---------|------|
| `README.md` | Index Shadow L1 |
| `HEARTBEAT_PROTOCOL.md` | **Doctrine pulse L1 (Symphony adapted)** — héritage de Shadow_L0 |
| `SPEC.md` | Spec mesh Shadow L1, acceptance criteria |
| `WORKFLOW.md` | Mission lifecycle L1 |
| `HEARTBEAT.md` | `tasks:` block lu par `heartbeat-tick-l1.ps1` |
| `agents/Claude_Code_CLI/Heartbeat.md` | Capsule orchestrateur (MiniMax backbone, 30 min cadence) |
| `agents/Claude_Code_CLI/Agent.md` | Identité 11th Doctor Life OS |
| `agents/Claude_Code_CLI/Tools.md` | Surface capability L1 |
| `A0_inbox/` | Anomaly digests (read by A0 daily) |
| `01_baserow-plane-handoff-20260517.md` | Etat canonique Baserow / Plane et variables attendues |
| `02_life-os-baserow-schema-20260517.md` | Schema Life OS / ZORA a appliquer dans Baserow |
| `03_life-os-baserow-database-analysis-20260517.md` | Analyse actuelle de la base Life OS Baserow |
| `04_life-os-baserow-12wy-architecture-analysis-20260517.md` | Analyse V2 de l'architecture 12WY complete |
| `05_life-os-baserow-population-test-20260518.md` | Rapport du test de peuplement LD01-LD04 |
| `handoffs/Gemini_CLI.md` | Instructions de reprise Gemini |
| `handoffs/Claude_Code_CLI.md` | Instructions de reprise Claude |

## Principe

Shadow L1 ne stocke pas de secrets.

Il documente seulement:

- les noms de variables;
- les chemins de configuration;
- les IDs techniques deja prouves;
- les erreurs connues;
- les prochaines actions.

## Etat Court

| Service | Etat | Note |
|---------|------|------|
| Baserow | Lisible | Solaris W1 a ete lu depuis table `955428`, row `133` |
| Baserow Life OS | Bloque schema | `LD 00 Life Wheel Zora` lisible, creation de champs refusee par token |
| Baserow Life OS Analyse | Lisible | `LD 00 Life Wheel Zora` + `12WY Warp Core` analyses via API |
| Baserow 12WY V2 | Lisible | Vision, Rocks, Warp Core, Scorecard, Time Use analyses via API |
| Baserow Population Test | Peuple | LD01-LD04, 12 Rocks, 17 tactiques W1-W4 |
| Plane | Bloque auth | HTTP 403 lors du test API, aucun work-item cree |
| Hermes | Archive | Ancien smoke test conserve comme preuve historique, pas comme zone active |

## A Lire Avant Action

1. `30_MEMORY_CORE/README.md`
2. `Shadow_L1/01_baserow-plane-handoff-20260517.md`
3. Handoff agent cible dans `Shadow_L1/handoffs/`
4. `LLM_Wiki/wiki/log.md`
