import os
import re
import csv
import json
import sys
import http.client
from datetime import datetime
from pathlib import Path

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

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
    except Exception as e:
        return f"ERROR: {str(e)}"
    return "ERROR"

video = {
    "id": "mS1lCfJ5Yig",
    "title": "I Built a Full SEO System With Antigravity + Agent OS!",
    "uploader": "Julian Goldie SEO",
    "duration": "07:43",
    "date": "20260530",
    "url": "https://www.youtube.com/watch?v=mS1lCfJ5Yig"
}

# 1. Génération du guide sémantique Business OS (Ops)
system_prompt_ops = (
    "Tu es l'agent sémantique expert d'A'Space OS V2. "
    "Ton but est de rédiger un guide Obsidian d'excellence et de haute densité (>110 lignes) "
    "pour le Domaine OPS (Opérations, Systématisation, n8n, n8n souverain, processus) de Jerry / Spock L2. "
    "Ton style est senior, technique, orienté systèmes, et 100% matérialisé en Français technique impeccable."
)

prompt_ops = f"""Rédige un guide de connaissances Obsidian ultra-dense et d'excellence (>110 lignes) sur le sujet '{video["title"]}' pour le Domaine des Opérations (OPS).

Ta réponse doit STRICTEMENT respecter le format Markdown Obsidian suivant, sans introduction ni blabla :

---
id: YT-{video["id"]}
title: "{video["title"]}"
channel: "{video["uploader"]}"
duration: "{video["duration"]}"
date: "{video["date"]}"
category: "Ops / Systématisation"
---

# 📖 {video["title"]}

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour le Domaine OPS (Opérations) - Systématisation et Architectures.

---

## 🧠 Concepts Clés à Haute Densité Sémantique
- **Synergie Antigravity + Agent OS (SEO Systémique)** : Fournis une explication technique et organisationnelle très poussée (4-5 lignes complètes) sur comment Julian Goldie intègre l'IA agentique d'Antigravity pour automatiser le SEO en boucle fermée.
- **Workflow SEO à Haute Vélocité** : Fournis une explication technique et organisationnelle très poussée (4-5 lignes complètes) sur le pipeline de crawling, rédaction, publication et audit sans intervention humaine.
- **Briques de Souveraineté IA locale** : Fournis une explication technique et organisationnelle très poussée (4-5 lignes complètes) sur l'intérêt d'exécuter ces agents en local ou en VPS souverain sans dépendre de logiciels propriétaires SaaS.
- **Micro-Agents Spécialisés (Strate A3)** : Fournis une explication technique et organisationnelle très poussée (4-5 lignes complètes).
- **Structures SOPs & Harnees de Rick** : Fournis une explication technique et organisationnelle très poussée (4-5 lignes complètes).
- **Mesure de Performance & Signal ZORA** : Fournis une explication technique et organisationnelle très poussée (4-5 lignes complètes).

## 🛠️ Outillage Stratégique & Matrice d'Alignement
| Outil / Technologie / Approche | Rôle Stratégique | Alignement Souverain A'Space Ops |
| :--- | :--- | :--- |
| **Antigravity CLI & Agents** | Automatisation et génération sémantique SEO | Exécution locale, Dockerisé ou orchestré sous WSL |
| **Agent OS Framework** | Routage et synchronisation du lore de connaissances | Système A'Space OS local |
| **n8n souverain (Local/VPS)** | Orchestration de workflows de crawling et publication | Remplacement complet de Make.com/Zapier |

## 🪐 Perspective Souveraine A'Space Ops (Systématisation)
Rédige une longue section de 15 à 20 lignes d'analyse conceptuelle profonde expliquant comment intégrer et transposer les enseignements du sujet '{video["title"]}' pour systématiser les opérations d'A'Space OS de manière 100% souveraine (évitement de la dépendance aux GAFAM, isolation réseau, agents spécialisés A3 locaux, automatisation via n8n souverain, réduction des points d'interfaçage tiers, etc.)

## 🕹️ Protocole d'Exécution D.E.A.L
| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | Cartographier le pipeline SEO agentique d'Antigravity | But dans l'OS |
| **Éliminer** | Supprimer les outils SaaS intermédiaires et dépendances onéreuses | But dans l'OS |
| **Automatiser** | Connecter les scripts Antigravity à n8n local pour publication automatique | But dans l'OS |
| **Libérer** | Écarter l'hôte de toute tâche de rédaction ou d'optimisation répétitive | But dans l'OS |

---
*Fiche de connaissances souveraine d'Ops générée sous A'Space OS V2.*
"""

# 2. Génération du guide sémantique Roue de la Vie (LD04_Cognition_Tilly)
system_prompt_life = (
    "Tu es l'agent sémantique expert d'A'Space OS V2. "
    "Ton but est de rédiger un guide Obsidian premium (>110 lignes) et actionnable pour "
    "le Life OS (Roue de la Vie) de l'utilisateur à partir du titre et de la chaîne de référence. "
    "Ton style est senior, précis, direct et 100% matérialisé en Français technique impeccable."
)

