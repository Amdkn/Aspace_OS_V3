# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

> **Project**: **ABC OS & Child Care BOS** — dual-entity Business OS at L2 for African cooperatives.
> **Repo root** (this file's location): `C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\abc`
> **Doctrine junction** (canonical, immutable): `_doctrine/` → `20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/02 ABC OS & Child Care BOS/`
> **Vercel contract**: `10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/04_vercel/AGENTS.md`
> **Parent context**: the CLAUDE.md at `C:\Users\amado\ASpace_OS_V2\CLAUDE.md` (Trust Zone + Shadow L0 rules).
> **Active handoff** (read first if picking up dev): `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_community_dev_2026-06-10.md`

---

## What this project is

A sovereignty-grade **cooperative business dashboard stack** designed for West/East African co-ops (current mock: *Umoja Weavers* in Nairobi, multilingual FR/EN). The 4-hub model is the spine: **Community** (discussions/events), **Learn** (courses), **Build** (project milestones), **Brand** (collective identity score).

The `Child Care BOS` entity is the parallel regulated entity — same stack, **B2-G8 Legal (Aquaman) must sign off on every offer** before launch (per `CERRIROS_HANDOVER.md`).

The routing chain is **Jerry (A1) → Cerritos → Picard/Summer (B1) → B2 Managers → B3 Squads**. This project is the B3 execution surface.

---

## The 3 apps (`apps/`)

Per `ADR-INFRA-002` (Repo-Home/Junction): **junction lives deep, apps live short**. The `abc/` root + `_doctrine` symlink is the long-lived home; the apps rotate and migrate. Each app owns its own build, its own `package.json`, and (when needed) its own app-level `CLAUDE.md` / `AGENTS.md`.

| App | Role | Stack | Git | Vercel |
|-----|------|-------|-----|--------|
| **`abc-os-community`** | **TARGET — primary dev app** (the one being built now) | Next.js 15.5.19 + React 19.1 + Turbopack + Tailwind 4 | ✅ 3 commits | ✅ `prj_HSw4IBR2omI5qegmEinOksr6xzo0` in team `team_d3JjRK4fJUE9ACohbdlhv9Gc` (amd-lab) |
| `abc-childcare-portal` | Parallel mature fork, already deployed — reference for i18n (next-intl FR/EN) and the `/build-hub` rename pattern | Next.js 16.2.7 + React 19.2 + next-intl + Tailwind 4 | ✅ 3+ commits | ✅ deployed |
| `ABC OS Community-01` | **Design source of truth** (vanilla static prototype, Space Grotesk + dark/light themes, iOS phone frame sandbox). The Next.js port must preserve visual parity | vanilla HTML/JS/CSS | ❌ | ❌ |

When porting from the static prototype, read `apps/ABC OS Community-01/picard_audit.md` (8.5/10 design, 0/10 infra — migration plan §4).

---

## Cross-app conventions

These hold across all Next.js apps in this project. When in doubt, the most mature fork (`abc-childcare-portal`) is the reference.

- **Vercel reserves `/build`**. Do not use `src/app/build/` as a route. Use `src/app/build-hub/`. `abc-childcare-portal` hit this and fixed it in commit `9ed1691`.
- **This is NOT the Next.js you know.** Recent Next 15/16 + React 19 changes APIs and conventions. Before writing any code that depends on Next APIs, read `node_modules/next/dist/docs/` in the relevant app. Sibling has a 1-line `AGENTS.md` warning — replicate it in any new app.
- **Tailwind 4** uses `@tailwindcss/postcss` + `@tailwindcss/oxide-linux-x64-gnu` (in devDependencies). Required for Linux prod builds, optional on Windows (JS fallback).
- **i18n** is `next-intl` with `messages/{fr,en}.json` — the static prototype and the community app are FR-only. Port the pattern when the app needs multilingual.
- **No tests yet** anywhere. When you add them, follow `~/.claude/rules/ecc/web/testing.md` priority: visual regression → a11y → perf → Playwright E2E.
- **TypeScript rules** (no `any`, immutable updates, no `console.log` in prod, Zod for input validation) auto-load from `~/.claude/rules/ecc/typescript/` and `~/.claude/rules/ecc/web/` in every session.

---

## Commands

```powershell
# from apps/<app-name>/
npm install      # Node 20+ enforced via package.json engines
npm run dev      # next dev --turbopack
npm run build    # next build --turbopack
npm run start
npm run lint     # eslint (next/core-web-vitals + typescript)
```

There is no top-level workspace (`npm workspaces` not configured) — each app installs its own deps. `node_modules/` is gitignored per app.

---

## Vercel contract

Canonical authority is `10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/04_vercel/AGENTS.md`. Read it before any deploy, env-var change, or domain wiring. Key extracts:

- **3-scope env vars** (`development` / `preview` / `production`) — same key holds 3 values. Set via `mcp__vercel__update_env_variable` × 3 in parallel, then re-verify with `list_env_variables` (Vercel sometimes silently drops the `target` array on PATCH).
- **Never set `SERVICE_ROLE_KEY` in any Vercel env** — the dashboard reads with anon + RLS; write ops use the VPS-side `aspace_admin` role.
- **Deploy**: Git push to a connected repo (default path), or `mcp__vercel__create_deployment` for hot-fixes.
- **Destructive ops** (project delete, domain removal, prod env-var changes) are HITL-gated — screenshot current config via `get_project` first.

App → Vercel project map (amd-lab team `team_d3JjRK4fJUE9ACohbdlhv9Gc`):

| App | Project ID |
|-----|------------|
| `abc-os-community` | `prj_HSw4IBR2omI5qegmEinOksr6xzo0` |
| `omk-dashboard` | `prj_FJpNDykkNMhDJUEg2FvKAegeeQG3` |
| `omk-landing` | `prj_o0ugJWfm19310ioQiMCngcBEOhfB` |

---

## Open tickets (cross-app)

Most tickets live at the app level (see the handoff for the 7 on `abc-os-community`). The few that are project-wide:

- **Custom domain** for `abc-os-community` (e.g. `abc-os.aspace.fr`) — DNS via `01_hostinger/AGENTS.md`, then Vercel domain assignment.
- **i18n strategy** — decision affects all 3 apps: stay FR-only, port next-intl everywhere, or EN-only compromise. Blocked on A0.
- **No tests anywhere** — if one app adds Playwright, the pattern should propagate.

---

## Verification (D1 / ADR-META-001)

Per **Verify-Before-Assert**: prove each change with observed output, not assertions.

| Change | Proof |
|--------|-------|
| App build | `npm run build` exits 0 + `npm run start` then `curl localhost:3000/<route>` → 200 |
| Type change | `npx tsc --noEmit` clean in the affected app |
| Env-var wire | `mcp__vercel__list_env_variables` shows the key in all 3 scopes |
| Deploy | `mcp__vercel__list_deployments` shows the new build + `curl` the preview URL |
| Doctrine touch | re-read the doc you're modifying before writing — junction is immutable |

---

## Write-back protocol

After meaningful work, append a one-liner to:
1. `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` (chronological append-only).
2. `00_Amadeus/30_MEMORY_CORE/README.md` (same date bullet).
3. The affected app's future `AGENTS.md` (close the relevant ticket in its Work Guidance).
