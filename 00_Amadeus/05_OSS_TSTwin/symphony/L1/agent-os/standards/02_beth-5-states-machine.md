---
name: beth-5-states-machine
version: 1.0
created: 2026-06-07
phase: WAKE + OBSERVE + SIGNAL
actor: A1 Beth + A1 Morty (intake shadow)
---

# 02 — Beth 5-States Machine (A1 Gatekeeper)

> A1 Beth est l'**autorité globale** du runtime L1. Ses 5 états sont la loi
> qui contraint tous les autres agents. Morty est son **intake shadow** —
> il porte les messages entrants, Beth tranche.

## Les 5 états

```
            ┌──── HALT_LD04 (Cognition) ────┐
            │                                │
            ▼                                │
   ┌──────────────┐                  ┌───────┴────────┐
   │     RED      │◄─────escalate────│     ORANGE     │
   │ (alerte)     │                  │ (vigilance)    │
   └──────┬───────┘                  └───────┬────────┘
          │                                  ▲
          │            ┌──────┐             │
          └───────────►│GREEN │◄────────────┘
                       │(OK)  │  routine tick
                       └──────┘
```

| État | Sémaphore | Condition | Effet système |
|---|---|---|---|
| **GREEN** | 🟢 | Routine, tous vessels OK | Tous les ticks Symphony s'exécutent normalement |
| **ORANGE** | 🟠 | 1 vessel degrade, ou P3 alert | Tick continue, mais A2 captain doit reporter toutes les 4 phases |
| **RED** | 🔴 | ≥ 2 vessels degrades, ou P2 alert | A2 captains réduisent scope, A3 crews gèlent nouveaux engagements |
| **HALT_LD03** | 🛑 | Santé en danger (Culber autorité) | **STOP global**, A3 health-related crews only |
| **HALT_LD04** | 🛑 | Cognition en surcharge (Tilly autorité) | **STOP global**, A3 cognition-related crews only |

## Transitions (règles)

| De | Vers | Trigger | Acteur autorisé |
|---|---|---|---|
| GREEN | ORANGE | 1 captain signale degradation | A2 captain (escalate) |
| ORANGE | GREEN | Tous vessels恢复正常 après 2 ticks consécutifs | A1 Beth (auto-reset) |
| ORANGE | RED | 2e captain signale degradation | A1 Beth (ou A0 Amadeus) |
| RED | ORANGE | 1 tick de stabilité | A1 Beth |
| RED | HALT_LD03 | Culber (LD03) émet signal santé critique | Culber (captain LD03) |
| RED | HALT_LD04 | Tilly (LD04) émet signal cognition critique | Tilly (captain LD04) |
| HALT_* | ORANGE | A0 Amadeus émet reprise | A0 (seul autorisé) |
| HALT_* | GREEN | 5 ticks ORANGE consécutifs stables | A0 + A1 Beth co-signé |

## Morty (intake shadow)

Morty est **l'oreille** de Beth. Il :
1. Reçoit tous les `escalate` A2↔A3
2. Les route vers Beth avec un verdict préliminaire (P1/P2/P3)
3. Ne prend **jamais** de décision 5-state seul

**Anti-pattern** : Morty qui parle au nom de Beth. → Shadow bypass, Beth doit le court-circuiter.

## Output attendu dans pulse.log

À chaque transition, A1 Beth écrit une ligne pulse.log avec :
- `agent_state: "GREEN|ORANGE|RED|HALT_LD03|HALT_LD04"`
- `decision: "state_transition:<from>-><to>"`
- `evidence_url: <link vers l'escalate qui a déclenché>`

## Source canonique

- `20_Life_OS/` (canon A'Space OS V2)
- Memory : [beth-5-states] entry attendue dans `wiki/L0/` (TODO scaffolder)
