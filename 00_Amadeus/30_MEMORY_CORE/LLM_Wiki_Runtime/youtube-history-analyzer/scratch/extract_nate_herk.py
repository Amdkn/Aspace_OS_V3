#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_nate_herk.py — Extrait les vidéos de Nate Herk (@nateherk),
les classifie exclusivement entre IT, Ops et Product, et les injecte dans le RAG.
"""

import sys
import csv
import json
from pathlib import Path
import yt_dlp
from datetime import datetime

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

RAG_CSV = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")
REPORT_PATH = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\03_IT\NATE_HERK_AUDIT.md")

SEARCH_QUERY = "ytsearch50:Nate Herk"

# Mots-clés de classification ciblés exclusivement pour IT, Ops et Product
DOMAIN_KEYWORDS = {
    "IT": ["code", "dev", "tech", "developer", "engineering", "api", "database", "security", "github", "git", "deploy", "next.js", "react", "typescript", "python", "docker", "cloud", "aws", "vps", "server", "cli", "terminal", "prompt", "ai stack", "programming", "backend", "frontend"],
    "Ops": ["ops", "operations", "process", "productivity", "calendar", "time", "focus", "schedule", "routine", "automate", "automation", "system", "sop", "efficiency", "n8n", "make", "zapier", "agent", "swarm", "flow", "rag", "orchestrate", "setup", "workspace"],
    "Product": ["product", "saas", "onboarding", "churn", "retention", "ux", "feature", "plg", "mvp", "software", "application", "figma", "wire", "intel", "user", "ui", "design"]
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
    return "IT" # Fallback par défaut (entre IT, Ops et Product, IT est le Bedrock)

def extract_and_classify():
    ydl_opts = {
        'extract_flat': True,
        'skip_download': True,
        'quiet': True
    }
    
    videos_data = []
    
    print("="*60)
    print(f"[*] Extraction de Nate Herk via '{SEARCH_QUERY}'...")
    print("="*60)
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(SEARCH_QUERY, download=False)
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
                    
                    videos_data.append({
                        'Issue Identifier': f"YT-{vid_id}",
                        'Title': title,
                        'Channel Name': "Nate Herk",
                        'Channel URL': f"https://www.youtube.com/watch?v={vid_id}",
                        'Duration': duration,
                        'Date Watched': date_str,
                        'Transcription Raw': "Captured via Nate Herk search extractor.",
                        'Serendipity Score': "8",
                        'Category': domain,
                        'Symphony Status': "CAPTURED"
                    })
            else:
                print("[-] Aucune vidéo trouvée.")
        except Exception as e:
            print(f"[-] Erreur de scan : {e}")
            
    return videos_data

def sync_and_report(videos):
    if not RAG_CSV.exists():
        print("[-] watch_history_rag.csv non trouvé.")
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
        print(f"[+] Ingestion RAG : {len(new_entries)} nouvelles vidéos de Nate Herk injectées.")
    else:
        print("[*] Toutes les vidéos de Nate Herk existent déjà dans le RAG.")
        
    # Génération du rapport consolidé de répartition
    by_domain = {}
    for v in videos:
        by_domain.setdefault(v['Category'], []).append(v)
        
    report_content = f"""# 🗂️ NATE_HERK_AUDIT — Ingestion & Répartition Doctrinale (IT, OPS, PRODUCT)

> [!IMPORTANT]
> Ce rapport compile la distribution doctrinale de la chaîne de référence **Nate Herk** (@nateherk).
> L'ensemble des {len(videos)} vidéos capturées a été réparti exclusivement entre les domaines **IT**, **Ops** et **Product**.

---

## 📊 Répartition Statistique par Domaine (Nate Herk)

"""
    for dom in ["IT", "Ops", "Product"]:
        count = len(by_domain.get(dom, []))
        report_content += f"- **{dom}** : {count} vidéos classifiées.\n"
        
    report_content += "\n---\n\n## 🦸 Cartographie par Domaine de Référence\n"
    
    for dom in ["IT", "Ops", "Product"]:
        vids = by_domain.get(dom, [])
        report_content += f"\n### 🔹 Domaine : {dom} ({len(vids)} vidéos)\n"
        if not vids:
            report_content += "_Aucune vidéo classifiée dans ce domaine._\n"
            continue
            
        report_content += "| Titre de la Vidéo | ID YouTube | Durée | Date |\n"
        report_content += "| :--- | :--- | :--- | :--- |\n"
        for v in sorted(vids, key=lambda x: x['Title']):
            report_content += f"| {v['Title']} | `{v['Issue Identifier']}` | {v['Duration']} | {v['Date Watched']} |\n"
            
    report_content += "\n---\n*Rapport d'audit de répartition Nate Herk généré sous A'Space OS V2.*"
    
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report_content, encoding="utf-8")
    print(f"[+] Rapport de répartition généré dans : {REPORT_PATH}")

if __name__ == "__main__":
    videos = extract_and_classify()
    if videos:
        sync_and_report(videos)
    else:
        print("[-] Aucune vidéo extraite.")
