---
source: A0_MEMORY_CORE
date: 2026-05-17
type: shadow-l0-index
status: ACTIVE
domain: Shadow_L0 / Codex / Claude / Gemini
tags: [#ShadowL0, #Codex, #ClaudeCode, #GeminiCLI, #LLM_Wiki, #Symphony]
---

# Shadow L0

Shadow L0 est la couche locale de coordination des executants IA:

- Codex CLI pour implementation locale et verification.
- Gemini CLI pour lecture large, exploration et synthese.
- Claude Code CLI pour execution Claude-style, notamment via MiniMax quand Anthropic est limite.

Ce dossier complete le routeur racine:

`C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\README.md`

## Source De Verite

| Fichier | Role |
|---------|------|
| `README.md` | Index Shadow L0 |
| `01_shadow-l0-coordination-20260517.md` | Doctrine de coordination Codex / Claude / Gemini |
| `agents/Codex_CLI/` | Capsule Codex locale |
| `agents/Claude_Code_CLI/` | Capsule Claude Code locale |
| `agents/Gemini_CLI/` | Capsule Gemini locale |

## Regle De Coordination

1. Lire le README racine du Memory Core.
2. Lire `LLM_Wiki/wiki/index.md`.
3. Lire `LLM_Wiki/wiki/log.md`.
4. Choisir l'executant Shadow L0 selon la mission.
5. Ecrire la memoire durable dans `LLM_Wiki/`, pas dans `Hermes Agent/`.

## Routage Rapide

| Mission | Executant primaire | Executant secondaire |
|---------|--------------------|----------------------|
| Modifier fichiers locaux | Codex CLI | Claude Code CLI |
| Explorer beaucoup de docs | Gemini CLI | Codex CLI |
| Produire un plan critique | Claude Code CLI | Gemini CLI |
| Verifier une configuration locale | Codex CLI | Claude Code CLI |
| Creer une synthese memoire | Gemini CLI | Codex CLI |

## Securite

- Ne jamais stocker de cle API dans ce dossier.
- Ne jamais ecrire de secret dans une capsule agent.
- Les fichiers doivent citer uniquement les noms de variables `.env`.
- Les modes bypass/yolo sont reserves aux workspaces jetables, sans secrets.

## Statut

Shadow L0 remplace le besoin Hermes pour la coordination locale.

Hermes reste archive. LLM Wiki devient memoire vivante.
