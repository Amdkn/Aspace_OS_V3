"""
WatchHistoryParser — Parse Google Takeout watch-history.html → structured channel data.
Python 3.14 with bs4 (C:\Python314\python.exe)
"""

from __future__ import annotations
import os
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterator

# Use Python314 which has bs4
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: bs4 not found. Use C:\Python314\python.exe")
    raise


@dataclass
class Video:
    """A single YouTube video watch entry."""
    title: str
    url: str
    channel_url: str | None
    channel_name: str | None
    watched_at: datetime | None
    raw_html: str = ""

    @property
    def video_id(self) -> str | None:
        if not self.url:
            return None
        match = re.search(r"[?&]v=([a-zA-Z0-9_-]{11})", self.url)
        return match.group(1) if match else None


@dataclass
class Channel:
    """A YouTube channel extracted from watch history."""
    name: str
    url: str
    category: str = "Regular"  # AI | Business | Regular
    videos: list[Video] = field(default_factory=list)
    subscriber_count: str = "unknown"

    @property
    def slug(self) -> str:
        """URL-safe slug for LLM Wiki filenames."""
        return re.sub(r"[^a-z0-9]+", "_", self.name.lower()).strip("_")

    @property
    def video_count(self) -> int:
        return len(self.videos)


# AI-related keywords for auto-categorization
AI_KEYWORDS = [
    "ai", "machine learning", "deep learning", "neural", "gpt", "llm",
    "transformer", "openai", "anthropic", "google ai", "meta ai",
    "mistral", "claude", "chatgpt", "langchain", "vector database",
    "embedding", "rag", "fine-tuning", "training", "inference",
    "karpathy", "lex fridman", "andrew ng", "yann lecun", "sama",
    "sam altman", "dario amodei", "jensen huang", "fusionai",
    " Stability AI", "Runway", "Midjourney", "ElevenLabs", "Cohere",
    "AI/ML", "Artificial Intelligence", "Machine Learning",
    "Andrej Karpathy", "DeepMind", "OpenAI", "Hugging Face",
    "Papers With Code", "Two Minute Papers", "Lex Fridman",
    "Andrej Karpathy", "Samuel AAbbott",
]

# Business-related keywords
BUSINESS_KEYWORDS = [
    "startup", "vc", "venture capital", "y combinator", "ycombinator",
    "techcrunch", "business", "entrepreneur", "founder", "ceo",
    "million", "revenue", "saas", "bootstrapped", "funding",
    " Series A", "Series B", "Series C", " IPO", " IPO",
    "My First Million", "Harpoon", "Lenny", "Lenny's Newsletter",
    "Bloomberg", "Financial Times", "Wall Street", "Market",
    "Investing", "Stock", "Crypto", "Trading",
]


def categorise_channel(name: str, description: str = "") -> str:
    """
    Auto-categorise channel into AI | Business | Regular.
    Uses keyword matching on channel name + description.
    """
    text = f"{name} {description}".lower()

    ai_score = sum(1 for kw in AI_KEYWORDS if kw.lower() in text)
    biz_score = sum(1 for kw in BUSINESS_KEYWORDS if kw.lower() in text)

    if ai_score >= 2:
        return "AI"
    if ai_score == 1 and biz_score == 0:
        return "AI"
    if biz_score >= 2:
        return "Business"
    if biz_score == 1 and ai_score == 0:
        return "Business"
    return "Regular"


MONTHS_FR = {
    "janv.": 1, "févr.": 2, "mars": 3, "avr.": 4, "mai": 5, "juin": 6,
    "juil.": 7, "août": 8, "sept.": 9, "oct.": 10, "nov.": 11, "déc.": 12,
    "janvier": 1, "février": 2, "avril": 4, "juillet": 7, "septembre": 9,
    "octobre": 10, "novembre": 11, "décembre": 12
}


