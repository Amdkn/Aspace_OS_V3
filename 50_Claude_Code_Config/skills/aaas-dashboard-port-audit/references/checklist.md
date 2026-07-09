# AaaS Dashboard Port Audit — Checklist

Reusable checklist. Tick every box before the audit is considered complete.
Include this list (with ticks) in the `port-plan-<date>.md` appendix.

---

## 0. Pre-audit setup

- [ ] Read target `CLAUDE.md` — confirm it exists and references ADR-META-001
- [ ] Read target `package.json` — capture runtime (Vite / Next / other),
      router, state, icon lib
- [ ] Read target `AGENTS.md` (if present) — capture local conventions
- [ ] Read AaaS doctrine files (cite each in the report):
  - [ ] `ASpace_OS_V2/_SPECS/ADR/ADR-INFRA-002_repo-home-junction.md`
  - [ ] `ASpace_OS_V2/_SPECS/ADR/ADR-INFRA-003_ceo-dashboard.md`
  - [ ] `ASpace_OS_V2/_SPECS/ADR/ADR-CANON-001_agent-roster.md`
  - [ ] `ASpace_OS_V2/_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md`
  - [ ] `ASpace_OS_V2/00_Amadeus/01_Identity_Core/AGENTS.md`
- [ ] Confirm the 4 ADR blockers status (see section 7 below) — STOP if any
      is open
- [ ] Confirm `source` arg resolves to the AaaS Solaris reference; if
      ambiguous, ASK A0

## 1. Runtime diff

- [ ] Bundler: Vite vs Next.js vs Remix vs other
- [ ] Render model: SPA (CSR) vs RSC vs SSG vs hybrid
- [ ] Router: react-router vs next/navigation vs tanstack-router vs other
- [ ] State: Zustand vs Redux vs Jotai vs RSC server actions vs other
- [ ] Auth gate: middleware vs HOC vs client-side guard
- [ ] Data fetching: TanStack Query vs SWR vs server components vs other
- [ ] Env management: `.env.local` vs Vercel env vs User-scope Windows env
- [ ] Note every divergence in a table; flag RSC-only files for `adapt` if
      target is Vite

## 2. Schema diff

- [ ] Schema location: `internal` (single-tenant) vs `saas` (multi-tenant)
- [ ] Table prefix: `omk_*` vs `solaris_*` vs other
- [ ] ORM: Drizzle vs Prisma vs raw SQL
- [ ] Migrations dir present and ordered
- [ ] RLS policies defined (saas only)
- [ ] Generated types committed
- [ ] Seeders present and runnable
- [ ] Note any table that exists in only one side

## 3. View parity (12 views)

For each view, mark: `present` / `partial` / `missing` / `divergent`.

### CULTIVATE
- [ ] Dashboard
- [ ] Finance
- [ ] Clients
- [ ] Tasks

### NURTURE
- [ ] SOP
- [ ] Legal
- [ ] Growth

### BLOOM
- [ ] Marketplace
- [ ] Sales

### ROOTS
- [ ] ItData
- [ ] People
- [ ] Settings

For each present view, capture: route path, primary components, data
sources, skeleton/empty/error state coverage.

## 4. Nav group parity (4 groups)

- [ ] `CULTIVATE` group present and routes to the 4 views above
- [ ] `NURTURE` group present and routes to the 3 views above
- [ ] `BLOOM` group present and routes to the 2 views above
- [ ] `ROOTS` group present and routes to the 3 views above
- [ ] Group order matches doctrine (CULTIVATE → NURTURE → BLOOM → ROOTS)
- [ ] No orphan routes (routes not in any group)
- [ ] No orphan groups (groups with no routes)

## 5. Sidebar structure parity

- [ ] Sidebar component exists (`Sidebar.tsx` or equivalent)
- [ ] Uses lucide icons (not heroicons / tabler / other lib)
- [ ] Collapsible (groups can expand/collapse)
- [ ] `NavGroup` enum / const present in `lib/nav.ts`
- [ ] `NavView` enum / const present in `lib/nav.ts`
- [ ] Route map keyed by `NavView`
- [ ] Active state styling intentional (not generic)
- [ ] Mobile responsive (drawer or hidden below md)

## 6. Skeletons + empty states parity

- [ ] Skeleton component(s) defined (one per view is fine)
- [ ] Empty state component(s) defined with icon + message + CTA
- [ ] Error boundary at the route level
- [ ] Loading state uses skeletons (not spinners) by default
- [ ] No view relies on a single `null` or `loading...` text fallback

## 7. ADR blockers status check

The audit HALTS and reports back to A0 if any of these is open.

- [ ] **ADR-RICK-001 (OpenHarness Incarnation)** — status: `resolved` /
      `open` / `N-A`
- [ ] **ADR-META-001 (Anti-Paresse Verify-Before-Assert)** — target has
      `CLAUDE.md` citing the doctrine — status: `resolved` / `open`
- [ ] **ADR-INFRA-002 (Repo-Home / Junction doctrine)** — target lives under
      a `_doctrine/` junction — status: `resolved` / `open`
- [ ] **ADR-INFRA-003 (CEO Dashboard doctrine)** — target has
      `_doctrine/NAV_DOCTRINE.md` + `_doctrine/REBUILD_WORKFLOW.md` matching
      12/4 — status: `resolved` / `open`

## 8. Report completeness

- [ ] Header (date, target, source, scope, doctrine rev)
- [ ] Doctrine check (section 7 above copied verbatim)
- [ ] Executive summary (1 paragraph, top 3 blockers)
- [ ] Runtime delta table
- [ ] Schema delta table
- [ ] View parity matrix (12 rows × 4 group columns)
- [ ] Nav parity table
- [ ] Gap list (must / should / nice / out-of-scope)
- [ ] File-by-file recommendations (`cp` / `adapt` / `rewrite` per file)
- [ ] Open questions for A0
- [ ] "What we will NOT change" section
- [ ] References (every cited file with hash/commit if possible)
- [ ] This checklist included as appendix, with every box ticked

---

## Doctrine quick-cite

| Item | Canonical source |
|------|------------------|
| 4 nav groups | `NAV_DOCTRINE.md` § Groups |
| 12 views | `NAV_DOCTRINE.md` § Views |
| `solaris_*` prefix | `NAV_DOCTRINE.md` § Schema (saas) |
| `omk_*` prefix | internal / legacy doctrine |
| Sidebar lucide | `NAV_DOCTRINE.md` § Sidebar |
| 4 ADR blockers | `SKILL.md` § Doctrine constraints |
| No-hard-delete | global `CLAUDE.md` § Loi du Checkpoint Profond |
| Test Key Pragma | global `CLAUDE.md` § Doctrine Test Key Pragma |
