---
name: vercel-deploy-from-github
description: Deploy a local app directory to Vercel production by linking the local repo to a new Vercel project (or reusing the existing link) and triggering a one-shot production deploy via the Vercel CLI. Use this skill whenever the user says "deploy on Vercel", "push to Vercel", "deploy my app", "ship the prod build", or wants to ship a Next.js / Vite / static site from `C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\<org>\apps\<app>` to a `<project>.vercel.app` URL. Validated 3× in the 2026-06-08 session (abc-os-community, omk-dashboard, omk-landing). Assumes Vercel CLI 54.x is installed, `VERCEL_TOKEN` is set in env User, and the user is in the `amd-lab` team (orgId `team_d3JjRK4fJUE9ACohbdlhv9Gc`). If the user is in a different team or no token is set, surface that as a blocking precondition before running.
---

# /vercel-deploy-from-github — One-shot Vercel prod deploy from a local Git repo

## Mission

Take a local app directory that already has a `git remote` pointing at a GitHub repo, link it to a Vercel project (creating one if needed), push a production build, and return the live alias URL with a verified HTTP 200.

The skill is **deterministic and idempotent** — running it twice on the same dir + same project name ends at the same live URL.

## MCP vs CLI — when to use which (added 2026-06-16)

A `vercel` MCP is wired in `.mcp.json` (server: `vercel-mcp@latest`, env `VERCEL_TOKEN`). It exposes inspection/management tools (list projects, list deployments, get deployment logs, list env vars, list domains, check build status). It does **NOT** replace the CLI for the actual `link` + `deploy` flow — those still go through the Vercel CLI because the MCP version of "deploy" is not stable in the 0.0.7 community build.

**Use the MCP for**: pre-flight checks, post-deploy inspection, env var auditing, domain/DNS checks, build log tailing — anything where staying in the agent context is faster than shelling out.

**Use the CLI for**: the actual `link` + `deploy --prod` flow described below. CLI is canonical and battle-tested across 3 prior deploys (abc-os-community, omk-dashboard, omk-landing).

**Token**: same `VERCEL_TOKEN` env var powers both. Set User scope once via Test Key Pragma.

## Preconditions (verify first, fail loud if missing)

Run these checks in parallel before doing anything else. If any fails, stop and report the missing piece.

| Check | Command | Pass criterion |
|---|---|---|
| Vercel CLI installed | `vercel --version` | prints `54.x` or newer |
| Auth OK + correct team | `vercel whoami` | prints `amdkn7` (not some other account) |
| Working dir is a git repo | `git -C <dir> rev-parse --is-inside-work-tree` | `true` |
| GitHub remote exists | `git -C <dir> remote get-url origin` | starts with `https://github.com/` |
| No uncommitted non-lockfile dirt | `git -C <dir> status --short` | empty, OR only `M package-lock.json` (CRLF noise is harmless) |

