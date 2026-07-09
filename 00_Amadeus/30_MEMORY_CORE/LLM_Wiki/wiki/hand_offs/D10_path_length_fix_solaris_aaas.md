---
source: Claude Code (A2) analysis, 2026-06-04
type: handoff_spec
domain: L0 Tech_OS / Infra / D10 path-length fix
owner_to_execute: Claude Code (A2) — executed in-session 2026-06-04 (A0 "lance le move ici")
status: EXECUTED / GREEN_BUILD_CONFIRMED
execution_record: |
  2026-06-04 — Move executed by Claude Code (A0 explicit "lance le move ici").
  Adjusted vs plan: the broken .next exceeded MAX_PATH so Remove-Item could not delete it;
  fixed by robocopy /MOVE with /XD .next (skip the gitignored artifact entirely), then
  mirror-empty the .next residue from an empty temp dir (robocopy /MIR handles >260),
  rmdir the empty deep folder, New-Item -ItemType Junction deep -> short home.
  Result: repo now at C:\Users\amado\ASpace_OS_V2\30_Business_OS\solaris-aaas (base 57);
  git intact (HEAD 8038f1d, clean); junction traversable; `npm run build` GREEN at short path
  (Next 16.2.6 Turbopack: Compiled successfully in 10.1s; /api/leads dynamic route present).
  D10 CLOSED.
tags: [#D10 #maxpath #junction #portal #solaris_aaas #infra #codex]
date: 2026-06-15
---

# D10 — Path-Length Fix for solaris-aaas (MAX_PATH)

## Problem (measured)
- Repo physical path is **161 chars**:
  `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\00 Agency as a Service\B2_Business_Domains\03_Product_Flash_Avengers\01_solaris-aaas`
- A Next/Turbopack build artifact reaches **262 chars** (> Windows MAX_PATH 260):
  `…\01_solaris-aaas\.next\server\chunks\ssr\node_modules_next_dist_client_components_builtin_global-error_0lgvd_..js.map`
- Result: `npm run build` fails locally with `TurbopackInternalError: path length exceeds max length of filesystem`. (lint + tsc are GREEN; this is purely a Windows path-length issue. Linux/Vercel build fine.)

## Why the existing portals DON'T fix it
The current links resolve **toward the deep path**, not away from it:
- `30_Business_OS/00_Summers_QuickAccess/00_Agency_aaS` → symlink → `…/01_Projects_Picard/00 Agency as a Service` (deep)
- `20_Life_OS/24_PARA_Enterprise/00_Links/30_Business_OS_Portal` → symlink → `30_Business_OS`
A symlink/junction resolves to the **target's real path** for file I/O. Building through a short portal still writes `.next` under the deep real path → MAX_PATH still breaks. **The link direction is inverted for a build-bearing repo.**

## Fix — invert the link for solaris-aaas only (surgical)
Move the **real repo** to a short canonical home; make the deep Picard location a **junction → the short home**.
The doctrine tree still "contains" the product via the junction; git + build run at the short path.

This matches `30_Business_OS/README.md` doctrine: *"projects are never stored at deep storage — use junctions"*
(precedent: `alykaly-front: Main Front-End (Product Flash)`).

**Recommended short home** (≈54 chars, inside Trust Zone + canonical L2 factory):
`C:\Users\amado\ASpace_OS_V2\30_Business_OS\solaris-aaas`  → build artifact ≈155 chars ✓

### Commands (PowerShell, run by Codex — local Windows infra lane)
```powershell
$ErrorActionPreference = 'Stop'
$deep = 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\00 Agency as a Service\B2_Business_Domains\03_Product_Flash_Avengers\01_solaris-aaas'
$home = 'C:\Users\amado\ASpace_OS_V2\30_Business_OS\solaris-aaas'

# 0. Safety: ensure clean git state + kill stray node/tsc; remove the broken .next
git -C $deep status --porcelain   # expect clean (D09 already committed+pushed 8038f1d)
Remove-Item -Recurse -Force "$deep\.next" -ErrorAction SilentlyContinue

# 1. Move the REAL repo to the short home (robocopy /MOVE handles long source paths)
robocopy $deep $home /MOVE /E /R:1 /W:1 /NFL /NDL /NP | Out-Null   # exit 0-7 = success

# 2. Replace the deep location with a JUNCTION -> short home (portal; doctrine tree keeps the product)
cmd /c mklink /J "$deep" "$home"

# 3. Verify: build now runs short
Push-Location $home; npm run build; Pop-Location   # should pass (no MAX_PATH)
```

### Notes / guardrails
- **Not destructive**: robocopy /MOVE relocates (git history intact); the junction preserves the deep reference. Reversible.
- Update the `00_Summers_QuickAccess/00_Agency_aaS` portal if desired to also point at the short home (optional — the agency *folder* can stay portaled; only the build-bearing **repo** needs the short physical home).
- Git remote unchanged (`github.com/Amdkn/00-Solaris`); the repo just lives at a shorter path locally.
- Alternative (not recommended): enable Windows `LongPathsEnabled=1` + `git config core.longpaths true` — system-level, admin-required, Turbopack support inconsistent. The junction-invert is cleaner + canon-aligned.
- Long-term: apply the same pattern to any future build-bearing repo (Node/Next/etc.) under deep PARA paths.

## Decision needed (A0)
Execute now? **Lane = Codex (local Windows infra, ADR-INFRA-001 D3).** Claude Code can also run the move from here if A0 prefers — but moving a live git repo + creating a junction is infra; recommend Codex executes + validates the green build, then re-pushes if `.next`-related gitignore needs touching (it shouldn't — `.next` is already ignored).

