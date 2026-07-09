---
id: ADR-INFRA-002
title: Repo-Home / Junction Law — build-bearing repos live short, doctrine stays deep
status: ACCEPTED
date: 2026-06-04
deciders: A0 Amadeus (Go), Claude Code (A2 analysis + execution)
supersedes: none
related: [ADR-INFRA-001 (governance console / doc-ownership), D10 (path-length fix), 30_Business_OS/README.md]
domain: L0 Tech_OS / Infra / Windows filesystem
tags: [#ADR #infra #D10 #maxpath #junction #repo_home #picard #solaris #preventive #immutable]
---

# ADR-INFRA-002 — Repo-Home / Junction Law

## Status
**ACCEPTED** (A0 explicit Go, 2026-06-04). Immutable per ADR Canon.

## Context
A'Space OS V2 organizes Life/Business work under deep PARA paths
(`20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\<NN Project Name>\…`). The Picard project
root alone is **76 chars**; a nested Product-domain leaf reaches **160+**. Windows enforces a
**260-char MAX_PATH** for most filesystem APIs (incl. Node/Turbopack/Next build artifacts).

**The triggering incident (D10):** `solaris-aaas` lived at base **161 chars**
(`…\03_Product_Flash_Avengers\01_solaris-aaas`). Its Next 16 build wrote a `.next` artifact at
**262 chars (> 260)** → `TurbopackInternalError: path length exceeds max length`. Lint + tsc were
green; the failure was purely environmental (Linux/Vercel built fine). The broken `.next` could
not even be deleted by `Remove-Item` (the artifact paths themselves exceeded MAX_PATH).

A scan (2026-06-04) showed the danger is structural, not a one-off:
- Picard root = 76; any Node build there + a `.next` (~165) ⇒ ~256–267 ⇒ at/over the limit.
- Partial flattening already on disk (`01-omk-business-os`=95, `omk-services`=89, base) was **still
  in the red zone**.
- **Only `30_Business_OS` (42 chars)** is safely short (worst-case `.next` ≈ 222 < 260).
- `30_Business_OS/README.md` already prescribed *"projects are never stored at deep storage — use
  junctions"*, but the rule was unnamed and applied inconsistently.

## Decision
**Two physical homes per project, separated by artifact type, bridged by a junction.**

### D1 — Doctrine stays deep
The **Verse / doctrine folder** (markdown, SOP, JTBD packets, audits, Summer logs — *no build
artifacts, no `node_modules`*) lives where it belongs under
`…/01_Projects_Picard/<NN Project Name>/`. Path length is irrelevant for text. **Do not move it.**

### D2 — Every build-bearing repo lives short
ANY repo that produces a build/dependency tree (`node_modules`, `.next`, `dist`, `build`,
`.turbo`, etc. — Next/Vite/Astro/any Node app) **MUST** physically live at
`30_Business_OS\<short-kebab-name>` (base ≤ ~60). `git` and all builds run there.

### D3 — The junction bridges them
The deep Verse keeps the app reachable via a **directory junction → the short home**:
- If the repo *is* the leaf folder (solaris case): the leaf folder itself becomes the junction.
- If the repo is a sub-app of a project (RILCOT/Alikaly/etc.): create a sub-junction
  `<Verse>\_app` → `30_Business_OS\<short-kebab>`.
Agents/humans still "find" the app inside the doctrine tree; the OS never sees the deep path for I/O.

### D4 — Naming
`30_Business_OS\<project>-<surface>` kebab-case, no spaces, no colliding leading ordinal
(e.g. `solaris-aaas`, `rilcot-members`, `alikaly-holding`, `marina-cleaning`, `abc-childcare-portal`,
`omk-front`).

### D5 — New projects are born short
New front-ends scaffold **directly** at the short home from day 1 + junction into the Verse.
Never scaffold a Node app inside the deep Picard tree "to move it later."

### D6 — Migration recipe (for existing deep repos)
```powershell
robocopy "$deep" "$short" /MOVE /E /XD ".next" /R:1 /W:1 /NFL /NDL /NP   # skip gitignored .next
$e="$env:TEMP\empty_$(Get-Random)"; ni -ItemType Directory $e|Out-Null
robocopy "$e" "$deep\.next" /MIR /R:0 /W:0|Out-Null; ri -Recurse -Force "$deep\.next",$e  # >260 delete
ri -Force $deep; ni -ItemType Junction -Path $deep -Target $short        # junction
cd $short; npm run build                                                  # must be GREEN
```
Reversible (git history intact; junction preserves the deep reference).

### D7 — Reference clones are not projects
Third-party clones kept for reference (e.g. `drawbridge`, `claudeclaw`) do not belong in the
Summers project register; they live under `00_Amadeus\05_OSS_Twin\_reference\`.

## Consequences
**Positive:** MAX_PATH eliminated for all builds; one canonical, consistent repo home
(`30_Business_OS`, the declared L2 factory); doctrine narrative preserved; reversible; no
admin-level `LongPathsEnabled` hack needed; Turbopack works unmodified.
**Negative / cost:** one indirection (junction) to remember; agents must resolve junctions when
reasoning about physical location; `git` lives at the short path while docs live deep (acceptable —
they are different artifact types).
**Rejected alternative:** Windows `LongPathsEnabled=1` + `git config core.longpaths true` —
system-level, admin-required, inconsistent Turbopack support. The junction-invert is cleaner and
canon-aligned with `30_Business_OS`.

## Applied (2026-06-04)
- ✅ `solaris-aaas` migrated to `30_Business_OS\solaris-aaas`; deep leaf is now a junction; build GREEN.
- ✅ `rilcot-members` short home pre-reserved + junction `03_RILCOT_Members_Space_OS\_app` → it (RESERVED.md).
- ✅ `drawbridge` + `claudeclaw` reference clones relocated to `00_Amadeus\05_OSS_Twin\_reference\`.
- Pending per-project (born-short on build): `omk-front`, `abc-childcare-portal`, `alikaly-holding`, `marina-cleaning`.
- Tooling: skill `/picard-repo-home` automates scaffold-short-or-migrate + junction + build-verify.
