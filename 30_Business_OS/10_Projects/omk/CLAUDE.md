# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in the **OMK Services Business OS** project.

> **Project root** : `C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\omk\`
> **Parent context** : `ASpace_OS_V2/CLAUDE.md` (sovereign OS, doctrine, ADR canon, L0–L2 layers)
> **Repo** : `github.com/omk-services/00-omk-saas-os` (canon unique, décarbonné Amdkn 2026-06-19, branch main). Ancien `Amdkn/01-OMK-Business-OS` supprimé par A0 (H1 LOCKED : 1 repo canon = 1 source de vérité). Per **ADR-OMK-004 RATIFIED 2026-06-19**, single SaaS mode, Vercel deploy.

---

## What this project is (and is not)

This is **OMK Services Business OS** — the staff/operator dashboard for a Paris-based services firm, productized for SaaS. It is **a rebuild, not a migration**: the contract lives in `apps/dashboard/REBUILD_WORKFLOW.md` (8 phases A→H, SQL DDL, 4 ADR blockers).

**Stakeholder** : OMK Services (single-tenant today, future-proofed for multi-tenant SaaS).

---

## The 2 apps

| App | Path | Stack | Status | Git? | Deploy? |
|-----|------|-------|--------|------|---------|
| **`omk-dashboard`** (target dev) | `apps/dashboard/` | Vite 6.2 · React 19 · TS 5.8 · Tailwind v4 · `@supabase/supabase-js` 2.107 · `react-router-dom` 7 · `motion` · `lucide-react` · `@google/genai` · `express` (prod) | Phase A+B(D)+E(F)+G(Vercel READY), C+H pending | ✅ `omk-services/00-omk-saas-os` (canon unique post-Amdkn-delete) | ✅ **Vercel** (team `omk-services`, project `omk-saas-os`, dpl_G4vkAKCVR9BG4ZA3qmDjJ5hEHuyq, prod READY) |
| `omk-landing` (dormant) | `apps/landing/` | Next.js 16.2.6 · React 19 · Tailwind v4 · ESLint 9 | Default Vite/AI-Studio boilerplate, no real content | ✅ mirror `omk-services/00-omk-landing-page` (dpl_ERCXgjM, READY) | ✅ **Vercel** (team `omk-services`, project `omk-landing-page`) |

The folder is `apps/dashboard/` on disk; the GitHub repo and Vercel project use the **`omk-dashboard`** alias (pivot Dokploy → Vercel per **ADR-OMK-004 RATIFIED 2026-06-19**). The landing app was revived during the pivot (Vercel mirror + deploy).

---

## 8-phase REBUILD contract — current state

Read `apps/dashboard/REBUILD_WORKFLOW.md` first — **it is the source of truth for WHAT to build**.

| Phase | Description | State (verified 2026-06-10) |
|-------|-------------|------------------------------|
| A | Foundations locales (config, supabase client, env) | 🟡 PARTIAL — `src/config/mode.ts` ✅, `src/lib/supabase.ts` ✅, `.env.example` ✅, `npm run lint` not verified |
| B | Schémas + seed Supabase | ❌ BLOCKED — requires `supabase-aspace` MCP v0.1 (ADR-SUPABASE-001 ACCEPTED 2026-06-08) |
| C | Auth + tenant (AuthProvider, useAuth, LoginView/SignupView) | ❌ NOT STARTED — `"Admin User"` still hardcoded in `App.tsx` |
| D | Repositories + branchement 7 views | ❌ NOT STARTED — `src/data/repository.ts` exists (Supabase+localStorage fallback) but views still import `lib/constants.ts` |
| E | Routing react-router-dom 7 | ❌ NOT STARTED — `useState(activeTab)` in `App.tsx` |
| F | Serveur + conteneur | 🟡 PARTIAL — `server.js` (Express, healthcheck `/healthz` + SPA fallback on `:3000`), `Dockerfile` (multi-stage `node:20-alpine`), `.dockerignore` |
| G | Déploiement Dokploy (2 services) | 🟡 UNBLOCKED (gates lifted) — ADR-OMK-001 RATIFIED 2026-06-11, démarre dès MCP prêt |
| H | Tests isolation + handoff (RLS adversarial + E2E) | ❌ NOT STARTED |

**The 4 ADR-level blockers** (état post-pivot 2026-06-19) :
1. `ADR-SUPABASE-001` (multi-tenant Supabase) — `✅ ACCEPTED 2026-06-08 in _SPECS/ADR/` → **fonctionnellement SUPERSEDED par ADR-OMK-004 §D1** (hosting self-host → Cloud). Note STATUS UPDATE à apposer en tête du fichier.
2. Rôles PG `aspace_admin` / `aspace_observer` on VPS — `✅ RATIFIED 2026-06-11 — ADR-OMK-002 + script 06_provision_pg_roles_omk.sql prêt (HITL VPS via SSH srv941028)` → **toujours valide** (couche rôles PG, orthogonale au hosting/deploy).
3. MCP `supabase-aspace` v0.1 — `🟡 ADR-OMK-003 en rédaction` → **scope à pivoter** post-ADR-OMK-004 : on a déjà `mcp__supabase-omk__*` (Cloud OMK Org) wired direct dans `.mcp.json`. Décision A0 HITL : radier ADR-OMK-003 ou le repurposer pour le MCP Cloud unifié.
4. `ADR-OMK-001` (dual-product deployment) — `✅ RATIFIED 2026-06-11 in _SPECS/ADR/` → **AMENDED 2026-06-19** par ADR-OMK-004 §Condition A : §runtime simplifié à single-mode SaaS (`VITE_APP_MODE=saas` only), `internal` mode retiré. §deploy (Dokploy Caddyfile) **fonctionnellement SUPERSEDED** par ADR-OMK-004 §D2 (Vercel).

Without these, Phases B, C, D, G are blocked. Phase H is gated on RLS working.

**3 conditions A0 HITL pending post-ratification** (ADR-OMK-004 §Verification) :
- **Condition B** : JWT custom_access_token_hook re-provisioning sur Supabase Cloud (Dashboard UI → Authentication → Hooks). Handoff `handoff_jwt_hook_cloud_migration_<date>.md` créé. ~10 min UI. **Bloquant silencieux pour Phase C SaaS** (RLS `org_id` claim = null → 0 rows).
- **Condition D** : Vercel Authentication OFF × 4 projects (omk-saas-os, omk-landing-page, abc-community-os, abc-landing-page). Manuel UI Settings → Security → Vercel Authentication → Off.
- **Condition E** : Rotation 2 PATs Cloud (`sbp_f2af0f71…` OMK + `sbp_4121633e…` ABC) — Test Key Pragma. New PATs via Dashboard Supabase → env vars User scope + `.mcp.json` update + revoke old.

---

## Common commands (dashboard)

All commands run from `apps/dashboard/`.

```bash
# Install
npm install

