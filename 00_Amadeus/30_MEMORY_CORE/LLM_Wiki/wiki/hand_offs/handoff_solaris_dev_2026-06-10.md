---
source: A2 Claude Code (this session) handoff after graphify/ABC OS/OMK delegation
date: 2026-06-10
type: handoff
status: ACTIVE — waiting for receiving session to pick up dev on solaris
domain: L2_Business_OS / 30_Business_OS / 10_Projects / solaris / apps /
tags: [#solaris, #solaris_os, #aaas, #digital_garden, #nextjs, #supabase, #dokploy, #soa01-08, #symphony_router, #zod, #8_domains, #handoff, #delegation, #dual_product, #doctrine_wired, #deploy_ready_blockers]
related: [LLM_Wiki/wiki/L0/entity_solaris_os.md (8 SOA domains canon), LLM_Wiki/wiki/L0/entity_symphony_router.md, LLM_Wiki/wiki/L0/entity_zod.md, LLM_Wiki/wiki/L0/entity_master_soc.md, _SPECS/ADR/ADR-SUPABASE-001, _SPECS/ADR/ADR-OMK-001, _SPECS/ADR/ADR-INFRA-002_repo-home-junction.md, 20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/00 Agency as a Service/ (Picard doctrine — symlink target), 30_Business_OS/10_Projects/solaris/apps/dashboard/REBUILD_WORKFLOW.md (THE contract, dated 2026-06-08), 30_Business_OS/10_Projects/solaris/apps/dashboard/picard_audit.md (Picard audit 2026-05-25)]
context_release: this session is being freed for project development; graphify/ABC OS/OMK/Solaris handoffs written (4 handoffs same session)
github: https://github.com/Amdkn/00-AaaS-Agency-Garden (per REBUILD_WORKFLOW line 6) OR https://github.com/Amdkn/00-Solaris (per wiki log "Livraison Solaris AaaS" 2026-05) — may have been renamed, verify with A0
deploy_target: Dokploy (per next.config.ts `output: 'standalone'` + Dockerfile + REBUILD_WORKFLOW) — Vercel NOT used
---

# Handoff — Solaris (AaaS Digital Garden) Dashboard (2026-06-10)

## Why this handoff exists

A0 wants to free this Claude Code session for project development (heho). The
**Solaris** project is the 4th handoff of this session. This handoff is the
**executable playbook** for finishing the Solaris dashboard to deployment-ready.

## Critical context (CORRECTED from initial draft)

The first pass of this handoff framed Solaris as **greenfield**. **This was
wrong** — Verify-Before-Assert failure. The actual state (verified by
filesystem inspection 2026-06-10) is:

- **The dashboard is ~85% built.** 12 views, full auth flow, repository pattern,
  Supabase clients, middleware, SQL migrations, Dockerfile, `next.config.ts`,
  `REBUILD_WORKFLOW.md`, `picard_audit.md` all exist.
- **The doctrine junction IS wired.** `_doctrine` symlink points to
  `00 Agency as a Service` Picard slot (B1/B2/B3 folders).
- **The 8 SOA domains have full doctrine in B2_Business_Domains** with one folder
  per domain (`01_Growth_Superman_Guardians`, ..., `08_Legal_Aquaman_Eternals`).
- **The deploy target is Dokploy** (matches OMK + Sovereign OS doctrine), not
  Vercel — confirmed by `next.config.ts: output: 'standalone'` + Dockerfile.
- **Backend Supabase IS wired** at the client level (`@supabase/ssr` +
  `lib/supabase/{client,index,server}.ts` + middleware + 6 SQL migrations),
  but **per `REBUILD_WORKFLOW.md` §0 (2026-06-08) the data layer is still
  100% mock in `constants.ts`** — the migrations exist but views are not yet
  consuming them. **Verify with A0 which is current.**

The receiving session should treat the 8-domain doctrine as the source of
truth for what the dashboard should surface, and use this handoff as the
gap-analysis between "what exists" and "what deploy-ready needs".

## Project overview — what is Solaris (AaaS Digital Garden)

**Solaris (AaaS = "Agency-as-a-Service")** is the **business operating
system** for the 8 SOA01-SOA08 domains of L2 Business Pulse, packaged as a
productized SaaS for non-technical founders / agencies (per
`LLM_Wiki/wiki/L0/entity_solaris_os.md`, 552 mentions, canonical since
2026-05-10; per `metadata.json`: "A streamlined Agency-as-a-Service
operating system for non-technical founders"). Branding: **"The Founder's
Digital Garden"** (per `apps/dashboard/src/app/layout.tsx`).

It is **architectural**, not a kernel — it orchestrates the A3 Nano Squads
under each domain. The 8 domains are:

| Domain (entity order) | Domain (Picard order) | Hero | Squad | B2 Folder |
|----------------------|----------------------|------|-------|-----------|
| **SOA01 People** | 07 | Green Lantern | X-Men | `07_People_GreenLantern_XMen` |
| **SOA02 IT** | 05 | Cyborg | Kang Dynasty | `05_IT_Cyborg_KangDynasty` |
| **SOA03 Ops** | 04 | Batman | Fantastic Four | `04_Ops_Batman_Fantastic4` |
| **SOA04 Product** | 03 | Flash | Avengers | `03_Product_Flash_Avengers` |
| **SOA05 Growth** | 01 | Superman | Guardians | `01_Growth_Superman_Guardians` |
| **SOA06 Finance** | 06 | Wonder Woman | Thunderbolts | `06_Finance_WonderWoman_Thunderbolts` |
| **SOA07 Legal** | 08 | Aquaman | Eternals | `08_Legal_Aquaman_Eternals` |
| **SOA08 Sales** | 02 | John Jones | Illuminati | `02_Sales_MartianManhunter_Illuminati` |

> **Numbering drift**: `entity_solaris_os.md` uses SOA01-SOA08 (canonical).
> Picard `B2_Business_Domains` uses 01-08 in a different order (probably
> business priority / build order). Both refer to the same 8 domains. **The
> receiving session should reconcile to SOA numbering** in any new code
> (types, route prefixes, repo names) for consistency with the rest of L2.

**Core architecture** (per entity + Picard `00_AAAS_DOMAIN_DEVELOPMENT_MAP.md`):
- **Master SOC Schema** — hierarchical unified schema (Master → 8 Domain SOCs → sub-schemas)
- **Zod Contracts** — runtime validation for inter-domain communication (canon, not yet wired)
- **Symphony Router** — orchestrator routing intents between domains without direct coupling (canon, not yet wired)

**Dual-mode runtime** (per `src/config/mode.ts`, mirrors OMK's pattern):
- `solaris_internal` — AaaS agency staff operating its own business OS (single-tenant, default mode)
- `solaris_saas` — productized multi-tenant SaaS sold to SMB clients (org_id + RLS, premium mode)
- `NEXT_PUBLIC_APP_MODE` env var controls; client-side flag is UI hint only — true isolation is Postgres RLS + JWT claims

The monorepo at `30_Business_OS/10_Projects/solaris/` is the 2-app web surface:

| App | `name` in package.json | Role | Stack |
|-----|----|------|-------|
| `apps/dashboard` | **`aaas-os`** | operator/staff dashboard (8 domains, the Solaris UI) | Next.js 16.2.6 + React 19.2.4 + @supabase/ssr + @supabase/supabase-js + Tailwind 4 + motion + lucide-react + Next App Router + `output: 'standalone'` |
| `apps/landing` | **`solaris-aaas`** | public marketing site for AaaS + `/api/leads` capture | Next.js 16.2.6 + React 19.2.4 + Tailwind 4 (no Supabase, no motion, no lucide) |

**Doctrine junction** (per ADR-INFRA-002, Repo-Home/Junction):
- `_doctrine` symlink at `30_Business_OS/10_Projects/solaris/_doctrine` →
  `20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/00 Agency as a Service/`
- Picard folder has B1_Summer_Direction (11 doc files including
  `00_B1_DIRECTION_INDEX.md`, `01_NORTH_STAR_1Y_3Y_10Y.md`, `SUMMERS_VERSE_MANIFEST.md`),
  B2_Business_Domains (8 domain folders + harmonization matrix), B3_Warp_Core_Execution,
  `CERRIROS_HANDOVER.md`, `_Inbox`
- ⚠️ **Picard slot 03 is already taken by `03_RILCOT_Members_Space_OS`** (and there's a `03_Product_Flash_Avengers - Shortcut.lnk`). The "00 Agency as a Service" slot is a B0 (agency-level) slot, not a numbered business slot. This is a doctrinal choice — verify with A0 whether AaaS should be promoted to a numbered slot (e.g., 06) and `00` reserved for the platform itself.

**Backend Supabase state** (per `supabase/migrations/` 6 files + wiki log 2026-06-08):
- `PGRST_DB_SCHEMAS += solaris_internal, solaris_saas` ✅
- Grants applied, anon revoked from `solaris_internal` ✅
- 6 SQL migrations present locally:
  - `0001_init_schemas.sql` — create schemas
  - `0002_solaris_saas_tables.sql` — saas tables (organizations, etc.)
  - `0003_solaris_saas_rls.sql` — saas RLS policies
  - `0004_solaris_internal_tables.sql` — internal tables
  - `0005_solaris_internal_rls.sql` — internal RLS
  - `0006_custom_access_token_hook.sql` — JWT custom access token hook (per ADR-SUPABASE-001)
- Verified: `solaris_saas` returns 200 (RLS []), `solaris_internal` returns 401 (anon denied)
- **GAP**: the dashboard `src/lib/constants.ts` is still 100% mock per
  `REBUILD_WORKFLOW.md §0`. The 12 views render from constants, not from
  the Supabase repos. The data layer wiring is the next big task.

## State of `solaris` as of 2026-06-10 (verified by source session)

### What's built ✅ (substantially more than initially thought)

```
solaris/
├── _doctrine → 20_Life_OS/.../00 Agency as a Service/  ✅ ALREADY WIRED
├── apps/
│   ├── dashboard/                              # aaas-os — operator side
│   │   ├── AGENTS.md                            # ⚠️ stub — only nextjs-agent-rules warning
│   │   ├── CLAUDE.md                            # @AGENTS.md (imports the stub)
│   │   ├── README.md                            # ❌ default create-next-app boilerplate
│   │   ├── REBUILD_WORKFLOW.md                  # ✅ OMK-style contract (2026-06-08, may be slightly stale)
│   │   ├── picard_audit.md                      # ✅ May 2026 audit (pre-Supabase wiring)
│   │   ├── Dockerfile                           # ✅ Node 20-alpine, multi-stage, production-ready
│   │   ├── docker-compose*.yml                  # verify
│   │   ├── package.json                         # ✅ has Supabase, Tailwind 4, motion, lucide
│   │   ├── .gitignore                           # ✅ default (with .vercel ignored, NEXT_PUBLIC_* in .env*)
│   │   ├── eslint.config.mjs                    # ✅ default
│   │   ├── postcss.config.mjs                   # ✅ default (Tailwind 4)
│   │   ├── next.config.ts                       # ✅ output: 'standalone' (Dokploy)
│   │   ├── tsconfig.json                        # ✅ exists (verify strict)
│   │   ├── metadata.json                        # ✅ A'Space AaaS metadata
│   │   ├── public/                              # 5 default SVGs
│   │   ├── supabase/
│   │   │   └── migrations/                      # ✅ 6 SQL files (0001-0006)
│   │   └── src/
│   │       ├── app/                             # ✅ App Router, fully scaffolded
│   │       │   ├── layout.tsx                   # ✅ AuthProvider wired, Geist font
│   │       │   ├── page.tsx                     # ✅ 189 lines, 12-view switcher
│   │       │   ├── globals.css
│   │       │   ├── favicon.ico
│   │       │   └── auth/
│   │       │       ├── actions.ts               # ✅
│   │       │       ├── callback/route.ts        # ✅
│   │       │       ├── check-email/page.tsx     # ✅
│   │       │       ├── signin/page.tsx          # ✅
│   │       │       ├── signout/route.ts         # ✅
│   │       │       └── signup/page.tsx          # ✅
│   │       ├── components/
│   │       │   ├── Sidebar.tsx                  # ✅
│   │       │   ├── AiPanel.tsx                  # ✅ (Board of Directors metaphor)
│   │       │   ├── Toast.tsx                    # ✅
│   │       │   ├── Modal.tsx                    # ✅
│   │       │   ├── auth/
│   │       │   │   ├── AuthProvider.tsx         # ✅ mirrors Supabase auth into React
│   │       │   │   ├── useAuth.ts               # ✅
│   │       │   │   └── useSessionContext.ts     # ✅
│   │       │   ├── empty-states/                # ✅ 12 files (one per view)
│   │       │   ├── skeletons/                   # ✅ 12 files (one per view)
│   │       │   └── views/                       # ✅ 12 files
│   │       │       ├── Dashboard.tsx
│   │       │       ├── Finance.tsx
│   │       │       ├── Clients.tsx
│   │       │       ├── People.tsx
│   │       │       ├── Legal.tsx
│   │       │       ├── SopLibrary.tsx
│   │       │       ├── Tasks.tsx
│   │       │       ├── Growth.tsx
│   │       │       ├── Sales.tsx
│   │       │       ├── Marketplace.tsx
│   │       │       ├── ItData.tsx
│   │       │       └── Settings.tsx
│   │       ├── config/
│   │       │   └── mode.ts                      # ✅ APP_MODE, DB_SCHEMA, IS_SAAS, IS_INTERNAL
│   │       ├── lib/
│   │       │   ├── types.ts                     # ✅ types métier
│   │       │   ├── constants.ts                 # ⚠️ 100% mock (per REBUILD_WORKFLOW)
│   │       │   └── supabase/
│   │       │       ├── client.ts                # ✅ createBrowserClient
│   │       │       ├── server.ts                # ✅ createSupabaseServerClient (schema-aware)
│   │       │       └── index.ts                 # ✅ barrel
│   │       ├── types/
│   │       │   └── supabase.ts                  # ✅ Organization, Membership, SessionContext
│   │       ├── repos/                           # ✅ 22 files (11 views × .client.ts + .server.ts)
│   │       │   ├── clients.{client,server}.ts
│   │       │   ├── dashboard.{client,server}.ts
│   │       │   ├── finance.{client,server}.ts
│   │       │   ├── growth.{client,server}.ts
│   │       │   ├── itdata.{client,server}.ts
│   │       │   ├── legal.{client,server}.ts
│   │       │   ├── marketplace.{client,server}.ts
│   │       │   ├── people.{client,server}.ts
│   │       │   ├── sales.{client,server}.ts
│   │       │   ├── settings.{client,server}.ts
│   │       │   ├── sop.{client,server}.ts
│   │       │   ├── tasks.{client,server}.ts
│   │       │   └── index.ts
│   │       └── middleware.ts                    # ✅ 3-phase OMK pattern (refresh, gate, inject)
│   └── landing/                                 # solaris-aaas — public side
│       ├── AGENTS.md                            # verify contents
│       ├── CLAUDE.md                            # verify
│       ├── README.md                            # ❌ default create-next-app boilerplate
│       ├── LEADS_SETUP.md                       # exists (verify)
│       ├── picard_audit_solaris.md              # ✅ landing-specific audit
│       ├── package.json                         # ✅ minimal (no Supabase, no Tailwind, no extras)
│       ├── next.config.ts                       # verify
│       ├── tsconfig.json                        # verify
│       ├── eslint.config.mjs
│       ├── postcss.config.mjs
│       ├── agent-os/standards/                  # ✅ likely internal standards docs
│       ├── public/                              # 5 default SVGs
│       └── src/app/
│           ├── layout.tsx
│           ├── page.tsx
│           ├── page.module.css
│           ├── favicon.ico
│           ├── globals.css
│           └── api/leads/                       # ✅ lead capture API for marketing
```

### Open tickets / known issues 🐛 (corrected list — D5 verify)

> Tickets #1-#6 in the initial draft are **STALE** (the underlying issues are
> either already resolved or significantly different from the initial claims).
> The list below is the corrected gap-analysis.

#### #1 — HIGH: No git repo in the monorepo (still true)

`git status` returns "fatal: not a git repository" at
`30_Business_OS/10_Projects/solaris/`. The repo is at
`https://github.com/Amdkn/00-AaaS-Agency-Garden` (per REBUILD_WORKFLOW) or
`https://github.com/Amdkn/00-Solaris` (per wiki log 2026-05) — possibly
renamed.

**Action**:
- **Verify with A0** which GitHub URL is canonical (the REBUILD_WORKFLOW is
  dated 2026-06-08, the wiki log entry is older 2026-05, so the AaaS-Agency-Garden
  name is likely newer/canonical).
- `git clone <canonical-url>`, then copy the local `apps/` over the clone
  (preserves any local divergence, e.g., the supabase/ folder may not be on
  GitHub yet).
- Add a root `.gitignore` for the monorepo (node_modules × 2, .next × 2,
  .vercel, dist, *.log).

#### #2 — HIGH: No `AGENTS.md` content beyond the nextjs-agent-rules stub

`apps/dashboard/AGENTS.md` is 5 lines: only the `<!-- BEGIN:nextjs-agent-rules -->`
warning block. No project-specific guidance.

**Action**: rewrite `apps/dashboard/AGENTS.md` to include:
- 8 SOA domain mapping (SOA order, not Picard numeric order) with hero/squad per domain
- Dual-mode runtime contract (`solaris_internal` vs `solaris_saas`, with `NEXT_PUBLIC_APP_MODE`)
- Supabase state (6 migrations applied, anon revoked from `solaris_internal`)
- The 12 view → 8 domain mapping (some views are cross-cutting: Settings, Tasks, SOP Library, Marketplace, IT Data, Clients)
- The repo pattern (`.client.ts` for browser, `.server.ts` for server components)
- The `src/lib/constants.ts` mock → real data migration path
- The Zod contracts location (per domain, canon in `entity_zod.md`)
- The Symphony Router integration point (per `entity_symphony_router.md`)
- The deploy target (Dokploy, NOT Vercel)
- The Vercel reserved `/build` gotcha (not yet hit, but future-proof)
- The 8 open tickets in this handoff

Same for `apps/landing/AGENTS.md` (verify content, likely also bare).

#### #3 — HIGH: `lib/constants.ts` is still 100% mock (the OMK-style Phase D)

Per `REBUILD_WORKFLOW.md §0`: "Backend / persistance ❌ 100% mock
(constants.ts), aucun `@supabase/supabase-js`". **But the package is in deps
and `lib/supabase/` + `repos/` exist** — so the wiring is there, just not
the consumption.

**Action**: the bulk of the dev work is to:
- Map each view to its corresponding Supabase repos
- Replace `import { MOCK_DATA } from '@/lib/constants'` with `import { getX } from '@/repos/x.server'`
- Validate responses with Zod contracts (locate or create per `entity_zod.md`)
- Surface `SUPABASE_READY` flag (already exported from `lib/supabase/server.ts`)
- Update views from "mock data is fine" to "show skeletons while loading,
  empty states on no data, errors on failure" (the skeleton + empty-state
  components already exist per view)

#### #4 — HIGH: No `.env.example` at the dashboard root

The dashboard reads `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`,
`NEXT_PUBLIC_APP_MODE` (and the server reads from cookies), but no template
documents the expected env vars.

**Action**: create `apps/dashboard/.env.example` with:
```
# Public (bundled in JS)
NEXT_PUBLIC_SUPABASE_URL=https://YOUR_PROJECT.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=YOUR_ANON_KEY
NEXT_PUBLIC_APP_MODE=internal  # or 'saas'

# Server-only (NEVER NEXT_PUBLIC_*)
SUPABASE_SERVICE_ROLE_KEY=YOUR_SERVICE_ROLE_KEY  # for admin tasks, RLS bypass
```

Also `apps/landing/.env.example` (just `NEXT_PUBLIC_*` if any, plus
`LEADS_*` per `LEADS_SETUP.md`).

#### #5 — MEDIUM: Default create-next-app README on dashboard + landing

Both READMEs are unmodified boilerplate. Need to be rewritten to:
- Describe the project (AaaS Digital Garden, 8 SOA domains)
- Link to `entity_solaris_os.md` (the 8-domain canon)
- Link to `REBUILD_WORKFLOW.md` (the contract) and `picard_audit.md` (the audit)
- Document dev/build/deploy commands (Dokploy)
- Document the env vars
- Reference the doctrine junction (`_doctrine` → Picard "00 Agency as a Service")
- Reference the GitHub repo (whichever URL is canonical)
- Reference the 8 SOA domain mapping
- Reference the landing app (LEADS_SETUP.md)

#### #6 — MEDIUM: `REBUILD_WORKFLOW.md` is slightly stale

The workflow doc is from 2026-06-08 and says "Backend / persistance ❌ 100%
mock" — but the supabase/ folder, lib/supabase/, repos/, and migrations all
exist now. The workflow was written BEFORE the data layer wiring was
complete (it lists the supabase/ folder as a target, not a current state).

**Action**: refresh `REBUILD_WORKFLOW.md` to:
- Update §0 "État vérifié" to reflect current state (migrations ✅, repos ✅, mock data ⏳)
- Mark Phase A-F as done, Phase G (data layer consumption) as in progress
- Add Phase H (deploy via Dokploy) as next
- Reference the actual SQL migration filenames (`0001_init_schemas.sql` etc.)

#### #7 — MEDIUM: `picard_audit.md` is from May (pre-Supabase)

The audit is dated 2026-05-25, before the Supabase integration. It will not
flag the data layer as a debt, but the rest of the audit should still be
relevant (architecture, modularization, naming, etc.).

**Action**: refresh `picard_audit.md` to add a 2026-06-10 addendum:
- "Phase A-F complete (Supabase multi-tenant, 6 migrations, middleware, repos)"
- "Phase G in progress (constants.ts → repos)"
- New tickets: deploy (Dokploy not wired), env example, README, AGENTS.md
- Original audit's grading (e.g., 8.5/10 design) should be preserved

#### #8 — MEDIUM: No Zod contracts wired in the dashboard (canon exists, not consumed)

Per the Solaris OS canon (`entity_zod.md`), every domain has a Zod contract
for runtime validation. The dashboard should consume these on client (form
validation, API response validation) and server (request body validation in
`api/leads/` and the auth actions).

**Action**: locate the Zod contracts (in `02_Areas_Spock/J0x_*` or in a
shared `zod/` folder — verify with A0). Wire them into the dashboard's data
layer for runtime validation per the ECC web/patterns.md guidance.

#### #9 — MEDIUM: No Symphony Router integration

Per the Solaris OS canon (`entity_symphony_router.md`), the Symphony Router
orchestrates inter-domain intents. The dashboard should be able to dispatch
intents (e.g., "create a Growth experiment from a Sales lead") and receive
routed responses.

**Action**: locate the Symphony Router MCP or library (per the
`entity_symphony_router.md` + `entity_adr_symph_{001,002,003}.md` series).
Wire the dashboard as a Symphony client. The AiPanel ("Board of Directors")
component is the natural UI surface for routed intents.

#### #10 — MEDIUM: No tests, no CI, no lint workflow

No test framework, no Playwright config, no GitHub Actions, no pre-commit
hooks. The receiving session should consider adding at minimum:
- ESLint 9 (already in deps) + a strict config
- Playwright E2E (per ECC web/testing.md)
- A `tsc --noEmit` check (TypeScript already in devDeps)
- Visual regression at 320, 768, 1024, 1440 (per ECC web/testing.md)

#### #11 — MEDIUM: Dokploy deploy not yet wired

The `Dockerfile` + `next.config.ts: output: 'standalone'` are Dokploy-ready,
but no Dokploy project has been created and no Dokploy API call has wired
the GitHub → build → deploy pipeline.

**Action**: per OMK's deploy pattern + `01_hostinger/AGENTS.md` (or Dokploy
equivalent), wire:
- Dokploy project for `aaas-os` (dashboard)
- Dokploy project for `solaris-aaas` (landing)
- Set `NEXT_PUBLIC_APP_MODE=internal` and `=saas` as separate env configs
- Custom domain (e.g., `app.aspace.fr` for dashboard, `aaas.aspace.fr` for
  landing) via Hostinger DNS

#### #12 — MEDIUM: GitHub repo URL ambiguity

Two URLs surface in the canon:
- `https://github.com/Amdkn/00-AaaS-Agency-Garden` (per `REBUILD_WORKFLOW.md` 2026-06-08)
- `https://github.com/Amdkn/00-Solaris` (per wiki log "Livraison Solaris AaaS" 2026-05)

May be the same repo, renamed; or two separate repos; or one is wrong.
**Verify with A0** before any `git remote add` or push.

## Files to read FIRST (the contract)

In this order:

1. **`LLM_Wiki/wiki/L0/entity_solaris_os.md`** — THE Solaris OS canon (8 SOA
   domains, Master SOC, Zod, Symphony)
2. **`LLM_Wiki/wiki/L0/entity_zod.md`** — Zod contracts canon
3. **`LLM_Wiki/wiki/L0/entity_symphony_router.md`** — Symphony Router canon
4. **`30_Business_OS/10_Projects/solaris/apps/dashboard/REBUILD_WORKFLOW.md`** —
   THE Solaris rebuild contract (the analogue of OMK's REBUILD_WORKFLOW)
5. **`30_Business_OS/10_Projects/solaris/apps/dashboard/picard_audit.md`** —
   the May 2026 design/architecture audit
6. **`30_Business_OS/10_Projects/solaris/apps/dashboard/src/config/mode.ts`** —
   the dual-mode runtime (read this to understand `NEXT_PUBLIC_APP_MODE`)
7. **`30_Business_OS/10_Projects/solaris/apps/dashboard/src/middleware.ts`** —
   the 3-phase OMK pattern (refresh, gate, inject) — template for
   understanding the auth flow
8. **`30_Business_OS/10_Projects/solaris/apps/dashboard/src/app/page.tsx`** —
   the 189-line view switcher with Sidebar + AiPanel
9. **`20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/00 Agency as a Service/B2_Business_Domains/00_AAAS_DOMAIN_DEVELOPMENT_MAP.md`**
   — the 8-domain mapping in Picard
10. **`30_Business_OS/10_Projects/omk/apps/dashboard/REBUILD_WORKFLOW.md`** —
    the OMK contract (use as comparison to see how Solaris is similar/different)
11. **`_SPECS/ADR/ADR-SUPABASE-001`** + **`_SPECS/ADR/ADR-OMK-001`** — the
    two ADRs that govern the data layer (multi-tenant Supabase, dual-product)
12. **`_SPECS/ADR/ADR-INFRA-002_repo-home-junction.md`** — the doctrine
    junction (already wired for Solaris)

## Quick start commands

```powershell
# 1. Verify doctrine junction
ls "C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\solaris\_doctrine"
# Should show: B1_Summer_Direction/  B2_Business_Domains/  B3_Warp_Core_Execution/  ...

# 2. Reconnect git (verify URL with A0 first)
cd "C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\solaris"
git init
git remote add origin https://github.com/Amdkn/00-AaaS-Agency-Garden  # VERIFY URL
git pull origin master  # if GitHub has the canonical state
# OR keep local as canonical and `git add .` + `git commit` + `git push -u origin master`

# 3. Install dashboard deps
cd apps/dashboard
npm install

# 4. Copy env example (after creating it, see ticket #4)
cp .env.example .env.local
# Edit .env.local with Supabase URL + anon key from dashboard project

# 5. Run dev
npm run dev
# → http://localhost:3000 (no /dashboard route — the page.tsx is the SPA root,
#   with internal state for view switching; auth flow at /auth/signin etc.)

# 6. Build production (Dokploy-ready)
npm run build
# → .next/standalone/ (used by Dockerfile)

# 7. Lint
npm run lint

# 8. Install landing deps (separate)
cd ../landing
npm install
npm run dev
# → http://localhost:3001 (set PORT=3001) or another port
```

## Deploy workflow (Dokploy — NOT Vercel)

**Target**: Dokploy (per `next.config.ts: output: 'standalone'` + Dockerfile
+ the Sovereign OS doctrine that pushes against Vercel). This is the same
target as OMK.

**Per-app pipeline** (one Dokploy project per app, per `NEXT_PUBLIC_APP_MODE`):

1. **Reconnect git** (ticket #1) — Dokploy needs a git repo to pull from.
2. **Create Dokploy project** for `aaas-os` (dashboard) — link to GitHub repo,
   set root directory to `30_Business_OS/10_Projects/solaris/apps/dashboard`.
3. **Create Dokploy project** for `solaris-aaas` (landing) — link to GitHub,
   root `apps/landing`.
4. **Configure env vars per Dokploy project**:
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - `NEXT_PUBLIC_APP_MODE=internal` (or `=saas` for the saas instance)
   - `SUPABASE_SERVICE_ROLE_KEY` (server-only, for admin tasks)
5. **Custom domain** (per `01_hostinger/AGENTS.md` for DNS):
   - `app.aspace.fr` → aaas-os internal instance
   - `aaas.aspace.fr` → aaas-os saas instance (or separate brand)
   - `solaris.aspace.fr` → landing
6. **Wire GitHub push → Dokploy rebuild** (webhook or Dokploy's auto-deploy
   on push to master).

> **Anti-pattern warning**: do NOT use Vercel for Solaris. The OMK doctrine
> (per Sovereign OS) explicitly avoids Vercel for the same reason. Even
> though `apps/dashboard/.vercel` is gitignored, that's just create-next-app
> defaults — it does NOT mean Vercel is the deploy target.

## Gotchas (read these before editing)

1. **The dashboard is SPA-style with `useState`-based view switching** —
   `app/page.tsx` uses `NavView` enum + `useState<NavView>` to switch views
   client-side. It does NOT use Next.js App Router for the 12 view pages
   (no `/dashboard`, `/finance` routes). This means:
   - **Vercel reserved `/build` gotcha is moot** (no route file at `/build`)
   - But if a future ticket adds real per-view routes, **name them
     `/build-hub` or similar to avoid the reserved path** (per ABC OS ticket)
   - And **add the 12 routes to `middleware.ts:PROTECTED_ROUTES`** if you do
     add them (the middleware already has 12 protected routes hardcoded
     in `/dashboard`, `/finance` etc. — but the page.tsx doesn't use them)
2. **Picard slot "00 Agency as a Service" is a B0 (agency-level) slot**,
   not a numbered business slot. **Verify with A0** whether AaaS should
   be promoted to a numbered slot (proposed 06, between OMK and marina).
3. **8 SOA domain numbering drift** — `entity_solaris_os.md` uses SOA01-08,
   Picard `B2_Business_Domains` uses 01-08 in different order. **Reconcile
   to SOA numbering** in any new code (types, route prefixes, repo names).
4. **`@supabase/ssr` is the new pattern** — the package uses the new SSR-aware
   Supabase client (not the older `auth-helpers`). This is the right choice
   for Next.js 16 App Router. Per Supabase docs, you need a server client
   (in `lib/supabase/server.ts`) + a browser client (`client.ts`), with
   cookie management done in middleware.
5. **Tailwind 4** uses `@tailwindcss/postcss` (not the old `tailwind.config.js`).
   Both `apps/` have `postcss.config.mjs` already.
6. **Next.js 16.2.6 is bleeding edge** — the community fork
   `abc-childcare-portal` is on 16.2.7, the community app `abc-os-community`
   is on 15.5.19. Solaris is on the latest 16.x. **There may be breaking
   changes vs older docs.** Read `node_modules/next/dist/docs/` before
   writing any new code (per the `AGENTS.md` nextjs-agent-rules warning).
7. **The middleware already implements the 3-phase OMK pattern** (refresh
   session, gate protected routes, inject x-tenant-org-id) — **use it as
   the template** for understanding and extending auth. Do NOT bypass it
   with custom auth in components.
8. **Repository pattern is split into `.client.ts` and `.server.ts`** —
   `.client.ts` for browser-side calls (with anon key, respects RLS),
   `.server.ts` for server components / route handlers (with anon key
   from cookies, also respects RLS). **Use the right split for context.**
9. **`lucide-react@^1.16.0` is suspect** — current canonical Lucide is
   `lucide-react@^0.5xx` (the leading 0 was the convention). `^1.16.0` looks
   like a stale or forked package. The dashboard imports from
   `lucide-react` (e.g., `PanelRightClose`, `Search`, `Leaf` in `page.tsx`).
   **Verify the package is legitimate and update if a newer version is
   available.**
10. **The TypeScript rules in `~/.claude/rules/ecc/typescript/` are auto-loaded**
    in every session — follow them (no `any`, immutable updates, Zod for
    input validation, no `console.log` in production, Playwright for E2E).

## Recommended order of work (D1 — verify before assert on each step)

1. **Verify the GitHub repo URL with A0** — `Amdkn/00-AaaS-Agency-Garden` vs
   `Amdkn/00-Solaris`. Affects tickets #1, #11, #12.
2. **Reconnect git** — `git init` + `git remote add` + `git pull` (or push
   the local as canonical). Add a root `.gitignore` for the monorepo.
3. **Create `apps/dashboard/.env.example`** (ticket #4) — quick win,
   unblocks local dev for other agents.
4. **Refresh `REBUILD_WORKFLOW.md`** (ticket #6) — update §0 to reflect
   current state. Critical for new agents picking up the work.
5. **Rewrite `apps/dashboard/AGENTS.md`** (ticket #2) — encode the 8 SOA
   mapping, dual-mode runtime, 12 view → 8 domain mapping, the 12 open
   tickets, the Dokploy deploy target.
6. **Refresh `picard_audit.md`** (ticket #7) — add the 2026-06-10 addendum
   noting Phase A-F complete, Phase G in progress.
7. **Rewrite `README.md`** files (ticket #5) — both dashboard and landing,
   ABC OS-specific content, link to entity_solaris_os.md + REBUILD_WORKFLOW.
8. **Wire constants.ts → repos** (ticket #3, Phase G) — the bulk of the
   dev work. Replace mock data with Supabase queries in the 12 views.
9. **Locate + wire Zod contracts** (ticket #8) — `entity_zod.md` is the
   canon, contracts are per domain.
10. **Locate + wire Symphony Router** (ticket #9) — `entity_symphony_router.md`
    is the canon, AiPanel is the UI surface.
11. **Add tests** (ticket #10) — Playwright E2E at minimum, visual regression
    at 320/768/1024/1440 (per ECC web/testing.md).
12. **Wire Dokploy deploy** (ticket #11) — per OMK's deploy pattern + Dokploy
    API (Dokploy API key is in env User, not in repo).
13. **Iterate on the product** — once data layer, deploy, docs, tests are
    all wired, the receiving session can finally build features against
    real Supabase data.

## Verification (D5 — proof on file)

After each step, prove it works:

| Step | Verification |
|------|--------------|
| 1 (A0 verify) | A0 confirms GitHub URL in chat (D1) |
| 2 (git) | `git status` shows clean working tree with `.gitignore` respected |
| 3 (env example) | `cat .env.example` shows the 4 documented env vars |
| 4 (workflow refresh) | `REBUILD_WORKFLOW.md §0` reflects current state (not "100% mock") |
| 5 (AGENTS.md) | File contains 8 SOA domain names, Vercel reserved `/build` note, Dokploy deploy target |
| 6 (picard audit) | Addendum dated 2026-06-10 present, lists 12 open tickets |
| 7 (READMEs) | `grep "Geist" README.md` returns 0 (boilerplate replaced) on BOTH apps |
| 8 (data layer) | `npm run dev` + visit `/` shows real data from Supabase, not mock constants |
| 9 (Zod) | Server actions parse inputs with Zod, return validation errors on bad input |
| 10 (Symphony) | AiPanel can dispatch a routed intent (e.g., "create Growth experiment from Sales lead") and receive a response |
| 11 (tests) | `npm run test:e2e` runs and passes for the 12 views + auth flow |
| 12 (deploy) | `git push` triggers Dokploy rebuild, `app.aspace.fr` serves the new build within 5 min |

## Write back to the source session (and the wiki)

When meaningful work is done, append a one-liner to:
1. `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` under `[2026-06-10]`.
2. `00_Amadeus/30_MEMORY_CORE/README.md` same date bullet.
3. `30_Business_OS/10_Projects/solaris/apps/dashboard/AGENTS.md` (when
   rewritten) → update the 12 open tickets as items close.
4. `30_Business_OS/10_Projects/solaris/apps/dashboard/REBUILD_WORKFLOW.md`
   → update §0 to reflect current state.
5. `30_Business_OS/10_Projects/solaris/apps/dashboard/picard_audit.md` →
   add 2026-06-10 addendum.

## Residual risks

- **Repo URL ambiguity** — `Amdkn/00-AaaS-Agency-Garden` vs `Amdkn/00-Solaris`.
  Two URLs surface in canon. May be a rename, may be two separate repos.
  **Verify with A0** before any push.
- **Picard slot 03 is taken** (`03_RILCOT_Members_Space_OS`). AaaS lives in
  `00 Agency as a Service` (B0). **Verify with A0** whether to promote AaaS
  to a numbered slot.
- **8 SOA domain numbering drift** — entity uses SOA01-08, Picard uses
  01-08 in different order. **Reconcile to SOA** in new code.
- **`lucide-react@^1.16.0` suspect version** — verify before relying on it.
- **No tests, no CI** — greenfield-style gap. Add Playwright + visual
  regression at minimum.
- **No Vercel vs Dokploy documentation** — the create-next-app defaults +
  `.vercel` gitignore suggest Vercel, but `next.config.ts: 'standalone'` +
  Dockerfile + Sovereign OS doctrine say Dokploy. **Document this in
  AGENTS.md** so future agents don't default to Vercel.
- **`constants.ts` is the entire data layer's mock source** — when wiring
  the data layer, search for ALL imports of `constants.ts` to find all the
  mock-data touch points. The repos exist but may not be imported yet.
- **Middleware hardcodes 12 protected routes** that don't actually exist
  in the App Router (the page.tsx is SPA-style). If real per-view routes
  are added later, **update `PROTECTED_ROUTES` in middleware.ts**.
- **The AGENTS.md nextjs-agent-rules warning is auto-injected by the
  childcare fork's tooling** — read it before writing any Next.js code.
  "This is NOT the Next.js you know" — APIs differ from training data.

## Next safe action for the receiving session

1. Read this handoff end-to-end.
2. Read the 12 files listed in `## Files to read FIRST` (in order).
3. **STOP at ticket #12** — open a chat with A0 to verify the GitHub
   repo URL and Picard slot. Do not reconnect git or push without this.
4. Once A0 confirms, follow the 13-step order of work above.
5. Report progress back via the wiki log + README + future AGENTS.md.

## Skill proposal (open follow-up)

The "delegating substantial project work between sessions" workflow (read
8-12 contract files → gap-analyze against actual state → triage tickets
by impact → write handoff with verification matrix) is a recurring pattern
that may apply to future L0/L1/L2 projects. Consider creating a
`/project-handoff` skill that encapsulates:
- The 4-section contract structure (Why / State / Tickets / Verify)
- The Doctrine Anti-Paresse "verify before assert" check
- The Picard slot reservation checklist
- The doctrine junction verification (`_doctrine` symlink target)
- The deploy target decision matrix (Vercel vs Dokploy vs other)
- The write-back protocol (wiki log + AGENTS.md + REBUILD_WORKFLOW)

The 4 handoffs in this session (graphify, ABC OS, OMK, Solaris) are all
distinct, but a meta-skill for **delegating project work between sessions**
would save the next A0 the ~10-15 minutes of "find files, draft structure,
write handoff" overhead. The proposal is queued in
`00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/skills_queue.md`.

## Secret handling

- `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY` are PUBLIC
  (bundled in JS). Safe to put in `.env.example` as placeholder.
- `SUPABASE_SERVICE_ROLE_KEY` is **NEVER** client-side. Server-only.
- Dokploy API key + Hostinger API token (per system state 2026-06-10) are
  exposed — flagged for rotation by A0. Do NOT echo values in chat/code/logs.
- GitHub deploy tokens: scope to repo, expire after deploy, never in repo files.
- `.env.local` is gitignored (per `apps/dashboard/.gitignore` line 34: `.env*`).
  Do not commit `.env.local`, `.env.production`, etc.
