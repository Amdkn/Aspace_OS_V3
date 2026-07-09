#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_yann_leonardi.py — Extrait la liste des vidéos de Yann Leonardi et génère un format Takeout compatible RAG.
"""

import sys
import csv
import json
from pathlib import Path
import yt_dlp

CHANNEL_URL = "https://www.youtube.com/@yannleonardi/videos"
OUTPUT_CSV  = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\yann_leonardi_takeout.csv")
RAG_CSV     = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")

def format_duration(seconds):
    if not seconds:
        return "00:00"
    seconds = int(seconds)
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    if hours > 0:
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"

def extract_videos():
    ydl_opts = {
        'extract_flat': True,
        'skip_download': True,
        'quiet': True
    }
    
    print(f"[*] Extraction des vidéos de la chaîne {CHANNEL_URL}...")
    
    videos_data = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(CHANNEL_URL, download=False)
            if 'entries' in info:
                entries = list(info['entries'])
                print(f"[+] {len(entries)} vidéos trouvées.")
                
                for entry in entries:
                    if not entry:
                        continue
                    vid_id = entry.get('id')
                    title = entry.get('title')
                    duration_sec = entry.get('duration')
                    # format duration
                    duration = format_duration(duration_sec)
                    
                    # Convert upload date
                    raw_date = entry.get('upload_date') or ""
                    if len(raw_date) == 8:
                        date_str = f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}"
                    else:
                        date_str = "2026-05-28"
                        
                    videos_data.append({
                        'Issue Identifier': f"YT-{vid_id}",
                        'Title': title,
                        'Channel Name': "Yann Leonardi",
                        'Channel URL': "https://www.youtube.com/@yannleonardi",
                        'Duration': duration,
                        'Date Watched': date_str,
                        'Transcription Raw': "Transcription non disponible (RAG Yann Leonardi extraction).",
                        'Serendipity Score': "8",
                        'Category': "Business",
                        'Symphony Status': "CAPTURED"
                    })
            else:
                print("[-] Aucune entrée trouvée.")
        except Exception as e:
            print(f"[FATAL] Erreur d'extraction: {e}")
            sys.exit(1)
            
    return videos_data

def write_to_csv(data):
    fields = [
        'Issue Identifier', 'Title', 'Channel Name', 'Channel URL', 
        'Duration', 'Date Watched', 'Transcription Raw', 
        'Serendipity Score', 'Category', 'Symphony Status'
    ]
    
    # 1. Écrire le CSV d'extraction isolé
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
    print(f"[+] Fichier Takeout isolé généré avec succès: {OUTPUT_CSV}")
    
    # 2. Optionnel: Injecter dans watch_history_rag.csv s'il existe
    if RAG_CSV.exists():
        # Lire les identifiants existants pour éviter les doublons
        existing_ids = set()
        with open(RAG_CSV, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_ids.add(row.get('Issue Identifier'))
                
        # Filtrer les nouvelles vidéos uniquement
        new_entries = [d for d in data if d['Issue Identifier'] not in existing_ids]
        
        if new_entries:
            with open(RAG_CSV, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writerows(new_entries)
            print(f"[+] {len(new_entries)} nouvelles vidéos injectées dans watch_history_rag.csv en statut CAPTURED.")
        else:
            print("[*] Toutes les vidéos extraites existent déjà dans la base RAG.")
            
def main():
    data = extract_videos()
    if data:
        write_to_csv(data)
    else:
        print("[-] Aucune donnée à écrire.")

if __name__ == "__main__":
    main()
