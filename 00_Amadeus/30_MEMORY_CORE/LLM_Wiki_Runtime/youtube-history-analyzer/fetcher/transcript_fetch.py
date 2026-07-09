"""
TranscriptFetcher — Fetch YouTube transcripts via yt-dlp or youtube-transcript-api.
Uses Python 3.14 (C:\Python314\python.exe)
"""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

# Check Python version
if sys.version_info < (3, 14):
    print("WARNING: TranscriptFetcher recommends Python 3.14 for full bs4 compatibility")

try:
    import yt_dlp
except ImportError:
    print("Installing yt-dlp...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp", "-q"])
    import yt_dlp

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("Installing youtube-transcript-api...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "youtube-transcript-api", "-q"])
    from youtube_transcript_api import YouTubeTranscriptApi


@dataclass
class TranscriptSegment:
    """A segment of a transcript with timestamps."""
    start: float  # seconds
    duration: float
    text: str


@dataclass
class Transcript:
    """Full transcript for a YouTube video."""
    video_id: str
    language: str
    is_generated: bool  # True = auto-generated, False = manual
    segments: list[TranscriptSegment] = field(default_factory=list)
    full_text: str = ""

    @property
    def word_count(self) -> int:
        return len(self.full_text.split())

    @property
    def duration_seconds(self) -> float:
        if not self.segments:
            return 0.0
        return max(seg.start + seg.duration for seg in self.segments)


def extract_video_id(url: str) -> str | None:
    """Extract video ID from various YouTube URL formats."""
    import re
    patterns = [
        r"[?&]v=([a-zA-Z0-9_-]{11})",
        r"/watch\?v=([a-zA-Z0-9_-]{11})",
        r"youtu\.be/([a-zA-Z0-9_-]{11})",
        r"/embed/([a-zA-Z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def fetch_transcript_yttapi(video_id: str) -> Transcript | None:
    """Fetch transcript via youtube-transcript-api (preferred method)."""
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Prefer manual transcripts, then auto-generated
        transcript_data = None
        is_generated = True

        try:
            # Try to get a manually created transcript first
            transcript_data = transcript_list.find_transcript(["en"])
            is_generated = False
        except Exception:
            try:
                # Fall back to any transcript
                transcript_data = transcript_list.find_generated_transcript(["en"])
            except Exception:
                # Try any available language
                available = list(transcript_list)
                if available:
                    transcript_data = available[0]
                    is_generated = transcript_data.is_generated

        if not transcript_data:
            return None

        raw_segments = transcript_data.fetch()
        segments = [
            TranscriptSegment(
                start=seg.start,
                duration=seg.duration,
                text=seg.text,
            )
            for seg in raw_segments
        ]

        full_text = " ".join(seg.text for seg in segments)

        return Transcript(
            video_id=video_id,
            language=transcript_data.language_code,
            is_generated=is_generated,
            segments=segments,
            full_text=full_text,
        )

    except Exception as e:
        return None


def fetch_transcript_ytdlp(video_id: str) -> Transcript | None:
    """Fetch transcript via yt-dlp (fallback method)."""
    output_template = "/tmp/transcript_%(id)s.json"

    ydl_opts = {
        "writeinfojson": False,
        "writeautomaticsub": True,
        "subtitlesformat": "json3",
        "skip_download": True,
        "outtmpl": output_template,
        "quiet": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)

        if not info:
            return None

        # Check for subtitles
        subtitles = info.get("subtitles", {}) or info.get("automatic_captions", {})

        if not subtitles:
            return None

        # Prefer English
        lang = "en" if "en" in subtitles else list(subtitles.keys())[0]
        sub_data = subtitles[lang]

        # Download and parse
        ydl_opts["outtmpl"] = "/tmp/transcript_%(id)s"
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"https://www.youtube.com/watch?v={video_id}"])

        # Parse JSON3 format
        json_path = f"/tmp/transcript_{video_id}.json3"
        if not Path(json_path).exists():
            return None

        with open(json_path, encoding="utf-8") as f:
            import json
            data = json.load(f)

        segments = [
            TranscriptSegment(
                start=seg.get("start", 0),
                duration=seg.get("dur", 0),
                text=seg.get("text", ""),
            )
            for seg in data
            if seg.get("text")
        ]

        full_text = " ".join(seg.text for seg in segments)

        return Transcript(
            video_id=video_id,
            language=lang,
            is_generated=True,
            segments=segments,
            full_text=full_text,
        )

    except Exception:
        return None
    finally:
        # Cleanup temp files
        for ext in ["", ".json3", ".info.json", ".ytdl"]:
            p = Path(f"/tmp/transcript_{video_id}{ext}")
            if p.exists():
                p.unlink()


def fetch_transcript(video_id: str) -> Transcript | None:
    """
    Fetch transcript for a YouTube video.
    Tries youtube-transcript-api first (faster, more reliable),
    falls back to yt-dlp for videos without captions.
    """
    import os
    result = fetch_transcript_yttapi(video_id)
    if result and result.segments:
        return result

    if os.environ.get("SKIP_YTDLP", "False") == "True":
        return None

    result = fetch_transcript_ytdlp(video_id)
    if result and result.segments:
        return result

    return None



def fetch_channel_transcripts(
    video_ids: list[str],
    max_per_channel: int = 10,
) -> Iterator[tuple[str, Transcript | None]]:
    """
    Fetch transcripts for multiple videos.
    Yields (video_id, transcript) tuples.

    Rate limiting: max 10 transcripts per channel to stay within quota.
    """
    for i, video_id in enumerate(video_ids[:max_per_channel]):
        if i > 0 and i % 5 == 0:
            # Brief pause every 5 videos to avoid rate limiting
            import time
            time.sleep(1)

        transcript = fetch_transcript(video_id)
        yield video_id, transcript


if __name__ == "__main__":
    # Quick test
    test_ids = [
        "dO022Y4-Hrg",  # Andrej Karpathy
        "aircA09vn5s",  # Lex Fridman
    ]

    print("Testing transcript fetcher...")
    for vid in test_ids:
        t = fetch_transcript(vid)
        if t:
            print(f"  [{vid}] {t.language} | {len(t.segments)} segments | {t.word_count} words")
        else:
            print(f"  [{vid}] No transcript available")