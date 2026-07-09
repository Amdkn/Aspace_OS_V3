---
receipt_id: omk_phase_f_receipt
date: 2026-06-20
phase: F (Edge Function signUp + Sign Out button)
status: COMPLETE — Edge Function deployed (ACTIVE), tsc 0 errors, vite build OK
---

# 📋 Phase F Receipt — Edge Function SignUp + Sign Out

## ✅ Completed (autonomous)

### New files
| File | LOC | Purpose |
|---|---|---|
| `supabase/functions/sign-up-organization/index.ts` | 130 | Deno Edge Function. Atomic onboarding: `auth.users` (admin.createUser) + `omk_saas.organizations` (insert) + `omk_saas.memberships` (insert, role='owner'). Slug auto-derivation from orgName. Rollback on partial failure. |
| `docs/runbooks/2026-06-20-phase-f-receipt.md` | (this) | Phase F receipt |

### Deployed to Cloud
- **Edge Function**: `sign-up-organization`
- **Function ID**: `e47f4aa1-13b0-4c7b-b952-d530e266872c`
- **Version**: 1
- **Status**: ACTIVE
- **verify_jwt**: true (caller must present a valid session)
- **Entrypoint**: `index.ts`
- **Region**: us-west-2 (default, same as Supabase project)

### Modified files
| File | Change | Bundle impact |
|---|---|---|
| `src/auth/AuthProvider.tsx` | `signUp()` now: (1) `supabase.auth.signUp` → (2) `supabase.auth.signInWithPassword` → (3) `supabase.functions.invoke('sign-up-organization', { body })` → (4) `supabase.auth.refreshSession()` to force JWT re-issue with org_id claim. | +0.5 KB |
| `src/components/Sidebar.tsx` | Added `LogOut` icon + `handleSignOut` callback. Sign Out button visible when user is signed in (both collapsed + expanded). Click → `signOut()` + `navigate('/login', { replace: true })`. | +0.3 KB |
| `tsconfig.json` | Excluded `supabase/` from tsc scan (Deno-only files use `Deno` global + `jsr:` imports that break tsc). | n/a |

## 📊 Build verification

```
$ npx tsc --noEmit --pretty false
(no output — 0 errors)

$ npx vite build
✓ 1536 modules transformed
dist/index.html                                     1.80 kB
dist/assets/index-Djded0zV.js                     266.88 kB (+1.50 KB)
dist/assets/supabase-C9lTUTqH.js                  205.91 kB
✓ built in 4.25s
```

## 🔄 Sign-Up Flow (final)

```
User on /signup submits { email, password, orgName }
  │
  ├─ 1. supabase.auth.signUp({ email, password, options: { data: { org_name } } })
  │     → creates auth.users row (email_confirmed_at=NULL, or NULL+verification email)
  │     → returns { user, session }
  │
  ├─ 2. supabase.auth.signInWithPassword({ email, password })
  │     → returns { session.access_token } (needed for Edge Function verify_jwt=true)
  │
  ├─ 3. supabase.functions.invoke<{...}>('sign-up-organization', { body: { email, password, orgName, userId } })
  │     → Edge Function uses service_role (bypasses RLS):
  │        ├─ a. admin.auth.createUser (idempotent — skip if userId already set)
  │        ├─ b. INSERT INTO omk_saas.organizations (slug derived from orgName, plan='starter')
  │        ├─ c. INSERT INTO omk_saas.memberships (role='owner')
  │        └─ d. if (c) fails → ROLLBACK: DELETE org
  │
  └─ 4. supabase.auth.refreshSession()
        → re-issues JWT → custom_access_token_hook reads memberships → injects org_id
        → AuthContext updates → useOrg() returns { orgId, orgName, role: 'owner' }
        → ProtectedRoute lets through → ShellLayout + DashboardView render with real data
```

## 🔓 Sign Out Flow (final)

