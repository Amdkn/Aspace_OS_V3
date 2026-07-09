"""
symphony_master.py — Master Orchestrator for the YouTube Takeout sémantique RAG & GTD-DEAL pipeline.
Sovereign Stack ASpace OS V2 — Master Controller.
"""

from __future__ import annotations
import os
import sys
import subprocess
from pathlib import Path

# Set paths
base_dir = Path(__file__).parent
sys.path.append(str(base_dir))

def run_symphony_pipeline(limit: int = 100):
    print("=" * 60)
    print("🧿 A'Space OS V2 — Meta Symphony YouTube Pipeline")
    print("=" * 60)
    
    # Step 1: Ingestion & Capture (GWS Sheets or Frugal CSV)
    print("\n[Phase 1] Launching Ingestion & Capture...")
    from parser.watch_history_parser import parse_watch_history
    from gws_sheets_adapter import adapt_watch_history, LOCAL_CSV_PATH
    
    html_path = r"C:\Users\amado\Downloads\Takeout-YouTube\watch-history.html"
    if not os.path.exists(html_path):
        print(f"[-] Takeout file not found at: {html_path}")
        print("[*] Searching for backup or recently downloaded Takeout HTML...")
        from parser.watch_history_parser import parse_watch_history as test_parse
        # Let the parser auto-locate it
        try:
            # Quick test of import/parse with auto-locate
            dummy = next(test_parse(""))
        except StopIteration:
            pass
        except Exception as e:
            if "watch-history.html not found" in str(e):
                print(f"[-] ERROR: watch-history.html not found. Place it in Downloads and restart.")
                return
    
    print(f"[+] Ingesting from Takeout file. Ingesting up to {limit} new videos...")
    try:
        channels = parse_watch_history(html_path)
        adapt_watch_history(channels, limit=limit)
    except Exception as e:
        print(f"[-] Extraction / Capture failed: {e}")
        return

    # Step 2: Clarification & Sémantique Extraction (Obsidian + Affine + Telegram)
    print("\n[Phase 2 & 3] Launching GTD Clarification & D.E.A.L Actionability...")
    from symphony_gtd_orchestrator import run_clarification_pipeline
    try:
        run_clarification_pipeline()
    except Exception as e:
        print(f"[-] Clarification / D.E.A.L Pipeline failed: {e}")
        return
        
    print("\n" + "=" * 60)
    print("[+] Meta Symphony YouTube Pipeline completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    # Ingest a larger batch for the real execution
    run_symphony_pipeline(limit=50)