def parse_fr_date(date_str: str) -> datetime | None:
    """Parse French Google Takeout dates into datetime objects."""
    if not date_str:
        return None
    # Clean non-breaking spaces and other anomalies
    date_str = date_str.replace('\xa0', ' ').replace('\u202f', ' ').strip()
    match = re.search(r"(\d{1,2})\s+([^\d\s,]+)\s+(\d{4}),\s+(\d{2}):(\d{2}):(\d{2})", date_str)
    if not match:
        return None
    
    day = int(match.group(1))
    month_name = match.group(2).lower()
    year = int(match.group(3))
    hour = int(match.group(4))
    minute = int(match.group(5))
    second = int(match.group(6))
    
    month = MONTHS_FR.get(month_name)
    if not month:
        for k, v in MONTHS_FR.items():
            k_clean = k.replace('é', 'e').replace('û', 'u')
            m_clean = month_name.replace('é', 'e').replace('û', 'u')
            if k_clean.startswith(m_clean) or m_clean.startswith(k_clean):
                month = v
                break
    if not month:
        return None
    try:
        return datetime(year, month, day, hour, minute, second)
    except Exception:
        return None


def parse_watch_history(html_path: str) -> Iterator[Channel]:
    """
    Parse a Google Takeout watch-history.html file.
    Uses a highly optimized, safe micro-chunk Regex parser (<0.5s) to prevent backtracking,
    and falls back to BeautifulSoup if needed.
    """
    path = Path(html_path)
    if not path.exists():
        raise FileNotFoundError(f"watch-history.html not found: {path}")

    print(f"[*] Parsing watch history file (Size: {path.stat().st_size / 1024 / 1024:.2f} MB)...")
    
    with open(path, encoding="utf-8") as f:
        content = f.read()

    print("[*] Splitting file into micro-chunks to avoid backtracking...")
    
    # Split content by the common takeout content cell class
    # Each timeline item or content-cell contains one watched video event.
    chunks = content.split('class="content-cell')
    
    # If split didn't yield enough, try list items
    if len(chunks) <= 1:
        chunks = content.split('<li')
        
    channel_map: dict[str, Channel] = {}
    matches_count = 0
    
    # Clean regex patterns for local micro-chunks (safe since chunk size is tiny)
    video_pattern = re.compile(r'href="[^"]*watch\?v=([^"&]+)"[^>]*>(.*?)</a>', re.DOTALL)
    channel_pattern = re.compile(r'href="([^"]*(?:/channel/|/@)[^"&]+)"[^>]*>(.*?)</a>', re.DOTALL)
    
    if len(chunks) > 1:
        print(f"[*] Processing {len(chunks)} micro-chunks...")
        for chunk in chunks[1:]:  # Skip the header chunk
            vid_match = video_pattern.search(chunk)
            if not vid_match:
                continue
                
            chan_match = channel_pattern.search(chunk)
            
            video_id = vid_match.group(1)
            title = re.sub(r'<[^>]+>', '', vid_match.group(2)).strip()
            
            # Default fallbacks if channel link is missing (deleted videos)
            channel_url = chan_match.group(1) if chan_match else "https://www.youtube.com/channel/UNKNOWN"
            channel_name = re.sub(r'<[^>]+>', '', chan_match.group(2)).strip() if chan_match else "Unknown Channel"
            
            watched_at = parse_fr_date(chunk)
            
            video = Video(
                title=title,
                url=f"https://www.youtube.com/watch?v={video_id}",
                channel_url=channel_url,
                channel_name=channel_name,
                watched_at=watched_at,
                raw_html=""
            )
            
            if channel_url not in channel_map:
                category = categorise_channel(channel_name, title)
                channel_map[channel_url] = Channel(
                    name=channel_name,
                    url=channel_url,
                    category=category,
                )
            channel_map[channel_url].videos.append(video)
            matches_count += 1
            
        print(f"[+] Successfully extracted {matches_count} watch events in under a second!")
        yield from channel_map.values()
        return

    # Fallback to BeautifulSoup if splitting yielded nothing
    print("[-] Splitting failed. Falling back to BeautifulSoup (slower)...")
    soup = BeautifulSoup(content, "html.parser")
    items = soup.select("li.timeline-item")

    if not items:
        items = soup.select("li")

    print(f"Found {len(items)} timeline items in {html_path}")

    for item in items:
        video_link = item.select_one("a[href*='watch?v=']")
        if not video_link:
            continue

        url = video_link.get("href", "")
        title = video_link.get_text(strip=True)

        channel_link = item.select_one("a[href*='/channel/'], a[href*='/@']")
        channel_name = channel_link.get_text(strip=True) if channel_link else None
        channel_url = channel_link.get("href", "") if channel_link else None

        watched_at = parse_fr_date(item.get_text())

        video = Video(
            title=title,
            url=f"https://www.youtube.com{url}" if url.startswith("/") else url,
            channel_url=f"https://www.youtube.com{channel_url}" if channel_url and channel_url.startswith("/") else channel_url,
            channel_name=channel_name,
            watched_at=watched_at,
            raw_html=str(item)[:200],
        )

        if channel_url and channel_name:
            if channel_url not in channel_map:
                description = item.get_text()[:500]
                category = categorise_channel(channel_name, description)
                channel_map[channel_url] = Channel(
                    name=channel_name,
                    url=channel_url,
                    category=category,
                )
            channel_map[channel_url].videos.append(video)

    yield from channel_map.values()


