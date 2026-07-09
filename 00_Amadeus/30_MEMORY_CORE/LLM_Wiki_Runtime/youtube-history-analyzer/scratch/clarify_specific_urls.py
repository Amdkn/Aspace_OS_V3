#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
clarify_specific_urls.py — Rédige des fiches Obsidian d'excellence pour les 13 ressources cibles
(10 de la Roue de la Vie pour Life OS et 3 d'Ops Absolus) via OpenRouter / GLM-4.7-Flash.
"""

import os
import re
import csv
import json
import sys
import http.client
import urllib.parse
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

META_FILE = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\scratch\specific_urls_meta.json")
RAG_CSV = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")
GUIDES_BASE = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides")

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

def call_openrouter(prompt: str, system_prompt: str = "") -> str:
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
                return "ERROR: No content in choices."
            elif response.status == 429:
                time.sleep(backoff)
                backoff *= 2.0
            else:
                return f"ERROR: Status {response.status}"
        except Exception as e:
            if attempt == retries - 1:
                return f"ERROR: {str(e)}"
            time.sleep(backoff)
            backoff *= 2.0
            
    return "ERROR: 429 Rate Limit"

def slugify(title):
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s-]+", "-", slug)
    return slug.strip("-")

# Répartition canonique Discovery (LD01 à LD08) de la Roue de la Vie de l'hôte
LIFE_WHEEL_DOMAINS = {
    # LD04_Cognition_Tilly (Cognition and mind)
    "uy-YFZPFT8c": "LD04_Cognition_Tilly",
    "Bgxsx8slDEA": "LD04_Cognition_Tilly",
    "5x3_U7b4eKU": "LD04_Cognition_Tilly",
    
    # LD01_Business_Book (Career and business)
    "TyeBniA85jE": "LD01_Business_Book",
    "BGxpATOGK_M": "LD01_Business_Book",
    "21L-iujzy9U": "LD01_Business_Book",
    
    # LD08_Impact_Georgiou (Impact)
    "qi9tVNA488Q": "LD08_Impact_Georgiou",
    "YCL1IXbvCWY": "LD08_Impact_Georgiou",
    "l0GahkvnWc4": "LD08_Impact_Georgiou",
    "DhQd4kUKj7A": "LD08_Impact_Georgiou"
}

def generate_life_os_guide(video):
    title = video["title"]
    channel = video["uploader"]
    vid_id = video["id"]
    duration = video["duration"]
    date_str = video["date"]
    domain = LIFE_WHEEL_DOMAINS.get(vid_id, "Mind")
    
    system_prompt = (
        "Tu es l'agent sémantique expert d'A'Space OS V2. "
        "Ton but est de rédiger un guide Obsidian premium (>110 lignes) et actionnable pour "
        "le Life OS (Roue de la Vie) de l'utilisateur à partir du titre et de la chaîne de référence. "
        "Ton style est senior, précis, direct et 100% matérialisé en Français technique impeccable."
    )
    
    prompt = f"""Rédige un guide de connaissances Obsidian ultra-dense et d'excellence (>110 lignes) sur le sujet '{title}' pour la Roue de la Vie (Life OS, Domaine : {domain}).

Ta réponse doit STRICTEMENT respecter le format Markdown Obsidian suivant, sans introduction ni blabla :

---
id: YT-{vid_id}
title: "{title}"
channel: "{channel}"
duration: "{duration}"
date: "{date_str}"
category: "Life OS / Roue de la Vie"
domain: "{domain}"
---

# 📖 {title}

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour la Roue de la Vie (Life OS) - Domaine {domain}.

---

## 🧠 Concepts Clés à Haute Densité Sémantique
- **<Concept 1 (Psychologie / Efficacité / Éducation)>** : Fournis une explication philosophique, conceptuelle et pratique très poussée (4-5 lignes complètes) en lien direct avec le sujet '{title}'.
- **<Concept 2>** : Fournis une explication technique et stratégique très poussée (4-5 lignes complètes).
- **<Concept 3>** : Fournis une explication conceptuelle très poussée (4-5 lignes complètes).
- **<Concept 4>** : Fournis une explication conceptuelle très poussée (4-5 lignes complètes).
- **<Concept 5>** : Fournis une explication conceptuelle très poussée (4-5 lignes complètes).
- **<Concept 6>** : Fournis une explication conceptuelle très poussée (4-5 lignes complètes).

## 🛠️ Outillage Stratégique & Matrice d'Alignement
| Outil / Technologie / Approche | Rôle Stratégique | Alignement Souverain A'Space Life OS |
| :--- | :--- | :--- |
| **<Outil/Concept principal>** | <Rôle précis dans l'optimisation personnelle ou business> | <Comment l'exécuter localement, ou l'intégrer dans le quotidien d'A'Space OS> |
| **<Outil secondaire>** | <Rôle stratégique> | <Remplacement souverain ou auto-hébergement> |
| **<Outil complémentaire>** | <Rôle stratégique> | <Remplacement souverain ou auto-hébergement> |

## 🪐 Perspective Souveraine A'Space Life OS (Domaine : {domain})
<Rédige une longue section de 15 à 20 lignes d'analyse conceptuelle profonde expliquant comment intégrer et transposer les enseignements du sujet '{title}' pour optimiser le Domaine '{domain}' de la Roue de la Vie de l'hôte (souveraineté attentionnelle, minimalisme, levier technologique au service de la liberté, digital twin pour la prise de décision de vie, élimination de la fatigue cognitive, etc.)>

## 🕹️ Protocole d'Exécution D.E.A.L
| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | <Action précise sur le mode de vie ou l'organisation> | <But dans l'OS> |
| **Éliminer** | <Action précise de suppression de friction cognitive ou de distraction> | <But dans l'OS> |
| **Automatiser** | <Action précise de délégation ou d'automatisation via n8n local> | <But dans l'OS> |
| **Libérer** | <Action précise pour libérer du temps pour les passions de l'hôte> | <But dans l'OS> |

---
*Fiche de connaissances souveraine de la Roue de la Vie générée sous A'Space OS V2.*
"""
    
    return call_openrouter(prompt, system_prompt)

def generate_ops_guide(video):
    title = video["title"]
    channel = video["uploader"]
    vid_id = video["id"]
    duration = video["duration"]
    date_str = video["date"]
    
    system_prompt = (
        "Tu es l'agent sémantique expert d'A'Space OS V2. "
        "Ton but est de rédiger un guide Obsidian d'excellence et de haute densité (>110 lignes) "
        "pour le Domaine OPS (Opérations, Systématisation, n8n, n8n souverain, processus) de Jerry / Spock L2. "
        "Ton style est senior, technique, orienté systèmes, et 100% matérialisé en Français technique impeccable."
    )
    
    prompt = f"""Rédige un guide de connaissances Obsidian ultra-dense et d'excellence (>110 lignes) sur le sujet '{title}' pour le Domaine des Opérations (OPS).

Ta réponse doit STRICTEMENT respecter le format Markdown Obsidian suivant, sans introduction ni blabla :

---
id: YT-{vid_id}
title: "{title}"
channel: "{channel}"
duration: "{duration}"
date: "{date_str}"
category: "Ops / Systématisation"
---

# 📖 {title}

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour le Domaine OPS (Opérations) - Systématisation et Architectures.

---

## 🧠 Concepts Clés à Haute Densité Sémantique
- **<Concept 1 (Systématisation / Processus)>** : Fournis une explication technique et organisationnelle très poussée (4-5 lignes complètes) en lien direct avec le sujet '{title}'.
- **<Concept 2>** : Fournis une explication technique et organisationnelle très poussée (4-5 lignes complètes).
- **<Concept 3>** : Fournis une explication technique et organisationnelle très poussée (4-5 lignes complètes).
- **<Concept 4>** : Fournis une explication technique et organisationnelle très poussée (4-5 lignes complètes).
- **<Concept 5>** : Fournis une explication technique et organisationnelle très poussée (4-5 lignes complètes).
- **<Concept 6>** : Fournis une explication technique et organisationnelle très poussée (4-5 lignes complètes).

## 🛠️ Outillage Stratégique & Matrice d'Alignement
| Outil / Technologie / Approche | Rôle Stratégique | Alignement Souverain A'Space Ops |
| :--- | :--- | :--- |
| **<Outil/Concept principal (ex: n8n, clickup)>** | <Rôle précis dans l'optimisation des flux opérationnels> | <Comment l'exécuter localement, ou l'intégrer dans le quotidien d'A'Space OS de manière souveraine> |
| **<Outil secondaire>** | <Rôle stratégique> | <Remplacement souverain ou auto-hébergement> |
| **<Outil complémentaire>** | <Rôle stratégique> | <Remplacement souverain ou auto-hébergement> |

## 🪐 Perspective Souveraine A'Space Ops (Systématisation)
<Rédige une longue section de 15 à 20 lignes d'analyse conceptuelle profonde expliquant comment intégrer et transposer les enseignements du sujet '{title}' pour systématiser les opérations d'A'Space OS de manière 100% souveraine (évitement de la dépendance aux GAFAM, isolation réseau, agents spécialisés A3 locaux, automatisation via n8n souverain, réduction des points d'interfaçage tiers, etc.)>

