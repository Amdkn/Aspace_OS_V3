---
type: Concept
title: state.json — bus sémantique SSOT inter-agents
description: Single source of truth entre A0 → A1 → A2 → A3. Chaque décision Beth/Morty/Curie/Discovery/Orville/Protostar écrit dans state.json avec stage, agent_path, evidence_paths, next_step.
tags: [state.json, bus, ssot, semantique, inter-agents, schema, lock]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: gatekeepers-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/README.md
    title: 00_Gatekeepers_Beth_Morty README — Bus sémantique d'état
    last_modified: 2026-06-21
  - id: beth-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md
    title: A1 Beth Spec — Bus d'état
    last_modified: 2026-05-20
  - id: snw-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/23_12WY_SNW/A2_Curie_SNW_Spec.md
    title: A2 Curie SNW Spec — state.json bus d'état
    last_modified: 2026-05-20
  - id: cerritos-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/25_GTD_Cerritos/README.md
    title: 25_GTD_Cerritos README — State.json bus canon
    last_modified: 2026-06-21
okf_version: "0.2"
---

# state.json — bus sémantique SSOT inter-agents

Le `state.json` est le **bus sémantique canonique** qui synchronise les décisions entre A0, A1, A2 et A3. C'est la machine à états partagée — **pas d'UI visuelle n8n**.

## Localisation

`C:\Users\amado\ASpace_OS_V2\00_Amadeus\40_SYMPHONY_BUS\state.json`

## Schéma canon v1 (plan §9.1)

```json
{
  "cycle": "Q3-2026",
  "week": "W1",
  "stage": "snw_planning",
  "agent_path": "A1:Morty > A2:Curie_SNW > A3:Una",
  "12wy_discipline": "Planning",
  "life_wheel_domain": "LD01",
  "para_bucket": "<path canon>",
  "tokens_used": 0,
  "tokens_budget": 15000,
  "drift_flag": false,
  "raw_input_hash": "sha256:...",
  "raw_input_preview": "first 80 chars...",
  "next_step": "A3:MBenga",
  "created_at": "<ISO-8601>",
  "updated_at": "<ISO-8601>"
}
```

## Stages canon par ship

| Ship | Stages |
|---|---|
| ORVILLE | `compiled` (synthèse 9 crew findings) → routed-to-Morty |
| DISCOVERY | `zora_compiled` → routed-to-Beth-pour-veto |
| SNW | `snw_planning` (W1), `snw_focus` (W2), `snw_metrics` (W3), `snw_execution` (W4) |
| CERRITOS | `captured` (Mariner) → `clarified` (Boimler) → `organized` (Rutherford) → `reviewed` (Tendi) → `engaged` (Freeman) |
| PROTOSTAR | `captured → clarified → eliminated → automated → liberated` (Karpathy loop) |

## Lock atomique et rotation

- `state_writer.py` retry 3× (backoff 100/300/900ms) si `.state.lock` existe.
- Garde-fou : `state.json > 10 KB` → rotation `state.json.prev`.

## Pourquoi state.json et pas une UI visuelle

> *"Pattern remplace UI visuelle n8n."*
> — `25_GTD_Cerritos/README.md`

Une UI n8n reproduirait l'état mais pas le sens. Le bus sémantique rend l'état **traçable, reproductible, et auditable** — chaque transition est lisible sans dépendre d'un rendu visuel.

## Écriture par gatekeeper

- **Beth** écrit `status: GREEN | ORANGE | RED | HALT_LD03 | HALT_LD04` + `agent_path: "A1:Beth > A2:<ship> > A3:<crew>"` + `evidence_paths`.
- **Morty** écrit `stage: executed` + `agent_path` + `next_step` + `evidence_paths`.

## Hook upstream

`mariner-capture.ps1` capture les intentions A0 dans `state.json` **avant** routage. C'est le seul moment où une intention A0 entre dans le bus — avant la classification A1.

## Champs canon à ajouter (plan §3.7 context pack canon)

Pour aligner `ContextPack.template.yml` sur §3.7 du plan : snake_case + ISO-8601. Champs canon à ajouter :

- `cycle: Q3-2026`
- `week: W<n>`
- `12wy_discipline`
- `life_wheel_domain`
- `tokens_used`
- `tokens_budget`
- `drift_flag`
- `raw_input_hash`
- `raw_input_preview`
- `next_step`

## Anti-patterns

- Écrire hors du verrou → race condition.
- Lire sans recharger après lock → stale state.
- Oublier `evidence_paths` → décision sans preuve.
- Multiples `next_step` actifs → drift inevitabil.