import csv
import sys
from pathlib import Path

# Force UTF-8 stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

rag_csv = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")

if not rag_csv.exists():
    print(f"[-] RAG CSV not found at {rag_csv}")
    sys.exit(1)

latest_row = None

# Let's read all rows and find the last one by chronological order or file order
# In many watch history Takeouts, the order is reverse-chronological (newest at the top) or chronological (newest at the bottom).
# Let's parse all rows and inspect the date format.
rows = []
with open(rag_csv, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

print(f"[*] Total rows in RAG CSV: {len(rows)}")

# Let's inspect the first 5 and last 5 rows to understand the ordering of dates
print("\n--- FIRST 5 ROWS IN FILE ---")
for r in rows[:5]:
    print(f"ID: {r.get('Issue Identifier')} | Date: {r.get('Date Watched')} | Title: {r.get('Title')}")

print("\n--- LAST 5 ROWS IN FILE ---")
for r in rows[-5:]:
    print(f"ID: {r.get('Issue Identifier')} | Date: {r.get('Date Watched')} | Title: {r.get('Title')}")

# Now let's write a parser to sort properly by date and extract the absolute latest video
# Note: Date Watched might contain formats like 'YYYY-MM-DD' or ISO formats with time.
# Let's find rows with valid dates, sort them, and get the maximum.
valid_rows = []
for r in rows:
    date_str = r.get('Date Watched')
    if date_str and date_str != "unknown":
        valid_rows.append(r)

if valid_rows:
    # Sort lexicographically by Date Watched
    sorted_rows = sorted(valid_rows, key=lambda x: x.get('Date Watched'), reverse=True)
    
    print("\n--- TOP 5 LATEST VIDEOS BY SORTED DATE ---")
    for idx, r in enumerate(sorted_rows[:5], 1):
         print(f"{idx}. Date: {r.get('Date Watched')} | Title: {r.get('Title')} | Channel: {r.get('Channel Name')}")
else:
    print("[-] No rows with valid Date Watched found.")
