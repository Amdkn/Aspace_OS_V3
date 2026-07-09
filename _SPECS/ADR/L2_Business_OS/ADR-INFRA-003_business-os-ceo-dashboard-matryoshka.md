---
id: ADR-INFRA-003
title: Business OS CEO Dashboard — the 10_Projects Matryoshka + LD01_Business_Picard H10 anchor (refines ADR-INFRA-002)
status: ACCEPTED + AMENDED 2026-06-21 RATIFIED (A0 Amadeus « GO » batch, §D1 LD01 Picard H10 + MANIFEST.md obligatoire ratified, sister scope ADR-L2-AAAS-001 + ADR-MEM-002 + ADR-SOBER-002)
date: 2026-06-04 (original) / 2026-06-21 (amendment §D1)
deciders: A0 Amadeus (Go — "30_Business_OS = poupée russe dans Life OS, CEO Dashboard, 8 domaines par projet"), Claude Code (A2 design + execution); amendment 2026-06-21 = sister scope A3 Data + A0 ratification pending
refines: ADR-INFRA-002 (Repo-Home / Junction Law — flat model)
amended_by: 2026-06-21 §D1 amendment (sister scope ADR-L2-AAAS-001 + ADR-MEM-002 + ADR-SOBER-002)
related: [D10, ADR-INFRA-001, 00_Summers_QuickAccess, 00_Jerry_Business_Pulse, ADR-L2-AAAS-001, ADR-MEM-002, ADR-SOBER-002, AGENTS.md §L1/A1 Beth Ikigai]
domain: L2 Business OS / structure / CEO Dashboard / LD01_Business_Picard
tags: [#ADR #ceo_dashboard #matryoshka #business_os #junction #maxpath #8_domains #picard #ld01 #h10 #manifest #immutable]
doctrine_anchors: [ADR-META-001, ADR-META-001-D4, ADR-META-001-D7, ADR-META-002-D9, ADR-INFRA-002, ADR-L2-AAAS-001, ADR-MEM-002, ADR-SOBER-002]
sign_off_a0: "A0 Amadeus — Original Go 2026-06-04 (CEO Dashboard) ; 2026-06-21 GO batch ratification §D1 amendment LD01 Picard H10 + MANIFEST.md obligatoire"
sign_off_pending_amendment: false
ratification_log_2026-06-21: "A0 verbal GO en chat Claude Code 2026-06-21. §D1 amendment sister scope à ADR-L2-AAAS-001 + ADR-MEM-002 + ADR-SOBER-002 (même batch). D4 append-only = section §D1 ajoutée sans modification des sections D2-D7 originales. D7 cost-of-escalation respecté. INFRA-003 = désormais ACCEPTED + AMENDED 2026-06-21 RATIFIED."
---

# ADR-INFRA-003 — Business OS CEO Dashboard (10_Projects Matryoshka)

## Status
**ACCEPTED** (A0 Go, 2026-06-04). Immutable. Refines ADR-INFRA-002.

## Context
ADR-INFRA-002 moved build-bearing repos to short homes but in a **flat** layout
(`30_Business_OS\<kebab>`). A0 rejected the flat model: *"au lieu de les jeter bêtement dans
Business OS comme si c'était un déchet"*. The correct model: **`30_Business_OS` is the poupée russe
inside Life OS** — a **CEO Dashboard** that mirrors the Life OS structure, with **each project
structured by its 8 Business domains**, and *intelligent* path management (only build-bearing
artifacts get a short home; doctrine stays deep).

A deep scan found **every project's apps were buried in the long `03_Product_Flash_Avengers` paths**
(25 app repos, base 156–224, the same MAX_PATH trap as solaris/D10), plus duplicates (OMK tree ×2 +
`_Inbox`) and dev prototypes.

## Decision
### D1 — The grid: `30_Business_OS\10_Projects\<project>\` + LD01_Business_Picard H10 anchor (AMENDED 2026-06-21)
The CEO Dashboard. Each project folder has two halves:
- **`_doctrine`** = junction → the deep Picard Verse (the full B1/B2/B3 + 8-domain narrative). The
  8-domain structure is **fully visible here**; it never builds, so its length is irrelevant.
- **`apps\<role>`** = the *real short build homes* for that project's build-bearing artifacts
  (`landing`, `dashboard`, `members`, `holding`, `os`, …). git + build run here.

**LD01_Business_Picard H10 anchor — AMENDED 2026-06-21 (sister scope ADR-L2-AAAS-001 + ADR-MEM-002 + ADR-SOBER-002)** :

Chaque projet dans `10_Projects/<proj>/` est ancré canoniquement sur **LD01_Business_Picard** comme **A3 captain USS Enterprise (PARA ship)** avec :
- **Horizon canonique** : **H10** (10-week sprint cycle, sister cadence `ADR-Meta-000_12-week-year-cycle-doctrine_DRAFT.md`).
- **Rôle canonique** : **projects owner** (pilote les projets dans le cycle 12WY Q3 2026 06/15 → 09/07).
- **MANIFEST.md obligatoire** par projet dans `<proj>/MANIFEST.md` (pas dans `_doctrine/` — au top-level du projet pour visibilité immédiate). Format canonique :
  ```yaml
  ---
  id: PROJ-<kebab-name>
  title: "<Project Display Name>"
  ldxx_mirror: "LD01_Business_Picard (H10 sprint, projects owner)"
  a3_anchor: "A3 Picard (LD01 Business H10 projects captain)"
  status: [INITIATED | ACTIVE | ARCHIVED | DORMANT]
  aaaS_variant: [Solaris | Nexus-OMK | Orbiter-ABC | Family-Home-dormant]
  cycle: "12WY-Q3-2026"
  rock_count: <int>
  ---
  ```
- **Cadence** : sprint H10 → decomposition H1 hebdo via A3 Book (LD01 H1 weekly P&L) → daily standup via A3 Ortegas (SNW Curie H1).
- **Tools canoniques** : `picard-repo-home` skill (`~/.claude/skills/picard-repo-home/`) + `build_ceo_dashboard.ps1` automation script (cf. §Consequences).

**Path canonique PICARD ownership matrix** :

| LDxx | A3 captain | Project role | `_doctrine/` content |
|---|---|---|---|
| **LD01** | **A3 Picard (Captain USS Enterprise, H10)** | **projects owner canon — primary** | Junction deep → `24_PARA_Enterprise/01_Projects_Picard/<NN>/` |
| LD02 | A3 Saru (LD02 Finance H3) | finance officer advisory | Junction deep → `24_PARA_Enterprise/01_Projects_Picard/<NN>/finance_models/` |
| LD03 | A3 Culber (LD03 Health H10) | health officer advisory | Junction deep → `24_PARA_Enterprise/01_Projects_Picard/<NN>/health/` |
| LD04 | A3 Tilly (LD04 Cognition H30) | science officer advisory | Junction deep → `24_PARA_Enterprise/01_Projects_Picard/<NN>/cognition/` |
| LD05 | A3 Stamets (LD05 Social H30) | mycelium network officer | Junction deep → `24_PARA_Enterprise/01_Projects_Picard/<NN>/social/` |
| LD06 | A3 Burnham (LD06 Family H10) | family officer advisory | Junction deep → `24_PARA_Enterprise/01_Projects_Picard/<NN>/family/` |
| LD07 | A3 Reno (LD07 Creativity H10) | chief engineer creative | Junction deep → `24_PARA_Enterprise/01_Projects_Picard/<NN>/creativity/` |
| LD08 | A3 Georgiou (LD08 Impact H90) | mirror emperor audit | Junction deep → `24_PARA_Enterprise/01_Projects_Picard/<NN>/impact/` |

**Doctrine Picard = "owner d'un projet Life Wheel-aware"** : chaque projet est un mini-B1/B2/B3 fractal ancré sur la matrice 8×8×8 (8 Domaines × 8 Hero Managers × 8 Marvel/DC squads, cf. ADR-CANON-001). Picard owns the projects, Book supervise P&L hebdo, Saru finance quarterly, Burnham family H10.

**Référence cross-ADR** :
- `ADR-L2-AAAS-001 §D3` (matrice 8 Domaines × LD01-LD08 × AaaS variants) — sister scope 2026-06-21.
- `ADR-MEM-002 §D1` (mapping 5-couches mémoire × 8-LDxx, row LD01 = Business_Picard) — sister scope 2026-06-21.
- `ADR-SOBER-002 §D3` (7 hard-stop triggers avec audit owner = A3 twins LDxx-spécifiques) — sister scope 2026-06-21.

### D2 — Only build-bearing domains materialize short
Product Flash apps (and later IT Cyborg backends) get real short homes under `apps\`. The other 7
domains live as doctrine (deep, via `_doctrine`) + cross-project doctrine (`00_Jerry_Business_Pulse`).
This is the "intelligent long/short management."

### D3 — Junction-back into the Verse
Each deep `…\03_Product_Flash_Avengers\<app>` becomes a junction → its short home, so the Verse still
"contains" the app for navigation while builds run short. (The D10 pattern, organized.)

### D4 — Path budget (proven)
Root `30_Business_OS` = 42. `10_Projects\<proj>\apps\<role>` homes measure **71–77 chars**; worst-case
`.next` ≈ +101 → **≈178 < 260** ✓ (~75 char headroom). Build verified GREEN at the new path
(solaris landing, Next 16.2.6).

### D5 — Lean naming
`10_Projects\<proj>\apps\<role>` (kebab, no spaces). Chosen over a fuller `04_Product_Flash\` Marvel
level to maximize path headroom; the Marvel/8-domain view lives in `_doctrine` + Jerry-Pulse.

### D6 — Coexistence
`00_Summers_QuickAccess` (deep-pointing nav junctions) is **kept** alongside the grid (A0 choice).
`00_Jerry_Business_Pulse` (8-domain perpetual doctrine) and `09_Blueprints` unchanged.

### D7 — Dedup & prototypes
- OMK canon = `01-omk-business-os` (per QuickAccess); the spaces-dup `01 OMK Business OS` + `_Inbox`
  quarantined to `_TRASH\omk-dedup_2026-06-04\` (not deleted — Deep Checkpoint Law).
- Non-remote dev prototypes under `00_Interface_Prototypes\` stay deep (reachable via `_doctrine`),
  archived later; only remote-backed v2 apps are promoted to short homes.

## Applied (2026-06-04 → 2026-06-05) — 8/8 migrated
| Project | app | short home (len) | status |
|---|---|---|---|
| solaris | landing | 10_Projects\solaris\apps\landing (75) | ✅ build GREEN |
| solaris | dashboard (aaas-os) | …\solaris\apps\dashboard (77) | ✅ |
| omk | landing | …\omk\apps\landing (71) | ✅ |
| omk | dashboard (bos) | …\omk\apps\dashboard (73) | ✅ |
| rilcot | members | …\rilcot\apps\members (74) | ✅ |
| alikaly | holding | …\alikaly\apps\holding (75) | ✅ |
| alikaly | os | …\alikaly\apps\os (70) | ✅ build GREEN (recovered — see incident) |
| marina | landing | …\marina\apps\landing (74) | ✅ |

All 8 have `_doctrine` junctions; all junction-backs reachable; OMK dup + flat homes retired.

### Incident — alikaly os (2026-06-05)
`02_alykaly-os-v2` was a **repo-in-repo** (nested `alykaly-os-V2`). It was locked by an open IDE
workspace (Antigravity/VS Code), so the first `Move-Item` fell back to copy+delete and aborted on
`.git` (access denied), partially gutting the source (root files + `.git` lost). **Recovery:** preserved
the mangled tree to `_TRASH\alikaly-os-mangled_2026-06-05` (Deep Checkpoint Law — checked: no `.env`
secrets, only `.env.example` which is in git), then **re-cloned from GitHub `Amdkn/04-Alikaly-Bana-OS`
(main)**, reused node_modules, junctioned back, build GREEN. **Lesson baked into the recipe:** for a
locked or repo-in-repo target, do NOT Move-Item (copy+delete corrupts) — require the lock released and
use atomic `[IO.Directory]::Move`; if a clean remote exists, re-clone is the safe recovery. Risk noted:
any *unpushed* local commits in that repo were lost (it was `dirty=0` + had a remote, so loss is
limited to unpushed commits, if any).

## Consequences
**Positive:** one structured CEO grid; 8-domain view preserved (via `_doctrine`); builds short & safe;
doctrine narrative intact; reversible (junctions). **Cost:** junction indirection; one IDE-lock edge
case on move (close the workspace, retry). **Tooling:** `/picard-repo-home` skill +
`build_ceo_dashboard.ps1` automate it.

---

## AMENDMENT 2026-06-21 — Sister scope LD01 Picard H10 + MANIFEST.md obligatoire

**Sister ADRs (même session 2026-06-21)** :
- `ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` (L2, AaaS Doctrine 3 variants × 4 leviers Solarpunk) — cite LD01 Picard H10 comme colonne vertébrale AaaS.
- `ADR-MEM-002_wiki-lifewheel-mapping-doctrine.md` (L1, Wiki ↔ Life Wheel mapping) — row LD01 = Business_Picard H10 projects owner.
- `ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md` (L0, Anti-Paperclip doctrine) — 7 hard-stop triggers avec audit owner LDxx-spécifiques.

**Amendment §D1 rationale** : L'analyse d'alignement 8 Domaines ↔ LD01 du 2026-06-21 a identifié que :
1. LD01_Business_Picard = H10 horizon, projects owner n'était pas formalisé comme doctrine (gap doctrinal).
2. MANIFEST.md obligatoire par projet (top-level du projet) n'était pas dans la convention (gap tooling).
3. La Picard ownership matrix (8 LDxx × A3 captain × project role) n'était pas ancrée dans l'INFRA-003 (gap structurel).

**Amendment outcome** : §D1 ci-dessus ancre LD01 Picard H10 + MANIFEST.md obligatoire + 8 LDxx Picard ownership matrix. D4 append-only = section ajoutée après §D1 original sans modification des sections D2-D7. **Pas de disruption de l'original ACCEPTED 2026-06-04** — extension forward-compatible.

**A0 ratification pending** : A0 doit ratifier l'amendment §D1 pour passer INFRA-003 de `ACCEPTED` à `ACCEPTED+AMENDED`. Sister ratification AAAS-001 + MEM-002 + SOBER-002 dans la même fenêtre.

**D7 cost-of-escalation respecté** : pas d'escalation mid-session, demande groupée post-Plan `fancy-hugging-bengio.md` §3 ratification.
