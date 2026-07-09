# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Identity

**Alikaly Bana Holding** — sovereign surplus-funds recovery operation (Hamilton County, OH court cases), structured as a two-app monorepo under A'Space OS V2 Business OS (L2 / Project Picard).

- **Doctrine anchor (junction)**: `_doctrine/` → symlink to `20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/04 Alikaly Bana Holding to LLC/` (the actual PARA Projects home for the project; doctrine lives deep, not in repo).
- **Architecture canon**: `ADR-INFRA-002` (Repo-Home / Junction pattern) + `ADR-INFRA-003` (CEO Dashboard) + Picard Audit (`apps/os/picard_audit.md`).
- **Repo-home rule** (ADR-INFRA-002): build-bearing code lives short (here, in `apps/`); doctrine stays deep. The `_doctrine` symlink is the junction that connects the two.

## Repo Layout

```
alikaly/
├── _doctrine → 20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/04 Alikaly Bana Holding to LLC/  # symlink (doctrine, junction)
└── apps/
    ├── holding/  # Alykaly Holding — public marketing site (alykaly.kalybana.com)
    │   ├── Next.js 16.2 + React 19 + Tailwind v4
    │   ├── Vitest + Testing Library (jsdom)
    │   ├── src/app/{layout,page}.tsx + globals.css
    │   ├── src/components/{layout,marketing,widgets}/
    │   └── src/lib/utils.ts (cn helper)
    │
    └── os/        # Alykaly OS — sovereign operations console (alykaly.kalybana.com internal)
        ├── Next.js 15.1 (App Router) + React 19 + Tailwind v4
        ├── Supabase (Postgres + Auth + Storage + Edge Functions + Realtime)
        ├── Supabase: 5 schemas (app, crm, identity, ops, audit) + 10 migrations + 5 Deno edge functions
        ├── src/app/{api,auth,page,layout,template}.tsx
        ├── src/components/{Sidebar,Dashboard,Finance,People,Docket,Clients,Legal,Knowledge,Growth,SalesSanctum,SystemRoots,Settings,Header,Footer,Hero,Icon,StitchWidget,bana/}
        ├── src/lib/{actions,store,utils,supabase/{server,client,admin,types}}.ts
        ├── src/middleware.ts (Supabase auth gate, PUBLIC_PATHS bypass)
        ├── Dockerfile (multi-stage, port 4444)
        ├── docs/DEPLOYMENT_RUNBOOK.md (Phase A→G full flow)
        ├── SUPABASE_STRATEGY.md (60K spec — architecture, RLS, money types, soft-delete, CDC)
        ├── picard_audit.md (Vite→Next.js migration audit, Phase 1-4 blueprint)
        └── deploy/{bootstrap-local-supabase.ps1, push-to-selfhost.ps1, hostinger.sh}
```

## Common Commands

### `apps/holding` (Next.js 16 marketing site)

```bash
cd apps/holding
npm install
npm run dev      # http://localhost:3011
npm run build    # production build
npm run start
npm run lint     # next lint (eslint config: eslint-config-next)
npm run test     # vitest run (jsdom env, setupFiles: src/test/setup.ts)
npm run clean    # rimraf .next node_modules
```

### `apps/os` (Next.js 15 sovereign console)

```bash
cd apps/os
npm install
npm run dev      # http://localhost:3000 (or 4444 via $PORT)
npm run build    # standalone output (next.config.ts output: 'standalone')
npm run start
npm run lint
```

### Supabase local stack (apps/os only)

```powershell
# One-shot bootstrap: Docker check + supabase start + db reset + print creds
cd apps/os
powershell -ExecutionPolicy Bypass -File .\deploy\bootstrap-local-supabase.ps1

# Then copy creds from `supabase status` into .env.local
# Supabase Studio: http://127.0.0.1:54323
```

### Deploy flows (apps/os)

- `deploy/bootstrap-local-supabase.ps1` — local dev stack
- `deploy/push-to-selfhost.ps1` — `supabase db push` + edge fns + types gen to `supabase.kalybana.com`
- `deploy/hostinger.sh` — `npm ci && npm run build && rsync` to Hostinger app root; expects `$APP_ROOT` env var; hPanel restart afterwards

## Key Architectural Patterns

### Dual-app monorepo (Picard doctrine)

