#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_it_channels_bulk.py — Extrait en masse les vidéos de 10 chaînes IT clés,
les classifie selon nos 8 domaines B2 Business OS et génère un rapport consolidé.
"""

import sys
import csv
import json
from pathlib import Path
import yt_dlp
from datetime import datetime

# Force UTF-8 stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

RAG_CSV = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")
REPORT_PATH = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\03_IT\IT_CHANNELS_BULK_AUDIT.md")

CHANNELS = {
    "Cole Medin": "ytsearch50:Cole Medin",
    "Mark Kashef": "ytsearch50:Mark Kashef",
    "Julian Goldie SEO": "ytsearch50:Julian Goldie SEO",
    "RoboNuggets": "ytsearch50:RoboNuggets",
    "Itssssss Jack": "ytsearch50:Itssssss Jack",
    "GithubAwesome": "ytsearch50:GithubAwesome",
    "World of AI": "ytsearch50:World of AI",
    "Manu AGI": "ytsearch50:Manu AGI",
    "AI Stack Engineer": "ytsearch50:AI Stack Engineer",
    "cocadmin": "ytsearch50:cocadmin"
}

# Framework de classification
DOMAIN_KEYWORDS = {
    "IT": ["code", "dev", "tech", "developer", "engineering", "api", "database", "security", "github", "git", "deploy", "next.js", "react", "typescript", "python", "docker", "ansible", "linux", "cloud", "aws", "vps", "server", "reverse", "local", "cli", "terminal", "prompt"],
    "Ops": ["ops", "operations", "process", "productivity", "calendar", "time", "focus", "schedule", "routine", "automate", "automation", "system", "sop", "efficiency", "n8n", "make", "zapier", "agent", "swarm", "openclaw", "framework", "orchestrate", "flow", "rag", "langchain"],
    "Growth": ["seo", "traffic", "growth", "marketing", "acquisition", "lead", "funnel", "viral", "branding", "tiktok", "instagram", "youtube", "affiliate", "niche", "keywords"],
    "Sales": ["sales", "close", "selling", "pricing", "pitch", "negotiation", "client", "deal", "pipeline", "vendre", "pricing strategy"],
    "Finance": ["mrr", "arr", "revenue", "profit", "finance", "scale", "exit", "valuation", "investment", "investor", "million", "rich", "money", "budget", "stripe", "wise"],
    "People": ["hire", "hiring", "team", "people", "delegation", "employee", "recruit", "recruiter", "manager", "management", "partner", "co-founder"],
    "Product": ["product", "saas", "onboarding", "churn", "retention", "rétention", "ux", "feature", "plg", "mvp", "software", "application", "figma", "wire", "intel"],
    "Legal": ["legal", "contract", "compliance", "law", "ip", "patent", "terms", "agreement", "rgpd"]
}

def format_duration(seconds):
    if not seconds:
        return "00:00"
    seconds = int(seconds)
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    if hours > 0:
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"

def classify_video(title):
    title_lower = title.lower()
    matches = {}
    
    for domain, kws in DOMAIN_KEYWORDS.items():
        score = 0
        for kw in kws:
            if kw in title_lower:
                score += 2
        if score > 0:
            matches[domain] = score
            
    if matches:
        sorted_matches = sorted(matches.items(), key=lambda x: -x[1])
        return sorted_matches[0][0]
    return "IT" # Fallback par excellence

def extract_and_classify():
    ydl_opts = {
        'extract_flat': True,
        'skip_download': True,
        'quiet': True
    }
    
    all_videos = []
    
    print("="*60)
    print(f"[*] Extraction de masse des 10 chaînes IT à l'ère de l'IA...")
    print("="*60)
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for uploader, query in CHANNELS.items():
            print(f"\n[*] Scan : {uploader} via '{query}'...")
            try:
                info = ydl.extract_info(query, download=False)
                if 'entries' in info:
                    entries = list(info['entries'])
                    print(f"[+] {len(entries)} vidéos identifiées.")
                    for entry in entries:
                        if not entry:
                            continue
                        vid_id = entry.get('id')
                        title = entry.get('title')
                        duration_sec = entry.get('duration')
                        duration = format_duration(duration_sec)
                        
                        raw_date = entry.get('upload_date') or ""
                        if len(raw_date) == 8:
                            date_str = f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}"
                        else:
                            date_str = datetime.now().strftime("%Y-%m-%d")
                            
                        domain = classify_video(title)
                        
                        all_videos.append({
                            'Issue Identifier': f"YT-{vid_id}",
                            'Title': title,
                            'Channel Name': uploader,
                            'Channel URL': f"https://www.youtube.com/watch?v={vid_id}",
                            'Duration': duration,
                            'Date Watched': date_str,
                            'Transcription Raw': "Captured via IT channels bulk search extractor.",
                            'Serendipity Score': "8",
                            'Category': domain,
                            'Symphony Status': "CAPTURED"
                        })
                else:
                    print("[-] Aucune vidéo trouvée.")
            except Exception as e:
                print(f"[-] Erreur de scan pour {uploader} : {e}")
                
    return all_videos

def sync_and_report(videos):
    if not RAG_CSV.exists():
        print(f"[-] watch_history_rag.csv non trouvé.")
        return
        
    # Charger les ID existants
    existing_ids = set()
    with open(RAG_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            existing_ids.add(row.get('Issue Identifier'))
            
    # Filtrer les nouvelles vidéos uniquement
    new_entries = [v for v in videos if v['Issue Identifier'] not in existing_ids]
    
    fields = [
        'Issue Identifier', 'Title', 'Channel Name', 'Channel URL', 
        'Duration', 'Date Watched', 'Transcription Raw', 
        'Serendipity Score', 'Category', 'Symphony Status'
    ]
    
    if new_entries:
        with open(RAG_CSV, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            for entry in new_entries:
                writer.writerow(entry)
        print(f"\n[+] Ingestion RAG : {len(new_entries)} nouvelles vidéos injectées.")
    else:
        print("\n[*] Toutes les vidéos extraites existent déjà dans la base RAG.")
        
    # Génération du rapport consolidé
    report_content = """# 🗂️ IT_CHANNELS_BULK_AUDIT — Ingestion & Classification de la Mine d'Or IT / IA

