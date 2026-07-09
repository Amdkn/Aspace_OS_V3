"""
gws_sheets_adapter.py — Hybrid Capture Adapter (GWS Sheets Cloud & Local Frugal CSV Fallback).
Sovereign Stack ASpace OS V2 — Phase 1.
"""

from __future__ import annotations
import os
import csv
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Iterator

from parser.watch_history_parser import Channel, Video

# Configuration
LOCAL_CSV_PATH = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")
CONFIG_PATH = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\config.json")


def check_gws_auth() -> bool:
    """Check if the gws CLI tool is globally authenticated."""
    try:
        # Run a simple query with pageSize 1 to check auth status
        args = ["gws", "drive", "files", "list", "--params", '{"pageSize": 1}', "--format", "json"]
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            shell=True,
            encoding="utf-8"
        )
        if result.returncode == 0:
            # Successfully authenticated
            return True
        else:
            return False
    except Exception:
        return False


def load_config() -> dict:
    """Load configuration details (e.g. spreadsheet ID)."""
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_config(config: dict) -> None:
    """Save configuration details persistently."""
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)


def get_or_create_spreadsheet() -> str | None:
    """Get the active Google Sheet ID or create a new one using gws CLI."""
    config = load_config()
    spreadsheet_id = config.get("spreadsheet_id")
    
    if spreadsheet_id:
        return spreadsheet_id

    # Create new Spreadsheet via gws
    print("[*] Creating a new Google Spreadsheet via gws CLI...")
    body = {
        "properties": {
            "title": "ASpace OS V2 — YouTube Takeout RAG Capture"
        }
    }
    
    args = [
        "gws", "sheets", "spreadsheets", "create",
        "--json", json.dumps(body)
    ]
    
    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            shell=True,
            encoding="utf-8"
        )
        if result.returncode == 0:
            res_data = json.loads(result.stdout)
            spreadsheet_id = res_data.get("spreadsheetId")
            if spreadsheet_id:
                print(f"[+] Spreadsheet created successfully! ID: {spreadsheet_id}")
                config["spreadsheet_id"] = spreadsheet_id
                save_config(config)
                
                # Add Header Row to the new spreadsheet
                add_headers_to_sheet(spreadsheet_id)
                return spreadsheet_id
        print(f"[-] Failed to create sheet via gws: {result.stderr}")
    except Exception as e:
        print(f"[-] Exception creating sheet: {e}")
        
    return None


def add_headers_to_sheet(spreadsheet_id: str) -> None:
    """Add the headers row to a newly created sheet."""
    headers = [[
        "Issue Identifier", "Title", "Channel Name", "Channel URL",
        "Duration", "Date Watched", "Transcription Raw", "Serendipity Score",
        "Category", "Symphony Status"
    ]]
    body = {
        "values": headers
    }
    args = [
        "gws", "sheets", "spreadsheets.values.append",
        "--params", f'{{"spreadsheetId": "{spreadsheet_id}", "range": "A1", "valueInputOption": "USER_ENTERED"}}',
        "--json", json.dumps(body)
    ]
    subprocess.run(args, capture_output=True, shell=True)


def push_to_sheets(spreadsheet_id: str, rows: list[list[str]]) -> bool:
    """Append a batch of rows to the Google Sheet using gws CLI."""
    body = {
        "values": rows
    }
    args = [
        "gws", "sheets", "spreadsheets.values.append",
        "--params", f'{{"spreadsheetId": "{spreadsheet_id}", "range": "A1", "valueInputOption": "USER_ENTERED"}}',
        "--json", json.dumps(body)
    ]
    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            shell=True,
            encoding="utf-8"
        )
        if result.returncode == 0:
            return True
        print(f"[-] gws append error: {result.stderr}")
    except Exception as e:
        print(f"[-] Exception pushing to sheets: {e}")
    return False


