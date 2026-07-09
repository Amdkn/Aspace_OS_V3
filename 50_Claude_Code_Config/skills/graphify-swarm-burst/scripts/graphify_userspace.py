"""
graphify_userspace.py — Burst-graphify each top-level app under C:\\Users\\amado\\
individually (not as one monolith).

Idempotent: re-runs detect existing junctions and graph.json files, skip
already-done apps, and update the cartography in place.

Output:
  - <USERSPACE>\\<app>\\graphify-out\\graph.json  (per app)
  - .claude/memory/<app>  (junction, idempotent)
  - .claude/memory/userspace-cartography.md  (cartography, auto-updated)
"""
from __future__ import annotations

import json
import logging
import os
import re
import shutil
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import asdict, dataclass, field
from pathlib import Path

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S",
)
log = logging.getLogger("graphify-userspace")

DEFAULT_USERSPACE = Path(r"C:\Users\amado")
DEFAULT_MEMORY = Path(r"C:\Users\amado\.claude\memory")
DEFAULT_SKILL_DIR = Path(r"C:\Users\amado\.claude\skills\graphify-swarm-burst")

# Apps to graphify (relative to USERSPACE). Each is a separate burst.
DEFAULT_APPS: list[str] = [
    "agent-os",                # Brian Casel Builder Methods (real app, not concept)
    ".agent",                  # Antigravity workflows
    ".agents",                 # newer
    ".aitk",                   # AI toolkit
    ".antigravity",
    ".antigravity-ide",
    ".antigravity_cockpit",
    ".antigravitycli",
    ".browser-use",
    ".cagent",
    ".claude",
    ".codex",
    ".context7",
    ".copilot",
    ".cursor",
    ".gemini",
    ".hermes",
    ".kimi",
]

# Hard skip: credentials / secrets / caches (NEVER graphify)
HARD_SKIP: frozenset[str] = frozenset({
    ".aws", ".azure", ".docker", ".bun", ".chocolatey", ".mcp-auth",
    ".cache", ".local", ".claude-server-commander", ".claude-server-commander-logs",
    "Downloads", "Documents",
})

PRIORITY_EXTS: frozenset[str] = frozenset({".md", ".mdx", ".markdown"})
SOURCE_EXTS: frozenset[str] = frozenset({".ts", ".tsx", ".js", ".jsx", ".mjs", ".py", ".yaml", ".yml", ".json", ".sh", ".ps1"})
SKIP_DIRS: frozenset[str] = frozenset({
    "node_modules", ".next", ".git", ".obsidian",
    ".venv", "venv", "dist", "build", "__pycache__", "graphify-out",
    "chunks", "Graphviz", "logs", ".claude", "cache", "Cache",
})


@dataclass(frozen=True)
class AppResult:
    app: str
    status: str  # "done", "skipped", "small", "failed"
    nodes: int = 0
    edges: int = 0
    elapsed_s: float = 0.0
    junction: str = ""
    error: str | None = None


def alias_for(app: str) -> str:
    """Map app dir name → safe junction alias in .claude/memory/."""
    safe = re.sub(r"[^A-Za-z0-9._-]", "-", app).strip("-")
    if not safe:
        safe = "root"
    return f"app-{safe}"


def make_junction(junction: Path, target: Path) -> str:
    """Idempotent: returns 'created' | 'exists-ok' | 'recreated' | 'error'."""
    junction.parent.mkdir(parents=True, exist_ok=True)
    if junction.exists() or junction.is_symlink():
        # Check if it points to the right target
        try:
            current = junction.resolve()
            if current == target.resolve():
                return "exists-ok"
            shutil.rmtree(junction) if junction.is_dir() else junction.unlink()
        except OSError:
            return "error"
    try:
        subprocess.run(
            ["powershell", "-NoProfile", "-Command",
             f"New-Item -ItemType Junction -Path '{junction}' -Target '{target}'"],
            check=True, capture_output=True, text=True, timeout=10,
        )
        return "created"
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        return f"error: {exc}"


def cartography_row(app: str, status: str, nodes: int, edges: int, junction: str) -> str:
    return f"| `{app}` | {status} | {nodes:,} | {edges:,} | `{junction}` |"


