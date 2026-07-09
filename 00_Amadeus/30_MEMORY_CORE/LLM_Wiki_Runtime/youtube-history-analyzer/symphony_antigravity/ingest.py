"""
ingest.py — Ordered, incremental mass ingestion from Google Takeout to RAG CSV.
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import os
import csv
from pathlib import Path


# Add parent directory to path to allow importing from parser
sys.path.append(str(Path(__file__).parent.parent))

from parser.watch_history_parser import parse_watch_history
from symphony_antigravity.config import LOCAL_CSV_PATH, TAKEOUT_HTML_PATH

def load_existing_identifiers() -> set[str]:
    """Load all existing video IDs from the RAG CSV to guarantee idempotence."""
    ids = set()
    if LOCAL_CSV_PATH.exists():
        with open(LOCAL_CSV_PATH, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("Issue Identifier"):
                    ids.add(row["Issue Identifier"])
    return ids

def calculate_serendipity_score(video_title: str, channel_category: str) -> tuple[int, str]:
    """Compute serendipity score and category based on keywords."""
    score = 3
    category = channel_category
    
    title_lower = video_title.lower()
    
    if channel_category == "AI":
        score = 7
        if any(kw in title_lower for kw in ["rag", "llm", "agent", "autonome", "sovereign", "claude", "gpt", "model", "local"]):
            score = 9
    elif channel_category == "Business":
        score = 6
        if any(kw in title_lower for kw in ["saas", "startup", "revenue", "bootstrap", "founder", "million"]):
            score = 8
            
    return score, category

def run_mass_ingestion(limit: int = 500) -> int:
    """
    Parse the watch-history.html and ingest up to `limit` NEW videos
    that are not already present in the CSV database, preserving chronological order.
    """
    print("=" * 60)
    print(f"[*] Symphony Antigravity — Mass Ingesting up to {limit} new videos...")
    print("=" * 60)
    
    if not TAKEOUT_HTML_PATH.exists():
        print(f"[-] Takeout file not found at: {TAKEOUT_HTML_PATH}")
        return 0
        
    existing_ids = load_existing_identifiers()
    print(f"[*] Loaded {len(existing_ids)} existing video IDs from RAG database.")
    
    new_rows = []
    channels = parse_watch_history(str(TAKEOUT_HTML_PATH))
    
    # Flatten channels and videos to flat chronological rows
    for channel in channels:
        if channel.name == "Unknown Channel" or not channel.url or "UNKNOWN" in channel.url:
            continue
            
        for video in channel.videos:
            if not video.watched_at:
                continue
                
            video_id = video.video_id
            if not video_id:
                continue
                
            issue_id = f"YT-{video_id}"
            
            # Check for duplicates to guarantee incremental continuation
            if issue_id in existing_ids:
                continue
                
            score, category = calculate_serendipity_score(video.title, channel.category)
            
            # Standard status is CAPTURED for target videos (score >= 7), or SKIPPED for regular videos
            status = "CAPTURED" if score >= 7 else "SKIPPED"
            
            new_rows.append([
                issue_id,
                video.title,
                channel.name,
                channel.url,
                "unknown",  # Duration (will be resolved when fetching transcript)
                video.watched_at.isoformat(),
                "Transcription non disponible",
                str(score),
                category,
                status
            ])
            
    if not new_rows:
        print("[+] No new watch events found. Database is perfectly up-to-date!")
        return 0
        
    # Sort new rows chronologically (oldest first) so that we process them in correct temporal sequence
    new_rows.sort(key=lambda r: r[5])
    
    # Keep only the first `limit` rows to respect the batch size request
    rows_to_ingest = new_rows[:limit]
    
    # Append the new records to watch_history_rag.csv
    file_exists = LOCAL_CSV_PATH.exists()
    with open(LOCAL_CSV_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "Issue Identifier", "Title", "Channel Name", "Channel URL",
                "Duration", "Date Watched", "Transcription Raw", "Serendipity Score",
                "Category", "Symphony Status"
            ])
        writer.writerows(rows_to_ingest)
        
    print(f"[+] Successfully ingested {len(rows_to_ingest)} new videos to watch_history_rag.csv!")
    print(f"    - Captured (Inbox) : {sum(1 for r in rows_to_ingest if r[9] == 'CAPTURED')}")
    print(f"    - Skipped (Filtered): {sum(1 for r in rows_to_ingest if r[9] == 'SKIPPED')}")
    print("=" * 60)
    
    return len(rows_to_ingest)

if __name__ == "__main__":
    run_mass_ingestion(limit=500)
