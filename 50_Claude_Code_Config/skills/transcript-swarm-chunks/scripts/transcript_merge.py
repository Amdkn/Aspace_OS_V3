"""
transcript_merge.py — Merge worker outputs into canonical handoff.

Reads chunks/outputs/chunk_NNN.json (one per sub-agent worker), deduplicates insights,
extracts cross-cuts, proposes ADR drafts, writes compact handoff for A0.

Environment variables:
  HANDOFF_ROOT = handoff directory from transcript_swarm.py (REQUIRED)
  TOP_INSIGHTS = max insights in handoff (default: 10)
  ADR_DRAFTS   = max ADR drafts proposed (default: 5)
  FORCE        = "1" to overwrite existing handoff.md

D6 lessons applied:
- 5× retry for missing chunk files (race condition Windows, Run #4 lesson)
- Idempotent — checks .processed.json before rewriting
- Compact output — NEVER dump raw transcript in handoff.md
"""
from __future__ import annotations

import json
import logging
import os
import re
import sys
import time
from collections import Counter
from dataclasses import dataclass, asdict, field
from pathlib import Path

# Force unbuffered output (D6 Run #1 lesson)
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("transcript-merge")

DEFAULT_TOP_INSIGHTS = 10
DEFAULT_ADR_DRAFTS = 5
MAX_RETRIES = 5
RETRY_SLEEP_S = 2.0

