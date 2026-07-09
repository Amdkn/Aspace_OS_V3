"""
GraphitiImporter — Import YouTube watch history into Neo4j via Graphiti / Neo4j Driver.
Uses Python 3.14 with neo4j driver (pip install neo4j).
"""

from __future__ import annotations

import os
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterator, Any

from parser.watch_history_parser import Channel, Video, parse_watch_history
from fetcher.transcript_fetch import Transcript, fetch_transcript

try:
    from neo4j import GraphDatabase
except ImportError:
    print("Installing neo4j driver...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "neo4j", "-q"])
    from neo4j import GraphDatabase


@dataclass
class GraphitiConfig:
    """Configuration for Graphiti / Neo4j connection."""
    uri: str = "bolt://localhost:7687"
    user: str = "neo4j"
    password: str = ""  # Set via NEO4J_PASSWORD env var
    database: str = "neo4j"
    ttl_minutes: int = 60  # Episode TTL before re-generation

    @classmethod
    def from_env(cls) -> GraphitiConfig:
        """Load from environment variables."""
        return cls(
            uri=os.environ.get("NEO4J_URI", "bolt://localhost:7687"),
            user=os.environ.get("NEO4J_USER", "neo4j"),
            password=os.environ.get("NEO4J_PASSWORD", ""),
            database=os.environ.get("NEO4J_DATABASE", "neo4j"),
        )


def build_graphiti_config() -> GraphitiConfig:
    """Build Graphiti config, prompting for password if missing."""
    config = GraphitiConfig.from_env()
    if not config.password:
        print("WARNING: NEO4J_PASSWORD not set. Set it via:")
        print("  [Environment]::SetEnvironmentVariable('NEO4J_PASSWORD', 'your-password', 'User')")
    return config


@dataclass
class EpisodeNode:
    """A channel as a Graphiti episode node."""
    name: str
    url: str
    category: str  # AI | Business | Regular
    video_count: int
    slug: str
    created_at: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "url": self.url,
            "category": self.category,
            "video_count": self.video_count,
            "slug": self.slug,
            "created_at": self.created_at.isoformat(),
        }


@dataclass
class FactNode:
    """A video watch event as a Graphiti fact node."""
    video_id: str
    title: str
    watched_at: datetime | None
    channel_name: str
    channel_slug: str
    transcript_available: bool = False
    transcript_text: str = ""
    language: str = ""
    is_generated: bool = False

    @property
    def fact_id(self) -> str:
        """Stable fact reference = video_id."""
        return self.video_id

    def to_dict(self) -> dict[str, Any]:
        return {
            "video_id": self.video_id,
            "title": self.title,
            "watched_at": self.watched_at.isoformat() if self.watched_at else None,
            "channel_name": self.channel_name,
            "channel_slug": self.channel_slug,
            "transcript_available": self.transcript_available,
            "language": self.language,
            "is_generated": self.is_generated,
        }


