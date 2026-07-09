---
name: graphify-swarm-burst
description: Burst-graphify a large target directory using parallel graphify CLI workers + chunk merge. Use this skill whenever the user says "graphify", "build a knowledge graph", "structure this folder", "swarm graphify", "burst graphify", "graphify in parallel", "graphify my user space", "graphify C:\\Users\\amado", or wants to process 100s-1000s of files into a single merged graph.json. Proven on Memory Core: 80 chunks in 6.87 min, 2231 nodes, 2935 edges, fits inside the 15K M2.7/5h budget. Includes a user-space mode (`graphify_userspace.py`) that per-app graphifies the C:\\Users\\amado root, idempotently creates junctions in `.claude/memory/`, and auto-writes a cartography to `.claude/CLAUDE.md`. **Anti-pattern guard**: NEVER generalize an app name to a concept — `agent-os` is the app at `C:\\Users\\amado\\agent-os\\` (with `commands/`, `config.yml`, `profiles/`, `scripts/`, `standards/`), NOT a category.
---

# graphify-swarm-burst

## When to use

- Target dir has **100+ files** and the user wants a knowledge graph.
- User mentions "swarm", "burst", "parallel", or "M2.7 budget" / "15K requests".
- User has already used `graphify` once for a calibration run (handoffs: `handoff_graphify_full_build_2026-06-10.md` and `handoff_graphify_business_life_build_2026-06-10.md`).
- User wants the result merged into ONE master `graph.json` (not 80 separate chunk graphs).

## When NOT to use

- Single-file or 1-10 file targets — run `graphify <dir>` directly, no swarm needed.
- No `graphify` CLI installed — install with `uv tool install "graphifyy[anthropic]" --force` first (see `wiki/hand_offs/handoff_graphify_full_build_2026-06-10.md` for the full install path).
- No M2.7/M3 budget remaining (5h rolling window at 100%) — wait for reset.

## The pattern (4 steps, ~10 min per 80-chunk run)

### Step 1 — Pick the target + output

```bash
export TARGET="C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE"  # example
export OUT_ROOT="C:\\Users\\amado\\ASpace_OS_V2\\memory-core-graphify-out"
export CHUNKS=80        # 80 chunks × ~5 files = ~400 files per pass
export WORKERS=16       # capped per CLAUDE.md (cpu cores - 2)
export TIMEOUT_S=300    # per-chunk graphify timeout (default 300; **600 for Life OS / Business OS**)
```

D2 — verify the target exists + estimate file count before launching.

### Step 2 — Swarm (parallel chunk graphify)

```bash
python "C:/Users/amado/.claude/skills/graphify-swarm-burst/scripts/graphify_swarm.py"
```

The script:
1. Lists `*.md` (priority) + source files (`.ts .tsx .py .yaml .json .sh .ps1`) under `$TARGET`
2. Excludes `node_modules, .git, .next, .obsidian, .venv, dist, build, __pycache__, graphify-out, aspace-graphify-out, chunks, Graphviz, logs, .claude, $OUT_ROOT`
3. Round-robin partition into `$CHUNKS` buckets
4. Spawns `$WORKERS` parallel `ProcessPoolExecutor` workers, each running `graphify <chunk_dir> -o <chunk_dir>/graph.json`
5. Writes `$OUT_ROOT/swarm_summary.json` with per-chunk elapsed time + rc

Proven results (Memory Core, 2026-06-16, $TARGET = wiki/):
- 80/80 chunks OK in 412.2 s (6.87 min)
- 214 files processed (graphify auto-skips empty/short)
- 2 231 unique nodes merged, 2 935 unique edges
- Within 15K M2.7/5h budget

### Step 3 — Merge

```bash
python "C:/Users/amado/.claude/skills/graphify-swarm-burst/scripts/graphify_merge.py"
```

Pure file I/O (no LLM calls). Reads each `chunks/chunk_NNN/graphify-out/graph.json`, deduplicates nodes by `id` and edges by `(source, target, key)`, writes `$OUT_ROOT/graph.json` (1.9 MB master) + `$OUT_ROOT/GRAPH_REPORT.json` (community counts).

