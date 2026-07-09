# Alikaly Bana Holding OS — V2

**Sovereign Operations Console** for surplus funds recovery + asset recovery
business (Texas court cases). Powered by Next.js 15 (App Router) + Supabase
(Postgres + Auth + Storage + Edge Functions + Realtime), deployed on
Hostinger Business via Node.js Application.

## Status

| Component | Status |
|---|---|
| Next.js 15 App Router | ✅ |
| Tailwind v4 | ✅ |
| Supabase schema (15+ tables, 6 schemas) | ✅ Migrations posées |
| RLS policies | ✅ 25+ policies |
| Edge Functions | ✅ 5 functions (sob-engine, docusign, intake, recalc, audit-rotate) |
| Storage buckets | ✅ 3 buckets (documents-private, intake-attachments, marketing-public) |
| Realtime CDC | ✅ Migration 010 |
| Auth flow (login + middleware) | ✅ |
| `actions.ts` Supabase-backed | ✅ |
| Build standalone | ✅ |
| Deploy Hostinger | ⏳ pending A0 SSH/Git config |
| Push to self-host `supabase.kalybana.com` | ⏳ pending A0 db URL |

## Quick Start

### Prérequis
- Node 22 (`node --version`)
- Docker Desktop running (pour Supabase local)
- Supabase CLI (`supabase --version`)

### Local dev (Supabase Docker)

```powershell
# 1. Bootstrap Supabase local (migrations + seed)
powershell -ExecutionPolicy Bypass -File .\deploy\bootstrap-local-supabase.ps1

# 2. Copy credentials from `supabase status` output into .env.local
cp .env.example .env.local
# ... edit .env.local with anon + service_role keys

# 3. Run Next.js
npm install
npm run dev
```

App : http://localhost:4444
Supabase Studio : http://127.0.0.1:54323

### Production deploy

Voir [`docs/DEPLOYMENT_RUNBOOK.md`](docs/DEPLOYMENT_RUNBOOK.md) pour le flow complet
local → self-hosted Supabase → Hostinger.

## Architecture

```
Hostinger Business (alykaly.kalybana.com)
   └── Node.js App (Passenger/LiteSpeed)
       └── Next.js 15 standalone (server.js)
                 │
                 ▼
   Supabase self-hosted (supabase.kalybana.com)
       ├── Postgres + RLS (5 schemas: app, crm, identity, ops, audit)
       ├── Auth (GoTrue, JWT custom claims)
       ├── Storage (3 buckets)
       ├── Edge Functions (5 Deno functions)
       └── Realtime (CDC on 6 tables)
```

## Key files

| Path | Role |
|---|---|
| [`SUPABASE_STRATEGY.md`](SUPABASE_STRATEGY.md) | Spec complète (architecture + decisions) |
| [`picard_audit.md`](picard_audit.md) | Audit migration initial Vite → Next.js |
| [`docs/DEPLOYMENT_RUNBOOK.md`](docs/DEPLOYMENT_RUNBOOK.md) | Runbook deploy étape par étape |
| `supabase/migrations/*.sql` | 10 migrations SQL versionnées |
| `supabase/functions/*/index.ts` | 5 Edge Functions Deno |
| `supabase/seed.sql` | Seed dev (cases, agents, knowledge, alerts) |
| `supabase/config.toml` | Config Supabase local |
| `src/lib/supabase/{server,client,admin,types}.ts` | Clients Supabase + types |
| `src/lib/actions.ts` | Server Actions Supabase-backed |
| `src/middleware.ts` | Auth gate (PUBLIC_PATHS bypass) |
| `src/app/auth/login/page.tsx` | Login form |
| `src/app/auth/callback/route.ts` | OAuth callback handler |
| `src/app/api/engine/status/route.ts` | Proxies sob-engine-simulate edge fn |
| `src/app/api/intake/route.ts` | Proxies intake-handler edge fn |
| `deploy/bootstrap-local-supabase.ps1` | Boot Supabase Docker + apply migrations |
| `deploy/push-to-selfhost.ps1` | Push migrations + edge fns to prod |
| `deploy/hostinger.sh` | Build + rsync to Hostinger app root |
| `.env.example` | Template env vars |

## Dev commands

```bash
npm run dev      # Dev mode (port 4444)
npm run build    # Production build → .next/standalone/server.js
npm run start    # Run standalone build locally
npm run lint     # Next.js lint (needs eslint installed: npm i -D eslint)
```

## Doctrinaux

- Tenancy **hybride** : `org_id TEXT DEFAULT 'alykaly'` sur toutes tables business
- PII **standard + clearance levels** (level_0 → level_5)
- Money en `NUMERIC(14,2)` partout
- Soft-delete via `deleted_at TIMESTAMPTZ`
- Audit log append-only sur tables sensibles
- RLS activée sur **toutes** les tables business
- Realtime CDC sur 6 tables (Dashboard live updates)

Voir [`SUPABASE_STRATEGY.md`](SUPABASE_STRATEGY.md) §3-§9 pour le détail.