# ADR topic extraction regex (heuristic — look for "should/need to/must + verb" patterns)
ADR_TRIGGER_RE = re.compile(
    r"\b(should|need(?:s)? to|must|ought to|require[sd]?|"
    r"recommend|propose|principle|doctrine|rule|always|never)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ChunkOutput:
    chunk_id: int
    insights: list[str]
    quote: str
    ldxx: str | None
    raw: dict


@dataclass
class HandoffData:
    video_id: str
    safe_title: str
    n_chunks: int
    n_outputs_ok: int
    n_outputs_missing: list[int] = field(default_factory=list)
    insights_ranked: list[tuple[str, int]] = field(default_factory=list)  # (insight, frequency)
    cross_cuts: list[tuple[str, int]] = field(default_factory=list)  # (theme, count)
    best_quote: str = ""
    ldxx_consensus: str | None = None
    adr_drafts: list[str] = field(default_factory=list)


def jaccard(a: str, b: str) -> float:
    """Word-set Jaccard similarity (0..1)."""
    wa = set(a.lower().split())
    wb = set(b.lower().split())
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / len(wa | wb)


def dedupe_insights(insights: list[str], threshold: float = 0.7) -> list[str]:
    """Remove near-duplicates (Jaccard >= threshold). Keep first occurrence."""
    kept: list[str] = []
    for ins in insights:
        if not ins or not ins.strip():
            continue
        is_dup = False
        for k in kept:
            if jaccard(ins, k) >= threshold:
                is_dup = True
                break
        if not is_dup:
            kept.append(ins.strip())
    return kept


def extract_cross_cuts(all_insights: list[str], min_count: int = 2) -> list[tuple[str, int]]:
    """Find themes (key noun phrases) appearing in multiple insights."""
    # Simple word-bag frequency (skip stopwords)
    STOPWORDS = frozenset({
        "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "could",
        "should", "may", "might", "must", "to", "of", "in", "for", "on",
        "with", "at", "by", "from", "as", "into", "through", "during", "and",
        "but", "or", "nor", "so", "yet", "both", "either", "neither", "not",
        "only", "own", "same", "than", "too", "very", "can", "this", "that",
        "these", "those", "i", "you", "he", "she", "it", "we", "they", "what",
        "which", "who", "whom", "whose", "where", "when", "why", "how", "all",
        "any", "both", "each", "few", "more", "most", "other", "some", "such",
    })
    word_freq: Counter[str] = Counter()
    for ins in all_insights:
        for w in re.findall(r"[a-zA-ZÀ-ÿ]{4,}", ins.lower()):
            if w not in STOPWORDS:
                word_freq[w] += 1
    # Themes = words appearing min_count+ times
    themes = [(w, c) for w, c in word_freq.most_common() if c >= min_count]
    return themes[:10]  # top 10 cross-cuts


def propose_adr_drafts(all_insights: list[str], max_drafts: int) -> list[str]:
    """Heuristic: insights containing ADR-trigger verbs become ADR drafts.
    Format: 'ADR-DRAFT-NNN: <insight>'
    """
    drafts: list[str] = []
    seen: set[str] = set()
    for ins in all_insights:
        if ADR_TRIGGER_RE.search(ins):
            # Truncate to first 120 chars for draft title
            title = ins.strip()[:120].rstrip(".,;:")
            key = title.lower()
            if key not in seen:
                seen.add(key)
                drafts.append(title)
        if len(drafts) >= max_drafts:
            break
    return drafts


def load_chunk_outputs(chunks_dir: Path, expected_ids: list[int]) -> tuple[list[ChunkOutput], list[int]]:
    """Load chunk_NNN.json outputs. Returns (loaded, missing). 5× retry on race condition."""
    outputs_dir = chunks_dir / "outputs"
    loaded: list[ChunkOutput] = []
    missing: list[int] = []

    for attempt in range(MAX_RETRIES):
        loaded = []
        missing = []
        for cid in expected_ids:
            out_file = outputs_dir / f"chunk_{cid:03d}.json"
            if not out_file.exists():
                missing.append(cid)
                continue
            try:
                raw = json.loads(out_file.read_text(encoding="utf-8"))
                loaded.append(ChunkOutput(
                    chunk_id=cid,
                    insights=raw.get("insights", []),
                    quote=raw.get("quote", ""),
                    ldxx=raw.get("ldxx"),
                    raw=raw,
                ))
            except (json.JSONDecodeError, OSError) as exc:
                log.warning("chunk_%03d: JSON read failed: %s", cid, exc)
                missing.append(cid)
        if not missing:
            break
        if attempt < MAX_RETRIES - 1:
            log.warning("missing %d chunks (attempt %d/%d), retrying in %.1fs...",
                        len(missing), attempt + 1, MAX_RETRIES, RETRY_SLEEP_S)
            time.sleep(RETRY_SLEEP_S)
        else:
            log.warning("after %d attempts, %d chunks still missing: %s",
                        MAX_RETRIES, len(missing), missing)
    return loaded, missing


def load_dispatch(handoff_root: Path) -> dict:
    dispatch_file = handoff_root / "chunks" / "dispatch.json"
    if not dispatch_file.exists():
        raise FileNotFoundError(f"dispatch.json missing: {dispatch_file}")
    return json.loads(dispatch_file.read_text(encoding="utf-8"))


def render_handoff(data: HandoffData, dispatch: dict) -> str:
    """Render compact markdown handoff for A0."""
    lines: list[str] = []
    lines.append(f"# YouTube Ingestion Handoff — {time.strftime('%Y-%m-%d')}")
    lines.append("")
    lines.append(f"**Video**: `{data.video_id}` — {data.safe_title}")
    lines.append(f"**Transcript**: {dispatch['total_chars']} chars → {data.n_chunks} chunks")
    lines.append(f"**Status**: {data.n_outputs_ok}/{data.n_chunks} workers OK" +
                 (f" (missing: {data.n_outputs_missing})" if data.n_outputs_missing else ""))
    if data.ldxx_consensus:
        lines.append(f"**LDxx consensus**: {data.ldxx_consensus}")
    lines.append("")
    lines.append("## Top insights")
    lines.append("")
    for i, (ins, freq) in enumerate(data.insights_ranked, 1):
        if freq > 1:
            lines.append(f"{i}. {ins}  _(×{freq})_")
        else:
            lines.append(f"{i}. {ins}")
    lines.append("")
    if data.cross_cuts:
        lines.append("## Cross-cuts (themes recurring across chunks)")
        lines.append("")
        for theme, count in data.cross_cuts:
            lines.append(f"- **{theme}** — appears in {count} chunks")
        lines.append("")
    if data.best_quote:
        lines.append("## Best quote")
        lines.append("")
        lines.append(f"> {data.best_quote}")
        lines.append("")
    if data.adr_drafts:
        lines.append(f"## {len(data.adr_drafts)} ADR drafts proposed")
        lines.append("")
        for i, draft in enumerate(data.adr_drafts, 1):
            lines.append(f"- ADR-DRAFT-{i:03d}: {draft}")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"_Generated by transcript-swarm-chunks on {time.strftime('%Y-%m-%d %H:%M:%S')}_")
    lines.append(f"_Transcript audit: `transcripts/01-{data.video_id}__{data.safe_title}.md`_")
    return "\n".join(lines)


