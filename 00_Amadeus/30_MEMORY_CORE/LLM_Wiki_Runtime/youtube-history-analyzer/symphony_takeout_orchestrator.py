#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
symphony_takeout_orchestrator.py — Orchestrateur souverain pour l'analyse chronologique inverse du Takeout YouTube.
Classifie les vidéos dans les 8 domaines de la Life Wheel (Zora), prépare la queue de traitement et scaffold les ressources Geordi dans PARA.
"""

import os
import sys
import json
import csv
from pathlib import Path
from datetime import datetime

# Force UTF-8 stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

# Chemins A'Space OS
YOUTUBE_ANALYZER_DIR = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer")
sys.path.append(str(YOUTUBE_ANALYZER_DIR))

try:
    from parser.watch_history_parser import parse_watch_history, Video
except ImportError:
    print("[-] Erreur : Impossible d'importer parse_watch_history. Vérifiez le chemin du module.")
    sys.exit(1)

# Configuration des répertoires PARA Geordi
GEORDI_GUIDES_BASE = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides")
RAG_CSV = YOUTUBE_ANALYZER_DIR / "watch_history_rag.csv"
QUEUE_FILE = YOUTUBE_ANALYZER_DIR / "takeout_processing_queue.json"

# Mappage des 8 domaines de la Life Wheel (Zora) aux sous-répertoires PARA
LIFE_WHEEL_DOMAINS = {
    "LD01_Business": {
        "folder": "01_Business",
        "keywords": ["business", "startup", "entrepreneur", "saas", "bootstrapped", "funding", "ceo", "built to sell", "e-myth", "offers", "sales", "marketing", "scale", "acquisition", "conversion"],
        "title": "Business & Carrière"
    },
    "LD02_Finance": {
        "folder": "02_Finance",
        "keywords": ["money", "investing", "finance", "wealth", "rich", "passive income", "portfolio", "stock", "crypto", "budget", "fastlane", "assets", "liabilities"],
        "title": "Finance & Indépendance"
    },
    "LD03_Vitality": {
        "folder": "03_Health",
        "keywords": ["sleep", "health", "vitality", "body", "diet", "gym", "breath", "outlive", "supple", "longevity", "physical", "exercise", "biohacking"],
        "title": "Vitalité & Santé Physique"
    },
    "LD04_Cognition": {
        "folder": "04_Cognition",
        "keywords": ["learn", "memory", "focus", "brain", "ultralearning", "teaching", "study", "learning", "anki", "reading", "attention", "cognitive", "mindset"],
        "title": "Cognition & Apprentissage"
    },
    "LD05_Social": {
        "folder": "05_Social",
        "keywords": ["social", "friends", "influence", "negotiation", "trust", "persuasion", "relationship", "network", "communication", "reciprocity", "languages of love"],
        "title": "Réseau Social & Relations"
    },
    "LD06_Family": {
        "folder": "06_Family",
        "keywords": ["family", "presence", "life partner", "children", "home", "parenting", "relationship", "marriage", "household", "love"],
        "title": "Famille & Présence"
    },
    "LD07_Creativity": {
        "folder": "07_Creativity",
        "keywords": ["flow", "creativity", "play", "game design", "gamification", "fun", "art", "music", "writing", "design", "invent", "hobby", "recreational"],
        "title": "Créativité & Flow"
    },
    "LD08_Solarpunk": {
        "folder": "08_Solarpunk",
        "keywords": ["biomimicry", "biomimetisme", "circular economy", "blue economy", "low tech", "urban acupuncture", "jaime lerner", "ellen macarthur", "gunter pauli", "permaculture", "solar", "ecology", "sustainability", "resilience", "connaissance", "aberkane"],
        "title": "Solarpunk & Impact"
    }
}

def classify_video(title: str, channel_name: str) -> str:
    """Classifie une vidéo dans l'un des 8 domaines de la Life Wheel en fonction de mots-clés."""
    text = f"{title} {channel_name}".lower()
    
    best_domain = "LD01_Business"  # Domaine par défaut
    max_score = 0
    
    for domain, config in LIFE_WHEEL_DOMAINS.items():
        score = sum(2 if kw in text else 0 for kw in config["keywords"])
        # Bonus pour correspondances exactes ou partielles spécifiques
        if score > max_score:
            max_score = score
            best_domain = domain
            
    return best_domain

