---
session: agent-ab1dc3701cb3ae15a
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\de35c5f1-6944-47f6-b8bc-849452b0313a\subagents\agent-ab1dc3701cb3ae15a.jsonl
debut: 2026-07-25T09:40:30.191Z
fin: 2026-07-25T09:43:09.257Z
messages_utilisateur: 1
reponses_assistant: 3
titre: "Read-only QA pass in C:\\Users\\ado/coach-os (nested git repo). Do not edit, commit, or push. Fan out via Task t…"
---

## >>> UTILISATEUR #1

Read-only QA pass in C:\Users\ado/coach-os (nested git repo). Do not edit, commit, or push. Fan out via Task tool if available; otherwise run independent reviewers in parallel via the Agent tool.

Objective: confirm the AppFrame hook boundary fix is complete and look for ANY remaining detail-reset / breadcrumb / hooks-of-rules / snag errors across the entire desktop shell. The two touchpoints in scope are:

- src/components/AppFrame.tsx (ActiveRender wrapper with key={active.id})
- src/apps/people/PeopleApp.tsx (render: Fleet alignment)

Constraints:
- Do not propose visual redesigns.
- Do not alter Fleet, useCollectionDrill, WindowContext, or any theme file.
- Do not touch unrelated working-tree files (e.g. src/lib/app-discovery.ts, src/apps/welcome/, pnpm-lock.yaml, .vite-smoke.log).

Tasks (run in parallel via the Task tool if exposed; otherwise spawn subagents with subagent_type=general-purpose to handle each sub-folder):

Sub-agent A — Hook & Render audit:
- Read every file in src/components and src/hooks. For every function/component, list hooks called and the order. Flag any conditional hook, hook after early return, or hook inside a try/catch. Cite file:line, hook name, condition.

Sub-agent B — Detail / breadcrumb contract audit:
- Read every file in src/apps. For each section that opens a detail view, confirm:
  - the detail is registered in WindowContext via setDetail({label, onBack}) OR uses useCollectionDrill, which auto-registers;
  - the closed/open transition cannot leave a stale crumb when sidebar section changes.
- Cross-check AppFrame's navigateToSection: it must call detail?.onBack() before setActiveId.

Sub-agent C — Browser regression coverage:
- Use mcp__playwright__browser_* tools to drive http://localhost:5180. Run the following transitions in this exact order, recording breadcrumb + visible heading + console error count after each:
  1. Open Dashboard → Client Pipeline → click any client card → click Runbooks (Operations)
  2. Open Tasks → Today → click a task → click Upcoming
  3. Open Clients → Active → click Ava Chen → click IP Vault
  4. Open Sales Sanctum → Pipeline → click a deal → click Forecast
  5. Open Product → Roadmap → click a roadmap item → click Specs
  6. Open Legal → Contracts → click a contract → click Policies
  7. Open People / Agents → Fleet → click Orchestrator → click Content (KEY test from previous turn)
  8. Open People / Agents → Fleet → click Scout → click Schedule
  9. Open Welcome → Overview → click any landing page entry → click Back
  10. Open Settings → click Themes → click any theme card → click another app via dock
- For each transition, record: app name, breadcrumb after, heading after, console error count delta. Any "This app hit a snag" overlay is a P0.
- At the end, also test: pressing the same sidebar entry twice (no-op should be safe) and clicking a dock button while a detail is open (detail should close).

Sub-agent D — Console & runtime health:
- browser_console_messages all=true at the end of every other sub-agent's run. Bucket messages by error / warning / log. Re-run sub-agent C if any error appears.

Aggregate your findings into a single report. Format:
- PASS / FAIL summary table (one row per transition).
- For each FAIL: exact file:line, the offending code snippet, the suggested minimum fix (no implementation).
- Final verdict: ready-for-merge iff zero FAILs and zero console errors.

If you find a fix outside what is mentioned, surface it explicitly. Do not bundle redesigns into the "fix" — only call out the structural change required. Under 700 words.

### assistant

I'll start by verifying the target directory exists, then dispatch the four sub-agents in parallel via the Agent tool.

### assistant

I see the target is `C:\Users\amado\coach-os` (the `ado/` in your message is a typo for `amado/`). I'll dispatch 4 sub-agents in parallel via the Agent tool, each scoped to a specific sub-folder or concern. All sub-agents are read-only.

### assistant

Acknowledged — skill list noted. The 4 sub-agents (A: Hook & Render, B: Detail/breadcrumb contract, C: Browser regression, D: Console & runtime) are still running in the background. I'll aggregate their findings into a single report under 700 words once they all return. No further action needed until the completion notifications arrive.
