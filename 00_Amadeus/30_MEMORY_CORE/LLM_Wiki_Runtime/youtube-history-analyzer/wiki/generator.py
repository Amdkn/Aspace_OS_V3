"""
WikiGenerator — Generate LLM Wiki entity pages from YouTube watch history graph data.
Reads from Neo4j via GraphitiImporter, generates markdown entity pages.
"""

from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterator

from parser.watch_history_parser import Channel, parse_watch_history
from fetcher.transcript_fetch import Transcript, fetch_transcript, fetch_channel_transcripts

# Wiki output root — relative to this file's location
WIKI_ROOT = Path(__file__).parent.parent / "wiki"
ENTITIES_DIR = WIKI_ROOT / "entities"
SOURCES_DIR = WIKI_ROOT / "sources"


@dataclass
class WikiPage:
    """A generated wiki page."""
    title: str
    slug: str
    category: str  # entities | concepts | sources
    tags: list[str] = field(default_factory=list)
    date: str = field(default_factory=datetime.now().strftime("%Y-%m-%d"))
    body: str = ""

    def to_markdown(self) -> str:
        """Render as Obsidian-compatible markdown with YAML frontmatter."""
        tags_yaml = ", ".join(f"#{t}" for t in self.tags)
        frontmatter = f"""---
source: youtube-history-analyzer
date: {self.date}
type: {self.category}
domain: A0_Sovereign / YouTube_RAG
tags: [{tags_yaml}]
---

# {self.title}
"""
        return frontmatter + self.body


@dataclass
class ChannelEntityPage(WikiPage):
    """Wiki entity page for a YouTube channel."""
    channel: Channel = field(default_factory=Channel)

    def build(self) -> WikiPage:
        """Build entity page from a Channel object."""
        videos = self.channel.videos

        # Build watch timeline summary
        total_watch_time = "unknown"
        if videos:
            earliest = min(v.watched_at for v in videos if v.watched_at)
            latest = max(v.watched_at for v in videos if v.watched_at)
            date_range = f"{earliest.strftime('%Y-%m-%d')} → {latest.strftime('%Y-%m-%d')}" if earliest and latest else "unknown"
        else:
            date_range = "unknown"

        # Top videos by recency
        recent_videos = sorted(videos, key=lambda v: v.watched_at or datetime.min, reverse=True)[:10]
        recent_table = "\n".join(
            f"| [{v.title[:60]}...]({v.url}) | {v.watched_at.strftime('%Y-%m-%d') if v.watched_at else '?'} |"
            for v in recent_videos
        )

        self.title = self.channel.name
        self.slug = self.channel.slug
        self.category = "entities"
        self.tags = ["youtube", "channel", self.channel.category.lower()]

        self.body = f"""## Summary

| Field | Value |
|-------|-------|
| Category | {self.channel.category} |
| URL | [{self.channel.url}]({self.channel.url}) |
| Videos | {self.channel.video_count} |
| Watch period | {date_range} |

## Recent Videos

| Title | Watched |
|-------|---------|
{recent_table}

## Channel Identity

- **Slug**: `{self.channel.slug}`
- **Category**: {self.channel.category}
  - AI channels: ML research, LLM deep dives, AI researchers
  - Business channels: startups, VC, tech business
  - Regular channels: entertainment, education, news

## Transcript Status

Transcripts are fetched on-demand via:
- Primary: `youtube-transcript-api` (manual captions preferred)
- Fallback: `yt-dlp` (auto-generated captions)

Fetch transcripts with:
```python
from fetcher import fetch_channel_transcripts
video_ids = [v.video_id for v in channel.videos if v.video_id]
for vid, transcript in fetch_channel_transcripts(video_ids[:5]):
    if transcript:
        print(f"[{vid}] {transcript.word_count} words")
```

---
*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} from YouTube watch history*
"""
        return self


