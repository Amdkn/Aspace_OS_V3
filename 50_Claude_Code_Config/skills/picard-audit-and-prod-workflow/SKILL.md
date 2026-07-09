---
name: picard-audit-and-prod-workflow
description: >
  End-to-end workflow to audit a legacy frontend prototype, migrate it to Next.js 15 + TS (born-short ADR-INFRA-002),
  verify it locally (Phase 4-5), push to GitHub, and deploy it through a HYBRID route: Vercel for front-only apps
  (Next.js / Vite SPA) and Dokploy via MCP for back/services/stateful workers. Adds an explicit Dashboard+Supabase
  path that delegates to /aspace-supabase-mastery for schema audit, RLS, and PostgREST exposure on the self-hosted
  Supabase (148.230.92.235). Trigger on "apply picard audit", "migrate and deploy", "prod workflow picard",
  "transform prototype", "deploy dashboard with supabase", or "vercel + supabase prod workflow".
---

# Picard Audit & Production Workflow (ADR-INFRA-002, Hybrid Vercel ⇆ Dokploy + Supabase)

You are an expert architect and implementation agent for **Project Picard**. Your mission is to transform "Prototype-Grade" legacy projects (HTML + CDN-Babel JSX snippets) into "Production-Grade" Next.js 15 TypeScript applications, verify their builds, version them on GitHub, and deploy them through the right specialist for the workload.

**Deployment is no longer one-size-fits-all.** Picard is a *conductor* that routes to leaf skills based on the app's shape:

| Workload | Route to leaf skill / tool |
|---|---|
| Front-only (Next.js, Vite SPA, marketing) | `/vercel-deploy-from-github` |
| Back / service / worker / stateful | Dokploy MCP (dokploy + hostinger) |
| App uses `@supabase/supabase-js` or `VITE_SUPABASE_URL` | `/aspace-supabase-mastery` (audit + schema + RLS) |

ADR-META-001 applies: **D2 Research FIRST** (read the leaf skill before invoking it), **D5 No self-congratulation before proof** (curl-verify each deploy step).

---

## 🧭 The End-to-End Workflow (7 Phases)

### Phase 1 — Deep Ingestion & Audit
Scan the legacy prototype directory and create a `picard_audit.md` file in its root.
1. **Scan**: Analyze HTML, JSX, CSS, Assets.
2. **Audit Score**: Rate Design (x/10) vs Infrastructure (0/10 for raw prototypes).
3. **Debt List**: Classify critical (CDN links, no Git, Babel-in-browser), high (global state, no types), and medium (inline CSS, no SEO) debt.
4. **Plan**: Formulate the migration path to Next.js 15.
5. **Detect backend shape**: grep the legacy code for `fetch(`, `XMLHttpRequest`, `import.*supabase`, `import.*axios` — record what the new app will need.

### Phase 2 — A0 Approval Gate (incl. deploy target choice)
**STOP** and present the `picard_audit.md` to A0 (the user). Wait for explicit approval ("Go") before touching any code. **At this gate, also confirm the deploy target:**
- `vercel` — front-only / SSR / static (Pro: instant preview, GitHub auto-deploy, zero infra. Con: no persistent workers/disks).
- `dokploy` — back / service / stateful (Pro: sovereign on VPS, $0/mo. Con: ops burden).
- `hybrid` — front on Vercel + back/state on Dokploy + Supabase on VPS (default for Dashboard apps needing Supabase).

Record the choice in the audit doc; downstream phases branch on it.

### Phase 3 — Born-Short Repo Migration (ADR-INFRA-002)
After approval, migrate the repository to its short canonical home under `30_Business_OS/` to avoid Windows `MAX_PATH` (>260 chars) build errors:
1. **Target Directory**: `C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\<project_name>\apps\<app_name>`
2. **Git Init**: Initialize a local git repository (`git init -b main`).
3. **Scaffold Next.js 15**:
   ```powershell
   npx -y create-next-app@15 . --ts --tailwind --app --src-dir --eslint --no-src-dir
   ```
