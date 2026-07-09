import csv
import sys
from pathlib import Path

# Force UTF-8 stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

rag_csv = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")

if not rag_csv.exists():
    print(f"[-] RAG CSV not found at {rag_csv}")
    sys.exit(1)

ids_to_find = ["YT-gU5KDeTb1JY", "YT-TZDMhtrty5E", "YT-DZtj2S_-qa8", "gU5KDeTb1JY", "TZDMhtrty5E", "DZtj2S_-qa8"]

rows_found = []
with open(rag_csv, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        v_id = row.get('Issue Identifier')
        if any(target in v_id for target in ids_to_find):
            rows_found.append(row)

if rows_found:
    print(f"[+] Found {len(rows_found)} matching rows:")
    for r in rows_found:
        print(f"ID: {r.get('Issue Identifier')} | Title: {r.get('Title')} | Status: {r.get('Symphony Status')}")
else:
    print("[-] No matching rows found in watch_history_rag.csv.")
