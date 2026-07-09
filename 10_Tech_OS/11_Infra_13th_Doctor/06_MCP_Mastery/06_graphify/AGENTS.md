# 06_graphify — DOX leaf for the graphify MCP/CLI

> Parent: `../AGENTS.md`. Framework: `../../06_MCP_Mastery_dox/AGENTS.md`.
> Repo: https://github.com/safishamsi/graphify (branch v8, 64,7k ⭐, 28 tree-sitter grammars).
> PyPI: `graphifyy` (the binary is `graphify`).
> Canon: vault = no token of its own. Uses existing `ANTHROPIC_API_KEY` + `ANTHROPIC_BASE_URL=https://api.minimax.io/anthropic` (MiniMax-M3).

## Purpose

Graphify is the **structural / cross-cutting knowledge graph** plane of A'Space OS. It pre-builds
a queryable map of the entire repo (code + ADRs + SDDs + wikis + skills) so agents can answer
"what connects X to Y?" without re-deriving. It's the 6th MCP in the dox tree — the only one
that's **read-mostly + project-wide**; the other 5 (hostinger/github/dokploy/vercel/supabase)
are vertical/silo.

Use cases (mapped 2026-06-10):
- Replace text-dump `wiki/index.md` with a clickable graph view.
- Auto-discover AGENTS.md cross-refs that the manual `Child DOX Index` misses.
- Donna DLQ root-cause tracing via `shortest_path`.
- Cross-OS (L0/L1/L2) unified view via `graphify global add/list/remove`.
- Cold-start accelerator: `GRAPH_REPORT.md` as a session-startup asset.

## Ownership

- A0 Amadeus — approves new graph builds, schema changes, vendor upgrades.
- A2 Claude Code — orchestrates graph build / query / re-build.
- A3 sub-agent — runs `graphify` and `mcp__graphify__*` calls.

## Local Contracts

### Auth

- No dedicated token. Reuses `ANTHROPIC_API_KEY` (env User Windows) + `ANTHROPIC_BASE_URL` =
  `https://api.minimax.io/anthropic` (MiniMax-M3 Anthropic-compat endpoint).
