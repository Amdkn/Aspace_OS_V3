---
name: graphify-viewer
description: Navigate the corpus graph from one entry point. Use this skill whenever the user says "show me the graph", "what's in the corpus", "graph stats", "find node by id", "search by keyword", "top communities", "graphify corpus state", "master graph", or "graphify inventory". Pure file I/O against the master `graph.json` (203K nodes / 490K edges / 260 MB) merged by `graphify_master_merge.py`. No LLM calls. Read-only.
---

# graphify-viewer

## When to use

- A0 wants to inspect the full graphified corpus (master + 42 per-app junctions)
- Need to find a node by id, search by keyword, see top communities
- Quick health check on the corpus (parse OK, count, provenance)
- Look up "which app did this node come from?" via `app_source` annotation

## When NOT to use

- Single-file graph build (use `graphify <dir>` directly)
- Re-build / re-merge the corpus (use `graphify-swarm-burst` or `graphify_master_merge.py`)
- Full text search across the underlying .md (use `grep` / `ripgrep` directly)

## The corpus (D1 receipts 2026-06-16)

- **Master graph**: `C:\Users\amado\ASpace_OS_V2\graphify-out-master\graph.json`
  - **203 351 unique nodes** / **489 793 unique edges** / 260 MB
  - Merged from **46 unique sources** (junctions + canon roots)
  - Each node annotated with `app_source` = which junction/canon it came from
  - Junction in `.claude/memory/graphify-out-master/`
- **Per-junction graphs**: 42 in `.claude/memory/app-*` + `amadeus-*` + `biz-*` + `aspace-*`
- **Skill bundle** (`graphify-swarm-burst`): 4 scripts (swarm, merge, userspace, master_merge)

## Commands (no LLM, pure I/O)

```bash
# 1. Master corpus stats
python "C:/Users/amado/.claude/skills/graphify-viewer/scripts/viewer.py" stats

# 2. Top 10 communities (by node count)
python ".../viewer.py" communities

# 3. Find a node by exact id
python ".../viewer.py" find-node "abc-123"

# 4. Search nodes by keyword in label/name/path
python ".../viewer.py" search "symphony"

# 5. Top sources by node count
python ".../viewer.py" sources

# 6. Per-source breakdown with dedup stats
python ".../viewer.py" breakdown
```

All commands read the master `graph.json` and print to stdout. Streaming for big corpus (no full load into memory if avoidable).

## Local web server (browser-based visualization)

For interactive exploration, the skill ships a localhost HTTP server (pure stdlib) + a self-contained HTML viewer (vis-network.js from CDN).

### Start the server

```bash
python "C:/Users/amado/.claude/skills/graphify-viewer/local_server.py"
```

Then open **http://localhost:8765** in your browser. The server loads the master graph (254 MB) into memory at startup, builds community + source + keyword indexes, and serves filtered subsets on demand.

Env vars (all optional):
- `GRAPHIFY_PORT` (default 8765)
- `GRAPHIFY_HOST` (default 127.0.0.1)
- `GRAPHIFY_LOAD=0` for lazy load (build indexes on first request)

### Endpoints

| Endpoint | Returns |
|---|---|
| `GET /` | viewer.html (single-file, vis-network.js from CDN) |
| `GET /api/stats` | corpus counts + top 20 communities + top 20 sources |
| `GET /api/community/<id>?limit=N` | nodes + edges in one community (sample first N) |
| `GET /api/source/<name>?limit=N` | nodes + edges from one app source (sample first N) |
| `GET /api/search?q=<kw>&limit=N` | keyword search across node fields |
| `GET /api/node/<id>` | single node + its edges (lazy expand) |
| `GET /api/path?from=<id>&to=<id>` | shortest path via `graphify` CLI (delegated) |

### UI features

- **Stats bar** — total nodes / edges / communities / sources
- **Community selector** — top 20 communities, click `load` to render
- **Source selector** — top 20 sources, click `load` to render
- **Search box** — full keyword search, Enter to submit
- **Pan/zoom/click** — vis-network standard controls
- **Click node** — sidebar with full JSON + incoming/outgoing edges (clickable to focus)
- **Color by community** — each community gets a palette color
- **Lazy expansion** — clicking a node's neighbor fetches it on demand

### D6 lessons shipped (2026-06-16)

- **D6 int-cast fix**: `community` field is stored as `int` in master graph JSON, but URL passes string. Handler tries `int(cid)` first, falls back to string. Without this fix, `/api/community/0` returned empty.

## Anti-patterns (D6 root cause)

- ❌ Loading the full 260 MB master into a Python dict in one go — slow + memory. Use the JSON streaming reader in `viewer.py` (`ijson` or `orjson` chunked).
- ❌ Re-running master merge to "see the latest" — read the existing `GRAPH_REPORT.json` (written on each merge). Re-merge is destructive.
- ❌ Treating `app_source` as authoritative provenance — it's the junction name, not the file path inside that junction. For file-level provenance, read the junction's own `graph.json`.
- ❌ Asking "what's in the corpus?" without a target — the corpus is 203K nodes, too big to dump. Use `stats` → `communities` → `sources` first to orient.

## Outputs (canonical paths)

```
graphify-out-master/
├── graph.json              # MASTER (260 MB, 203K nodes, 490K edges)
├── GRAPH_REPORT.json       # per-source breakdown + top communities
└── .graphify-state.json    # incremental state (future: per-app mtime tracking)
```

Junction: `.claude/memory/graphify-out-master/` → `ASpace_OS_V2/graphify-out-master/`

## D1 verify checklist

- [ ] `graph.json` exists, parses as valid JSON, has `nodes[]` and `links[]` arrays
- [ ] `len(nodes) > 200_000` and `len(links) > 480_000` (sanity range)
- [ ] `app_source` field is set on every node (sample-check 10 random nodes)
- [ ] `GRAPH_REPORT.json` exists and lists all 46 sources
- [ ] No junction in `.claude/memory/` is broken (ls -la shows valid junction)

## Related

- `graphify-swarm-burst` — builds the per-junction graphs
- `graphify_master_merge.py` — produces the master + this viewer reads from it
- `wiki/hand_offs/handoff_graphify_burst_swarm_delegation_2026-06-16.md` — original delegation
- Junction: `.claude/memory/graphify-out/` exposes the merged graph
