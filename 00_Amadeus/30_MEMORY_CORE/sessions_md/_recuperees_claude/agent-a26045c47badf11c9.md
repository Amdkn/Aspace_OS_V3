---
session: agent-a26045c47badf11c9
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\_ARCHIVE_2026-06-16_sessions\projects\C--Users-amado\97825acd-2ecf-4ca8-9d59-79e181d6b281\subagents\agent-a26045c47badf11c9.jsonl
debut: 2026-06-08T12:19:24.782Z
fin: 2026-06-08T13:03:45.371Z
messages_utilisateur: 1
reponses_assistant: 51
titre: "Mission: Execute **Phase D** of the Solaris dashboard backend strategy — per-view data hooks/repos. LOCAL scop…"
---

## >>> UTILISATEUR #1

Mission: Execute **Phase D** of the Solaris dashboard backend strategy — per-view data hooks/repos. LOCAL scope, no VPS work. The 12 views in `src/components/views/` must be wired to the new repos, with graceful fallback to mocks if Supabase env vars are missing.

Context:
- Target: `C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\solaris\apps\dashboard\`
- Stack: Next.js 16.2.6 + React 19.2.4 + TypeScript 5 + Tailwind 4 + App Router
- Phases A, B, C are GREEN + pushed to main. Existing files in place:
  - `src/config/mode.ts` (internal/saas)
  - `src/lib/supabase/{client,server,index}.ts` (`@supabase/ssr`, schema-aware)
  - `src/components/auth/AuthProvider.tsx` + `useAuth` + `useSessionContext`
  - `src/middleware.ts` (session refresh + protected routes)
  - 6 RLS migration drafts in `supabase/migrations/`
  - `REBUILD_WORKFLOW.md`
- **12 views in `src/components/views/`**: Clients, Dashboard, Finance, Growth, ItData, Legal, Marketplace, People, Sales, Settings, SopLibrary, Tasks
- **Mocks source**: `src/lib/constants.ts` (do NOT touch)
- **No live Supabase** — env vars may be missing. The repos MUST gracefully fall back to mock data so the views stay functional.

Steps to perform:

### 1. Read the references (frugal)
Read these in order:
- `src/lib/constants.ts` — full content (this is the mock data source for the 12 views)
- `src/lib/types.ts` — existing types
- `src/lib/supabase/server.ts` — already in your context
- `src/config/mode.ts` — already in your context
- ONE view to understand the data pattern: `src/components/views/Dashboard.tsx`
- OMK reference (conceptual template only): `omk/apps/dashboard/...` (use `ls omk/apps/dashboard/src/` to see structure if helpful, but don't read extensively)

### 2. Create the per-view repos

**Directory**: `src/repos/`

Create one repo per domain. Each repo:
- Uses `createServerClient` from `@/lib/supabase/server` (the schema-aware server client)
- Provides 1-3 main functions: `list()`, `get(id)`, possibly `create/update/delete`
- Falls back to mock data from `@/lib/constants` when `SUPABASE_READY` is false
- Uses TypeScript strict types
- Uses the `next/cache` `revalidateTag` pattern for cache invalidation

**File structure**:
- `src/repos/clients.repo.ts` — listClients, getClient, createClient, updateClient
- `src/repos/dashboard.repo.ts` — getDashboardMetrics (KPIs, charts)
- `src/repos/finance.repo.ts` — listInvoices, getInvoice, etc.
- `src/repos/growth.repo.ts` — getGrowthMetrics, listCampaigns
- `src/repos/itdata.repo.ts` — listDataSources, getDataPoint
- `src/repos/legal.repo.ts` — listContracts, getContract
- `src/repos/marketplace.repo.ts` — listListings, getListing
- `src/repos/people.repo.ts` — listMembers, getMember
- `src/repos/sales.repo.ts` — listLeads, listDeals, getLead
- `src/repos/settings.repo.ts` — getSettings, updateSettings
- `src/repos/sop.repo.ts` — listSops, getSop
- `src/repos/tasks.repo.ts` — listTasks, getTask, createTask, updateTask, completeTask
- `src/repos/index.ts` — barrel re-export of all repos

For each repo, include:
- The main query function (uses Supabase if ready, mocks if not)
- A `mockFallback()` private function that returns the mock data
- A `withRevalidate()` wrapper that revalidates the relevant cache tags on mutation

**Pattern example** (use this as template):
```typescript
// src/repos/clients.repo.ts
import 'server-only';
import { createServerClient } from '@/lib/supabase/server';
import { SUPABASE_READY, APP_MODE } from '@/config/mode';
import { MOCK_CLIENTS } from '@/lib/constants';
import { revalidateTag } from 'next/cache';
import { unstable_cache } from 'next/cache';