- **`holding/`** = public marketing/landing (Conversion surface — Hero, PromiseBar, Expertises, Methode, ClosingCTA). Pure client, no Supabase in code; "Admin Login" is visual-only per Picard audit.
- **`os/`** = sovereign operations console (Dashboard, Finance, People, Docket, Clients, Legal, Knowledge, Growth, Sales, Settings, plus public `/bana` intake landing).
- Both target `alykaly.kalybana.com` via Hostinger Node.js app, but `os/` is the "internal" console (Supabase-backed) while `holding/` is the "public conversion" surface. Public Bana intake lives under `os/src/app/bana/` (sibling marketing route inside the console).

### Supabase tenancy model (apps/os)

- **Hybrid tenancy**: every business table has `org_id TEXT DEFAULT 'alykaly'` (per ADR-OMK-001 dual-product doctrine — this is one tenant of the multitenant model).
- **5 schemas**: `app` (core: cases, clients, transactions, knowledge_docs, intake_submissions), `crm` (sales_pipeline_items, court_filings, feed_events, kanban views), `identity` (profiles, clearance), `ops` (agents, wind_direction_alerts), `audit` (audit.log).
- **PII clearance levels**: `level_0_public` → `level_5_sovereign`; RLS policies enforce both `org_id` and `clearance_required`.
- **Money**: `NUMERIC(14,2)` everywhere (never `FLOAT`).
- **Soft-delete**: `deleted_at TIMESTAMPTZ`; queries in `actions.ts` filter `is('deleted_at', null)`.
- **Realtime CDC**: `supabase_realtime` publication covers 6 tables (cases, transactions, sales_pipeline_items, court_filings, feed_events, wind_direction_alerts) → Dashboard live updates.
- **Auth**: Supabase Auth (GoTrue) with custom JWT claims; `src/middleware.ts` gates everything except `PUBLIC_PATHS` (`/bana`, `/api/intake`, `/api/engine`, `/auth`, `/_next`, `/favicon.ico`).

### Server Actions pattern (apps/os)

`src/lib/actions.ts` is the single chokepoint for all DB reads. Every function:
1. Creates server client via `createSupabaseServerClient()`.
2. Scopes query to a schema explicitly (`supabase.schema('app')`, `supabase.schema('crm')`, `supabase.schema('ops')`).
3. Filters `is('deleted_at', null)` for soft-deletable tables.
4. Logs error with `console.error('[fnName]', error)`, returns `null` / `[]` / empty kanban (never throws).
5. RPCs for aggregates: `app.dashboard_kpis()`, `app.dashboard_pipeline_weekly()`.

### Edge Functions (Deno, apps/os/supabase/functions/)

| Function | JWT verify | Role |
|---|---|---|
| `sob-engine-simulate` | false | SOB Engine™ live exposure calc (public demo) |
| `intake-handler` | false | Bana intake web form ingestion (public) |
| `docusign-webhook` | false (HMAC) | DocuSign signature events |
| `case-confidence-recalc` | true | Daily cron 06:00 UTC |
| `audit-rotate` | true | Weekly Monday 03:00 UTC |

### Middleware (apps/os)

`src/middleware.ts` is the auth gate. **Critical pattern**: if `NEXT_PUBLIC_SUPABASE_URL` or `NEXT_PUBLIC_SUPABASE_ANON_KEY` are missing (build/dev without Supabase), middleware short-circuits to `NextResponse.next()` — this lets `npm run build` succeed offline.

### Storage (apps/os)

3 buckets: `documents-private` (case docs), `intake-attachments` (Bana form files), `marketing-public` (logos, public assets).

### Bana public intake flow

`/bana` is the public landing for new clients (inside `os/` app). Form submission goes through `submitIntake()` server action → `app.intake_submissions` row + optional `N8N_WEBHOOK_URL` outbound. Public, no auth required, RLS-by-design via `app.intake_submissions` INSERT policy.

## Critical Conventions

### Next.js versions differ between apps

This is **NOT the Next.js you know** — `apps/holding` is on Next 16.2, `apps/os` is on Next 15.1. Per `apps/holding/AGENTS.md` (which `@import`s `CLAUDE.md`):

> APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.

**Both apps are non-trivial departures from older Next.js patterns** — always read the local `node_modules/next/dist/docs/` first.

### TypeScript strict mode

Both apps: `"strict": true`, `noEmit`, `moduleResolution: "bundler"`, `@/*` path alias → `./src/*`. No `any`; `unknown` + narrowing required.

### Standalone output (apps/os only)

`next.config.ts` has `output: 'standalone'`. The `hostinger.sh` deploy script verifies `.next/standalone/server.js` exists, then rsyncs `.next/standalone/`, `.next/static/`, and `public/` to the Hostinger app root. Startup file in hPanel = `server.js`.

