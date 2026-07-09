#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_product_channels.py — Extrait les vidéos de Leo Grindarss, Sachmoney et Romain Brunel,
puis les classifie et les injecte dans la base RAG watch_history_rag.csv.
"""

import sys
import csv
import re
import json
from pathlib import Path
from datetime import datetime
import yt_dlp

# Force UTF-8 stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

RAG_CSV = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")
REPORT_PATH = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\01_Product\PRODUCT_CHANNELS_AUDIT.md")

CHANNELS = {
    "Leo Grindarss": "https://www.youtube.com/@grindarss/videos",
    "Sachmoney": "https://www.youtube.com/@Sachmoneys/videos",
    "Romain Brunel (Affiseo)": "https://www.youtube.com/@Affiseo_/videos"
}

# Framework de classification par mots-clés
DOMAIN_KEYWORDS = {
    "Product": ["saas", "interface", "design", "wire", "intel", "app", "low-code", "no-code", "flutterflow", "bubble", "figma", "produit", "onboarding", "ux", "ui", "tvr", "built to sell", "e-myth"],
    "Growth": ["growth", "aarrr", "acquisition", "trafic", "seo", "cocon", "instagram", "tiktok", "moteur", "viral", "referral", "marketing", "visibilité", "audience"],
    "Finance": ["millionnaire", "million", "argent", "finance", "marge", "rentable", "stripe", "mrr", "arr", "kiabi", "cultura", "banque", "impot", "rich", "richesse"],
    "Sales": ["tunnel", "funnel", "closing", "vendre", "pricing", "high-ticket", "sales", "client", "négociation", "offre", "pitch"],
    "Ops": ["agent", "ia", "openclaw", "automatiser", "n8n", "zapier", "make", "rpa", "run", "monitoring", "stabilité", "process", "sop"],
    "IT": ["code", "reverse", "engineer", "dev", "next.js", "github", "react", "esbuild", "typescript", "git", "api", "database", "server", "infra"],
    "Legal": ["rgpd", "loi", "conformité", "contrat", "cabinet", "legal", "compliance", "sécurité", "cybersecurité"]
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
        # Trier par score décroissant et prendre le meilleur domaine
        sorted_matches = sorted(matches.items(), key=lambda x: -x[1])
        return sorted_matches[0][0]
    return "Product" # Fallback par défaut car ce sont des chaînes majoritairement orientées Produit/SaaS

def extract_and_classify():
    ydl_opts = {
        'extract_flat': True,
        'skip_download': True,
        'quiet': True
    }
    
    all_videos = []
    
    print("="*60)
    print("[*] Extraction de masse des 3 chaînes de référence Product...")
    print("="*60)
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for uploader, url in CHANNELS.items():
            print(f"\n[*] Scan de la chaîne : {uploader} ({url})...")
            try:
                info = ydl.extract_info(url, download=False)
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
                            'Transcription Raw': "Captured via bulk Product channel extractor.",
                            'Serendipity Score': "8",
                            'Category': domain,
                            'Symphony Status': "CAPTURED"
                        })
                else:
                    print("[-] Aucune vidéo trouvée.")
            except Exception as e:
                print(f"[-] Erreur sur {uploader} : {e}")
                
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
            
    # Filtrer et insérer uniquement les nouveaux
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
        print("\n[*] Toutes les vidéos extraites existent déjà dans watch_history_rag.csv.")
        
    # Génération du rapport d'audit classifié
    report_content = """# 🗂️ PRODUCT_CHANNELS_AUDIT — Analyse & Classification du Gisement Product

> [!NOTE]
> Ce rapport constitue l'audit sémantique et la cartographie complète de trois chaînes de référence complémentaires sur le Domaine Product : **Leo Grindarss**, **Sachmoney**, et **Romain Brunel (Affiseo)**.
> Les vidéos ont été classifiées dynamiquement selon nos 8 domaines B2 Business OS de A'Space OS V2.

---

## 📊 Répartition Statistique par Domaine

"""
    # Calculer les stats
    by_channel = {}
    by_domain = {}
    
    for v in videos:
        by_channel.setdefault(v['Channel Name'], []).append(v)
        by_domain.setdefault(v['Category'], []).append(v)
        
    report_content += "### 1. Par Chaîne de Référence :\n"
    for chan, vids in by_channel.items():
        report_content += f"- **{chan}** : {len(vids)} vidéos capturées.\n"
        
    report_content += "\n### 2. Par Domaine Business OS (B2) :\n"
    for dom, vids in sorted(by_domain.items(), key=lambda x: -len(x[1])):
        report_content += f"- **{dom}** : {len(vids)} vidéos classifiées.\n"
        
    report_content += "\n---\n\n## 🦸 Cartographie par Domaine (Prêts pour Clarification)\n"
    
    for dom in sorted(by_domain.keys()):
        report_content += f"\n### 🔹 Domaine : {dom}\n"
        report_content += "| Chaîne | Titre de la Vidéo | ID YouTube | Durée | Date Upload |\n"
        report_content += "| :--- | :--- | :--- | :--- | :--- |\n"
        
        for v in sorted(by_domain[dom], key=lambda x: x['Title']):
            report_content += f"| {v['Channel Name']} | {v['Title']} | `{v['Issue Identifier']}` | {v['Duration']} | {v['Date Watched']} |\n"
            
    report_content += "\n---\n*Rapport d'audit sémantique généré de manière autonome sous A'Space OS V2.*"
    
    # Créer le répertoire parent s'il n'existe pas
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report_content, encoding="utf-8")
    print(f"[+] Rapport d'audit généré avec succès dans : {REPORT_PATH}")

if __name__ == "__main__":
    videos = extract_and_classify()
    if videos:
        sync_and_report(videos)
    else:
        print("[-] Aucune vidéo extraite.")
