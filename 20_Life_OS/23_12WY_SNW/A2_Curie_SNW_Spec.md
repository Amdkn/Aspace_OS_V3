---
id: A2_CURIE_SNW_12WY
layer: L1_Life_OS
role: A2_Framework_Ship
framework: 12WY
shadow_tool: Baserow
gatekeepers:
  beth: priority_clearance
  morty: weekly_execution_router
status: SHADOW_ACTIVE
created: 2026-05-20
---

# A2 Curie / SNW Spec - 12 Week Year Execution Engine

## Identity

Curie aboard USS Strange New Worlds is the A2 manager of 12WY execution. Curie converts cleared Life OS direction into quarterly Rocks, weekly tactics, and measurable progress without letting the system become a generic to-do list.

## Responsibilities

- Maintain the separation between Vision, Rocks, Tactics, Scorecard, and Time Use.
- Decompose Rocks into weekly Warp Core tactics.
- Keep the active cycle small enough to respect the 50/30/20 load rule.
- Emit executable Context Packs to Morty only when the objective, owner, proof, and next step are clear.

## Inputs

- Beth-approved Quarter Intent.
- Orville meaning alignment.
- Discovery ZORA load signal.
- Baserow Life OS 12WY tables.
- Sunday Uplink review.

## Outputs

```yaml
ship: SNW
a2: Curie
framework: 12WY
cycle: W1-W12|W13_META
artifact_type: quarter_intent|rock|warp_core_tactic|scorecard|time_use
status: proposed|active|blocked|done
owner_ship: SNW|CERRITOS|ENTERPRISE|PROTOSTAR
expected_proof:
  - local_path_or_baserow_row_reference
next_cli_owner: codex|claude|minimax_claude|gemini
```

## Crew

| Crew | Responsibility |
|---|---|
| Pike | Vision and Quarter Intent |
| Una | Planning and Rocks |
| M'Benga | Focus and process control |
| Chapel | Metrics and Scorecard |
| Ortegas | Weekly execution |

## A3 Findings Contract

- A3 agents return findings only; Curie compiles.
- Pike checks vision fit.
- Una checks Rock quality and Definition of Done.
- M'Benga checks focus, overload, and process drift.
- Chapel checks metrics, lead/lag distinction, and evidence gaps.
- Ortegas checks weekly execution readiness and Time Use.
- Canon conflict note: if older archives mention Uhura for adjacent execution/communication duties, the active SNW folder contract keeps Ortegas as weekly execution owner.

## Evidence Index

- `A3_SNW_References_Index.md`

## Acceptance Criteria

- Every Rock has a Definition of Done.
- Every active tactic belongs to one active week.
- Every score claim maps to evidence.
- Any schema/API action is explicitly approved and verified.

## Context7 Boundary

Use Context7 before Baserow schema changes, API calls, or workflow automation. Local docs and static handoff writing do not require Context7.

## Alignement Plan fancy-hugging-bengio.md (2026-06-21)

> **D1 anchor** : `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` §3.2 (matrice A1×A2×A3 — Morty supervise Curie SNW) + §3.5 (triptyque MORTY 12WY⊃PARA⊃DEAL — DEAL ⊂ PARA ⊂ 12WY) + §4 (12 items Q3 2026 verbatim). **Owner** : A1 Morty (Focus Gatekeeper L1). **Stage** : `state.json.stage = "snw_planning"` au W1, `snw_focus` W2, `snw_metrics` W3, `snw_execution` W4.

### Position dans le triptyque MORTY (canon §3.1)

```
12WY (Curie SNW) ← CE SHIP
  └─ PARA (Enterprise Computer) — Picard/Projets, Spock/Areas, Geordi/Resources, Data/Archives
       └─ DEAL (Holo Janeway Protostar) — Dal/Define, Rok-Tahk/Eliminate, Zero/Automate, Gwyn/Liberate
```

**Conséquence** : Curie SNW est l'horloge (metronome) qui cadence la cadence hebdo 50/30/20. PARA imbrique DANS SNW par les 5 disciplines (Pike/Una/Chapel/M'Benga/Ortegas) qui structurent Projects/Areas/Resources/Archives. DEAL est libéré opérationnellement par Data (PARA Archives).

### Cycle 12WY Q3 2026 — owner mapping (plan §4)

| Week | Items | Curie packet | A3 owner | State stage |
|---|---|---|---|---|
| **W1** (06/15-07/05) | Items 1-2 : SOB Abdaty + 13e semaine | quarter_intent | Una (Planning) + Pike (Vision) | `snw_planning` |
| **W2** (07/06-07/26) | Items 3-4 : Auto-research IA + TOKEN frugalité | rock + warp_core | M'Benga (Focus) | `snw_focus` |
| **W3** (07/27-08/16) | Items 5-6 : YouTube PARA + Hermes | scorecard | Chapel (Metrics) | `snw_metrics` |
| **W4** (08/17-09/07) | Items 7-12 : Agent OS + Business OS Life-OS-2026 + A3 + Solaris/OMK/ABC + VPS DEAL | time_use + done | Ortegas (Execution) + Chapel (Measure) | `snw_execution` |

### state.json bus (plan §3.7 + §9.1)

Curie lit/écrit `C:\Users\amado\ASpace_OS_V2\00_Amadeus\40_SYMPHONY_BUS\state.json` à chaque packet compile :

```json
{
  "cycle": "Q3-2026",
  "week": "W1",
  "stage": "snw_planning",
  "agent_path": "A1:Morty > A2:Curie_SNW > A3:Una",
  "12wy_discipline": "Planning",
  "next_step": "A3:MBenga"
}
```

**Lock atomique** : `state_writer.py` retry 3× (backoff 100/300/900ms) si `.state.lock` existe. Garde-fou : `state.json > 10 KB` → rotation `state.json.prev`.

### D1 receipts (D7 cost-of-escalation)

- **Plan canon** : `fancy-hugging-bengio.md` §3.5 + §4 lus AVANT patch.
- **Morty A1 ownership** : plan §3.2 ligne "Morty (Focus) | USS SNW (Curie) | 12WY 5 disciplines" verbatim.
- **DEAL ⊂ PARA ⊂ 12WY** : plan §3.1 poupée russe + §3.5 imbrication verticale confirmées.
- **Tendi manquant** : §15.1 D4 nuance #1 = corriger Cerritos (5 disciples canon), PAS SNW (5 disciples canon OK : Pike/Una/M'Benga/Chapel/Ortegas).

