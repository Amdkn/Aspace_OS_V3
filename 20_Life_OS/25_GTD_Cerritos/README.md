# 25_GTD_Cerritos - Handoff A2

> Layer: L1 Life OS  
> A2: Holo Deck aboard USS Cerritos  
> Framework: GTD  
> Shadow tool: Plane  
> Gatekeepers: Beth prevents overload; Morty routes next actions  
> Status: SHADOW_ACTIVE

## Mission

Cerritos is the chaos-to-action engine. It captures loose inputs, clarifies them, organizes them, reviews them, and turns them into next actions without pretending that every input is a project.

## Resume Protocol

1. Read Beth/Morty specs.
2. Read `A2_HoloDeck_Cerritos_Spec.md`.
3. Check whether the item is inbox, clarify, organize, review, or engage.
4. If it is larger than a next action, route to Enterprise or SNW.
5. Do not create remote Plane tasks unless explicitly asked and credential scope is clear.

## A2 Spec

- `A2_HoloDeck_Cerritos_Spec.md`
- `A3_Cerritos_References_Index.md`

## Crew Map

| Folder | A3 role | GTD stage |
|---|---|---|
| `01_Inbox_Mariner` | Mariner | Capture |
| `02_Clarify_Boimler` | Boimler | Clarify |
| `03_Organize_Rutherford` | Rutherford | Organize |
| `04_Review_Tendi` | Tendi | Review |
| `05_Engage_Freeman` | Freeman | Engage |

## A3 Rule

Cerritos A3 agents produce narrow GTD findings only. Holo Deck compiles the GTD decision and Morty routes executable next actions. If a claim cannot cite a local path or the references index, it stays a `hypothesis`.

## Outputs

- Next-action packet.
- Project escalation to Enterprise.
- Rock/tactic escalation to SNW.
- Blocked/overload signal to Beth.

## Handoff Rules

- Cerritos owns next actions, not life strategy.
- Plane is the Shadow L1 GTD surface, but remote mutation requires explicit approval.
- If an item needs more than one session or one week, do not leave it as a loose Plane task.
- Plane API/config claims are `NEEDS_CONTEXT7` until verified.

## Evidence

- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\symphony-plane.spec.md`
- `C:\Users\amado\ASpace_OS_V2\10_Tech_OS\12_Blueprints\01-SDD\SDD-008_shadow-L1-life-os.md`

## Context7 Boundary

No Context7 lookup is required to read or update this local handoff. Use Context7 before Plane API, project schema, MCP, webhook, or provider configuration.

## Alignement Plan fancy-hugging-bengio.md (2026-06-21)

**Source de vérité canonique** : `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` §3.5 (triptyque MORTY 12WY⊃PARA⊃DEAL + GTD bus horizontal) + §27 (ADR-GTD-001 Cerritos 5 stages canon, à créer — voir §15.2 gap #10).

**Matrice canon 5 stages × 5 A3 twins (A1 Morty Focus → A2 Holo Deck Cerritos → A3 5 Airlock)** :

| Stage GTD | A3 twin | Stage canon | state.json stage | D3 nuance |
|---|---|---|---|---|
| 1. Capture | **Mariner** | `Capture` | `captured` | Mariner = raw_input_preview (80 chars) + sha256 hash, `next_step: "A3:Boimler"` |
| 2. Clarify | **Boimler** | `Clarify` | `clarified` | Boimler = para_bucket assigné + tag (`@next`/`@waiting`/`@someday`/`@archive`) |
| 3. Organize | **Rutherford** | `Organize` | `organized` | **D3 nuance détectée** : `fancy-hugging-bengio.md §15.1` identifie **Tendi = Organize** (canon twin protostar). Le terrain canon local garde **Rutherford = Organize** (résolu 2026-05-20, canon actif). Voir `A3_Cerritos_References_Index.md` Canon Conflicts. |
| 4. Review | **Tendi** | `Review` | `reviewed` | **D3 nuance détectée** : `fancy-hugging-bengio.md §15.1` identifie **Rutherford = Reflect**. Le terrain canon local garde **Tendi = Review** (canon actif). Voir `A3_Cerritos_References_Index.md` Canon Conflicts. |
| 5. Engage | **Freeman** | `Engage` | `engaged` | Freeman = `next_step` actionnable + drift_flag si context drifté, dispatch vers A1 Morty |

**Shadow tool Plane.so** : Plane workspace = surface GTD distante (L1 Shadow per `SDD-008`). Migrations A0 → CC doivent vérifier Plane scope avant mutation (D6 fan-out, `mcp__symphony-plane__*` tools listés).

**State.json bus (canon §3.7 plan fancy-hugging-bengio)** : chaque transition A3 écrit dans `00_Amadeus/40_SYMPHONY_BUS/state.json` (state-bus.v1). Pattern = machine à états sémantique, **pas d'UI visuelle n8n**. Schema canon : `cycle`, `week`, `stage`, `agent_path`, `para_bucket`, `12wy_discipline`, `life_wheel_domain`, `raw_input_hash`, `raw_input_preview`, `next_step`, `tokens_used`, `tokens_budget`, `drift_flag`, `created_at`, `updated_at`.