class GraphitiImporter:
    """
    Import YouTube watch history into Neo4j via Graphiti-style temporal graph.
    Episode = Channel (time-bounded conversation with the channel)
    Facts = Individual video watch events with metadata
    """

    def __init__(self, config: GraphitiConfig):
        self.config = config
        self._driver = None

    def _connect(self) -> Any:
        """Lazy connect to Neo4j."""
        if self._driver is None:
            self._driver = GraphDatabase.driver(
                self.config.uri,
                auth=(self.config.user, self.config.password),
                max_connection_lifetime=3600,
            )
        return self._driver

    def close(self) -> None:
        if self._driver:
            self._driver.close()
            self._driver = None

    def verify_connection(self) -> bool:
        """Test Neo4j connectivity."""
        try:
            with self._connect().session(database=self.config.database) as session:
                result = session.run("RETURN 1 AS n")
                return result.single() is not None
        except Exception as e:
            print(f"Neo4j connection failed: {e}")
            return False

    # ─── Episode (Channel) Operations ───────────────────────────────────────

    def upsert_episode(self, episode: EpisodeNode) -> str:
        """
        Upsert a channel episode node.
        Returns episode_uuid.
        """
        cypher = """
        MERGE (e:Episode {slug: $slug})
        SET e.name = $name,
            e.url = $url,
            e.category = $category,
            e.video_count = $video_count,
            e.updated_at = datetime(),
            e.created_at = coalesce(e.created_at, datetime())
        RETURN e.slug AS slug
        """
        with self._connect().session(database=self.config.database) as session:
            result = session.run(
                cypher,
                name=episode.name,
                url=episode.url,
                category=episode.category,
                video_count=episode.video_count,
                slug=episode.slug,
            )
            return result.single()["slug"]

    # ─── Fact (Video Watch) Operations ────────────────────────────────────────

    def upsert_fact(self, fact: FactNode, episode_slug: str) -> str:
        """
        Upsert a video watch fact node linked to an episode.
        Returns fact_uuid (video_id).
        """
        cypher = """
        MATCH (e:Episode {slug: $episode_slug})
        MERGE (f:Fact {video_id: $video_id})
        SET f.title = $title,
            f.watched_at = $watched_at,
            f.channel_name = $channel_name,
            f.transcript_available = $transcript_available,
            f.transcript_language = $language,
            f.is_generated_caption = $is_generated,
            f.updated_at = datetime()
        MERGE (f)-[:BELONGS_TO_EPISODE]->(e)
        RETURN f.video_id AS video_id
        """
        watched_at = fact.watched_at.isoformat() if fact.watched_at else None
        with self._connect().session(database=self.config.database) as session:
            result = session.run(
                cypher,
                video_id=fact.video_id,
                title=fact.title,
                watched_at=watched_at,
                channel_name=fact.channel_name,
                episode_slug=episode_slug,
                transcript_available=fact.transcript_available,
                language=fact.language,
                is_generated=fact.is_generated,
            )
            return result.single()["video_id"]

    def link_transcript(self, video_id: str, transcript: Transcript) -> None:
        """Attach transcript text to an existing fact node."""
        cypher = """
        MATCH (f:Fact {video_id: $video_id})
        SET f.transcript_text = $full_text,
            f.transcript_word_count = $word_count,
            f.transcript_duration_sec = $duration,
            f.transcript_language = $language,
            f.updated_at = datetime()
        """
        with self._connect().session(database=self.config.database) as session:
            session.run(
                cypher,
                video_id=video_id,
                full_text=transcript.full_text[:32000],  # Neo4j string limit safety
                word_count=transcript.word_count,
                duration=transcript.duration_seconds,
                language=transcript.language,
            )

    # ─── Bulk Import Pipeline ─────────────────────────────────────────────────

    def import_channel(self, channel: Channel) -> tuple[int, int]:
        """
        Import a full channel (all videos as facts).
        Returns (episode_uuid, fact_count).
        """
        episode = EpisodeNode(
            name=channel.name,
            url=channel.url,
            category=channel.category,
            video_count=channel.video_count,
            slug=channel.slug,
        )
        self.upsert_episode(episode)

        fact_count = 0
        for video in channel.videos:
            vid = video.video_id
            if not vid:
                continue
            fact = FactNode(
                video_id=vid,
                title=video.title,
                watched_at=video.watched_at,
                channel_name=channel.name,
                channel_slug=channel.slug,
            )
            self.upsert_fact(fact, channel.slug)
            fact_count += 1

        return channel.slug, fact_count

    def import_channels(
        self,
        channels: list[Channel],
        fetch_transcripts: bool = False,
        max_transcripts_per_channel: int = 5,
    ) -> Iterator[tuple[str, int, int | None]]:
        """
        Import multiple channels with optional transcript fetching.

        Yields: (channel_slug, fact_count, transcript_count)
        """
        for ch in channels:
            slug, fact_count = self.import_channel(ch)
            transcript_count: int | None = None

            if fetch_transcripts:
                video_ids = [v.video_id for v in ch.videos if v.video_id]
                transcripts_fetched = 0

                for i, vid in enumerate(video_ids[:max_transcripts_per_channel]):
                    if i > 0 and i % 5 == 0:
                        time.sleep(1)  # Rate limit

                    t = fetch_transcript(vid)
                    if t and t.segments:
                        try:
                            self.link_transcript(vid, t)
                            transcripts_fetched += 1
                        except Exception as e:
                            print(f"  [WARN] Transcript link failed for {vid}: {e}")

                transcript_count = transcripts_fetched

            yield slug, fact_count, transcript_count

    def get_stats(self) -> dict[str, int]:
        """Return graph statistics."""
        queries = {
            "episodes": "MATCH (e:Episode) RETURN count(e) AS c",
            "facts": "MATCH (f:Fact) RETURN count(f) AS c",
            "facts_with_transcript": "MATCH (f:Fact) WHERE f.transcript_available = true RETURN count(f) AS c",
            "ai_episodes": "MATCH (e:Episode {category: 'AI'}) RETURN count(e) AS c",
            "business_episodes": "MATCH (e:Episode {category: 'Business'}) RETURN count(e) AS c",
        }
        stats = {}
        with self._connect().session(database=self.config.database) as session:
            for key, q in queries.items():
                try:
                    result = session.run(q)
                    stats[key] = result.single()["c"]
                except Exception:
                    stats[key] = -1
        return stats


