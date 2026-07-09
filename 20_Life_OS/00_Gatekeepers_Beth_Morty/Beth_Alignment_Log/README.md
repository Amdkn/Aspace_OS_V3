# Beth Alignment Log

> Layer: L1 Life OS
> Owner: A1 Beth
> Purpose: relay-safe decision, veto, and alignment handoff between CLI agents
> Status: SHADOW_ACTIVE

This folder is Beth's handoff ledger. It stores decisions that must survive quota limits, harness changes, and agent rotation across Claude Code, Codex, Gemini, and Antigravity CLI.

Beth is the Life OS filesystem conscience. A CLI agent may continue a Beth decision only by reading the newest alignment record here, then checking `A1_Beth_Spec.md`.

## What Belongs Here

- Beth veto records.
- ZORA / LD03 / LD04 health and cognition risk decisions.
- PRD-L1 go/no-go notes.
- Cross-layer overrides where L2 urgency must stop because Life OS coherence is at risk.
- Alignment handoffs from Claude, Codex, Gemini, or Antigravity CLI.

## What Does Not Belong Here

- Raw tasks or todo lists. Send those to `Morty_Global_Queue/`.
- Weekly review rituals. Send those to `Sunday_Uplink_Protocols/`.
- Secrets, API keys, cookies, tokens, or credential values.
- External tool mutation logs. Store only proof paths and outcomes.

## Record Naming

Use one file per decision:

```text
YYYY-MM-DD_HHMM_beth-<short-slug>.md
```

Examples:

```text
2026-05-20_0845_beth-ld04-overload-veto.md
2026-05-20_0910_beth-life-os-greenlight.md
```

## Required Record Shape

```markdown
---
type: beth_alignment
status: GREEN | ORANGE | RED | HALT_LD03 | HALT_LD04
created_at: YYYY-MM-DDTHH:MM:SS-04:00
created_by: Claude_Code_CLI | Codex_CLI | Gemini_CLI | Antigravity_CLI
handoff_to: any | Claude_Code_CLI | Codex_CLI | Gemini_CLI | Antigravity_CLI
related_context_pack: ../ContextPack.template.yml
evidence_paths:
  - C:\Users\amado\ASpace_OS_V2\...
---

# Beth Alignment — <short title>

## Decision

State the decision in one paragraph.

## Why

Explain the Life OS reason: health, cognition, priority, coherence, or evidence.

## Evidence

List exact local paths, Baserow table names, Plane issue names, Obsidian notes, or LLM Wiki entries. If evidence is missing, mark it `HYPOTHESIS`.

## Relay Instructions

Tell the next CLI agent what to read and what not to do.

## Residual Risk

Name the risk left open.
```

## CLI Relay Protocol

1. Read latest file in this folder.
2. Read `..\A1_Beth_Spec.md`.
3. If status is `RED`, `HALT_LD03`, or `HALT_LD04`, do not execute through Morty.
4. If status is `ORANGE`, only draft or request missing proof.
5. If status is `GREEN`, create or update a Context Pack for Morty.
6. Append a durable summary to LLM Wiki only when the decision changes doctrine or state.

## Harness-Agnostic Rule

The decision is Beth's, not the harness's. A handoff remains valid when moving from Claude Code to Codex, Gemini, or Antigravity CLI as long as:

- the evidence paths are readable;
- no secret is required;
- the next action stays inside the cleared scope;
- Morty receives a complete Context Pack before execution.

## Context7 Boundary

No Context7 lookup is required for local Beth decisions. Use Context7 or official docs only when the decision depends on current external tool behavior, provider config, SDK syntax, MCP setup, or CLI documentation.

## Alignement Plan fancy-hugging-bengio.md (2026-06-21)

> **D1 receipt** : ce log est aligné avec le plan canonique `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` (§3.5 Doctrine Life OS + §3.6 Matrice routage + §3.7 State.json bus + §3.8 Anti-paperclip Saru 1000T).

- **Champ state.json obligatoire** : tout fichier `beth-<short-slug>.md` créé ici doit référencer une écriture dans `C:\Users\amado\ASpace_OS_V2\00_Amadeus\40_SYMPHONY_BUS\state.json` avec `status: GREEN|ORANGE|RED|HALT_LD03|HALT_LD04` (cohérent avec le frontmatter `status` du record).
- **Veto distribué 6 ships** : Beth peut décider sur les 6 A2 engines. Référencer le ship dans `evidence_paths` du record (ex: `symphony/L1/lane_A_specs/03_A3_crews/<ship>/<crew>.twin.md`).
- **Anti-paperclip Saru** : toute décision Beth touchant LD02 Finance doit inclure une note explicite sur les 3 garde-fous canon (Book LD01 boundary + Musk pivot agency over utopia + Wonder Woman v4 horizon ladder F13-F18).
- **Cycle 12WY Q3 2026** : 12 items canon (plan §4). Items déclenchant Beth GREEN = items 3 (auto-research IA Stamets), 6 (Hermes Mariner), 8 (Business OS Picard), 9 (structuration A3), 10 (Solaris/OMK/ABC Picard), 11 (VPS Memory core Rok-Tahk+Zero), 12 (auto-amélioration Tilly). Items déclenchant Beth ORANGE = items 1-2 (terrain A0), 4 (TOKEN frugalité), 5 (YouTube PARA Spock), 7 (Agent OS Geordi).
- **A0 board observer** : escalade Beth → A0 uniquement aux milestones W1/W2/W3/W4 (4 fois max par cycle). Hors milestone = drift_flag: true dans state.json.
- **HARD SAFETY** : tout `status: HALT_LD03` ou `HALT_LD04` doit contenir une path d'évidence Culber (LD03) ou Tilly (LD04) respectivement.