def write_cartography(results: list[AppResult], target: Path) -> None:
    """Auto-updated cartography markdown (idempotent overwrite per run, but
    MERGES with prior entries so partial re-runs don't lose history)."""
    target.parent.mkdir(parents=True, exist_ok=True)

    # D4 append-only for canon: merge new results with existing cartography rows.
    # We re-parse the existing table (if any) to preserve apps from prior runs.
    prior_rows: dict[str, tuple[str, int, int, str]] = {}  # app → (status, nodes, edges, junction)
    if target.exists():
        try:
            for line in target.read_text(encoding="utf-8").splitlines():
                # Match | `app` | status | N | E | junction |
                if not line.startswith("| `") or "`" not in line[3:]:
                    continue
                parts = [p.strip() for p in line.split("|")]
                if len(parts) < 6:
                    continue
                app = parts[1].strip("`")
                try:
                    nodes = int(parts[3].replace(",", ""))
                    edges = int(parts[4].replace(",", ""))
                except ValueError:
                    continue
                prior_rows[app] = (parts[2], nodes, edges, parts[5])
        except OSError:
            pass

    # Overlay new results on top of prior rows
    for r in results:
        prior_rows[r.app] = (r.status, r.nodes, r.edges, r.junction)

    lines: list[str] = [
        "---",
        "source: graphify_userspace.py",
        f"date: {time.strftime('%Y-%m-%d')}",
        "type: cartography",
        "status: ACTIVE",
        "tags: [#userspace, #cartography, #graphify, #apps]",
        "---",
        "",
        "# User-Space Cartography — C:\\Users\\amado",
        "",
        "> Auto-generated by `graphify_userspace.py`. **Idempotent**: re-run updates this file in place.",
        "> **Anti-pattern guard**: every app below is a SPECIFIC installed app, NOT a concept.",
        "> Agent OS = the app at `C:\\Users\\amado\\agent-os\\` (with `commands/`, `config.yml`, `profiles/`, `scripts/`, `standards/`), NOT a category.",
        "",
        "| App | Status | Nodes | Edges | Junction |",
        "|-----|--------|------:|------:|----------|",
    ]
    # Sort by app name for stable output
    for app in sorted(prior_rows.keys()):
        status, nodes, edges, junction = prior_rows[app]
        lines.append(cartography_row(app, status, nodes, edges, junction))
    lines.append("")
    lines.append("## Hard-skipped (credentials / caches / user data)")
    lines.append("")
    for s in sorted(HARD_SKIP):
        lines.append(f"- `{s}`")
    lines.append("")
    target.write_text("\n".join(lines), encoding="utf-8")


