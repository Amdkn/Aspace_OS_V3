"""
viewer.py — Read-only navigator for the graphify corpus.

Subcommands:
  stats         — corpus counts + size + sources
  communities   — top N communities by node count
  find-node ID  — exact-id node lookup
  search KW     — keyword search across node label/name/path
  sources       — top sources by node count
  breakdown     — per-source detailed breakdown (from GRAPH_REPORT.json)

Pure file I/O, no LLM calls. Loads the master graph on demand only.
"""
from __future__ import annotations

import json
import logging
import sys
from collections import Counter
from pathlib import Path

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S",
)
log = logging.getLogger("graphify-viewer")

DEFAULT_MASTER = Path(r"C:\Users\amado\ASpace_OS_V2\graphify-out-master\graph.json")
DEFAULT_REPORT = Path(r"C:\Users\amado\ASpace_OS_V2\graphify-out-master\GRAPH_REPORT.json")


def load_graph(path: Path) -> dict:
    """Load the full master graph. D6 (2026-06-16): 260 MB — keep memory in mind."""
    if not path.exists():
        log.error("master graph not found: %s", path)
        sys.exit(1)
    log.info("loading %s (%d KB)...", path, path.stat().st_size // 1024)
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def cmd_stats(graph: dict) -> None:
    nodes, links = graph.get("nodes", []), graph.get("links", [])
    sources = Counter(n.get("app_source", "?") for n in nodes)
    communities = Counter(n.get("community") for n in nodes)
    print(f"=== Master corpus stats ===")
    print(f"  nodes:    {len(nodes):,}")
    print(f"  links:    {len(links):,}")
    print(f"  unique sources:   {len(sources)}")
    print(f"  unique communities: {len(communities)}")
    print(f"  top community size: {communities.most_common(1)[0][1]:,}")


def cmd_communities(graph: dict, top: int = 10) -> None:
    nodes = graph.get("nodes", [])
    communities = Counter(n.get("community") for n in nodes)
    print(f"=== Top {top} communities ===")
    for cid, count in communities.most_common(top):
        print(f"  community {cid}: {count:,} nodes")


def cmd_find_node(graph: dict, node_id: str) -> None:
    for n in graph.get("nodes", []):
        if n.get("id") == node_id:
            print(json.dumps(n, indent=2, ensure_ascii=False))
            return
    print(f"NOT FOUND: {node_id}")


def cmd_search(graph: dict, keyword: str, limit: int = 20) -> None:
    kw = keyword.lower()
    hits: list[dict] = []
    for n in graph.get("nodes", []):
        text = " ".join(str(v) for v in n.values() if v).lower()
        if kw in text:
            hits.append(n)
            if len(hits) >= limit:
                break
    print(f"=== Search '{keyword}' ({len(hits)} hits) ===")
    for h in hits:
        print(f"  {h.get('id', '?'):30s} | {h.get('app_source', '?'):30s} | {h.get('label') or h.get('name') or h.get('path') or '?'}")


def cmd_sources(graph: dict, top: int = 15) -> None:
    nodes = graph.get("nodes", [])
    sources = Counter(n.get("app_source", "?") for n in nodes)
    print(f"=== Top {top} sources by node count ===")
    for src, count in sources.most_common(top):
        print(f"  {count:>7,}  {src}")


def cmd_breakdown(report_path: Path) -> None:
    if not report_path.exists():
        log.error("report not found: %s", report_path)
        sys.exit(1)
    report = json.loads(report_path.read_text(encoding="utf-8", errors="replace"))
    print(f"=== Per-source breakdown (merged {report.get('merged_at', '?')}) ===")
    print(f"  total sources: {report.get('sources_total')}")
    print(f"  unique nodes:  {report.get('unique_nodes'):,}")
    print(f"  unique edges:  {report.get('unique_edges'):,}")
    print(f"  duplicates skipped: {report.get('duplicates_skipped'):,}")
    print()
    print(f"  {'source':40s} {'nodes':>8s} {'edges':>8s} {'dups':>6s}")
    per_source = report.get("per_source", {})
    for src in sorted(per_source.keys(), key=lambda k: per_source[k].get("nodes_added", 0), reverse=True):
        info = per_source[src]
        print(f"  {src:40s} {info.get('nodes_added', 0):>8,} {info.get('edges_added', 0):>8,} {info.get('nodes_dup', 0):>6,}")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cmd = sys.argv[1]
    master = DEFAULT_MASTER
    report = DEFAULT_REPORT
    if cmd == "breakdown":
        cmd_breakdown(report)
        return 0
    if cmd in ("stats", "communities", "sources"):
        graph = load_graph(master)
        if cmd == "stats":
            cmd_stats(graph)
        elif cmd == "communities":
            n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
            cmd_communities(graph, top=n)
        elif cmd == "sources":
            n = int(sys.argv[2]) if len(sys.argv) > 2 else 15
            cmd_sources(graph, top=n)
        return 0
    if cmd == "find-node":
        if len(sys.argv) < 3:
            print("usage: viewer.py find-node <id>")
            return 1
        graph = load_graph(master)
        cmd_find_node(graph, sys.argv[2])
        return 0
    if cmd == "search":
        if len(sys.argv) < 3:
            print("usage: viewer.py search <keyword>")
            return 1
        graph = load_graph(master)
        cmd_search(graph, sys.argv[2])
        return 0
    print(f"unknown command: {cmd}")
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
