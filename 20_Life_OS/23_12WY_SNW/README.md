# 23_12WY_SNW - Handoff A2

> Layer: L1 Life OS  
> A2: Curie aboard USS Strange New Worlds  
> Framework: 12 Week Year  
> Shadow tool: Baserow 12WY tables  
> Gatekeepers: Beth validates priorities; Morty routes execution packets  
> Status: SHADOW_ACTIVE

## Mission

SNW turns validated Life OS direction into 12WY execution: Quarter Intent, Rocks, Warp Core tactics, Scorecard, and Time Use discipline. It is the bridge between meaning and weekly movement.

## Resume Protocol

1. Read Beth/Morty specs in `..\00_Gatekeepers_Beth_Morty`.
2. Read `A2_Curie_SNW_Spec.md`.
3. Check whether the Context Pack names a Quarter Intent, Rock, tactic, scorecard, or time block.
4. Use Baserow only as the Shadow L1 surface; do not mutate schemas without explicit approval.
5. Return proof paths and next owner.

## A2 Spec

- `A2_Curie_SNW_Spec.md`
- `A3_SNW_References_Index.md`

## Crew Map

| Folder | A3 role | 12WY discipline |
|---|---|---|
| `01_Vision_Pike` | Pike | Vision / Quarter Intent |
| `02_Planning_Una` | Una | Planning / Rocks |
| `03_Focus_MBenga` | M'Benga | Process control / strategic focus |
| `04_Metrics_Chapel` | Chapel | Scorecard / measurement |
| `05_Execution_Ortegas` | Ortegas | Weekly execution |

## A3 Rule

SNW A3 agents produce narrow findings only. Curie compiles the 12WY packet and Morty routes execution. If an A3 claim cannot cite a local path or the references index, it stays a `hypothesis`.

## Outputs

- Quarter Intent proposal or audit.
- Rock decomposition.
- Warp Core tactical packet.
- Scorecard / Time Use routing note.

## Handoff Rules

- SNW does not invent priorities without Beth or A0 intent.
- A Rock longer than one week must be decomposed into Warp Core tactics.
- Failed tactics are routed to Cerritos for GTD clarification or Protostar for DEAL relief.
- Baserow current docs are `NEEDS_CONTEXT7` before schema mutation.

## Evidence

- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\symphony-baserow.spec.md`
- `C:\Users\amado\ASpace_OS_V2\10_Tech_OS\12_Blueprints\01-SDD\SDD-008_shadow-L1-life-os.md`

## Context7 Boundary

No Context7 lookup is required to read or update this local handoff. Use Context7 before Baserow API, schema, rollup, MCP, Symphony adapter, or CLI configuration.

## Alignement Plan fancy-hugging-bengio.md (2026-06-21)

> **D1 anchor** : `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` §3.5 (triptyque MORTY 12WY⊃PARA⊃DEAL) + §4 (Cycle 12WY Q3 2026). **Owner** : A1 Morty (Focus Gatekeeper). **Parent canon** : `AGENTS.md` L1 Life OS. **Mode** : SHADOW_ACTIVE, alignment pending A0 milestone W1 (07/05/26).

### Matrice 5 disciples × 5 horizons (Ikigai 4P+5H bridge)

| A3 disciple | 12WY discipline | Hor. canon | Ikigai pilier / horizon | Item Q3 2026 owner | A1 routing |
|---|---|---|---|---|---|
| **Pike** | Vision / Quarter Intent | H10 | Klyden (H90 héritage) ↔ Bortus (H10 stratégie) | Item 2 — Définir 09/14 = 13e semaine, 09/21 = Semaine 0 du 4e cycle | A1 Morty |
| **Una** | Planning / Rocks | H10 | Bortus (H10 discipline) | Items 1-2 — SOB Abdaty + 13e semaine | A1 Morty |
| **M'Benga** | Focus / Process control | H1 | Ed (H1 craft) ↔ Gordon (H1 passion) | Items 3-4 — Auto-research IA + TOKEN frugalité | A1 Morty |
| **Chapel** | Metrics / Scorecard | H10 | Claire (H3 vocation) + D11 Fable score | Items 5-7 — YouTube PARA + Hermes + Agent OS | A1 Morty |
| **Ortegas** | Weekly execution / Time Use | H1 | Ed (H1 craft) + Isaac (H1 logique) | Items 8-10 — Business OS Life-OS-2026 + A3 structuration + Solaris/OMK/ABC | A1 Morty |

**Doctrine** : les 5 disciples SNW structurent la cadence hebdo (50/30/20 rule) qui sert de rail à l'alignement Ikigai 4P+5H et à l'équilibre Life Wheel LD01-LD08. Curie compile, A1 Morty route.

### Cycle 12WY Q3 2026 (06/15 → 09/07) — mapping A3

| Week | Dates | Items | A3 owner principal | Livrables observables |
|---|---|---|---|---|
| **W1** | 06/15 → 07/05 | Items 1-2 | **Una** (Planning) + **Pike** (Vision) | SOB Abdaty introduit + 13e semaine définie (09/14) |
| **W2** | 07/06 → 07/26 | Items 3-4 | **M'Benga** (Focus) | Auto-research LLM WIKI lancé + TOKEN plan MiniMax/Ollama frugalité |
| **W3** | 07/27 → 08/16 | Items 5-6 | **Chapel** (Metrics) | YouTube → PARA Geordi 114 .md + Hermes Agent LIVE |
| **W4** | 08/17 → 09/07 | Items 7-12 | **Ortegas** (Execution) + **Chapel** (Measure) | Agent OS Symphony interface + Life-OS-2026 BETA + 36 A3 Life OS structurés + Memory core VPS DEAL Muse + auto-amélioration cycle 4 |
| **W5+** | 09/14 = W13 → 09/21 W0 | Kick-off Cycle 4 | (hors scope Q3) | Semaine 0 = 09/21/26 |

**Total** : 12 items canoniques A0 verbatim, tous routés via A2 Curie SNW (5 disciplines) → A1 Morty (Focus Gatekeeper) → B1/B2/B3 (Solarpunk/OMK/ABC swarms).

### state.json bus d'état (Amorçage 1 §9.1 plan)

Chaque transition d'agent SNW écrit dans `C:\Users\amado\ASpace_OS_V2\00_Amadeus\40_SYMPHONY_BUS\state.json` (bus sémantique canon) :

```json
{
  "cycle": "Q3-2026",
  "week": "W1",
  "stage": "snw_planning",
  "agent_path": "A1:Morty > A2:Curie_SNW > A3:Una",
  "12wy_discipline": "Planning",
  "next_step": "A3:MBenga",
  "tokens_used": 0,
  "tokens_budget": 15000,
  "drift_flag": false
}
```

**Schéma complet** : voir plan §9.1 + `40_SYMPHONY_BUS/SCHEMA.md` (à créer Amorçage 1).

### Out of scope Q3 2026

- **Rick Sobriété Kernel pivots** : différé Q4 2026 / Q1 2027 (SDD-010 veto 90j jusqu'au 2026-08-11).
- **Doctors Who faction canonisation** : Q4 2026 / Q1 2027 / Q2 2027.
- **OMK Services BOS** : CLOS (2026-06-20), hors scope.
- **Refactor Symphony 35 A3 twins** : pas demandé sauf surnuméraire.

**Critère de succès W1** : Items 1-2 livrés d'ici 2026-07-05. A0 émet "OK" milestone.