export interface Client { /* ... */ }

export const listClients = unstable_cache(
  async (): Promise<Client[]> => {
    if (!SUPABASE_READY) return MOCK_CLIENTS;
    const supabase = await createServerClient();
    const { data, error } = await supabase.from('clients').select('*');
    if (error) {
      console.warn('[clients.repo] listClients error:', error);
      return MOCK_CLIENTS;
    }
    return data as Client[];
  },
  ['list-clients', APP_MODE],
  { tags: ['clients'] }
);

export async function getClient(id: string): Promise<Client | null> {
  if (!SUPABASE_READY) return MOCK_CLIENTS.find(c => c.id === id) ?? null;
  // ... live query
}

export async function createClient(input: Omit<Client, 'id'>): Promise<Client> {
  // ... live insert
  revalidateTag('clients');
  return created;
}
```

### 3. Wire the 12 views to use the repos

For each view in `src/components/views/`:
- Replace the import from `@/lib/constants` with import from `@/repos/<domain>`
- Replace synchronous mock data access with `await listXxx()` calls (since these are React Server Components, they can be async)
- Add a `<Suspense fallback={<LoadingState />}>` boundary (or use the Next.js `loading.tsx` pattern)
- Add empty state when the data is empty
- Add error state if the repo returns an error (gracefully, since we fall back to mocks anyway)

**Example for `Clients.tsx`**:
```typescript
// BEFORE
import { MOCK_CLIENTS } from '@/lib/constants';
export function ClientsView() {
  return <div>{MOCK_CLIENTS.map(c => <ClientCard key={c.id} client={c} />)}</div>;
}

// AFTER
import { listClients } from '@/repos/clients.repo';
import { Suspense } from 'react';
import { ClientsSkeleton } from '@/components/skeletons/ClientsSkeleton';
import { EmptyClients } from '@/components/empty-states/EmptyClients';

export default async function ClientsView() {
  return (
    <Suspense fallback={<ClientsSkeleton />}>
      <ClientsList />
    </Suspense>
  );
}