## 🕹️ Protocole d'Exécution D.E.A.L
| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | <Action précise de cartographie des processus opérationnels> | <But dans l'OS> |
| **Éliminer** | <Action précise d'élimination de logiciels redondants ou de goulots d'étranglement> | <But dans l'OS> |
| **Automatiser** | <Action précise de délégation technique ou d'automatisation via n8n local> | <But dans l'OS> |
| **Libérer** | <Action précise pour libérer l'hôte des tâches opérationnelles chronophages> | <But dans l'OS> |

---
*Fiche de connaissances souveraine d'Ops générée sous A'Space OS V2.*
"""
    
    return call_openrouter(prompt, system_prompt)

def generate_it_guide(video):
    title = video["title"]
    channel = video["uploader"]
    vid_id = video["id"]
    duration = video["duration"]
    date_str = video["date"]
    
    system_prompt = (
        "Tu es l'agent sémantique expert d'A'Space OS V2. "
        "Tu rédiges un guide d'excellence Obsidian (>110 lignes) pour le Domaine IT / IA de Kang L2. "
        "Ton style est senior, technique, précis, 100% matérialisé en Français technique impeccable."
    )
    
    prompt = f"""Rédige un guide de connaissances Obsidian ultra-dense et d'excellence (>110 lignes) sur le sujet '{title}' pour le Domaine IT / Souveraineté Technologique.

