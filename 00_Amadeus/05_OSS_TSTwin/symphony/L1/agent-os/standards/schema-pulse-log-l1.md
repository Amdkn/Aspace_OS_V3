---
name: schema-pulse-log-l1
version: 1.0
created: 2026-06-07
layer: L1
extends: 02-ADR/ADR-SYMPH-003 §D3 (schema 14 champs L2)
path: symphony/L1/agent-os/pulse.log
format: JSONL append-only
---

# Schema `pulse.log` — L1 Life OS

> Le runtime L1 a son **propre** `pulse.log` (distinct du L2 et du L0).
> 14 champs L2 hérités + 4 champs L1-specific.

## Path

```
symphony/L1/agent-os/pulse.log         ← ce runtime
symphony/agent-os/pulse.log            ← L0/L2
symphony/L2/agent-os/pulse.log         ← L2 (futur)
```

Append-only. 1 ligne JSON par phase. 8 lignes par tick. Timestamps UTC ISO-8601 ms.

## Champs (18 total : 14 L2 + 4 L1)

### Hérités de L2 (14)

| Champ | Type | Description |
|---|---|---|
| `ts` | string ISO 8601 ms UTC | Timestamp d'écriture de la ligne |
| `tick_id` | string | `<vessel>-<UTC ts min-precision>` |
| `workflow_id` | string | "L1_morning_brief" / "L1_weekly_review" / etc. |
| `issue_id` | string\|null | Plane issue ID, Baserow row ID, etc. |
| `phase` | enum | WAKE\|PROBE\|DECIDE\|EXECUTE\|OBSERVE\|LEARN\|SIGNAL\|SLEEP |
| `duration_ms` | int | Durée de la phase |
| `standards_injected` | array<string> | Liste des 11 standards L1 utilisées |
| `decision` | string | Décision textuelle de la phase |
| `evidence_url` | string\|null | Lien Obsidian/Plane/Affine/Baserow |
| `cost_delta_usd` | float\|null | Coût LLM de la phase |
| `cumulative_cost_usd` | float\|null | Coût cumulé du tick |
| `aspace_layer` | enum | Toujours "L1" pour ce runtime |
| `soc_target_domain` | string\|null | Domaine SOA01-SOA08 si impact Business OS, sinon null |
| `error` | string\|null | null si OK, message si fail |

### L1-specific (4)

| Champ | Type | Description |
|---|---|---|
| `vessel_id` | string\|null | "Orville"\|"Discovery"\|"SNW"\|"Enterprise"\|"Cerritos"\|"Protostar"\|null |
| `crew_id` | string\|null | "Boimler"\|"Tendi"\|"Tilly"\|"Culber"\|... |
| `ld_id` | string\|null | "LD01"..."LD08" (Life Domain impacté) |
| `agent_state` | string\|null | "GREEN"\|"ORANGE"\|"RED"\|"HALT_LD03"\|"HALT_LD04" (Beth 5-state) |

## Invariants

- `error: null` quand tout va bien
- Aucune ligne n'est jamais réécrite
- Rotation hebdomadaire (7j) → `pulse.log.archive/YYYY-MM-DD.jsonl.gz`
- Validation post-rotation par `jq -e .` sur le fichier compressé
- `aspace_layer` toujours "L1" pour ce runtime

## Exemple (matinale typique)

