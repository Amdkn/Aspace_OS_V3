---
name: l2-e2e-pr
description: >
  End-to-end smoke test for a PR on abc-os-community (or sibling Next.js app)
  before merge. USE THIS SKILL whenever the user (A0) wants to: smoke-test a
  PR, verify a build is safe to merge, run a quick E2E on the critical user
  flows, catch console errors / 404s / auth walls before the human reviewer
  sees the PR, or close the "Flash review" gate. Bakes in MCP interactive
  preference (Playwright MCP for stateful browser runs — needs persistent
  context across navigation, screenshot, console check), Flash / Product
  mapping (SOA04_PRODUCT / Flash / Avengers), the abc-os-community critical
  paths (`/`, `/login`, `/dashboard`, `/community`, `/build-hub`), per-PR
  isolation (each PR gets a fresh ephemeral preview URL — never run E2E
  against the same preview as a previous PR), D1 proof (paste the
  Playwright MCP output, not "looks good"), no console errors tolerated
  (block merge on any error level message), HITL gate on merge (never auto-
  merge — this skill produces a report for A0/human reviewer), and the
  4-file writeback contract. L2 = Business OS / Product.
when_to_use: |
  - User says "smoke test the PR", "E2E the build", "Flash review", "ready to merge?"
  - A Vercel preview deployment just completed for a PR branch
  - A0 wants to validate a feature before the human reviewer looks
  - The "auto-merge" candidate list needs verification
inputs: |
  1. PR URL or preview deployment URL
  2. Implicit: A0 wants PASS/FAIL per critical path, with observed evidence
  3. Optional: focus area (e.g. "test the new /build-hub view specifically")
outputs: |
  1. 1 markdown report at `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/reports/l2_e2e_pr_<PR#>.md`
  2. PASS/FAIL per critical path with screenshot + console log
  3. Append 1 line to `wiki/log.md` with the report path
  4. **NEVER auto-merge** — surface verdict, wait for A0
---

# /l2-e2e-pr — Pre-merge E2E smoke test

> **Doctrine** : L2 = Business OS / Product. Flash = SOA04 manager, Avengers
> = B3 squad. E2E is INPUT to merge, not the merge itself.
>
> **Canon refs** : `concept_l2_fractal_b1b2b3.md` ·
> `00_Business_OS/10_Projects/abc/CLAUDE.md` (Vercel contract) ·
> Vercel `AGENTS.md` (env vars).

## When to trigger

| Signal | Action |
|---|---|
| A0 says "smoke test the PR" / "E2E the build" | Run for the named PR |
| Vercel preview deployment just completed | Run the 5-step gate (see below) |
| A0 says "ready to merge?" | Run, surface verdict, wait for GO |
| A0 says "Flash review" | Same as above — Flash is the SOA04 manager |
| Auto-merge workflow asks for verification | Run, return verdict as JSON |

## MCP interactive — Playwright (the right tool here)

Why MCP, not CLI? E2E needs **stateful browser context** across multiple
tool calls: navigate → snapshot → click → screenshot → console check.
Playwright MCP keeps the browser alive between tool calls. CLI `npx
playwright test` requires writing a script first and is overkill for 5-step
smoke.

```text
mcp__playwright__browser_navigate url=<preview_url>
mcp__playwright__browser_snapshot
mcp__playwright__browser_console_messages level=error
mcp__playwright__browser_take_screenshot filename=pr_<N>_home.png

# Repeat for each critical path
mcp__playwright__browser_navigate url=<preview_url>/login
... etc
```

## The 5-path smoke test (canonical for abc-os-community)

| # | Path | What to check | PASS criterion |
|---|---|---|---|
| 1 | `/` (landing) | Page renders, no 404, expected `<h1>` text | Sentinel string present in snapshot |
| 2 | `/login` | Auth wall renders, no console error | Page loads, console clean |
| 3 | `/dashboard` | Auth-redirect or content renders | 200 + expected dashboard chrome |
| 4 | `/community` | Community hub renders | Expected community view text present |
| 5 | `/build-hub` | Build hub renders (NOT `/build` — Vercel reserves it) | Expected build-hub view text present |

