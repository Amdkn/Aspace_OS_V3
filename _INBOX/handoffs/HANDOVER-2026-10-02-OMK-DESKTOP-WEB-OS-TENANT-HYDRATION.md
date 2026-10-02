# Handoff: Tenant Hydration from Supabase Memberships (Issue #289)

**Target Repository**: `omk-services/OMK-DESKTOP-WEB-OS`
**Blocker Type**: `MissingWriteAccess`

## Summary
The goal of Issue #289 was to hydrate the active tenant from authenticated Supabase memberships, replacing the hardcoded `demo-coach` defaults, and purging the CMS cache on tenant switch.
The implementation was successfully completed, tested, and typechecked locally in a clone of `omk-services/OMK-DESKTOP-WEB-OS`. However, due to lack of write permissions to push branches or create PRs directly on `omk-services/OMK-DESKTOP-WEB-OS`, the patch file containing the fix is provided.

## Actions Taken
1.  **Updated `src/stores/tenant.store.ts`**:
    *   Replaced static imports with dynamic imports for `supabase`, `backend.supabase`, and `memberships` inside `bootstrap()` and `switchTenant()` to resolve a circular dependency between `tenant.store.ts` and `cms.store.ts`.
    *   In `bootstrap()`, fetched the current user's session.
    *   Fetched the user's active memberships using `listerTenantsPourUser`.
    *   Hydrated `knownTenants` with `org_id` mapped to `TenantId`.
    *   Deterministically chose the `activeTenantId` based on persisted values or fallback.
    *   In `switchTenant(next)`, added a dynamic import of `useCmsStore` to call `purge(previousTenantId)` before the switch.
2.  **Updated `src/lib/auth/memberships.ts`**:
    *   Modified `listerTenantsPourUser` to query `supabase` for the user's active memberships, as the `InMemoryBackend` method was insufficient for Supabase.
3.  **Tests**:
    *   Ran `npm run typecheck`, `npm run typecheck:api`, and `npm test` successfully.
    *   Ran `npm run build` which passed.

## Artifacts
The commit patch is available in the root of the ASpace OS V3 repository as `0001-BUSINESS-OS-OPERATIONS-P0-Hydrate-active-tenant-from.patch`.

## Next Steps for Human Operator
Apply the patch to `omk-services/OMK-DESKTOP-WEB-OS` and push the branch.