# Dev (Vite, port 3000 — NOT 5173 to avoid conflict with Next.js landing)
npm run dev          # → http://localhost:3000

# Lint / type-check (tsc --noEmit, no console --watch)
npm run lint

# Build production → dist/
npm run build

# Preview built bundle via Vite (dev preview only)
npm run preview

# Run prod bundle via Express (serves dist/ with /healthz + SPA fallback)
node server.js       # → http://localhost:3000

# Docker (multi-stage build → node:20-alpine)
docker build -t omk-dashboard .
docker run -p 3000:3000 omk-dashboard
curl http://localhost:3000/healthz   # → 200 OK

# Wipe build artifacts (also removes server.js — git restore it)
npm run clean
```

`.env.local` is gitignored — copy from `.env.example` and fill `VITE_APP_MODE`, `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY`, `GEMINI_API_KEY`.

---

## Big-picture architecture

The data flow is **views → repositories → Supabase (or localStorage)**, gated by a single `APP_MODE` resolved at build time.

```
┌────────────────────────────────────────────────────────────────────┐
│  Vite build  (port 3000, VITE_* env vars baked at build)          │
│                                                                    │
│  VITE_APP_MODE ──► src/config/mode.ts                              │
│                      ├── APP_MODE:  'internal' | 'saas'           │
│                      └── DB_SCHEMA: 'omk_internal' | 'omk_saas'    │
│                                                                    │
│  src/lib/supabase.ts  ◄── schema-aware Supabase client             │
│      │                                                             │
│      ▼                                                             │
│  src/data/repository.ts  (generic makeRepository<T>)               │
│      │                                                             │
│      ├── if SUPABASE_READY  → supabase.from(table) (RLS-scoped)    │
│      └── else               → localStorage seeded with mocks       │
│                                                                    │
│  src/components/views/*  ◄── 7 views (Dashboard, Clients,          │
│      │                            Documents, Agents, Finance,       │
│      │                            SOPLibrary, Settings)            │
│      │                                                             │
│      └── Currently import directly from lib/constants.ts           │
│          (Phase D = swap to data/ repos + loading/empty/error)     │
│                                                                    │
│  src/App.tsx  (shell + sidebar + useState<TabType>)                │
│      └── Phase E = <RouterProvider> + <NavLink> from react-router  │
└────────────────────────────────────────────────────────────────────┘
        │                                          │
        │ Express (server.js)                      │ Dokploy (Phase G)
        │   /healthz, SPA fallback                 │   2 services × 2 schemas
        ▼                                          ▼
   Production container                  omk-internal.aspace.fr
                                          omk-saas.aspace.fr
```

**Two key files** (read these to grok the dual-mode contract):
- `src/config/mode.ts` — exports `APP_MODE`, `DB_SCHEMA`, `IS_SAAS`, `IS_INTERNAL`. **Mode is baked at `vite build` time** (import.meta.env), not a runtime toggle.
- `src/lib/supabase.ts` — `createClient({ db: { schema: DB_SCHEMA } })`. Only `VITE_SUPABASE_ANON_KEY` is bundled; `SERVICE_ROLE_KEY` is server-side only.

**Auth boundary** : client-side `APP_MODE` is a UI hint. True isolation is enforced server-side by Supabase RLS using `org_id` from a custom JWT claim (Supabase `auth.hook` reads `memberships` table).

---

## Single-mode runtime contract (post-ADR-OMK-004, A1 LOCKED 2026-06-19)

**One codebase, one product, single SaaS mode.** Per **ADR-OMK-004 §Condition A = A1** (A0 directive 2026-06-19), le mode `internal` est retiré. Avant ce pivot, le runtime était dual-mode (`internal` + `saas`) avec 2 Dokploy services. Post-pivot : single Vercel project, single schema, single mode.

| Mode | Schema | Auth | User | RLS |
|------|--------|------|------|-----|
| `saas` (only) | `omk_saas` | Signup + login (creates org) | External PME clients | `org_id = (auth.jwt() ->> 'org_id')::uuid` |

**Mode baked = `'saas'` only.** Pas de switch, pas de 2 services. `VITE_APP_MODE=saas` est set dans Vercel project env vars au build. Voir `REBUILD_WORKFLOW.md` §3 Phase G (réécrit 2026-06-19) pour les détails Vercel.

> **Note historique** : avant 2026-06-19, OMK avait 2 modes (internal pour staff, saas pour clients PME) avec 2 Dokploy services sur 2 subdomains distincts. Dokploy tué pour cause de saturation VPS KVM 2 (D6 #9, ADR-OMK-004 §Context).

---

## Deploy (Vercel + Supabase Cloud, post-ADR-OMK-004)

**Pivot** : avant 2026-06-19, deploy Dokploy sur VPS `148.230.92.235` (2 services × 2 subdomains). Post-pivot : 1 Vercel project sur Supabase Cloud.

**Vercel project actif** (team `omk-services`, mirroré depuis `Amdkn/01-OMK-Business-OS` SHA `ef2cc36`) :

| Project | Deploy ID | URL preview | Status |
|---------|-----------|-------------|--------|
| `omk-saas-os` | `dpl_Fx8b821` | `omk-saas-9q6hbl8xz-omk-services.vercel.app` | ✅ READY (Auth ON, Condition D pending) |

**Env vars** (set in Vercel project settings, never in `.env` committed) :
- `VITE_APP_MODE=saas` (baked at build)
- `VITE_SUPABASE_URL` (Cloud, OMK Services Org — `SUPABASE_OMK_URL` env var)
- `VITE_SUPABASE_ANON_KEY` (PUBLIC, bundled in JS — `SUPABASE_OMK_ANON_KEY`)
- `GEMINI_API_KEY` (PUBLIC, bundled — rotate if exposed)
- `SUPABASE_SERVICE_ROLE_KEY` is **NEVER** client-side, never here.

**Vercel Authentication** : **OFF** requis (Condition D, Étape 4 runbook ADR-OMK-004). Sinon URLs preview retournent 401 même quand READY.

**Custom domain** (optionnel) : `omk.kalybana.com` → CNAME → `cname.vercel-dns.com` (DNS via Hostinger MCP).

---

## Critical gotchas (read before editing)

1. **`VITE_APP_MODE` is build-time, single value `'saas'`** (post-ADR-OMK-004 A1) — pas de switch runtime. Set dans Vercel project env vars. Pas de "rebuild to switch mode" : single product, single schema.
2. **`SERVICE_ROLE_KEY` is server-side only** — `VITE_*` env vars are bundled into JS and PUBLIC. The service role key must never appear in `apps/dashboard/.env` or be sent to the browser.
3. **Supabase Cloud OMK Services Org ≠ `supabase.com` (login) ≠ self-host VPS** — URL via `SUPABASE_OMK_URL` env var (Cloud project URL). Différent du legacy self-host `148.230.92.235.sslip.io` (archivé post-ADR-OMK-004). Différent auth, différent dashboard, différent PostgreSQL host.
4. **JWT custom access token hook is a single point of failure** — if misconfigured, every saas RLS query returns 0 rows silently. Hook reads `omk_saas.memberships` table and injects `org_id` into JWT; the RLS policy `org_id = (auth.jwt() ->> 'org_id')::uuid` is the multi-tenant security boundary. Add a `console.warn` if the claim is null in saas mode. **⚠️ Condition B (ADR-OMK-004) : hook doit être re-provisionné sur Supabase Cloud** (voir `handoff_jwt_hook_cloud_migration_<date>.md` post-pivot).
5. **Cloud auto-managed schemas** — unlike self-host (où `PGRST_DB_SCHEMAS` reload était HITL), Supabase Cloud auto-manage les schemas exposés. Pas de HITL restart requis post-migration.
6. **Vite dev server runs on port 3000** (not the default 5173) to avoid clash with the Next.js landing app if both run together.
7. **`server.js` is a prod server, not a dev one** — Docker container runs `node server.js`, NOT `vite preview`. The Express server serves `dist/` with SPA fallback; `/healthz` MUST be registered **before** the catch-all route.
8. **`src/lib/constants.ts` is hardcoded mock data** — to wire Phase D, rename to `seed.ts` and restrict use to the dev/seed flow. The 7 views should branch on repositories, not constants.
9. **`metadata.json` says "OMK Services"** with capability `MAJOR_CAPABILITY_SERVER_SIDE_GEMINI_API` — this is the AI-Studio stub, not a runtime constraint. `@google/genai` is installed but not yet wired in current code.
10. **TypeScript rules in `~/.claude/rules/ecc/typescript/` are auto-loaded** — follow them: no `any`, immutable updates, Zod for input validation, no `console.log` in production, Playwright for E2E.
11. **`.gitignore` lists `.vercel/`** (post-pivot 2026-06-19) — Vercel CLI artifacts (`.vercel/project.json` + `.vercel/README.txt`) sont gitignored. Si Vercel CLI recrée `.vercel/` au prochain `vercel link`, c'est normal.
12. **`@supabase/supabase-js` types** — `supabase.from(table).select('*')` returns `any`-ish without a generated `Database` type. Phase B step 4 (`generate_typescript_types`) creates `src/lib/database.types.ts` to fix this.

---

## Files to read FIRST when picking this up

In order:
1. `apps/dashboard/REBUILD_WORKFLOW.md` — the **contract** (pivot post-ADR-OMK-004, 8 phases, Vercel Phase G, SQL DDL).
2. `apps/dashboard/picard_audit.md` — superseded 2026-05-25 audit (41/100, 7 defects D01–D07). Périmé sur la modularisation (déjà faite in commit `4a1c6b3`), still useful for the original defect context.
3. `20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/CERRIROS_HANDOVER.md` — doctrine junction.
4. `apps/dashboard/src/config/mode.ts` + `apps/dashboard/src/lib/supabase.ts` + `apps/dashboard/src/data/repository.ts` — the data layer triple (post-A1: single mode `'saas'`, single schema `omk_saas`).
5. `apps/dashboard/src/App.tsx` — current shell, shows exactly what's stubbed (hardcoded "Admin User", `useState` routing).
6. `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_omk_dashboard_dev_2026-06-10.md` — full handoff with verification checklist per phase (mostly superseded par pivot 2026-06-19, mais utile pour le contexte originel).
7. **`_SPECS/ADR/ADR-OMK-004_pivot-supabase-cloud-vercel.md` RATIFIED 2026-06-19** — pivot canon, A1 LOCKED (single SaaS mode), supersedes ADR-OMK-001 deploy + ADR-SUPABASE-001 hosting.
8. `_SPECS/ADR/ADR-OMK-001_dual-product.md` (AMENDED) + `_SPECS/ADR/ADR-SUPABASE-001_multi-tenant.md` (superseded fonctionnellement).

---

## Recommended order of work

1. **4 ADR blockers ratifiés 2026-06-11** (3/4 done, MCP reste en rédaction). Phases B/C/D/G gates lifted sauf dépendance MCP.
2. **Split `lib/constants.ts` → `seed.ts`** + add `Organization`/`Membership` to `lib/types.ts`. Type work unblocks Phase D.
3. **Phase A cleanup** — verify `npm run lint` is GREEN, then move to Phase B.
4. **Phase B** — Supabase schemas + RLS + types. HITL step: reload `PGRST_DB_SCHEMAS` on VPS.
5. **Phase C** — AuthProvider + useAuth + LoginView/SignupView + JWT hook. Replaces `"Admin User"`.
6. **Phase D** — 5 repositories (clients/documents/agents/invoices/sops) + branch 7 views + loading/empty/error states.
7. **Phase E** — `react-router-dom 7`, `<RouterProvider>`, sidebar → `<NavLink>`, kill `useState(activeTab)`.
8. **Phase F** — verify `docker build` + `docker run` end-to-end with `curl /healthz`.
9. **Phase G** — deploy Vercel project `omk-saas-os` (team `omk-services`), env vars + Vercel Auth OFF (Condition D), optional custom domain `omk.kalybana.com` via Hostinger DNS, smoke test.
10. **Phase H** — adversarial RLS test (org A user cannot read org B), Playwright E2E for 7 views + auth flow, final README, commit, push, MAJ wiki log.

---

## Verification per phase (proof on file, D5)

| Phase | Verification |
|-------|--------------|
| A | `npm run lint` GREEN, `npm run dev` shows dashboard at :3000 |
| B | `psql` shows both schemas, `generate_typescript_types` produces non-empty `src/lib/database.types.ts` |
| C | `useAuth().session` non-null after login, `useAuth().orgId` matches `memberships.org_id` |
| D | 7 views load from Supabase (not constants), create/update/delete round-trips persist |
| E | Browser URL changes on sidebar nav, refresh on `/clients` shows clients view |
| F | `docker run` → `curl /healthz` returns 200, SPA loads at `/` |
| G | Login on `omk.kalybana.com` (or Vercel preview URL) works, Vercel Auth OFF, RLS isolation test passes (org A user cannot read org B) |
| H | **Adversarial RLS test**: user A's session cannot read org B's clients (via DevTools or psql) |

---

## Write-back protocol

When meaningful work is done, append a one-liner to:
1. `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` (under today's date)
2. `00_Amadeus/30_MEMORY_CORE/README.md` (today's bullet)
3. `apps/dashboard/REBUILD_WORKFLOW.md` §0 "État vérifié" — update as phases complete
4. (When created) `apps/dashboard/AGENTS.md` — encode the contract from this handoff + 4 blockers

---

## Secret handling

- `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY`, `GEMINI_API_KEY` — PUBLIC (bundled). Safe as placeholders in `.env.example`, real values in **Vercel project env vars** only (not Dokploy — pivot post-ADR-OMK-004).
- `SUPABASE_SERVICE_ROLE_KEY` — **NEVER** client-side. Use env User Windows (durable) for long-term; commit `.env` to gitignore (already is).
- **Vercel API tokens** + **Hostinger API token** + **Supabase Cloud PATs** (`SUPABASE_OMK_ACCESS_TOKEN`, `SUPABASE_ABC_ACCESS_TOKEN`) — exposed in `.mcp.json` (Test Key Pragma). Rotation recommandée post-pivot (Condition E, Étape 6 runbook ADR-OMK-004). Do NOT echo values in chat/code/logs.

---

## Local / external rules already loaded

- `ASpace_OS_V2/CLAUDE.md` — sovereign OS doctrine (this file inherits/overrides nothing; you MUST respect it).
- `~/.claude/rules/ecc/typescript/` — coding style, hooks, patterns, security, testing (auto-loaded).
- `~/.claude/rules/ecc/web/` — design quality, patterns, performance, security (auto-loaded for frontend work).
- No Cursor rules (`.cursor/`, `.cursorrules`) or Copilot rules (`.github/copilot-instructions.md`) exist in this project.

---

## Residual risks (load-bearing)

- **4 ADR blockers** — the rebuild is fully blocked until ratified. Highest-leverage decision. **MAJ 2026-06-19** : 1 ADR pivoté (ADR-OMK-004 RATIFIED), 1 ADR amended (OMK-001), 1 ADR superseded fonctionnellement (SUPABASE-001), 2 ADRs toujours valides (OMK-002 rôles PG, OMK-003 MCP en rédaction avec scope à pivoter).
- **Supabase Cloud coupling** (post-pivot) — entire app depends on Supabase Cloud (OMK Services Org) being up. localStorage fallback exists for dev but is not wired into views yet. **Vercel + Cloud = ops surface plus simple que Dokploy + VPS self-host**.
- **No tests** — Phase H is the test phase. Consider adding unit tests for repos (mock Supabase client) and Playwright E2E for 7 views + auth flow before Phase G.
- **JWT custom hook re-provisioning Cloud** (Condition B) — see gotcha #4. Le hook self-host reste actif mais ne sert plus l'app prod. **A0 HITL** : re-provisionner sur Cloud via Dashboard UI.
- **Vercel Authentication default ON** (Condition D) — voir Deploy section. Manuel UI Settings → Security → Vercel Authentication → Off par projet.
- **`@google/genai` is installed but unused in current code** — verify the API key is real before building AI features on top.

---

**Next safe action for a fresh session** : read this file, then `apps/dashboard/REBUILD_WORKFLOW.md`, then open the ADR-ratification session with A0.
