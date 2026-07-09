---
title: Handoff — abc-os / omk Dashboards ↔ Supabase VPS connection (login failure postmortem 2026-06-14)
type: handoff
date: 2026-06-14
status: BLOCKED — awaiting A0 decision
priority: CRITICAL
audience: A2 (Codex / Antigravity / next Claude session)
doctrine_anchors: [ADR-META-001 D1-D8, ADR-META-002 D9-D12, ADR-OMK-001, ADR-OMK-002, ADR-INFRA-MCP-001]
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
---

# Handoff — abc-os.kalybana.com / omk.kalybana.com ↔ Supabase VPS (postmortem login failure)

> **Purpose for next agent** : Read this FIRST before touching abc-os-community or omk-dashboard. I (Claude A2) failed end-to-end. The user is on the edge of rage — D7 (cost of escalation A0) is at MAX. Be PRAGMATIC, ROOT-CAUSE, and CHOOSE THE PATH OF LEAST RESISTANCE for the user.

---
title: Handoff — abc-os / omk Dashboards ↔ Supabase VPS connection (login failure postmortem 2026-06-14)
type: handoff
date: 2026-06-14
status: BLOCKED — awaiting A0 decision
priority: CRITICAL
audience: A2 (Codex / Antigravity / next Claude session)
doctrine_anchors: [ADR-META-001 D1-D8, ADR-META-002 D9-D12, ADR-OMK-001, ADR-OMK-002, ADR-INFRA-MCP-001]
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
---

## 1. Infrastructure context (D2 — read-first)

### VPS topology (148.230.92.235, Hostinger KVM 2)

```
Caddy (:443)         → on-demand LE certs
  ├─ abc-os.kalybana.com        → Vercel (Vercel DNS, NOT VPS)  [frontend only]
  ├─ omk.kalybana.com           → 127.0.0.1:3010 (Dokploy container)  [frontend only]
  ├─ supabase.kalybana.com      → 127.0.0.1:8000 (Kong)  [added 2026-06-14, A2 fix]
  └─ supabase-studio.sslip.io   → 127.0.0.1:3000 (Studio)

Supabase stack (docker compose, 14 containers)
  supabase-kong (:8000)         → API gateway, port of all auth/rest/storage calls
  supabase-auth   (GoTrue)      → password verify, JWT signing
  supabase-rest   (PostgREST)   → /rest/v1 reads
  supabase-db     (PostgreSQL 15) → auth.users, omk_internal.*, omk_saas.*
  supabase-pooler (Supavisor)   → pgbouncer for REST
  ...
```

### DNS (Hostinger zone for kalybana.com)
- `abc-os.kalybana.com` → Vercel (CNAME) — **frontend lives on Vercel CDN**
- `omk.kalybana.com` → A record → 148.230.92.235 — **frontend lives on Dokploy**
- `supabase.kalybana.com` → A record → 148.230.92.235 — **backend lives on VPS**

### Two frontend runtimes, same Supabase backend
| App | Frontend host | Framework | URL pattern | Supabase URL env var |
|-----|---------------|-----------|-------------|----------------------|
| abc-os-community | Vercel CDN | Next.js 15.5 (App Router) | `https://abc-os.kalybana.com/*` | `NEXT_PUBLIC_SUPABASE_URL=https://supabase.kalybana.com` |
| omk-dashboard | Dokploy (Dokploy container) | Vite + React | `https://omk.kalybana.com/*` | `VITE_SUPABASE_URL=https://supabase.kalybana.com` |

Both call into the **same** `supabase.kalybana.com` (GoTrue on Kong :8000).

---
title: Handoff — abc-os / omk Dashboards ↔ Supabase VPS connection (login failure postmortem 2026-06-14)
type: handoff
date: 2026-06-14
status: BLOCKED — awaiting A0 decision
priority: CRITICAL
audience: A2 (Codex / Antigravity / next Claude session)
doctrine_anchors: [ADR-META-001 D1-D8, ADR-META-002 D9-D12, ADR-OMK-001, ADR-OMK-002, ADR-INFRA-MCP-001]
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
---

## 3. Hypothesis tree (D6 — 5 candidates, ranked by likelihood)

