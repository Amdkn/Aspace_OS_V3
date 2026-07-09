---
source: A2 Claude Code (this session)
date: 2026-06-16
type: handoff
status: ACTIVE — architecture pivot ratified by A0 (2026-06-16)
domain: L2_Business_OS / 30_Business_OS / 10_Projects + 00_Summers_QuickAccess + 00_Jerry_Business_Pulse
tags: [#business_os, #vercel, #supabase_cloud, #hermes_agent, #claude_code, #n8n, #coolify, #paas, #bare_metal_kill, #architecture_pivot, #handoff, #resumption]
context_release: 2026-06-16 — A0 has ratified the new stack: **Vercel (FE) + Supabase Cloud (BE) + Hermes Agent + Claude Code (workflow) + Coolify (N8N only, PaaS)**, replacing Bare Metal Ubuntu on Hostinger VPS for everything else.
supersedes: handoff_omk_dashboard_dev_2026-06-10.md (Dokploy → Vercel), handoff_abc_os_community_dev_2026-06-10.md (Supabase VPS → Supabase Cloud), handoff_solaris_dev_2026-06-10.md (Vercel ✓, BE routing change)
related: project_vps_hostinger_cpu_dokploy_kill_2026-06-15.md, project_abc_os_kalybana_login_postmortem_2026-06-14.md, 30_Business_OS/00_Summers_QuickAccess/02_ABC_OS/CERRIROS_HANDOVER.md (Jerry doctrine, unchanged), 30_Business_OS/00_Jerry_Business_Pulse/CEO_Directives.md
---

# Handoff — Business OS Resumption (2026-06-16)

## 0. Why this handoff exists (architecture pivot)

A0 has ratified (2026-06-16) a **major architecture pivot** for all Business OS
projects. The previous stack (Vercel FE + Supabase VPS BE + Dokploy PaaS + N8N
on Bare Metal Ubuntu at Hostinger VPS) is **defunct**. The new stack:

| Layer | Old (DOKPLOY era) | **New (2026-06-16 ratified)** |
|---|---|---|
| **Front-end** | Vercel ✓ (kept) | **Vercel** (unchanged) |
| **Back-end** | Supabase self-hosted on Hostinger VPS | **Supabase Cloud** (supabase.com) |
| **Workflow Agentic** | N8N on Hostinger VPS | **Hermes Agent + Claude Code** (orchestrator + executor) |
| **PaaS orchestration** | Dokploy (killed — see VPS postmortem) | **Coolify** (VPS-side, but **N8N-only**) |
| **VPS role** | Bare-metal-everything (Supabase, N8N, Dokploy, Coolify) | **N8N host only** (via Coolify PaaS) |
| **Dokploy** | Running, 4 containers | **KILLED 2026-06-15** (D6 root cause: 89.5% steal time) |
| **Hostinger KVM 2** | Over-provisioned, 2109 zombies | **Keep for N8N+Coolify ONLY**, kill all other containers |

**Trigger D6 root cause** (from `project_vps_hostinger_cpu_dokploy_kill_2026-06-15.md`):
- Hostinger KVM 2 steal time 89.5% → Supabase can't run on it
- Dokploy 4 containers killed definitively
- VPS-side bare-metal Kubernetes/Docker is dead for production

**Trigger D6 abc-os login** (from `project_abc_os_kalybana_login_postmortem_2026-06-14.md`):
- `https://abc-os.kalybana.com/login` returns 504 / "Failed to fetch"
- Server-side 200 OK verified via curl direct, but Kong timeout 10s < GoTrue bcrypt
- A0 rage max — 0 fix promised, D7 respect
- A0 decided: don't fix the VPS, **move Supabase to Cloud**

## 1. D1 receipts — current Business OS inventory (2026-06-16 verified)

### 1.1 Top-level structure

```
C:\Users\amado\ASpace_OS_V2\30_Business_OS\
├── 00_Jerry_Business_Pulse\         # L2 A1 vision (LD01 doctrine)
│   ├── 01_Vision_Strategy\
│   ├── 02_Global_Dashboard\
│   ├── 03_Master_Agreements\
│   ├── 04_Business_Domains\
│   ├── CEO_Directives.md
│   └── README.md
├── 00_Summers_QuickAccess\          # L2 B1/B2/B3 (5 apps quick-access)
│   ├── 00_Agency_aaS\
│   ├── 01-omk-business-os\
│   ├── 01_OMK_BOS\
│   ├── 02_ABC_OS\                   # ← most mature, has Cerritos handover
│   │   ├── B1_Summer_Direction\     # 11 .md (NORTH_STAR, 12WY, DECISION_CHARTER, B2_HANDOFF_QUEUE, DOD_SPEC, JTBD_SPEC, GOVERNANCE, BALANCE_REVIEW, VALIDATION_SPRINT, GRADUATION_GATES, FRACTAL_DEV_PLAN)
│   │   ├── B2_Business_Domains\
│   │   ├── B3_Warp_Core_Execution\ # 6 .md (SWARM_CONFIG, + 6 domain squads: Growth/Sales/Product/Ops/IT/Finance/People/Legal)
│   │   ├── CERRIROS_HANDOVER.md     # ← Jerry doctrine 2026-05-21
│   │   ├── SUMMERS_VERSE_MANIFEST.md
│   │   ├── _Inbox\
│   │   └── graphify-out\            # 1 446 nodes / 1 541 edges
│   ├── 03_RILCOT\
│   ├── 04_Alikaly\
│   └── 05_Marina\
├── 09_Blueprints\                   # business blueprints, 53 .md
├── 10_Projects\                     # 6 active project repos
│   ├── abc\                         # ABC OS + Childcare (Next.js + Supabase + 3 apps)
│   │   ├── CLAUDE.md
│   │   ├── _doctrine\
│   │   ├── apps\
│   │   │   ├── ABC OS Community\
│   │   │   ├── abc-childcare-portal\  # Next.js 15 + i18n
│   │   │   └── abc-os-community\      # Next.js + Supabase (kalybana) — LOGIN BROKEN
│   │   ├── scratch\
│   │   └── graphify-out\            # 1 689 nodes / 3 588 edges
│   ├── alikaly\
│   ├── ceo-desktop\
│   ├── marina\
│   ├── omk\                         # Vite 6 + React 19 + Supabase (REBUILD planned → Vercel)
│   ├── rilcot\
│   └── solaris\                     # Already on Vercel ✓ (2026-06-10)
├── graphify-out\                    # root, 2 155 nodes / 2 927 edges
├── Manifesto.md
└── README.md
```

**D1 totals** : 7 top-level dirs, 6 active project repos, ~30K source files estimated
(post-graphify 234 404 nodes across full ASpace).

### 1.2 Active app repos (FE/BE stack today, pre-pivot)

| App | Repo path | Frontend stack | Backend | Deploy (today) | Status |
|---|---|---|---|---|---|
| **omk-dashboard** | `30_Business_OS/10_Projects/omk/apps/omk-dashboard/` | Vite 6 + React 19 + TS 5.8 + Tailwind v4 | Supabase (target multi-tenant) | Vercel link UNUSED (was Dokploy) | REBUILD phase A done, B-H TODO |
| **abc-os-community** | `30_Business_OS/10_Projects/abc/apps/abc-os-community/` | Next.js + TS | Supabase (kalybana VPS) | Vercel ✓ | **LOGIN BROKEN 504** (see §2.1) |
| **abc-childcare-portal** | `30_Business_OS/10_Projects/abc/apps/abc-childcare-portal/` | Next.js 15 + next-intl (EN/FR) | TBD | TBD | scaffolded, i18n seed EN-default |
| **solaris** | `30_Business_OS/10_Projects/solaris/` | TBD | TBD | Vercel ✓ | dev in progress, see handoff 2026-06-10 |
| **ABC OS Community** (Landing) | `30_Business_OS/10_Projects/abc/apps/ABC OS Community/` | TBD | TBD | TBD | dormant |
| **ceo-desktop** | `30_Business_OS/10_Projects/ceo-desktop/` | TBD | TBD | TBD | dormant |
| **marina / alikaly / rilcot** | `30_Business_OS/10_Projects/<name>/` | TBD | TBD | TBD | dormant |

### 1.3 Workflow / orchestration today (pre-pivot)

- **N8N** on Hostinger VPS (PID ?, port ?, behind Dokploy).
- **Hermes CLI** = MiniMax-M3 gateway, Desktop + VPS. Token in env User.
- **Claude Code** = MiniMax-M3, 15K calls / 5h budget.
- **Symphony** (A1/A2/A3) defined canonically but not yet wired to N8N.

## 2. Architecture decisions ratified (D6 root causes + A0 sign-off)

### 2.1 Front-end = Vercel (unchanged, confirmed)

- **Rationale** : Vercel already works for abc-os-community (until 504) and
  solaris. A0 wants to keep it.
- **Constraint** : all apps must be Next.js 15+ (for native Vercel deploy) OR
  use Vercel static adapter for Vite/React.
- **Env vars** : Vercel project settings → Project root per app. No secrets in
  .md/.json/git (Test Key Pragma doctrine). Supabase keys live in Vercel env.

### 2.2 Back-end = Supabase Cloud (NEW, replaces Supabase VPS)

- **Rationale** : Hostinger VPS steal time 89.5% → Supabase self-hosted cannot
  run reliably. Supabase Cloud eliminates infra ops.
- **Migration path** : `supabase db push` from local → Cloud project. Schema in
  `supabase/migrations/`. RLS policies preserved (CRITICAL for multi-tenant).
- **Auth** : Supabase Cloud GoTrue, no Kong timeout issues (Cloud has no Kong
  in user path).
- **Cost** : Supabase Cloud FREE tier (500 MB DB, 1 GB egress, 50K MAU) is
  enough for MVP. Pro plan ($25/mo) for production.
- **Caddy vhost** : drop Caddy on VPS for kalybana.com → Supabase. Apps talk
  to Supabase Cloud directly via NEXT_PUBLIC_SUPABASE_URL.
- **A0 decision captured** : 2026-06-16, supersedes kalybana VPS architecture.

### 2.3 Workflow Agentic = Hermes Agent + Claude Code (NEW, replaces N8N-on-VPS)

- **Rationale** : N8N is a static-workflow tool. Hermes + Claude Code is a
  goal-driven agentic stack (Symphony Lane A + B + C). Already canonical in
  `00_Amadeus/05_OSS_Twin/symphony/` and wired in `MEMORY.md §"Symphony"`.
- **Pattern** :
  - **Hermes Agent** = orchestrator (routes tasks to A2 ships via routing
    patterns in `_twin.md` files).
  - **Claude Code** = executor (does the actual code/file/edit/build work).
  - **Sub-agents (A3)** = 35+ specialized twins (Picard, Freeman, Tilly, etc.)
    for parallel execution.
- **N8N** is reserved for **non-agentic** static workflows (scheduled crons,
  webhook receivers, simple if/then). It's the **lower tier** — agentic work
  goes through Hermes+Claude.
- **Hosting** : Hermes gateway on Desktop + VPS (already running per
  `MEMORY.md §"Hermes"`). Claude Code is the same M2.7/M3 backend.
- **D8 cross-agent** : Codex and Gemini CLI can be invoked from the same
  Hermes routing pattern, but Claude is the primary executor.

### 2.4 N8N = reserved to Coolify (PaaS) (NEW, replaces N8N-on-Bare-Metal)

- **Rationale** : Bare-metal N8N is fragile (zombie processes, no auto-recovery).
  Coolify = PaaS that gives N8N auto-restart, health checks, backup.
- **VPS role shrinks** : ONLY N8N (in Coolify) + maybe 1 backup postgres for
  archival. All other VPS containers killed.
- **Coolify install** : single binary on Hostinger VPS, web UI on port 8000
  (or behind Caddy reverse-proxy with TLS).
- **D7 warning** : Coolify is itself a Docker orchestrator, so if VPS steal
  time spikes again, N8N will hang. N8N is acceptable here because it has
  retries + alerts, unlike Supabase which silently 504s.

### 2.5 VPS = N8N host ONLY (kill all else) (D6 root cause applied)

- **Killed 2026-06-15** :
  - Dokploy + 4 containers (`/srv/dokploy`, all stacks)
  - Bare-metal Supabase (`supabase.kalybana.com` Caddy vhost — KEEP Caddy
    only for HTTP→HTTPS redirect)
  - 2109 zombie processes
- **Keep** :
  - Caddy (TLS + reverse proxy for Coolify web UI)
  - Coolify + N8N container
  - SSH access (mcp__claude__remote SSH)
- **VPS specs** : Hostinger KVM 2 (4 vCPU, 8 GB RAM, 100 GB SSD) — enough
  for Coolify + 1 N8N container. **Not enough** for Supabase self-hosted.
- **Renaming** : `srv941028` / `aspace-vps` / `hostinger` are all the same
  machine. Use `ASPSACE_VPS_HOST` env var (ADR-002 portability).

## 3. Migration roadmap (D7 HITL gates marked)

### Phase 1 — **Cutover Supabase VPS → Supabase Cloud** (HIGHEST PRIORITY)

**Why first** : abc-os login is broken TODAY. Other apps waiting on schema.

1. **Provision Supabase Cloud project** (A0 action required) — `amdkn` org.
2. **Dump schema from VPS** : `supabase db dump --db-url "$VPS_DB_URL" -f schema.sql`
3. **Push to Cloud** : `supabase db push --project-ref <cloud-ref>` (after A0
   sets `SUPABASE_CLOUD_DB_URL` env var User scope).
4. **Migrate RLS policies** : dump + apply (CRITICAL — multi-tenant safety).
5. **Update Vercel env vars** per app :
   - `NEXT_PUBLIC_SUPABASE_URL` = Cloud project URL
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY` = Cloud anon key
   - `SUPABASE_SERVICE_ROLE_KEY` = Cloud service key (server-side only)
6. **Test login** : `https://abc-os.kalybana.com/login` (after Caddy still
   points to nothing, app talks to Cloud directly) — expected 200 OK.
