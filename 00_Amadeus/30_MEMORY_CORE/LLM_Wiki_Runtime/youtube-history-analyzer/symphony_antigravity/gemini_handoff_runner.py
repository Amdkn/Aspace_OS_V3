"""
gemini_handoff_runner.py — Self-contained handoff script for Gemini CLI.

This script is the ENTRY POINT that Gemini CLI executes to take over
the Symphony Antigravity pipeline from where Antigravity left off.

It reads the CSV database, identifies all CAPTURED videos still pending,
regenerates clean batch JSON files, and outputs the execution plan for
Gemini CLI to process sequentially.

Usage (from Gemini CLI):
    python symphony_antigravity/gemini_handoff_runner.py [--batch-size 20] [--dry-run]
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import os
import csv
import json
import argparse
from pathlib import Path
from datetime import datetime

# ── Paths ──────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).parent.parent
CSV_PATH     = PROJECT_ROOT / "watch_history_rag.csv"
GEORDI_DIR   = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides")
AFFINE_DRAFT = GEORDI_DIR / "affine_deal_drafts.md"
BATCH_DIR    = PROJECT_ROOT / "symphony_antigravity" / "handoff_batches"


def load_captured_videos() -> list[dict]:
    """Read CSV and return all rows with Symphony Status == CAPTURED, in order."""
    if not CSV_PATH.exists():
        print(f"[FATAL] CSV not found: {CSV_PATH}")
        sys.exit(1)

    captured = []
    with open(CSV_PATH, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("Symphony Status", "").strip() == "CAPTURED":
                captured.append(row)

    return captured


def partition_batches(videos: list[dict], size: int) -> list[list[dict]]:
    """Split videos into chunks of `size`."""
    return [videos[i:i+size] for i in range(0, len(videos), size)]


def write_batch_files(batches: list[list[dict]]) -> list[dict]:
    """Write each batch to a JSON file and return the manifest."""
    BATCH_DIR.mkdir(parents=True, exist_ok=True)

    manifest = []
    for idx, batch in enumerate(batches, 1):
        batch_id = f"handoff_batch_{idx:03d}"
        batch_file = BATCH_DIR / f"{batch_id}.json"

        payload = []
        for row in batch:
            payload.append({
                "id":         row["Issue Identifier"],
                "title":      row["Title"],
                "channel":    row["Channel Name"],
                "channel_url": row["Channel URL"],
                "duration":   row["Duration"],
                "date":       row["Date Watched"],
                "transcript": row["Transcription Raw"],
                "score":      int(row.get("Serendipity Score", 5)),
                "category":   row.get("Category", "Regular")
            })

        with open(batch_file, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

        manifest.append({
            "batch_id":   batch_id,
            "file":       str(batch_file),
            "size":       len(payload),
            "video_ids":  [v["id"] for v in payload],
            "first_title": payload[0]["title"][:60] if payload else ""
        })

    # Write manifest
    manifest_file = BATCH_DIR / "manifest.json"
    with open(manifest_file, "w", encoding="utf-8") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "total_videos": sum(m["size"] for m in manifest),
            "total_batches": len(manifest),
            "batches": manifest
        }, f, ensure_ascii=False, indent=2)

    return manifest


def update_csv_status(video_id: str, new_status: str = "CLARIFIED_PLANE"):
    """Update a single video's status in the CSV database."""
    rows = []
    fieldnames = None

    with open(CSV_PATH, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            if row.get("Issue Identifier") == video_id:
                row["Symphony Status"] = new_status
            rows.append(row)

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def inject_affine_sop(title: str, channel: str, sop_block: str):
    """Append an SOP draft to affine_deal_drafts.md, with deduplication."""
    marker = f"## 📝 Draft SOP — {title}"

    if AFFINE_DRAFT.exists():
        existing = AFFINE_DRAFT.read_text(encoding="utf-8")
        if marker in existing:
            return  # Already exists, skip

    with open(AFFINE_DRAFT, "a", encoding="utf-8") as f:
        f.write(f"\n{marker} (Chaîne: {channel})\n")
        f.write(f"*Date de capture : {datetime.now().strftime('%Y-%m-%d')}*\n\n")
        f.write(sop_block.strip())
        f.write("\n\n---\n")


def generate_obsidian_filename(title: str) -> str:
    """Generate a slugified filename for the Obsidian resource guide."""
    import re
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s]', '', slug)
    slug = re.sub(r'\s+', '_', slug.strip())
    slug = slug[:80]  # Limit length
    return f"resource_{slug}.md"