4. **Junction Link**: Link the deep Verse doctrine folder to this short home:
   ```powershell
   New-Item -ItemType Junction -Path "<Deep_Verse_Path>\_app" -Target "C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\<project_name>\apps\<app_name>"
   ```

### Phase 4 — ESM & TypeScript Refactoring
Refactor the legacy prototype files into structured Next.js Page Router or App Router components:
1. **Convert to TSX**: Rename `.jsx` -> `.tsx` and add types/interfaces for all components and states.
2. **Convert Globals to ESM**: Replace legacy window binding patterns (e.g. `Object.assign(window, ...)` or `<script>` bindings) with standard ESM `export`/`import`.
3. **Extract CSS & Tailwind**: Move inline CSS to `globals.css` or Tailwind classes. Centralize design tokens in `src/design/tokens.ts`.
4. **Local Fonts & Asset Optimization**: Download Google Fonts locally, use `next/font/local` to avoid FCP delay.
5. **SEO & Metadata**: Add descriptive page titles, meta descriptions, OpenGraph tags, and favicon config.
6. **Local Persistence**: Implement robust `localStorage` client-side hooks (`useLocalStorage`) for user options/tweaks, removing any parent `postMessage` dependencies.
7. **Repository pattern** (if backend present): see common/patterns.md — define `Repository<T>` with `findAll / findById / create / update / delete` and route to Supabase when env is set, localStorage fallback otherwise.

### Phase 5 — Quality Gate & Local Validation
Ensure the application is compilation-error-free and runs stably:
1. **Type-Check**: Run `npx tsc --noEmit` and fix all strict TypeScript errors.
2. **Build-Verify**: Run `npm run build` and ensure the bundle compilation completes with `0` errors.
3. **Dev Boot**: Start the development server (`npm run dev`) **strictly inside the specific subdirectory** containing the `package.json` (ADR-INFRA-002 Hard Rule).
4. **Smoke Test**: Run a curl request (`curl -I http://localhost:3000`) and verify it returns a `200 OK` status with the correct title.
5. **If Supabase is wired**: visit `/api/healthz` (or the home page) and confirm the console shows `[supabase]` env banner is **not** warning "missing". If it warns, the env wiring is incomplete — fix before Phase 6.

### Phase 6 — Hybrid Deploy + Backend Wiring (the new shape)

Phase 6 routes to the right specialist. **Do not improvise a manual deploy** — always go through a leaf skill or MCP tool, never the browser.

#### 6.1 Pre-conditions (verify before any deploy)
- [ ] `git log --oneline | head` shows clean commit history
- [ ] GitHub repo exists and A0 has confirmed the URL
- [ ] `.env.example` lists **all** required env vars (no real values — public-only convention)
- [ ] No `console.log` left in production code (per common/coding-style)
- [ ] Tests ≥ 80% coverage (per common/testing)
- [ ] `package.json` has correct `engines.node` and the right framework preset
- [ ] If deploying to Vercel: Tailwind/postcss oxide native bindings are in `devDependencies` (Vercel `npm install` resolves devDeps)
- [ ] If deploying to Dokploy: a Dockerfile OR a buildable image plan is committed
- [ ] No secrets in source: scan `git grep -E '(api[_-]?key|password|token|secret).*=.{16,}'` → must return 0 hits

#### 6.2A Vercel path (front-only)
Hand off to **`/vercel-deploy-from-github`** skill. It handles the full 3-step flow: `vercel link` → `vercel deploy --prod` → `curl` verify, plus GitHub auto-deploy webhook wiring.

The leaf skill bakes in: amd-lab team (`team_d3JjRK4fJUE9ACohbdlhv9Gc`), iad1 region, Next.js/Turbopack auto-detection, known-error filters (401 on per-deploy URLs is expected, `--team` deprecation is cosmetic, Tailwind oxide Linux binding resolution).

