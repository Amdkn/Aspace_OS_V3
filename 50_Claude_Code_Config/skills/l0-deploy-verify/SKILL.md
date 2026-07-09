---
name: l0-deploy-verify
description: >
  Post-deploy verification gate for L0 surfaces (Vercel, self-hosted Supabase, VPS).
  USE THIS SKILL whenever the user (A0) wants to: verify a deploy is GREEN, prove
  a preview URL responds, smoke-test a critical page after push, check that env
  vars landed in the right scope, or close a P1.x gate. Bakes in the 5-step
  Verify-Before-Assert gate (build status, URL 200, key page renders, no console
  errors, Supabase schema matches), MCP preference for interactive debugging
  (Playwright MCP, chrome-devtools MCP, supabase-aspace MCP), D1 proof (no
  assertions, only observed output), no secrets in any output (Test Key
  Pragma), and HITL gate on prod env-var changes. L0 = Tech OS / Rick's Verse.
when_to_use: |
  - User says "verify the deploy", "is the prod up?", "check Vercel", "smoke test", "post-deploy"
  - A Vercel deployment just completed (build webhook, or A0 said "deployed")
  - A Supabase migration was just applied (P1.x gate closing)
  - A change to VPS self-hosted infra (VPS file push, docker restart)
  - A0 wants proof the production is healthy after a code change
inputs: |
  1. Target surface (Vercel project ID, Supabase project ref, or VPS subdomain)
  2. Critical paths to verify (e.g. `/`, `/login`, `/api/health`)
  3. Implicit: A0 wants PASS/FAIL per step, with observed evidence
outputs: |
  1. Step-by-step report (5/5 GREEN or partial with failures)
  2. Screenshot of the key page (if MCP available)
  3. Console errors list (if any)
  4. Suggested next step on FAIL (rollback, hotfix, or escalate to A0)
---

# /l0-deploy-verify — Post-deploy verification gate

> **Doctrine** : L0 = Tech OS / Rick's Verse. Verification is the gate, not
> the deploy itself. D1 = observed output, not assertions.
>
> **Canon refs** : `00_Amadeus/01_Identity_Core/AGENTS.md` · `ADR-META-001` ·
> `Shadow_L0/HEARTBEAT_PROTOCOL.md` · Vercel contract `10_Tech_OS/.../04_vercel/AGENTS.md`.

## When to trigger

| Signal | Action |
|---|---|
| A0 just said "deployed" or "pushed to prod" | Run the 5-step gate below |
| A0 said "verify Vercel" / "verify Supabase" / "verify VPS" | Run for the named surface |
| A0 closed a P1.x gate (P1.0, P1.1, P1.4) | Run as the gate's verification step |
| A0 said "is the prod up?" | Run the URL-only subset (step 2 + 3) |
| A0 wants to know if env vars landed | Run the env-var subset (Vercel `list_env_variables` or Supabase GUC check) |
| A0 did NOT explicitly ask for verification | Do NOT auto-verify. Wait. |

## The 5-step gate

### Step 1 — Build / migration status

| Surface | Command | PASS criterion |
|---|---|---|
| Vercel | `mcp__vercel__list_deployments` (or `curl https://api.vercel.com/v6/deployments?projectId=...`) | latest deployment `state = "READY"` |
| Supabase migrations | `ssh aspace-vps "docker exec supabase-db psql -U postgres -d postgres -c 'SELECT filename FROM <schema>._<schema>_migrations ORDER BY applied_at DESC LIMIT 5'"` | latest expected migration present |
| VPS infra | `ssh aspace-vps "docker ps --format '{{.Names}}\t{{.Status}}'"` | all critical services `Up X minutes` (no `Restarting`) |

**Proof format** : paste the exact command output. Do not paraphrase. If the
output is empty or error, that's a FAIL — don't say "looks good".

### Step 2 — URL responds 200

| Surface | URL | PASS criterion |
|---|---|---|
| Vercel preview | preview URL from `list_deployments` | HTTP 200 (or 307→200 for auth walls) |
| Vercel prod | production URL (e.g. `https://abc.kalybana.com`) | HTTP 200 |
| Supabase REST | `https://<project-ref>.supabase.co/rest/v1/` | HTTP 200 (returns `[]` or schema list) |
| Supabase self-hosted | `https://abc.kalybana.com/rest/v1/` | HTTP 200 |

**Tool of choice** : `curl -I -sS -o /dev/null -w "%{http_code}\n" <url>` for
fast head-only check. Use Playwright MCP for JavaScript-rendered pages.

### Step 3 — Key page renders

| Path type | Tool | PASS criterion |
|---|---|---|
| Static HTML | `curl -sS <url> \| head -100` | expected `<title>` or sentinel string present |
| Next.js / React | Playwright MCP `browser_navigate` + `browser_snapshot` | expected `<h1>` text present |
| API health | `curl -sS <url>/api/health` | JSON `{"status":"ok"}` or equivalent |