Ta réponse doit STRICTEMENT respecter le format Markdown Obsidian suivant, sans introduction ni blabla :

---
id: YT-{vid_id}
title: "{title}"
channel: "{channel}"
duration: "{duration}"
date: "{date_str}"
category: "IT / Souveraineté Technologique"
---

# 📖 {title}

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour le Domaine IT - Architecture, Cloud et Algorithmes.

---

## 🧠 Concepts Clés à Haute Densité Sémantique
- **<Concept 1 (Infrastructure / IA)>** : Fournis une explication technique très poussée (4-5 lignes complètes) en lien direct avec le sujet '{title}'.
- **<Concept 2>** : Fournis une explication technique très poussée (4-5 lignes complètes).
- **<Concept 3>** : Fournis une explication technique très poussée (4-5 lignes complètes).
- **<Concept 4>** : Fournis une explication technique très poussée (4-5 lignes complètes).
- **<Concept 5>** : Fournis une explication technique très poussée (4-5 lignes complètes).
- **<Concept 6>** : Fournis une explication technique très poussée (4-5 lignes complètes).

## 🛠️ Outillage Stratégique & Matrice d'Alignement
| Outil / Technologie | Rôle Stratégique | Alignement Souverain A'Space IT |
| :--- | :--- | :--- |
| **<Outil principal>** | <Rôle dans l'infrastructure technologique> | <Auto-hébergement local ou architecture souveraine> |
| **<Outil secondaire>** | <Rôle stratégique> | <Remplacement souverain ou auto-hébergement> |
| **<Outil complémentaire>** | <Rôle stratégique> | <Remplacement souverain ou auto-hébergement> |

## 🪐 Perspective Souveraine A'Space IT
<Rédige une longue section de 15 à 20 lignes d'analyse conceptuelle profonde expliquant comment intégrer et transposer les enseignements du sujet '{title}' pour l'infrastructure technologique et IA d'A'Space OS de manière 100% souveraine (évitement de la dépendance aux GAFAM, sécurité d'infrastructure, hébergement de modèles locaux, protection des données de l'hôte, etc.)>

## 🕹️ Protocole d'Exécution D.E.A.L
| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | <Action précise de cartographie technique ou d'architecture> | <But dans l'OS> |
| **Éliminer** | <Action précise d'élimination de dépendance technologique externe> | <But dans l'OS> |
| **Automatiser** | <Action précise d'intégration dans la forge logicielle locale> | <But dans l'OS> |
| **Libérer** | <Action précise pour libérer l'hôte des complexités de gestion système> | <But dans l'OS> |