7. **Drop Caddy vhost** for `supabase.kalybana.com` (no longer needed).
8. **D7 HITL gate** : A0 must approve before deleting VPS postgres.

**D1 estimated effort** : 4-6 hours (mostly waiting on Supabase Cloud
provisioning). A0 action : 1 env var + 1 Cloud project.

### Phase 2 — **N8N-on-Coolify setup** (PARALLEL with Phase 1)

1. **Install Coolify on VPS** : `curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash`
2. **Web UI behind Caddy** : `coolify.kalybana.com` → `127.0.0.1:8000`
3. **Deploy N8N via Coolify** : image `n8nio/n8n:latest`, port 5678, env
   `N8N_HOST=n8n.kalybana.com`, `WEBHOOK_URL=https://n8n.kalybana.com/`.
4. **Migrate existing N8N workflows** : export JSON from VPS N8N → import
   to Coolify N8N (manual, 1-2 hours).
5. **D7 HITL gate** : A0 must approve before nuking bare-metal N8N.

**D1 estimated effort** : 6-8 hours (Coolify install + N8N migration).

### Phase 3 — **Wire Hermes Agent + Claude Code for agentic workflows**

1. **Hermes gateway already running** (Desktop + VPS). Verify routing to
   Claude Code.
2. **Symphony twins already defined** in `00_Amadeus/05_OSS_Twin/symphony/`.
   Wire to N8N via webhook (N8N can call `https://hermes.kalybana.com/...`
   for non-static dispatches).
