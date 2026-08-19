---
type: Concept
title: 40_SYMPHONY_BUS — le bus sémantique (state.json v1)
description: SSOT (Single Source Of Truth) de l'état canonique entre agents A0→A1→A2→A3→B1/B2/B3. Lock atomique + tempfile + rename. Schéma state.json v1 avec 16 champs.
tags: [symphony, bus, state-json, ssot, lock-atomique, canonique]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture_v2, at: 2026-08-19 }
sources:
  - id: SCHEMA_SYMPHONY_BUS
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/40_SYMPHONY_BUS/SCHEMA.md
    title: 40_SYMPHONY_BUS — Schéma canonique du bus sémantique
    last_modified: 2026-06-21
  - id: fancy-hugging-bengio
    resource: .claude/plans/fancy-hugging-bengio.md §23.1
    title: Plan Amorçages 1+2
    last_modified: 2026-06-21
okf_version: "0.2"
---

# 40_SYMPHONY_BUS — le bus sémantique (state.json v1)

## Énoncé

`40_SYMPHONY_BUS/` est le **SSOT (Single Source Of Truth)** de l'état canonique entre agents A0 → A1 → A2 → A3 → B1/B2/B3. Chaque transition écrit dans `state.json` via `state_writer.py` (lock atomique + tempfile + rename).

## Doctrine

2 triptyques imbriqués (12WY⊃PARA⊃DEAL sous Morty + Ikigai⊃Life Wheel⊃Muse sous Beth) + GTD bus horizontal + state.json bus d'état entre agents.

## Fichiers canon

| Path | Rôle |
|------|------|
| `state.json` | État canonique courant (SSOT) |
| `state.json.prev` | Snapshot rotation si state.json > 10 KB (garde-fou taille) |
| `state_writer.py` | Helper Python : lock atomique + write JSON |
| `.state.lock` | Lock file (dossier vide, présence = write en cours) |
| `hand_offs/inbox/` | Inbox A3 Mariner (captures brutes) |
| `hand_offs/outbox/` | Outbox dispatch A3 → B1/B2/B3 |
| `SCHEMA.md` | Ce fichier |

## Schéma state.json v1 (16 champs)

| Champ | Type | Description |
|-------|------|-------------|
| `$schema` | string | Toujours `state-bus.v1` |
| `status` | enum | `INIT` / `ACTIVE` / `DRAINED` |
| `created` | ISO-8601 | Timestamp création state.json |
| `updated` | ISO-8601 | Timestamp dernière écriture |
| `agent_id` | string | Ex: `A0_Amadeus`, `A1:Beth`, `A3:Mariner` |
| `session_id` | string | UUID session CC (ex: `fancy-hugging-bengio`) |
| `cycle` | string | `Q3-2026`, `Q4-2026`, etc. |
| `week` | string | `W1`, `W2`, ..., `W13` (13e semaine) |
| `stage` | enum | `captured` / `clarified` / `organized` / `reviewed` / `engaged` |
| `agent_path` | string | `A1:Morty > A2:Cerritos > A3:Mariner` |
| `para_bucket` | string? | `01_Projects/<name>` / `02_Areas/<domain>` / `03_Resources/<topic>` / `04_Archives/<date>` |
| `12wy_discipline` | string? | `Vision` / `Planning` / `Measure` / `Focus` / `Execution` |
| `life_wheel_domain` | string? | `LD01`..`LD08` |
| `raw_input_hash` | string? | `sha256:<hex>` du prompt A0 |
| `raw_input_preview` | string? | First 80 chars du prompt A0 |
| `next_step` | string | Prochain agent à invoquer |
| `tokens_used` | int | Tokens consommés session courante |
| `tokens_budget` | int | Budget tokens session (default 15000) |
| `drift_flag` | bool | Alerte Morty si true |
| `extra` | object | Champs libres (extensibilité) |
| `metadata` | object | Métadonnées libres (extensibilité) |

## Loi lock atomique (D6 risk)

```
1. Tentative mkdir(.state.lock)
   - si existe, retry 3× avec backoff 100/300/900ms
2. Si succès : tempfile + rename atomique sur state.json
3. Toujours rmdir(.state.lock) en finally
4. Garde-fou : si state.json > 10 KB → warning + rotation prev
```

## Anti-patterns interdits

- ❌ Écrire state.json directement (sans lock) → corruption D6 race condition
- ❌ Oublier rmdir(.state.lock) en finally → bus bloqué
- ❌ raw_input_preview > 80 chars → state.json gonfle + dépasse 10 KB
- ❌ raw_input_hash non-sha256 → incompatibilité downstream verify
- ❌ Hardcoder tokens_budget hors 15000 → anti-pattern Morty

## Voir aussi

- `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` §23 — plan canon Amorçages 1+2
- `40_SYMPHONY_BUS/hand_offs/inbox/` — captures A3 Mariner
- `40_SYMPHONY_BUS/hand_offs/outbox/` — dispatch A3 → B1/B2/B3
