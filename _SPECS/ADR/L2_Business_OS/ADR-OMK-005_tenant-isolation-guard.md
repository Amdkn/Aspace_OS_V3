---
adr_id: ADR-OMK-005
title: OMK Dashboard — Tenant Isolation Guard (client + Edge Function)
status: RATIFIED
date: 2026-06-20
deciders: A0_Amadeus
consulted: A2 (Claude Code)
informed: A3 (Symphony A3 twins)
supersedes: null
amends: ADR-OMK-001 §runtime, ADR-OMK-002 §workflow
related: ADR-OMK-004 (Cloud pivot), ADR-SUPABASE-001 (multi-tenant doctrine)
---

# ADR-OMK-005 — Tenant Isolation Guard

## Context

The OMK Tax Service dashboard is multi-tenant (ADR-OMK-001): every authenticated user belongs to one or more `omk_saas.organizations` via `omk_saas.memberships`, and the JWT custom_access_token hook (`public.custom_access_token_hook`) injects the `org_id` claim on every JWT issuance (Phase A migration).

Server-side isolation is enforced by RLS policies on every `omk_saas.*` table (5 business tables + 2 new in Phase D):
```sql
CREATE POLICY tenant_isolation_select ON omk_saas.clients
  FOR SELECT TO authenticated
  USING (org_id = (SELECT current_org_id()));
```

This works ONLY if:
1. The JWT hook is wired in Supabase Auth dashboard (D6 #64 — A0 action).
2. The hook reads the user's memberships and injects `org_id` claim.
3. The client makes queries with the user's JWT (anon key alone returns 0 rows).

Before this ADR, the client was vulnerable to two classes of bug:
- **Stale org_id cache** — `useOrg()` returned a previous user's orgId after sign-out, leaking data on next sign-in.
- **Writes without org_id** — `supabase.from('clients').insert({ name: 'X' })` succeeded without an explicit `org_id`, inserting a row with `org_id = NULL` which then silently failed RLS (no error returned, but data persisted in the wrong state).

## Decision

Implement a **defense-in-depth tenant guard** at the application layer with 4 components:

### 1. `src/lib/tenant.ts` — `useOrg()` React hook

```typescript
export function useOrg(): TenantContext {
  // reads AuthContext (user.orgId, user.role, organization.name)
  // computes isMissing = IS_SAAS && isReady && orgId === null
  // warns in dev mode if isMissing
}
```

Consumer-facing hook. Returns `{ orgId, orgName, role, isAuthenticated, isReady, isMissing }`.

### 2. `src/lib/tenant.ts` — non-React accessor + cache

```typescript
let _activeOrgIdCache: string | null = null;
export function setActiveOrgIdCache(orgId: string | null): void { _activeOrgIdCache = orgId; }
export function getActiveOrgId(): string | null { return _activeOrgIdCache; }
```

Used by the `repository.ts` `makeRepository<T>()` function which is called from non-React code paths (event handlers, async data loaders). The `AuthProvider` calls `setActiveOrgIdCache` on every auth state change AND on `signOut()` to prevent stale-state leaks.

### 3. `assertOrgIdForWrite()` — TypeScript assertion function

```typescript
export function assertOrgIdForWrite(orgId: string | null, table: string): asserts orgId is string {
  if (IS_SAAS && !orgId) {
    throw new Error(`[${table}] Cannot write in saas mode without an active orgId.`);
  }
}
```

Called by `repository.ts` on every `create()` / `update()` / `remove()`. In saas mode, throws if no orgId. Fails loud at the call site (better than silent RLS rejection).

### 4. `src/components/ProtectedRoute.tsx` — auth gate

Wraps the entire `ShellLayout`. Reads `useAuth()` + `useOrg()`. If `!user` → `<Navigate to="/login" state={{ from }} replace>`. If `IS_SAAS && isMissing(orgId)` → render children with a console.warn (avoids infinite spinner during the D6 #64 hook wiring window).

## Consequences

### Positive
- **No silent data leaks** — `signOut()` clears the cache, next sign-in starts fresh.
- **No silent RLS denials** — `assertOrgIdForWrite` throws at the call site, not at the network.
- **Faster debugging** — `useOrg().isMissing = true` is a single boolean A0 can check in the console.
- **Tenant guard survives cross-tab race conditions** — the `setActiveOrgIdCache` global is module-scope, so a signOut in tab 1 invalidates reads in tab 2 on the next request.

### Negative
- **3 places to update for tenant-related changes** — `AuthProvider`, `useOrg`, and the cache. Mitigated by the `useAuth` hook being the single source of truth.
- **TypeScript assertion function `asserts orgId is string`** can be misused (caller ignores the throw). Mitigated by linting + the type system narrowing the variable for subsequent code.
- **Cache invalidation is manual** — relies on `AuthProvider` calling `setActiveOrgIdCache` on every relevant state change. A future bug where a state change forgets to update the cache would re-introduce the stale-state issue.

### Risks
- **Risk**: New repos forget to call `assertOrgIdForWrite`. **Mitigation**: `makeRepository<T>` does it automatically; repos that bypass `makeRepository` are not allowed.
- **Risk**: `signIn` does not refresh the orgId cache. **Mitigation**: `hydrate()` in AuthProvider sets the cache after every auth state change (including sign-in).
- **Risk**: JWT custom_access_token hook is unconfigured (D6 #64) → `useOrg().orgId = null` for all users → SaaS is unusable. **Mitigation**: `useOrg().isMissing` warning banner visible in every view; A0 cannot miss it.

## Alternatives Considered

1. **Pure server-side RLS, no client guard.** Rejected: silent RLS denials are hard to debug; client should fail loud when orgId is missing.
2. **Per-view `org_id` injection via repository.ts only.** Rejected: doesn't help debugging — you'd see "0 rows returned" with no explanation. The `isMissing` flag is the diagnostic.
3. **Use Supabase `setSession()` + auto-refresh on every query.** Rejected: too expensive (network round-trip per query).

## References

- **Implementation**: `src/lib/tenant.ts` (90 lines), `src/components/ProtectedRoute.tsx` (60 lines), `src/auth/AuthProvider.tsx` lines 73-82 (cache sync), `src/data/repository.ts` lines 91-99 (`assertOrgIdForWrite`).
- **D6 lessons**: D6 #64-#67 (Phase C), D6 #75-#76 (Phase E).
- **Related docs**: `docs/runbooks/2026-06-20-phase-c-receipt.md`, `docs/runbooks/2026-06-20-phase-e-receipt.md`.

## History

- **2026-06-20** — RATIFIED. Implemented across Phase A → C → E → F.
- **2026-06-20** — Edge Function `sign-up-organization` (Phase F) uses service_role to atomically create org + membership, ensuring the JWT hook has data to inject on next refresh.