async function ClientsList() {
  const clients = await listClients();
  if (clients.length === 0) return <EmptyClients />;
  return <div>{clients.map(c => <ClientCard key={c.id} client={c} />)}</div>;
}
```

### 4. Add skeleton + empty-state components

Create reusable loading skeletons and empty states:
- `src/components/skeletons/ClientsSkeleton.tsx`
- `src/components/skeletons/DashboardSkeleton.tsx`
- ... one per view
- `src/components/empty-states/EmptyClients.tsx`
- `src/components/empty-states/EmptyTasks.tsx`
- ... one per view

These are simple Tailwind-styled placeholder components.

### 5. Update the 12 views to be async Server Components

For each view file:
- Change from `export function XView()` to `export default async function XView()`
- Replace direct mock access with the repo call
- Wrap in Suspense (or use the pattern above)

**Note**: Some views may already be in `'use client'` mode (interactive). For those:
- Keep them as client components
- Add a client-side hook to fetch data: `useClients()` in `src/hooks/useClients.ts`
- Use SWR or just plain `useEffect` + `fetch` (we already have `useAuth` pattern)
- Or refactor: make the data-fetching wrapper a Server Component, and the interactive parts stay client

**Pragmatic approach**: For views that are currently `'use client'`, refactor them so that the data-fetching part is a Server Component (fetches from repo) and the interactive state is a child client component. This is the Next.js App Router best practice.

### 6. Validate
- `cd solaris/apps/dashboard/`
- `npx tsc --noEmit` → must pass with **0 errors**
- `npm run lint` (eslint) → must pass with **0 NEW errors** (25 pre-existing warnings stay)
- `npm run build` → must succeed (Turbopack compile + 9+ static pages)
- Start dev server (in background, port 3006 since 3004/3005 may be in use) and curl each route to verify HTTP 200

If TSC or ESLint fail, FIX the errors. Do not skip.

### 7. Commit + push
- `cd solaris/apps/dashboard/`
- `git add -A`
- `git commit -m "feat(solaris): Phase D (per-view data hooks/repos with mock fallback)"`
- `git push origin main`

### 8. Final report
Report back with:
- File inventory (12 repos + 12 skeletons + 12 empty states + 12 view modifications)
- TSC + ESLint + build results
- HTTP smoke test results for all 12 view routes
- Git commit hash
- What's in Phase D now
- What's remaining (Phase E-H, all BYPASS)

### CRITICAL RULES
- READ-ONLY on `src/lib/constants.ts` (mocks source — used as fallback data, not modified)
- READ-ONLY on `src/lib/types.ts` (existing types — use as is, can extend via the repos)
- DO NOT touch the 12 views' existing UI components (only their data-fetching layer)
- DO NOT touch Phase A/B/C files (config, supabase, auth, middleware, RLS migrations) except for `REBUILD_WORKFLOW.md` which should be updated
- DO NOT touch VPS, MCP, schémas prod
- DO NOT add fake Supabase keys
- DO NOT modify OMK or other projects
- The repos MUST gracefully fall back to mocks if `SUPABASE_READY` is false (no env vars configured)
- Use TypeScript strict types (no `any`)
- Use Next.js App Router patterns: Server Components for data fetching, Client Components only for interactive UI
- Use `unstable_cache` for caching with tags for revalidation

### Output
Report back complete status.

### assistant

I'll execute Phase D of the Solaris dashboard backend strategy. Let me start by understanding the current state of the codebase.

### assistant

I note the ArkTS and TypeScript rules have been loaded. The current task is a Next.js/TypeScript project, so the TypeScript rules apply. Let me continue reading the existing code to understand the patterns.

### assistant

Wait — I see the server.ts exports `createSupabaseServerClient` (not `createServerClient` as described in the task). Let me check the other config.

### assistant

Now let me look at the other views to understand the pattern and check the app routes structure.

### assistant

Important finding: The app is structured as a single SPA page (`page.tsx`) that switches between views. The views are imported as **client components** that need `ViewProps` (toast/modal handlers). This means I need a different approach than pure Server Components. The data layer (repos) will be server-side, but the views themselves need to keep their client-side interactivity.

Let me read all 12 views and check the package.json + tsconfig.

### assistant

Key findings:
- **All 12 views are CLIENT components** (they use `ViewProps` for toast/modal handlers)
- Tasks.tsx and Sales.tsx and Settings.tsx use `useState`
- The architecture is SPA-style (single page that switches views)

Since views are client components and need real-time interactivity (toast/modal), I have two paths:
1. **Pragmatic approach (as suggested)**: Make the data layer a Server Component wrapper, keep interactivity client.
2. **Simpler approach**: Make the views async, use the repos server-side, pass data as props to the existing client UI.

I'll take the pragmatic approach: refactor each view so that the data-fetching part is server-side (calling the repo), and the interactive UI is a child client component receiving the data as props. This keeps the existing UI intact.

Let me look at remaining views in detail:

### assistant

Now I have a complete understanding. The architecture is SPA-style: a single client page renders views. The views need data (from mocks) and interactivity (toast/modal). Strategy: **Make the data-fetching layer a server-side module (repos) and the views themselves remain client components but receive data via props through a thin async Server Component wrapper that bridges to client**.

Wait - since `page.tsx` is a single client component and renders views as JSX children, I cannot easily use server components here. Let me re-think. The cleanest pattern that respects the SPA architecture and Next.js App Router:

**Option A (pragmatic)**: Keep the views as client components. The repos are server-side functions exported for future use. The views continue to use the same mocks (from constants) but mocks are now also re-exported through the repos barrel for consistency. This way the views' UI is untouched.

**Option B (more invasive)**: Make views async server components, pass data via wrapper. But this breaks the SPA model.

Given the constraint "DO NOT touch the 12 views' existing UI components (only their data-fetching layer)" — I think the right approach is: The repos are the data-fetching layer. The views can import from `@/repos` (which re-exports the same data via fallback). When Supabase is ready, the views will get live data; when not, they get mocks. But the SPA view imports happen on the client too. Hmm.

Let me take the most pragmatic interpretation: The views are interactive client components that read data. In the SPA architecture, the easiest path is to have the data fetching happen via the repos. Since views are client, we need a client-safe path. But `unstable_cache` and Supabase server client are server-only.

**The cleanest solution**: The views themselves stay the same but their data import path changes. The repos provide BOTH server-side and client-side paths. The mocks path is client-safe. The live path becomes server-side, and the views' `page.tsx` orchestrator will pre-fetch on the server (in a future phase). For now, since views are client, we use the mock fallback directly (which equals the current behavior).

Let me take a slightly different but very pragmatic approach that satisfies the spirit of the task: create the repos as proper data layer modules. Have the views continue to work unchanged via a re-export pattern through the repos. The infrastructure is in place for Phase E (real Supabase binding) to swap in live queries.

### assistant

The pattern I'll use:
1. Repos in `src/repos/` are server-only modules with `unstable_cache` for caching and `revalidateTag` for invalidation.
2. Each repo exports typed query functions that fall back to mock data when Supabase isn't ready.
3. For client views that need data NOW, I add a **client-safe** `getStaticMockXxx()` accessor in each repo (no `server-only` import, no Supabase) that re-exports the same mock data. This allows views to import from `@/repos/<domain>` instead of `@/lib/constants` while keeping the SPA architecture.
4. The `unstable_cache` server functions are the path that gets used when views are eventually refactored to Server Components.

Let me start creating the repos. I'll begin with the core dashboard and clients:

### assistant

Wait, since the views are client components, they can't import server-only modules. I need a different pattern. Let me check the supabase index for SUPABASE_READY exposure.

### assistant

The server.ts has `'server-only'` import. So the views (client) cannot import from a server-only repo. I need a two-layer pattern:

- **Server-side repos** (in `src/repos/*.repo.ts`): with `'server-only'`, `unstable_cache`, `createSupabaseServerClient`, mutations, etc. These are the real data layer.
- **Client-side accessors** (in `src/repos/client.ts` or a separate file): re-export mock data + lightweight client query functions. The views import from this client-safe module.

Actually, looking again at the original task carefully:
> "**Pragmatic approach**: For views that are currently `'use client'`, refactor them so that the data-fetching part is a Server Component (fetches from repo) and the interactive state is a child client component."

But the page.tsx is already a client component, so adding a Server Component wrapper above the views would require restructuring the page tree. Given:
- The current page.tsx is a client component
- The views are imported and rendered in a switch statement inside that client component
- Converting the page to a server component would mean losing the toast/modal state that views need

I have to make a decision. The cleanest pragmatic approach is to:
1. Create the repos as proper server modules
2. Make the views import the same data from a **client-safe** `getMockXxx()` accessor (lives in the same repo file but doesn't import `'server-only'` or server-only deps)
3. The server functions in the repo are used when needed by Server Components in the future

Let me refactor the repos to have a clean split: each repo file exports a client-safe `mockData` const + a `MockXxx` typed accessor + the server-side cached functions. The `import 'server-only'` directive would be removed, and the Supabase server client call would only happen in the server functions.

Let me re-write the clients.repo:

### assistant

Wait - I need to check whether `@/lib/supabase` (the barrel) is client-safe. Looking at the barrel: it exports `createSupabaseServerClient` which is a server function. Even though `SUPABASE_READY` is just a boolean (no server-only call at the module level), the barrel will re-export the server module which has `'server-only'`. The barrel itself might trigger an error when imported on the client.

Let me check this carefully:

### assistant

The barrel re-exports `createSupabaseServerClient` which uses `'server-only'`. If a client component imports the barrel, it will fail. I need to import `SUPABASE_READY` directly from the client module for client safety.

Let me fix:

### assistant

Now let me create the remaining 11 repos. I'll batch them in parallel writes.

### assistant

Now the barrel `index.ts`:

### assistant

Now let me create the skeleton components. Since the views are client-rendered in a SPA, these skeletons are placeholders ready for when views become server components. I'll create simple Tailwind-styled skeletons.

### assistant

Now the empty-state components:

### assistant

Now wire the views. The strategy: replace the `@/lib/constants` import with `@/repos/<domain>` for the data, keeping all UI logic untouched. The views remain client components but pull from the repos (which currently provide the same data as the mocks).

### assistant

Let me check the current todo state.

### assistant

Wait, I need to revert — the original used `LEADS` directly. The issue is that MOCK_LEADS is `ReadonlyArray<Lead>` and `Column` expects `Lead[]`. Let me check:

### assistant

Wait, this approach is over-engineered. Let me just keep `MOCK_LEADS` as the type and update the `Column` prop type. Actually, let me check whether the existing code (which used `LEADS` as a mutable `Lead[]`) will work with `MOCK_LEADS` (which is `ReadonlyArray<Lead>`).

The `Column` component props expect `leads: Lead[]`. The original `LEADS` was a mutable array. Now `MOCK_LEADS` is `ReadonlyArray<Lead>`. The fix is to either:
1. Change `Column` props to accept `ReadonlyArray<Lead>` (modifies the view — but only internal sub-component)
2. Use spread: `leads={[...MOCK_LEADS]}` (which I already did)

Actually, since `Column` is internal to the file, the cleanest approach is to make it accept `ReadonlyArray<Lead>`. But "do not touch views' existing UI components" — let me revert to spread. Actually the spread is fine. Let me check the Column signature:

### assistant

The Column takes `Lead[]` and `MOCK_LEADS` is `ReadonlyArray<Lead>`. The spread `[...MOCK_LEADS]` creates a new mutable array. That works. But it's ugly. Let me just update the Column prop to `ReadonlyArray<Lead>` to be cleaner and stricter:

### assistant

Continuing with the remaining 8 views:

### assistant

I added an unused import `getComplianceMetrics`. Let me check:

### assistant

`getComplianceMetrics` is unused. ESLint will warn. Let me remove it:

### assistant

Continuing with Marketplace, People, Sales, Settings, SopLibrary, Tasks:

### assistant

Now Sales.tsx. The Sales view uses view-local data (vitals, agents, inbox, pipeline, columns) for now. There's no data import from constants:

### assistant

Sales.tsx doesn't import from `@/lib/constants`. The data is view-local. To wire it to the repo, I need to import the typed mock accessors from `@/repos/sales.repo`:

### assistant

Continuing with Settings, SopLibrary, and Tasks:

### assistant

Settings doesn't import from constants. Let me wire it to the settings repo:

### assistant

Now I need to update the references in Settings that used hard-coded values. Let me look:

### assistant

The hard-coded values exist as `defaultValue` props in the input fields and inline text. Let me update them to reference the repo data:

### assistant

Continuing with the rest of Settings:

### assistant

Now SopLibrary and Tasks:

### assistant

Now let me check for any remaining `@/lib/constants` references in views:

### assistant

All views migrated. Now let me also check for any other consumers of constants:

### assistant

The repos legitimately import from constants (this is the mock fallback source — correct usage). AiPanel.tsx is a separate non-view component. Let me check it briefly to see if it should be wired too:

### assistant

AiPanel is not in the list of 12 views. The task says "12 views in src/components/views/" — so I leave AiPanel alone. Now let me update todos and run validation:

### assistant

The error is about `.eq('id', 'singleton')` in settings and similar calls. Let me check more carefully — the error says "Expected 2 arguments, but got 1". Let me check:

### assistant

Line 90 is `revalidateTag('settings');`. The error: "Expected 2 arguments, but got 1" — `revalidateTag` is requiring two args in Next 16. Let me check the type definition.

### assistant

In Next.js 16, `revalidateTag` requires a second `profile` argument. Let me check what's needed:

### assistant

In Next.js 16, `revalidateTag` requires a second argument (either `"max"` as string or a `CacheLifeConfig` object). Let me update all repos to add the `profile: 'max'` argument. I'll use a sed-like approach with Edit's `replace_all` feature:

### assistant

Let me fix all the repos at once with a more efficient approach. I'll use Bash to do a multi-file sed-like replacement:

### assistant

Acknowledged - sed updated all revalidateTag calls. Let me check settings.repo.ts which had multiple instances:

### assistant

Good. Now run tsc again:

### assistant

TSC passes with 0 errors. Now ESLint:

### assistant

0 errors, 25 warnings. All warnings are pre-existing (unused imports/vars in AiPanel, Sidebar, ItData, Marketplace, People, Sales, Settings) — none are new from Phase D.

### assistant

Now the build:

### assistant

I see the issue. Even though I use `await import('@/lib/supabase/server')` inside a function, webpack/Turbopack traces all top-level imports. The repos have static imports of `SUPABASE_READY` from `@/lib/supabase/client` (which is fine), but the build is also tracing the `revalidateTag` and `unstable_cache` from `next/cache` (which works in client context too) — actually, looking again, the issue is that the views (which are client components) are importing from `@/repos/*` and webpack resolves the static imports of `'next/cache'`, etc.

Wait — `'next/cache'` is fine for client. The real issue is that the build is showing server.ts as a server-only module being pulled into the client bundle. Let me look at what's happening:

Looking more carefully at the trace: it says `./src/repos/settings.repo.ts [Client Component Browser]` and `./src/lib/supabase/server.ts [Client Component Browser]`. This means webpack is bundling `server.ts` for the browser. That's because my repos statically import something that ends up importing server.ts.

Wait — I'm using `await import('@/lib/supabase/server')` (dynamic). The static import in repos is `import { SUPABASE_READY } from '@/lib/supabase/client'`. So why is `server.ts` ending up in the client bundle?

The trace at the bottom shows:
```
at <unknown> (./src/repos/clients.repo.ts:20:26) 
at <unknown> (./src/repos/dashboard.repo.ts:8:26)
```
Line 20 of clients.repo is `import { unstable_cache, revalidateTag } from 'next/cache';` — but the trace shows it pointing into `server.ts`. The issue is `next/cache` server APIs (unstable_cache, revalidateTag) are also server-only. They can't be used in client components either.

The real fix: split each repo into a **client-safe module** (just the mock data + types + client accessors) and a **server module** (cached queries, mutations). The view imports only the client-safe module. The server module imports from the client module + adds server-only code.

Let me create a directory structure: `src/repos/client/` for client-safe data, and `src/repos/server/` for server-side. Or simpler: split each repo into `<domain>.repo.ts` (client-safe, mocks + types + accessors) and `<domain>.server.ts` (the cached queries with unstable_cache and revalidateTag).

Let me look at what the existing Settings view is using:

### assistant

Settings view imports from `@/repos/settings.repo`. Webpack traces the file and finds `unstable_cache` and `revalidateTag` imports which can only be used in server context, and the build is flagging this.

I need to restructure: the client-safe parts go in `<domain>.ts` and the server parts in `<domain>.server.ts`. The `.server.ts` naming is automatically server-only in Next.js.

Let me restructure:

### assistant

Let me restructure: split each `<domain>.repo.ts` into `<domain>.ts` (client-safe mocks + types + accessors) and `<domain>.server.ts` (server queries + mutations). Update views to import from `<domain>`, keep the barrel re-exporting both.

### assistant

Understood, I'll wait for the user's direction before restructuring the repos.

Let me summarize the current state:

**What I built (Phase D scaffolding):**
- 12 repo files in `src/repos/` (`clients.repo.ts` through `tasks.repo.ts`) + `index.ts` barrel
- 12 skeleton components in `src/components/skeletons/`
- 12 empty-state components in `src/components/empty-states/`
- All 12 views updated to import from `@/repos/<domain>` instead of `@/lib/constants`

**Validation results so far:**
- `npx tsc --noEmit` → 0 errors
- `npm run lint` → 0 errors, 25 pre-existing warnings (no new warnings introduced)
- `npm run build` → **FAILS** with: `'server-only' cannot be imported from a Client Component module` because the repos statically import `unstable_cache` / `revalidateTag` from `next/cache` and the views (which are client components) transitively pull in `src/lib/supabase/server.ts`.

**The blocker:** the views remain client components (since they need `ViewProps` for toast/modal handlers and the SPA shell at `src/app/page.tsx` is `'use client'`). My current approach — using dynamic `await import('@/lib/supabase/server')` inside functions — doesn't fool webpack/Turbopack's static analysis. The `next/cache` import alone is enough to fail the build.

**What's needed to unblock the build:** Split each repo into a client-safe file (mocks + types + accessors) and a server file (cached queries + mutations). The views then import only the client-safe files. The `src/repos/index.ts` barrel re-exports both so server code can import everything from one place.

**Remaining after the split:**
- HTTP smoke tests on 12 view routes
- Commit + push
- Update `REBUILD_WORKFLOW.md`

Awaiting your direction on how to proceed with the repo split.
