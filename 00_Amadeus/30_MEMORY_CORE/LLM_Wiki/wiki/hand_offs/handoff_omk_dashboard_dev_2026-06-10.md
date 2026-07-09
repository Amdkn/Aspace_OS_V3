---
source: A2 Claude Code (this session) handoff after graphify delegation
date: 2026-06-10
type: handoff
status: ACTIVE — waiting for receiving session to pick up dev on omk-dashboard
domain: L2_Business_OS / 30_Business_OS / 10_Projects / omk / apps / omk-dashboard
tags: [#omk, #vite, #react, #supabase, #multi_tenant, #rebuild, #handoff, #delegation, #typescript, #tailwind4, #dokploy]
related: [_SPECS/ADR/ADR-OMK-001_dual-product.md (PROPOSED), _SPECS/ADR/ADR-SUPABASE-001_multi-tenant.md (PROPOSED), 20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/CERRIROS_HANDOVER.md, 30_Business_OS/10_Projects/omk/apps/dashboard/REBUILD_WORKFLOW.md]
context_release: this session is being freed for project development; graphify full build delegated separately; ABC OS dev handoff also already written (see handoff_abc_os_community_dev_2026-06-10.md)
---

# Handoff — OMK Dashboard Dev (2026-06-10)

## Why this handoff exists

A0 wants to free this Claude Code session for project development (heho). The
**OMK Dashboard** (Vite 6 + React 19 + Supabase multi-tenant rebuild) is substantial
enough to warrant its own session. This handoff is the executable playbook.

**CRITICAL DIFFERENCE FROM ABC OS Handoff**: OMK is not a migration — it's a
**rebuild with backend integration**. The contract already exists in
`REBUILD_WORKFLOW.md` (7.4KB, 8 phases A→H, SQL DDL). This handoff is a *companion*
to that contract: it orients a fresh session, names the 4 blockers, and points at
the right files in the right order. **Always read REBUILD_WORKFLOW.md first.**

## Project overview — what is OMK Dashboard

**OMK Services Business OS** is the operating system for OMK, a Paris-based
services firm. The dashboard is the staff/operator view of the OS: client
engagements, documents, agents, finance, SOPs, settings.

**Doctrine** (per `CERRIROS_HANDOVER.md`):
- **Mode default**: Nexus (data-first/systems) at $25K–$200K
- **Constraint**: Zero-Jerry dependency within 12 months
- **Operating rules**: All 8 B2 domains active; all 6 LD01 books mapped
- **Routing chain**: Jerry (A1) → Cerritos (GTD triage) → Picard/Summer (B1) → B2 Rocks → B3 Squads

Stakeholder: OMK Services (current single-tenant). Future-proofed for SaaS
(multi-tenant, per-organization isolation).

## The 2 apps in this project

Located at `C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\omk\apps\`:

| App | Role | Stack | Git? | Deploy? |
|-----|------|-------|------|---------|
| **`omk-dashboard`** | **TARGET — primary dev app** | Vite 6 + React 19 + TS 5.8 + Tailwind v4 + @supabase/supabase-js + react-router-dom 7 + motion + lucide-react + @google/genai | ✅ `github.com/Amdkn/01-OMK-Business-OS` (3 commits) | ⚠️ Vercel project link UNUSED → **Dokploy** is the deploy target (per REBUILD Phase G) |
| `omk-landing` | Public marketing site | Next.js | ❌ | ❌ |

The doctrine junction (per ADR-INFRA-002) lives at `_doctrine` symlink in
`30_Business_OS/10_Projects/omk/` → `20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/`.

## State of `omk-dashboard` as of 2026-06-10 (verified by source session)

### Phase state (per `REBUILD_WORKFLOW.md` 8-phase plan)

| Phase | Description | State |
|-------|-------------|-------|
| **A** | Fondations local (config/mode, supabase client, env example) | 🟡 PARTIAL — `src/config/mode.ts` ✅, `src/lib/supabase.ts` ✅, `.env.example` ✅, but `npm run lint` not verified |
| **B** | Schémas + seed Supabase (via `supabase-aspace` MCP) | ❌ NOT STARTED — blocked by `supabase-aspace` MCP v0.1 (not yet implemented) |
| **C** | Auth + tenant (AuthProvider, useAuth, LoginView/SignupView) | ❌ NOT STARTED — "Admin User" still hardcoded in App.tsx |
| **D** | Repositories + branchement views (data/*.repo.ts, 7 views) | ❌ NOT STARTED — `src/data/repository.ts` exists but not wired |
| **E** | Routing (routes/router.tsx, react-router) | ❌ NOT STARTED — `useState(activeTab)` still in App.tsx (no URL) |
| **F** | Serveur + conteneur (server.js, Dockerfile) | 🟡 PARTIAL — `server.js` + `Dockerfile` + `.dockerignore` added in commit `83099ab` |
| **G** | Déploiement Dokploy (2 services, env Supabase par service) | ❌ NOT STARTED — blocked by ADR-OMK-001 (PROPOSED) |
| **H** | Tests isolation + handoff (RLS adversarial test, README, commit) | ❌ NOT STARTED |

### What's built ✅

```
src/
├── App.tsx                     # 144 lines, 7 views via useState
├── main.tsx
├── vite-env.d.ts
├── components/
│   ├── Badge.tsx / Card.tsx / ProgressBar.tsx / index.ts
│   └── views/                  # 7 views
│       ├── AgentsView.tsx
│       ├── ClientsView.tsx
│       ├── DashboardView.tsx
│       ├── DocumentsView.tsx
│       ├── FinanceView.tsx
│       ├── SettingsView.tsx
│       ├── SOPLibraryView.tsx
│       └── index.ts
├── config/mode.ts              # ✅ resolveAppMode() per REBUILD spec
├── data/repository.ts          # ✅ exists, not wired to views
├── hooks/useCollection.ts      # ✅ exists
├── lib/
│   ├── constants.ts            # ⚠️ still mock data (needs split → seed.ts)
│   ├── supabase.ts             # ✅ client schema-aware
│   └── types.ts                # ✅ business types
index.css                       # Design System (preserved)
server.js                       # Express for prod (serves dist/)
Dockerfile                      # multi-stage build
.dockerignore
```

Git history (3 commits):
- `83099ab chore(omk): add Express production server, Dockerfile, and dockerignore for production deployment`
- `70efe01 feat: add Supabase-ready data layer with localStorage fallback (Phase A+B)`
- `4a1c6b3 feat: modularize and refactor OMK Services Business OS into clean views`

Uncommitted: `.gitignore` modified (uncommitted change adding `.vercel`/build artifacts).

### Open tickets / known issues 🐛

#### #1 — CRITICAL: 4 ADR-level blockers must be lifted first

The rebuild cannot meaningfully start until these 4 are resolved:

| Blocker | Statut | Action |
|---------|--------|--------|
| `ADR-SUPABASE-001` (multi-tenant Supabase) | ⏳ PROPOSED | A0 ratify → move to RATIFIED in `_SPECS/ADR/` |
| Rôles PG `aspace_admin`/`aspace_observer` | ⏳ à créer (VPS) | Codex/Hermes on VPS — needs VPS-side coordination |
| MCP `supabase-aspace` v0.1 | ⏳ à implémenter | Required for `create_project_schema`, `generate_typescript_types` |
| `ADR-OMK-001` (dual-product deployment) | ⏳ PROPOSED | A0 ratify → Dokploy vs Vercel decision |

**Action**: open a session with A0 specifically to ratify ADRs. Without these, every
later phase is blocked on schema creation (B), auth wiring (C), and deploy (G).

#### #2 — `lib/constants.ts` is still mock data (needs split)

Per REBUILD §1: `lib/constants.ts` should become `lib/seed.ts` (used only for SQL/dev
seeding) + `lib/types.ts` (already exists, but membership/org_id types are missing).

**Action**: add `Organization`, `Membership` types to `lib/types.ts`. Rename
`constants.ts` → `seed.ts` and restrict its use to the dev/seed flow.

#### #3 — `.gitignore` has an uncommitted change

`git status` shows `.gitignore` modified (uncommitted). Standard for the OMK project
(follows the same pattern as `abc-os-community`), but breaks `vercel` CLI deploy —
**Dokploy doesn't care**.

**Decision**: keep gitignored (Dokploy reads env from Dokploy panel, not from
`.vercel/`). Document in AGENTS.md.

#### #4 — README is default Vite boilerplate

`README.md` mentions Vite + React, doesn't mention OMK, Supabase, or the dual-mode
runtime. Needs to be rewritten to:
- Describe the project (what is OMK Dashboard, who is it for, dual-mode)
- Link to `REBUILD_WORKFLOW.md` as the contract
- Document the dev/build/deploy commands
- Document the `VITE_APP_MODE` env var
- Reference the doctrine junction

#### #5 — No `AGENTS.md` in `omk-dashboard/`

No agent guidance file. The receiving session should create one with:
- The 4 ADR-level blockers
- The 8-phase REBUILD state
- The dual-mode runtime contract (`VITE_APP_MODE`)
- The Supabase architecture (self-hosted on VPS, schemas `omk_internal` + `omk_saas`)
- The RLS pattern (org_id in JWT via custom hook)
- The Dokploy deploy path (NOT Vercel)
- The data flow: views → repositories → Supabase

#### #6 — Vercel project link is UNUSED (do not wire GitHub)

`prj_FJpNDykkNMhDJUEg2FvKAegeeQG3` in `team_d3JjRK4fJUE9ACohbdlhv9Gc` exists on
Vercel but **the deploy target is Dokploy** (per REBUILD Phase G). Do NOT link
GitHub to this Vercel project — the Vercel project is leftover/orphaned.

**Action**: in AGENTS.md, explicitly note "Vercel project ignored — use Dokploy
(per REBUILD Phase G)." Optionally archive the Vercel project via
`mcp__vercel__archive_project` to remove it from the dashboard clutter.

#### #7 — Auth is hardcoded ("Admin User")

`App.tsx` line 93 (per REBUILD) still has `"Admin User"` hardcoded. Phase C replaces
this with `AuthProvider` + `useAuth` (Supabase session + org_id from JWT).

**Action**: Phase C work. Do not start until blocker #1 (ADR-SUPABASE-001) is
ratified, otherwise the auth wiring has no schema to authenticate against.

#### #8 — No tests (unit + E2E + RLS)

Neither unit tests nor E2E tests exist. Phase H is the test phase, including the
**adversarial RLS test** (org A user cannot read org B data — this is the
multi-tenant security boundary).

**Action**: Phase H is the test phase per REBUILD. Don't ship to Dokploy without it.
For E2E: Playwright (per ECC web/testing.md priority: visual regression, a11y, perf).

## Files to read FIRST (the contract)

In this order:

1. **`30_Business_OS/10_Projects/omk/apps/dashboard/REBUILD_WORKFLOW.md`** — THE
   CONTRACT. 7.4KB, 8 phases A→H, SQL DDL for `omk_internal` + `omk_saas` schemas,
   4 named blockers, garde-fous. **This is the source of truth for WHAT to build.**
2. `30_Business_OS/10_Projects/omk/apps/dashboard/picard_audit.md` — superseded
   May 25 audit (score 41/100). Useful for context on the original 7 defects (D01-D07)
   but **périmé sur la modularisation** (already done in commit `4a1c6b3`).
3. `20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/CERRIROS_HANDOVER.md`
   — doctrine junction, routing chain Jerry → Cerritos → Picard/Summer
4. `20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/SUMMERS_VERSE_MANIFEST.md`
   — B1 vision, 1y/3y/10y, ICP variant rules
5. `30_Business_OS/10_Projects/omk/apps/dashboard/package.json` — Vite 6 + React 19 +
   Supabase + react-router-dom 7 + @google/genai
6. `30_Business_OS/10_Projects/omk/apps/dashboard/.env.example` — env contract
   (`VITE_APP_MODE`, `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY`, `GEMINI_API_KEY`)
7. `30_Business_OS/10_Projects/omk/apps/dashboard/src/config/mode.ts` — dual-mode
   runtime (`internal` | `saas`)
8. `30_Business_OS/10_Projects/omk/apps/dashboard/src/lib/supabase.ts` — schema-aware
   Supabase client (`db.schema` switches on `VITE_APP_MODE`)

## Quick start commands

```powershell
# 1. Clone the project (or navigate if local)
cd "C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\omk\apps\omk-dashboard"

# 2. Install deps
npm install

# 3. Set env (copy from .env.example, fill in real values)
cp .env.example .env
# Edit .env: VITE_APP_MODE=internal, VITE_SUPABASE_URL, VITE_SUPABASE_ANON_KEY, GEMINI_API_KEY

# 4. Run dev (Vite, port 3000 — NOT 5173 to avoid conflict with Next.js apps)
npm run dev
# → http://localhost:3000

# 5. Lint (TypeScript no-emit)
npm run lint

# 6. Build production
npm run build

# 7. Run prod locally (Express serves dist/)
node server.js
# → http://localhost:3000 (or PORT env)
```

## Deploy workflow (per `REBUILD_WORKFLOW.md` Phase G)

**Target: Dokploy, NOT Vercel.**

The 2 services to deploy (per REBUILD Phase G):
- `omk-dashboard-internal` — `VITE_APP_MODE=internal` → routes to `omk_internal` schema
- `omk-dashboard-saas` — `VITE_APP_MODE=saas` → routes to `omk_saas` schema

These are 2 separate Dokploy services with:
- Distinct env vars (Supabase URL/key per service, mode baked at build)
- Caddy/Traefik routing to distinct subdomains
  (e.g. `omk-internal.aspace.fr` and `omk-saas.aspace.fr`)

**Vercel project `prj_FJpNDykkNMhDJUEg2FvKAegeeQG3` is UNUSED.** Per ticket #6, do
NOT link GitHub to it. Optionally archive via `mcp__vercel__archive_project`.

**Dokploy setup steps** (one-time):
1. Create 2 services in Dokploy panel
2. Point each to a branch/tag in `github.com/Amdkn/01-OMK-Business-OS`
3. Set env vars in Dokploy (NEVER commit `.env` with real values)
4. Configure Caddy/Traefik subdomains
5. Smoke test: login, CRUD scoped, **test isolation org A vs org B** (Phase H gate)

## Gotchas (read these before editing)

1. **Dual-mode runtime** — `VITE_APP_MODE` is baked at `vite build` time. Switching
   mode requires a rebuild, not a runtime toggle. Keep 2 Dokploy services (per Phase G)
   rather than 1 service with runtime switching.
2. **`SERVICE_ROLE_KEY` NEVER client-side** — `VITE_*` env vars are public-bundled.
   The service role key must stay server-side (use it in a server function or
   scheduled job, NOT in the Vite app).
3. **Self-hosted Supabase at `https://supabase.148.230.92.235.sslip.io`** — this is
   NOT `supabase.com` cloud. The receiving session needs the real anon key (in env
   User Windows, not committed) before Phase B.
4. **JWT custom access token hook** — required for saas RLS. The hook reads
   `memberships` table and injects `org_id` into the JWT. The RLS policy
   `org_id = (auth.jwt() ->> 'org_id')::uuid` is the security boundary. If the hook
   is misconfigured, EVERY saas query returns empty (or worse, leaks data).
5. **PGRST_DB_SCHEMAS reload** — after creating `omk_internal` and `omk_saas`
   schemas, the `supabase-core` service on VPS must be restarted (or PostgREST
   reloaded) to pick up the new schemas. This is a **human-in-the-loop** step
   (Codex/Hermes on VPS), per ADR-SUPABASE-001 D7.
6. **Vite dev server runs on port 3000** (not 5173 default) to avoid conflict with
   Next.js apps in the same monorepo.
7. **Express server in `server.js`** for production. The Docker container runs
   `node server.js`, NOT `vite preview`. The Express server serves `dist/` with
   SPA fallback + `/healthz` healthcheck.
8. **`src/lib/constants.ts` is hardcoded mock data** — to wire Phase D, rename to
   `seed.ts` and restrict to dev/seed flow. The 7 views should branch on
   repositories, not constants.
9. **The TypeScript rules in `~/.claude/rules/ecc/typescript/` are auto-loaded** in
   every session — follow them (no `any`, immutable updates, Zod for input
   validation, no `console.log` in production, Playwright for E2E).
10. **No Vercel reserved-path issues here** (OMK is Vite, not Next.js) — but the
    `/healthz` path used by Express should be the FIRST route registered, before
    SPA fallback, to avoid `index.html` being served for the healthcheck.

## Recommended order of work (D1 — verify before assert on each step)

1. **Triage the 4 ADR blockers** with A0 — open a dedicated ADR-ratification
   session. Without these, every later phase is blocked.
2. **Write `AGENTS.md`** for `omk-dashboard/` — encode the contract from this
   handoff + the 4 blockers + the dual-mode runtime + the RLS pattern.
3. **Rewrite `README.md`** — OMK-specific content, link to REBUILD_WORKFLOW.md.
4. **Ticket #2** — split `lib/constants.ts` into `seed.ts` + complete `types.ts`
   with `Organization` and `Membership`. (Type work unblocks Phase D.)
5. **Phase A cleanup** — verify `npm run lint` GREEN, then move to Phase B.
6. **Phase B** — create Supabase schemas (requires supabase-aspace MCP). HITL
   step: reload PGRST_DB_SCHEMAS on VPS.
7. **Phase C** — AuthProvider + useAuth + LoginView/SignupView + JWT hook. Replace
   "Admin User" hardcoded.
8. **Phase D** — Repositories (5 entities) + branch 7 views + loading/empty/error
   states.
9. **Phase E** — Routing via react-router-dom 7. Sidebar → `<NavLink>`.
10. **Phase F** — Verify `server.js` + `Dockerfile` work end-to-end (`docker build`
    + `docker run`).
11. **Phase G** — Deploy 2 services to Dokploy. Configure Caddy/Traefik
    subdomains. Run smoke test.
12. **Phase H** — Adversarial RLS test. README final. Commit + push. MAJ
    `30_MEMORY_CORE/README.md` + register schemas in `agents_registry.json`.

## Verification (D5 — proof on file)

After each phase, prove it works:

| Phase | Verification |
|-------|--------------|
| A | `npm run lint` (tsc --noEmit) GREEN, `npm run dev` shows dashboard at :3000 |
| B | `psql $SUPABASE_URL -c "SELECT schema_name FROM information_schema.schemata WHERE schema_name LIKE 'omk%'"` returns both schemas; `generate_typescript_types` produces non-empty `src/lib/database.types.ts` |
| C | `useAuth().session` is non-null after login; `useAuth().orgId` matches `memberships.org_id` for current user |
| D | 7 views load from Supabase (not constants); refresh page → data persists; create/update/delete round-trips |
| E | Browser URL changes when navigating sidebar; refresh on `/clients` shows clients tab |
| F | `docker build` + `docker run` → `curl http://localhost:3000/healthz` returns 200; SPA loads at `/` |
| G | Login on `omk-internal.aspace.fr` works, login on `omk-saas.aspace.fr` works, both reach Supabase |
| H | **Adversarial RLS test**: create 2 orgs + 2 users; user A's session cannot read org B's clients (via browser DevTools or `psql` test) |

## Write back to the source session (and the wiki)

When meaningful work is done, append a one-liner to:

1. `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` under `[2026-06-10]` (or new date).
2. `00_Amadeus/30_MEMORY_CORE/README.md` same date bullet.
3. `30_Business_OS/10_Projects/omk/apps/omk-dashboard/REBUILD_WORKFLOW.md` → update
   the "État vérifié" table as phases complete.
4. `30_Business_OS/10_Projects/omk/apps/omk-dashboard/AGENTS.md` (when created) →
   update the Work Guidance / open tickets as items close.

## Residual risks

- **4 ADR blockers** — the rebuild is fully blocked until these are ratified.
  This is the highest-leverage decision for the receiving session.
- **Self-hosted Supabase coupling** — the entire app depends on the VPS Supabase
  being up. If the VPS is down, the dashboard is down. No fallback to local-only
  mode is wired yet (Phase D would need a `localStorage` fallback that the data
  layer already has, per commit `70efe01`).
- **No tests** — Phase H is the test phase, but the receiving session should
  consider adding unit tests for repositories (mock Supabase client) and Playwright
  E2E for the 7 view navigation + auth flow.
- **Dual Dokploy service complexity** — 2 services with 2 subdomains is more ops
  surface than 1. The dual-mode was a clean architectural choice, but ops cost is
  real. Consider whether 1 service with `VITE_APP_MODE` runtime switch (and a
  strict server-side org check) is viable for OMK's scale.
- **No dark/light theme persistence** — the dashboard does not have theme
  switching yet. Add via `useLocalStorage` hook (already exists) or `next-themes`-style
  library when the time comes.
- **JWT custom hook is single-point-of-failure** — if the Supabase auth hook fails
  to inject `org_id`, every saas RLS query returns 0 rows. This is silent failure;
  add a `console.warn` if `auth.jwt() ->> 'org_id'` is null in saas mode.
- **The `@google/genai` dep is installed but unused in current code** — Phase D
  or later may add AI features. Verify the API key is real before building
  features on top.

## Next safe action for the receiving session

1. Read this handoff end-to-end.
2. Read `REBUILD_WORKFLOW.md` end-to-end (the contract).
3. Read the 8 files listed in `## Files to read FIRST` (in order).
4. **Open an ADR-ratification session with A0** for the 4 blockers — this is
   the highest-leverage action and unblocks everything else.
5. After ADRs are ratified, resume from Phase A cleanup (verify `npm run lint`).
6. Report progress back via the wiki log + README + REBUILD_WORKFLOW.md.

## Skill proposal (open follow-up)

The "OMK rebuild" workflow (lift 4 ADRs → Supabase schemas → AuthProvider → repos
→ routing → Docker → Dokploy → RLS test) is a recurring pattern that may apply
to other Supabase + React + multi-tenant apps. Consider creating a
`/supabase-multi-tenant-rebuild` skill that encapsulates:
- The 4-ADR pre-flight (data, auth, deploy, MCP)
- The schema DDL templates (`omk_internal` + `omk_saas` + RLS policies)
- The JWT custom hook setup
- The adversarial RLS test pattern
- The Dokploy 2-service deploy pattern

Queue: `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/skills_queue.md`.

## Secret handling

- `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY` are PUBLIC (bundled in JS).
  Safe to put in `.env.example` as placeholder + real in Dokploy env.
- `GEMINI_API_KEY` is PUBLIC (Vite bundles it). Rotate if exposed.
- `SUPABASE_SERVICE_ROLE_KEY` is **NEVER** client-side. Server-side only.
- Dokploy API key + Hostinger API token (per system state 2026-06-10) are
  exposed — flagged for rotation by A0. Do NOT echo values in chat/code/logs.
- Use env User Windows for long-term durable secrets (`.env` files in the repo are
  gitignored, env User survives repo clones).
