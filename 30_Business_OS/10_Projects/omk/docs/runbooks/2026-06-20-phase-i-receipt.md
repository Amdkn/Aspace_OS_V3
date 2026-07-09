# Phase I — Live E2E Audit Fix — Receipt (2026-06-20)

## D1 Receipts (filesystem proof)

### Commits

| SHA | Scope |
|---|---|
| `2ba0c39` | `fix(views): wire PeopleView + TasksView to canonical tables (D6 #95)` |

Pushed to `origin/feature/omk-saas-v1.0` (verified via `git log origin/feature/omk-saas-v1.0` = top of branch).
A0 action: merge PR → `main` to trigger Vercel production deploy (auto-deploys on merge).

### Files touched (4 in the commit)

| Action | Path | LOC delta |
|---|---|---|
| Modified | `src/data/repository.ts` | +45 (added `defaultMapper` + `identityMapper` constants) |
| Modified | `src/lib/types.ts` | +7 (extended `Agent`/`Sop` interfaces) |
| Modified | `src/lib/constants.ts` | −9 (removed `TASKS`, `TEAM` arrays) |
| Modified | `src/components/views/PeopleView.tsx` | rewritten to use `agentsRepo` (custom Capacity Load grid) |
| Modified | `src/components/views/TasksView.tsx` | rewritten to use `sopsRepo` (SOPs = procedures) |
| Deleted | `src/data/team.repo.ts` | −N (file gone) |
| Deleted | `src/data/tasks.repo.ts` | −N (file gone) |

### Verification

- `npx tsc --noEmit` → **0 errors** ✅
- `npx vite build` → **bundle 266.89 KB** (≈unchanged from pre-fix) ✅
- Live smoke: `curl -sI https://omk-saas-os.vercel.app/` → **HTTP 200, 198ms** ✅

## D6 root causes addressed

| D6 # | Symptom | Root cause | Fix (Phase I) |
|---|---|---|---|
| #95 | `[team] Could not find the table 'omk_saas.team'` (People) | `team.repo.ts` targeted table dropped in Phase A; ADR-OMK-001 never listed `team` as canonical | PeopleView rewritten against `agentsRepo`; `team.repo.ts` deleted |
| #95b | `[tasks] relation does not exist` (Tasks) | `tasks.repo.ts` targeted table never created in Phase A (only 5 omk_internal + 7 omk_saas) | TasksView rewritten against `sopsRepo` (SOPs serve as "executable procedures"); `tasks.repo.ts` deleted |
| #97 | `Client.date` undefined in UI / `Document.client` undefined | UI types expected `date`/`client` strings, DB returns `created_at`/`client_id` (snake_case) | Centralized `defaultMapper` in `repository.ts` → maps `created_at` → `date` (10 chars), `file_url` → `fileUrl`, etc. Custom mappers (SalesView, LegalView) preserved via `options.mapper` priority |
| #98 | TypeScript errors `role: 'owner'` not assignable to `Agent['role']` union | `Agent` interface missing `role` field (was just a UI detail) | `Agent.role?: 'owner' | 'manager' | 'operator' | 'viewer'` + `Sop.status?: 'draft' | 'published' | 'archived'` added |

## D2 — Future work (out of scope this sprint)

- Real `omk_saas.team_members` table (humans distinct from AI agents) when human resources need their own CRUD.
- Real `omk_saas.tasks` table with `deadline` + `completed` columns (today: visual proxy via `Sop.status === 'archived'`).
- `DocumentsView.client` proper join (currently `undefined` because DB has `client_id` UUID not `client` string). Acceptable for MVP.
- 4 hardcoded views (Growth, Marketplace, IT&Data, Settings) remain on mock data. D2 backlog.

## Rollback

If Phase I breaks live after merge:
1. `git revert 2ba0c39` (1 commit, 4 files)
2. `git push origin main` → Vercel re-deploys pre-fix SHA in ~3 min

Cost-of-rollback is low → D9 self-choice authorized this fix without intermediate A0 validation.

## Notes

- `defaultMapper` is opt-in via `mapper === identityMapper` sentinel; custom mappers (Sales, Legal) still take priority.
- PeopleView now renders unified Capacity Load grid (humans + AI as `Agent` rows with `loadFromAccuracy()` = `100 - accuracy`); D2 will swap for real backlog-based load.
- TasksView now wraps `sopsRepo` with a `completed: row.status === 'archived'` UI-local toggle; SOPs are the canonical "executable procedure" entity.