def main():
    parser = argparse.ArgumentParser(
        description="Symphony Antigravity → Gemini CLI Handoff Runner"
    )
    parser.add_argument("--batch-size", type=int, default=20,
                        help="Videos per batch (default: 20)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Only generate batches, don't process")
    parser.add_argument("--process-batch", type=str,
                        help="Process a specific batch file (for Gemini CLI sub-invocation)")
    args = parser.parse_args()

    if args.process_batch:
        # Sub-mode: Gemini CLI calls this to process a single batch
        batch_file = Path(args.process_batch)
        if not batch_file.exists():
            print(f"[FATAL] Batch file not found: {batch_file}")
            sys.exit(1)

        with open(batch_file, encoding="utf-8") as f:
            videos = json.load(f)

        print(f"\n{'='*60}")
        print(f"[*] Processing batch: {batch_file.name} ({len(videos)} videos)")
        print(f"{'='*60}\n")

        for i, video in enumerate(videos, 1):
            vid_id = video["id"]
            title  = video["title"]
            channel = video["channel"]

            print(f"\n[{i}/{len(videos)}] {title[:50]}...")
            print(f"  ID: {vid_id} | Channel: {channel}")
            print(f"  Transcript: {len(video.get('transcript',''))} chars")

            # The ACTUAL semantic analysis is done by Gemini CLI's LLM
            # This script just provides the data and handles the I/O
            # Gemini CLI should:
            #   1. Read the transcript
            #   2. Generate the Obsidian guide
            #   3. Call update_csv_status() and inject_affine_sop()

            obsidian_file = generate_obsidian_filename(title)
            obsidian_path = GEORDI_DIR / obsidian_file

            print(f"  → Target Obsidian: {obsidian_file}")
            print(f"  → Status: PENDING GEMINI CLI SEMANTIC PROCESSING")

        print(f"\n[*] Batch {batch_file.name} data loaded. Gemini CLI must now generate the semantic content.")
        return

    # Main mode: Generate batches and print execution plan
    print("\n" + "=" * 70)
    print("   SYMPHONY ANTIGRAVITY → GEMINI CLI HANDOFF")
    print(f"   Generated: {datetime.now().isoformat()}")
    print("=" * 70 + "\n")

    captured = load_captured_videos()
    print(f"[*] Found {len(captured)} videos in CAPTURED status.\n")

    if not captured:
        print("[+] Nothing to process! All videos are already clarified.")
        return

    batches = partition_batches(captured, args.batch_size)
    manifest = write_batch_files(batches)

    print(f"[+] Generated {len(manifest)} batch files in: {BATCH_DIR}\n")

    if args.dry_run:
        print("[DRY RUN] Batch files created. No processing will occur.\n")

    print("─" * 70)
    print("EXECUTION PLAN FOR GEMINI CLI:")
    print("─" * 70)

    for m in manifest:
        print(f"  {m['batch_id']}: {m['size']} videos → {m['file']}")

    print(f"\n  TOTAL: {sum(m['size'] for m in manifest)} videos across {len(manifest)} batches")
    print("─" * 70)

    print(f"\nManifest written to: {BATCH_DIR / 'manifest.json'}")
    print("\n[HANDOFF COMPLETE] Gemini CLI can now begin sequential processing.\n")


if __name__ == "__main__":
    main()