---
*Fiche de connaissances souveraine d'IT générée sous A'Space OS V2.*
"""
    
    return call_openrouter(prompt, system_prompt)

def process_life_video(video):
    vid_id = video["id"]
    title = video["title"]
    uploader = video["uploader"]
    domain = LIFE_WHEEL_DOMAINS.get(vid_id, "LD04_Cognition_Tilly")
    
    try:
        print(f"[*] Traitement et double routage parallèle de : {title[:60]}...")
        slug = slugify(title)
        
        # 1. Écriture obligatoire pour le Business OS d'Ops : Toujours à plat directement sous 02_Ops unique
        content_ops = generate_ops_guide(video)
        ops_dir = GUIDES_BASE / "02_Ops"
        ops_dir.mkdir(parents=True, exist_ok=True)
        ops_filepath = ops_dir / f"{slug}.md"
        ops_filepath.write_text(content_ops, encoding="utf-8")
        print(f"  [+] Obsidian page created in Business OS (02_Ops): {ops_filepath.name}")
        
        # 2. Écriture obligatoire pour la Roue de la Vie : sous 09_Life_OS avec le vrai nom canonique Discovery LDXX
        content_life = generate_life_os_guide(video)
        life_dir = GUIDES_BASE / "09_Life_OS" / domain
        life_dir.mkdir(parents=True, exist_ok=True)
        life_filepath = life_dir / f"{slug}.md"
        life_filepath.write_text(content_life, encoding="utf-8")
        print(f"  [+] Obsidian page created in Life OS ({domain}): {life_filepath.name}")
        
        return vid_id, True
    except Exception as e:
        print(f"  [-] Erreur pour {vid_id} : {e}")
        return vid_id, False

def process_ops_video(video):
    vid_id = video["id"]
    title = video["title"]
    uploader = video["uploader"]
    
    try:
        print(f"[*] Traitement Ops Absolus : {title[:60]}...")
        content = generate_ops_guide(video)
        
        slug = slugify(title)
        
        # Toutes les fiches d'Ops vont directement dans le dossier unique 02_Ops sans uploader
        target_dir = GUIDES_BASE / "02_Ops"
        target_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = target_dir / f"{slug}.md"
        filepath.write_text(content, encoding="utf-8")
        print(f"  [+] Obsidian page created in 02_Ops: {filepath.name}")
        return vid_id, True
    except Exception as e:
        print(f"  [-] Erreur pour {vid_id} : {e}")
        return vid_id, False

def run_specific_clarification():
    if not META_FILE.exists():
        print("[-] specific_urls_meta.json non trouve.")
        return
        
    with open(META_FILE, "r", encoding="utf-8") as f:
        meta_data = json.load(f)
        
    life_videos = meta_data.get("life_os", [])
    ops_videos = meta_data.get("ops", [])
    
    success_ids = set()
    
    # 3 workers en parallèle
    max_workers = 3
    
    print("\n" + "="*60)
    print("[*] Lancement de la clarification des ressources Life OS (Roue de la Vie)...")
    print("="*60)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_life_video, v): v for v in life_videos}
        for fut in as_completed(futures):
            vid_id, success = fut.result()
            if success:
                success_ids.add(vid_id)
                
    print("\n" + "="*60)
    print("[*] Lancement de la clarification des ressources d'Ops Absolues...")
    print("="*60)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_ops_video, v): v for v in ops_videos}
        for fut in as_completed(futures):
            vid_id, success = fut.result()
            if success:
                success_ids.add(vid_id)
                
    # Ingestion dans watch_history_rag.csv
    if RAG_CSV.exists() and success_ids:
        rows = []
        with open(RAG_CSV, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(r)
                
        # Dictionnaire pour vérification des ID existants dans watch_history_rag.csv
        existing_in_csv = {r["Issue Identifier"] for r in rows}
        
        # Mettre à jour les lignes existantes ou ajouter les nouvelles au statut CLARIFIED_PLANE
        all_videos = life_videos + ops_videos
        
        for v in all_videos:
            vid_id_str = f"YT-{v['id']}"
            if vid_id_str in success_ids:
                # Si déjà présent, passer à CLARIFIED_PLANE
                found = False
                for r in rows:
                    if r["Issue Identifier"] == vid_id_str:
                        r["Symphony Status"] = "CLARIFIED_PLANE"
                        found = True
                        break
                # Si absent, l'injecter au propre
                if not found:
                    domain = LIFE_WHEEL_DOMAINS.get(v['id'], "Ops" if v in ops_videos else "LD04_Cognition_Tilly")
                    rows.append({
                        'Issue Identifier': vid_id_str,
                        'Title': v['title'],
                        'Channel Name': v['uploader'],
                        'Channel URL': v['url'],
                        'Duration': v['duration'],
                        'Date Watched': datetime.now().strftime("%Y-%m-%d"),
                        'Transcription Raw': "Captured and clarified via specific URLs conductor.",
                        'Serendipity Score': "9",
                        'Category': domain if v in life_videos else "Ops",
                        'Symphony Status': "CLARIFIED_PLANE"
                    })
                    
        with open(RAG_CSV, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
            
        print(f"\n[+] watch_history_rag.csv synchronise avec {len(success_ids)} videos passees a CLARIFIED_PLANE.")

if __name__ == "__main__":
    run_specific_clarification()