3. **Replace N8N static workflows with agentic calls** : for any workflow
   that needs LLM reasoning, route through Hermes → Claude Code → A3 twin.
4. **D7 HITL gate** : A0 must ratify the routing pattern per workflow.

**D1 estimated effort** : ongoing, no deadline. Each workflow migrated
individually.

### Phase 4 — **App-by-app FE/BE cutover**

| App | Current | Target | Effort | Blocker |
|---|---|---|---|---|
| abc-os-community | Vercel + Supabase VPS | Vercel + Supabase Cloud | 2h (just env vars + schema push) | Phase 1 done |
| abc-childcare-portal | scaffolded | Vercel + Supabase Cloud | 4h (deploy + env) | Phase 1 done + Supabase schema for childcare |
| omk-dashboard | Vite + Supabase (target) | Vite on Vercel + Supabase Cloud | 16-32h (REBUILD Phase A-H) | Phase 1 done + design (Nexus mode) |
| solaris | Vercel ✓ + Supabase TBD | Vercel + Supabase Cloud | 2h (env vars) | Phase 1 done |
| ceo-desktop | dormant | TBD (depends on A0 priorities) | n/a | A0 decision |
| marina / alikaly / rilcot | dormant | TBD | n/a | A0 decision |

### Phase 5 — **VPS cleanup**

