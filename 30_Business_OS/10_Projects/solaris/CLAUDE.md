# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> **Repo root**: `30_Business_OS/10_Projects/solaris/`
> **GitHub** (dashboard, per REBUILD_WORKFLOW): `github.com/Amdkn/00-AaaS-Agency-Garden`
> **Doctrine anchor**: ADR-INFRA-002 (Repo-Home, short build-bearing) · ADR-SUPABASE-001 · ADR-OMK-001 · ADR-META-001

## ⚠️ Read `AGENTS.md` BEFORE writing any `.ts`/`.tsx`

Both `apps/dashboard/AGENTS.md` and `apps/landing/AGENTS.md` declare:

> *This is NOT the Next.js you know. This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.*

**Next 16.2.6 is bleeding edge.** Do not import patterns from training-data memory; consult the bundled docs first. This applies to the per-app `node_modules/next/dist/docs/` only — the apps are independent (each has its own `node_modules`).

## Monorepo layout

Two independent Next.js apps. **No root `package.json`, no workspace tool.** Operate inside one app at a time:

| App | Path | `name` | Stack | Dev port | Build artifact |
|-----|------|--------|-------|----------|----------------|
| **dashboard** | `apps/dashboard/` | `aaas-os` | Next 16.2.6 + React 19.2.4 + TS 5 + Tailwind v4 + Supabase self-hosted | `3000` | `.next/standalone/` (Dokploy) |
| **landing** | `apps/landing/` | `solaris-aaas` | Next 16.2.6 + React 19.2.4 + TS 5 | `3000` (or `3001` when both run) | default `.next/` |

The two apps share **zero** code at the package level. They live in the same directory only because the AaaS product = public landing + private dashboard.

## Commands (per app)

```bash
cd apps/dashboard        # or apps/landing
npm run dev              # next dev
npm run build            # next build  (dashboard → .next/standalone/ for Dokploy)
npm run start            # next start  (after build)
npm run lint             # eslint
npx tsc --noEmit         # type check (no test runner wired)
```

**There is no test command** in either `package.json` — Playwright E2E is planned in dashboard's REBUILD_WORKFLOW Phase H but not yet wired. Type-check + lint is the only automated gate. When introducing tests, follow the `common/testing.md` global rules (unit + integration + E2E, 80% coverage).

## Big-picture architecture

### Dashboard — dual-product, multi-tenant

The dashboard is one product running in two modes, switched by `NEXT_PUBLIC_APP_MODE`:

- **`internal`** — AaaS staff uses the same UI to manage clients (single-tenant, schema `solaris_internal`).
- **`saas`** — SMB clients log in, see only their own data (multi-tenant, schema `solaris_saas`, RLS scoped by JWT `org_id` claim).

Mode is resolved server-side in `apps/dashboard/src/config/mode.ts` and re-validated by the JWT. The mode **must not** be inferred from the client alone — a client claim is a UI hint, the server is the source of truth (REBUILD_WORKFLOW §4).

The 12 business views (Dashboard, Finance, Clients, Tasks, SOP, Legal, Growth, Marketplace, Sales, ItData, People, Settings) sit in `src/components/views/` and are mirrored by `src/components/skeletons/` + `src/components/empty-states/`. Data flows through a `.client.ts` / `.server.ts` repo split under `src/repos/` — every server-side repo is RLS-scoped (the `org_id` is read from the session in `src/middleware.ts`, forwarded as `x-tenant-org-id`, enforced by Supabase RLS).

Auth is full Supabase (`@supabase/ssr` browser + server, `@supabase/supabase-js` for service-role contexts only) with `signIn` / `signUp` / `signOut` server actions, an OAuth + magic-link `callback` route, and a `useSessionContext()` hook exposing `{ session, user, orgId, role, isStaff, isSaas, isInternal, mode, loading }`. Supabase is **self-hosted on the VPS `aspace-vps`**, not Supabase Cloud. MCP names: `supabase-solaris` (read, anon) and `supabase-aspace` (write, `aspace_admin`).