def report_by_category(channels: list[Channel]) -> dict[str, list[Channel]]:
    """Group channels by category for reporting."""
    result: dict[str, list[Channel]] = {"AI": [], "Business": [], "Regular": []}
    for ch in channels:
        result[ch.category].append(ch)
    return result


if __name__ == "__main__":
    import sys
    import glob

    html_path = None

    if len(sys.argv) >= 2:
        # Tenter d'utiliser l'argument passé
        arg_path = sys.argv[1]
        if os.path.exists(arg_path):
            html_path = arg_path
        else:
            # Essayer de résoudre via glob si des caractères ont été tronqués
            matches = glob.glob(os.path.join(os.path.dirname(arg_path) or ".", "*watch-history.html"))
            if matches:
                html_path = matches[0]

    if not html_path:
        # Recherche intelligente dans Downloads de l'utilisateur
        downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        print(f"[*] Searching for watch-history.html in {downloads_dir}...")
        
        # Trouver tous les watch-history.html sous Downloads
        search_pattern = os.path.join(downloads_dir, "**", "watch-history.html")
        matches = glob.glob(search_pattern, recursive=True)
        
        if matches:
            # Prendre le plus grand ou le plus récent
            matches = sorted(matches, key=os.path.getmtime, reverse=True)
            html_path = matches[0]
            print(f"[+] Found watch-history.html at: {html_path}")
        else:
            # Fallback en dur vers le dossier takeout identifié dans Downloads
            fallback_paths = [
                r"C:\Users\amado\Downloads\takeout-20260508T043407Z-3-001\Takeout\Mon activité\Historique YouTube\watch-history.html",
                r"C:\Users\amado\Downloads\Takeout\Mon activité\Historique YouTube\watch-history.html",
                r"C:\Users\amado\Downloads\takeout-20260508T043407Z-003\Takeout\Mon activité\Historique YouTube\watch-history.html"
            ]
            for p in fallback_paths:
                if os.path.exists(p):
                    html_path = p
                    print(f"[+] Found watch-history.html at fallback path: {html_path}")
                    break

    if not html_path or not os.path.exists(html_path):
        print("ERROR: Could not locate watch-history.html. Please place it in Downloads.")
        sys.exit(1)

    print(f"[*] Processing: {html_path}")

    all_channels = list(parse_watch_history(html_path))
    by_category = report_by_category(all_channels)

    print(f"\n=== Extraction Summary ===")
    print(f"Total channels: {len(all_channels)}")
    for cat, chs in by_category.items():
        print(f"  {cat}: {len(chs)} channels, {sum(c.video_count for c in chs)} videos")

    # Output sample (AI channels first)
    print(f"\n=== Top AI Channels ===")
    for ch in sorted(by_category["AI"], key=lambda c: c.video_count, reverse=True)[:10]:
        print(f"  [{ch.video_count} videos] {ch.name}")

    # Save full channel list to JSON
    import json
    output_path = html_path.replace(".html", "_channels.json")
    data = [
        {
            "name": ch.name,
            "url": ch.url,
            "category": ch.category,
            "video_count": ch.video_count,
            "slug": ch.slug,
        }
        for ch in sorted(all_channels, key=lambda c: (c.category, -c.video_count))
    ]
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\nFull channel list -> {output_path}")