1. Once Phase 1-2 done + A0 confirms Cloud stable for 7 days, drop Caddy
   `supabase.kalybana.com` vhost.
2. Drop bare-metal postgres data.
3. Optional : resize VPS to smaller (KVM 1 = 2 vCPU 4 GB) since N8N + Coolify
   need less.

## 4. D6 lessons already shipped (do NOT re-discover)

From canon (D1 verified):
1. **VPS steal time 89.5%** = Hostinger over-provision. Don't try to host
   Supabase there. Solution: Supabase Cloud, not "fix the VPS".
2. **Dokploy is dead** : killed 2026-06-15, no resurrection. Coolify ≠ Dokploy.
3. **Kong 10s timeout** at Supabase VPS layer = 504 on slow bcrypt. Cloud
   eliminates this (no Kong in user path).
4. **Test Key Pragma** : A0 shares API keys in chat, agent sets env var User
   scope. NEVER hardcode in .md/.json/git.
5. **Caddy vhost order** : `supabase.kalybana.com` MUST be added before
   wildcard `*.kalybana.com` or it gets caught. (Already correct, but
   verify when re-adding).

## 5. Skills to use (already in `.claude/skills/`)

- `graphify-swarm-burst` — burst-graphify any new app repo (creates
  per-app junction in `.claude/memory/app-<name>/`).
