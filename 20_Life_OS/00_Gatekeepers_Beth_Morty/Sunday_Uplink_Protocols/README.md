# Sunday Uplink Protocols

> Layer: L1 Life OS
> Owners: A1 Beth + A1 Morty
> Purpose: weekly relay checkpoint between human review and CLI execution
> Status: SHADOW_ACTIVE

This folder stores the weekly Life OS uplink protocol. It is the handoff ritual that lets any CLI agent resume the week without asking A0 to re-explain Life OS, Baserow, Plane, Obsidian, Affine, or the current quota situation.

Sunday Uplink is not a report factory. It is a short control loop:

```text
Beth reviews alignment -> Morty prepares executable queue -> A0 decides -> next CLI executes
```

## Weekly File Naming

Use one file per weekly uplink:

```text
YYYY-WW_sunday-uplink.md
```

Example:

```text
2026-W21_sunday-uplink.md
```

## Required Weekly Shape

```markdown
---
type: sunday_uplink
week: YYYY-WW
created_at: YYYY-MM-DDTHH:MM:SS-04:00
created_by: Claude_Code_CLI | Codex_CLI | Gemini_CLI | Antigravity_CLI
status: DRAFT | READY_FOR_A0 | A0_REVIEWED | CLOSED
handoff_to: any | Claude_Code_CLI | Codex_CLI | Gemini_CLI | Antigravity_CLI
evidence_paths:
  - C:\Users\amado\ASpace_OS_V2\...
---

# Sunday Uplink — YYYY-WW

## 1. Beth Alignment

- Current Beth state: GREEN | ORANGE | RED | HALT_LD03 | HALT_LD04
- Vetoes:
- Health / LD03:
- Cognition / LD04:
- Priority conflict:

## 2. Morty Execution Queue

- Ready:
- Blocked:
- Needs Beth:
- Needs A0:

## 3. Shadow L1 Surface Check

| Surface | State | Proof |
|---|---|---|
| Baserow / ZORA / 12WY | unknown | path or note |
| Obsidian / PARA | unknown | path or note |
| Plane / GTD | unknown | path or note |
| Affine / DEAL | unknown | path or note |
| LLM Wiki | unknown | path or note |

## 4. Quota / Harness State

| Harness | Role this week | State |
|---|---|---|
| Claude Code on MiniMax | long execution / L2 style loops | unknown |
| Codex CLI | local implementation / docs / audit | unknown |
| Gemini CLI | long-context synthesis / L1 bridge | unknown |
| Antigravity CLI | emerging harness / UI-assisted local work | unknown |

## 5. A0 Decision Required

List only decisions A0 must make. Everything else should be a Morty queue item.

## 6. Next Handoff

Tell the next CLI exactly which file to open first.
```

## Cadence

- Draft Sunday Uplink before the review.
- Close it after A0 chooses priorities.
- Convert only the executable next actions into `Morty_Global_Queue/`.
- Convert only veto/alignment decisions into `Beth_Alignment_Log/`.
- Log durable doctrine changes in LLM Wiki.

## No-Empty-Uplink Rule

Do not create a weekly uplink if there is no new state. Instead, append a one-line `NO_CHANGE` note to the previous weekly file.

## Handoff Between CLI Agents

When Claude, Codex, Gemini, or Antigravity reaches quota or needs to stop:

1. Update the current weekly uplink `Handoff` section.
2. Link the active Beth decision and Morty queue item.
3. Mark unresolved external docs/config claims as `NEEDS_CONTEXT7`.
4. Avoid pasting long chat history. Link files and summarize the next action.
5. The next CLI starts from the weekly uplink, then Beth, then Morty.

## Context7 Boundary

Sunday Uplink may mention external tools, but it should not claim current API behavior without Context7 or official docs. Use `NEEDS_CONTEXT7` when a future agent must verify provider, MCP, SDK, or CLI details before acting.

## Alignement Plan fancy-hugging-bengio.md (2026-06-21)

> **D1 receipt** : ce protocole est aligné avec le plan canonique `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` (§3.5 Doctrine Life OS + §3.7 State.json bus + §4 Cycle 12WY Q3 2026 + §8.3 A0 board observer + §10 Risques).

- **Bus d'état state.json** : chaque Sunday Uplink doit inclure un snapshot de `C:\Users\amado\ASpace_OS_V2\00_Amadeus\40_SYMPHONY_BUS\state.json` (cycle + week + stage + drift_flag + tokens_used). Le Sunday Uplink n'est plus une review subjective mais un **checkpoint machine à états** (plan §3.7).
- **Cycle 12WY Q3 2026 cadence** : 4 Sunday Uplinks canon par cycle (W1 fin 07/05, W2 fin 07/26, W3 fin 08/16, W4 fin 09/07). Items 1-2 livrés W1, items 3-4 W2, items 5-6 W3, items 7-12 W4 (plan §4 + §8.2).
- **A0 = board observer (plan §8.3)** : A0 valide **uniquement** les milestones W1/W2/W3/W4 (4 décisions par cycle max). Sunday Uplink escalade à A0 uniquement quand `drift_flag: true` OU milestone atteint. Pas d'escalade quotidienne.
- **Triptyque imbriqué (plan §3.1)** : Sunday Uplink doit refléter l'état des 2 triptyques (Morty 12WY⊃PARA⊃DEAL + Beth Ikigai⊃Life Wheel⊃Muse) + GTD bus horizontal. Section `§3 Shadow L1 Surface Check` devient la jauge d'alignement des 6 frameworks.
- **AaaS 3 variants (plan §3.4)** : Sunday Uplink note l'état des 3 variants AaaS (Solaris Book H1 / Nexus-OMK Saru H3 / Orbiter-ABC Burnham H10) + 1 dormant (LD03+LD04 Family/Home). Cohérent avec `J03_Jerry_Nexus_LD02_LD06_Finance_Family | FIP STANDARD` canon.
- **5 ADRs Life OS framework manquants** (gap L0 plan §15.2 #10) : ADR-DEAL-001, ADR-GTD-001, ADR-PARA-001, ADR-LIFE-WHEEL-001, ADR-SYMPHONY-001 — ratifier avant Item 11 (avant 2026-09-07). Sunday Uplink peut proposer l'amendement DDD/CODE lié.
- **No-empty-uplink rule** renforcé : un uplink vide = Sunday passé sans action n'est PAS créé. Append `NO_CHANGE` au précédent. Mais un uplink `READY_FOR_A0` doit OBLIGATOIREMENT contenir une référence state.json + un path d'évidence Culber (LD03) ou Tilly (LD04) si HALT.
