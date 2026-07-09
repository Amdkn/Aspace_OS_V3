"""
transcript_swarm.py — Chunk a YouTube transcript and dispatch parallel sub-agents.

Pattern: analogue of graphify_swarm.py adapted for text.
- Reads single transcript file (md or txt).
- Slices into N chunks (default 2000 chars/chunk, CHUNK_SIZE env var).
- Writes chunks/chunk_NNN.md + chunks/dispatch.json for sub-agent workers.
- Returns dispatch manifest for A2 (main agent) to launch sub-agents.

Environment variables:
  TRANSCRIPT_PATH  = absolute path to transcript .md/.txt (REQUIRED)
  CHUNK_SIZE       = chars per chunk (default: 2000)
  WORKERS          = parallel sub-agents planned (default: 8, capped 12)
  TIMEOUT_S        = per-worker timeout (default: 600 per D6 lesson)
  HANDOFF_ROOT     = output dir (default: $ASPACE_OS/.../youtube_ingest_<DATE>)
  FORCE            = "1" to re-chunk even if .processed.json has video_id

D6 lessons applied (graphify-swarm-burst 2026-06-16):
- TIMEOUT_S=600 mandatory for .md-heavy (Run #2 lesson)
- python -u unbuffered for live log (Run #1 lesson)
- SKIP_DIRS relative-to-root (not implemented here; single-file input)
- Idempotency via .processed.json (Lesson from youtube-takeout-to-lifeos)
"""
from __future__ import annotations

import json
import logging
import os
import re
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path

# Force unbuffered output for live logging (D6 Run #1 lesson)
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("transcript-swarm")

DEFAULT_CHUNK_SIZE = 2000
DEFAULT_WORKERS = 8
DEFAULT_TIMEOUT_S = 600

SAFE_SLUG_RE = re.compile(r"[^a-zA-Z0-9_-]+")


@dataclass(frozen=True)
class ChunkInfo:
    chunk_id: int
    file: str
    char_start: int
    char_end: int
    chars: int


@dataclass(frozen=True)
class DispatchManifest:
    transcript_path: str
    video_id: str
    safe_title: str
    total_chars: int
    chunk_size: int
    n_chunks: int
    handoff_root: str
    workers_planned: int
    timeout_s: int
    chunks: list[ChunkInfo]


def detect_video_id(path: Path) -> str:
    """Best-effort video_id extraction from filename (e.g. ow1we5PzK-o_luke-alvoeiro.md → ow1we5PzK-o)."""
    stem = path.stem
    # Common patterns: 11-char ID prefix or middle token
    candidates = re.findall(r"[A-Za-z0-9_-]{11}", stem)
    if candidates:
        return candidates[0]
    # Fallback: hash of stem
    import hashlib
    return hashlib.md5(stem.encode("utf-8")).hexdigest()[:11]


def safe_title_from_path(path: Path) -> str:
    """Convert stem to filesystem-safe slug (max 60 chars)."""
    stem = path.stem
    slug = SAFE_SLUG_RE.sub("-", stem).strip("-").lower()
    return slug[:60] if slug else "untitled"


def load_processed(handoff_root: Path) -> dict[str, dict]:
    """Load idempotency tracker. Empty dict if missing/corrupt."""
    p = handoff_root / ".processed.json"
    if not p.exists():
        return {}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        return {}


def save_processed(handoff_root: Path, state: dict[str, dict]) -> None:
    """Atomic write (tmp + rename)."""
    p = handoff_root / ".processed.json"
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(p)


def chunk_text(text: str, chunk_size: int) -> list[tuple[int, int, str]]:
    """Split text into chunks respecting paragraph boundaries when possible.
    Returns list of (start, end, chunk_text) tuples.

    Strategy: try to break on \\n\\n first, fall back to sentence (. ! ?), fall back to char boundary.
    D6 nuance: never break mid-word (look ahead for whitespace).
    """
    chunks: list[tuple[int, int, str]] = []
    pos = 0
    n = len(text)
    while pos < n:
        end = min(pos + chunk_size, n)
        if end < n:
            # Try paragraph boundary
            para_break = text.rfind("\n\n", pos, end)
            if para_break > pos + chunk_size // 2:
                end = para_break + 2
            else:
                # Try sentence boundary
                for punct in ".!?":
                    sent_break = text.rfind(punct, pos, end)
                    if sent_break > pos + chunk_size // 2:
                        end = sent_break + 1
                        break
                else:
                    # Try whitespace boundary
                    ws_break = text.rfind(" ", pos, end)
                    if ws_break > pos + chunk_size // 2:
                        end = ws_break + 1
        chunk = text[pos:end]
        chunks.append((pos, end, chunk))
        pos = end
    return chunks


