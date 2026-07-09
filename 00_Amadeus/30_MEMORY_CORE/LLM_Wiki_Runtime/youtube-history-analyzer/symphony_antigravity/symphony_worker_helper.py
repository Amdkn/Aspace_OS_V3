import sys
import os
import csv
import re
from pathlib import Path
from datetime import datetime

# Configuration
GEORDI_DIR = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides")
CSV_PATH = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")
AFFINE_DRAFT = GEORDI_DIR / "affine_deal_drafts.md"

def update_status(video_id, status="CLARIFIED_PLANE"):
    rows = []
    fieldnames = None
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            if row.get("Issue Identifier") == video_id:
                row["Symphony Status"] = status
            rows.append(row)
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def inject_deal_block(full_deal_text):
    # Appends the whole block to the file
    with open(AFFINE_DRAFT, "a", encoding="utf-8") as f:
        f.write("\n" + full_deal_text.strip() + "\n\n---\n")

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "bulk_update":
        ids = sys.argv[2].split(",")
        deal_file = sys.argv[3]
        
        with open(deal_file, "r", encoding="utf-8") as f:
            deal_content = f.read()
            
        for vid_id in ids:
            update_status(vid_id)
        
        inject_deal_block(deal_content)
        print(f"Bulk updated {len(ids)} videos and injected DEAL block.")