def init_queue(html_path: str):
    """Parse le fichier Takeout HTML, filtre les vidéos et initialise la queue de traitement."""
    if not os.path.exists(html_path):
        print(f"[-] Erreur : Fichier non trouvé à {html_path}")
        return
        
    print(f"[*] Ingestion du fichier Takeout : {html_path}")
    channels = list(parse_watch_history(html_path))
    
    # Extraction à plat de toutes les vidéos
    all_videos = []
    for channel in channels:
        for video in channel.videos:
            if video.video_id:  # Ignorer les vidéos sans identifiant valide (ex. supprimées)
                all_videos.append(video)
                
    print(f"[+] {len(all_videos)} vidéos extraites avec succès.")
    
    # Tri chronologique inverse (du plus récent au plus ancien)
    # Les vidéos sans date d'observation valide sont repoussées à la fin
    all_videos.sort(
        key=lambda v: v.watched_at if v.watched_at else datetime.min, 
        reverse=True
    )
    
    # Filtrage des identifiants déjà clarifiés ou capturés dans watch_history_rag.csv
    existing_ids = set()
    if RAG_CSV.exists():
        with open(RAG_CSV, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_ids.add(row.get('Issue Identifier'))
                
    queue_data = []
    
    for idx, video in enumerate(all_videos, 1):
        issue_id = f"YT-{video.video_id}"
        if issue_id in existing_ids:
            continue
            
        domain = classify_video(video.title, video.channel_name or "")
        watched_str = video.watched_at.strftime("%Y-%m-%dT%H:%M:%S") if video.watched_at else datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        
        queue_data.append({
            "id": issue_id,
            "title": video.title,
            "url": video.url,
            "channel_name": video.channel_name or "Unknown Channel",
            "channel_url": video.channel_url or "",
            "watched_at": watched_str,
            "domain": domain,
            "folder": LIFE_WHEEL_DOMAINS[domain]["folder"],
            "status": "QUEUED"
        })
        
    # Sauvegarde de la queue
    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
        json.dump(queue_data, f, ensure_ascii=False, indent=2)
        
    print(f"[+] Queue de traitement initialisée : {len(queue_data)} vidéos en attente dans {QUEUE_FILE}")
    return queue_data

def scaffold_next_guide():
    """Récupère la prochaine vidéo non traitée de la queue, crée le scaffold du Guide Geordi et met à jour le CSV."""
    if not QUEUE_FILE.exists():
        print("[-] Erreur : Aucune queue de traitement active. Lancez d'abord l'initialisation.")
        return None
        
    with open(QUEUE_FILE, "r", encoding="utf-8") as f:
        queue = json.load(f)
        
    next_video = None
    for item in queue:
        if item["status"] == "QUEUED":
            next_video = item
            break
            
    if not next_video:
        print("[*] Toutes les vidéos de la queue ont été traitées !")
        return None
        
    # Création du répertoire cible PARA
    target_dir = GEORDI_GUIDES_BASE / next_video["folder"]
    os.makedirs(target_dir, exist_ok=True)
    
    # Nettoyage du titre pour le nom du fichier
    safe_title = "".join(c for c in next_video["title"].lower() if c.isalnum() or c in " -_").replace(" ", "_")
    safe_title = safe_title[:50].strip("_")
    filename = f"resource_{safe_title}.md"
    file_path = target_dir / filename
    
    # Template du Guide Geordi Premium avec Note A3 Zora
    template_content = f"""---
title: "{next_video["title"]}"
author: "Unknown"
channel: "{next_video["channel_name"]}"
duration: "00:00"
date_watched: "{next_video["watched_at"][:10]}"
category: "{next_video["domain"]}"
status: "CLARIFIED_PLANE"
id: "{next_video["id"]}"
---

# Analyse {LIFE_WHEEL_DOMAINS[next_video["domain"]]["title"]} : {next_video["title"]}

## 🧭 Métadonnées Sémantiques & Alignement RAG
- **ID Source** : `{next_video["id"]}`
- **URL Source** : {next_video["url"]}
- **Chaîne** : {next_video["channel_name"]}
- **Date d'Observation** : {next_video["watched_at"]}
- **Axe Sémantique (Zora)** : {next_video["domain"]}

---

## 💡 Concepts Clés & Analyse Stratégique
[Développement approfondi de la ressource. Expliquez les concepts fondamentaux de la vidéo en lien avec la Life Wheel. Minimum 40 lignes d'analyse structurelle].

---

## 🛠️ Entités, Outils & Alignement Infrastructure
| Outil Externe | Rôle Fonctionnel | Alternative Souveraine A'Space OS |
| :--- | :--- | :--- |
| | | |

---

## 🔮 Synthèse Pratique & Alignement Souverain (A'Space OS)
[Comment transposer ces apprentissages sous forme de règles, d'automatisation ou d'habitudes au sein de notre Life OS ou de notre infrastructure technique].

---

## 🚀 Section D.E.A.L (Définir, Éliminer, Automatiser, Libérer)
| Phase | Action Concrète | Objectif Opérationnel |
| :--- | :--- | :--- |
| **Définir** | | |
| **Éliminer** | | |
| **Automatiser** | | |
| **Libérer** | | |

---

# Fiche d'Analyse Approfondie (DIKW Continuité)
### Note Technique A3-01 : Principe d'Identité Zora
[Formulez ici le premier principe sémantique souverain extrait de cette vidéo pour le noyau d'identité Zora de l'USS Discovery].

### Note Technique A3-02 : Directive d'Exécution
[Formulez ici une directive claire d'action ou de contrôle de surcharge cognitive].

*Fin du Guide Obsidian Souverain A'Space OS - Lot Handoff {next_video["id"]}*
"""
    
    # Écriture du fichier scaffold
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(template_content)
        
    # Mise à jour du statut dans la queue
    next_video["status"] = "SCAFFOLDED"
    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)
        
    # Injection dans watch_history_rag.csv en statut CAPTURED
    if RAG_CSV.exists():
        fields = [
            'Issue Identifier', 'Title', 'Channel Name', 'Channel URL', 
            'Duration', 'Date Watched', 'Transcription Raw', 
            'Serendipity Score', 'Category', 'Symphony Status'
        ]
        entry = {
            'Issue Identifier': next_video["id"],
            'Title': next_video["title"],
            'Channel Name': next_video["channel_name"],
            'Channel URL': next_video["channel_url"],
            'Duration': "00:00",
            'Date Watched': next_video["watched_at"],
            'Transcription Raw': f"Scaffolded in Geordi Guides ({next_video['domain']}). Pending deep A3 clarification.",
            'Serendipity Score': "9",
            'Category': next_video["domain"],
            'Symphony Status': "CAPTURED"
        }
        with open(RAG_CSV, 'a', newline='', encoding='utf-8') as f_csv:
            writer = csv.DictWriter(f_csv, fieldnames=fields)
            writer.writerow(entry)
            
    print(f"[+] Prochaine vidéo scaffoldée : '{next_video['title']}' dans {file_path.name}")
    return next_video

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Initialiser la queue : python symphony_takeout_orchestrator.py init <PATH_TO_WATCH_HISTORY_HTML>")
        print("  Scaffolder le suivant : python symphony_takeout_orchestrator.py next")
        sys.exit(1)
        
    cmd = sys.argv[1]
    if cmd == "init" and len(sys.argv) >= 3:
        init_queue(sys.argv[2])
    elif cmd == "next":
        scaffold_next_guide()
    else:
        print("[-] Commande invalide ou argument manquant.")
        sys.exit(1)
