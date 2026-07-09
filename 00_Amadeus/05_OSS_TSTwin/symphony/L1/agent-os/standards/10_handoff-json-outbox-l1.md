---
name: handoff-json-outbox-l1
version: 1.0
created: 2026-06-07
phase: SIGNAL (toutes phases qui produisent un output)
actor: A1 ↔ A2 ↔ A3
format: JSONL append-only, 1 ligne par message
path: outbox/l1/YYYY-MM-DD/
---

# 10 — Hand-off JSON Outbox (L1 Inter-Agent Comms)

> Tous les hand-offs A1↔A2↔A3 passent par un **outbox JSONL append-only**.
> Pas de base de données, pas de daemon, pas de queue. Juste des fichiers.
> Même pattern que Symphony SYMPH-001, scopé L1.

## Structure

```
outbox/
└── l1/
    └── 2026-06-07/
        ├── 14-22-08_WAKE_t1-2f7a-beth.json
        ├── 14-22-09_PROBE_t1-2f7a-boimler.json
        ├── 14-22-10_DECIDE_t1-2f7a-mercer.json
        ├── 14-22-11_EXECUTE_t1-2f7a-tendi.json
        ├── 14-22-12_OBSERVE_t1-2f7a-tilly.json
        ├── 14-22-13_LEARN_t1-2f7a-archer.json
        ├── 14-22-14_SIGNAL_t1-2f7a-beth.json
        └── 14-22-15_SLEEP_t1-2f7a-a0.json
```

- Dossier par date UTC
- Nom : `HH-MM-SS_PHASE_t<tick>-<agent>.json`
- Append-only (jamais de modification, jamais de suppression sauf rotation 7j)

## Format standard (tous messages)

```json
{
  "msg_id": "<uuid>",
  "tick_id": "<workflow>-<ts>",
  "phase": "WAKE|PROBE|DECIDE|EXECUTE|OBSERVE|LEARN|SIGNAL|SLEEP",
  "ts": "<ISO 8601 UTC ms>",
  "from": {
    "level": "A0|A1|A2|A3",
    "agent_id": "Amadeus|Beth|Morty|Mercer|Boimler|...",
    "vessel_id": "Orville|Discovery|SNW|Enterprise|Cerritos|Protostar|null"
  },
  "to": {
    "level": "A0|A1|A2|A3",
    "agent_id": "...",
    "vessel_id": "..."
  },
  "intent": "<short text>",
  "payload": { /* spécifique par phase */ },
  "evidence_url": "<string|null>",
  "cost_delta_usd": <float|null>,
  "error": "<string|null>"
}
```

## Spécificités par phase

| Phase | Payload type | Exemple |
|---|---|---|
| WAKE | `{"beth_state": "GREEN"}` | Morning brief |
| PROBE | `{"incoming": [...], "filtered": [...]}` | Boimler triage |
| DECIDE | `{"routing": [{"vessel_id": "...", "crew_ids": [...]}]}` | Mercer route |
| EXECUTE | `{"mission_id": "...", "result": {...}}` | Freeman work |
| OBSERVE | `{"observation": "...", "verdict": "OK|WARN|FAIL"}` | Tilly reflect |
| LEARN | `{"lesson": "...", "linked_kb": "[[obsidian:...]]"}` | Archer learn |
| SIGNAL | `{"report_to_beth": {...}, "beth_state": "ORANGE"}` | A2 → A1 |
| SLEEP | `{"close": true, "a0_check": "pending|ok|halt"}` | A0 close |

## Anti-patterns

- ❌ Fichier dans `outbox/` qui n'est pas JSON valide → lint fail au LEARN
- ❌ Fichier modifié après écriture (append-only violation) → Donna DLQ alert
- ❌ Fichier sans `from` ou `to` → shadow message
- ❌ Hard-delete d'un fichier (utiliser `_archive/2026-06-07/` après 7 jours)
- ❌ Hand-off direct agent↔agent sans passer par l'outbox (shadow mesh)

## Rotation (7 jours)

```
outbox/l1/2026-06-07/  ── après 2026-06-14 ──>  outbox/l1/_archive/2026-06-07/
  (toujours lisible)                            (gzippé, conservé 90j)
```

## Source canonique

- `ADR-SYMPH-001` (pattern outbox/inbox files)
- `AGENTS.md` (séparation A0/A1/A2/A3)
- Format inspiré de : `heartbeat-tick-symphony.ps1` (cf. SDD-008)