- `graphify-viewer` — explore the Business OS subgraph via `localhost:8765`.
  Useful for "show me all the nodes related to omk-dashboard".
- `vercel-deploy-from-github` — Vercel deploy workflow (already exists).
- `abc-os-write-back-protocol` — post-mission write-back to canon.
- `abc-os-backend-delegation` — sibling precedent for delegation.

## 6. Open questions (D7 HITL for A0)

1. **Supabase Cloud org/region** : `amdkn` personal or new `aspace-os` org?
   EU-West-1 (Frankfurt) or US-East-1?
2. **N8N retention** : keep all existing workflows or only mission-critical
   ones (auth webhooks, payment, scheduled reports)?
3. **ceo-desktop priority** : dormant — A0 wants to revive or archive?
4. **marina / alikaly / rilcot** : dormant — A0 wants to revive or archive?
5. **Supabase Cloud plan** : FREE tier sufficient for MVP? Pro ($25/mo) from
   day 1?
6. **Custom domain on Supabase Cloud** : use `*.supabase.aspace.com` or
   keep `*.supabase.co` URLs?

## 7. D7 anti-patterns (what NOT to do)

- ❌ **Don't try to fix the VPS** (steal time is Hostinger's problem, not yours).
  Move workloads to Cloud, not optimize the host.
- ❌ **Don't resurrect Dokploy** (killed 2026-06-15, no path back).
- ❌ **Don't put N8N on bare metal** (Coolify only — auto-restart, health
  checks, backup).
- ❌ **Don't route LLM calls through N8N** (N8N is for static workflows only;
  agentic work goes Hermes → Claude Code → A3).
