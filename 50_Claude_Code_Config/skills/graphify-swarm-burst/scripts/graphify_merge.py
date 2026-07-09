"""
graphify_merge.py — Merge chunk graph.json files into one master graph.

Parameterised via environment variables:
  OUT_ROOT   = where chunks/ lives (default: $TARGET/graphify-out)

Pure file I/O. No LLM calls.
"""
from __future__ import annotations

import json
import logging
import os
import sys
from collections import Counter
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("graphify-merge")

DEFAULT_OUT_ROOT = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\graphify-out")


def merge_one(path: Path, master: dict, seen_nodes: set[str], seen_edges: set[tuple], community_counter: Counter) -> tuple[int, int]:
    try:
        g = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        # D7 (2026-06-16): skip malformed chunks from failed graphify runs rather
        # than aborting the whole merge — losing 33 OK chunks to 1 corrupt file
        # is wasteful when A0 escalation cost dwarfs the data loss.
        log.warning("skipping %s: %s", path.parent.name, exc)
        return 0, 0
    n_added = 0
    e_added = 0
    for node in g.get("nodes", []):
        nid = node.get("id")
        if nid and nid not in seen_nodes:
            seen_nodes.add(nid)
            master["nodes"].append(node)
            community_counter[node.get("community")] += 1
            n_added += 1
    for link in g.get("links", []):
        s = link.get("source")
        t = link.get("target")
        k = link.get("key", link.get("relation", 0))
        ek = (s, t, k)
        if s and t and ek not in seen_edges:
            seen_edges.add(ek)
            master["links"].append(link)
            e_added += 1
    return n_added, e_added


def main() -> int:
    import time
    out_root = Path(os.environ.get("OUT_ROOT", str(DEFAULT_OUT_ROOT)))
    chunks_dir = out_root / "chunks"

    master: dict = {
        "directed": False,
        "multigraph": False,
        "graph": {"merged_from": 0, "source": "graphify-swarm-burst"},
        "nodes": [],
        "links": [],
    }
    seen_nodes: set[str] = set()
    seen_edges: set[tuple] = set()
    community_counter: Counter = Counter()

    paths = sorted(chunks_dir.glob("chunk_*/graphify-out/graph.json"))
    # D7 (2026-06-16): on .cursor burst, 0 chunks visible immediately after swarm rc=1
    # return — graphify CLI writes flushed after process exit but Windows file
    # cache held them. Retry up to 5× with 2s sleep before giving up.
    if not paths:
        log.warning("merge: 0 paths on first scan, retrying (race vs chunk flush)...")
        for attempt in range(5):
            import time as _t
            _t.sleep(2)
            paths = sorted(chunks_dir.glob("chunk_*/graphify-out/graph.json"))
            if paths:
                break
        log.info("merge: recovered %d paths after retry", len(paths))
    log.info("merging %d chunk graph.json", len(paths))
    skipped = 0
    for p in paths:
        before = (len(master["nodes"]), len(master["links"]))
        merge_one(p, master, seen_nodes, seen_edges, community_counter)
        if (len(master["nodes"]), len(master["links"])) == before:
            skipped += 1

    master["graph"]["merged_from"] = len(paths)
    out_root.mkdir(parents=True, exist_ok=True)
    (out_root / "graph.json").write_text(json.dumps(master, indent=2, ensure_ascii=False), encoding="utf-8")
    report = {
        "merged_at": time.strftime("%Y-%m-%d"),
        "chunk_count": len(paths),
        "unique_nodes": len(master["nodes"]),
        "unique_edges": len(master["links"]),
        "communities": dict(community_counter.most_common(20)),
    }
    (out_root / "GRAPH_REPORT.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info("merged: %d nodes, %d edges", report["unique_nodes"], report["unique_edges"])
    log.info("written: %s/graph.json (%d bytes)", out_root, (out_root / "graph.json").stat().st_size)
    return 0


if __name__ == "__main__":
    import time
    sys.exit(main())
