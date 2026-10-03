import csv
import json
import os
import re
import hashlib
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Set, Optional, Any

@dataclass
class WatchedVideo:
    video_id: str
    url: str
    title: str
    channel_name: str
    channel_id: Optional[str]
    watched_timestamp: str
    source_archive: str
    source_hash: str

@dataclass
class ChannelRecurrence:
    channel_id: str
    channel_name: str
    watched_count: int = 0
    most_recent_watch: Optional[str] = None
    subscribed: bool = False
    return_frequency: int = 0
    videos: List[WatchedVideo] = field(default_factory=list)
    topic_clusters: List[str] = field(default_factory=list)

class ChannelHarvester:
    def __init__(self, out_dir="harvester_output"):
        self.out_dir = Path(out_dir)
        self.out_dir.mkdir(parents=True, exist_ok=True)
        self.snapshots = []
        self.canonical_graph: Dict[str, WatchedVideo] = {}
        self.channel_recurrence: Dict[str, ChannelRecurrence] = {}
        self.promoted_channels: List[str] = []
        self.subscriptions: Set[str] = set()

    def _compute_sha256(self, filepath: Path) -> str:
        sha256_hash = hashlib.sha256()
        try:
            with open(filepath, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception:
            return ""

    def h0_immutable_inventory(self, source_paths: List[str]):
        """Stage H0: Discover candidate Takeout archives, classify, and hash."""
        print("-> Stage H0: Building immutable inventory")
        for path_str in source_paths:
            path = Path(path_str)
            if not path.exists():
                print(f"Warning: path {path} does not exist")
                continue

            # If it's a directory, hash the key files and classify
            key_files = []
            family = "other"
            if "Gemini" in str(path):
                family = "Gemini"
            elif "YouTube" in str(path):
                family = "YouTube"

            if path.is_dir():
                for root, _, files in os.walk(path):
                    if "watch-history.html" in files:
                        family = "YouTube"
                    for file in files:
                        if file in ["watch-history.html", "subscriptions.csv"]:
                            full_path = Path(root) / file
                            key_files.append({
                                "path": str(full_path),
                                "hash": self._compute_sha256(full_path)
                            })
            else:
                if "watch-history.html" in path.name:
                    family = "YouTube"
                key_files.append({
                    "path": str(path),
                    "hash": self._compute_sha256(path)
                })

            snapshot = {
                "id": f"snap_{len(self.snapshots)}",
                "source_path": str(path),
                "archive_timestamp": datetime.now(timezone.utc).isoformat(),
                "family": family,
                "key_files": key_files
            }
            self.snapshots.append(snapshot)
            print(f"Ingested snapshot: {snapshot['id']} ({family})")

        # Save inventory
        inventory_file = self.out_dir / "h0_inventory.json"
        with open(inventory_file, 'w') as f:
            json.dump(self.snapshots, f, indent=2)

    def _parse_watch_history_html(self, file_path: str, snapshot_id: str, file_hash: str):
        # Matches video link, optional channel link (channel/, c/, or @handle), and timestamp
        pattern = re.compile(
            r'<a href="https://www\.youtube\.com/watch\?v=([^"&]+)[^"]*">([^<]+)</a><br>'
            r'(?:<a href="https://www\.youtube\.com/(?:channel/|c/|@)([^"&]+)[^"]*">([^<]+)</a><br>)?'
            r'([^<]+)</div>'
        )

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            for match in pattern.finditer(content):
                v_id, title, c_id, c_name, ts = match.groups()

                # If channel is missing in HTML, default to unknown
                c_id_clean = c_id.strip() if c_id else "unknown_channel"
                c_name_clean = c_name.strip() if c_name else "Unknown Channel"

                # If channel was specified as @handle, prefix or retain cleanly
                if c_id and not c_id_clean.startswith("@") and not c_id_clean.startswith("UC"):
                    # keep as is or format handle
                    pass

                # Check for duplicate canonical identity across snapshots
                if v_id not in self.canonical_graph:
                    self.canonical_graph[v_id] = WatchedVideo(
                        video_id=v_id,
                        url=f"https://www.youtube.com/watch?v={v_id}",
                        title=title.strip(),
                        channel_name=c_name_clean,
                        channel_id=c_id_clean,
                        watched_timestamp=ts.strip(),
                        source_archive=snapshot_id,
                        source_hash=file_hash
                    )

    def _parse_subscriptions_csv(self, file_path: str):
        # Parse Takeout subscriptions CSV properly using csv.reader
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                # Skip header rows
                if "Channel" in row[0] or "Identifiant" in row[0] or "Channel Id" in row[0]:
                    continue
                c_id = row[0].strip()
                if c_id:
                    self.subscriptions.add(c_id)

    def h1_canonical_graph(self):
        """Stage H1: Extract watch history into stable records without duplicate identity."""
        print("-> Stage H1: Building canonical graph")
        for snapshot in self.snapshots:
            if snapshot["family"] != "YouTube":
                continue

            for file_info in snapshot["key_files"]:
                path = file_info["path"]
                if "watch-history.html" in path:
                    self._parse_watch_history_html(path, snapshot["id"], file_info["hash"])
                elif "subscriptions.csv" in path:
                    self._parse_subscriptions_csv(path)

        print(f"Built canonical graph with {len(self.canonical_graph)} unique videos.")

        # Save graph
        graph_file = self.out_dir / "h1_canonical_graph.json"
        with open(graph_file, 'w') as f:
            json.dump({k: asdict(v) for k, v in self.canonical_graph.items()}, f, indent=2)


    def h2_channel_recurrence(self):
        """Stage H2: Build channel-level evidence (recurrence ranking)."""
        print("-> Stage H2: Building channel recurrence")

        for v_id, video in self.canonical_graph.items():
            # Use channel_id if available, otherwise channel_name as fallback ID
            c_key = video.channel_id if video.channel_id else video.channel_name

            if c_key not in self.channel_recurrence:
                self.channel_recurrence[c_key] = ChannelRecurrence(
                    channel_id=c_key,
                    channel_name=video.channel_name,
                    subscribed=(c_key in self.subscriptions)
                )

            cr = self.channel_recurrence[c_key]
            cr.watched_count += 1
            cr.videos.append(video)

            # Simple recency check (string comparison works okay if standard formats,
            # but usually we'd parse the date. We'll leave it as most recently seen in iteration for now,
            # or naive string replace)
            cr.most_recent_watch = video.watched_timestamp # Simplified

            # Simple return frequency heuristic: if they watched more than 1 video, they returned
            cr.return_frequency = cr.watched_count - 1

        # Rank channels by watched count
        ranked_channels = sorted(self.channel_recurrence.values(), key=lambda x: x.watched_count, reverse=True)

        ranking_file = self.out_dir / "h2_channel_ranking.json"
        with open(ranking_file, 'w') as f:
            json.dump([asdict(c) for c in ranked_channels], f, indent=2)

        print(f"Ranked {len(ranked_channels)} channels.")

    def h3_research_expansion(self, promoted_channel_ids: List[str]):
        """Stage H3: Enumerate channel inventory, distinguish watched/unseen, route."""
        print(f"-> Stage H3: Research expansion for {len(promoted_channel_ids)} promoted channels")

        expansion_results = []

        for c_id in promoted_channel_ids:
            if c_id not in self.channel_recurrence:
                print(f"Channel {c_id} not found in historical evidence.")
                continue

            cr = self.channel_recurrence[c_id]
            print(f"Expanding channel: {cr.channel_name} ({c_id})")

            # In a real run, we'd use yt-dlp to get the full inventory
            # We simulate it or run it if available and a URL is provided
            # Let's run yt-dlp flat-playlist if we can
            url = f"https://www.youtube.com/channel/{c_id}"

            # We mock the discovery if we are in testing (using an env var or similar)
            # or just execute yt-dlp
            inventory_urls = []

            cmd = ["yt-dlp", "--flat-playlist", "--dump-json", url]
            try:
                if os.environ.get("MOCK_YTDLP") == "1":
                    # Mock output for testing
                    inventory_urls = [
                        {"id": "mock_unseen_1", "title": "Mock Unseen Video 1"},
                        {"id": cr.videos[0].video_id, "title": "Mock Watched Video"} # overlaps with watched
                    ]
                else:
                    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
                    for line in res.stdout.strip().split('\n'):
                        if not line: continue
                        try:
                            entry = json.loads(line)
                            if entry.get("id"):
                                inventory_urls.append({
                                    "id": entry.get("id"),
                                    "title": entry.get("title", "")
                                })
                        except json.JSONDecodeError:
                            pass
            except Exception as e:
                print(f"Warning: could not enumerate channel inventory via yt-dlp: {e}")

            # Distinguish watched vs unseen
            watched_ids = {v.video_id for v in cr.videos}
            unseen = []
            watched_in_inventory = []

            for item in inventory_urls:
                if item["id"] in watched_ids:
                    watched_in_inventory.append(item)
                else:
                    unseen.append(item)

            # Route to WATCH S1/PAPER with provenance
            # Build structured WATCH S1 candidates preserving provenance from watched videos where applicable
            watch_s1_candidates = []
            for u in unseen[:5]:
                watch_s1_candidates.append({
                    "video_id": u["id"],
                    "url": f"https://www.youtube.com/watch?v={u['id']}",
                    "title": u.get("title", ""),
                    "channel_id": c_id,
                    "channel_name": cr.channel_name,
                    "status": "unseen",
                    "provenance": {
                        "harvester_channel_id": c_id,
                        "promoted_channel": True,
                        "discovered_at": datetime.now(timezone.utc).isoformat()
                    }
                })

            # Also create routing payload for watched items if deep transcript/paper microscope is needed
            paper_candidates = []
            for w_vid in cr.videos[:5]:
                paper_candidates.append({
                    "video_id": w_vid.video_id,
                    "url": w_vid.url,
                    "title": w_vid.title,
                    "channel_id": w_vid.channel_id,
                    "channel_name": w_vid.channel_name,
                    "watched_timestamp": w_vid.watched_timestamp,
                    "status": "watched",
                    "provenance": {
                        "source_archive": w_vid.source_archive,
                        "source_hash": w_vid.source_hash
                    }
                })

            routing_manifest = {
                "channel_id": c_id,
                "channel_name": cr.channel_name,
                "total_inventory": len(inventory_urls),
                "unseen_count": len(unseen),
                "watched_count": len(watched_in_inventory),
                "routed_to_watch_s1": watch_s1_candidates,
                "routed_to_paper_s1": paper_candidates
            }
            expansion_results.append(routing_manifest)

        expansion_file = self.out_dir / "h3_expansion.json"
        with open(expansion_file, 'w') as f:
            json.dump(expansion_results, f, indent=2)

    def generate_report(self):
        """Aggregate report with future monitoring design (Stage H4)."""
        report = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "h0_snapshots": len(self.snapshots),
            "h1_canonical_videos": len(self.canonical_graph),
            "h2_channels_tracked": len(self.channel_recurrence),
            "h4_future_monitoring_design": {
                "strategy": "cron_monitor",
                "target_channels": self.promoted_channels,
                "delta_only": True,
                "description": "Monitor new uploads from promoted recurring channels. Route only meaningful deltas (unseen videos). Do not re-ingest historical corpus every run."
            }
        }

        report_file = self.out_dir / "harvester_report.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)

        return report

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Multi-source Channel Harvester")
    parser.add_argument("sources", nargs="+", help="Paths to Takeout archives or extracted directories")
    parser.add_argument("--out-dir", default="harvester_output", help="Output directory")
    parser.add_argument("--promote-channels", nargs="*", default=[], help="Channel IDs to promote for expansion")
    args = parser.parse_args()

    harvester = ChannelHarvester(out_dir=args.out_dir)
    harvester.h0_immutable_inventory(args.sources)
    harvester.h1_canonical_graph()
    harvester.h2_channel_recurrence()
    if args.promote_channels:
        harvester.promoted_channels = args.promote_channels
        harvester.h3_research_expansion(args.promote_channels)
    report = harvester.generate_report()
    print("Harvester run completed successfully.")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