- ❌ **Don't hardcode Supabase keys** (env vars User scope + Vercel env, not
  in .md/.json/.git).
- ❌ **Don't skip the 7-day stability window** before dropping Caddy vhost
  for `supabase.kalybana.com` (D7 = verification before destruction).

## 8. Critical files to read FIRST when resuming

1. `30_Business_OS/00_Summers_QuickAccess/02_ABC_OS/CERRIROS_HANDOVER.md` —
   Jerry doctrine, B1→B2→B3 routing. **Unchanged** by this pivot.
2. `30_Business_OS/00_Jerry_Business_Pulse/CEO_Directives.md` — A1 vision
   anchor.
3. `30_Business_OS/00_Summers_QuickAccess/02_ABC_OS/B1_Summer_Direction/` —
   11 .md including 12WY_COMMAND_CYCLES, DECISION_CHARTER, B2_HANDOFF_QUEUE.
4. `30_Business_OS/00_Summers_QuickAccess/02_ABC_OS/B3_Warp_Core_Execution/00_B3_SWARM_CONFIG.md` —
   how the B3 squads are wired.
5. `30_Business_OS/10_Projects/omk/apps/omk-dashboard/REBUILD_WORKFLOW.md` —
   8-phase rebuild contract (A→H). **Update target = Vercel, not Dokploy**.
6. `ASpace_OS_V2/_SPECS/ADR/` — `ADR-INFRA-002` (Repo-Home/Junction) +
   `ADR-INFRA-003` (CEO Dashboard) + `ADR-CANON-001` (roster) — still binding.

## 9. Verification checklist before resuming (D1)

- [ ] `30_Business_OS/` structure unchanged from §1.1
- [ ] `ABC OS/CERRIROS_HANDOVER.md` exists + has Jerry doctrine intact
- [ ] `omk-dashboard/REBUILD_WORKFLOW.md` exists + has Phase A-F contract
- [ ] Supabase Cloud project provisioned (A0 action)
- [ ] `SUPABASE_CLOUD_DB_URL` env var User scope set
- [ ] Coolify installed on VPS
- [ ] N8N container running via Coolify
- [ ] Caddy config updated (Coolify web UI + N8N)

## 10. Out of scope (this handoff)

- Marketing site rebuild (ABC OS Community landing) — separate A0 priority.
- Mobile app variants — none exist yet.
- Data migration from legacy systems (Kounta, etc.) — see
  `MEMORY.md §"Kounta"` for separate handoff.
- Vercel project cost optimization — separate analysis.

## 11. Related canon (D1 pointers)

- `MEMORY.md` topic table lines : VPS/Hostinger, abc-os/kalybana, Kounta,
  Symphony MCPs — all in INDEX.
- `MEMORY.md` §"Graphify Open Follow-ups CLOSED 2026-06-16" — corpus state
  for the Business OS subgraph.
- `MEMORY.md` §"Doctrine Anti-Paresse" — D1-D8 binding for this handoff too.
- `MEMORY.md` §"TTS + Communication" — A0 communication style (frustrated,
  prefers TTS, hates Windows audio questions).
- `wiki/hand_offs/handoff_omk_dashboard_dev_2026-06-10.md` — **SUPERSEDED**
  by this handoff (Dokploy → Vercel, schema → Supabase Cloud).
- `wiki/hand_offs/handoff_abc_os_community_dev_2026-06-10.md` —
  **SUPERSEDED** (Supabase VPS → Cloud).
- `wiki/hand_offs/handoff_solaris_dev_2026-06-10.md` — partially applies
  (Vercel ✓, BE needs update).
- `wiki/hand_offs/handoff_telegram_channel_sovereign_2026-06-13.md` —
  unrelated (Telegram channel, no BE change).
- `MEMORY.md §"Current Session Doctrine"` — one active session at a time,
  archive others to `_TRASH`.

---

**End of handoff. A0 sign-off pending on §6 open questions. D7 = no work
without explicit A0 GO on each HITL gate.**
