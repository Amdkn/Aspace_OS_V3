---
type: Archive
title: OpenClaw Body Legacy — l'avant-M3 (février-mars 2026)
description: Le dossier `03_OpenClaw_Body_Legacy/` archive l'état du corps OpenClaw tel qu'il était entre février et mars 2026, avant l'ère M3 : modèle GPT-5.2-codex + fallbacks Sonnet 4.5 / Opus 4.5 thinking, version 2026.2.1, et un ensemble de 10 fichiers de configuration + AGENTS.md (20 576 octets).
tags: [openclaw, body, legacy, gpt-5.2, codex, sonnet-4-5, opus-4-5, 2026-02, 2026-03]
generated: { by: minimax-m3, at: 2026-08-17T23:25:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-17T23:25:00Z }
sources:
  - id: openclaw-dir
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/03_OpenClaw_Body_Legacy/"
    title: Annuaire legacy — 10 fichiers de config + AGENTS.md
    last_modified: 2026-03-05
  - id: openclaw-json
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/03_OpenClaw_Body_Legacy/openclaw.json"
    title: openclaw.json (model primary, fallbacks, version 2026.2.1)
    last_modified: 2026-03-01
  - id: agents-md
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/03_OpenClaw_Body_Legacy/AGENTS.md"
    title: AGENTS.md (20 576 octets — registre d'agents legacy)
    last_modified: 2026-02-16
  - id: registry-json
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/03_OpenClaw_Body_Legacy/agents_registry.json"
    title: agents_registry.json (26 106 octets)
    last_modified: 2026-02-28
okf_version: "0.2"
---

# OpenClaw Body Legacy — l'avant-M3 (février-mars 2026)

## Périmètre

Le dossier `03_OpenClaw_Body_Legacy/` est un instantané de l'état du
**corps OpenClaw** (la harness agent d'avant Claude Code) tel qu'il
existait entre février et mars 2026. Il contient **10 fichiers de
configuration** + un `AGENTS.md` de 20 576 octets.

Liste exhaustive (mesurée par `ls -la`) :

| Fichier | Taille | Modifié | Nature |
|---|---|---|---|
| `AGENTS.md` | 20 576 | 2026-02-16 | registre d'agents (registre humain) |
| `agents_registry.json` | 26 106 | 2026-02-28 | registre machine (26 Ko) |
| `CLAUDE.md` | 0 | 2026-03-05 | **vide** (signal d'arrêt) |
| `device.json` | 416 | 2026-02-14 | device fingerprint |
| `device-auth.json` | 366 | 2026-02-14 | device auth token (legacy) |
| `openclaw.json` | 3 571 | 2026-03-01 | config principale (modèle + fallbacks) |
| `openclaw.example.json` | 2 497 | 2026-02-15 | template de config |
| `openclaw.json.template` | 557 | 2026-02-28 | autre template (probablement Podman) |
| `openclaw.mjs` | 1 414 | 2026-02-16 | entrypoint Node |
| `openclaw.podman.env` | 889 | 2026-02-16 | env vars Podman (conteneur) |
| `bootstrap.sh` | 1 849 | 2026-02-28 | script de bootstrap |
| `paired.json` | 1 749 | 2026-02-14 | pairings Telegram actifs |
| `telegram-allowFrom.json` | 58 | 2026-02-14 | allowlist Telegram |
| `telegram-pairing.json` | 37 | 2026-02-14 | état de pairing |
| `update-offset-default.json` | 48 | 2026-02-14 | offset Telegram update |
| `pending.json` | 2 | 2026-02-14 | (quasi-vide) |
| `.env.template` | 1 067 | 2026-02-28 | template d'env |
| `AGENTS.md` | 20 576 | 2026-02-16 | (déjà listé) |

## Le `openclaw.json` — verbatim

```json
{
  "meta": {
    "lastTouchedVersion": "2026.2.1",
    "lastTouchedAt": "2026-02-03T16:44:14.666Z"
  },
  "wizard": {
    "lastRunAt": "2026-02-03T16:44:14.635Z",
    "lastRunVersion": "2026.2.1",
    "lastRunCommand": "onboard",
    "lastRunMode": "local"
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "openai-codex/gpt-5.2-codex",
        "fallbacks": [
          "google-antigravity/claude-sonnet-4-5",
          "google-antigravity/claude-opus-4-5-thinking"
        ]
      }
```

**Trois choses à remarquer** :

1. **Modèle primaire = `openai-codex/gpt-5.2-codex`** — c'est-à-dire
   **GPT-5.2 Codex** comme moteur par défaut, pas un modèle Claude.
2. **Fallbacks** : Sonnet 4.5 puis Opus 4.5 thinking — les modèles
   Claude récents (4.5, post Opus 4.5) sont en repli, pas en première
   ligne.
3. **Version `2026.2.1`** — un cycle de release early-2026.

## Pourquoi cette archive existe

L'**OpenClaw Body** est la harness qui précédait l'arrivée de M3 comme
runtime principal. Le dossier archive :

- Les **identités de device** (`device.json`, `device-auth.json`) —
  fingerprint d'un matériel précis.
- Les **pairings Telegram** (`paired.json`, `telegram-allowFrom.json`,
  `telegram-pairing.json`) — qui était autorisé à parler au bot à
  l'époque.
- L'**état du registre d'agents** (`AGENTS.md`, `agents_registry.json`)
  — la nomenclature d'agents active avant la migration.
- L'**état vide de `CLAUDE.md`** (0 octet, modifié 2026-03-05) — un signal
  d'arrêt : le runtime principal n'est plus OpenClaw, c'est Claude Code.

## Distinction avec la version actuelle

| | Legacy (fév-mars 2026) | Actuel (août 2026) |
|---|---|---|
| Runtime principal | OpenClaw (Node + Podman) | Claude Code (M3 + Sonnet/Opus) |
| Modèle primaire | GPT-5.2 Codex | M3 (MiniMax-M3) |
| Fallbacks | Sonnet 4.5, Opus 4.5 | (pas de fallback canonique) |
| Vocabulaire d'agents | A'0/A'1/A'2/A3 (GravityClaw) | A0/A1/A2/A3 (Amadeus, Beth, Computer, Data) |
| Container | Podman | (n/a — direct CLI) |
| Telegram | `paired.json` allowlist | géré par `~/.claude/plugins/telegram` |

**Six mois** séparent les deux, et la **transition est totale** : pas
seulement le moteur, mais tout le vocabulaire d'agents a été refondu.

## Ce que ce concept n'est PAS

- Il **n'est pas une description d'OpenClaw** — c'est un pointeur vers
  une archive, pas une spec.
- Il **n'est pas un récapitulatif de GPT-5.2 Codex** — ce qui a été
  mesuré ici est sa présence dans une config, pas son fonctionnement.
- Il **n'est pas un mode d'emploi** — le bootstrap est dans
  `bootstrap.sh`, non lu ici.

## Concepts liés

- [[legacy-lifeos-app-specs-evolution]] — un autre pan de l'avant-2026-05-22 archivé.
- [[archive-v3-structure-snapshot-2026-08-02]] — le grand versement de l'ère M3.