- LLM backend is **Claude / Anthropic-compat** (per A0's choice 2026-06-10).

### Capabilities (verified 2026-06-10)

| Tool | Use |
|------|-----|
| `graphify .` | Build graph at repo root |
| `graphify ./docs --update` | Incremental re-extract (changed files only) |
| `graphify query "..."` | Natural-language query over the graph |
| `graphify path "A" "B"` | Shortest path between 2 nodes |
| `graphify explain "node"` | All edges + neighbors of a node |
| `graphify prs --triage` | AI-ranked PR review queue (Donna DLQ pattern) |
| `graphify global add <path>` | Add a sub-graph to the cross-project global graph |
| `mcp__graphify__*` | Same as above, exposed via MCP server (stdio or HTTP) |

### Build outputs (in `graphify-out/`)

- `graph.html` — interactive browser view (D3.js, clickable nodes).
- `GRAPH_REPORT.md` — key concepts + surprising connections + suggested questions.
- `graph.json` — full graph (programmatic query).
- `manifest.json` — portable metadata (commit this).
- Optional: `graph.svg`, wiki export, Obsidian vault, GraphML, Neo4j cypher.

### Ignore policy

- `graphify-out/` and `graph.json` are **gitignored** (per root `.gitignore`).
- `manifest.json` and `GRAPH_REPORT.md` SHOULD be committed (small, useful for cold-start).
- `.graphifyignore` (when needed) is the **explicit** filter; falls back to `.gitignore`.

## Work Guidance

### W1 — Always update, never full rebuild

```bash
# Default: incremental (only changed files since last build):
graphify . --update
# Full rebuild only when: schema change, .graphifyignore change, or first build:
graphify .
```

### W2 — Python 3.13 cap for Leiden

`graphifyy[leiden]` requires **Python <3.13** for community detection. Current system is
**3.14.2** — install Leiden extras only if you have a separate 3.10–3.12 venv. Core
graphify works on 3.14.

### W3 — Scope discipline (A0 chose "ASpace_OS_V2 entier" on 2026-06-10)

Verified canon-only = **13 658 files** (after node_modules/.git/_TRASH/.next/dist/build
exclusion via root `.gitignore`). First build on this scope: 5–15 min expected.

**Calibration from 1-file test (2026-06-10)**: 1 small doc (4.3 KB) = 32 nodes, 42 edges,
~1 min wall time (LLM call), $0.07 cost via MiniMax-M3. Linear extrapolation to 13 658 files
= **~$910 lower bound** and **hours of wall time** with `--max-concurrency 4` default.
The full build's actual cost will be tracked in the run logs (cost.json in graphify-out/).

If a future build exceeds 30 min: scope down via `.graphifyignore` (e.g. scope to
`10_Tech_OS + _SPECS` for L0 only, or to one `30_Business_OS/10_Projects/<proj>` for
a single app).

### W4 — Destructive ops

- `graphify .` (full rebuild) — auto-approved (overwrites `graphify-out/`, no upstream effect).
- `rm -rf graphify-out/` — auto-approved.
- `graphify global add <path>` — **HITL**. Affects the cross-project global graph.
- `graphify hook install` — **HITL**. Modifies `.git/hooks/post-commit` and the union-merge driver.
- `mcp__graphify__*` — read-only ops auto-approved; write/delete ops HITL.

### W5 — Cold-start recipe

```bash
# At session start (if graphify-out/ is fresh):
ls graphify-out/GRAPH_REPORT.md && head -200 graphify-out/GRAPH_REPORT.md
# Read this BEFORE any /graphify . rebuild, to leverage prior knowledge.
```

### W6 — LLM backend config

graphify auto-detects `ANTHROPIC_API_KEY` + `ANTHROPIC_BASE_URL` from env. No config file
needed. To force a different backend: `graphify . --llm openai` (or `gemini`, `ollama`,
`bedrock`).

### W7 — Install gotcha (the [anthropic] extra is NOT optional)

**Discovered 2026-06-10** during the first build attempt: `uv tool install graphifyy` installs
the CLI but **not** the `anthropic` Python SDK. Every semantic chunk then fails silently
with `"the 'anthropic' package is required for this backend"`. The CLI buffers stdout, so
the failure is invisible until the run completes with empty `graphify-out/`.

**Correct install** (one shot):

```bash
uv tool install "graphifyy[anthropic]" --force
# Verify SDK is present:
uv tool run --from "graphifyy[anthropic]" python -c "import anthropic; print(anthropic.__version__)"
```

**Why `--force`**: uv locks the tool's `Scripts/` dir while any `graphify.exe` or
`python.exe` from the previous venv is still running. If a previous build is hung in
background, `taskkill /F /PID <graphify.exe pid> /PID <python.exe pid>` first, then
reinstall. Symptom of a stuck lock: `os error 5` on
`C:\Users\amado\AppData\Roaming\uv\tools\graphifyy\Scripts`.

**Symptom of the missing SDK** (D6 — exact command to detect): run on a 1-file scope:

```bash
mkdir -p /tmp/gtest && echo "# hello" > /tmp/gtest/x.md
cd /tmp/gtest && graphify extract . --no-cluster 2>&1 | tail -10
# If SDK missing: "the 'anthropic' package is required..." + "all semantic chunks failed"
# If SDK present: "wrote graphify-out/graph.json — N nodes, M edges"
```

## Verification

```bash
# Confirm install (MUST use the [anthropic] extra per W7):
uv tool install "graphifyy[anthropic]" --force
graphify --version
# Expect: 0.8.x or similar (v8 branch is active dev; pin version in `requirements.txt` when shipping)

# Confirm LLM reachability (smoke test before full build):
graphify . --dry-run 2>&1 | grep -i "llm\|backend\|model"
# Expect: anthropic / claude / claude-3-5-sonnet (or whatever MiniMax maps to)

# Confirm outputs after build:
ls -la graphify-out/ | grep -E "graph\.html|GRAPH_REPORT|graph\.json|manifest"
# Expect: 4 files, sizes 1 KB – 100 MB
```

## Child DOX Index

This leaf has no sub-domains yet. If "build" vs "query/MCP" vs "global graph" become
separate concerns, split here (e.g. `06a_build_pipeline/`, `06b_mcp_query/`).
