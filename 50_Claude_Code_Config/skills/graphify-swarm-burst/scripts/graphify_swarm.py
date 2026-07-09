"""
graphify_swarm.py — Burst-graphify a large target directory.

Parameterised via environment variables:
  TARGET       = root to graphify (default: C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE)
  OUT_ROOT     = output dir (default: $TARGET/graphify-out)
  CHUNKS       = number of parallel chunks (default: 80)
  WORKERS      = parallel workers (default: 16, capped per CLAUDE.md)
  TIMEOUT_S    = per-chunk graphify timeout in seconds (default: 300; bump to 600 for Life OS .md handoffs)
  INCREMENTAL  = "1" to skip chunks where all files are unchanged since last run
                  (state file: $OUT_ROOT/.graphify-state.json)

Proven on Memory Core (2026-06-16): 80/80 OK in 6.87 min, 2231 nodes, 2935 edges.
Run #2 04_Archives_Data (2026-06-16): 14/25 OK (56%) — TIMEOUT_S=600 recommended for Life OS.
Incremental mode added 2026-06-16: re-run on unchanged corpus = 0 chunks reprocessed.
"""
from __future__ import annotations

import json
import logging
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("graphify-swarm")

DEFAULT_TARGET = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE")
PRIORITY_EXTS: frozenset[str] = frozenset({".md", ".mdx", ".markdown"})
SOURCE_EXTS: frozenset[str] = frozenset({".ts", ".tsx", ".js", ".jsx", ".mjs", ".py", ".yaml", ".yml", ".json", ".sh", ".ps1"})
SKIP_DIRS: frozenset[str] = frozenset({
    "30_MEMORY_CORE", "node_modules", ".next", ".git", ".obsidian",
    ".venv", "venv", "dist", "build", "__pycache__", "graphify-out",
    "aspace-graphify-out", "chunks", "Graphviz", "logs", ".claude",
})


@dataclass(frozen=True)
class ChunkResult:
    chunk: int
    files: int
    ok: bool
    rc: int
    elapsed_s: float
    error: str | None = None
    skipped: bool = False  # D7 (2026-06-16): incremental mode — chunk unchanged, skipped


