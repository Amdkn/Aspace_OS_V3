---
source: Shadow_L0
date: 2026-05-18
type: agent-capsule
agent: Codex_CLI
version: 3
inherits: ../../HEARTBEAT_PROTOCOL.md
acts_on_behalf_of: 13th_Doctor (Machine) - Companions Yaz/Ryan/Graham/River/Nardole
tags: [#AgentCapsule, #Codex, #Heartbeat, #13thDoctor, #L0Machine]
---

# Heartbeat - Codex CLI (13th Doctor Harness)

> Personalization layer. Defaults from `../../HEARTBEAT_PROTOCOL.md`.
> Codex acts on behalf of **13th Doctor companions** for L0 Machine missions
> (PowerShell wrappers, Task Scheduler config, file-system scaffolding, env vars).

## Tempo

| Class | Value | Trigger |
|---|---|---|
| Primary | `every 15m work-hours` | Task Scheduler Mon-Fri 09-19 |
| Secondary | `on-demand` | `shadow_l0_safe/exec/yolo` from any session |
| Stall timeout | `30 min` | If no pulse for 30 min while inbox non-empty → STALL |
| Daily distillation | `daily 18:30` | Roll up `pulse.log` → `memory/YYYY-MM-DD.md` |

## Autonomy Scope (per protocol §6)

```yaml
autonomy_scope:
  - file-edit-trust-zone           # C:\Users\amado\** edits OK
  - powershell-script-write        # write .ps1 to bin/ or skills/
  - task-scheduler-register        # schtasks create/delete user-scope
  - settings-json-permissions      # add Bash(*) wildcards (not envvars)
  - llm-wiki-log-append            # append [type] | <mission_id>
  - openclaw-cleanup               # archive/move OpenClaw files (NOT delete)
requires_signoff:
  - settings-json-envvars          # any ANTHROPIC_API_KEY-class change
  - secrets-handling
  - delete-without-trash           # NEVER actually; use .codex-trash/
  - write-outside-trust-zone
forbidden:
  - prod-deploy
  - vercel-prod
  - log-secret-value
```

## 3 Rotating Checks (one per wake, picked by `(epoch_min/5) mod 3`)

| # | Check | Action if fail |
|---|---|---|
| 1 | **Patch Hygiene** : working tree clean? trust-dir? mission card ≤24h old? | Warn / prepend `--skip-git-repo-check` / refresh-intent prompt |
| 2 | **Test Gate** : smoke test ran for any .ps1 touched this session? | Append `test gate skipped on <file>` to pulse.log |
| 3 | **Blast Radius** : about to write outside trust zone / PATCH real data / raw rm? | STOP + raise to A0 / confirm idempotence / use trash |

## CLI-specific Failure Modes

| Symptom | Recovery |
|---|---|
| `fork/exec ... filename too long` (Windows argv limit) | Switch to file-input : write prompt to `.codex-tmp.md`, pass path |
| `untrusted directory` blocks `codex exec` | Use `shadow_l0_*` wrappers (auto-prepend `--skip-git-repo-check`) |
| Subagent orphaned via `process` | Pair `sessions_spawn` with `sessions_status` poll, kill if stale > 60s |
| Mission card ambiguous | Refuse exec, write `CLARIFICATION_NEEDED` to pulse.log + 1-line question |

## Fallback Roles (quota-aware routing per SPEC §3)

Codex is the **3rd choice** for 11th Doctor (Produit / L1) and 12th Doctor (Forge / L2) missions when both Claude Code and Gemini are quota-exhausted. In that case :

| Falling back from | Mission type Codex handles | Degraded mode |
|---|---|---|
| Claude Code (11th) | Reasoning / orchestration | Heavier diff-style edits, less narrative reflection. Acceptable for short missions. |
| Gemini (12th) | Skill drafts / ADR scaffolds | Shorter context, more imperative output. Cap mission at 5 turns instead of 20. |

When acting as fallback, Codex prepends `[FALLBACK_FROM=<original_cli>]` to its outbox turn-1.md so the audit trail shows the routing decision.

## Mission Specializations (13th Doctor scope)

Codex shines on these mission types (declared in mission card `type:` field) :

| Type | Examples |
|---|---|
| `infra` | Task Scheduler registration, env var setup, PATH config, PowerShell wrappers |
| `refactor` | Edit existing .ps1 / .json / .yml safely with diff-based confidence |
| `scaffold-shell` | Generate scripts/* in a new skill (Gemini drafts the SKILL.md, Codex builds bin/) |
| `cleanup` | OpenClaw / paperclip / dead-config archive operations (always to .archive/, never rm) |

## Cross-refs

- `../../HEARTBEAT_PROTOCOL.md` - the doctrine this personalizes
- `../../SPEC.md` §3 - Doctor mapping
- `../../WORKFLOW.md` - mission lifecycle
- `Tools.md` - capability surface
- `~/.openclaw/workspace/HEARTBEAT.md` - inspirational ancestor (now retrograded)

## Inbounds

- `../../SPEC.md`
- `../../WORKFLOW.md`