> [!IMPORTANT]
> Ce rapport compile l'audit sémantique et la distribution de **10 chaînes de référence IT / IA** majeures.
> Toutes les vidéos ont été cataloguées sous nos 8 domaines B2 Business OS pour structurer le futur RAG d'A'Space OS V2.

---

## 📊 Répartition Statistique par Domaine (Ingestion Globale)

"""
    by_channel = {}
    by_domain = {}
    
    for v in videos:
        by_channel.setdefault(v['Channel Name'], []).append(v)
        by_domain.setdefault(v['Category'], []).append(v)
        
    report_content += "### 1. Par Chaîne de Référence :\n"
    for chan, vids in by_channel.items():
        report_content += f"- **{chan}** : {len(vids)} vidéos capturées.\n"
        
    report_content += "\n### 2. Par Domaine Business OS (B2) :\n"
    for dom in sorted(DOMAIN_KEYWORDS.keys()):
        count = len(by_domain.get(dom, []))
        report_content += f"- **{dom}** : {count} vidéos classifiées.\n"
        
    report_content += "\n---\n\n## 🦸 Cartographie par Domaine de Référence\n"
    
    for dom in sorted(DOMAIN_KEYWORDS.keys()):
        vids = by_domain.get(dom, [])
        report_content += f"\n### 🔹 Domaine : {dom} ({len(vids)} vidéos)\n"
        if not vids:
            report_content += "_Aucune vidéo dans ce domaine._\n"
            continue
            
        report_content += "| Chaîne | Titre de la Vidéo | ID YouTube | Durée | Date |\n"
        report_content += "| :--- | :--- | :--- | :--- | :--- |\n"
        for v in sorted(vids, key=lambda x: x['Title']):
            report_content += f"| {v['Channel Name']} | {v['Title']} | `{v['Issue Identifier']}` | {v['Duration']} | {v['Date Watched']} |\n"
            
    report_content += "\n---\n*Rapport d'audit sémantique IT consolidé généré sous A'Space OS V2.*"
    
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report_content, encoding="utf-8")
    print(f"[+] Rapport d'audit généré dans : {REPORT_PATH}")

if __name__ == "__main__":
    videos = extract_and_classify()
    if videos:
        sync_and_report(videos)
    else:
        print("[-] Aucune vidéo extraite.")