@dataclass
class CategoryOverviewPage(WikiPage):
    """Wiki entity page for a category of channels (AI or Business)."""
    category: str = "AI"
    channels: list[Channel] = field(default_factory=list)

    def build(self) -> WikiPage:
        sorted_chs = sorted(self.channels, key=lambda c: c.video_count, reverse=True)
        channel_table = "\n".join(
            f"| [{ch.name}](entities/entity_{ch.slug}.md) | {ch.video_count} | {ch.url} |"
            for ch in sorted_chs
        )
        total_videos = sum(c.video_count for c in sorted_chs)

        self.title = f"YouTube — {self.category} Channels"
        self.slug = f"youtube_{self.category.lower()}_channels"
        self.category = "entities"
        self.tags = ["youtube", "channel", self.category.lower(), "overview"]

        self.body = f"""## Overview

This page lists all **{self.category}** channels in the watch history corpus.

| Channel | Videos | URL |
|---------|--------|-----|
{channel_table}

**Total**: {len(sorted_chs)} channels, {total_videos} videos.

## Category Definition

{self._category_description()}

## Top Channels

"""
        for ch in sorted_chs[:5]:
            self.body += f"- **{[{ch.name}]}** — {ch.video_count} videos\n"
        return self

    def _category_description(self) -> str:
        if self.category == "AI":
            return """**AI channels** cover:
- Machine learning, deep learning, neural networks
- LLMs, transformers, RAG, fine-tuning
- AI researchers: Karpathy, Lex Fridman, Yann LeCun, Sam Altman
- AI companies: OpenAI, Anthropic, DeepMind, Mistral, Cohere"""
        elif self.category == "Business":
            return """**Business channels** cover:
- Startups, venture capital, Y Combinator
- TechCrunch, business news, market analysis
- Entrepreneur stories, funding, Series A/B/C
- SaaS, bootstrapping, revenue growth"""
        else:
            return "Regular channels — entertainment, news, education, and general content."


def slugify(text: str) -> str:
    """URL-safe slug for wiki filenames."""
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def generate_channel_entities(channels: list[Channel]) -> Iterator[WikiPage]:
    """Generate entity pages for all channels."""
    for ch in channels:
        page = ChannelEntityPage(channel=ch)
        yield page.build()


def generate_category_overviews(channels: list[Channel]) -> list[WikiPage]:
    """Generate overview pages for AI and Business categories."""
    by_category: dict[str, list[Channel]] = {"AI": [], "Business": [], "Regular": []}
    for ch in channels:
        by_category[ch.category].append(ch)

    pages = []
    for cat in ["AI", "Business"]:
        if by_category[cat]:
            page = CategoryOverviewPage(category=cat, channels=by_category[cat])
            pages.append(page.build())

    return pages


