"""
batch_worker.py — Automate low-level CSV status changes, deduplicated Affine SOP drafts injection, and Telegram alerts.
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import os
import argparse
import csv
from pathlib import Path


# Add parent directory to path to allow importing from other modules
sys.path.append(str(Path(__file__).parent.parent))

from symphony_antigravity.config import LOCAL_CSV_PATH
from deal_symphony_bridge import generate_affine_deal_drafts, notify_a0_engagement

def update_csv_status(video_id: str, new_status: str = "CLARIFIED_PLANE") -> bool:
    """Find the video in watch_history_rag.csv and update its status."""
    if not LOCAL_CSV_PATH.exists():
        print(f"[-] RAG CSV database not found at: {LOCAL_CSV_PATH}")
        return False
        
    rows = []
    updated = False
    
    with open(LOCAL_CSV_PATH, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            if row.get("Issue Identifier") == video_id:
                row["Symphony Status"] = new_status
                updated = True
            rows.append(row)
            
    if updated:
        with open(LOCAL_CSV_PATH, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"[+] Status of video {video_id} updated to {new_status} in watch_history_rag.csv.")
        return True
    else:
        print(f"[-] Video {video_id} not found in CSV database.")
        return False

def main():
    parser = argparse.ArgumentParser(description="Symphony Antigravity Batch Worker Helper.")
    parser.add_argument("--video_id", required=True, help="YouTube Video Identifier (e.g. YT-xxx)")
    parser.add_argument("--title", required=True, help="Title of the video")
    parser.add_argument("--channel", required=True, help="Name of the channel")
    parser.add_argument("--score", type=int, default=7, help="Serendipity score")
    parser.add_argument("--obsidian_file", required=True, help="Obsidian resource filename created")
    parser.add_argument("--draft_sop", required=True, help="Extracted sémantique SOP block")
    parser.add_argument("--status", default="CLARIFIED_PLANE", help="New status to set in CSV")
    
    args = parser.parse_args()
    
    print(f"[*] Symphony Antigravity Helper running for video: {args.video_id}")
    
    # 1. Update CSV database status
    csv_ok = update_csv_status(args.video_id, args.status)
    
    # 2. Inject SOP into Affine Drafts without duplicates
    try:
        generate_affine_deal_drafts(args.title, args.channel, args.draft_sop.strip())
        affine_ok = True
    except Exception as e:
        print(f"[!] Error writing to Affine drafts: {e}")
        affine_ok = False
        
    # 3. Send Telegram engagement alert to A0
    try:
        notify_a0_engagement(args.title, args.channel, args.score, args.obsidian_file)
        telegram_ok = True
    except Exception as e:
        print(f"[!] Error sending Telegram alert: {e}")
        telegram_ok = False
        
    if csv_ok and affine_ok and telegram_ok:
        print(f"[+] Complete workflow successfully automated for video: {args.video_id}")
        sys.exit(0)
    else:
        print(f"[!] Workflow partially failed for video: {args.video_id} (CSV: {csv_ok}, Affine: {affine_ok}, Telegram: {telegram_ok})")
        sys.exit(1)

if __name__ == "__main__":
    main()