def push_to_local_csv(rows: list[list[str]]) -> None:
    """Append rows locally to the RAG CSV file."""
    file_exists = LOCAL_CSV_PATH.exists()
    
    with open(LOCAL_CSV_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            # Write Header
            writer.writerow([
                "Issue Identifier", "Title", "Channel Name", "Channel URL",
                "Duration", "Date Watched", "Transcription Raw", "Serendipity Score",
                "Category", "Symphony Status"
            ])
        writer.writerows(rows)
    print(f"[+] Successfully wrote {len(rows)} entries to local RAG CSV: {LOCAL_CSV_PATH}")


def adapt_watch_history(channels: Iterator[Channel], limit: int = 0) -> None:
    """
    Main entry point to capture parsed channels/videos and push them
    to the active adapter (GWS Cloud Sheets or Local Frugal CSV).
    """
    print("[*] Filtering and flattening channels to flat rows...")
    from fetcher.transcript_fetch import fetch_transcript
    
    rows_to_push = []
    
    for channel in channels:
        # Skip unknown or low-quality channels
        if channel.name == "Unknown Channel" or not channel.url or "UNKNOWN" in channel.url:
            continue
            
        for video in channel.videos:
            if not video.watched_at:
                continue
                
            watched_at_str = video.watched_at.isoformat()
            video_id = video.video_id or ""
            
            # 1. Issue Identifier
            issue_id = f"YT-{video_id}"
            
            # 2. Serendipity Score Heuristics
            score = 3
            if channel.category == "AI":
                score = 7
                if any(kw in video.title.lower() for kw in ["rag", "llm", "agent", "autonome", "sovereign", "claude", "gpt", "model", "local"]):
                    score = 9
            elif channel.category == "Business":
                score = 6
                if any(kw in video.title.lower() for kw in ["saas", "startup", "revenue", "bootstrap", "founder", "million"]):
                    score = 8
            
            # 3. Category & Symphony Status
            category = channel.category
            status = "CAPTURED"  # Standard GTD Inbox status
            
            # 4. Fetch Transcription Raw for target videos in the dry-run/batch
            transcription = "Transcription non disponible"
            duration = "unknown"
            
            if score >= 7 and len(rows_to_push) < limit:
                print(f"[*] Fetching transcript for video: {video.title[:45]}...")
                t = fetch_transcript(video_id)
                if t:
                    if t.full_text:
                        transcription = t.full_text
                        print(f"  [+] Transcript fetched successfully ({len(transcription)} chars)!")
                    if t.duration_seconds > 0:
                        duration = f"{int(t.duration_seconds // 60)}m {int(t.duration_seconds % 60)}s"
                else:
                    print("  [-] Transcript not available.")
            
            # Format row
            rows_to_push.append([
                issue_id,
                video.title,
                channel.name,
                channel.url,
                duration,
                watched_at_str,
                transcription,
                str(score),
                category,
                status
            ])
            if limit > 0 and len(rows_to_push) >= limit:
                break
        if limit > 0 and len(rows_to_push) >= limit:
            break

    if not rows_to_push:
        print("[-] No video data to push.")
        return

    # Sort rows by Date Watched (chronological oldest to newest)
    rows_to_push.sort(key=lambda r: r[5])

    print(f"[*] Checking Cloud connectivity (gws CLI)...")
    is_authenticated = check_gws_auth()
    
    if is_authenticated:
        print("[+] gws is authenticated! Pushing to Google Sheets...")
        spreadsheet_id = get_or_create_spreadsheet()
        if spreadsheet_id:
            batch_size = 500
            success = True
            for i in range(0, len(rows_to_push), batch_size):
                batch = rows_to_push[i:i+batch_size]
                if not push_to_sheets(spreadsheet_id, batch):
                    success = False
                    break
            if success:
                print(f"[+] Successfully uploaded {len(rows_to_push)} entries to Google Sheets Cloud!")
                return
            print("[-] Sheet append failed, falling back to local RAG CSV.")
        else:
            print("[-] Google Sheet resolution failed, falling back to local RAG CSV.")
    else:
        print("[-] gws is offline or unauthenticated. Using Sovereign Local Frugal RAG CSV.")

    # Fallback to local CSV
    push_to_local_csv(rows_to_push)


if __name__ == "__main__":
    # Test execution
    print("[*] Running standalone adapter dry-run test (limit 10 items)...")
    from parser.watch_history_parser import parse_watch_history
    
    html_path = r"C:\Users\amado\Downloads\Takeout-YouTube\watch-history.html"
    if os.path.exists(html_path):
        # Delete existing test CSV to avoid duplicates in dry-run
        if LOCAL_CSV_PATH.exists():
            LOCAL_CSV_PATH.unlink()
        channels = parse_watch_history(html_path)
        adapt_watch_history(channels, limit=10)
    else:
        print("[-] Please run watch_history_parser first to verify watch-history.html exists.")
