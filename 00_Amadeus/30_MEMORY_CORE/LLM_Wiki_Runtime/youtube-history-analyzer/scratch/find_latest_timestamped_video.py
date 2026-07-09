import csv
import sys
from pathlib import Path

# Force UTF-8 stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

rag_csv = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")

rows = []
with open(rag_csv, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

# Filter for rows that have a full ISO timestamp (contains 'T')
real_takeout_rows = [r for r in rows if r.get('Date Watched') and 'T' in r.get('Date Watched')]

if real_takeout_rows:
    # Sort descending by date
    sorted_takeout = sorted(real_takeout_rows, key=lambda x: x.get('Date Watched'), reverse=True)
    
    print("\n--- 10 LATEST REAL TAKEOUT WATCH EVENTS (WITH TIME) ---")
    for idx, r in enumerate(sorted_takeout[:10], 1):
        print(f"{idx}. Date: {r.get('Date Watched')} | Title: {r.get('Title')} | Channel: {r.get('Channel Name')}")
else:
    print("[-] No real Takeout rows with timestamps found.")