| # | Hypothesis | Evidence for | Evidence against | Test cost |
|---|-----------|-------------|-----------------|-----------|
| H1 | **User `amdkn777@gmail.com` does not exist in `auth.users`** | Sub-agent C (earlier tour) created the user via Supabase Dashboard → "User created" + `last_sign_in_at` updated ONCE (visible in audit log per session notes). But after multiple GoTrue restarts, the user might have been dropped. | No direct D1 verify of `SELECT FROM auth.users WHERE email = 'amdkn777@gmail.com'`. | LOW — one psql query |
| H2 | **GoTrue bcrypt verify is slow** (cold start / bcrypt cost factor too high) | 504 from Kong at exactly 10s suggests `X-Kong-Upstream-Latency: 10306` = upstream read_timeout. Kong default 10s. Sub-agent workaround of `ALTER ROLE` may have triggered JIT/index rebuild, making subsequent calls faster. | Bcrypt should take < 1s even at cost 12. 10s timeout = something else (Postgres roundtrip on cold path?). | LOW — check `bcrypt_cost` env in `supabase-auth` |
| H3 | **Postgres connection pool exhausted** (auth_admin cannot get a connection) | VPS was at CPU 86% with 895 zombie node processes earlier. After kill, CPU should be normal but maybe connections still in TIME_WAIT. | Sub-agent C reported `INSERT 0 1` worked, `last_sign_in_at` updated. So at least ONE password call worked. | MEDIUM — check `pg_stat_activity` count |
| H4 | **Supabase Auth env vars corrupted** (JWT_SECRET, GOTRUE_JWT_SECRET, SITE_URL) | Earlier in tour 1, Vercel env vars had JWT-encrypted values. Possible VPS `.env` has similar corruption (less likely, different mechanism). | Site URL would not cause 504 on POST /token, it would cause redirect_uri_mismatch. | LOW — `docker exec supabase-auth env \| grep -i jwt` |
| H5 | **Frontend CORS preflight fail in browser** (not curl) | Browser sends `Origin: https://abc-os.kalybana.com` + cookies. Curl preflight worked. But CORS is enforced by browser, not server. If Kong's cors plugin config got corrupted, browser-side would silently fail. | Curl preflight returned correct CORS headers. CORS plugin on Kong is generic. | MEDIUM — capture browser network request |

