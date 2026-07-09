#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_post_takeout.py — Récupération dynamique et souveraine de l'historique post-Takeout YouTube.
Permet d'ajouter des vidéos visionnées récemment dans la base RAG active watch_history_rag.csv.
"""

import sys
import csv
import re
from pathlib import Path
from datetime import datetime
import yt_dlp

# Force UTF-8 stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

RAG_CSV = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")

def extract_video_id(url: str) -> str | None:
    patterns = [
        r"[?&]v=([a-zA-Z0-9_-]{11})",
        r"/watch\?v=([a-zA-Z0-9_-]{11})",
        r"youtu\.be/([a-zA-Z0-9_-]{11})",
        r"/embed/([a-zA-Z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def format_duration(seconds):
    if not seconds:
        return "00:00"
    seconds = int(seconds)
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    if hours > 0:
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"

def sync_urls(urls):
    if not RAG_CSV.exists():
        print(f"[-] watch_history_rag.csv non trouvé à {RAG_CSV}")
        return

    # Chargement des identifiants existants pour éviter les doublons
    existing_ids = set()
    with open(RAG_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            existing_ids.add(row.get('Issue Identifier'))

    new_entries = []
    
    ydl_opts = {
        'extract_flat': True,
        'skip_download': True,
        'quiet': True
    }
    
    print("="*60)
    print("[*] Lancement du Sync Post-Takeout YouTube...")
    print("="*60)
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            vid_id = extract_video_id(url)
            if not vid_id:
                print(f"[!] URL invalide : {url}")
                continue
                
            issue_id = f"YT-{vid_id}"
            if issue_id in existing_ids:
                print(f"[*] {issue_id} existe déjà dans watch_history_rag.csv, mise à jour forcée...")
                
            try:
                info = ydl.extract_info(url, download=False)
                title = info.get('title')
                channel = info.get('uploader') or "Unknown Channel"
                channel_url = info.get('uploader_url') or ""
                duration_sec = info.get('duration')
                duration = format_duration(duration_sec)
                
                # Utiliser la date du jour avec l'heure courante (format ISO de Takeout)
                now_str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                
                entry = {
                    'Issue Identifier': issue_id,
                    'Title': title,
                    'Channel Name': channel,
                    'Channel URL': channel_url,
                    'Duration': duration,
                    'Date Watched': now_str,
                    'Transcription Raw': "Captured via dynamic post-Takeout sync script.",
                    'Serendipity Score': "9",  # Élevé car ajouté manuellement
                    'Category': "Product",     # Catégorisable par défaut
                    'Symphony Status': "CAPTURED"
                }
                new_entries.append(entry)
                print(f"[+] Succès : '{title}' par {channel} capturé.")
            except Exception as e:
                print(f"[-] Erreur pour {url} : {e}")

    if new_entries:
        fields = [
            'Issue Identifier', 'Title', 'Channel Name', 'Channel URL', 
            'Duration', 'Date Watched', 'Transcription Raw', 
            'Serendipity Score', 'Category', 'Symphony Status'
        ]
        
        # Injection
        with open(RAG_CSV, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            for entry in new_entries:
                writer.writerow(entry)
        print(f"\n[+] Injection réussie : {len(new_entries)} nouvelles références post-Takeout injectées en statut CAPTURED.")
    else:
        print("\n[*] Aucune nouvelle référence injectée.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sync_post_takeout.py <URL_1> [URL_2] ...")
        sys.exit(1)
        
    sync_urls(sys.argv[1:])