**Path swap rule** : if the PR changes one of these paths (e.g. adds a new
view), swap the changed path IN and one of the others OUT (cap = 5 paths).
Document the swap in the report.

**Vercel `/build` guard** : NEVER test `/build` directly — Vercel reserves
this route. Use `/build-hub`. The fact that an E2E tries to hit `/build` is
itself a FAIL.

## Per-path checks

For each of the 5 paths, the skill runs:

1. **`browser_navigate`** to the path
2. **`browser_snapshot`** — capture the accessibility tree, look for the
   sentinel string (path-specific `<h1>` or a stable text)
3. **`browser_console_messages level=error`** — assert NO error-level
   messages (warn and info are OK; error is not)
4. **`browser_take_screenshot`** — save to `wiki/reports/screenshots/pr_<N>_<path>.png`

If any of the 4 sub-checks fails, that path = FAIL.

## Report structure

Path: `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/reports/l2_e2e_pr_<PR#>.md`

```markdown
---
report_type: l2_e2e_pr
pr: <PR# or branch>
preview_url: <url>
date: YYYY-MM-DD
agent: <session id>
verdict: PASS | FAIL | PARTIAL
---

# E2E Smoke Test — PR #<N>

## TL;DR

<1 line: PASS / FAIL / PARTIAL (X/5 paths), with the failing path if any>

## Per-path results

### `/`

- **Status**: PASS | FAIL
- **Snapshot**: <expected sentinel string present?>
- **Console**: <N errors, top 3 quoted>
- **Screenshot**: `wiki/reports/screenshots/pr_<N>_home.png`

### `/login`

- **Status**: ...
- **Snapshot**: ...
- **Console**: ...
- **Screenshot**: ...

### `/dashboard`

- **Status**: ...

### `/community`

- **Status**: ...

### `/build-hub`

- **Status**: ...

## Console errors (all paths, filtered)

<aggregated list, deduplicated>

## Vercel `/build` guard

- Checked: yes | no
- If yes: result

## Suggested next step

<1-2 sentences: "All GREEN — ready to merge" or "FAIL on /build-hub: console
error 'X' — investigate before merge" or "PARTIAL: 3/5 paths pass, swap
/build-hub for the new view <name> and re-run">
```

## Critical constraints

| Constraint | Enforcement |
|---|---|
| Per-PR isolation | Each run uses a fresh preview URL — never reuse from previous run |
| Never test `/build` | Vercel reserves this route; if a test hits it, that's a FAIL |
| Never auto-merge | Surface verdict, wait for A0 GO |
| D1 proof | Every PASS/FAIL backed by the Playwright MCP output in context |
| Screenshots saved | All 5 paths get a PNG, regardless of PASS/FAIL |
| Console errors block | Any error-level message on any path = that path = FAIL |
| No secrets in screenshots | If a screenshot captures an API key in the URL, redact before writing |

## Anti-patterns (do NOT)

| Anti-pattern | Why | Fix |
|---|---|---|
| Use `npx playwright test` for 5 paths | Overkill, slow, requires writing a script | Use Playwright MCP interactive |
| Mark PASS without checking console | Hidden runtime errors slip through | Always check `browser_console_messages` |
| Auto-merge on PASS | HITL violation | Surface verdict, wait |
| Reuse a previous PR's preview URL | Stale state, false confidence | Always re-query `list_deployments` for the latest |
| Test `/build` directly | Vercel reserves it — `/build` returns 404, not your code | Test `/build-hub` |
| Skip the screenshot on PASS | Can't review later | Always take it |
| Use Lighthouse as the only check | Lighthouse = perf, not functional | Combine with sentinel + console check |

## See also

- `00_Business_OS/10_Projects/abc/CLAUDE.md` — Vercel contract + critical paths
- `10_Tech_OS/.../04_vercel/AGENTS.md` — Vercel env var rules
- `/l0-deploy-verify` — the L0 analog (full surface, not per-PR)
- `/l2-competitor-pulse` — L2 Growth pulse
- `/l2-linkedin-prospect` — L2 Sales pulse
- `wiki/reports/l2_e2e_pr_*.md` — accumulated history
