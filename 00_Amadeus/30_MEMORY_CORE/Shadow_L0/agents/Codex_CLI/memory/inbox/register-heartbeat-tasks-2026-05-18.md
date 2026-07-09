---
mission_id: register-heartbeat-tasks-2026-05-18
issued_at: 2026-05-18T22:00:00Z
issued_by: Claude_Code_CLI
target_cli: Codex_CLI
on_behalf_of: 13th_Doctor.Yaz
type: infra
priority: H1
turns_budget: 8
autonomy: signoff
related_skills: []
related_docs:
  - 00_Amadeus/30_MEMORY_CORE/Shadow_L0/HEARTBEAT_PROTOCOL.md
  - 00_Amadeus/30_MEMORY_CORE/Shadow_L0/SPEC.md
  - 00_Amadeus/30_MEMORY_CORE/Shadow_L0/WORKFLOW.md
  - ~/.claude/bin/heartbeat-tick.ps1
  - ~/.claude/bin/heartbeat-watchdog.ps1
---

# Mission - Register Heartbeat Tasks in Windows Task Scheduler

## Intent

Bootstrap the Shadow L0 mesh by creating the Windows Task Scheduler entries that fire `heartbeat-tick.ps1` and `heartbeat-watchdog.ps1` at their declared tempos. This is the **first real Mission Card** — its successful execution is the proof that the protocol works end-to-end.

A0 must not invoke `schtasks` himself (50/30/20 rule, L0 work). 13th Doctor companion Yaz handles Machine layer config.

## Constraints

- **User scope only** (no admin elevation). Use `schtasks /CREATE /SC ... /RU "%USERNAME%" /RL LIMITED`
- **Idempotent**. If a task with the target name already exists, `/DELETE /F` first, then `/CREATE`. Don't fail on pre-existing.
- **Path safety** : full absolute path to `powershell.exe` + full absolute path to the `.ps1` script. Quote everything with apostrophes in the surrounding path (`C:\Users\amado\...` has no spaces, but be safe).
- **No logging of secrets**. The tasks pass only the agent name; no API keys touched.
- **Trust zone respected** : all task actions stay within `C:\Users\amado\`.

## Inputs

Read these before execution :

1. `00_Amadeus/30_MEMORY_CORE/Shadow_L0/HEARTBEAT_PROTOCOL.md` §8 (Tempo Conventions) — to confirm declared cadences match
2. `Shadow_L0/agents/<CLI>/Heartbeat.md` §Tempo per agent — for the exact `Primary` value of each
3. `~/.claude/bin/heartbeat-tick.ps1` — verify it accepts `-Agent <name>` parameter (it does)
4. `~/.claude/bin/heartbeat-watchdog.ps1` — verify it runs without args (it does)

## Acceptance Criteria

After execution, `schtasks /Query /FO LIST /V` filtered on the names below should list **4 active tasks** :

- [ ] `ASpace-Heartbeat-Codex` — every 15min, Mon-Fri 09:00-19:00, action = `powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\amado\.claude\bin\heartbeat-tick.ps1 -Agent Codex_CLI`
- [ ] `ASpace-Heartbeat-Gemini` — every 30min, Mon-Fri 09:00-19:00, action = `powershell ... -File ... -Agent Gemini_CLI`
- [ ] `ASpace-Heartbeat-ClaudeCode` — every 60min, Mon-Fri 09:00-19:00, action = `powershell ... -File ... -Agent Claude_Code_CLI`
- [ ] `ASpace-Heartbeat-Watchdog` — every 5min, 24/7, action = `powershell ... -File C:\Users\amado\.claude\bin\heartbeat-watchdog.ps1`

After the first natural fire (or manual trigger via `schtasks /Run`), the `pulse.log` of each agent and `watchdog.log` should contain at least one `HEARTBEAT_OK` line.

## Out of Scope

- Configuring the daily distillation tasks (`daily 18:30 Codex` and `daily 06:00 watchdog deep`). Mission for a follow-up card.
- Wiring Telegram MCP notifications from the watchdog (TBD).
- Cron-style override (Windows Task Scheduler is sufficient for v1).
- Modifying `heartbeat-tick.ps1` or `heartbeat-watchdog.ps1` (already validated, don't touch unless a syntax error surfaces in your Turn-1 dry-run).

## Recommended Approach

1. **Dry-run first** : `schtasks /Query /FO LIST | findstr ASpace-Heartbeat` to see if any pre-existing entries conflict. Report findings before destructive action.
2. **Compose the 4 `schtasks /CREATE` invocations** as a single PowerShell function for re-use (idempotent register helper).
3. **Run** the function, capturing output to `outbox/<mission-id>/turn-1.md`.
4. **Verify** with a fresh `/Query` — paste the list of 4 tasks in the output.
5. **Trigger one manually** via `schtasks /Run /TN ASpace-Heartbeat-Codex` and confirm `pulse.log` got an entry.

## Terminal Markers

- `<NEEDS_REVIEW>` — preferred. A0 reviews the schtasks list before the first auto-fire. Since `autonomy: signoff`, this mission **must** end with `<NEEDS_REVIEW>` so A0 confirms before the mesh runs unattended.
- `<ESCALATE>` if `schtasks` blocks (admin required for some operations) or `powershell.exe` can't be located on the default PATH.

Do NOT emit `<DONE>` — by design A0 owns sign-off on the first activation.

## Routing Note (per HEARTBEAT_PROTOCOL §5)

Preferred CLI : Codex (13th Doctor Machine specialty).
Fallback chain if Codex 429 : Gemini → Claude Code on MiniMax.
Persona invariant : `on_behalf_of: 13th_Doctor.Yaz` regardless of executor.

## A0 Sign-off Gate

When you reach `<NEEDS_REVIEW>`, the outbox moves to `Shadow_L0/A0_inbox/`. At A0's next session, Claude Code will surface this for sign-off. Approval triggers a follow-up mission to `Trigger ASpace-Heartbeat-* tasks once each and verify pulse.log writes`.