```jsonl
{"ts":"2026-06-07T07:00:00.123Z","tick_id":"L1_morning-20260607T07","workflow_id":"L1_morning_brief","issue_id":null,"phase":"WAKE","duration_ms":120,"standards_injected":["01_agent-hierarchy-contract.md","02_beth-5-states-machine.md"],"decision":"beth_state=GREEN","evidence_url":"[[adr:SYMPH-001]]","cost_delta_usd":0.001,"cumulative_cost_usd":0.001,"aspace_layer":"L1","soc_target_domain":null,"error":null,"vessel_id":null,"crew_id":"Beth","ld_id":null,"agent_state":"GREEN"}
{"ts":"2026-06-07T07:00:01.500Z","tick_id":"L1_morning-20260607T07","workflow_id":"L1_morning_brief","issue_id":null,"phase":"PROBE","duration_ms":850,"standards_injected":["08_affine-kanban-gtd.md","04_crew-bridge-protocol.md"],"decision":"2min_rule:3_cards_processed","evidence_url":"affine://board/L1_main/card/1234","cost_delta_usd":0.003,"cumulative_cost_usd":0.004,"aspace_layer":"L1","soc_target_domain":null,"error":null,"vessel_id":"Cerritos","crew_id":"Boimler","ld_id":null,"agent_state":"GREEN"}
{"ts":"2026-06-07T07:00:02.800Z","tick_id":"L1_morning-20260607T07","workflow_id":"L1_morning_brief","issue_id":null,"phase":"DECIDE","duration_ms":600,"standards_injected":["03_vessel-captain-protocol.md","10_handoff-json-outbox-l1.md"],"decision":"route:Cerritos->Tendi;Discovery->Tilly","evidence_url":"outbox://l1/2026-06-07/07-00-02_DECIDE_t1-2f7a-mercer.json","cost_delta_usd":0.002,"cumulative_cost_usd":0.006,"aspace_layer":"L1","soc_target_domain":null,"error":null,"vessel_id":"Cerritos","crew_id":"Mercer","ld_id":null,"agent_state":"GREEN"}
{"ts":"2026-06-07T07:00:05.100Z","tick_id":"L1_morning-20260607T07","workflow_id":"L1_morning_brief","issue_id":null,"phase":"EXECUTE","duration_ms":2300,"standards_injected":["04_crew-bridge-protocol.md","08_affine-kanban-gtd.md","11_canon-vs-runtime-drift.md"],"decision":"affine_cards_moved:5,drift_audit:OK","evidence_url":"affine://board/L1_main/card/1235","cost_delta_usd":0.005,"cumulative_cost_usd":0.011,"aspace_layer":"L1","soc_target_domain":null,"error":null,"vessel_id":"Cerritos","crew_id":"Tendi","ld_id":null,"agent_state":"GREEN"}
{"ts":"2026-06-07T07:00:06.000Z","tick_id":"L1_morning-20260607T07","workflow_id":"L1_morning_brief","issue_id":null,"phase":"OBSERVE","duration_ms":700,"standards_injected":["02_beth-5-states-machine.md","09_stop-authority-protocol.md"],"decision":"reflect:ORANGE_warn(cerritos_load=high)","evidence_url":"obsidian://20_Life_OS/Cerritos/weekly_log.md","cost_delta_usd":0.002,"cumulative_cost_usd":0.013,"aspace_layer":"L1","soc_target_domain":null,"error":null,"vessel_id":"Discovery","crew_id":"Tilly","ld_id":"LD04","agent_state":"ORANGE"}
{"ts":"2026-06-07T07:00:07.500Z","tick_id":"L1_morning-20260607T07","workflow_id":"L1_morning_brief","issue_id":null,"phase":"LEARN","duration_ms":1100,"standards_injected":["06_obsidian-vault-linkage.md","11_canon-vs-runtime-drift.md"],"decision":"lesson:cerritos_load_pattern","evidence_url":"obsidian://20_Life_OS/Cerritos/lessons/2026-06-07.md","cost_delta_usd":0.003,"cumulative_cost_usd":0.016,"aspace_layer":"L1","soc_target_domain":null,"error":null,"vessel_id":"Enterprise","crew_id":"Archer","ld_id":null,"agent_state":"ORANGE"}
{"ts":"2026-06-07T07:00:08.900Z","tick_id":"L1_morning-20260607T07","workflow_id":"L1_morning_brief","issue_id":null,"phase":"SIGNAL","duration_ms":800,"standards_injected":["01_agent-hierarchy-contract.md","02_beth-5-states-machine.md"],"decision":"report_to_beth:state=ORANGE","evidence_url":"outbox://l1/2026-06-07/07-00-08_SIGNAL_t1-2f7a-beth.json","cost_delta_usd":0.001,"cumulative_cost_usd":0.017,"aspace_layer":"L1","soc_target_domain":null,"error":null,"vessel_id":null,"crew_id":"Beth","ld_id":null,"agent_state":"ORANGE"}
{"ts":"2026-06-07T07:00:09.200Z","tick_id":"L1_morning-20260607T07","workflow_id":"L1_morning_brief","issue_id":null,"phase":"SLEEP","duration_ms":300,"standards_injected":["01_agent-hierarchy-contract.md"],"decision":"close:tick_complete,a0_pending","evidence_url":null,"cost_delta_usd":0.0,"cumulative_cost_usd":0.017,"aspace_layer":"L1","soc_target_domain":null,"error":null,"vessel_id":null,"crew_id":"Amadeus","ld_id":null,"agent_state":"ORANGE"}
```

## Anti-patterns

- ❌ `aspace_layer` ≠ "L1" dans ce fichier (污染 cross-layer)
- ❌ `agent_state` manquant quand `vessel_id` est Cerritos/Discovery (LD04 manquant)
- ❌ Ligne sans `crew_id` quand phase = EXECUTE/OBSERVE
- ❌ Coût cumulé > `sla.max_cost_usd` (= 0.05 USD) sans escalade

## Source canonique

- `ADR-SYMPH-003` §D3 (L2 schema, parent)
- `AGENTS.md` (séparation A0/A1/A2/A3)