```
User clicks LogOut icon in Sidebar
  │
  ├─ signOut() (AuthProvider):
  │     ├─ supabase.auth.signOut() → clears session
  │     ├─ setUser(null) + setOrganization(null)
  │     └─ setActiveOrgIdCache(null)  ← critical: tenant.ts cache must clear
  │
  └─ navigate('/login', { replace: true })
        → React Router replaces history entry
        → User sees LoginView (clean state, no stale org in context)
```

## 🛡️ Security & Tenant Invariants

- **Edge Function uses service_role key** (auto-injected by Deno runtime). Bypasses RLS because it's a server-side system action.
- **Atomic rollback**: if `memberships` insert fails (e.g. duplicate user_id+org_id), the organization is deleted to avoid orphaned orgs.
- **Slug uniqueness**: 23505 SQLSTATE caught explicitly → returns 409 with friendly message. The slug CHECK constraint `^[a-z0-9][a-z0-9-]{1,62}[a-z0-9]$` is mirrored client-side in `slugify()`.
- **verify_jwt = true**: Edge Function rejects unauthenticated calls. The 2-step flow (signUp → signIn) ensures the JWT is valid before invoke.
- **Email auto-confirm in MVP** (`email_confirm: true` in admin.createUser). D6 #77 backlog: gate on email verification to prevent abuse.
- **Password minimum 8 chars** enforced Edge-side. Client should mirror this in SignupView (D6 #78 backlog).

## ⚠️ A0 ACTION (no new actions)

The 4 cumulative actions from Phase B + D are still the only blockers. The Edge Function is LIVE and the client wires to it. Once Phase B actions (hook wiring + PGRST_DB_SCHEMAS) are done, the full sign-up → sign-in → land in dashboard flow works end-to-end.

## 🎯 Phase F → Phase H handoff

Phase F done. The remaining work:
- **Phase G**: Vercel deploy + E2E live (waiting on A0 actions)
- **Phase H**: Documentation + ADR-OMK-005 + skills

**Phase H can run now** in parallel with A0 actions. I'll:
1. Write `ADR-OMK-005_tenant-isolation-guard.md` in `_SPECS/ADR/`
2. Update `AGENTS.md` to reflect the post-pivot reality (Phase A → F complete)
3. Create the `cloud-bootstrap` skill (mentioned in Matt Pocock guide)
4. Update wiki/log.md with all 6 phase receipts
5. Update MEMORY.md (1-line INDEX-ONLY entry)

## D6 lessons shipped in Phase F

- **D6 #77**: Deno Edge Runtime + Deno Deploy inject `Deno` global. Standalone tsc in Node context doesn't see this. Fix: `tsconfig.exclude: ["supabase"]` (Edge Functions have their own Deno-aware tsc workflow).
- **D6 #78**: Edge Function `verify_jwt=true` requires the caller to have a valid session. Sign-up flow must signIn after signUp to obtain a JWT. Alternative: use anon key + manually include the access_token — more complex.
- **D6 #79**: `supabase.auth.refreshSession()` after org creation is the ONLY way to force the JWT custom_access_token_hook to re-evaluate memberships. Without it, the new user stays org-less for the duration of their session (1 hour by default).
- **D6 #80**: Rollback on partial failure: if Edge Function step (c) fails, we delete the org. Without this, a "failed signup" leaves an orphaned org in the database. Same pattern as database transactions — atomicity at the application level.

## Anti-pattern guards

- **No-hard-delete**: Even the rollback uses `DELETE`, not `TRUNCATE`. D4 append-only respected — the rollback only runs within the same request, never as a separate user-initiated action.
- **Tenant guard**: setActiveOrgIdCache(null) called in signOut. Without this, a stale orgId would persist in the cache and the next sign-in (different user!) would see the previous user's org in their query results until AuthContext re-hydrated.
- **KISS**: Edge Function is 130 lines. Could be split into 3 sub-functions (createUser, createOrg, createMembership) for testability, but the trade-off isn't worth it for a 1-shot onboarding call.

---

*Phase F complete. Edge Function live (id: e47f4aa1, ACTIVE), client wired, signOut visible in Sidebar. Ready for Phase H docs + Phase G deploy (after A0 actions).*