def run_app(app_rel: str, chunks: int, workers: int) -> AppResult:
    """Graphify one app. Idempotent: skips if graph.json already exists."""
    app_dir = DEFAULT_USERSPACE / app_rel
    alias = alias_for(app_rel)
    junction = DEFAULT_MEMORY / alias

    if not app_dir.exists():
        return AppResult(app=app_rel, status="missing", junction=str(junction))

    out_dir = app_dir / "graphify-out"
    graph_json = out_dir / "graph.json"

    # Idempotency: skip if already done
    if graph_json.exists() and graph_json.stat().st_size > 100:
        try:
            existing = json.loads(graph_json.read_text(encoding="utf-8"))
            nodes = len(existing.get("nodes", []))
            edges = len(existing.get("links", []))
            j_state = make_junction(junction, out_dir)
            return AppResult(app=app_rel, status="already-done", nodes=nodes, edges=edges,
                             junction=str(junction) + f" ({j_state})")
        except (json.JSONDecodeError, OSError):
            pass

    # List files via Python rglob (D6 fix 2026-06-16: bash subprocess hits broken WSL
    # on this Windows box → empty stdout → false "empty" status. Pure-Python rglob
    # is fine for per-app scope (max ~3K files in .claude), ASpace monolith already
    # uses /usr/bin/find via the Bash tool elsewhere).
    target_exts = PRIORITY_EXTS | SOURCE_EXTS

    def _scan(p: Path) -> list[Path]:
        out: list[Path] = []
        try:
            for entry in p.iterdir():
                if entry.is_dir():
                    if entry.name in SKIP_DIRS:
                        continue
                    out.extend(_scan(entry))
                elif entry.is_file() and entry.suffix.lower() in target_exts:
                    out.append(entry)
        except (PermissionError, OSError):
            pass
        return out

    files = _scan(app_dir)
    if len(files) > 50000:
        files = files[:50000]

    if not files:
        # Empty app: still create the target dir + junction so cartography has a
        # consistent junction entry. D7 (2026-06-16): avoid junction-creation
        # failure on missing target by mkdir-ing first.
        out_dir.mkdir(parents=True, exist_ok=True)
        j_state = make_junction(junction, out_dir)
        return AppResult(app=app_rel, status="empty", nodes=0, edges=0,
                         junction=str(junction) + f" ({j_state})")

    if len(files) < 5:
        # Too small to swarm — run graphify once on the whole app
        out_dir.mkdir(parents=True, exist_ok=True)
        t0 = time.time()
        try:
            subprocess.run(["graphify", str(app_dir), "-o", str(graph_json)], check=True, capture_output=True, timeout=180)
        except subprocess.TimeoutExpired:
            return AppResult(app=app_rel, status="timeout-small", junction=str(junction))
        if graph_json.exists():
            existing = json.loads(graph_json.read_text(encoding="utf-8"))
            nodes = len(existing.get("nodes", []))
            edges = len(existing.get("links", []))
            j_state = make_junction(junction, out_dir)
            return AppResult(app=app_rel, status="small", nodes=nodes, edges=edges,
                             elapsed_s=round(time.time() - t0, 1),
                             junction=str(junction) + f" ({j_state})")
        return AppResult(app=app_rel, status="failed-small", junction=str(junction))

    # Large app: spawn the swarm script
    t0 = time.time()
    try:
        result = subprocess.run(
            ["python", "-u", str(DEFAULT_SKILL_DIR / "scripts" / "graphify_swarm.py")],
            env={**os.environ, "TARGET": str(app_dir), "OUT_ROOT": str(out_dir),
                 "CHUNKS": str(chunks), "WORKERS": str(workers),
                 "TIMEOUT_S": os.environ.get("TIMEOUT_S", "300")},
            capture_output=True, text=True, timeout=900,
        )
    except subprocess.TimeoutExpired:
        return AppResult(app=app_rel, status="timeout-swarm", junction=str(junction))

    if result.returncode != 0:
        # Partial failure: log but continue to merge (D7: don't waste 23 OK chunks
        # because 2 timed out — A0 escalation cost > false-positive merge cost)
        log.warning("    swarm rc=%d (partial) — proceeding to merge", result.returncode)

    # Merge
    try:
        merge = subprocess.run(
            ["python", str(DEFAULT_SKILL_DIR / "scripts" / "graphify_merge.py")],
            env={**os.environ, "OUT_ROOT": str(out_dir)},
            capture_output=True, text=True, timeout=60,
        )
        if merge.returncode != 0:
            # D7 (2026-06-16): don't lose the chunks because merge can't combine
            # all of them — fall through to check if a partial graph.json was written
            log.warning("    merge rc=%d stderr=%s", merge.returncode, merge.stderr[-200:])
    except subprocess.TimeoutExpired:
        return AppResult(app=app_rel, status="timeout-merge", junction=str(junction))

    if graph_json.exists():
        existing = json.loads(graph_json.read_text(encoding="utf-8"))
        nodes = len(existing.get("nodes", []))
        edges = len(existing.get("links", []))
        j_state = make_junction(junction, out_dir)
        return AppResult(app=app_rel, status="done", nodes=nodes, edges=edges,
                         elapsed_s=round(time.time() - t0, 1),
                         junction=str(junction) + f" ({j_state})")
    return AppResult(app=app_rel, status="failed-no-graph", junction=str(junction))


def main() -> int:
    apps_env = os.environ.get("APPS")
    apps = apps_env.split(",") if apps_env else DEFAULT_APPS
    chunks = int(os.environ.get("CHUNKS", "40"))
    workers = int(os.environ.get("WORKERS", "16"))

    log.info("userspace=%s | %d apps | chunks=%d | workers=%d", DEFAULT_USERSPACE, len(apps), chunks, workers)
    results: list[AppResult] = []
    t_total = time.time()
    for app in apps:
        log.info("=== %s ===", app)
        r = run_app(app, chunks, workers)
        log.info("    status=%s nodes=%d edges=%d", r.status, r.nodes, r.edges)
        results.append(r)
    elapsed = round(time.time() - t_total, 1)

    cartography_path = DEFAULT_MEMORY / "userspace-cartography.md"
    write_cartography(results, cartography_path)
    log.info("cartography updated: %s", cartography_path)

    summary = {"elapsed_s": elapsed, "results": [asdict(r) for r in results]}
    (DEFAULT_MEMORY / "userspace-cartography.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info("DONE: %d apps in %.1fs", len(results), elapsed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