def episode_nodes(channels: list[Channel]) -> list[EpisodeNode]:
    """Convert Channel objects to EpisodeNode list."""
    return [
        EpisodeNode(
            name=ch.name,
            url=ch.url,
            category=ch.category,
            video_count=ch.video_count,
            slug=ch.slug,
        )
        for ch in channels
    ]


# ─── CLI Entry Point ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Import YouTube watch history into Neo4j")
    parser.add_argument("html_path", nargs="?", help="Path to watch-history.html")
    parser.add_argument("--neo4j-password", help="Neo4j password (or set NEO4J_PASSWORD env var)")
    parser.add_argument("--fetch-transcripts", action="store_true", help="Also fetch transcripts")
    parser.add_argument("--max-transcripts", type=int, default=5, help="Max transcripts per channel")
    parser.add_argument("--dry-run", action="store_true", help="Parse only, don't import")

    args = parser.parse_args()

    # Resolve password
    if args.neo4j_password:
        os.environ["NEO4J_PASSWORD"] = args.neo4j_password

    if not args.html_path:
        # Default Google Takeout path
        default_path = os.path.join(
            os.path.expanduser("~"),
            "Downloads",
            "takeout-20260508T043407Z-3-001",
            "Takeout",
            "Mon activité",
            "Historique YouTube",
            "watch-history.html",
        )
        if os.path.exists(default_path):
            args.html_path = default_path
        else:
            print(f"ERROR: watch-history.html not found at default path.")
            print(f"Usage: python importer.py <path_to_watch-history.html>")
            sys.exit(1)

    print(f"Parsing: {args.html_path}")
    channels = list(parse_watch_history(args.html_path))
    print(f"Found {len(channels)} channels")

    if args.dry_run:
        for ch in channels[:10]:
            print(f"  [{ch.category}] {ch.name} ({ch.video_count} videos)")
        print(f"  ... ({len(channels) - 10} more)")
        sys.exit(0)

    # Connect to Neo4j
    config = build_graphiti_config()
    if not config.password:
        print("ERROR: NEO4J_PASSWORD required. Set it or pass --neo4j-password")
        sys.exit(1)

    importer = GraphitiImporter(config)
    if not importer.verify_connection():
        print("ERROR: Could not connect to Neo4j. Check URI/credentials.")
        sys.exit(1)

    print("Connected to Neo4j. Starting import...")
    imported = 0

    for slug, fact_count, transcript_count in importer.import_channels(
        channels,
        fetch_transcripts=args.fetch_transcripts,
        max_transcripts_per_channel=args.max_transcripts,
    ):
        print(f"  [{slug}] {fact_count} facts", end="")
        if transcript_count is not None:
            print(f" | {transcript_count} transcripts", end="")
        print()
        imported += 1

    stats = importer.get_stats()
    print(f"\n=== Import Complete ===")
    print(f"Channels imported: {imported}")
    print(f"Total episodes: {stats.get('episodes', '?')}")
    print(f"Total facts: {stats.get('facts', '?')}")
    print(f"AI episodes: {stats.get('ai_episodes', '?')}")
    print(f"Business episodes: {stats.get('business_episodes', '?')}")

    importer.close()