prompt_life = f"""Rédige un guide de connaissances Obsidian ultra-dense et d'excellence (>110 lignes) sur le sujet '{video["title"]}' pour la Roue de la Vie (Life OS, Domaine : LD04_Cognition_Tilly).

Ta réponse doit STRICTEMENT respecter le format Markdown Obsidian suivant, sans introduction ni blabla :

---
id: YT-{video["id"]}
title: "{video["title"]}"
channel: "{video["uploader"]}"
duration: "{video["duration"]}"
date: "{video["date"]}"
category: "Life OS / Roue de la Vie"
domain: "LD04_Cognition_Tilly"
---

# 📖 {video["title"]}

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour la Roue de la Vie (Life OS) - Domaine LD04_Cognition_Tilly.

---

## 🧠 Concepts Clés à Haute Densité Sémantique
- **Expansion cognitive via Antigravity** : Fournis une explication philosophique, conceptuelle et pratique très poussée (4-5 lignes complètes) sur comment déléguer son infrastructure mentale à des agents sémantiques.
- **Réduction de la charge mentale opérationnelle** : Fournis une explication technique et stratégique très poussée (4-5 lignes complètes) sur la libération de la fatigue attentionnelle.
- **Souveraineté attentionnelle par l'automatisation** : Fournis une explication conceptuelle très poussée (4-5 lignes complètes) sur le recentrage de l'hôte sur ses passions créatives.
- **IA comme miroir de pensée (Digital Twin)** : Fournis une explication conceptuelle très poussée (4-5 lignes complètes).
- **Vibration et alignement existentiel de la forge** : Fournis une explication conceptuelle très poussée (4-5 lignes complètes).
- **Cadence 12WY et régulation de l'énergie** : Fournis une explication conceptuelle très poussée (4-5 lignes complètes).

## 🛠️ Outillage Stratégique & Matrice d'Alignement
| Outil / Technologie / Approche | Rôle Stratégique | Alignement Souverain A'Space Life OS |
| :--- | :--- | :--- |
| **Antigravity + Agent OS** | Externalisation de la cognition et de la synthèse de connaissances | Système A'Space local sécurisé |
| **Obsidian LLM Wiki** | Mémoire externe structurée et cristallisation d'instincts | Zéro-Knowledge hébergé en local |
| **Discovery / ZORA** | Mesure continue de la fatigue attentionnelle et cognitive | Tableau de bord de pilotage Life OS |

## 🪐 Perspective Souveraine A'Space Life OS (Domaine : LD04_Cognition_Tilly)
Rédige une longue section de 15 à 20 lignes d'analyse conceptuelle profonde expliquant comment intégrer et transposer les enseignements du sujet '{video["title"]}' pour optimiser le Domaine 'LD04_Cognition_Tilly' de la Roue de la Vie de l'hôte (souveraineté attentionnelle, minimalisme, levier technologique au service de la liberté, digital twin pour la prise de décision de vie, élimination de la fatigue cognitive, etc.)

## 🕹️ Protocole d'Exécution D.E.A.L
| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | Établir les limites de la mémoire déléguée à Antigravity | But dans l'OS |
| **Éliminer** | Éliminer les tâches de recherche documentaires à faible valeur | But dans l'OS |
| **Automatiser** | Lancer la clarification autonome de connaissances via GLM | But dans l'OS |
| **Libérer** | Libérer des blocs de temps ininterrompus pour la réflexion philosophique | But dans l'OS |

---
*Fiche de connaissances souveraine de la Roue de la Vie générée sous A'Space OS V2.*
"""

print("[*] Génération de la fiche Ops...")
content_ops = call_openrouter(prompt_ops, system_prompt_ops)
ops_dir = GUIDES_BASE / "02_Ops"
ops_dir.mkdir(parents=True, exist_ok=True)
ops_filepath = ops_dir / "i-built-a-full-seo-system-with-antigravity-agent-os.md"
ops_filepath.write_text(content_ops, encoding="utf-8")
print(f"  [+] Fiche Ops créée: {ops_filepath}")

print("[*] Génération de la fiche Life OS...")
content_life = call_openrouter(prompt_life, system_prompt_life)
life_dir = GUIDES_BASE / "09_Life_OS" / "LD04_Cognition_Tilly"
life_dir.mkdir(parents=True, exist_ok=True)
life_filepath = life_dir / "i-built-a-full-seo-system-with-antigravity-agent-os.md"
life_filepath.write_text(content_life, encoding="utf-8")
print(f"  [+] Fiche Life OS créée: {life_filepath}")

# 3. Ingestion dans watch_history_rag.csv
if RAG_CSV.exists():
    rows = []
    with open(RAG_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
            
    vid_id_str = "YT-mS1lCfJ5Yig"
    found = False
    for r in rows:
        if r["Issue Identifier"] == vid_id_str:
            r["Symphony Status"] = "CLARIFIED_PLANE"
            found = True
            break
            
    if not found:
        rows.append({
            'Issue Identifier': vid_id_str,
            'Title': video['title'],
            'Channel Name': video['uploader'],
            'Channel URL': video['url'],
            'Duration': video['duration'],
            'Date Watched': datetime.now().strftime("%Y-%m-%d"),
            'Transcription Raw': "I Built a Full SEO System With Antigravity + Agent OS! - Clarified.",
            'Serendipity Score': "9",
            'Category': "LD04_Cognition_Tilly",
            'Symphony Status': "CLARIFIED_PLANE"
        })
        
    with open(RAG_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print("[+] RAG synchronisé.")