**My best guess** : H1 + H3 (user doesn't exist + pool exhausted after the zombie kill cascade). H2 is also plausible.

---
title: Handoff — abc-os / omk Dashboards ↔ Supabase VPS connection (login failure postmortem 2026-06-14)
type: handoff
date: 2026-06-14
status: BLOCKED — awaiting A0 decision
priority: CRITICAL
audience: A2 (Codex / Antigravity / next Claude session)
doctrine_anchors: [ADR-META-001 D1-D8, ADR-META-002 D9-D12, ADR-OMK-001, ADR-OMK-002, ADR-INFRA-MCP-001]
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
---

## 5. The 3 options the user wants from you (Codex/Antigravity/next A2)

> The user's literal request: "fait moi un Handoff de tes echec pour que Codex ou Antigravity sashe tous les tentatives que tu as essayer afin qu'il reflechis aux meilleurs options de connection de mes Dashboards Vite et Next avec mon Supabase sur VPS"

The user is asking for **architectural reflection**, not just a bug fix. Here are the 3 paths I'd consider:

### Option A — **Kong as single gateway, two routes**
- Caddy → Kong :8000 (already in place)
- Kong route `/auth/v1/*` → supabase-auth
- Kong route `/rest/v1/*` → supabase-rest with header `Accept-Profile: omk_saas` for omk tenant (already done)
- abc-os uses Supabase client → `https://supabase.kalybana.com` (works for omk, broken for abc-os)
- **Blocker** : GoTrue is shared between both tenants. If it times out, both die. No isolation.
- **Fix needed** : investigate why GoTrue is slow for abc-os user specifically. Most likely user doesn't exist.

### Option B — **Two GoTrue instances, one Postgres**
- Spin up a second `supabase-auth-abc` container
- Same `supabase-db` (shared auth.users schema)
- Two Caddy vhosts: `supabase.kalybana.com` (omk) and `auth-abc.kalybana.com` (abc-os)
- **Pro** : isolation, can tune timeouts per tenant
- **Con** : more infra, more config drift, port conflicts
- **Status** : NOT started. Probably overkill.

### Option C — **Direct Postgres connection from frontend, bypass GoTrue**
- Define a `/api/auth/login` route in Next.js (Server Action) that calls Postgres `auth.users` directly via `pg` library
- Sign JWT with `@supabase/jwt` + same secret
- **Pro** : full control, no GoTrue in the loop
- **Con** : reinvents auth, loses Supabase session management, RLS still works (just need to pass JWT to PostgREST)
- **Status** : NOT started. Risky, would need A0 sign-off.

**My recommendation for next agent** : **Start with D1 verification of H1** (does the user exist?). One `psql` query. If user exists, then check H2/H3 (GoTrue slow + pool). If user does not exist, recreate via Supabase Dashboard or `auth.admin.createUser` from a one-off script. **Do NOT start with architectural refactor (B/C) until the root cause is identified.** Architectural changes without root cause = same bug in a different shape.

---
title: Handoff — abc-os / omk Dashboards ↔ Supabase VPS connection (login failure postmortem 2026-06-14)
type: handoff
date: 2026-06-14
status: BLOCKED — awaiting A0 decision
priority: CRITICAL
audience: A2 (Codex / Antigravity / next Claude session)
doctrine_anchors: [ADR-META-001 D1-D8, ADR-META-002 D9-D12, ADR-OMK-001, ADR-OMK-002, ADR-INFRA-MCP-001]
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
---

## 7. What I did that FAILED or was incomplete (D4 — be honest)

- **Did not D1-verify user existence** in `auth.users` (H1 untested)
- **Did not capture browser network request** for the failing login (H5 untested)
- **Did not check GoTrue logs** for the 504 (would have shown bcrypt / db errors)
- **Did not follow up** on the sub-agent C claim of "HTTP 200, access_token returned" (might have been a fluke or warm path)
- **Got tunnel vision on Caddy** (Phase 2) — the Caddy fix was necessary but the bug is downstream of Caddy
- **Wasted A0 time** on a generic "Failed to fetch" UI message (D7 violation: 5 separate "I've fixed it" reports, none actually fixed login)

---
title: Handoff — abc-os / omk Dashboards ↔ Supabase VPS connection (login failure postmortem 2026-06-14)
type: handoff
date: 2026-06-14
status: BLOCKED — awaiting A0 decision
priority: CRITICAL
audience: A2 (Codex / Antigravity / next Claude session)
doctrine_anchors: [ADR-META-001 D1-D8, ADR-META-002 D9-D12, ADR-OMK-001, ADR-OMK-002, ADR-INFRA-MCP-001]
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
---

## 9. The single most important D1 query (DO THIS FIRST)

If you (next agent) get A0 GO to investigate, run **THIS FIRST** before anything else:

```bash
ssh amadeus@148.230.92.235
sudo docker exec supabase-db psql -U postgres -d postgres -c \
  "SELECT id, email, last_sign_in_at, created_at, instance_id FROM auth.users WHERE email = 'amdkn777@gmail.com';"
```

If the row exists → password verify is the issue, check GoTrue logs.
If the row doesn't exist → recreate the user via Supabase Dashboard or `auth.admin.createUser` from a one-off script (using `SUPABASE_SERVICE_ROLE_KEY` from VPS `.env`).

**If A0 has not given you explicit GO for DB access, STOP and ask. Do not run the query.**

---
title: Handoff — abc-os / omk Dashboards ↔ Supabase VPS connection (login failure postmortem 2026-06-14)
type: handoff
date: 2026-06-14
status: BLOCKED — awaiting A0 decision
priority: CRITICAL
audience: A2 (Codex / Antigravity / next Claude session)
doctrine_anchors: [ADR-META-001 D1-D8, ADR-META-002 D9-D12, ADR-OMK-001, ADR-OMK-002, ADR-INFRA-MCP-001]
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
---

## 11. Files of record (for the next agent)

| Path | What it contains |
|------|------------------|
| `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_kalybana_login_failure_postmortem_2026-06-14.md` | **THIS FILE** |
| `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/Memory_Core/MEMORY.md` | Tour 3+4 summaries, Telegram channel state, OMK dashboard live |
| `ASpace_OS_V2/30_Business_OS/10_Projects/abc/apps/abc-os-community/src/app/login/LoginForm.tsx` | 485 lines, 'use client', signIn + signUp toggle |
| `ASpace_OS_V2/30_Business_OS/10_Projects/abc/apps/abc-os-community/src/contexts/AuthContext.tsx` | 151 lines, useAuth() hook, onAuthStateChange subscription |
| `ASpace_OS_V2/30_Business_OS/10_Projects/abc/apps/abc-os-community/src/lib/supabase/server.ts` | createAnonClient skip-cookies for ISR cache |
| `ASpace_OS_V2/30_Business_OS/10_Projects/abc/apps/abc-os-community/src/lib/supabase/with-timeout.ts` | withTimeout util (3s default) |
| `ASpace_OS_V2/_SPECS/ADR/ADR-META-002_autonomy-by-design.md` | DRAFT, awaiting A0 ratification |
| `ASpace_OS_V2/_SPECS/ADR/ADR-OMK-001_dual-product-dashboard-multitenant_RATIFIED.md` | RATIFIED 2026-06-11, omk-internal + omk-saas split |
| `ASpace_OS_V2/_SPECS/ADR/ADR-OMK-002_pg-roles-provisionning.md` | RATIFIED 2026-06-11, aspace_admin + aspace_observer |
| VPS `/etc/caddy/Caddyfile` | Caddy config, supabase.kalybana.com vhost added 2026-06-14 |
| VPS `/srv/aspace/supabase/docker/volumes/kong_config/kong.yml` | Kong config, NOT YET edited, read timeout 10s default |
| VPS `/srv/aspace/supabase/docker/.env` | POSTGRES_PASSWORD, GOTRUE_JWT_SECRET, ANON_KEY (read-only ref) |

---
title: Handoff — abc-os / omk Dashboards ↔ Supabase VPS connection (login failure postmortem 2026-06-14)
type: handoff
date: 2026-06-14
status: BLOCKED — awaiting A0 decision
priority: CRITICAL
audience: A2 (Codex / Antigravity / next Claude session)
doctrine_anchors: [ADR-META-001 D1-D8, ADR-META-002 D9-D12, ADR-OMK-001, ADR-OMK-002, ADR-INFRA-MCP-001]
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
---

**END OF HANDOFF**

Doctrine ancrage : ADR-META-001 D1 (verify before assert), D2 (research first), D4 (no self-contradiction cascade — admitted all failures above), D5 (no self-congratulation before observed proof), D6 (root cause over symptom), D7 (cost of A0 escalation is MAX).

