---
receipt_id: omk_phase_b_receipt
date: 2026-06-20
phase: B (Vercel + Cloud Supabase Auth wiring)
status: 80% COMPLETE — 2 A0 actions blocking 100%
---

# 📋 Phase B Receipt — Vercel + Auth Wiring

## ✅ Completed (autonomous)

| # | Action | Receipt |
|---|---|---|
| B.1 | Verify Vercel env state | 3 env vars present: VITE_SUPABASE_URL, VITE_SUPABASE_ANON_KEY, VITE_APP_MODE=saas. GEMINI_API_KEY missing (expected). |
| B.1 | Probe hook logic via direct invocation | SQL test injected correct payload: `org_id: 00000000-0000-0000-0000-000000000a01, role: owner, app_metadata.memberships: [{role: owner, org_id: ...}]`. Function returns valid event JSON. |
| B.1 | Verify hook grants | `has_function_privilege('supabase_auth_admin', 'public.custom_access_token_hook', 'EXECUTE')` = true. |
| B.3 | Persist runbook for A0 | `omk/docs/runbooks/2026-06-20-phase-b-auth-hook-wiring.md` (3.2 KB, 4 sections, includes curl E2E test + adversarial cross-tenant test + rollback procedure). |
| B.4 | Attempt hook wiring via Management API | Attempted `POST /v1/projects/<ref>/auth/hooks` → 404 (endpoint doesn't exist on Management API). Attempted `GET /auth/hooks` → 404. Attempted `GET /config/auth` → 403 (insufficient privileges — PAT lacks owner/admin scope). **Conclusion**: only Dashboard UI can wire hooks. D6 #62 documented. |

## ⚠️ A0 ACTION REQUIRED (2 manual steps, ~5 min total)

### Action 1: Wire JWT custom_access_token_hook in Supabase Auth dashboard

**Time**: 2 minutes
**URL**: https://supabase.com/dashboard/project/ndvqwcapwcnpdvknxcjw/auth/hooks
**Steps**:
1. Toggle "Custom Access Token" → **Enabled**
2. Function: **`public.custom_access_token_hook`**
3. Save
4. Wait ~30 sec for auth provider reload
5. Verify: trigger a magic link for `dev+omk@acme-demo.fr`, decode JWT at https://jwt.io, confirm `app_metadata.org_id = 00000000-0000-0000-0000-000000000a01`

### Action 2: Verify Vercel Authentication toggle is OFF

**Time**: 1 minute
**URL**: https://vercel.com/omk-services/omk-saas-os/settings/security
**Check**: "Vercel Authentication" should be **DISABLED** per ADR-OMK-004 Condition D
**If ON**: toggle OFF, save. This prevents Vercel from forcing its own login UI on top of Supabase Auth.

### Action 3 (optional, blocks AI features only): Set GEMINI_API_KEY on Vercel

**Time**: 1 minute
**Why**: `@google/genai` is in `package.json` deps but key is missing → AI features silently fail. Not blocking for Phase C-F (which are auth + CRUD), but blocks any AI Agents view (Phase D / BLOOM).

**If A0 wants AI features to work**: paste a Gemini API key in the chat (Test Key Pragma doctrine). I'll set it on Vercel as `GEMINI_API_KEY` (encrypted, all targets).

## 📊 State summary

```
Vercel project omk-saas-os (prj_l1OkipXvr3KbLnY5fufgn2xCnZuP)
├── env vars: 3/4 set (GEMINI_API_KEY pending)
├── Vercel Authentication: A0 to verify OFF
├── latest deploy: dpl_CN5DLYP84Lh2S2z9QweBTGsMbtFx (READY/PROMOTED, sha 4837830)
└── production aliases: 3 (vercel.app + omk-services.vercel.app + git-main)

Cloud Supabase ndvqwcapwcnpdvknxcjw
├── 7 omk_saas.* tables (RLS + FORCE RLS + FK + indexes)
├── 30 RLS policies installed
├── 2 PG roles (aspace_admin + aspace_observer) with REVOKE defense
├── 1 JWT hook function (logic verified, wiring pending)
└── 7/7 drift tables archived in _archive_drift_2026_06_20 (RLS locked)
```

## 🎯 Phase B → Phase C handoff

**Blockers for Phase C**: Action 1 (hook wired). Phase C (`src/data/repository.ts` upgrade + `src/lib/tenant.ts` + `useOrg()` hook) doesn't strictly need the hook wired to **compile**, but the **runtime E2E** (curl test, live RLS query) requires the hook.

**Decision point for A0**:
- **Option A**: Pause here, you wire the hook (2 min), I resume Phase C with full E2E validation.
- **Option B**: I proceed Phase C in autonomy (compile + typecheck + unit tests only), you wire hook in parallel, full E2E at Phase G.
- **Option C**: I scaffold Phase C + D + E together (full repo rewrite, ~30 min), then we pause for hook wiring before Phase G E2E.

**Default recommendation**: Option B. Reason: Phase C + D + E are mostly code, don't need live Cloud E2E. Phase G (deploy + curl E2E) is where the hook wiring matters. Doing it in autonomy maximizes the sprint velocity.

## D6 lessons shipped in Phase B

- **D6 #62**: Supabase Management API (`api.supabase.com/v1/projects/<ref>/auth/hooks`) does NOT expose hook config endpoints. PAT insufficient. Only Dashboard UI wires hooks.
- **D6 #63**: `auth.hooks` is not queryable from SQL editor — GoTrue uses in-memory Go data structure, not a Postgres table. Verification of hook wiring is via decoded JWT inspection only.

---

*Phase B complete with 2 A0 actions remaining. Status: 80% autonomous, 20% A0.*
