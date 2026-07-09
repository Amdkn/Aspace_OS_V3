---
name: aaas-dashboard-port-audit
description: Audit a target dashboard against the AaaS Solaris reference and produce a structured port plan (missing views, schema divergences, runtime differences, file-by-file recommendations). Use when migrating or porting a non-Solaris dashboard to mirror the AaaS 12-view structure across 4 nav groups (CULTIVATE / NURTURE / BLOOM / ROOTS).
---

# AaaS Dashboard Port Audit

Read-only audit skill. Compares a target dashboard codebase against the AaaS
"Solaris" reference dashboard and outputs a structured port plan. Does NOT
modify any file, run SQL, or execute migrations.

## When to use

- A0 asks "audit this dashboard against Solaris / AaaS"
- A new dashboard repo needs a gap analysis before it can mirror AaaS doctrine
- A repo diverged from AaaS structure and you need a one-shot reconciliation map
- Onboarding a dashboard into the AaaS fleet (CEO dashboard, Odoo mirror, etc.)
- A0 invokes `/aaas-dashboard-port-audit` or describes a port intent in plain
  English ("compare X to Solaris", "what's missing to match AaaS", etc.)

## Inputs

| Arg | Required | Default | Meaning |
|-----|----------|---------|---------|
| `target` | yes | — | Absolute path to the dashboard to audit |
| `source` | no  | AaaS Solaris canonical location | Absolute path to the reference dashboard |
| `scope`  | no  | `full` | `full` / `views` / `schema` / `nav` / `runtime` |
| `out`    | no  | `<target>/.audit/port-plan-<date>.md` | Where to write the report |

Resolve `source` from the AaaS doctrine: the canonical Solaris dashboard lives
under the AaaS Business OS tree. If ambiguous, ASK A0 before assuming.

## Reference paths (Solaris)

Doctrine-level references (read first, treat as Canon):

- `ASpace_OS_V2/_SPECS/ADR/ADR-INFRA-003_ceo-dashboard.md` — CEO dashboard doctrine
- `ASpace_OS_V2/_SPECS/ADR/ADR-CANON-001_agent-roster.md` — escouade / squad canon
- `ASpace_OS_V2/00_Amadeus/01_Identity_Core/AGENTS.md` — fractal A0-A3 hierarchy
- `30_Business_OS/10_Projects/<proj>/_doctrine/REBUILD_WORKFLOW.md` — port procedure
- `30_Business_OS/10_Projects/<proj>/_doctrine/NAV_DOCTRINE.md` — 4 groups, 12 views

Solaris itself (the reference dashboard to diff against):

- Repo root: the AaaS Solaris dashboard (path resolved per project)
- `src/views/*.tsx` — 12 views (see checklist)
- `src/components/nav/Sidebar.tsx` — collapsible lucide-icon sidebar
- `src/lib/nav.ts` — `NavGroup` enum + `NavView` enum
- `src/lib/schema.ts` — `solaris_*` table names (saas tier)

### 12 views / 4 nav groups (doctrine)

| Group      | Views                                                          |
|------------|----------------------------------------------------------------|
| CULTIVATE  | Dashboard · Finance · Clients · Tasks                          |
| NURTURE    | SOP · Legal · Growth                                           |
| BLOOM      | Marketplace · Sales                                            |
| ROOTS      | ItData · People · Settings                                     |

A target missing any of these 12 is, by doctrine, incomplete.

## Audit steps

1. **Pre-flight** — read target's `CLAUDE.md`, `package.json`, target's
   `AGENTS.md` (if any), and the canonical AaaS doctrine files above. Confirm
   the 4 ADR blockers are resolved (see Doctrine constraints). If any blocker
   is open, STOP and report to A0.
2. **Inventory target** — walk the target tree, capture: views, nav files,
   schema files (Drizzle/Prisma/SQL), routing, layout, state management,
   sidebar component, icon library, empty-state / skeleton patterns.
3. **Inventory source** — same walk on the AaaS Solaris reference.
4. **Diff runtime** — SPA vs RSC, Vite vs Next.js, state mgmt, router,
   bundler, auth gate. Record every divergence in a table.
5. **Diff schema** — table prefix (`omk_*` vs `solaris_*`), schema location
   (`internal` vs `saas`), RLS policies, generated types, seeders.
6. **Diff nav** — sidebar component, icon set, collapsibility, `NavGroup` /
   `NavView` enum presence, route map.
