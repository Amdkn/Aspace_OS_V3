"""
graphify_master_merge.py — Merge ALL per-app graph.json (junctions + canon roots)
into ONE master graph.json. Pure file I/O, no LLM calls.

Output: $MASTER_OUT_ROOT/graph.json + GRAPH_REPORT.json
Idempotent. Re-run = re-read all sources + rewrite master. No destructive ops.

Source discovery:
  1) .claude/memory/ junctions (app-*, amadeus-*, biz-*, aspace-*)
  2) Known canon roots under ASpace_OS_V2/

Env vars:
  MEMORY_ROOT    = .claude/memory (default)
  CANON_ROOTS    = comma-separated canon paths (default: 6 known)
  MASTER_OUT     = output dir (default: ASpace_OS_V2/graphify-out-master)
"""
from __future__ import annotations

import json
import logging
import os
import sys
import time
from collections import Counter
from pathlib import Path

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S",
)
log = logging.getLogger("graphify-master-merge")

DEFAULT_MEMORY = Path(r"C:\Users\amado\.claude\memory")
DEFAULT_CANON = [
    r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\graphify-out\graph.json",
    r"C:\Users\amado\ASpace_OS_V2\graphify-out\graph.json",
    r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\graphify-out\graph.json",
    r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\02_Areas_Spock\graphify-out\graph.json",
    r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\04_Archives_Data\graphify-out\graph.json",
    r"C:\Users\amado\agent-os\graphify-out\graph.json",
]
DEFAULT_MASTER_OUT = Path(r"C:\Users\amado\ASpace_OS_V2\graphify-out-master")
JUNCTION_PREFIXES = ("app-", "amadeus-", "biz-", "aspace-")


def discover_sources(memory_root: Path, canon_roots: list[str]) -> list[tuple[str, str, Path]]:
    """Return list of (kind, source_label, graph_json_path) for every graph.json found."""
    sources: list[tuple[str, str, Path]] = []
    seen_targets: set[Path] = set()

    # 1) Junctions
    if memory_root.exists():
        for entry in sorted(memory_root.iterdir()):
            if not any(entry.name.startswith(p) for p in JUNCTION_PREFIXES):
                continue
            g = entry / "graph.json"
            if not g.exists():
                continue
            try:
                target = g.resolve()
            except OSError:
                target = g
            if target in seen_targets:
                log.info("skip duplicate junction: %s (same target as prior)", entry.name)
                continue
            seen_targets.add(target)
            sources.append(("junction", entry.name, g))

    # 2) Canon roots
    for c in canon_roots:
        p = Path(c)
        if not p.exists():
            continue
        try:
            target = p.resolve()
        except OSError:
            target = p
        if target in seen_targets:
            log.info("skip duplicate canon: %s", p.parent.parent.name)
            continue
        seen_targets.add(target)
        sources.append(("canon", p.parent.parent.name, p))

    return sources


def merge_one(path: Path, label: str, master: dict, seen_nodes: set[str], seen_edges: set[tuple],
              per_source: dict) -> tuple[int, int, int]:
    """Parse one graph.json, add nodes/edges to master, return (nodes_added, edges_added, nodes_skipped_dup)."""
    try:
        g = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except (json.JSONDecodeError, OSError) as exc:
        log.warning("skip %s: %s", label, exc)
        per_source[label] = {"error": str(exc)}
        return 0, 0, 0
    n_added = 0
    e_added = 0
    n_dup = 0
    n_total = 0
    for node in g.get("nodes", []):
        n_total += 1
        nid = node.get("id")
        if not nid:
            continue
        if nid in seen_nodes:
            n_dup += 1
            continue
        seen_nodes.add(nid)
        # Annotate source for provenance
        node_copy = dict(node)
        node_copy["app_source"] = label
        master["nodes"].append(node_copy)
        n_added += 1
    for link in g.get("links", []):
        s = link.get("source")
        t = link.get("target")
        k = link.get("key", link.get("relation", 0))
        if not s or not t:
            continue
        ek = (s, t, k)
        if ek in seen_edges:
            continue
        seen_edges.add(ek)
        link_copy = dict(link)
        link_copy["app_source"] = label
        master["links"].append(link_copy)
        e_added += 1
    per_source[label] = {
        "nodes_total": n_total,
        "nodes_added": n_added,
        "nodes_dup": n_dup,
        "edges_added": e_added,
    }
    return n_added, e_added, n_dup


def main() -> int:
    memory_root = Path(os.environ.get("MEMORY_ROOT", str(DEFAULT_MEMORY)))
    canon_roots = os.environ.get("CANON_ROOTS", ",".join(DEFAULT_CANON)).split(",")
    master_out = Path(os.environ.get("MASTER_OUT", str(DEFAULT_MASTER_OUT)))

    log.info("memory=%s | canon_roots=%d | master_out=%s", memory_root, len(canon_roots), master_out)

    sources = discover_sources(memory_root, canon_roots)
    log.info("discovered %d unique sources", len(sources))

    master: dict = {
        "directed": False,
        "multigraph": False,
        "graph": {
            "merged_from": 0,
            "source": "graphify-master-merge",
            "merged_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        },
        "nodes": [],
        "links": [],
    }
    seen_nodes: set[str] = set()
    seen_edges: set[tuple] = set()
    per_source: dict = {}
    community_counter: Counter = Counter()
    t0 = time.time()

    for kind, label, path in sources:
        n, e, d = merge_one(path, label, master, seen_nodes, seen_edges, per_source)
        log.info("  %s [%s]: +%d nodes (%d dup), +%d edges", label, kind, n, d, e)
        # community tally from added nodes
        for node in master["nodes"][-n:]:
            community_counter[node.get("community")] += 1

    elapsed = round(time.time() - t0, 1)
    master["graph"]["merged_from"] = len(sources)

    master_out.mkdir(parents=True, exist_ok=True)
    graph_path = master_out / "graph.json"
    graph_path.write_text(json.dumps(master, indent=2, ensure_ascii=False), encoding="utf-8")
    size = graph_path.stat().st_size

    # Provenance report
    report = {
        "merged_at": master["graph"]["merged_at"],
        "elapsed_s": elapsed,
        "sources_total": len(sources),
        "unique_nodes": len(master["nodes"]),
        "unique_edges": len(master["links"]),
        "duplicates_skipped": sum(s.get("nodes_dup", 0) for s in per_source.values()),
        "per_source": per_source,
        "top_communities": dict(community_counter.most_common(15)),
    }
    (master_out / "GRAPH_REPORT.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # Junction in .claude/memory/ for future sessions
    junction = Path(r"C:\Users\amado\.claude\memory\graphify-out-master")
    if not junction.exists():
        try:
            # On Windows, junctions require admin or same-volume. Try.
            os.system(f'mklink /J "{junction}" "{master_out}" >nul 2>&1')
            log.info("junction created: %s", junction)
        except Exception:
            pass

    log.info("DONE: %d nodes, %d edges from %d sources in %ss",
             len(master["nodes"]), len(master["links"]), len(sources), elapsed)
    log.info("written: %s (%d KB)", graph_path, size // 1024)
    return 0


if __name__ == "__main__":
    sys.exit(main())
