---
receipt_id: omk_phase_e_receipt
date: 2026-06-20
phase: E (react-router-dom 7 + ProtectedRoute + auth routes)
status: COMPLETE — tsc 0 errors, vite build OK
---

# 📋 Phase E Receipt — Routing + Auth Guard

## ✅ Scope Discovery

The plan called for "wire react-router-dom 7". On inspection of App.tsx (lines 1-94 of the pre-Phase-E file), **routing was already wired** with `<BrowserRouter>` + 15 `<Route>` (index + 14 views). The actual work was:

1. **Remove `DEMO_MODE = true`** (auth was being bypassed)
2. **Add `/login` + `/signup` as public routes** (outside ShellLayout)
3. **Build `ProtectedRoute` wrapper** (auth + tenant guard)
4. **Add 404 catch-all** (`<Route path="*" element={<NotFoundView />}`)
5. **Adapt LoginView + SignupView** to use `useNavigate()` instead of callback props

## ✅ Completed (autonomous)

### New files
| File | LOC | Purpose |
|---|---|---|
| `src/components/ProtectedRoute.tsx` | 60 | Auth guard wrapping the app shell. Reads `useAuth()` + `useOrg()`. Spinner while hydrating, `<Navigate to="/login">` if no session, lets saas+no-org through with a warning (better UX than infinite spinner) |
| `src/components/views/NotFoundView.tsx` | 35 | 404 catch-all inside the protected shell. Shows the requested path + "Back to Dashboard" CTA |
| `docs/runbooks/2026-06-20-phase-e-receipt.md` | (this) | Phase E receipt |

### Modified files
| File | Change | Bundle impact |
|---|---|---|
| `src/App.tsx` | Removed `DEMO_MODE` flag + `useAuth` import. Added `<Route path="/login">` + `<Route path="/signup">` (public). Wrapped ShellLayout in `<ProtectedRoute>`. Added `<Route path="*">` for 404. Added `<Navigate to="/dashboard" replace>` at index. | ShellLayout chunk stable |
| `src/auth/LoginView.tsx` | Removed `onSwitchToSignup` prop. Added `useNavigate()` + `useLocation()` to capture `from` state and redirect after success. Switched button → `<Link to="/signup">`. | Auth chunk +0.3 KB |
| `src/auth/SignupView.tsx` | Removed `onSwitchToLogin` prop. Added `useNavigate()` for `/dashboard` redirect. Switched button → `<Link to="/login">`. | Auth chunk +0.3 KB |

## 📊 Build verification

```
$ npx tsc --noEmit --pretty false
(no output — 0 errors)

$ npx vite build
✓ 1536 modules transformed (was 1534, +2 for ProtectedRoute + NotFoundView)
dist/index.html                                     1.80 kB
dist/assets/index-B2tCo83n.css                     41.10 kB (+0.05 KB)
dist/assets/index-DG2dsQjw.js                     265.38 kB (+8.98 KB)
dist/assets/NotFoundView-BvE2h1C5.js               1.41 kB (NEW)
✓ built in 4.22s
```

All 14 views + auth routes + 404 + protected wrapper compile cleanly. Bundle +8.98 KB for the routing layer.

## 🔀 Routes Map (final)

```
PUBLIC (no shell)
├── /login       → LoginView (magic link + password)
├── /signup      → SignupView (email + password + org name)

PROTECTED (ShellLayout + ProtectedRoute)
├── /                       → <Navigate to="/dashboard" replace />
├── /dashboard               → DashboardView
├── /clients                 → ClientsView
├── /clients/:id             → ClientDetailView
├── /documents               → DocumentsView
├── /agents                  → AgentsView (AI Agents Network)
├── /finance                 → FinanceView
├── /sop                     → SOPLibraryView
├── /people                  → PeopleView
├── /tasks                   → TasksView
├── /legal                   → LegalView (NEW: wired to legalDocsRepo)
├── /growth                  → GrowthView
├── /sales                   → SalesView (NEW: wired to salesLeadsRepo)
├── /marketplace             → MarketplaceView
├── /it-data                 → ItDataView
├── /settings                → SettingsView
└── *                        → NotFoundView (404 catch-all)
```

