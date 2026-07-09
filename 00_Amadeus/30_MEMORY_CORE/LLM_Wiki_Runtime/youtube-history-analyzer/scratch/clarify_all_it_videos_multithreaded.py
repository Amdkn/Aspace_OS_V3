#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
clarify_all_it_videos_multithreaded.py — Clarification sémantique industrielle
et multithreadée de l'ensemble des vidéos IT au statut CAPTURED.
"""

import sys
import csv
import json
import os
import re
from pathlib import Path
from datetime import datetime
import http.client
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

RAG_CSV = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")
GEORDI_DIR = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\03_IT")

# Verrou pour la synchronisation de l'écriture CSV
csv_lock = threading.Lock()

def get_api_key():
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        hermes_env = Path(r"C:\Users\amado\.hermes\.env")
        if hermes_env.exists():
            with open(hermes_env, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("OPENROUTER_API_KEY="):
                        api_key = line.split("=", 1)[1].strip()
    return api_key

API_KEY = get_api_key()

import time

def call_minimax_llm(prompt: str, system_prompt: str = "") -> str:
    # On garde le nom de la fonction pour éviter de modifier le reste du script
    if not API_KEY:
        return "FALLBACK: Clé OpenRouter manquante."
        
    host = "openrouter.ai"
    path = "/api/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://aspace-os.local",
        "X-Title": "ASpace OS V2"
    }
    
    payload = {
        "model": "z-ai/glm-4.7-flash",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }
    
    retries = 4
    backoff = 3.0
    
    for attempt in range(retries):
        try:
            conn = http.client.HTTPSConnection(host, timeout=60)
            conn.request("POST", path, json.dumps(payload), headers)
            response = conn.getresponse()
            res_data = response.read().decode("utf-8")
            
            if response.status == 200:
                res_json = json.loads(res_data)
                choices = res_json.get("choices", [])
                if choices:
                    content = choices[0].get("message", {}).get("content", "").strip()
                    content = re.sub(r"<think>[\s\S]*?</think>", "", content).strip()
                    return content
                return "ERROR: No content in response choices."
            elif response.status == 429:
                print(f"[!] Rate Limit (429) detecte. Tentative {attempt+1}/{retries}. Attente de {backoff}s...")
                time.sleep(backoff)
                backoff *= 2.0
            else:
                return f"ERROR: Status {response.status} - {res_data}"
        except Exception as e:
            if attempt == retries - 1:
                return f"ERROR: {str(e)}"
            time.sleep(backoff)
            backoff *= 2.0
            
    return "ERROR: Trop de requêtes (429) après tentatives de retry."

def slugify(title):
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s-]+", "-", slug)
    return slug.strip("-")

def generate_guide_content(video):
    title = video["Title"]
    channel = video["Channel Name"]
    vid_id = video["Issue Identifier"]
    duration = video["Duration"]
    date_str = video["Date Watched"]
    
    system_prompt = (
        "Tu es l'agent sémantique d'ingénierie A3 de l'OS souverain A'Space OS V2. "
        "Ton but est de rédiger un guide Obsidian premium exhaustif et haute densité (>110 lignes) "
        "sur une thématique IT / IA à partir du titre de la vidéo et de la chaîne de référence. "
        "Le guide doit être rédigé en Français technique impeccable, sans aucun placeholder."
    )
    
    prompt = f"""Rédige un guide de connaissances Obsidian ultra-dense et technique (>110 lignes) pour la vidéo suivante :
Titre : {title}
Chaîne de référence : {channel}
ID : {vid_id}
Catégorie : IT & IA Souveraine

Ta réponse doit STRICTEMENT respecter le format Markdown Obsidian suivant, sans introduction ni blabla :

---
id: {vid_id}
title: "{title}"
channel: "{channel}"
duration: "{duration}"
date: "{date_str}"
category: "IT / IA"
---

# 📖 {title}

> [!NOTE]
> Fiche de clarification industrielle haute fidélité sémantique.

---

## 🧠 Concepts Clés à Haute Densité Sémantique
- **<Concept 1>** : Fournis une explication technique et stratégique très poussée (4-5 lignes complètes) en lien direct avec le sujet '{title}'.
- **<Concept 2>** : Fournis une explication technique et stratégique très poussée (4-5 lignes complètes) en lien direct avec le sujet '{title}'.
- **<Concept 3>** : Fournis une explication technique et stratégique très poussée (4-5 lignes complètes).
- **<Concept 4>** : Fournis une explication technique et stratégique très poussée (4-5 lignes complètes).
- **<Concept 5>** : Fournis une explication technique et stratégique très poussée (4-5 lignes complètes).
- **<Concept 6>** : Fournis une explication technique et stratégique très poussée (4-5 lignes complètes).

