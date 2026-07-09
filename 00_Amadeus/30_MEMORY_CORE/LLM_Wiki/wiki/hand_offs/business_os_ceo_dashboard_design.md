---
source: Claude Code (A2) architecture design, 2026-06-04 (A0 reframe: "30_Business_OS = poupée russe DANS Life OS, CEO Dashboard, 8 domaines par projet, gestion intelligente long/court chemin")
type: architecture_proposal
domain: L2 Business OS / structure / CEO Dashboard Matryoshka
status: EXECUTED 2026-06-04 (ADR-INFRA-003 ACCEPTED; 7/8 apps migrated; alikaly-os pending IDE-lock release)
tags: [#ceo_dashboard #matryoshka #business_os #junction #maxpath #picard #8_domains #structure]
date: 2026-06-15
---

# 🏛️ Business OS as CEO Dashboard — the Matryoshka design

## The reframe (A0)
`30_Business_OS` is NOT a flat dustbin where build repos get "jetés bêtement comme un déchet".
It is the **poupée russe à l'intérieur de Life OS** — a **CEO Dashboard** that mirrors the Life OS
structure: **each project, structured by its 8 Business domains**, with *intelligent* path management
— only the artifacts that *need* a short path (apps that build) get one; doctrine stays deep.

## What already exists (don't reinvent — extend)
- `00_Jerry_Business_Pulse/04_Business_Domains/` — the **8-domain PERPETUAL doctrine** (Jerry, the *why*). Cross-project.
- `00_Summers_QuickAccess/` — **junctions to each project's deep Verse** (the navigation portal). 7 entries
  (Agency, OMK→`01-omk-business-os`, ABC, RILCOT, Alikaly, Marina). They resolve *toward* the deep paths
  (great for reading doctrine; useless for building — same MAX_PATH inversion as D10).
- `09_Blueprints/` — ADR/onboarding templates.
- `solaris-aaas`, `rilcot-members` — flat short homes (the "déchet" to re-home into the dashboard).

**Tiebreaker resolved:** QuickAccess already canonicalizes OMK as `01-omk-business-os` (kebab). So that
tree is canon; `01 OMK Business OS` (spaces) + `_Inbox` copies are the duplicates to quarantine.

## The design — `10_Projects` (the CEO grid)
Replace the flat dump + the deep-pointing portal with ONE structured grid. Per project, two halves:
- **`_doctrine`** = junction → the deep Picard Verse (the full B1/B2/B3 + 8-domain narrative; long paths fine).
- **`apps/`** = the *real short build homes* for that project's build-bearing artifacts (landing + dashboard).

```
30_Business_OS/                                  (base 42 — the whole reason this works)
├── 00_Jerry_Business_Pulse/        8-domain doctrine (the WHY) — unchanged
├── 09_Blueprints/                  templates — unchanged
└── 10_Projects/                    ← THE CEO DASHBOARD (each project, 8 domains visible)
    ├── solaris/
    │   ├── _doctrine →J→ Picard\00 Agency as a Service   (8-domain narrative, build-free)
    │   └── apps/
    │       ├── landing      = solaris-aaas      (00-Solaris)         [moved ✅ → re-home here]
    │       └── dashboard    = aaas-os           (00-AaaS-Agency-Garden)
    ├── omk/
    │   ├── _doctrine →J→ Picard\01-omk-business-os
    │   └── apps/{ landing = omk-services-front-end, dashboard = omk-services-business-os }
    ├── abc/   └── _doctrine →J→ Picard\02 ABC OS & Child Care BOS   (no app yet)
    ├── rilcot/
    │   ├── _doctrine →J→ Picard\03_RILCOT_Members_Space_OS
    │   └── apps/{ members = rilcot-members-v2 }                      (reuse rilcot-members home)
    ├── alikaly/
    │   ├── _doctrine →J→ Picard\04 Alikaly Bana Holding to LLC
    │   └── apps/{ holding = alikaly-holding-front-v2, os = alykaly-os-v2 }
    └── marina/
        ├── _doctrine →J→ Picard\05 marina Cleaning BOS & SOP
        └── apps/{ landing = marina-cleaning-front-end }
```

**The bridge back:** in each deep Picard `…\03_Product_Flash_Avengers\<app>`, the app folder becomes a
**junction → its short home** in `10_Projects/<proj>/apps/<role>`. So the deep Verse still "contains"
the app for narrative continuity; git + build run short. (Exactly the D10 pattern, now organized.)

## Why the 8-domain view is preserved without blowing the path budget
- The **8-domain structure is fully visible** through `_doctrine` (the junction exposes the deep
  B1/B2/B3 with all 8 Marvel/DC domains — that tree never builds, so its length is irrelevant).
- Only **Product Flash (and later IT Cyborg backends)** materialize as *real* short homes under `apps/`.
  The other 7 domains don't need a physical home in the dashboard — they live as doctrine (deep) +
  Jerry-Pulse (cross-project). This is the "intelligent long/short management" you asked for.

### Path-length math (the proof it's safe)
`30_Business_OS\10_Projects\solaris\apps\dashboard` = **42 + 39 = 81 base**.
Worst-case Next `.next` artifact adds ≈101 → **≈182 < 260** ✓ (solaris's killer artifact was 262 at base 161).
Even the deepest (`alikaly\apps\holding`) stays ≈185. Headroom ≈75 chars. Safe for every project.

## Decisions I'll bake in (you said "sais pas" — Architect's call, reversible)
1. **OMK canon = `01-omk-business-os`** (kebab, per your QuickAccess). Quarantine the spaces-dup + `_Inbox`
   to `_TRASH/` (not delete — Deep Checkpoint Law).
2. **Prototypes** (`00_Interface_Prototypes/*`, no GitHub remote): move to a per-project
   `_doctrine/…/_archive/` (kept, out of the build path) — not deleted. The remote-backed v2 apps are the keepers.
3. **QuickAccess** stays as-is (doctrine navigation) OR folds into `10_Projects/<proj>/_doctrine` (cleaner —
   one grid). Recommend fold-in, leave a compatibility note.

## Migration = 8 apps (the canonical, remote-backed set)
solaris-aaas (re-home) · aaas-os · omk landing · omk dashboard · rilcot-members-v2 · alikaly-holding ·
alikaly-os · marina-cleaning. Each via the proven `/picard-repo-home` recipe (handles >260 `.next`),
build-verified GREEN, junctioned back into its deep Verse.

## Turn-2 — what I need from you
**Go on this structure?** (then I write ADR-INFRA-003 + execute the 8 migrations + quarantine the OMK dup).
Adjustments to weigh:
- Segment naming: `10_Projects/<proj>/apps/<role>` (lean, recommended) vs a fuller per-project
  `04_Product_Flash/` Marvel level (richer mirror, ~22 chars more — still safe, just closer).
- Fold QuickAccess into the grid, or keep both?