def load_state(out_root: Path) -> dict[str, dict]:
    """Load per-file mtime/size state from prior runs. Empty dict if missing/corrupt."""
    state_file = out_root / ".graphify-state.json"
    if not state_file.exists():
        return {}
    try:
        data = json.loads(state_file.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        return {}


def save_state(out_root: Path, state: dict[str, dict]) -> None:
    """Write state back atomically (tmp + rename) to avoid corruption on partial writes."""
    state_file = out_root / ".graphify-state.json"
    tmp = state_file.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(state_file)


def file_signature(p: Path) -> dict[str, int | float]:
    """Compact file fingerprint: mtime_ns + size. Used for incremental skip."""
    st = p.stat()
    return {"mtime_ns": st.st_mtime_ns, "size": st.st_size}


def list_files(root: Path) -> list[Path]:
    """Priority: .md first, then source files. Sort for determinism.

    D6 fix 2026-06-16: SKIP_DIRS check was absolute (any part of full path),
    which skipped ALL files when TARGET itself was in SKIP_DIRS (e.g. .claude
    has .claude in SKIP_DIRS for ASpace scope but IS the target here). Use
    relative-to-root parts so we only skip descendants, not the root itself.
    """
    md_files: list[Path] = []
    src_files: list[Path] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        try:
            rel_parts = p.relative_to(root).parts
        except ValueError:
            rel_parts = p.parts
        if any(s in rel_parts for s in SKIP_DIRS):
            continue
        if p.suffix.lower() in PRIORITY_EXTS:
            md_files.append(p)
        elif p.suffix.lower() in SOURCE_EXTS:
            src_files.append(p)
    md_files.sort()
    src_files.sort()
    files = md_files + src_files
    log.info("md=%d + source=%d = total %d", len(md_files), len(src_files), len(files))
    return files


def partition(files: list[Path], n: int) -> list[list[Path]]:
    """Round-robin into n buckets. Drops empty buckets."""
    chunks: list[list[Path]] = [[] for _ in range(n)]
    for i, f in enumerate(files):
        chunks[i % n].append(f)
    return [c for c in chunks if c]


def run_chunk(args: tuple[int, list[Path], Path, int]) -> ChunkResult:
    """Stage files in a chunk dir then run graphify. Returns immutable result."""
    idx, files, chunks_dir, timeout_s = args
    chunk_dir = chunks_dir / f"chunk_{idx:03d}"
    chunk_dir.mkdir(parents=True, exist_ok=True)
    for f in files:
        dst = chunk_dir / f.name
        if not dst.exists():
            try:
                shutil.copy2(f, dst)
            except OSError:
                pass
    t0 = time.time()
    try:
        result = subprocess.run(
            ["graphify", str(chunk_dir), "-o", str(chunk_dir / "graph.json")],
            capture_output=True, text=True, timeout=timeout_s,
        )
        return ChunkResult(
            chunk=idx, files=len(files), ok=result.returncode == 0,
            rc=result.returncode, elapsed_s=round(time.time() - t0, 1),
        )
    except subprocess.TimeoutExpired:
        return ChunkResult(chunk=idx, files=len(files), ok=False, rc=-1, elapsed_s=float(timeout_s), error=f"timeout>{timeout_s}s")
    except Exception as exc:
        return ChunkResult(chunk=idx, files=len(files), ok=False, rc=-2, elapsed_s=round(time.time() - t0, 1), error=str(exc))


def main() -> int:
    target = Path(os.environ.get("TARGET", str(DEFAULT_TARGET)))
    out_root = Path(os.environ.get("OUT_ROOT", str(target / "graphify-out")))
    chunks_dir = out_root / "chunks"
    n_chunks = int(os.environ.get("CHUNKS", "80"))
    max_workers = int(os.environ.get("WORKERS", "16"))
    timeout_s = int(os.environ.get("TIMEOUT_S", "300"))
    incremental = os.environ.get("INCREMENTAL", "0") == "1"

    log.info("target=%s | out=%s | chunks=%d | workers=%d | timeout_s=%d | incremental=%s",
             target, out_root, n_chunks, max_workers, timeout_s, incremental)

    out_root.mkdir(parents=True, exist_ok=True)
    if chunks_dir.exists() and not incremental:
        shutil.rmtree(chunks_dir)
    chunks_dir.mkdir(parents=True, exist_ok=True)

    files = list_files(target)
    chunks = partition(files, n_chunks)
    log.info("partitioned into %d chunks, sizes=%s…", len(chunks), [len(c) for c in chunks[:5]])

    # Incremental: load state, mark chunks with all-unchanged files for skip
    state: dict[str, dict] = load_state(out_root) if incremental else {}
    new_state: dict[str, dict] = dict(state)  # carry over + update
    chunks_to_run: list[tuple[int, list[Path]]] = []
    chunks_skipped = 0
    if incremental:
        for i, c in enumerate(chunks):
            all_unchanged = True
            for f in c:
                try:
                    rel = str(f.relative_to(target))
                except ValueError:
                    rel = str(f)
                sig = file_signature(f)
                prev = state.get(rel)
                if prev != sig:
                    all_unchanged = False
                    break
            if all_unchanged and c:
                chunks_skipped += 1
                log.info("chunk_%03d: SKIPPED (all %d files unchanged since last run)", i, len(c))
            else:
                chunks_to_run.append((i, c))
        log.info("incremental: %d chunks to run, %d skipped", len(chunks_to_run), chunks_skipped)
    else:
        chunks_to_run = list(enumerate(chunks))

    t0 = time.time()
    results: list[ChunkResult] = []
    if chunks_skipped:
        for i, c in enumerate(chunks):
            if any(i == run_i for run_i, _ in chunks_to_run):
                continue
            # Synthetic skipped result
            results.append(ChunkResult(
                chunk=i, files=len(c), ok=True, rc=0, elapsed_s=0.0, skipped=True,
            ))
    with ProcessPoolExecutor(max_workers=max_workers) as ex:
        futs = {ex.submit(run_chunk, (i, c, chunks_dir, timeout_s)): i for i, c in chunks_to_run}
        for fut in as_completed(futs):
            r = fut.result()
            results.append(r)
            log.info("chunk_%03d ok=%s files=%d %.1fs rc=%d", r.chunk, r.ok, r.files, r.elapsed_s, r.rc)

    # Update state for all currently-known files (covers new + changed + removed)
    if incremental:
        for c in chunks:
            for f in c:
                try:
                    rel = str(f.relative_to(target))
                except ValueError:
                    rel = str(f)
                new_state[rel] = file_signature(f)
        # Remove entries for files that no longer exist
        existing_files = {str(f.relative_to(target)) if f.is_relative_to(target) else str(f)
                          for c in chunks for f in c}
        removed = [k for k in list(new_state.keys()) if k not in existing_files]
        for k in removed:
            del new_state[k]
        save_state(out_root, new_state)
        log.info("state updated: %d files tracked, %d removed", len(new_state), len(removed))

    elapsed = round(time.time() - t0, 1)
    ok_count = sum(1 for r in results if r.ok)
    summary = {
        "target": str(target),
        "out_root": str(out_root),
        "n_chunks": n_chunks,
        "max_workers": max_workers,
        "timeout_s": timeout_s,
        "incremental": incremental,
        "ok": ok_count,
        "skipped": chunks_skipped,
        "failed": len(results) - ok_count - chunks_skipped,
        "elapsed_s": elapsed,
        "total_files": sum(r.files for r in results),
    }
    (out_root / "swarm_summary.json").write_text(
        json.dumps({"summary": summary, "results": [asdict(r) for r in results]}, indent=2),
        encoding="utf-8",
    )
    log.info("DONE: %d OK, %d skipped, %d failed in %.1fs", ok_count, chunks_skipped,
             len(results) - ok_count - chunks_skipped, elapsed)
    return 0 if ok_count + chunks_skipped == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