def generate_pipeline_summary(
    channels: list[Channel],
    transcript_stats: dict[str, int] | None = None,
) -> WikiPage:
    """Generate the pipeline entity page (same as entity_youtube_history_rag_pipeline.md)."""
    by_cat = {"AI": 0, "Business": 0, "Regular": 0}
    for ch in channels:
        by_cat[ch.category] += 1

    total_videos = sum(c.video_count for c in channels)

    page = WikiPage(
        title="YouTube History RAG Pipeline",
        slug="entity_youtube_history_rag_pipeline",
        category="entities",
        tags=["youtube", "rag", "graphiti", "neo4j", "pipeline"],
    )

    page.body = f"""## Pipeline Overview

YouTube watch history → temporal knowledge graph → LLM Wiki entity pages.

## Architecture (Phase 1–4)

| Phase | Component | Status |
|-------|-----------|--------|
| 1. Parse | `parser/watch_history_parser.py` | ✅ Complete |
| 2. Fetch | `fetcher/transcript_fetch.py` | ✅ Complete |
| 3. Graph | `graphiti/importer.py` | ✅ Complete |
| 4. Wiki | `wiki/generator.py` | ✅ Complete |

## Channel Statistics

| Category | Channels | Description |
|----------|---------|-------------|
| AI | {by_cat['AI']} | ML, LLMs, AI researchers, OpenAI, Anthropic |
| Business | {by_cat['Business']} | Startups, VC, Y Combinator, TechCrunch |
| Regular | {by_cat['Regular']} | Entertainment, education, general content |

**Total**: {len(channels)} channels, {total_videos} videos across all categories.

## Component Stack

- **Parser**: Python 3.14 + bs4, Google Takeout `watch-history.html`
- **Transcript fetcher**: `youtube-transcript-api` (primary) + `yt-dlp` (fallback)
- **Graph store**: Neo4j 5.26+ via `neo4j` Python driver
- **Knowledge graph**: Graphiti-style episodic temporal graph
- **Wiki output**: Obsidian-compatible markdown with YAML frontmatter

## Data Model

- **Episode** = Channel (time-bounded conversation with a creator)
- **Fact** = Video watch event (video_id, title, watched_at, channel)
- **Transcript** = Full video transcript (when available)

## Files

```
youtube-history-analyzer/
├── parser/
│   ├── watch_history_parser.py   # Channel + Video dataclasses, categorise_channel()
│   └── __init__.py
├── fetcher/
│   ├── transcript_fetch.py       # Transcript, fetch_transcript(), fetch_channel_transcripts()
│   └── __init__.py
├── graphiti/
│   ├── importer.py               # GraphitiImporter, Neo4j bulk import
│   └── __init__.py
└── wiki/
    ├── generator.py              # WikiPage, generate_channel_entities(), generate_category_overviews()
    └── __init__.py
```

## Usage

```bash
# Step 1: Parse watch history
python parser/watch_history_parser.py ~/Downloads/watch-history.html

# Step 2: Import to Neo4j
$env:NEO4J_PASSWORD = "your-password"
python graphiti/importer.py ~/Downloads/watch-history.html --fetch-transcripts

# Step 3: Generate wiki pages
python wiki/generator.py --channels-json watch-history_channels.json
```

---
*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
    return page


def write_wiki_pages(pages: list[WikiPage], output_dir: Path | None = None) -> None:
    """Write wiki pages to disk."""
    if output_dir is None:
        output_dir = WIKI_ROOT

    output_dir.mkdir(parents=True, exist_ok=True)
    ENTITIES_DIR.mkdir(parents=True, exist_ok=True)
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)

    for page in pages:
        if page.category == "entities" and page.slug.startswith("entity_"):
            filepath = ENTITIES_DIR / f"{page.slug}.md"
        elif page.category == "sources":
            filepath = SOURCES_DIR / f"{page.slug}.md"
        else:
            filepath = output_dir / f"{page.slug}.md"

        filepath.write_text(page.to_markdown(), encoding="utf-8")
        print(f"  → {filepath.relative_to(output_dir)}")


# ─── CLI Entry Point ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Generate LLM Wiki pages from YouTube watch history")
    parser.add_argument("html_path", nargs="?", help="Path to watch-history.html")
    parser.add_argument("--channels-json", help="Pre-parsed channels JSON (skip parsing)")
    parser.add_argument("--output-dir", type=Path, help="Wiki output directory")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated")

    args = parser.parse_args()

    # Load or parse channels
    if args.channels_json:
        channels_data = json.loads(Path(args.channels_json).read_text(encoding="utf-8"))
        # Reconstruct Channel objects (simple dict-based for now)
        from parser.watch_history_parser import Channel, Video
        channels = []
        for cd in channels_data:
            videos = [
                Video(
                    title=v["title"],
                    url=v["url"],
                    channel_url=v.get("channel_url"),
                    channel_name=v.get("channel_name"),
                    watched_at=datetime.fromisoformat(v["watched_at"]) if v.get("watched_at") else None,
                )
                for v in cd.get("videos", [])
            ]
            ch = Channel(
                name=cd["name"],
                url=cd["url"],
                category=cd.get("category", "Regular"),
                videos=videos,
            )
            channels.append(ch)
    elif args.html_path:
        channels = list(parse_watch_history(args.html_path))
        # Save intermediate channels JSON
        channels_json_path = Path(args.html_path).with_name("watch-history_channels.json")
        json.dump(
            [
                {
                    "name": ch.name,
                    "url": ch.url,
                    "category": ch.category,
                    "slug": ch.slug,
                    "video_count": ch.video_count,
                    "videos": [
                        {
                            "title": v.title,
                            "url": v.url,
                            "video_id": v.video_id,
                            "watched_at": v.watched_at.isoformat() if v.watched_at else None,
                        }
                        for v in ch.videos
                    ],
                }
                for ch in channels
            ],
            open(channels_json_path, "w", encoding="utf-8"),
            ensure_ascii=False,
            indent=2,
        )
        print(f"Channels saved to {channels_json_path}")
    else:
        print("ERROR: Provide --channels-json or <html_path>")
        sys.exit(1)

    print(f"Loaded {len(channels)} channels, {sum(c.video_count for c in channels)} total videos")

    if args.dry_run:
        for ch in channels[:5]:
            print(f"  [{ch.category}] {ch.name} ({ch.video_count} videos)")
        print(f"  ... ({len(channels) - 5} more)")
        sys.exit(0)

    # Generate pages
    print("Generating wiki pages...")
    pages: list[WikiPage] = []

    # Pipeline summary
    pages.append(generate_pipeline_summary(channels))

    # Category overviews
    pages.extend(generate_category_overviews(channels))

    # Individual channel entities
    pages.extend(list(generate_channel_entities(channels)))

    print(f"Generated {len(pages)} pages:")
    print(f"  1 pipeline overview")
    print(f"  {len(channels)} channel entity pages")
    print(f"  2 category overview pages")

    write_wiki_pages(pages, args.output_dir)
    print(f"\nWiki pages written to: {args.output_dir or WIKI_ROOT}")