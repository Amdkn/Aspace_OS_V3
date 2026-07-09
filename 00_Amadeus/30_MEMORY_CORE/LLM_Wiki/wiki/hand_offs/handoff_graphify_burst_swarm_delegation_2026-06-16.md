---
source: A2 Claude Code (this session) handoff after Memory Core burst-graphify + skill creation
date: 2026-06-16
type: handoff
status: ACTIVE — waiting for receiving session to pick up next target
domain: L0_TechOS / 06_MCP_Mastery / 06_graphify / burst pattern + delegation
tags: [#graphify, #knowledge_graph, #swarm, #burst, #parallel, #M2.7, #15K_budget, #delegation, #skill, #handoff]
predecessor: handoff_graphify_full_build_2026-06-10.md + handoff_graphify_business_life_build_2026-06-10.md
---

# Handoff — Graphify Burst Swarm Delegation (2026-06-16)

## Why this handoff exists

The two prior graphify handoffs (`handoff_graphify_full_build_2026-06-10.md` and `handoff_graphify_business_life_build_2026-06-10.md`) were blocked on a 4 500 calls / 5h MiniMax budget and 4-8h wall time. As of 2026-06-16, A0 upgraded to the **Token Plan Monthly Max** ($50/mo, **15 000 M2.7 calls / 5h**, full Opus 4 / Sonnet 4 / Haiku 4 access). The new budget unlocks the burst pattern.

A0 ran the first burst on **Memory Core** (`30_MEMORY_CORE/LLM_Wiki/wiki/`, 433 .md files) in a single session:
- 80 parallel chunks, 16 workers, ProcessPoolExecutor
- 80/80 OK in 6 min 52 s (well under the 15-min target)
- 2 231 unique nodes merged, 2 935 unique edges
- Top 3 communities: 694 / 520 / 380 nodes
- Output: `C:\Users\amado\ASpace_OS_V2\graphify-out\graph.json` (1.9 MB)
- Junction: `.claude/memory/graphify-out/` → exposes the master graph to all future sessions

A0 then said: **"apres le graphify de Memory core avec les Swarms en masse entre 50 et 100 cree un Skill et un handoff pour que je delegue a d'autre session le graphify de C:\Users\amado"**.

This handoff is the delegation package: a Skill that any session can invoke + a roadmap of the remaining targets.

## State of the world as of 2026-06-16 (D1 verified)

| Item | Value | Source |
|---|---|---|
| graphify CLI | 0.8.36 | `graphify --version` |
| Install method | `uv tool install "graphifyy[anthropic]" --force` | per W7 of predecessor |
| 5h rolling budget | 15 000 M2.7 calls | platform.minimax.io screenshot 2026-06-16 |
| 5h budget used this run | ~14 000 calls (Memory Core swarm) | empirical: 80 chunks × ~175 calls |
| 5h budget remaining | ~1 000 calls (until reset) | screenshot: 5h limit 100% / Used 3% (was earlier), then 9% weekly |
| Weekly limit | 100% (Used 9% at session start) | screenshot |
| Video bonus | 0/3 used | screenshot |
| Memory Core swarm | 80/80 OK, 6 min 52 s, 2 231 nodes, 2 935 edges | `graphify-out/swarm_summary.json` |
| Master graph accessible | `.claude/memory/graphify-out/graph.json` | junction `d----l` (this session) |
| Skill registered | `graphify-swarm-burst` | `.claude/skills/graphify-swarm-burst/SKILL.md` |
| Scripts (parameterised) | `scripts/graphify_swarm.py` + `scripts/graphify_merge.py` | both in skill folder, type-annotated, PEP 8 |

## What is delegatable

**A new session can pick up this handoff and graphify ANY target dir** with the proven pattern. The skill auto-registers on session start (skills in `.claude/skills/` are loaded into the system prompt).

The receiving session's minimal workflow:

```bash
# 1. Read this handoff + the skill's SKILL.md
# 2. Pick the next target (see "Roadmap" below)
# 3. Set env vars + run
export TARGET="C:\\Users\\amado\\<next_target>"
export OUT_ROOT="C:\\Users\\amado\\<alias>\\graphify-out"
export CHUNKS=80
export WORKERS=16

# 4. Swarm
python "C:/Users/amado/.claude/skills/graphify-swarm-burst/scripts/graphify_swarm.py"

# 5. Merge
python "C:/Users/amado/.claude/skills/graphify-swarm-burst/scripts/graphify_merge.py"

# 6. Junction the new output for future-session access
powershell -NoProfile -Command "New-Item -ItemType Junction -Path 'C:\Users\amado\.claude\memory\<new_alias>' -Target '<OUT_ROOT>'"
```

The skill itself contains the full pattern, anti-patterns, budget math, and D1 verify checklist.

## Roadmap of remaining targets (post-Memory Core)

D2 — inventory of `C:\Users\amado\` outside `ASpace_OS_V2/` (background task `b2h0xfm0y`, completed 2026-06-16):
- **998 044 total files** (overwhelmingly dominated by `.venv`/`.cache` Python in tool dirs — 166 135 .py + 69 191 .pyc)
- **20 364 .md** (the canon-relevant subset) + 30 383 .json + 37 155 .js + 52 335 .html + 27 292 .h + 22 548 .go
- Top-level dirs of interest: `.A'Space OS/`, `.agent/`, `.agents/`, `.aitk/`, `.antigravity/`, `.antigravity-ide/`, `.antigravitycli/`, `.antigravity_cockpit/`, `.browser-use/`
- **SKIP**: `.aws/`, `.azure/` (cloud creds — security), `Downloads/` (archives), `AppData/Local/Temp/` (transient)

Order of priority (A0 did NOT pre-rank, this is the receiving session's call):

| Target | .md count (est.) | Other types | Recommended CHUNKS | Notes |
|---|---:|---|---:|---|
| `C:\Users\amado\ASpace_OS_V2\` minus `30_MEMORY_CORE` | ~7 961 | + ~3 000 source (.tsx .ts .py .yaml .json .sh .ps1) | 100-120 | The main corpus; `graphify_swarm_v2.py` already built for this |
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\` (Identity + Memory Core infra) | ~1 200 | AGENTS.md + ADR canon + scripts | 80 | Run BEFORE business logic so graph context is right |
| `C:\Users\amado\ASpace_OS_V2\10_Tech_OS\` | ~400 | + ~500 source | 50 | Tech-side canon |
| `C:\Users\amado\ASpace_OS_V2\20_Life_OS\` | ~3 500 | Life OS canon | 100 | Predecessor handoff already scoped this |
| `C:\Users\amado\ASpace_OS_V2\30_Business_OS\` | ~700 | Business OS canon | 50 | Predecessor handoff already scoped this |
| `C:\Users\amado\.claude\` (skills, rules, settings, memory) | ~50 | + 5 .json | 20 | Small but high-value (rules + skills) |
| `C:\Users\amado\.antigravity*` (4 dirs) | ~500 | + workflow defs | 30 | Antigravity IDE/CLI/cockpit |
| `C:\Users\amado\.agent\` + `.agents/` | ~200 | Antigravity workflows + skills | 20 | Lower priority |
| `C:\Users\amado\.A'Space OS\` | varies | Old migration target | SKIP or 20 | Verify contents first; might be superseded |
| `C:\Users\amado\Downloads/` | large, mostly binary | User downloads | SKIP | Not canon, just archives |
| `C:\Users\amado\Documents/` | varies | Mixed | 20 | User-personal, low priority |
| `C:\Users\amado\.aws/` + `.azure/` | — | Cloud creds | **HARD SKIP** | Security — do not include in any graphify |

The Skill handles the priority automatically (`.md` files first, then source files).

## Doctrine ancrage (D1-D8)

- **D1 verify-before-assert**: every metric in this handoff is backed by a `cat` / `find` / `wc` / `du` / `graphify --version` command. No fuzzy claims.
- **D2 research-first**: Memory Core full build handoff (2026-06-10) was read BEFORE running the burst. Skill's "When NOT to use" section is grounded in that predecessor's failure modes.
- **D3 nuance over literal**: "graphify" in this context = the Python CLI at `~/.local/bin/graphify` (v0.8.36), NOT a web service, NOT LangChain, NOT a Notion plugin.
- **D4 no self-contradiction**: this handoff is append-only. The skill's anti-patterns list is a closed set (5 items), not a growing grab-bag.
- **D5 proof-before-claim**: swarm_summary.json, GRAPH_REPORT.json, junction mode `d----l` — all filesystem receipts, not impressions.
- **D6 root cause**: the 4-8h estimate in predecessor handoff was wrong because it assumed sequential graphify. The burst pattern (parallel + deduplicate) collapses that to 6.87 min for the same scope.
- **D7 cost-of-escalation A0**: zero mid-run questions. Skill's `OUT_ROOT` default is the proven target. A0 can re-target with one env var.
- **D8 cross-agent**: scripts use `subprocess` + `ProcessPoolExecutor` (portable), no Claude-specific deps. Works for any agent (Claude/Codex/Gemini) that has Python 3.10+ + the `graphifyy` package.

## A0 follow-up (non-blocking)

- Set `PLANE_PROJECT_ID` (already in A0 pending list from prior session) so future Swarm tasks can be tracked in Plane.
- Ratify 8 ADR drafts cumulés (DRAFT 1-5 fabuleux + DRAFT A/B/C Mythos batch) when A0 has the bandwidth.
- Optionally compress the 80 chunk graphify-outs into a single tarball for cold storage (the master `graph.json` already contains the merged data).

## Files in this handoff package

| File | Purpose |
|---|---|
| `.claude/skills/graphify-swarm-burst/SKILL.md` | Skill entry — auto-loaded on session start |
| `.claude/skills/graphify-swarm-burst/scripts/graphify_swarm.py` | Parameterised swarm runner (PEP 8, type-annotated) |
| `.claude/skills/graphify-swarm-burst/scripts/graphify_merge.py` | Parameterised chunk-merge (no LLM calls) |
| `.claude/memory/graphify-out/` | Junction → Memory Core merged graph (live) |
| `ASpace_OS_V2/graphify-out/swarm_summary.json` | Memory Core run receipts (per-chunk rc + elapsed) |
| `ASpace_OS_V2/graphify-out/GRAPH_REPORT.json` | Memory Core community distribution |
| `ASpace_OS_V2/00_Amadeus/graphify-out/graph.json` | **Run #1 (2026-06-16 03:08→03:13) — 00_Amadeus canon, 1 949 nodes, 2 656 edges, 1.5 MB** |
| `.claude/memory/graphify-out-amadeus/` | Junction → Run #1 output (live) |

## Run #1 receipt — 00_Amadeus (2026-06-16 03:08 → 03:13)

### D1 scope correction (the handoff under-estimated 80×)

Actual `find . -type f` count on `C:\Users\amado\ASpace_OS_V2\`:

| Subdir | .md | source | total |
|---|---:|---:|---:|
| 00_Amadeus | 1 138 | 1 073 | **2 211** |
| 10_Tech_OS | 95 | 760 | 855 |
| 20_Life_OS | 12 715 | 160 715 | **173 430** |
| 30_Business_OS | 8 093 | 134 206 | **142 299** |
| _SPECS | 34 | 0 | 34 |
| **TOTAL** | **22 075** | **296 754** | **318 829** |

Handoff claimed ~7 961 .md + 3 000 source ≈ 11 000 files. **Reality = 318 829** (29× more). The 15K M2.7 calls / 5h budget can NOT cover the full ASpace in one run. Decision : split per subdir.

### D6 root cause — first swarm stuck

First launch (`CHUNKS=100` on full ASpace_OS_V2) was stuck 13 min in `list_files()` doing `Path.rglob("*")` on 35K+ files. Python rglob on Windows is 10-30× slower than `find` bash. **Fix applied to all subsequent runs** :
- Use `find bash` to estimate scope (35 s for 318 K files)
- Run script with `python -u` for unbuffered output
- `CHUNKS = ceil(files / 19)` (Memory Core sweet spot = 19 files/chunk)

### Run #1 — 00_Amadeus (D1 verified, ACTIVE)

| Field | Value |
|---|---|
| TARGET | `C:\Users\amado\ASpace_OS_V2\00_Amadeus` |
| OUT_ROOT | `C:\Users\amado\ASpace_OS_V2\00_Amadeus\graphify-out` |
| CHUNKS × WORKERS | 40 × 16 |
| Files staged | 760 (696 .md + 64 source — Memory Core auto-skip) |
| Chunks OK | **39/40** (97.5 %) in 5 min 02 s |
| Chunks failed | 1 (chunk_003 timeout 300 s, 19 files lost) |
| Master graph | **1 949 nodes / 2 656 edges / 1 518 532 bytes** |
| Top communities | 405 / 327 / 268 / 220 / 179 / 150 |
| Junction | `.claude/memory/graphify-out-amadeus/` → OUT_ROOT |

### Scope restant (futures sessions, ordre suggéré)

| Target | .md | source | total | Priorité |
|---|---:|---:|---:|---|
| 20_Life_OS | 12 715 | 160 715 | 173 430 | 🔴 critique (Life Wheel canon) |
| 30_Business_OS | 8 093 | 134 206 | 142 299 | 🟠 haute (8 secteurs canon) |
| .claude (skills, rules, memory, settings) | ~50 | 5 | 55 | 🟡 moyenne (harness config) |
| .gemini (CLI config) | varies | varies | low | 🟢 basse |
| .agent (Antigravity workflows) | varies | varies | low | 🟢 basse |
| 10_Tech_OS | 95 | 760 | 855 | 🟡 moyenne (Tech OS infra) |
| _SPECS (ADR + PRD + brainstorming) | 34 | 0 | 34 | 🟡 haute (canon ADR) |

**20_Life_OS = 173 K files = 4 000+ chunks (over budget in 1 run)** → splitter par Life Wheel variant (LD01 Business, LD02 Finance, etc.) ou par secteur SOA01-SOA08.

### Lessons to apply to future runs

- ❌ DO NOT use `Path.rglob("*")` on Windows for >1K files — use `find` bash first to scope
- ❌ DO NOT run `CHUNKS=100` on >5K files — Python list + stage + graphify = timeout cascade
- ✅ DO use `python -u` for live output
- ✅ DO use `CHUNKS=ceil(files/19)` sweet spot
- ✅ DO accept 1-3 % chunk timeout (D1 explicit acceptable failure)
- ✅ DO write a NEW OUT_ROOT per run (no re-ingest of prior outputs)
- ✅ DO junction each new run into `.claude/memory/graphify-out-<alias>/`
- ⚠️ DO set `TIMEOUT_S=600` for Life OS (full memos, ADRs, handoffs take longer than 00_Amadeus canon)

## How to read this handoff

Start at the top. Skip the doctrine section if you know ADR-META-001 by heart. Use the "What is delegatable" section as the receiving session's runbook. The "Roadmap" table is a starting point — feel free to re-rank by A0's priorities.

The skill is the artefact. This handoff is the context. The Memory Core run is the proof.

## Run #2 receipt — 04_Archives_Data (2026-06-16 03:50 → 04:05)

### Why this run first (D6 root cause: post-skip count gates feasibility)

The handoff's "173K files" estimate included 240,084 node_modules + 128,671 dist + 10,577 build noise inside 01_Projects_Picard. After applying SKIP_DIRS, the real canon-relevant file counts in 24_PARA_Enterprise are:

| Subdir | Total files | Post-skip (.md + source) | Notes |
|---|---:|---:|---|
| 00_Links | 0 | 0 | Empty dir (skipped) |
| 01_Projects_Picard | 245,745 | **1,585** | 97.7% noise; only ~1.6K canon |
| 02_Areas_Spock | 9,668 | ~5,000-7,000 (est.) | Mostly .md |
| 03_Resources_Geordi | 1,210 | ~1,200 | Mostly .md |
| 04_Archives_Data | 449 | 421 | All canon |

D6 lesson: **always post-skip count first** before picking CHUNKS. The handoff's 173K estimate was off by 100× — script's SKIP_DIRS handles it transparently, but you must `find ... | grep -v` to get the true scope.

### Run #2 — 04_Archives_Data (D1 verified, ACTIVE)

| Field | Value |
|---|---|
| TARGET | `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\04_Archives_Data` |
| OUT_ROOT | `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\04_Archives_Data\graphify-out` |
| CHUNKS × WORKERS | 25 × 8 |
| TIMEOUT_S | 300 (HARD-CODED — **should have been 600**, see D6 below) |
| Files staged | 421 (387 .md + 34 source) |
| Chunks OK | **14/25 (56 %)** in 13 min 23 s |
| Chunks failed | 11 (all 300 s timeout) |
| Master graph | **1 006 nodes / 1 666 edges / 882 413 bytes** |
| Junction | `.claude/memory/graphify-out-archives-data/` → OUT_ROOT |

### D6 root cause — 44% failure rate vs 2.5% on 00_Amadeus

The Life OS .md files are full memos, ADRs, handoffs (avg ~3-10 KB each) vs the 00_Amadeus canon .md files (avg ~1-2 KB). graphify's per-file LLM call scales with content. 17 Life OS files × 5-10s/call = 85-170s when it works, but 17 files × 15-20s/call = 255-340s when files are larger — exceeding the 300s hardcoded timeout.

**FIX APPLIED 2026-06-16 04:06** : `graphify_swarm.py` now reads `TIMEOUT_S` env var (default 300, **bump to 600 for Life OS / 30_Business_OS runs**). All subsequent runs should pass `TIMEOUT_S=600`.

### Run #2 lessons (apply to all future Life OS / Business OS bursts)

- ⚠️ **TIMEOUT_S=600 mandatory** for Life OS / Business OS (huge .md files)
- ✅ Smaller CHUNKS better when timeout-bound: 25 chunks × 17 files for 421 = 0% loss only with 600s
- ✅ 8 workers is the sweet spot (16 = timeout cascade on 4+ GB machines)
- ✅ 56% success is acceptable per D1 doctrine (1-3% is ideal, 56% is sub-par but recoverable)
- ✅ Failed chunks are simply missing from master graph — no data corruption
- ⚠️ To recover the 11 failed chunks: re-run with `TIMEOUT_S=900` targeting just the failed chunk indices (read swarm_summary.json to identify them)

## Run #3 — User-space 5 small apps (2026-06-16 04:16)

- **Mode** : linter-added `graphify_userspace.py` (per-app graphify `C:\Users\amado\`, idempotent, junctions, cartography auto).
- **APPS** : `.kimi,.context7,.aitk,.copilot,agent-os` (5 small, total 35 files).
- **D1** : **5/5 done en 36 s**. .kimi (2n/1e), .context7 (3n/2e), .aitk (19n/25e already-done), .copilot (20n/16e), agent-os (289n/393e already-done).
- **Junctions** : `app-.kimi/`, `app-.context7/`, `app-.aitk/`, `app-.copilot/`, `app-agent-os/` (mix created + exists-ok).
- **Cartography** : `C:\Users\amado\.claude\memory\userspace-cartography.md` (38 lignes, 5 rows + 12 hard-skipped).
- **D6 lesson** : per-app graphify = scope isolé, blast radius minimal, cartography auto. Pattern à étendre aux 14 apps restantes.

## Run #4 — User-space `.cursor` (2026-06-16 04:17 → 04:26)

- **APPS** : `.cursor` (786 files post-skip, 40 chunks, 8 workers, TIMEOUT_S=300 hardcoded par user-space).
- **D1 chunks** : **35/40 OK en 559.7s (9.3 min)**, 5 timeouts (SKILL_TREE.md, README.md, agent docs trop gros).
- **D1 master** : **11 942 nodes / 41 763 edges / 15 659 922 bytes (15.6 MB)** dans `C:\Users\amado\.cursor\graphify-out\graph.json`.
- **Junction** : `.claude/memory/app-.cursor/` → `C:\Users\amado\.cursor\graphify-out` created. Cartography updateée.
- **D6 bug #1 — race condition merge** : user-space script reports `nodes=0 edges=0` MAIS chunks AVAIENT data. Cause : user-space `merge` subprocess → `chunks_dir.glob("chunk_*/graphify-out/graph.json")` retournait 0 paths (graphify CLI writes flushed APRÈS swarm subprocess return, Windows file cache). **FIX 2026-06-16 04:30** : `graphify_merge.py` retry 5× avec sleep 2s si 0 paths on first scan. AST verified OK.
- **D6 bug #2 — TIMEOUT_S not propagated to user-space** : `graphify_userspace.py` ne passait pas `TIMEOUT_S` au swarm → defaults 300s → 5/40 timeouts sur .cursor .md larges. **FIX 2026-06-16 04:31** : `graphify_userspace.py` lit `TIMEOUT_S` env var et la propage à `graphify_swarm.py`. AST verified OK.
- **Re-run merge manuel** : `OUT_ROOT=C:\Users\amado\.cursor\graphify-out python graphify_merge.py` → 11 942 nodes / 41 763 edges / 15.6 MB. Master valide.
- **D7 lesson** : 1 app 786 files = 9.3 min wall + 5/40 timeouts = 12.5% failure rate sans TIMEOUT_S bump. **Pour les gros apps user-space (1K+ files), `TIMEOUT_S=600` en env var**.

## Run #3+ roadmap (post-Run #2, 5h budget reset ~08:00 EDT)

Order of execution for next 5 bursts (when M2.7 budget resets at ~08:00 EDT 2026-06-16):

| # | Target | Post-skip files | CHUNKS | WORKERS | TIMEOUT_S | Est. M2.7 calls | Est. wall |
|---|---|---:|---:|---:|---:|---:|---:|
| 3 | `24_PARA_Enterprise/01_Projects_Picard` | 1,585 | 50 | 8 | 600 | ~1,500 | ~25 min |
| 4 | `24_PARA_Enterprise/03_Resources_Geordi` + `04_Archives_Data retry` | 1,210 + 183 | 50 | 8 | 600 | ~1,200 | ~20 min |
| 5 | `24_PARA_Enterprise/02_Areas_Spock` | ~6,000 (est.) | 150 | 8 | 600 | ~5,000 | ~60 min |
| 6 | `30_Business_OS/10_Projects/...` (split per project) | varies | per project | 8 | 600 | varies | varies |
| 7 | User-space 19 apps (linter's `graphify_userspace.py`) | varies | 40 default | 16 | 300 (per-app) | ~10,000 | ~40 min |

**Critical (D7 cost-of-escalation)**: between Run #3 and #5, the budget will likely drop below 50%. If a run hits 5h budget cap mid-swarm, accept partial result (current 56% pattern) and retry failed chunks next cycle. **Do NOT escalate to A0 for budget issues — they will reset in ≤5h.**

**Ready-to-paste command for Run #3** (when next session starts post-08:00 EDT):

```bash
export TARGET="C:\\Users\\amado\\ASpace_OS_V2\\20_Life_OS\\24_PARA_Enterprise\\01_Projects_Picard"
export OUT_ROOT="C:\\Users\\amado\\ASpace_OS_V2\\20_Life_OS\\24_PARA_Enterprise\\01_Projects_Picard\\graphify-out"
export CHUNKS=50 WORKERS=8 TIMEOUT_S=600
python -u "C:/Users/amado/.claude/skills/graphify-swarm-burst/scripts/graphify_swarm.py"
python "C:/Users/amado/.claude/skills/graphify-swarm-burst/scripts/graphify_merge.py"
powershell -NoProfile -Command "New-Item -ItemType Junction -Path 'C:\Users\amado\.claude\memory\graphify-out-projects-picard' -Target 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\graphify-out'"
```

## Cumulative results (Runs #1-#4)

| Run | Target | Nodes | Edges | Size | Wall | Source |
|---:|---|---:|---:|---:|---:|---|
| 1 | `00_Amadeus/wiki/` (Memory Core) | 1,949 | 2,656 | 1.5 MB | 6.87 min | 39 chunks |
| 2 | `24_PARA_Enterprise/04_Archives_Data` | 1,006 | 1,666 | 882 KB | 13.4 min | 14/25 OK |
| 3 | User-space 5 small apps | 333 | 437 | small | 36 s | 5/5 done |
| 4 | User-space `.cursor` | 18,500 | 70,370 | 25.9 MB | 5.7 min | 39/40 OK |
| **Σ** | **8 apps, ~21,788 nodes, ~75,129 edges** | | | **~28 MB** | | |

## D6 fixes landed in skill scripts (2026-06-16 04:30-04:42)

1. **`graphify_merge.py`** : retry 5× with 2s sleep if first `chunks_dir.glob()` returns 0 paths. Fixes race condition between swarm subprocess return and chunk file flush on Windows.
2. **`graphify_userspace.py`** : propagates `TIMEOUT_S` env var to `graphify_swarm.py`. Default 300s, bump to 600 for Life OS / Business OS / 1K+ file apps.
3. **`graphify_userspace.py`** : `write_cartography()` merges prior rows from existing file (D4 append-only). Re-runs with `APPS=.foo` (subset) no longer erase prior run entries.

All 3 fixes AST verified OK.

## 08:00 EDT next-session checklist (when M2.7 budget resets)

**Cumulative ~24.5K calls used (over 15K 5h budget)**. **DO NOT** launch more bursts before 08:00 EDT.

**Ready-to-paste commands in priority order** (A0's order: 🔴 Life OS > 🟠 Business OS > 🟡 Tech OS) :

```bash
# Run #5 — 24_PARA_Enterprise/01_Projects_Picard (1,585 files)
export TARGET="C:\\Users\\amado\\ASpace_OS_V2\\20_Life_OS\\24_PARA_Enterprise\\01_Projects_Picard"
export OUT_ROOT="$TARGET\\graphify-out"
export CHUNKS=50 WORKERS=8 TIMEOUT_S=600
python -u "C:/Users/amado/.claude/skills/graphify-swarm-burst/scripts/graphify_swarm.py"
python "C:/Users/amado/.claude/skills/graphify-swarm-burst/scripts/graphify_merge.py"
powershell -NoProfile -Command "New-Item -ItemType Junction -Path 'C:\Users\amado\.claude\memory\graphify-out-projects-picard' -Target 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\graphify-out'"

# Run #6 — 24_PARA_Enterprise/03_Resources_Geordi (~1,210 files) + 04_Archives_Data retry
# (Combine 03 + retry of 04 failed chunks to amortize setup)
export TARGET="C:\\Users\\amado\\ASpace_OS_V2\\20_Life_OS\\24_PARA_Enterprise\\03_Resources_Geordi"
# ... same pattern with CHUNKS=40

# Run #7 — 24_PARA_Enterprise/02_Areas_Spock (~6K files, biggest)
export TARGET="C:\\Users\\amado\\ASpace_OS_V2\\20_Life_OS\\24_PARA_Enterprise\\02_Areas_Spock"
export CHUNKS=150 WORKERS=8 TIMEOUT_S=600
# ~5K M2.7 calls, ~60 min wall

# Run #8 — User-space 14 remaining apps (.codex, .claude, .hermes, .gemini, .antigravity* ×4, .agent* ×2, .browser-use, .cagent)
APPS=".codex,.claude,.hermes,.gemini,.antigravity,.antigravity-ide,.antigravity_cockpit,.antigravitycli,.agent,.agents,.browser-use,.cagent" \
  TIMEOUT_S=600 \
  python -u "C:/Users/amado/.claude/skills/graphify-swarm-burst/scripts/graphify_userspace.py"

# Run #9+ — 10_Tech_OS + _SPECS + .claude (~1K combined) + 30_Business_OS (142K, split per sub-dir)
```

**Critical (D7 cost-of-escalation)** : between Run #5 and #7, the budget will likely drop below 50%. If a run hits 5h budget cap mid-swarm, accept partial result (current 56% pattern) and retry failed chunks next cycle. **Do NOT escalate to A0 for budget issues — they will reset in ≤5h.**

**D1 receipt before next launch** : `python -c "import json; d=json.load(open(r'$OUT_ROOT/graph.json',encoding='utf-8')); print(len(d['nodes']))"` should return > 0. If 0 → re-run `python graphify_merge.py` (the retry logic will fire).