7. **Diff views** — for each of the 12 doctrine views, mark: present /
   partial / missing / divergent. For present views, note component parity
   (skeletons, empty states, error boundaries).
8. **Categorize gaps** — bucket every gap as: `must-port` (doctrine),
   `should-port` (parity), `nice-to-have` (polish), `out-of-scope` (rejected
   with reason).
9. **Write port plan** — emit a markdown report with: executive summary,
   runtime delta, schema delta, view-by-view matrix, nav parity table,
   prioritized gap list, file-by-file recommendations, ADR blockers status,
   and an explicit "What we will NOT change" section.

## Output format

The audit report (`port-plan-<date>.md`) MUST contain, in this order:

1. **Header** — date, target path, source path, auditor, scope, doctrine rev.
2. **Doctrine check** — 4 ADR blockers status (resolved / open / N/A).
3. **Executive summary** — one paragraph: target maturity vs Solaris, top 3
   blockers, recommended next move.
4. **Runtime delta table** — Vite/Next, SPA/RSC, router, state, auth.
5. **Schema delta table** — prefix, location, RLS, types, seeders.
6. **View parity matrix** — 12 rows × 4 columns (CULTIVATE/NURTURE/BLOOM/ROOTS)
   with status badges: `present` / `partial` / `missing` / `divergent`.
7. **Nav parity table** — sidebar, icons, collapse, enums, route map.
8. **Gap list (prioritized)** — `must-port` → `should-port` → `nice-to-have`
   → `out-of-scope`. Each item: id, title, why, files affected, est. effort.
9. **File-by-file recommendations** — concrete `cp` / `adapt` / `rewrite`
   per file, with target file path and AaaS source file path.
10. **Open questions for A0** — anything that needs Amadeus judgment, never
    silently assumed.
11. **What we will NOT change** — explicit out-of-scope list with rationale.
12. **References** — every AaaS doctrine file cited, with hash or commit
    pin if possible.

## What this skill does NOT do

- Does NOT modify any file in the target or source repo.
- Does NOT run SQL, migrations, or `drizzle-kit push`.
- Does NOT touch `AGENTS.md`, doctrine files, or any Canon document.
- Does NOT install dependencies or run `pnpm install` / `npm i`.
- Does NOT create branches, commits, or PRs.
- Does NOT bypass the 4 ADR blockers — if any is open, the skill reports and
  exits. A0 must ratify before the port can proceed.
- Does NOT touch secrets, `.env`, or any file under `_TRASH/`.

## Doctrine constraints (BLOCKERS)

The audit MUST halt and report back to A0 if any of the following is open
(true at the moment the skill is invoked):

1. **ADR-RICK-001 (OpenHarness Incarnation)** — open or unratified.
2. **ADR-META-001 (Anti-Paresse Verify-Before-Assert)** — the target lacks a
   `CLAUDE.md` referencing the doctrine, OR the auditor cannot cite the
   doctrine hash for any claim.
3. **ADR-INFRA-002 (Repo-Home / Junction doctrine)** — the target dashboard
   does not live under a `_doctrine/` junction pointing to the Verse, OR the
   junction is broken (path mismatch, dead symlink).
4. **ADR-INFRA-003 (CEO Dashboard doctrine)** — no `_doctrine/NAV_DOCTRINE.md`
   and no `_doctrine/REBUILD_WORKFLOW.md` at the target, OR the doctrine
   files contradict the 12-view / 4-group structure.

In addition to the 4 blockers, the auditor MUST honor:

- **No-hard-delete** — never `Remove-Item` / `rm -rf`; use `_TRASH/`.
- **Test Key Pragma** — never paste or read secrets from `.md` / `.json` /
  `.env`; use env vars User scope only.
- **Vite vs Next.js adaptation** — if target is Vite SPA and source is
  Next.js RSC, mark every RSC-only file as `adapt` (not `cp`); never assume
  server components can be copy-pasted into a Vite app.
- **Doctrine citation required** — every claim about view count, nav group
  count, or schema prefix MUST cite the file and line. No unverified
  assertions (ADR-META-001 D2).

## Quick reference

- Run from `C:/Users/amado/`.
- Read `references/checklist.md` before each audit and tick every box.
- If target is unreadable (permissions, missing), STOP and report — do not
  silently skip.
- Default report name: `port-plan-YYYY-MM-DD.md` (use session local date).
