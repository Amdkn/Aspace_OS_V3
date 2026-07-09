"""
symphony_gtd_orchestrator.py — Clarification GTD, Extraction sémantique (LLM) & Double-Way Obsidian Links.
Uses Python 3.14 (C:\Python314\python.exe) and local MiniMax API.
"""

from __future__ import annotations
import csv
import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime
import http.client
import urllib.parse

# Setup local paths
sys.path.append(str(Path(__file__).parent))

LOCAL_CSV_PATH = Path(__file__).parent / "watch_history_rag.csv"
GEORDI_DIR = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides")
SPOCK_DIR = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\02_Areas_Spock")

# 8 Domaines de Business Pulse (Spock)
BUSINESS_DOMAINS = ["Growth", "Sales", "Product", "Ops", "IT", "Finance", "People", "Legal"]

# 8 Domaines de la Roue de la vie
LIFE_DOMAINS = ["Health", "Mind", "Social", "Family", "Play", "Impact", "Career", "Finance"]

def call_minimax_llm(prompt: str, system_prompt: str = "") -> str:
    """Make a HTTP call to the local Ollama API endpoint using qwen3.5:9b (or fallback to MiniMax if Ollama is unavailable)."""
    # Try calling Ollama local first (Frugalité Maximax)
    ollama_host = "127.0.0.1"
    ollama_port = 11434
    ollama_model = "qwen3.5:9b"
    
    print(f"[*] Attempting local Ollama inference on CPU with model: {ollama_model}...")
    
    ollama_payload = {
        "model": ollama_model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }
    
    try:
        conn = http.client.HTTPConnection(ollama_host, ollama_port, timeout=None)
        conn.request("POST", "/v1/chat/completions", json.dumps(ollama_payload), {"Content-Type": "application/json"})
        response = conn.getresponse()
        res_data = response.read().decode("utf-8")
        
        if response.status == 200:
            res_json = json.loads(res_data)
            choices = res_json.get("choices", [])
            if choices:
                content = choices[0].get("message", {}).get("content", "").strip()
                # Clean thinking tags if present in output
                content = re.sub(r"<think>[\s\S]*?</think>", "", content).strip()
                print("[+] Local Ollama inference completed successfully.")
                return content
            else:
                print("[!] Local Ollama response parsed but choices array was empty.")
        else:
            print(f"[!] Local Ollama call returned status {response.status}: {res_data}")
    except Exception as e:
        print(f"[!] Local Ollama inference failed or timed out: {e}")
        print("[*] Falling back to remote MiniMax API gateway...")

    # Remote MiniMax Fallback
    api_key = os.environ.get("ANTHROPIC_API_KEY", "") or os.environ.get("MINIMAX_API_KEY", "")
    base_url = "https://api.minimax.io"  # Verified working gateway host
    model = "MiniMax-M2.7"  # Target the verified high-quality model
    
    if not api_key:
        # Check fallback files
        hermes_env = Path(r"C:\Users\amado\.hermes\.env")
        if hermes_env.exists():
            with open(hermes_env, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("MINIMAX_API_KEY="):
                        api_key = line.split("=", 1)[1].strip()
                        
    if not api_key:
        print("[!] Warning: MiniMax API Key not found. Simulating extraction fallback.")
        return "FALLBACK: LLM Extraction skipped due to missing API key."
        
    parsed_url = urllib.parse.urlparse(base_url)
    host = parsed_url.netloc
    
    # Route to the verified Anthropic-compatible messages endpoint
    path = "/anthropic/v1/messages"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01"
    }
    
    payload = {
        "model": model,
        "max_tokens": 4096,
        "system": system_prompt,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }
    
    try:
        conn = http.client.HTTPSConnection(host, timeout=120)
        conn.request("POST", path, json.dumps(payload), headers)
        response = conn.getresponse()
        res_data = response.read().decode("utf-8")
        
        if response.status == 200:
            res_json = json.loads(res_data)
            # Fetch content array blocks
            content_blocks = res_json.get("content", [])
            text_parts = []
            for block in content_blocks:
                if block.get("type") == "text":
                    text_parts.append(block.get("text", ""))
            
            content = "".join(text_parts).strip()
            # Clean thinking tags if present in output
            content = re.sub(r"<think>[\s\S]*?</think>", "", content).strip()
            return content
        else:
            print(f"[!] API call failed with status {response.status}: {res_data}")
            return f"ERROR: API returned status {response.status}"
    except Exception as e:
        print(f"[!] Exception during API call: {e}")
        return f"ERROR: Exception occurred - {str(e)}"

def slugify(text: str) -> str:
    """Create a URL-safe slug."""
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")