> **Why these matter**: a wrong `whoami` means deploying under a different team/org (the alias would be on someone else's account). A missing GitHub remote means `vercel link` will fail to connect a repo. Local dirty changes (other than lockfile) are silently NOT deployed by `vercel deploy` — they live in the working copy only and the next git push would also push them; surface this to the user.

## Inputs (ask the user ONCE)

Use `AskUserQuestion` for these — don't infer.

| Input | Required | Default | Notes |
|---|---|---|---|
| Working dir | yes | (the directory the user mentioned) | absolute Windows path |
| Vercel project name | yes | (none) | kebab-case, must be URL-safe; `vercel link` will fail with 409 if a project with that name already exists in the team under a different repo |

If the user doesn't know the project name, suggest the directory's kebab-case form (`omk-dashboard`, `abc-os-community`) and confirm.

## Workflow (3 steps, run sequentially — each step is a single shell call)

### Step 1 — Link (idempotent)

```bash
cd "<working-dir>" && vercel link --project <project-name> --team amd-lab --yes 2>&1
```

- `--team` is deprecated but still works (Vercel prints a warning). Use `--scope amd-lab` if you want to silence the warning — both are equivalent in this session.
- The CLI auto-detects the framework (Next.js / Vite / etc.) from `package.json` and prints it.
- The CLI auto-connects the GitHub repo from the local `origin` remote and registers a webhook.
- If `.vercel/project.json` already exists with a DIFFERENT project name, STOP and ask the user: "this dir is already linked to project `<other>`. Redeploy to it, or relink to `<requested>`?".

Verify success by reading `.vercel/project.json`:
```json
{"projectId":"prj_...","orgId":"team_d3JjRK4fJUE9ACohbdlhv9Gc","projectName":"<name>"}
```

### Step 2 — Deploy prod

```bash
cd "<working-dir>" && vercel deploy --prod --yes 2>&1
```

- Build runs in Vercel's default region (iad1, Washington DC — 2 cores / 8 GB).
- The CLI uploads the source, runs `npm install` + the build script, then deploys.
- Wait for `Deployment ... ready.` and capture the JSON block at the end.
- The output JSON contains: `deployment.url` (per-deploy URL, returns 401 outside Vercel auth), `deployment.inspectorUrl` (Vercel dashboard), `deployment.id` (the dpl_... ID), and the alias `https://<project-name>.vercel.app` printed just above the JSON.

Build time benchmark from the 2026-06-08 session:
- Vite SPA (omk-dashboard): ~30 s total
- Next.js 15 + Turbopack (abc-os-community): ~50 s total
- Next.js 16 + Turbopack (omk-landing): ~25 s total

### Step 3 — Verify live (run from the local machine, NOT from the VPS)

```bash
curl -skL -o /dev/null -w "HTTP %{http_code} | %{size_download}B | %{time_total}s\n" \
  https://<project-name>.vercel.app/
curl -skL https://<project-name>.vercel.app/ | grep -oE '<title>[^<]+</title>' | head -1
```

Pass criteria:
- HTTP 200 on the alias URL
- `<title>` non-empty and matches the app's expected title (e.g. `OMK Services Business OS — The Autonomous Swarm Orchestrator`)

If the app has multiple routes (Next.js) or asset paths (Vite), curl a sample:
```bash
for r in / /brand /build /community; do
  printf "  %-15s " "$r"
  curl -skL -o /dev/null -w "HTTP %{http_code} | %{size_download}B\n" \
    "https://<project-name>.vercel.app$r"
done
```

## Known-error filters (NOT failures — report as warnings, don't halt)

| Symptom | Where | Meaning | Action |
|---|---|---|---|
| HTTP 401 on `https://<project-name>-<hash>-amd-lab.vercel.app/` | per-deploy URL | Vercel auth on per-deploy URLs | IGNORE — the alias URL is the user-facing one. Mention it. |
| HTTP 405 on `/api/<route>` with GET | Next.js API route | Route exists, only POST/OPTIONS allowed | IGNORE — expected. Try `curl -X OPTIONS` to confirm route is live. |
| HTTP 500 on `/api/<route>` with POST | Next.js API route | App handler crashes (missing env var, unimplemented, etc.) | WARN — not a deploy failure. Surface to user as "API route is wired but handler throws; check env vars / handler code". |
| Vite SPA returns 593B on `/` | Vite app | Normal — Vite serves a minimal HTML shell, JS hydrates client-side | OK — verify with the title check + asset URLs in the HTML. |
| `--team` deprecation warning | CLI | Cosmetic, Vercel pushes `--scope` | OK — works fine. |

## Real failures (HALT and report)

| Symptom | Likely cause | Report |
|---|---|---|
| `vercel whoami` returns a different user | wrong `VERCEL_TOKEN` | "Auth is for `<user>`, not amdkn7. Set `VERCEL_TOKEN` to the amd-lab token." |
| `vercel link` exits with "already exists" / 409 | name collision with another project in the team | "Project name `<name>` is taken in amd-lab. Pick another or pass the existing projectId via `vercel link --project prj_...`." |
| `vercel deploy` exits non-zero | build failure, missing deps, out-of-memory, etc. | "Deploy failed at build step. Tail of error: `<last 20 lines of build log>`." |
| Alias URL returns non-200 after successful deploy | DNS/CDN propagation lag, or DNS not yet active | Wait 30 s and re-curl. If still failing, check `vercel inspect <url>` for the deployment status. |

## Final report (output to user)

After Step 3 passes, report this exact block (or close to it):

```
🟢 LIVE — https://<project-name>.vercel.app

| Item | Value |
|---|---|
| Project | <project-name> (prj_...) |
| Org | amd-lab (team_d3JjRK4fJUE9ACohbdlhv9Gc) |
| GitHub | <github-org>/<github-repo> (<default-branch>) |
| Deployment | dpl_... (READY, target=production) |
| Inspector | https://vercel.com/amd-lab/<project-name>/<dpl-id> |
| Title | <extracted from HTML> |
| Alias | https://<project-name>.vercel.app → HTTP 200 |
| Auto-deploy | ACTIVE — `git push` to <branch> will redeploy |
```

The "Auto-deploy ACTIVE" line is the most useful thing to tell the user — they don't need to re-run this skill for subsequent deploys. They just `git push`.

## What this skill does NOT do (so the user knows to ask separately)

- ❌ Custom domain (Vercel alias only — the user can add a domain in the Vercel dashboard)
- ❌ Env vars (Vite/Next.js env vars must be set in the Vercel dashboard or via `vercel env add` before deploy)
- ❌ Push to GitHub first (the deploy is from the local working copy; the GitHub integration is established for FUTURE `git push` auto-deploys)
- ❌ Promote a previous deployment to prod (use `vercel promote` separately)
- ❌ Roll back (use `vercel rollback` separately)
- ❌ Multi-region / edge config (Vercel defaults are iad1)

## Worked example — `omk-dashboard`

```bash
# Step 1
cd "C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\omk\apps\dashboard"
vercel link --project omk-dashboard --team amd-lab --yes
# → Linked amd-lab/omk-dashboard · GitHub connected
# → .vercel/project.json = {"projectId":"prj_FJpNDykkNMhDJUEg2FvKAegeeQG3",...}

# Step 2
vercel deploy --prod --yes
# → Building in iad1 · vite v6.4.2 · 229 packages · 6 s
# → ▲ Aliased https://omk-dashboard.vercel.app
# → {"status":"ok","deployment":{"id":"dpl_GxPDq7QgAf4LDP2Y2FfbEaeAEZ1G",...}}

# Step 3
curl -skL -w "HTTP %{http_code}\n" -o /dev/null https://omk-dashboard.vercel.app/
# → HTTP 200
curl -skL https://omk-dashboard.vercel.app/ | grep -oE '<title>[^<]+</title>'
# → <title>OMK Services Business OS — The Autonomous Swarm Orchestrator</title>
```

Total time: ~30 s. Three tool calls. One user prompt.

## Related

- Skill `picard-audit-and-prod-workflow` — the higher-level "make this app prod-ready" workflow. This skill is a leaf: it assumes the app is already prod-ready and just needs the deploy step.
- Skill `mcp-mastery` — for MCP-specific patterns (server selection, transport choices, token rotation via Test Key Pragma). The `vercel` MCP mentioned above is wired via `mcp-mastery`'s standard pattern.
- Skill `github-cli-orchestration` — sibling for GitHub-side ops (PR creation, repo discovery). Vercel deploy auto-triggers from GitHub pushes wired here.
- ADR-INFRA-002 (Repo-Home / Junction) — explains why `apps/<app>/` is the canonical build-bearing path for the Business OS projects.
- ADR-RICK-001 (OpenHarness Incarnation) — the meta-doctrine about not letting an agent skip verify-before-assert. This skill embeds D5/D6 from ADR-META-001: every step ends in an observed proof (HTTP code, file content, deployment status), not a hopeful assertion.