def main() -> int:
    default_root = Path(
        rf"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\youtube_ingest_{time.strftime('%Y-%m-%d')}"
    )
    handoff_root = Path(os.environ.get("HANDOFF_ROOT", str(default_root)))
    if not handoff_root.exists():
        log.error("HANDOFF_ROOT missing: %s", handoff_root)
        log.error("Run transcript_swarm.py first.")
        return 2

    top_insights_n = int(os.environ.get("TOP_INSIGHTS", str(DEFAULT_TOP_INSIGHTS)))
    adr_drafts_n = int(os.environ.get("ADR_DRAFTS", str(DEFAULT_ADR_DRAFTS)))
    force = os.environ.get("FORCE", "0") == "1"

    log.info("handoff=%s | top_insights=%d | adr_drafts=%d | force=%s",
             handoff_root, top_insights_n, adr_drafts_n, force)

    # Idempotency check
    processed_file = handoff_root / ".processed.json"
    processed: dict[str, dict] = {}
    if processed_file.exists():
        try:
            processed = json.loads(processed_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            processed = {}

    # Load dispatch
    try:
        dispatch = load_dispatch(handoff_root)
    except FileNotFoundError as exc:
        log.error("%s", exc)
        return 2

    video_id = dispatch["video_id"]
    expected_ids = [c["chunk_id"] for c in dispatch["chunks"]]
    chunks_dir = handoff_root / "chunks"

    handoff_file = handoff_root / f"youtube_ingestion_handoff_{time.strftime('%Y-%m-%d')}.md"
    if handoff_file.exists() and not force:
        log.warning("handoff already exists: %s. Set FORCE=1 to overwrite.", handoff_file)
        return 0

    # Load worker outputs (5× retry for Windows race)
    outputs, missing = load_chunk_outputs(chunks_dir, expected_ids)
    log.info("loaded %d outputs, %d missing", len(outputs), len(missing))

    if not outputs:
        log.error("zero worker outputs loaded — aborting")
        return 3

    # Aggregate insights
    all_insights: list[str] = []
    insight_freq: Counter[str] = Counter()
    quotes: list[tuple[str, int]] = []  # (quote, chunk_id)
    ldxx_votes: Counter[str] = Counter()

    for out in outputs:
        deduped = dedupe_insights(out.insights)
        all_insights.extend(deduped)
        for ins in deduped:
            insight_freq[ins] += 1
        if out.quote:
            quotes.append((out.quote, out.chunk_id))
        if out.ldxx and re.match(r"^LD0[1-8]$", out.ldxx):
            ldxx_votes[out.ldxx] += 1

    # Rank insights by frequency then by length (proxy for substance)
    ranked = sorted(insight_freq.items(), key=lambda kv: (-kv[1], -len(kv[0])))
    insights_ranked = ranked[:top_insights_n]

    # Cross-cuts (themes from all insights)
    cross_cuts = extract_cross_cuts(all_insights)

    # Best quote = longest quote from earliest chunk (proxy for representative)
    best_quote = max(quotes, key=lambda q: len(q[0]))[0] if quotes else ""

    # LDxx consensus
    ldxx_consensus = ldxx_votes.most_common(1)[0][0] if ldxx_votes else None

    # ADR drafts from prescriptive insights
    all_ranked_insights = [ins for ins, _ in ranked]
    adr_drafts = propose_adr_drafts(all_ranked_insights, adr_drafts_n)

    data = HandoffData(
        video_id=video_id,
        safe_title=dispatch["safe_title"],
        n_chunks=len(expected_ids),
        n_outputs_ok=len(outputs),
        n_outputs_missing=missing,
        insights_ranked=insights_ranked,
        cross_cuts=cross_cuts,
        best_quote=best_quote,
        ldxx_consensus=ldxx_consensus,
        adr_drafts=adr_drafts,
    )

    handoff_md = render_handoff(data, dispatch)
    handoff_file.write_text(handoff_md, encoding="utf-8")
    log.info("handoff written: %s (%d lines)", handoff_file, len(handoff_md.splitlines()))

    # Update .processed.json (D4 append-only, never mutate existing entries)
    processed[video_id] = {
        "date": time.strftime("%Y-%m-%d"),
        "chunks": len(expected_ids),
        "n_ok": len(outputs),
        "n_missing": len(missing),
        "ldxx": ldxx_consensus,
        "handoff": str(handoff_file.relative_to(handoff_root.parent.parent)),
        "n_insights": len(insights_ranked),
        "n_adr_drafts": len(adr_drafts),
    }
    processed_file.write_text(
        json.dumps(processed, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    log.info(".processed.json updated: %d videos tracked", len(processed))

    # Compact stdout for A0 (NEVER dump transcript)
    print(f"\n=== TRANSCRIPT SWARM MERGE COMPLETE ===")
    print(f"video_id: {video_id}")
    print(f"chunks: {len(outputs)}/{len(expected_ids)} OK" +
          (f" (missing: {missing})" if missing else ""))
    print(f"top insights: {len(insights_ranked)}")
    print(f"cross-cuts: {len(cross_cuts)}")
    print(f"ADR drafts: {len(adr_drafts)}")
    print(f"handoff: {handoff_file}")
    print(f"\nA0: read {handoff_file.name} — NO transcript dump.\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())