## 🛠️ Outillage Stratégique & Matrice d'Alignement
| Outil / Technologie | Rôle Stratégique | Alignement Souverain A'Space |
| :--- | :--- | :--- |
| **<Outil principal>** | <Rôle précis et contextuel dans l'architecture> | <Comment l'exécuter localement, Docker, SQLite, instance n8n ou agent local> |
| **<Outil secondaire>** | <Rôle stratégique> | <Remplacement souverain ou auto-hébergement> |
| **<Outil complémentaire>** | <Rôle stratégique> | <Remplacement souverain ou auto-hébergement> |

## 🪐 Perspective Souveraine A'Space OS
<Rédige une longue section de 15 à 20 lignes d'analyse conceptuelle de haut niveau sur la manière de transposer, implémenter et exploiter les enseignements du sujet '{title}' dans l'architecture locale et résiliente d'A'Space OS V2 (concept de Digital Twin, évitement de la dépendance aux GAFAM, isolation réseau, pipelines autonomes, agents spécialisés locaux, etc.)>

## 🕹️ Protocole d'Exécution D.E.A.L
| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | <Action précise et mesurable sur le système> | <But dans l'OS> |
| **Éliminer** | <Action précise et mesurable sur le système> | <But dans l'OS> |
| **Automatiser** | <Action précise et mesurable sur le système> | <But dans l'OS> |
| **Libérer** | <Action précise et mesurable sur le système> | <But dans l'OS> |

---
*Fiche de connaissances IT souveraine générée sous A'Space OS V2.*
"""
    
    content = call_minimax_llm(prompt, system_prompt)
    return content

def process_single_video(video):
    vid_id = video["Issue Identifier"]
    title = video["Title"]
    channel = video["Channel Name"]
    
    try:
        print(f"[*] Traitement : [{channel}] {title[:60]}...")
        content = generate_guide_content(video)
        
        if content.startswith("ERROR:") or content.startswith("FALLBACK:"):
            print(f"[-] Echec de génération pour {vid_id} : {content}")
            return vid_id, False
            
        slug = slugify(title)
        chan_slug = slugify(channel)
        
        target_dir = GEORDI_DIR / chan_slug
        target_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = target_dir / f"{slug}.md"
        filepath.write_text(content, encoding="utf-8")
        print(f"[+] Guide créé : {filepath.name} ({len(content.splitlines())} lignes)")
        return vid_id, True
    except Exception as e:
        print(f"[-] Erreur sur la vidéo {vid_id} : {e}")
        return vid_id, False

def run_bulk_clarification():
    if not RAG_CSV.exists():
        print("[-] RAG CSV introuvable.")
        return
        
    rows = []
    with open(RAG_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
            
    it_captured = [r for r in rows if r["Category"] == "IT" and r["Symphony Status"] == "CAPTURED"]
    total = len(it_captured)
    
    print("="*60)
    print(f"🧿 Lancement de la clarification industrielle de {total} vidéos IT")
    print("="*60)
    
    if total == 0:
        print("[*] Aucune vidéo IT au statut CAPTURED à clarifier.")
        return
        
    # Exécution multithreadée (3 workers pour maximiser la sécurité vis-à-vis du rate limit)
    max_workers = 3
    success_ids = set()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # On soumet les tâches avec un infime décalage de démarrage
        futures = {}
        for vid in it_captured:
            futures[executor.submit(process_single_video, vid)] = vid
            time.sleep(0.5) # Petit délai de soumission pour étaler
            
        for fut in as_completed(futures):
            vid_id, success = fut.result()
            if success:
                success_ids.add(vid_id)
                
    print("\n" + "="*60)
    print(f"[*] Synchronisation finale des statuts dans le RAG...")
    print("="*60)
    
    # Mettre à jour les statuts en mémoire
    for r in rows:
        if r["Issue Identifier"] in success_ids:
            r["Symphony Status"] = "CLARIFIED_PLANE"
            
    # Écriture atomique dans le CSV
    with csv_lock:
        with open(RAG_CSV, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
            
    print(f"[+] Mise à jour RAG achevée : {len(success_ids)}/{total} vidéos clarifiées avec succès.")
    
if __name__ == "__main__":
    run_bulk_clarification()