**Critical paths to test per project** (canonical):
- `abc-os-community`: `/`, `/login`, `/dashboard`, `/community`, `/build-hub`
- `omk-dashboard`: `/`, `/dashboard`, `/people`
- `omk-landing`: `/`

### Step 4 — No console errors

For Next.js / React apps, run Playwright MCP `browser_console_messages` after
navigating to the key page. PASS = no `error` level messages related to the
app (filter out third-party network noise and known Chromium warnings).

**Anti-pattern** : do not skip this step because the page "looks fine". A
white screen with `Error: Cannot read property 'X' of undefined` looks fine in
a screenshot if you don't check the console.

### Step 5 — Supabase schema matches (only if migration was applied)

| Check | SQL |
|---|---|
| Schema exists | `SELECT count(*) FROM information_schema.schemata WHERE schema_name = '<expected>'` |
| Tables present | `SELECT count(*) FROM information_schema.tables WHERE table_schema = '<expected>'` |
| RLS enabled | `SELECT count(*) FROM pg_tables WHERE schemaname = '<expected>' AND rowsecurity = true` |
| Seeded rows | `SELECT count(*) FROM <expected>.<seed_table>` (if seeding was part of the deploy) |

Compare observed counts to expected. Any mismatch = FAIL.

## Output format

```
=== L0 DEPLOY VERIFY: <surface> ===

Target: <project ID or domain>
Deploy ID: <if Vercel>
Branch: <if known>
Time: <ISO 8601>

Step 1 — Build/migration status:  [PASS|FAIL]  <observed output>
Step 2 — URL responds 200:        [PASS|FAIL]  <HTTP code>
Step 3 — Key page renders:        [PASS|FAIL]  <sentinel string or h1>
Step 4 — No console errors:       [PASS|FAIL]  <N errors, top 3 quoted>
Step 5 — Supabase schema:         [PASS|FAIL|N/A]  <observed counts>

Overall: <X>/5 PASS

Next step: <rollback | hotfix | close gate | escalate to A0>
```

## MCP preference (interactive mode)

| MCP server | When to use |
|---|---|
| `playwright` (built-in) | Default for any browser-rendered page |
| `chrome-devtools` | When you need Lighthouse, perf trace, heap snapshot |
| `supabase-aspace` (HTTP, port 3100) | Schema introspection, RLS check, query smoke |
| `supabase-solaris` (SSH) | VPS-side DB queries (migrations, replication lag) |

If MCP is unavailable, fall back to `curl` + `ssh` for headless verification.
Always note which mode you used in the report.

## Constraints

| Constraint | Enforcement |
|---|---|
| D1 = observed output | Never write "PASS" without the command output in your context |
| No secrets in output | If a step returns a token/key, redact (`****`) before pasting |
| No hard-delete | Never run `rm -rf` on prod logs; use `mv` to `_TRASH/<date>_` first |
| HITL on prod env-var changes | If Step 5 reveals missing env vars, surface to A0 — don't auto-set |
| HITL on rollback | Never run `vercel rollback` without explicit A0 GO |
| Append-only wiki log | After verification, append 1 line to `wiki/log.md` (PASS or FAIL) |
| Idempotent | Re-running on a GREEN surface should re-PASS, not double-log |

## Anti-patterns (do NOT)

| Anti-pattern | Why it's bad | What to do instead |
|---|---|---|
| Assert "looks good" without command output | D1 violation | Paste the exact curl/ssh/MCP output |
| Skip Step 4 (console errors) because page renders | Hidden runtime errors slip through | Always check console for React/Next.js |
| Auto-fix a FAIL by editing env vars | HITL violation — prod changes need A0 GO | Surface the FAIL, propose 2-3 fix options, wait |
| Run verification on a stale deploy ID | Verifies old code, not the just-pushed one | Always re-query `list_deployments` first |
| Mark schema check PASS based on file existence | Schema file ≠ applied migration | Query `pg_tables` for the actual count |
| Use Lighthouse as the only check | Lighthouse is perf, not functional | Combine with Step 3 sentinel + Step 4 console |

## See also

- `Shadow_L0/HEARTBEAT_PROTOCOL.md` — 5m/15m/on-demand tick cadence
- `_SPECS/ADR/ADR-INFRA-001_console-gouvernance.md` — the L0 surface
- `/l0-watchdog-scrape` — batch watchdog scrape (different cadence, different scope)
- `/aspace-supabase-mastery` — for Supabase-specific deep checks
- `/vercel-deploy-from-github` — the deploy side; this skill is the verify side
- `/mcp-mastery` — when to use which MCP server