def main() -> int:
    transcript_path = Path(os.environ.get("TRANSCRIPT_PATH", ""))
    if not transcript_path or not transcript_path.exists():
        log.error("TRANSCRIPT_PATH unset or file missing: %s", transcript_path)
        log.error("Set TRANSCRIPT_PATH=/abs/path/to/transcript.md and re-run.")
        return 2

    chunk_size = int(os.environ.get("CHUNK_SIZE", str(DEFAULT_CHUNK_SIZE)))
    workers_planned = min(int(os.environ.get("WORKERS", str(DEFAULT_WORKERS))), 12)
    timeout_s = int(os.environ.get("TIMEOUT_S", str(DEFAULT_TIMEOUT_S)))
    force = os.environ.get("FORCE", "0") == "1"

    handoff_date = os.environ.get("HANDOFF_DATE", time.strftime("%Y-%m-%d"))
    default_root = Path(
        rf"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\youtube_ingest_{handoff_date}"
    )
    handoff_root = Path(os.environ.get("HANDOFF_ROOT", str(default_root)))

    log.info("transcript=%s | handoff=%s | chunk_size=%d | workers=%d | timeout_s=%d | force=%s",
             transcript_path, handoff_root, chunk_size, workers_planned, timeout_s, force)

    # Read transcript
    text = transcript_path.read_text(encoding="utf-8", errors="replace")
    log.info("loaded transcript: %d chars", len(text))

    # Video ID + safe title
    video_id = detect_video_id(transcript_path)
    safe_title = safe_title_from_path(transcript_path)
    log.info("video_id=%s safe_title=%s", video_id, safe_title)

    # Idempotency check
    handoff_root.mkdir(parents=True, exist_ok=True)
    processed = load_processed(handoff_root)
    if video_id in processed and not force:
        log.warning("video_id=%s already processed (date=%s). Set FORCE=1 to re-process.",
                    video_id, processed[video_id].get("date"))
        log.info("Existing handoff: %s", processed[video_id].get("handoff"))
        return 0

    # Chunk
    raw_chunks = chunk_text(text, chunk_size)
    log.info("chunked: %d chunks (sizes min=%d max=%d avg=%d)",
             len(raw_chunks),
             min(len(c) for _, _, c in raw_chunks) if raw_chunks else 0,
             max(len(c) for _, _, c in raw_chunks) if raw_chunks else 0,
             sum(len(c) for _, _, c in raw_chunks) // len(raw_chunks) if raw_chunks else 0)

    if len(raw_chunks) > workers_planned:
        log.warning("chunks=%d > workers=%d: %d chunks will be queued after first batch",
                    len(raw_chunks), workers_planned, len(raw_chunks) - workers_planned)

    # Stage chunks + audit transcript copy
    chunks_dir = handoff_root / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)
    outputs_dir = chunks_dir / "outputs"
    outputs_dir.mkdir(parents=True, exist_ok=True)

    # Copy transcript to transcripts/ for audit trail (D4 append-only)
    transcripts_dir = handoff_root / "transcripts"
    transcripts_dir.mkdir(parents=True, exist_ok=True)
    audit_file = transcripts_dir / f"01-{video_id}__{safe_title}.md"
    if not audit_file.exists():
        audit_file.write_text(text, encoding="utf-8")
        log.info("audit transcript written: %s (%d chars)", audit_file, len(text))

    chunk_infos: list[ChunkInfo] = []
    for i, (start, end, chunk_text_content) in enumerate(raw_chunks):
        chunk_file = chunks_dir / f"chunk_{i:03d}.md"
        header = (
            f"# Chunk {i:03d} of {len(raw_chunks)}\n"
            f"video_id: {video_id}\n"
            f"chars: {start}-{end} ({end - start} chars)\n"
            f"---\n\n"
        )
        chunk_file.write_text(header + chunk_text_content, encoding="utf-8")
        chunk_infos.append(ChunkInfo(
            chunk_id=i,
            file=str(chunk_file.relative_to(handoff_root)),
            char_start=start,
            char_end=end,
            chars=end - start,
        ))

    # Dispatch manifest for A2 to launch sub-agents
    dispatch = {
        "transcript_path": str(transcript_path),
        "video_id": video_id,
        "safe_title": safe_title,
        "total_chars": len(text),
        "chunk_size": chunk_size,
        "n_chunks": len(raw_chunks),
        "handoff_root": str(handoff_root),
        "workers_planned": workers_planned,
        "timeout_s": timeout_s,
        "chunks": [asdict(ci) for ci in chunk_infos],
        "worker_prompt_template": (
            "Read ONLY the file {chunk_file}. Return STRICT JSON, no prose: "
            "{{\"insights\": [\"<1-line insight>\", ...], "
            "\"quote\": \"<best 1-line quote verbatim>\", "
            "\"ldxx\": \"<LD01..LD08 or null>\"}}. "
            "DO NOT dump the transcript back. DO NOT read other chunks."
        ),
    }
    dispatch_file = chunks_dir / "dispatch.json"
    dispatch_file.write_text(json.dumps(dispatch, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info("dispatch.json written: %s", dispatch_file)

    manifest = DispatchManifest(
        transcript_path=str(transcript_path),
        video_id=video_id,
        safe_title=safe_title,
        total_chars=len(text),
        chunk_size=chunk_size,
        n_chunks=len(raw_chunks),
        handoff_root=str(handoff_root),
        workers_planned=workers_planned,
        timeout_s=timeout_s,
        chunks=chunk_infos,
    )

    # Summary for A2 to act on
    summary = {
        "video_id": video_id,
        "n_chunks": len(raw_chunks),
        "workers_planned": workers_planned,
        "next_step": (
            f"A2: launch {len(raw_chunks)} sub-agents in parallel (Task tool, run_in_background=true). "
            f"Each agent reads chunks/chunk_NNN.md and returns compact JSON. "
            f"Then run transcript_merge.py to combine outputs."
        ),
        "manifest": asdict(manifest),
    }
    summary_file = handoff_root / "swarm_summary.json"
    summary_file.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info("swarm_summary.json written: %s", summary_file)

    log.info("DONE chunking. Dispatch ready at %s. %d chunks, %d chars total.",
             dispatch_file, len(raw_chunks), len(text))
    return 0


if __name__ == "__main__":
    sys.exit(main())