def generate_obsidian_resource(
    video_title: str,
    channel_name: str,
    transcript: str,
    category: str,
    score: int
) -> tuple[str, str]:
    """
    Generate the Obsidian PARA Resource Page with Double-Way Junction Links.
    Returns (filename, content).
    """
    print(f"[*] Running LLM Extraction for: {video_title[:50]}...")
    
    system_prompt = (
        "Tu es l'agent sémantique d'A'Space OS. Ton rôle est d'extraire la substantifique moelle "
        "d'une transcription de vidéo pour en faire une ressource de connaissance structurée dans Obsidian. "
        "Sois précis, technique et direct. Réponds en Français."
    )
    
    prompt = f"""Analyse la transcription de la vidéo YouTube suivante :
Titre : {video_title}
Chaîne : {channel_name}
Catégorie : {category}

Transcription (extraits ou complète) :
{transcript[:8000]}  # Limit for safety

Rédige une fiche de connaissances structurée selon les sections suivantes :
1. **Concepts Clés** : Théories, architectures, idées ou frameworks abordés (ex: RAG, Agentic Loop, Karpathy Loop).
2. **Entités & Outils** : Outils logiciels, technologies, entreprises ou figures citées (ex: Vercel, Supabase, Anthropic).
3. **Synthèse Pratique** : Un résumé condensé et orienté exécution pour un OS souverain autonome.
4. **Actionnabilité (D.E.A.L)** :
   - D (Définir) : Quelle SOP ou cron peut-on ébaucher à partir de là ?
   - E (Éliminer) : Quelle dette technique ou config obsolète peut-on retirer ?
   - A (Automatiser) : Qu'est-ce qui peut être délégué à un agent en tâche de fond ?
   - L (Libérer) : Comment cela simplifie-t-il le travail humain ?

Ne mets pas de blabla ou d'introduction. Produis uniquement le contenu Markdown structuré.
"""

    extraction = call_minimax_llm(prompt, system_prompt)
    
    # Classify domains for Double-Way links
    # Let's map dynamically using simple keyword heuristics
    assigned_biz: list[str] = []
    assigned_life: list[str] = []
    
    title_lower = video_title.lower() + " " + category.lower()
    
    # 8 Domaines de Business Pulse (Jerry Spock L2)
    if "growth" in title_lower or "marketing" in title_lower or "ads" in title_lower:
        assigned_biz.append("Growth")
    if "sales" in title_lower or "revenue" in title_lower:
        assigned_biz.append("Sales")
    if "product" in title_lower or "design" in title_lower or "ux" in title_lower:
        assigned_biz.append("Product")
    if "ops" in title_lower or "workflow" in title_lower or "process" in title_lower:
        assigned_biz.append("Ops")
    if "it" in title_lower or "code" in title_lower or "software" in title_lower or "ai" in title_lower:
        assigned_biz.append("IT")
    if "finance" in title_lower or "budget" in title_lower or "capital" in title_lower:
        assigned_biz.append("Finance")
    if "people" in title_lower or "team" in title_lower or "hr" in title_lower:
        assigned_biz.append("People")
    if "legal" in title_lower or "compliance" in title_lower or "ip" in title_lower:
        assigned_biz.append("Legal")
        
    # Default to IT / Ops if empty for AI/OS
    if not assigned_biz and (category in ["AI", "OS_Dev"]):
        assigned_biz.extend(["IT", "Ops"])
        
    # 8 Domaines de la Roue de la vie (Discovery L1)
    if "health" in title_lower or "medical" in title_lower:
        assigned_life.append("Health")
    if "mind" in title_lower or "philosophy" in title_lower or "psychology" in title_lower:
        assigned_life.append("Mind")
    if "social" in title_lower or "network" in title_lower or "comms" in title_lower:
        assigned_life.append("Social")
    if "family" in title_lower:
        assigned_life.append("Family")
    if "play" in title_lower or "entertainment" in title_lower:
        assigned_life.append("Play")
    if "impact" in title_lower or "climate" in title_lower or "legacy" in title_lower:
        assigned_life.append("Impact")
    if "career" in title_lower or "business" in title_lower or "job" in title_lower:
        assigned_life.append("Career")
    if "finance" in title_lower or "investing" in title_lower:
        assigned_life.append("Finance")
        
    if not assigned_life:
        assigned_life.append("Career")
        
    # Double-Way Junction Links Section
    junctions_md = "\n## 🧿 Jonctions Transverses (Double-Way Links)\n\n"
    junctions_md += "### Business Pulse (Jerry L2)\n"
    for b in assigned_biz:
        junctions_md += f"- [[02_Areas_Spock/{b}|Spock Domain — {b}]]\n"
        
    junctions_md += "\n### Roue de la Vie (Discovery L1)\n"
    for l in assigned_life:
        junctions_md += f"- [[02_Areas_Spock/{l}|Life Wheel — {l}]]\n"
        
    junctions_md += "\n### Fondations A'Space OS\n"
    junctions_md += "- [[03_Resources_Geordi/A3_Geordi_Resources_Spec|Geordi Resources Spec]]\n"
    junctions_md += "- [[00_Index/index_youtube_rag|YouTube RAG Hub]]\n"
    
    filename = f"resource_{slugify(video_title[:40])}.md"
    
    full_markdown = f"""---
id: {slugify(video_title[:40])}
title: "{video_title}"
channel: "{channel_name}"
category: "{category}"
serendipity_score: {score}
date_extracted: {datetime.now().strftime('%Y-%m-%d')}
type: resource
tags: [#youtube, #rag, #{category.lower()}]
---

# {video_title}

{extraction}

{junctions_md}

---
*Généré automatiquement par l'Orchestrateur Symphony A'Space OS*
"""
    return filename, full_markdown