### Landing — public, single-tenant

A marketing site (10 sections + 4 diagrams) at `apps/landing/src/components/{sections,diagrams}/`. The lead-capture CTA posts to `apps/landing/src/app/api/leads/route.ts`, which validates, dedupes via honeypot, captures UTM/referrer, and persists to Supabase `public.leads` (canonical) or `.data/leads.jsonl` (dev fallback when env is absent). See `apps/landing/LEADS_SETUP.md`.

## Per-app CLAUDE.md = stubs

`apps/dashboard/CLAUDE.md` and `apps/landing/CLAUDE.md` contain only `@AGENTS.md` — they inherit the breaking-changes warning and the global A'Space doctrines. App-specific notes (e.g. "view skeletons must mirror view name") belong in the app's `AGENTS.md`, not in those stubs. This root CLAUDE.md is the cross-app map.

## Playbook files (read first when picking up work)

| File | Read when |
|------|-----------|
| `apps/dashboard/REBUILD_WORKFLOW.md` | Touching the dashboard. 8 phases (A foundations → H tests isolation) with strict scope per phase. Bloquants status table in §6. |
| `apps/dashboard/picard_audit.md` | Initial dashboard audit (2026-05-25, 28/100 → ~85% now). |
| `apps/landing/picard_audit_solaris.md` | Landing audit (2026-05-17, 31/100 → 82/100). |
| `apps/landing/LEADS_SETUP.md` | Editing the lead form, leads env, or storage fallback. |
| `_doctrine/` (symlink) | Business canon: B1 direction, B2 domains (8 SOA), B3 warps. Solaris JTBDs live here: `JTBD-002_SOLARIS_ICP_FILTER.md`, `JTBD-003_SOLARIS_PAINKILLER_VARIANTS.md`. Read-only — never modify. |

## Deploy: Dokploy (Track B), not Vercel

- **Dashboard**: Dockerfile (`apps/dashboard/Dockerfile`) is multi-stage `node:20-alpine`, consumes `.next/standalone/` because `next.config.ts` sets `output: 'standalone'`. Two Dokploy services will run — one per `NEXT_PUBLIC_APP_MODE` — with separate Supabase env and Caddy routes.
- **Landing**: no Dockerfile yet. `picard_audit_solaris.md` planned both Vercel (Track A) and Dokploy (Track B); Vercel is an **anti-pattern** for the sovereign track. Migrate to Dokploy before any prod traffic.
- Image base: `node:20-alpine` (Next 16 requires Node ≥ 20). Do not downgrade to Node 18.

## Doctrine bindings (repo-specific restatements)

The global `~/.claude/CLAUDE.md` has the full list. These are the ones a slip in *this* repo would cost real damage:

- **D1 Verify-Before-Assert** (ADR-META-001) — The dashboard was 85% built when it looked empty. Read the file. Trust filesystem, not memory or handoff summaries.
- **Test Key Pragma** — `apps/dashboard/.env.example` and `apps/landing/.env.example` ship with placeholder strings. **Never** paste real keys into `.env.example`, `.md`, `.json`, or `git`. Real values go in `.env.local` (gitignored) or Dokploy env. The "Test Key" lifecycle is: paste in chat → set env var → curl smoke test → rotate in the source service.
- **No-hard-delete** — Move to `_TRASH/`, never `Remove-Item` without A0 sign-off. The Trust Zone itself is in `C:\Users\amado\`.
- **Repo-Home short** (ADR-INFRA-002) — Solaris lives short under `30_Business_OS/10_Projects/solaris/`. Do not nest another build-bearing repo inside it.
- **Migration scope discipline** (REBUILD_WORKFLOW §4) — Each dashboard phase has strict scope. Read the phase before opening it; do not bundle unrelated edits.
- **Auth gate** — Dashboard home (`/`) is still reachable without auth in the current phase; the route gate applies once each view is moved to its own URL (REBUILD_WORKFLOW Phase D-DX).
