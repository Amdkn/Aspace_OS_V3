"""
local_server.py — Localhost web server for graphify corpus visualization.

Pure stdlib. Reads the master graph.json once at startup, builds community + source
indexes in memory, then serves filtered subsets to a browser viewer on-demand.

Endpoints:
  GET  /                                  → viewer.html
  GET  /api/stats                         → corpus counts + top communities/sources
  GET  /api/community/<id>?limit=200      → nodes + edges for one community
  GET  /api/source/<name>?limit=200       → nodes + edges from one app source
  GET  /api/search?q=<kw>&limit=50        → keyword search across node fields
  GET  /api/node/<id>                     → single node + its edges
  GET  /api/path?from=<id>&to=<id>        → shortest path via graphify CLI (delegated)

Env:
  GRAPHIFY_MASTER  = path to master graph.json (default: ASpace_OS_V2/graphify-out-master/graph.json)
  GRAPHIFY_HOST    = bind host (default: 127.0.0.1)
  GRAPHIFY_PORT    = port (default: 8765)
  GRAPHIFY_LOAD    = "0" to skip eager load (build indexes on first request)
"""
from __future__ import annotations

import json
import logging
import os
import subprocess
import sys
from collections import Counter, defaultdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S",
)
log = logging.getLogger("graphify-local")

DEFAULT_MASTER = Path(r"C:\Users\amado\ASpace_OS_V2\graphify-out-master\graph.json")
DEFAULT_REPORT = Path(r"C:\Users\amado\ASpace_OS_V2\graphify-out-master\GRAPH_REPORT.json")
HTML_PATH = Path(__file__).parent / "viewer.html"