def run_clarification_pipeline(limit: int = 1):
    """
    Clarify GTD & Process sémantique pipeline.
    Reads CAPTURED rows, extracts sémantique knowledge, generates files, and marks as CLARIFIED_PLANE.
    """
    if not LOCAL_CSV_PATH.exists():
        print("[-] No Local RAG CSV found. Execute gws_sheets_adapter.py first.")
        return
        
    rows = []
    with open(LOCAL_CSV_PATH, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
            
    captured_rows = [r for r in rows if r["Symphony Status"] == "CAPTURED"]
    print(f"[*] Found {len(captured_rows)} videos in CAPTURED status (Inbox).")
    
    processed_count = 0
    GEORDI_DIR.mkdir(parents=True, exist_ok=True)
    
    for row in captured_rows:
        if limit is not None and processed_count >= limit:
            print(f"[*] Reached process limit of {limit} videos. Stopping clarification batch.")
            break
            
        score = int(row["Serendipity Score"])
        category = row["Category"]
        
        # Filter utility criteria: score >= 7 and category matches desired domains (including Life Wheel LD*)
        valid_categories = ["AI", "Business", "OS_Dev", "Sales", "Finance", "Growth", "IT", "Ops", "Product", "People", "Legal"]
        is_life_wheel = category.startswith("LD0") or category.startswith("LD1")
        if score >= 7 and (category in valid_categories or is_life_wheel):
            print(f"\n[+] Video PASSED Utility Filter! (Score: {score}/10, Category: {category})")
            
            # Generate Obsidian Resource Page
            filename, content = generate_obsidian_resource(
                video_title=row["Title"],
                channel_name=row["Channel Name"],
                transcript=row["Transcription Raw"],
                category=category,
                score=score
            )
            
            # Write to Obsidian Geordi Section
            filepath = GEORDI_DIR / filename
            filepath.write_text(content, encoding="utf-8")
            print(f"  [+] Obsidian page created: {filepath.name}")
            
            # Câblage automatique D.E.A.L : Drafts Affine & Notification Telegram
            try:
                print("  [*] Triggering D.E.A.L bridge...")
                from deal_symphony_bridge import notify_a0_engagement, generate_affine_deal_drafts
                
                # Extraction de la section D.E.A.L du Markdown pour Affine
                sop_match = re.search(r"##\s+4\.\s+Actionnabilité\s*\(D\.E\.A\.L\)([\s\S]+?)(?=\n##\s+|\Z)", content, re.IGNORECASE)
                draft_sop = sop_match.group(1).strip() if sop_match else "- Ébauche de SOP à définir à partir du rapport de raffinage."
                
                # Générer le draft d'SOP pour Affine
                generate_affine_deal_drafts(row["Title"], row["Channel Name"], draft_sop)
                
                # Envoyer la notification d'engagement à A0 sur Telegram
                notify_a0_engagement(row["Title"], row["Channel Name"], score, filename)
            except Exception as bridge_err:
                print(f"  [!] D.E.A.L Bridge execution failed: {bridge_err}")
            
            row["Symphony Status"] = "CLARIFIED_PLANE"
            processed_count += 1
        else:
            print(f"\n[-] Video SKIPPED Utility Filter (Score: {score}/10, Category: {category}): {row['Title'][:50]}")
            row["Symphony Status"] = "SKIPPED"
            
    # Rewrite CSV with updated status
    if captured_rows:
        with open(LOCAL_CSV_PATH, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=row.keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"\n[+] Statuses updated in Local RAG CSV. {processed_count} clarified.")
    else:
        print("\n[+] No new captured videos to process.")

if __name__ == "__main__":
    run_clarification_pipeline()
