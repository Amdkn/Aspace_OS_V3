import csv
from pathlib import Path

RAG_CSV = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")

def count_captured_it():
    if not RAG_CSV.exists():
        print("[-] watch_history_rag.csv non trouvé.")
        return
    
    count = 0
    with open(RAG_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('Category') == 'IT' and row.get('Symphony Status') == 'CAPTURED':
                count += 1
    print(f"[*] Nombre de vidéos IT au statut CAPTURED : {count}")

if __name__ == "__main__":
    count_captured_it()