### No secrets in repo

`SUPABASE_SERVICE_ROLE_KEY`, `DOCUSIGN_WEBHOOK_SECRET`, etc. live in `.env.local` (gitignored) for dev and in hPanel env vars for prod. Never commit.

### ASCII / i18n

- `apps/holding` is `lang="fr"` (FR-first marketing — récupération de fonds, Hamilton County OH).
- `apps/os` is `lang="en"` (internal console).
- Catalog i18n follows the ABC-OS doctrine: EN default, FR drift to be normalized (see ABC-OS ADR-ABCOS-001 D10 mixed-tenancy).

## Environment Variables (apps/os)

| Var | Required | Notes |
|---|---|---|
| `NEXT_PUBLIC_SUPABASE_URL` | yes (runtime) | Local: `http://127.0.0.1:54321` · Prod: `https://supabase.kalybana.com` |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | yes (runtime) | From `supabase status` or self-host dashboard |
| `SUPABASE_SERVICE_ROLE_KEY` | yes (runtime) | Server-only, bypasses RLS |
| `SUPABASE_JWT_SECRET` | optional | Token verification |
| `N8N_WEBHOOK_URL` | optional | Outbound webhook from `submitIntake` |
| `DOCUSIGN_WEBHOOK_SECRET` | optional | HMAC for docusign-webhook edge fn |
| `PORT` | yes (Hostinger) | Default 4444 |
| `HOSTNAME` | yes (Hostinger) | `0.0.0.0` |
| `NEXT_TELEMETRY_DISABLED` | yes (prod) | `1` |

## Acceptance Criteria (gating deploy per SUPABASE_STRATEGY.md §14)

- **AC-01** Schema deployed — 15+ tables visible in `supabase db diff --linked`
- **AC-02** RLS — `viewer` role cannot INSERT into `app.cases`
- **AC-03** Clearance — `level_1` user cannot see `clearance_required = 'level_5_sovereign'` rows
- **AC-04** Intake — anon `POST /api/intake` succeeds, row visible in Studio
- **AC-05** SOB Engine — `sob-engine-simulate` returns `global_exposure` live
- **AC-06** Refactor — `getActiveCases()` returns ≥ 5 rows (seed)
- **AC-07** Realtime — modify `app.cases.status` in Studio → Dashboard refreshes without reload
- **AC-08** Deploy — `https://alykaly.kalybana.com` returns 200, login works
- **AC-09** Audit — DELETE on `app.cases` generates a row in `audit.log`
- **AC-10** Backup — `pg_dump` succeeds, restore on test DB passes

## Common Pitfalls

- **Middleware blocks `npm run build` if env vars set but Supabase unreachable** — keep `.env.local` unset for offline builds, or rely on the short-circuit logic in `src/middleware.ts`.
- **`esModuleInterop` + `moduleResolution: "bundler"`** — both apps use this combo; do not import CJS modules via default.
- **Tailwind v4** in both apps — config is CSS-based (`@tailwindcss/postcss`), not `tailwind.config.js`. Theme tokens live in `globals.css` via `@theme` blocks.
- **`lucide-react` versions differ**: `apps/holding` is on `1.16.0` (very old fork-style), `apps/os` is on `0.546.0` (the real one). Icon imports are not interchangeable.
- **Picard audit gaps** (Phase 2-4 still open): SEO metadata, self-hosted fonts, real Supabase data, SOB Engine API endpoints, Docker multi-stage, CI/CD. The current `os/` is past Phase 1 (Vite→Next.js) and into Phase 3 (Supabase-backed).
- **Hostinger app root is uXXX-specific** — never hardcode the path; pass via `$APP_ROOT` env var to `hostinger.sh`.

## Related ADRs / Doctrine (read before changing architecture)

- `ADR-INFRA-002` Repo-Home/Junction — `_doctrine` symlink doctrine
- `ADR-INFRA-003` CEO Dashboard — apps/ structure
- `ADR-OMK-001` dual-product deployment — multitenant `org_id` pattern
- `ADR-META-001` Doctrine Anti-Paresse — D1-D8 verification, no narrative shipping
- `apps/os/SUPABASE_STRATEGY.md` — full Supabase spec (RLS, money types, soft-delete, CDC, tenancy, edge fns)
- `apps/os/picard_audit.md` — Vite→Next.js migration history
- `apps/os/docs/DEPLOYMENT_RUNBOOK.md` — Phase A→G deploy flow
