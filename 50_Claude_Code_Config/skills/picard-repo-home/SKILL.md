---
name: picard-repo-home
description: >
  Enforce the A'Space ADR-INFRA-002 Repo-Home / Junction Law on Windows: keep build-bearing
  repos (Node/Next/Vite/Astro — anything with node_modules/.next/dist) at the short canonical home
  30_Business_OS\<short-kebab>, while the deep Picard doctrine folder keeps a junction to it.
  USE THIS SKILL whenever the user (A0) wants to scaffold a new Picard/Summer front-end, "create the
  landing page / member space / dashboard" for a project, OR when a Windows build fails with
  "path length exceeds max length" / MAX_PATH / TurbopackInternalError / a repo sits deep under
  01_Projects_Picard and needs rescuing. Trigger on phrases like "born short", "move the repo",
  "fix the path length", "junction the project", "scaffold rilcot-members / alikaly-holding /
  marina-cleaning / abc-childcare / omk-front", or any new build-bearing repo under a deep PARA path.
  Prefer this over ad-hoc robocopy/mklink sequences — it bakes in the proven D10 recipe (handles the
  >260-char .next that Remove-Item can't delete) and verifies a GREEN build.
---

# Picard Repo-Home / Junction Law (ADR-INFRA-002)

## Why
Windows caps most filesystem paths at **260 chars (MAX_PATH)**. The Picard project tree is deep
(`20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\<NN Project Name>\…` ≥ 76 chars before the repo).
A Node/Next build writes `.next`/`dist` artifacts ~165 chars long → deep repos blow past 260 and the
build dies (`TurbopackInternalError: path length exceeds max length`). Worse, the broken `.next`
can't even be deleted by `Remove-Item` because its own paths exceed MAX_PATH.

The fix (ratified as **ADR-INFRA-002**): **build-bearing repos live short** at
`30_Business_OS\<short-kebab>` (base ≈ 42–60, safe); the **doctrine folder stays deep**; a
**junction** bridges them so navigation still finds the app inside the Verse.

Read the canon if unsure: `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\ADR-INFRA-002_repo-home-junction-law.md`.

## Two modes

### Mode A — NEW front-end (born short)
The default and preferred path. Never scaffold a Node app inside the deep Picard tree.
1. Pick a short kebab name: `<project>-<surface>` (e.g. `rilcot-members`, `alikaly-holding`).
2. Scaffold/`git init` **directly** at `C:\Users\amado\ASpace_OS_V2\30_Business_OS\<name>`.
3. Create the bridge junction into the project's deep Verse folder:
   - If the app is the project's sole deliverable and the leaf folder is the repo: make the leaf a junction.
   - If the app is one sub-app of a doctrine project: `New-Item -ItemType Junction -Path "<Verse>\_app" -Target "30_Business_OS\<name>"`.
4. Verify: `cd 30_Business_OS\<name>; npm run build` is GREEN.

### Mode B — RESCUE an existing deep repo (the D10 case)
Use the bundled script — it handles the un-deletable `.next`:
```powershell
powershell -NoProfile -File "<this-skill>\scripts\migrate_repo_home.ps1" `
  -Deep  "<full deep path to the repo>" `
  -Short "C:\Users\amado\ASpace_OS_V2\30_Business_OS\<short-kebab>"
```
The script: confirms clean git → `robocopy /MOVE /XD .next` (skips the gitignored artifact) →
mirror-empties the leftover `.next` with `robocopy /MIR` from an empty temp dir (only way to delete
a >260-char tree) → removes the empty deep folder → creates the junction → runs `npm run build`.
It is **reversible** (git history intact; junction preserves the deep reference).

## Hard rules (from ADR-INFRA-002)
- **Never** scaffold or leave a Node/build repo under `01_Projects_Picard\…` deep paths.
- **Only** `30_Business_OS\<short-kebab>` is a safe build home (Picard root at 76 is already too deep).
- Doctrine (markdown/SOP) **stays deep** — do not move text into `30_Business_OS`.
- Naming: kebab-case, no spaces, no colliding leading ordinal.
- Reference clones (3rd-party) are **not projects** → `00_Amadeus\05_OSS_Twin\_reference\`.
- After any migration, the build **must be GREEN** before declaring done. Log the close to
  `00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\log.md`.

## Pre-reserved homes (already created)
- `30_Business_OS\solaris-aaas` (LIVE, migrated) · `30_Business_OS\rilcot-members` (RESERVED).
Future: `omk-front`, `abc-childcare-portal`, `alikaly-holding`, `marina-cleaning`.
