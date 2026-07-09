# Morty Global Queue

> Layer: L1 Life OS
> Owner: A1 Morty
> Purpose: executable handoff queue for CLI agents
> Status: SHADOW_ACTIVE

This folder is Morty's relay queue. It stores executable Context Packs and dry-runs that can be resumed by Claude Code, Codex, Gemini, or Antigravity CLI without depending on the quota or memory of the previous harness.

Morty is the terminal executor/router. Morty does not choose priorities and does not create Rocks from nothing. Morty only executes Beth-cleared work.

## Accepted Items

- Complete Context Packs with `beth_clearance`.
- Dry-run proposals awaiting A0/Beth approval.
- Blocked execution records that state the missing field.
- Handoff notes for a partially executed workflow.

## Rejected Items

- Raw ideas. Send those to Plane/GTD or Cerritos capture.
- Beth decisions. Send those to `Beth_Alignment_Log/`.
- Sunday review material. Send that to `Sunday_Uplink_Protocols/`.
- Any secret value.

## File Naming

Use one file per execution unit:

```text
YYYY-MM-DD_HHMM_morty-<framework>-<short-slug>.md
```

Examples:

```text
2026-05-20_0930_morty-12wy-baserow-rock-dryrun.md
2026-05-20_1015_morty-gtd-plane-inbox-clarify.md
```

## Required Execution Shape

```markdown
---
type: morty_queue_item
status: READY | DRY_RUN | BLOCKED | IN_PROGRESS | DONE | NEEDS_BETH
created_at: YYYY-MM-DDTHH:MM:SS-04:00
created_by: Claude_Code_CLI | Codex_CLI | Gemini_CLI | Antigravity_CLI
handoff_to: any | Claude_Code_CLI | Codex_CLI | Gemini_CLI | Antigravity_CLI
beth_clearance: GREEN | ORANGE
framework: Ikigai | ZORA | 12WY | PARA | GTD | DEAL | Symphony
target_surface: Baserow | Obsidian | Plane | Affine | Local_Files | Symphony
external_write_requires_signoff: true
evidence_paths:
  - C:\Users\amado\ASpace_OS_V2\...
output_artifact: C:\Users\amado\ASpace_OS_V2\...
---

# Morty Queue — <short title>

## Context Pack

Copy the relevant fields from `..\ContextPack.template.yml`.

## Command Plan

List commands or tool steps. For external systems, dry-run first.

## Execution Log

Append timestamped events. Never paste secret values.

## Handoff State

State exactly what the next CLI should do.

## Verification

List checks run and proof paths.

## Residual Risk

State what remains unsafe or unverified.
```

## Routing Matrix

| Framework | Primary surface | Default harness |
|---|---|---|
| ZORA / Life Wheel | Baserow LD00 | Gemini CLI or Codex CLI read-only |
| 12WY | Baserow Warp Core | Gemini CLI for synthesis, Codex for local docs |
| PARA | Obsidian / filesystem | Codex CLI or Antigravity CLI |
| GTD | Plane | Gemini CLI or Claude Code on MiniMax once auth is valid |
| DEAL | Affine | Claude Code on MiniMax or Gemini CLI |
| Symphony orchestration | Local specs / adapters | Codex CLI for docs, Claude/Gemini for long runs |

This table is operational doctrine, not a technical claim about provider capabilities. Revalidate current CLI/provider details before changing live configs.

## Quota-Agnostic Handoff

If a harness hits quota:

1. Mark current item `BLOCKED` or `IN_PROGRESS`.
2. Add `handoff_to: any` unless a specific harness is required.
3. Write the last safe command, last proof, and next reversible step.
4. Do not compress the whole conversation into the task. Link evidence paths instead.
5. The next CLI reads this file, `..\A1_Morty_Spec.md`, and `..\A1_Beth_Spec.md`.

## Context7 Boundary

Use Context7 or official docs before changing live external tool configuration, provider settings, MCP servers, SDK calls, or CLI syntax. For local file relay and dry-run planning, local evidence is enough.

## Alignement Plan fancy-hugging-bengio.md (2026-06-21)

> **D1 receipt** : cette queue est alignée avec le plan canonique `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` (§3.5 Doctrine Life OS + §3.6 Matrice routage 20 intentions + §3.7 State.json bus + §4 Cycle 12WY Q3 2026).

- **Routing distribué 6 ships** : Morty route les Context Packs vers les 6 A2 engines selon la matrice canon du plan §3.6 (20 intentions A0 → A1 → A2 → A3 → frame → commande CC). Le plan §3.5 simplifie Morty = "12WY+PARA+GTD" comme **responsabilité principale**, pas exclusivité.
- **ContextPack.template.yml alignement §3.7** : champs canon à ajouter au YAML pour cohérence state.json bus — `cycle: Q3-2026`, `week: W<n>`, `12wy_discipline`, `life_wheel_domain`, `tokens_used`, `tokens_budget`, `drift_flag`, `raw_input_hash`, `raw_input_preview`, `next_step`. (Workstream à part, pas dans cette session.)
- **Bus d'état state.json** : chaque exécution Morty terminée écrit dans `C:\Users\amado\ASpace_OS_V2\00_Amadeus\40_SYMPHONY_BUS\state.json` (`stage: executed` + `agent_path` + `next_step` + `evidence_paths`). Hook `mariner-capture.ps1` capture l'intention A0 upstream.
- **Cycle 12WY Q3 2026** : 12 items canon (plan §4). Items routés par Morty vers A3 twins : Item 3 Stamets (auto-research IA), Item 4 Data (TOKEN frugalité), Item 5 Spock (YouTube PARA), Item 6 Mariner (Hermes), Item 7 Geordi (Agent OS), Item 8 Picard+Spock (Business OS), Item 10 Picard (Solaris/OMK/ABC), Item 11 Rok-Tahk+Zero (VPS Memory core DEAL), Item 12 Tilly (auto-amélioration).
- **D7 cost-of-escalation** : Morty ne remonte JAMAIS à A0 mid-execution. Si drift_flag: true dans state.json, Beth décide au Sunday Uplink suivant (pas d'escalade synchrone).
- **Quotas MiniMax + Hermes + Codex + Gemini** : le `handoff_to: any` par défaut supporte le relais inter-CLI. Si quota MiniMax tombe, Codex CLI ou Gemini CLI reprennent (cf. routing matrix §"Routing Matrix" du plan `fancy-hugging-bengio.md §3.6`).
