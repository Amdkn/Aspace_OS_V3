import csv
import sys
from collections import Counter
from pathlib import Path

# Force UTF-8 stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

rag_csv = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")

if not rag_csv.exists():
    print(f"[-] RAG CSV not found at {rag_csv}")
    sys.exit(1)

channels = []
titles_by_channel = {}

with open(rag_csv, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        channel = row.get('Channel Name')
        title = row.get('Title')
        if channel:
            channel = channel.strip()
            channels.append(channel)
            titles_by_channel.setdefault(channel, []).append(title)

counter = Counter(channels)

print("="*60)
print(f"[*] Analyse de watch_history_rag.csv ({len(channels)} vidéos au total)")
print("="*60)

# Top 50 channels by video count
top_channels = counter.most_common(50)

print("\n--- TOP 30 DES CHAINES LES PLUS VISIONNÉES ---")
for idx, (chan, count) in enumerate(top_channels[:30], 1):
    print(f"{idx:02d}. {chan:<35} | {count:4d} vidéos")

# We can output some representative titles for the top channels to help analyze
print("\n--- EXEMPLES DE TITRES PAR CHAINE POUR ANALYSE SÉMANTIQUE DE DOMAINE ---")
for chan, count in top_channels[:25]:
    examples = titles_by_channel[chan][:3]
    print(f"\n🔹 Chaine: {chan} ({count} vidéos)")
    for ex in examples:
        print(f"   - {ex}")