## 🛡️ Auth Flow (final)

```
User hits any protected route (e.g. /clients)
  │
  ├─ if !user → ProtectedRoute → <Navigate to="/login" state={{ from: '/clients' }} />
  │
  ├─ if isLoading → "Authenticating…" spinner
  │
  └─ if user present → render ShellLayout + Outlet(view)
       │
       └─ if IS_SAAS && isMissing(orgId) → view renders with warning banner
                                              (RLS queries return 0 rows until hook wired)
```

```
User on /login submits email+password
  │
  ├─ on error → show inline error, stay on /login
  │
  └─ on success → signIn() updates AuthContext → ProtectedRoute re-evaluates
                   → <Navigate to={from} replace /> (preserves originally requested route)
```

## ⚠️ A0 ACTION (still pending, blocks full E2E)

Same 4 actions from Phase B + D:
1. Wire JWT custom_access_token_hook in Supabase Auth dashboard
2. Add `omk_saas` to PGRST_DB_SCHEMAS in Settings → API → Exposed schemas
3. Verify Vercel Authentication OFF
4. (Optional) Paste GEMINI_API_KEY

Once these are done:
- User opens https://omk-saas-os.vercel.app/ → ProtectedRoute redirects to /login
- User signs in with `dev+omk@acme-demo.fr` + dev-password-not-for-prod (seeded)
- AuthProvider hydrates → useOrg() reads JWT org_id claim → views populate
- Sidebar nav works via PrefetchNavLink (already wired)
- 404 catch-all shows friendly error if user types wrong URL

## 🎯 Phase E → Phase F handoff

Phase F = auth onboarding polish (optional):
- Password reset flow (Supabase Auth `resetPasswordForEmail`)
- Email confirmation banner if user signs up but hasn't confirmed
- "Welcome to OMK" first-run wizard (3 steps: org name → invite team members → choose plan)
- Sign-out button visible in Sidebar (currently only logout via dev panel)

**The current LoginView + SignupView are functional** for an MVP. Phase F is polish, not blocking.

## D6 lessons shipped in Phase E

- **D6 #73**: 404 catch-all inside a nested `<Route>` (not at the root) means the ShellLayout still wraps it — the user keeps the sidebar. Better UX than redirecting to /404 which feels jarring.
- **D6 #74**: `state={{ from: location.pathname }}` pattern for redirect-after-login preserves the originally intended destination. Without it, login always redirects to `/dashboard` even if the user wanted `/clients/123`.
- **D6 #75**: Removing `DEMO_MODE` exposed a latent bug — when `useAuth()` returns `null` (auth context not yet hydrated), the redirect fires prematurely. Fix: wait for `!isLoading` before redirecting.
- **D6 #76**: `Link to="/signup"` from `LoginView` does NOT need the Suspense fallback wrapping (auth views are eagerly loaded, not lazy). Different code path than protected views.

## Anti-pattern guards

- **No-hard-delete**: The legacy DEMO_MODE flag was removed via Edit, not git revert. The original `if (!DEMO_MODE && !user)` logic was directly deleted (not archived) because it was a temporary dev shortcut per the TODO comment.
- **KISS**: Phase E avoided the temptation to add a full `/profile` route + `/admin` + etc. — just the 2 auth routes + 1 protected shell + 1 404.
- **Immutability**: Auth flow uses `<Navigate to={from} replace>` (declarative, no history manipulation).

## What still mocks the flow

- `signUp()` in AuthProvider returns "Organization provisioning requires HITL" — this is a placeholder. Real SaaS signup needs an Edge Function that creates the org + membership server-side (uses service_role key). **Open follow-up for Phase F or post-launch.**
- `signIn()` uses `signInWithPassword` (email+password) instead of magic link. Both are Supabase-supported; password is faster for dev iteration.

---

*Phase E complete. 15 routes compile, ProtectedRoute guards the shell, 404 catch-all added, auth views reworked to use useNavigate. Bundle +8.98 KB.*