**Do not** re-implement these steps in picard — they live in the leaf skill to keep responsibilities clean.

#### 6.2B Dokploy path (back / service / stateful)
Stay on MCP-driven flow. Use the local `dokploy` MCP server (registered in `~/.claude/mcp-configs/mcp-servers.json`):
1. **GitHub Push** (if not already done):
   - `git remote add origin <URL>` (HITL: ask A0 for the URL)
   - Conventional commit
   - `git push -u origin main`
2. **Dokploy app create + bind** (MCP `dokploy` server):
   - `applicationCreate` to instantiate the application
   - `applicationSaveGithubProvider` (or similar Git tool) to link the app to the GitHub repo
   - `applicationSaveBuildType` to specify the framework preset (Next.js / Node / Docker)
   - `applicationSaveEnvironment` to inject env vars (Supabase URL, ANON key, etc.)
   - `applicationDeploy` to trigger the build
   - `applicationReadAppMonitoring` for build/deploy status
3. **Hostinger DNS** (MCP `hostinger` server):
   - `DNS_updateDNSRecordsV1` to point the subdomain to VPS IP `148.230.92.235`
4. **Production smoke test**: `curl -I https://<subdomain>` → expect `200 OK`

#### 6.3 Supabase backend wiring (Dashboard apps needing a DB)

**Trigger condition** — at least one of:
- `package.json` has `@supabase/supabase-js` in dependencies
- `.env.example` lists `VITE_SUPABASE_URL` or `VITE_SUPABASE_ANON_KEY` (or `SUPABASE_URL` / `SUPABASE_SERVICE_ROLE_KEY` for server)
- The app calls `supabase.from(...)` anywhere in `src/`

