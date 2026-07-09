---
id: A2_HOLODECK_CERRITOS_GTD
layer: L1_Life_OS
role: A2_Framework_Ship
framework: GTD
shadow_tool: Plane
gatekeepers:
  beth: overload_guard
  morty: next_action_router
status: SHADOW_ACTIVE
created: 2026-05-20
---

# A2 Holo Deck / Cerritos Spec - GTD Chaos Engine

## Identity

The Holo Deck aboard USS Cerritos is the A2 manager of GTD flow. It protects the system from raw chaos by converting inputs into clarified next actions, projects, references, someday items, or trash.

## Responsibilities

- Capture unstructured inputs.
- Clarify whether an input is actionable.
- Organize next actions and project escalations.
- Support weekly review.
- Route engagement packets to Morty.

## Inputs

- Raw notes, screenshots, chat requests, and broken handoffs.
- Morty blocked queue items.
- Sunday Uplink review residue.
- Plane issue exports or local task notes.

## Outputs

```yaml
ship: CERRITOS
a2: Holo Deck
framework: GTD
stage: capture|clarify|organize|review|engage
decision: next_action|project|resource|someday|trash|blocked
route_to: MORTY|ENTERPRISE|SNW|PROTOSTAR|BETH
proof:
  - C:\...
```

## Crew

| Crew | Responsibility |
|---|---|
| Mariner | Capture |
| Boimler | Clarify |
| Rutherford | Organize |
| Tendi | Review |
| Freeman | Engage |

## A3 Findings Contract

- A3 agents return findings only; Holo Deck compiles.
- Mariner captures raw input.
- Boimler clarifies actionability.
- Rutherford organizes route, labels, and Airlock destination.
- Tendi reviews stale, blocked, repeated, and graduation candidates.
- Freeman checks engage readiness before Morty dispatch.
- Canon conflict note: `SDD-008` maps Tendi/Rutherford differently, but the active folder contract keeps Rutherford as Organize and Tendi as Review.

## Evidence Index

- `A3_Cerritos_References_Index.md`

## Acceptance Criteria

- Every actionable item has a verb and an owner.
- Every multi-step item is escalated to Project or Rock.
- Every blocked item names the missing input.
- No empty heartbeat or task churn is created.

## Context7 Boundary

Use Context7 before Plane API usage, schema setup, project configuration, or automation. Local GTD classification does not require Context7.

## Alignement Plan fancy-hugging-bengio.md (2026-06-21)

**Anchor canon** : `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md`

- **§3.5** (Couche 4 — Hiérarchie Business OS) : GTD (Cerritos Holodeck) = bus horizontal qui boucle les 2 triptyques (MORTY 12WY⊃PARA⊃DEAL + BETH Ikigai⊃Life Wheel⊃Muse) vers B1 Fractal. Position canon = **A1 Morty Focus → A2 USS Cerritos → A3 5 Airlock (Mariner/Boimler/Rutherford/Tendi/Freeman)**.
- **§3.6** (Routage par intention A0) : intentions A0 `Capture idée brute` (→ Mariner `/aside`), `Clarifier` (→ Boimler `/plan`), `Today focus` (→ SNW Ortegas `/plan`) routing canon A0 → A1 Morty → A2 Cerritos.
- **§3.7** (State.json pattern) : bus d'état sémantique entre agents. Chaque transition A3 écrit dans `00_Amadeus/40_SYMPHONY_BUS/state.json`. Pattern remplace UI visuelle n8n.
- **§15.1 row 1** (D3 nuance) : `fancy-hugging-bengio.md` mappait initialement Tendi = Organize (gap détecté par 26 Explore sub-agents swarm 2026-06-21). **Canon local actif** (résolu 2026-05-20) garde **Rutherford = Organize + Tendi = Review**. Le canon twin `A2_HoloDeck_Cerritos_Spec.twin.md` confirme.
- **§15.2 row 10** (gap L0 ADR) : `ADR-GTD-001 Cerritos 5 stages canon` à créer (post-cycle foundering, Q3 2026). Cette spec sert d'input à la rédaction.

**Workflow canon (D1 receipt = `fancy-hugging-bengio.md §3.3`)** :

```
A0 intention (court terme / exécution)
  ↓
[A1 Morty] ← filtre focus (budget tokens, priorité cycle, scope)
  ↓
[A2 Cerritos GTD] ← workflow 5 stages canon
  ├─ Mariner (Capture)     → state.json: "captured"
  ├─ Boimler (Clarify)     → state.json: "clarified" + tag
  ├─ Rutherford (Organize) → state.json: "organized" + bucket PARA
  ├─ Tendi (Review)        → state.json: "reviewed" + drift check
  └─ Freeman (Engage)      → state.json: "engaged" + next_action
```

Cette spec A2 = source de vérité canonique terrain, **prevaut** sur `fancy-hugging-bengio.md §15.1` tant que A0 n'inverse pas explicitement le mapping A3 (D4 append-only, pas d'auto-réécriture).
