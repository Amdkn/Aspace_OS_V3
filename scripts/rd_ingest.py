#!/usr/bin/env python3
"""Replayable A'Space R&D ingestion adapter.

Deterministic capture only:
source -> metadata/transcript/keyframes -> Discovery Packet + Evidence Manifest.

Provider order for transcript:
1. --transcript-file (existing WATCH/corpus output)
2. --transcript-command or ASPACE_TRANSCRIPT_CMD (existing transcript-api bridge)
3. yt-dlp native/auto captions fallback

No LLM analysis is performed here. Bill enriches claims/questions afterwards.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shlex
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = ROOT / "_INBOX" / "research_ingest"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def slug(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-")
    return value[:80] or "source"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True, check=True)


def tool_version(name: str, args: list[str]) -> str | None:
    exe = shutil.which(name)
    if not exe:
        return None
    try:
        cp = run([exe, *args])
    except (OSError, subprocess.CalledProcessError):
        return None
    lines = (cp.stdout or cp.stderr).splitlines()
    return lines[0].strip() if lines else "available"


def youtube_id(source: str) -> str | None:
    parsed = urlparse(source)
    host = parsed.netloc.lower().split(":")[0]
    if host in {"youtu.be", "www.youtu.be"}:
        return parsed.path.strip("/").split("/")[0] or None
    if host.endswith("youtube.com"):
        if parsed.path == "/watch":
            return parse_qs(parsed.query).get("v", [None])[0]
        parts = [p for p in parsed.path.split("/") if p]
        if len(parts) >= 2 and parts[0] in {"shorts", "embed", "live"}:
            return parts[1]
    return None


def resolve_watch_skill() -> Path | None:
    override = os.environ.get("ASPACE_WATCH_SKILL")
    if override:
        candidate = Path(override).expanduser()
        if candidate.exists():
            return candidate

    candidates = [
        ROOT / ".agents" / "skills" / "watch",
        Path.home() / ".agents" / "skills" / "watch",
    ]
    cache = Path.home() / ".claude" / "plugins" / "cache" / "claude-video" / "watch"
    if cache.exists():
        candidates.extend(sorted(cache.glob("*/skills/watch"), reverse=True))

    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def parse_vtt(text: str) -> str:
    lines: list[str] = []
    previous = None
    for raw in text.replace("\ufeff", "").splitlines():
        line = raw.strip()
        if not line or line == "WEBVTT":
            continue
        if line.startswith(("NOTE", "STYLE", "Kind:", "Language:")):
            continue
        if "-->" in line or re.fullmatch(r"\d+", line):
            continue
        line = re.sub(r"<[^>]+>", "", line)
        line = re.sub(r"\s+", " ", line).strip()
        if line and line != previous:
            lines.append(line)
            previous = line
    return "\n".join(lines).strip() + ("\n" if lines else "")


def normalize_transcript(text: str, suffix: str = "") -> str:
    if suffix.lower() == ".vtt" or text.lstrip().startswith("WEBVTT"):
        return parse_vtt(text)
    return text.strip() + "\n"


def metadata_for(source: str) -> dict:
    local = Path(source).expanduser()
    if local.exists():
        resolved = local.resolve()
        return {
            "source_type": "local-file",
            "id": sha256_file(resolved)[:16],
            "title": resolved.name,
            "url": None,
            "local_path": str(resolved),
            "size_bytes": resolved.stat().st_size,
            "sha256": sha256_file(resolved),
        }

    cp = run(["yt-dlp", "--dump-single-json", "--skip-download", "--no-playlist", source])
    data = json.loads(cp.stdout)
    return {
        "source_type": "youtube" if youtube_id(source) else "remote-video",
        "id": data.get("id") or youtube_id(source),
        "title": data.get("title"),
        "url": data.get("webpage_url") or source,
        "author": data.get("uploader") or data.get("channel"),
        "date": data.get("upload_date"),
        "duration": data.get("duration"),
        "description": data.get("description"),
        "tags": data.get("tags") or [],
    }


def transcript_from_command(command: str, source: str) -> tuple[str, str]:
    rendered = command.replace("{source}", source)
    cp = run(shlex.split(rendered, posix=os.name != "nt"))
    raw = cp.stdout.strip()
    if not raw:
        raise RuntimeError("transcript command returned empty stdout")

    provider = "transcript-api:bridge"
    try:
        payload = json.loads(raw)
        if isinstance(payload, dict):
            for key in ("transcript", "text", "content"):
                if isinstance(payload.get(key), str):
                    return normalize_transcript(payload[key]), provider
            if isinstance(payload.get("segments"), list):
                chunks = [
                    str(item.get("text", "")).strip()
                    for item in payload["segments"]
                    if isinstance(item, dict) and item.get("text")
                ]
                if chunks:
                    return "\n".join(chunks) + "\n", provider
    except json.JSONDecodeError:
        pass
    return normalize_transcript(raw), provider


def transcript_ytdlp(source: str, run_dir: Path) -> tuple[str, str, Path]:
    pattern = str(run_dir / "transcript.%(ext)s")
    run([
        "yt-dlp", "--skip-download", "--no-playlist",
        "--write-subs", "--write-auto-subs",
        "--sub-langs", "en.*,en,fr.*,fr",
        "--sub-format", "vtt",
        "-o", pattern,
        source,
    ])
    candidates = sorted(run_dir.glob("transcript*.vtt"))
    if not candidates:
        raise RuntimeError("yt-dlp produced no VTT transcript")
    selected = candidates[0]
    return normalize_transcript(
        selected.read_text(encoding="utf-8", errors="replace"),
        selected.suffix,
    ), "yt-dlp:vtt", selected


def ensure_media(source: str, run_dir: Path) -> Path:
    local = Path(source).expanduser()
    if local.exists():
        return local.resolve()
    pattern = str(run_dir / "media.%(ext)s")
    run([
        "yt-dlp", "--no-playlist",
        "-f", "worstvideo[ext=mp4]/worstvideo/worst",
        "-o", pattern,
        source,
    ])
    media = [p for p in run_dir.glob("media.*") if p.is_file()]
    if not media:
        raise RuntimeError("yt-dlp did not produce media")
    return media[0]


def extract_keyframes(media: Path, out_dir: Path, limit: int = 40) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(media),
        "-vf", "select='gt(scene,0.30)',scale=960:-2",
        "-vsync", "vfr", "-frames:v", str(limit),
        str(out_dir / "frame_%04d.jpg"),
    ])
    return sorted(out_dir.glob("frame_*.jpg"))


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def build_packet(
    source: str,
    metadata: dict,
    transcript: str,
    provider: str,
    transcript_sha: str,
    frames: list[Path],
    code_refs: list[str],
    watch_skill: Path | None,
    versions: dict,
) -> dict:
    return {
        "schema": "aspace.discovery-packet.v1",
        "captured_at": now_iso(),
        "source": {
            "input": source,
            "type": metadata.get("source_type"),
            "id": metadata.get("id"),
            "title": metadata.get("title"),
            "author": metadata.get("author"),
            "date": metadata.get("date"),
            "url": metadata.get("url"),
        },
        "capture": {
            "metadata": metadata,
            "transcript": {
                "provider": provider,
                "sha256": transcript_sha,
                "chars": len(transcript),
            },
            "keyframes": [
                {"path": str(frame), "sha256": sha256_file(frame)}
                for frame in frames
            ],
            "code_refs": code_refs,
        },
        "capabilities": {
            "watch_detected": bool(watch_skill),
            "watch_skill": str(watch_skill) if watch_skill else None,
            "yt_dlp": versions.get("yt-dlp"),
            "ffmpeg": versions.get("ffmpeg"),
        },
        "analysis_contract": {
            "claims": [],
            "contradictions": [],
            "unanswered_questions": [],
            "candidate_patterns": [],
            "confidence": None,
            "state": "CAPTURED_NOT_ANALYZED",
            "next_owner": "Bill/DISCOVER",
            "provenance_review": "Graham/REMEMBER",
            "design_return_to": "Clara/DESIGN",
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--transcript-file", type=Path)
    ap.add_argument("--transcript-command")
    ap.add_argument("--keyframes", choices=["none", "balanced"], default="none")
    ap.add_argument("--code-ref", action="append", default=[])
    args = ap.parse_args()

    versions = {
        "yt-dlp": tool_version("yt-dlp", ["--version"]),
        "ffmpeg": tool_version("ffmpeg", ["-version"]),
    }
    if not Path(args.source).expanduser().exists() and not versions["yt-dlp"]:
        raise SystemExit("yt-dlp is required for remote metadata capture")

    metadata = metadata_for(args.source)
    source_id = str(metadata.get("id") or hashlib.sha256(args.source.encode()).hexdigest()[:16])
    run_dir = args.out_dir / slug(source_id)
    run_dir.mkdir(parents=True, exist_ok=True)
    write_json(run_dir / "metadata.json", metadata)

    raw_ref: str
    if args.transcript_file:
        raw = args.transcript_file.read_text(encoding="utf-8", errors="replace")
        transcript = normalize_transcript(raw, args.transcript_file.suffix)
        provider = "file:watch-or-corpus"
        raw_ref = str(args.transcript_file)
    else:
        command = args.transcript_command or os.environ.get("ASPACE_TRANSCRIPT_CMD")
        if command:
            transcript, provider = transcript_from_command(command, args.source)
            raw_ref = "stdout:ASPACE_TRANSCRIPT_CMD"
        else:
            transcript, provider, raw_path = transcript_ytdlp(args.source, run_dir)
            raw_ref = str(raw_path)

    transcript_path = run_dir / "transcript.md"
    transcript_path.write_text(transcript, encoding="utf-8")
    transcript_sha = sha256_file(transcript_path)

    frames: list[Path] = []
    if args.keyframes == "balanced":
        if not versions["ffmpeg"]:
            raise SystemExit("ffmpeg is required for balanced keyframes")
        media = ensure_media(args.source, run_dir)
        frames = extract_keyframes(media, run_dir / "keyframes")

    watch_skill = resolve_watch_skill()
    packet = build_packet(
        args.source, metadata, transcript, provider, transcript_sha,
        frames, args.code_ref, watch_skill, versions,
    )
    packet_path = run_dir / "discovery_packet.json"
    write_json(packet_path, packet)

    evidence = {
        "schema": "aspace.rnd-ingest-evidence.v1",
        "captured_at": now_iso(),
        "source": args.source,
        "run_dir": str(run_dir),
        "artifacts": {
            "metadata": {
                "path": str(run_dir / "metadata.json"),
                "sha256": sha256_file(run_dir / "metadata.json"),
            },
            "transcript": {
                "path": str(transcript_path),
                "sha256": transcript_sha,
                "raw_ref": raw_ref,
            },
            "discovery_packet": {
                "path": str(packet_path),
                "sha256": sha256_file(packet_path),
            },
            "keyframes": len(frames),
        },
        "tool_versions": versions,
        "watch_skill": str(watch_skill) if watch_skill else None,
        "rollback": "Delete this run directory; source and canonical state are untouched.",
        "return_to": ["Bill/DISCOVER", "Graham/REMEMBER", "Clara/DESIGN"],
    }
    evidence_path = run_dir / "evidence_manifest.json"
    write_json(evidence_path, evidence)

    print(json.dumps({
        "run_dir": str(run_dir),
        "discovery_packet": str(packet_path),
        "evidence_manifest": str(evidence_path),
        "transcript_provider": provider,
        "watch_detected": bool(watch_skill),
        "keyframes": len(frames),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