If triggered, hand off to **`/aspace-supabase-mastery`** skill. It handles:
- Topology check: VPS reachable via `ssh aspace-vps`, `docker ps | grep supabase-` shows 12+ containers
- Schema audit: which `<product>_internal` and `<product>_saas` schemas exist, with RLS, policies, grants, default privileges
- Schema creation: idempotent, with the **correct grants pattern** (gotcha #2 from the leaf skill — `ALTER DEFAULT PRIVILEGES` only applies to future tables, must `GRANT` explicitly for existing)
- Multi-tenancy doctrine (ADR-OMK-001 / ADR-SUPABASE-001): one schema per product, RLS-by-org for `*_saas` (`org_id` in JWT via custom access token hook), schema-USAGE for staff on `*_internal` only
- PostgREST exposure: add the schema to `PGRST_DB_SCHEMAS` in `/srv/aspace/supabase/docker/.env` + restart `supabase-rest`
- Defense-in-depth: enable RLS on `*_internal` with a `staff_only` policy (so the schema USAGE grant is not the only barrier)
- Live verification (D5 protocol from the leaf skill): 200 [] on saas, 401 on internal, 200 on public — no regression

**Required pre-conditions for the Supabase handoff:**
- [ ] VPS reachable: `ssh aspace-vps "uptime"` succeeds
- [ ] Supabase running: `docker ps | grep supabase-` shows healthy containers
- [ ] `mcp-supabase-launch.sh` resolves `supabase-db` IP dynamically (per the 2026-06-08 fix that replaced the hardcoded `172.19.0.2` with `docker inspect` lookup)
- [ ] `DOCKER-USER` chain has ACCEPT for `172.16.0.0/12` on `5432,6543,8000,8001,8443` (gotcha #1 — otherwise container→container traffic dies with "connection timed out" while the DB itself is healthy)

**Do not** attempt to run DDL from this skill. The leaf skill owns every Supabase mutation.

#### 6.4 Env var wiring (after deploy target chosen)
- **Vercel**: `vercel env add VITE_SUPABASE_URL production` + `vercel env add VITE_SUPABASE_ANON_KEY production`, then re-trigger deploy. Confirm with `vercel env ls production`.
- **Dokploy**: `applicationSaveEnvironment` MCP call with the same key names (transformed if the framework needs server-side equivalents).
- **Self-host on VPS**: write to `.env` on the deploy host (gitignored). Never commit.

`ANON_KEY` is public (client-side) but still don't paste it in chat, .md, .json, or git. `SERVICE_ROLE_KEY` is admin — never reaches the browser. Both come from `/srv/aspace/supabase/docker/.env` on the VPS.

#### 6.5 Final production verify (D5 — proof before done)
- App URL: `curl -I <url>` → 200
- Supabase path: open in browser → dev tools console shows **no** `[supabase] VITE_SUPABASE_URL missing` warning → useCollection resolves from Supabase, not localStorage fallback
- If both modes (internal + saas) are intended: deploy two Vercel projects (or two Dokploy apps) with different `VITE_APP_MODE` env values (`internal` vs `saas`), per ADR-OMK-001 D1
- RLS gates from production: hit `kong:8000/rest/v1/<table>` with the production ANON key + `Accept-Profile: <schema>` → 200 [] (saas) or 401 (internal)

### Phase 7 — Digital Twin Logging
Record the operation in the sovereign tracking documents:
- **README**: Add a bullet point summary in `00_Amadeus/30_MEMORY_CORE/README.md`.
- **LLM Wiki Log**: Add a chronologically formatted entry in `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` under the current ISO date `[YYYY-MM-DD]`.
- **Memory Core canon**: if a new ADR-worthy decision was made (e.g. a new schema, a new deploy target combo), append to `_SPECS/ADR/`.

---

## 🛡️ Operational Safeguards
1. **Read-Only Audit**: Do not modify any source code files during Phase 1 (Audit).
2. **Port Hygiene**: Never leave multiple dev servers running on the same port. Use `3003` for alternative previews or test suites, and clean up active PIDs after verification.
3. **Secrets Management**: Never write passwords, API keys, or cookies into git, the wiki, or the chat. Read secrets from local `.env` files or secure paths.
4. **No manual browser deploy**: This skill never says "open Dokploy UI and click Deploy" — the MCP tools exist for a reason. Browser is fallback only when MCP is broken and A0 explicitly approves manual mode.
5. **Leaf skills are the source of truth** for their domain — read them, don't paraphrase or re-derive their steps. If a leaf skill's steps look outdated, fix the leaf skill, not this one.

---

## 🔗 Related Skills
- **`/vercel-deploy-from-github`** — the Vercel 3-step leaf (link → deploy → verify). 171 lines, indexed in available_skills.
- **`/aspace-supabase-mastery`** — the self-hosted Supabase on `aspace-vps` leaf (multi-tenancy, RLS, grants, PostgREST exposure, the 2 critical gotchas). 113 lines, indexed.
- **`/dokploy-mcp-ops`** (referenced via `mcp-configs/mcp-servers.json`) — the `dokploy` MCP server config and the launch commands for `applicationCreate` / `applicationSaveGithubProvider` / `applicationSaveBuildType` / `applicationSaveEnvironment` / `applicationDeploy`.
- **`/replicate-squads`** — if the deploy needs the A'Space agent roster replicated to the new env.

## 📜 Change Log
- **2026-06-09** — Phase 6 refactored: Dokploy-only → **hybrid Vercel ⇆ Dokploy** with explicit Supabase handoff. Default for Dashboard apps needing Supabase is `hybrid`. Pre-conditions checklist added. Leaf skills promoted to first-class citizens (this skill is now a conductor).
- **2026-06-08** — Phase 6 rewritten to use Dokploy MCP instead of manual browser. Created `mcp-supabase-launch.sh` with dynamic IP resolution (fix for the `172.19.0.2 → 172.19.0.3` drift).
- **earlier** — Initial 7-phase workflow with Dokploy browser deploy.
