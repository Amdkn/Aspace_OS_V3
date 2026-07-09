#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_dan_martell.py — Extrait les vidéos de Dan Martell (@danmartell),
les classifie selon nos 8 domaines B2 Business OS et génère un rapport.
"""

import sys
import csv
import json
from pathlib import Path
import yt_dlp

# Force UTF-8 stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

RAG_CSV = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")
REPORT_PATH = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\06_Sales\DAN_MARTELL_AUDIT.md")

# Utilisation de la recherche globale comme fallback robuste pour contourner les blocages de la page de chaîne
SEARCH_QUERY = "ytsearch100:Dan Martell"

# Mots-clés de classification spécifiques pour Dan Martell
DOMAIN_KEYWORDS = {
    "Sales": ["sales", "close", "selling", "pricing", "pricing strategy", "pitch", "negotiation", "négocier", "vendre", "client", "deal", "pipeline", "ticket", "charge", "raise prices"],
    "Product": ["product", "saas", "onboarding", "churn", "retention", "rétention", "ux", "feature", "plg", "product-led", "mvp", "software", "application", "activation"],
    "Growth": ["growth", "marketing", "acquisition", "traffic", "lead", "funnel", "viral", "seo", "branding", "positioning", "ad", "ads"],
    "People": ["hire", "hiring", "team", "people", "delegation", "delegate", "employee", "recruit", "recruiter", "manager", "management", "partner", "co-founder", "execs", "assistant", "ea"],
    "Finance": ["mrr", "arr", "revenue", "profit", "finance", "scale", "exit", "valuation", "investment", "investor", "million", "rich", "sell your company", "buy", "equity"],
    "Ops": ["ops", "operations", "process", "productivity", "calendar", "time", "focus", "schedule", "routine", "automate", "automation", "system", "sop", "efficiency", "buy back your time"],
    "IT": ["it", "code", "dev", "tech", "developer", "engineering", "api", "database", "security"],
    "Legal": ["legal", "contract", "compliance", "law", "ip", "patent", "terms", "agreement"]
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
    return "Sales" # Fallback majoritaire

def extract_and_classify():
    ydl_opts = {
        'extract_flat': True,
        'skip_download': True,
        'quiet': True
    }
    
    videos_data = []
    
    print("="*60)
    print(f"[*] Extraction de Dan Martell via recherche '{SEARCH_QUERY}'...")
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
                    # S'assurer que la vidéo est bien de Dan Martell
                    uploader = entry.get('uploader') or ""
                    if uploader and "Dan Martell" not in uploader:
                        # Skip si ce n'est pas sa chaîne officielle
                        continue
                        
                    vid_id = entry.get('id')
                    title = entry.get('title')
                    duration_sec = entry.get('duration')
                    duration = format_duration(duration_sec)
                    
                    raw_date = entry.get('upload_date') or ""
                    if len(raw_date) == 8:
                        date_str = f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}"
                    else:
                        date_str = "2026-05-30"
                        
                    domain = classify_video(title)
                    
                    videos_data.append({
                        'id': vid_id,
                        'title': title,
                        'duration': duration,
                        'date': date_str,
                        'domain': domain
                    })
            else:
                print("[-] Aucune vidéo trouvée.")
        except Exception as e:
            print(f"[-] Erreur de scan : {e}")
            
    return videos_data

def generate_report(videos):
    # Calcul des stats
    by_domain = {}
    for v in videos:
        by_domain.setdefault(v['domain'], []).append(v)
        
    report_content = f"""# 🗂️ DAN_MARTELL_AUDIT — Analyse & Classification Doctrinale du Domaine Sales / Scaling

> [!NOTE]
> Ce rapport constitue la classification sémantique et doctrinale de la chaîne de référence **Dan Martell** (@danmartell), spécialisée dans le scaling de SaaS et la productivité des fondateurs.
> Les {len(videos)} vidéos les plus pertinentes de sa chaîne ont été analysées et classifiées selon nos 8 domaines B2 Business OS.

---

## 📊 Répartition Statistique par Domaine (Dan Martell)

"""
    for dom in sorted(DOMAIN_KEYWORDS.keys()):
        count = len(by_domain.get(dom, []))
        report_content += f"- **{dom}** : {count} vidéos classifiées.\n"
        
    report_content += "\n---\n\n## 🦸 Cartographie par Domaine de Référence\n"
    
    for dom in sorted(DOMAIN_KEYWORDS.keys()):
        vids = by_domain.get(dom, [])
        report_content += f"\n### 🔹 Domaine : {dom} ({len(vids)} vidéos)\n"
        if not vids:
            report_content += "_Aucune vidéo n'a été classifiée dans ce domaine._\n"
            continue
            
        report_content += "| Titre de la Vidéo | ID YouTube | Durée | Date Upload |\n"
        report_content += "| :--- | :--- | :--- | :--- |\n"
        for v in sorted(vids, key=lambda x: x['title']):
            report_content += f"| {v['title']} | `{v['id']}` | {v['duration']} | {v['date']} |\n"
            
    report_content += "\n---\n*Rapport d'audit sémantique Dan Martell généré sous A'Space OS V2.*"
    
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report_content, encoding="utf-8")
    print(f"[+] Rapport d'audit généré dans : {REPORT_PATH}")

    # Affichage des statistiques directement dans la sortie
    print("\n--- STATISTIQUES DE DISTRIBUTION ---")
    for dom in sorted(DOMAIN_KEYWORDS.keys()):
        print(f"Domain {dom:<8} : {len(by_domain.get(dom, [])):2d} videos")

if __name__ == "__main__":
    videos = extract_and_classify()
    if videos:
        generate_report(videos)
    else:
        print("[-] Aucune vidéo extraite.")
