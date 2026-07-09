---
receipt_id: omk_phase_c_receipt
date: 2026-06-20
phase: C (Repository layer upgrade + Tenant isolation guard)
status: COMPLETE — all green (tsc 0 errors, vite build OK)
---

# 📋 Phase C Receipt — Repository + Tenant Guard

## ✅ Completed (autonomous)

| # | File | Change | Lines |
|---|---|---|---|
| C.3 | `src/lib/supabase.ts` | Removed hardcoded `'public'` schema; now uses `DB_SCHEMA` (= `omk_saas`). Added `fromSchema()` helper. | ~50 |
| C.3 | `src/data/repository.ts` | Added Mapper<T> (toDb/fromDb), Mapper<T> injectable via options, tenant guard via `getActiveOrgId()`, `assertOrgIdForWrite()` on create/update/remove, localStorage fallback also filters by org_id, `create()` auto-injects org_id + auto-gen UUID via `crypto.randomUUID()` | 184 (was 105) |
| C.4 | `src/lib/tenant.ts` (NEW) | `useOrg()` React hook + `getActiveOrgId()` non-React accessor + `setActiveOrgIdCache()` for AuthProvider sync + `assertOrgIdForWrite()` helper. Warns in dev if saas + no org_id. | 92 |
| C.4 | `src/auth/AuthProvider.tsx` | Calls `setActiveOrgIdCache()` on hydrate AND on signOut. | +3 |
| C.5-C.6 | `src/data/*.repo.ts` | All 7 repos (clients, documents, agents, sops, invoices, tasks, team) use the same `makeRepository<T>(table, seed)` API — no changes needed because the table name is unchanged from `public.*` to `omk_saas.*` (Supabase client uses `db.schema` from constructor). | 0 |
| C.7 | `npx tsc --noEmit` | **0 errors** | 0 |

## 📊 What changed (high-level)

### Before (drift)
```typescript
// supabase.ts (BROKEN — D6 #50 / D6 #64)
const effectiveSchema: string = (DB_SCHEMA as unknown) === 'public' ? (DB_SCHEMA as string) : 'public';
// result: ALWAYS 'public' regardless of APP_MODE

// repository.ts (no tenant guard)
async list() {
  return supabase.from(table).select('*');  // returns ALL rows in all orgs (if RLS not on)
}
async create(item) {
  return supabase.from(table).insert(item);  // NO org_id injected — RLS would deny
}
```

### After (Phase C)
```typescript
// supabase.ts — schema is the active APP_MODE schema
const effectiveSchema: string = DB_SCHEMA as string;  // 'omk_saas' in saas mode

// repository.ts — tenant-aware
async list() {
  return supabase.from(table).select('*');  // RLS filters by org_id from JWT
}
async create(item) {
  const orgId = getActiveOrgId();
  assertOrgIdForWrite(orgId, table);  // fail loud if no orgId in saas mode
  const dbRow = { ...item, org_id: orgId };  // auto-inject
  return supabase.from(table).insert(dbRow).select().single();
}
```

## 🔐 Multi-tenant defense in depth (4 layers)

1. **Postgres RLS** (server-side, authoritative) — `omk_saas.*` policies filter by `org_id = current_org_id()` from JWT claim.
2. **JWT custom_access_token_hook** (server-side) — injects `org_id` claim from `memberships` table on every JWT issuance.
3. **Repository layer** (client-side, this phase) — `getActiveOrgId()` + `assertOrgIdForWrite()` prevents writes without active org context.
4. **localStorage fallback** (dev-only) — filters in-memory by `org_id` field.

## ⚠️ A0 ACTION (still blocking E2E)

The repository upgrade is **complete and type-safe** BUT requires the **JWT custom_access_token_hook** to be wired in the Supabase Auth dashboard (see `2026-06-20-phase-b-auth-hook-wiring.md`). Without it:
- All `clientsRepo.list()` calls return 0 rows (RLS denies)
- The UI shows empty states
- The `useOrg().isMissing` flag fires true and `assertOrgIdForWrite()` throws on writes

## 🎯 Phase C → Phase D handoff

**Phase D**: bulk-generate the 13 sub-pages (1 sprint). All views already compile and exist as skeletons/empty states. Phase D adds:
- Real Supabase queries (replace localStorage fallbacks)
- Loading/error/empty state components
- Form components (create/update modals)
- Per-tenant data binding (org_id from useOrg)

**Recommendation**: proceed Phase D in autonomy. The compile + tsc + vite-build are already green. The 13 sub-pages will use the upgraded repository layer, so when A0 wires the hook, the live queries will work automatically.

## D6 lessons shipped in Phase C

- **D6 #64**: PostgREST `PGRST_DB_SCHEMAS` env var is read-once at boot, NOTIFY does not reload. The previous hardcoded `'public'` schema in `supabase.ts` was a workaround for this. Now that the A0 action in Phase B is documented, we switch to `DB_SCHEMA` (which is `omk_saas` in saas mode) but the actual exposure still requires the Dashboard UI step (`Settings > API > Exposed schemas: add 'omk_saas'`).
- **D6 #65**: `createClient({ db: { schema: 'omk_saas' } })` only works if the schema is in `PGRST_DB_SCHEMAS`. Otherwise, the call succeeds but `.from('clients')` returns 404. This is the silent failure risk.
- **D6 #66**: `Omit<T, 'id'> & { id?: string }` for `create()` is a strict pattern that catches missing `id` at compile time. Migrated from `T` (where `id` was required even though Postgres auto-generates).
- **D6 #67**: `assertOrgIdForWrite` is a TypeScript assertion function (`asserts orgId is string`). It both throws AND narrows the type for the rest of the function, so the caller cannot accidentally pass `null` to `.insert({ org_id: null })`.

## Build verification

```
$ npx tsc --noEmit --pretty false
(no output — 0 errors)

$ npx vite build
✓ 1531 modules transformed.
dist/index.html                                     1.80 kB
dist/assets/index-BNXK7fmX.css                     40.58 kB
dist/assets/index-QTahCSxX.js                     255.84 kB
dist/assets/supabase-C9lTUTqH.js                  205.91 kB
✓ built in 4.21s
```

All 14 views compile (DashboardView, FinanceView, PeopleView, ClientsView, ClientDetailView, DocumentsView, SOPLibraryView, TasksView, AgentsView, GrowthView, SalesView, MarketplaceView, LegalView, ItDataView, SettingsView). Ready for Phase D content.

---

*Phase C complete. Status: 100% autonomous (no A0 action required for compile). Live E2E still requires Phase B hook wiring (D6 #64).*
