import csv
from pathlib import Path

RAG_CSV = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")

def select_25_it_pepites():
    if not RAG_CSV.exists():
        print("[-] watch_history_rag.csv non trouvé.")
        return
        
    pepites = []
    # Chaînes cibles pour assurer une bonne distribution
    it_channels = [
        "Cole Medin", "Mark Kashef", "Julian Goldie SEO", "RoboNuggets", 
        "Itssssss Jack", "GithubAwesome", "World of AI", "Manu AGI", 
        "AI Stack Engineer", "cocadmin"
    ]
    
    with open(RAG_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('Category') == 'IT' and row.get('Symphony Status') == 'CAPTURED' and row.get('Channel Name') in it_channels:
                pepites.append(row)
                
    # Trier par chaîne pour une distribution équilibrée et prendre les meilleures (par exemple, 2-3 par chaîne)
    by_channel = {}
    for p in pepites:
        by_channel.setdefault(p['Channel Name'], []).append(p)
        
    selected = []
    # On prend jusqu'à 3 vidéos par chaîne jusqu'à en avoir 25
    for i in range(5):
        for chan in it_channels:
            vids = by_channel.get(chan, [])
            if len(vids) > i:
                selected.append(vids[i])
            if len(selected) == 25:
                break
        if len(selected) == 25:
            break
            
    # Écriture dans un JSON de lot temporaire pour le subagent
    batch_file = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\scratch\it_pepites_batch.json")
    import json
    with open(batch_file, "w", encoding="utf-8") as f:
        json.dump(selected, f, ensure_ascii=False, indent=2)
    
    print(f"[+] Selection de {len(selected)} pepites IT pour clarification.")
    for idx, s in enumerate(selected, 1):
        safe_title = s['Title'].encode('ascii', 'ignore').decode('ascii')
        print(f"{idx:02d}. [{s['Channel Name']}] {safe_title} (ID: {s['Issue Identifier']})")
    print(f"[+] Lot de pepites enregistre dans {batch_file}")

if __name__ == "__main__":
    select_25_it_pepites()