### Step 4 — Verify (D1 receipts)

```bash
ls -la "$OUT_ROOT"          # expect graph.json + GRAPH_REPORT.json + chunks/ + swarm_summary.json
python -c "import json; d=json.load(open(r'$OUT_ROOT/GRAPH_REPORT.json',encoding='utf-8')); print(d)"
```

## Budget math (M2.7 5h rolling window)

| Target size | Chunks | Workers | Wall time | Est. M2.7 calls |
|---|---:|---:|---:|---:|
| ~400 files | 80 | 16 | ~7 min | ~14 000 |
| ~2 000 files | 80 | 16 | ~15 min | ~14 000 (parallel) |
| ~10 000 files | 120 | 16 | ~25 min | ~21 000 (over budget, split into 2 runs) |

The 5h window holds all 15 000 calls. Bursting within a 15-min wall-clock is possible because 16 workers run in parallel and the bottleneck is API rate, not CPU.

## Anti-patterns (D6 root cause)

- ❌ Re-ingesting `graphify-out/` → 0 nodes, doubles the work, wastes budget. **Excluded by SKIP_DIRS** — verify with `find $TARGET -name "graph.json" | wc -l` before launch.
- ❌ Re-running on already-graphified files → re-processes. Use a NEW `$OUT_ROOT` for each pass.
- ❌ Running `graphify` once on the whole target → exceeds single-call timeout on 100+ files, no parallelism.
- ❌ Spawning 100+ workers → CLAUDE.md caps at `min(16, cpu cores - 2)`. More workers = more contention = slower, not faster.
- ❌ Skipping the merge step → 80 separate graphs, no master to feed downstream consumers.
- ❌ Forgetting `TIMEOUT_S=600` on Life OS / Business OS / 30_Business_OS .md-heavy dirs → 44% chunk timeout (Run #2 lesson 2026-06-16).
- ❌ **Trusting user-space script's `nodes=0` report** without manual `chunks_dir.glob()` verification. Race condition between swarm subprocess return and chunk file flush on Windows → merge sees 0 paths. **FIX** : `graphify_merge.py` retries 5× with 2s sleep if first scan returns 0. If `nodes=0` after retry → D1 verify by listing `chunks/*/graphify-out/graph.json` and re-run merge manually with `OUT_ROOT` set.
- ❌ **Forgetting `TIMEOUT_S=600` on user-space mode for apps with 1K+ files** → 5/40 .cursor chunks timed out at 300s (Run #4 lesson 2026-06-16). `graphify_userspace.py` propagates `TIMEOUT_S` env var to swarm as of 2026-06-16 04:31.
- ❌ **Re-running user-space with `APPS=.foo` (subset) overwrites the cartography**, losing prior run entries. **FIX 2026-06-16 04:42** : `write_cartography()` merges prior rows from existing file (D4 append-only). Always re-run with the FULL app list, or trust the merge logic.

## Outputs (canonical layout under `$OUT_ROOT`)

```
$OUT_ROOT/
├── graph.json              # MASTER — merged, deduplicated, 1.9 MB for Memory Core
├── GRAPH_REPORT.json       # node/edge counts + community distribution
├── swarm_summary.json      # per-chunk rc + elapsed_s, for debugging
└── chunks/
    ├── chunk_000/
    │   ├── <staged files>
    │   └── graphify-out/
    │       ├── graph.json
    │       ├── manifest.json
    │       └── cache/
    ├── chunk_001/...
    └── chunk_079/...
```

The `$OUT_ROOT` is meant to be **junctioned** into `.claude/memory/` (doctrine no-duplication):

```bash
powershell -NoProfile -Command "New-Item -ItemType Junction -Path 'C:\Users\amado\.claude\memory\<alias>' -Target '$OUT_ROOT'"
```

Example (done 2026-06-16): `.claude/memory/graphify-out` → `C:\Users\amado\ASpace_OS_V2\graphify-out`.

## D1 verify checklist before reporting success

- [ ] `$OUT_ROOT/graph.json` exists, parses as valid JSON, has `nodes[]` and `links[]` arrays
- [ ] `len(nodes) > 0` and `len(links) > 0` (no empty graphs)
- [ ] `swarm_summary.json` `summary.failed == 0`
- [ ] `GRAPH_REPORT.json` `unique_nodes` matches master `len(graph.json.nodes)` after merge
- [ ] All 80 chunk dirs have `graphify-out/graph.json` (or however many chunks the run used)

## User-Space Mode — `graphify_userspace.py` (idempotent per-app)

When the target is `C:\Users\amado\` (the user-space root), do NOT burst-graphify the whole tree in one go — it's 998K+ files and dwarfs the 5h budget. Instead, graphify **each top-level app individually** with idempotency built in.

### When to use user-space mode

- User says "graphify my user space", "graphify C:\Users\amado", "cartography of my apps", or "structure my installs"
- User wants a list of installed apps (cartography)
- Re-running the skill (idempotency = re-run updates rather than recreates)

### The pattern

```bash
# 1. Per-app graphify (idempotent — skips apps already done)
python "C:/Users/amado/.claude/skills/graphify-swarm-burst/scripts/graphify_userspace.py"

# 2. Custom app list
APPS="agent-os,.claude,.antigravity" python "C:/Users/amado/.claude/skills/graphify-swarm-burst/scripts/graphify_userspace.py"

# 3. Cartography is auto-written to .claude/memory/userspace-cartography.md
# 4. Each app's graph is junctioned to .claude/memory/app-<safe-name>/
```

### Idempotency rules (D4 no-self-contradiction)

- If `<app>/graphify-out/graph.json` already exists with `nodes > 0` → skip, just verify junction
- If junction `.claude/memory/app-<name>/` already points to the right target → no-op
- If junction exists but points to the wrong target → recreate
- Cartography is always OVERWRITTEN (the table reflects current state, not history)

### Per-app heuristic (no swarm if small)

- `< 5 files` in app → run `graphify <app_dir>` directly, no swarm
- `5-100 files` → swarm with `CHUNKS=ceil(files/19)` (e.g., 60 files → 4 chunks)
- `100+ files` → swarm with `CHUNKS=40` (proven budget) or 80 for very large apps

### Hard-skipped apps (credentials / caches / user data)

`.aws`, `.azure`, `.docker`, `.bun`, `.chocolatey`, `.mcp-auth`, `.cache`, `.local`, `.claude-server-commander`, `.claude-server-commander-logs`, `Downloads`, `Documents`. **NEVER graphify** — these contain credentials, caches, or user-private data.

### Anti-pattern guard (D3 nuance)

- ❌ Treating `agent-os` as a concept (Brian Casel philosophy) instead of the SPECIFIC installed app at `C:\Users\amado\agent-os\`
- ❌ Confusing Agent OS with LangChain, Fabuleux-tiers, OpenAI AgentOS, or any other "agent framework" — they are different installs, in different dirs, and may not even exist on this machine
- ❌ Asking "what is Agent OS" when the user has a `C:\Users\amado\agent-os\` directory — read the directory first
- ✅ `agent-os` = the app at `C:\Users\amado\agent-os\` with `commands/`, `config.yml`, `profiles/`, `scripts/`, `standards/`. Nothing more, nothing less.

## TTS handoff

After the swarm + merge, write the D1 receipts to `C:\Users\amado\AppData\Local\Temp\last_tts.txt` so the Stop hook speaks them. 30-sec summary:

```
Graphify swarm fini. Quatre-vingts chunks sur quatre-vingts. Six minutes quatre-vingt-douze. Deux mille nœuds fusionnés. Junction en place. Budget OK.
```

## Related

- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_graphify_full_build_2026-06-10.md` — original 13k-file plan (pre-burst)
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_graphify_business_life_build_2026-06-10.md` — Business OS + Life OS scoped
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_graphify_burst_swarm_delegation_2026-06-16.md` — this run + delegation handoff
- Junction: `.claude/memory/graphify-out/` exposes the merged graph for all future sessions
