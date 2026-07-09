---
source: Claude Code (A2) brainstorm, 2026-06-04 (A0 "BRAINSTORM sur la Meme chose pour les autres projets Picard")
type: brainstorm_proposal
domain: L0 Tech_OS / Infra / Repo-Home Standard (D10 generalization)
status: RATIFIED 2026-06-04 — ADR-INFRA-002 ACCEPTED; rilcot-members reserved; clones moved; /picard-repo-home skill created
tags: [#D10 #maxpath #junction #repo_home #picard #solaris #omk #abc #rilcot #alikaly #marina #infra #preventive]
date: 2026-06-15
---

# 🧭 Picard Repo-Home Alignment — generalize the D10 fix (preventive standard)

> **Trigger** : D10 just closed for solaris-aaas (moved to `30_Business_OS\solaris-aaas` + junction, build GREEN).
> A0 asked to brainstorm the same alignment for the other Picard projects:
> **00_solaris (done) · 01 OMK · 02 ABC OS · 03 RILCOT Members Space · 04 Alikaly Holding landing · 05 Marina Cleaning.**

## 1. What the scan actually found (measured 2026-06-04)
| Picard entry | base len | type | build-bearing? |
|---|---|---|---|
| `00 Agency as a Service/.../01_solaris-aaas` | was 161 → now **junction** | AaaS front (Next 16) | **YES — migrated ✅** |
| `01 OMK Business OS` | 95 | doctrine folder (md/SOP) | no |
| `01-omk-business-os` (git, Amdkn/01-OMK-Business-OS) | 95 | **doctrine git repo** (B1/B2/B3 + .md) | no — no package.json anywhere |
| `omk-services` | 89 | folder | no |
| `02 ABC OS & Child Care BOS` | 103 | doctrine folder | no |
| `03_RILCOT_Members_Space_OS` | 103 | doctrine folder | no (member-space app not built yet) |
| `04 Alikaly Bana Holding to LLC` | 107 | doctrine folder | no (landing not built yet) |
| `05 marina Cleaning BOS & SOP` | 105 | doctrine folder | no (landing/booking not built yet) |
| `drawbridge` (breschio/drawbridge, pkg "moat") | 87 | **3rd-party clone** (reference) | yes, but not A0's project |
| `claudeclaw` (robonuggets/claudeclaw) | 87 | **3rd-party clone** (reference) | — |

**Key insight:** *only solaris had a build-bearing front-end.* The other 5 named projects are **doctrine folders today** — they have NO `node_modules`/`.next`, so they are NOT currently breaking MAX_PATH. The work here is therefore **preventive doctrine**, not a fire to put out: lock the rule now so the next front-end (RILCOT member space, Alikaly landing, Marina booking, an OMK dashboard) is **born short** instead of repeating the solaris mistake.

**Second insight:** the partial flattening already on disk (`01-omk-business-os`, `omk-services` at Picard root, base 87–95) is **still inside the danger zone** (base 87 + `.next` ~165 = ~252–267 > 260). Picard root itself is 76 chars — too deep to safely host a Node build. **Only `30_Business_OS` (42) is safe.**

## 2. The proposed standard — separate the two artifact types
Every Picard/Summer project has (or will have) up to **two** distinct physical homes:

1. **The Verse/Doctrine folder** — deep, human-readable, spaces allowed, lives under `…/01_Projects_Picard/<NN Project Name>/`. Holds markdown, SOPs, audits, JTBD packets, Summer execution logs. **Path length is irrelevant** (no build artifacts, no node_modules). This is the A0-facing narrative home. *Leave these exactly where they are.*

2. **The build-bearing repo** — ANY Node/Next/Vite/Astro app (anything with `node_modules` + a `.next`/`dist`/`build` artifact tree). **MUST live at** `30_Business_OS\<short-kebab-name>` (base 42, worst-case `.next` ≈ 222 < 260 ✓). The deep Verse folder gets a **junction → the short home**, so navigation/agents still "find" the app inside the doctrine tree, while `git` + `npm run build` run at the safe short path.

This is exactly what `30_Business_OS/README.md` already prescribes (*"projects are never stored at deep storage — use junctions"*) — we're making it a hard, named law and applying it consistently.

### Naming convention (short home)
`30_Business_OS\<project>-<surface>` in kebab-case, no spaces, no leading ordinal that collides:
- solaris-aaas ✅ (already)
- omk-dashboard / omk-front (when built)
- abc-childcare-portal
- rilcot-members (the member space — almost certainly the next real front-end)
- alikaly-holding (landing)
- marina-cleaning (landing/booking)

## 3. Per-project plan
| Project | Action now | Action when a front-end is built |
|---|---|---|
| **00 solaris** | ✅ done (junction live, build GREEN) | — |
| **01 OMK** | none (doctrine-only; `01-omk-business-os` git repo is docs, stays put) | new front → `30_Business_OS\omk-front` + junction into the OMK Verse |
| **02 ABC OS** | none (doctrine-only) | childcare portal → `30_Business_OS\abc-childcare-portal` + junction |
| **03 RILCOT Members Space** | none yet — **but this is the most likely next build** (a "members space" = web app) → pre-reserve `30_Business_OS\rilcot-members` | scaffold directly at the short home from day 1 |
| **04 Alikaly Holding landing** | none yet | landing → `30_Business_OS\alikaly-holding` (born short) |
| **05 Marina Cleaning** | none yet | landing/booking → `30_Business_OS\marina-cleaning` (born short) |

**Optional side-cleanup (not blocking):** `drawbridge` + `claudeclaw` are third-party reference clones sitting at Picard root — they don't belong in the Summers project register. Recommend relocating to `00_Amadeus\05_OSS_Twin\_reference\` (or a `_reference/` under Picard) so the project root stays clean. A0 call.

## 4. The reusable procedure (proven on solaris — the migration recipe)
For an **existing** build-bearing repo stuck deep (the solaris case):
```powershell
$deep = '<deep Verse path>\<repo>'
$short = 'C:\Users\amado\ASpace_OS_V2\30_Business_OS\<short-kebab>'
# 1. confirm clean git; 2. move everything EXCEPT the gitignored .next (which may itself exceed MAX_PATH):
robocopy "$deep" "$short" /MOVE /E /XD ".next" /R:1 /W:1 /NFL /NDL /NP
# 3. mirror-empty the leftover .next from an empty temp dir (only way to delete >260-char trees):
$e = "$env:TEMP\empty_$(Get-Random)"; ni -ItemType Directory $e | Out-Null
robocopy "$e" "$deep\.next" /MIR /R:0 /W:0 | Out-Null; ri -Recurse -Force "$deep\.next","$e"
# 4. rmdir the empty deep folder, junction it to the short home:
ri -Force $deep; ni -ItemType Junction -Path $deep -Target $short
# 5. verify: cd $short; npm run build   (must be GREEN, no MAX_PATH)
```
For a **new** project: skip all of the above — just `git init` / scaffold straight into `30_Business_OS\<short-kebab>` and junction it into the Verse folder.

> 🛠️ **Skill Reflex note** (proposal, not auto-run): this 5-step move now has a name and will recur every time a Picard front-end is born or rescued. Candidate skill `/picard-repo-home` (scaffold-short-or-migrate + junction + verify build). ROI ≈ 10–15 min + 1 averted MAX_PATH incident per project. Propose only — awaiting A0 Go.

## 5. Decision needed (A0)
1. **Ratify the standard** as **ADR-INFRA-002 (Repo-Home / Junction Law)** — build-bearing repos live at `30_Business_OS`, doctrine stays deep, junction bridges them? (recommend YES — it's the generalization of the fix you just approved.)
2. **Pre-reserve `rilcot-members`** now (the obvious next front-end), or wait until you actually start it?
3. **Side-cleanup** of the `drawbridge`/`claudeclaw` reference clones out of Picard root — do it, or leave?
4. **Create `/picard-repo-home` skill** now, or after the next project proves the recipe a second time?