class Corpus:
    def __init__(self, master_path: Path) -> None:
        self.master_path = master_path
        self.nodes: list[dict] = []
        self.links: list[dict] = []
        self.id_to_node: dict[str, dict] = {}
        self.community_index: dict[str, list[str]] = defaultdict(list)
        self.source_index: dict[str, list[str]] = defaultdict(list)
        self.keyword_index: dict[str, set[str]] = defaultdict(set)
        self._loaded = False

    def load(self) -> None:
        if self._loaded:
            return
        if not self.master_path.exists():
            log.error("master graph not found: %s", self.master_path)
            sys.exit(1)
        log.info("loading %s (%d MB)...", self.master_path, self.master_path.stat().st_size // (1024 * 1024))
        data = json.loads(self.master_path.read_text(encoding="utf-8", errors="replace"))
        self.nodes = data.get("nodes", [])
        self.links = data.get("links", [])
        for n in self.nodes:
            nid = n.get("id")
            if not nid:
                continue
            self.id_to_node[nid] = n
            cid = n.get("community", "?")
            src = n.get("app_source", "?")
            self.community_index[cid].append(nid)
            self.source_index[src].append(nid)
            # Keyword index: words from label/name/path
            for field in ("label", "name", "path"):
                v = n.get(field)
                if isinstance(v, str):
                    for word in v.lower().split():
                        if len(word) > 3:
                            self.keyword_index[word].add(nid)
        self._loaded = True
        log.info("loaded: %d nodes, %d edges, %d communities, %d sources, %d keywords",
                 len(self.nodes), len(self.links),
                 len(self.community_index), len(self.source_index), len(self.keyword_index))

    def slice_community(self, cid: str, limit: int) -> dict:
        if not self._loaded:
            self.load()
        node_ids = set(self.community_index.get(cid, [])[:limit])
        nodes = [self.id_to_node[nid] for nid in node_ids if nid in self.id_to_node]
        links = [l for l in self.links if l.get("source") in node_ids and l.get("target") in node_ids]
        return {"nodes": nodes, "links": links, "truncated": len(self.community_index.get(cid, [])) > limit}

    def slice_source(self, src: str, limit: int) -> dict:
        if not self._loaded:
            self.load()
        node_ids = set(self.source_index.get(src, [])[:limit])
        nodes = [self.id_to_node[nid] for nid in node_ids if nid in self.id_to_node]
        links = [l for l in self.links if l.get("source") in node_ids and l.get("target") in node_ids]
        return {"nodes": nodes, "links": links, "truncated": len(self.source_index.get(src, [])) > limit}

    def search(self, q: str, limit: int) -> dict:
        if not self._loaded:
            self.load()
        q_lower = q.lower()
        hits: list[dict] = []
        for n in self.nodes:
            text = " ".join(str(v) for v in n.values() if v).lower()
            if q_lower in text:
                hits.append(n)
                if len(hits) >= limit:
                    break
        node_ids = {n.get("id") for n in hits}
        links = [l for l in self.links if l.get("source") in node_ids and l.get("target") in node_ids]
        return {"nodes": hits, "links": links}

    def get_node(self, nid: str) -> dict | None:
        if not self._loaded:
            self.load()
        node = self.id_to_node.get(nid)
        if not node:
            return None
        links = [l for l in self.links if l.get("source") == nid or l.get("target") == nid]
        return {"node": node, "links": links}

    def stats(self) -> dict:
        if not self._loaded:
            self.load()
        return {
            "nodes": len(self.nodes),
            "links": len(self.links),
            "communities": len(self.community_index),
            "sources": len(self.source_index),
            "top_communities": Counter({c: len(ids) for c, ids in self.community_index.items()}).most_common(20),
            "top_sources": Counter({s: len(ids) for s, ids in self.source_index.items()}).most_common(20),
        }


CORPUS = Corpus(Path(os.environ.get("GRAPHIFY_MASTER", str(DEFAULT_MASTER))))


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        log.info("%s - %s", self.address_string(), fmt % args)

    def do_GET(self) -> None:
        url = urlparse(self.path)
        path = url.path
        qs = parse_qs(url.query)
        try:
            if path == "/" or path == "/viewer.html":
                self._serve_html()
            elif path == "/api/stats":
                self._serve_json(CORPUS.stats())
            elif path.startswith("/api/community/"):
                cid_raw = path[len("/api/community/"):]
                # D6 (2026-06-16): graphify stores community as int in JSON, but URL is string.
                # Try int first, fall back to string.
                cid: str | int
                try:
                    cid = int(cid_raw)
                except ValueError:
                    cid = cid_raw
                limit = int(qs.get("limit", ["200"])[0])
                self._serve_json(CORPUS.slice_community(cid, limit))
            elif path.startswith("/api/source/"):
                src = path[len("/api/source/"):]
                limit = int(qs.get("limit", ["200"])[0])
                self._serve_json(CORPUS.slice_source(src, limit))
            elif path == "/api/search":
                q = qs.get("q", [""])[0]
                limit = int(qs.get("limit", ["50"])[0])
                self._serve_json(CORPUS.search(q, limit))
            elif path.startswith("/api/node/"):
                nid = path[len("/api/node/"):]
                result = CORPUS.get_node(nid)
                if result is None:
                    self._serve_json({"error": "not found", "id": nid}, status=404)
                else:
                    self._serve_json(result)
            elif path == "/api/path":
                frm = qs.get("from", [""])[0]
                to = qs.get("to", [""])[0]
                self._serve_path(frm, to)
            else:
                self._serve_json({"error": "not found", "path": path}, status=404)
        except Exception as exc:
            log.exception("handler error")
            self._serve_json({"error": type(exc).__name__, "detail": str(exc)}, status=500)

    def _serve_html(self) -> None:
        if not HTML_PATH.exists():
            self._serve_json({"error": "viewer.html missing", "path": str(HTML_PATH)}, status=500)
            return
        body = HTML_PATH.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_json(self, payload: dict, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _serve_path(self, frm: str, to: str) -> None:
        # Delegate to graphify CLI: graphify path A B --graph master.json
        if not frm or not to:
            self._serve_json({"error": "missing from/to", "from": frm, "to": to}, status=400)
            return
        try:
            r = subprocess.run(
                ["graphify", "path", frm, to, "--graph", str(CORPUS.master_path)],
                capture_output=True, text=True, timeout=30,
            )
            self._serve_json({"from": frm, "to": to, "rc": r.returncode, "stdout": r.stdout, "stderr": r.stderr})
        except FileNotFoundError:
            self._serve_json({"error": "graphify CLI not on PATH", "hint": "uv tool install graphifyy[anthropic]"}, status=500)
        except subprocess.TimeoutExpired:
            self._serve_json({"error": "timeout"}, status=500)


def main() -> int:
    host = os.environ.get("GRAPHIFY_HOST", "127.0.0.1")
    port = int(os.environ.get("GRAPHIFY_PORT", "8765"))
    eager = os.environ.get("GRAPHIFY_LOAD", "1") == "1"
    if eager:
        CORPUS.load()
    server = ThreadingHTTPServer((host, port), Handler)
    log.info("serving on http://%s:%d (master=%s, eager_load=%s)", host, port, CORPUS.master_path, eager)
    log.info("open http://localhost:%d in your browser", port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        log.info("shutting down")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
