"""
deal_symphony_bridge.py — D.E.A.L actionability bridge: Telegram notifications (A0 Engagement) and Affine drafts.
Uses Python 3.14 (C:\Python314\python.exe) and native Telegram API requests.
"""

from __future__ import annotations
import http.client
import urllib.parse
import json
import os
import sys
from pathlib import Path
import re
from datetime import datetime

# Telegram configuration (Test Key Pragma 2026-06-15 : token via env var User scope)
# A0 mandate : "utilise le token en clair pour configurer telegram" — env var User scope = OK
# Set command : [Environment]::SetEnvironmentVariable('TELEGRAM_BOT_TOKEN', '<token>', 'User')
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = "8466501613"  # A0 User ID (constant, not secret)

AFFINE_DRAFT_PATH = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\affine_deal_drafts.md")

def send_telegram_message(text: str) -> bool:
    """Send a structured markdown message to A0 via Telegram Bot API."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    parsed_url = urllib.parse.urlparse(url)
    host = parsed_url.netloc
    path = parsed_url.path
    
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    
    try:
        conn = http.client.HTTPSConnection(host, timeout=15)
        conn.request("POST", path, json.dumps(payload), headers)
        response = conn.getresponse()
        res_data = response.read().decode("utf-8")
        
        if response.status == 200:
            print("[+] Telegram notification sent successfully to A0.")
            return True
        else:
            print(f"[!] Telegram API failed with status {response.status}: {res_data}")
            return False
    except Exception as e:
        print(f"[!] Exception during Telegram send: {e}")
        return False

def generate_affine_deal_drafts(video_title: str, channel_name: str, draft_sop: str) -> None:
    """Add or update the SOP / Playbook draft in our Affine drafts markdown file without duplicates."""
    file_exists = AFFINE_DRAFT_PATH.exists()
    
    header_section = f"## 📝 Draft SOP — {video_title} (Chaîne: {channel_name})"
    markdown_content = f"""{header_section}
*Date de capture : {datetime.now().strftime('%Y-%m-%d')}*

### 💡 Intention sémantique
Ce draft a été extrait du raffinage YouTube et attend sa clarification finale D.E.A.L sous Affine.

### 📋 SOP Ébauchée
{draft_sop}

---
"""
    
    try:
        content = ""
        if file_exists:
            with open(AFFINE_DRAFT_PATH, mode="r", encoding="utf-8") as f:
                content = f.read()
                
        if not content:
            content = "# 📊 Affine D.E.A.L — Drafts de SOPs & Innovations\n\nCe document regroupe les SOPs et playbooks ébauchés à valider lors de la Weekly Review sous Affine.\n"
            
        # Chercher si la section existe déjà
        if header_section in content:
            print(f"[*] Updating existing draft SOP block for: {video_title}")
            # Regex pour capturer le bloc depuis la section cible jusqu'à la prochaine section "## 📝 Draft SOP —" ou la fin
            pattern = re.escape(header_section) + r"[\s\S]*?(?=\n## 📝 Draft SOP —|\Z)"
            content = re.sub(pattern, markdown_content.strip(), content)
        else:
            print(f"[+] Appending new draft SOP block for: {video_title}")
            # Veiller à ajouter des retours à la ligne propres
            if not content.endswith("\n\n"):
                content = content.rstrip() + "\n\n"
            content += markdown_content
            
        with open(AFFINE_DRAFT_PATH, mode="w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"[+] Saved draft SOP in Affine Drafts: {AFFINE_DRAFT_PATH.name}")
    except Exception as e:
        print(f"[!] Failed to write Affine draft: {e}")


def notify_a0_engagement(video_title: str, channel_name: str, score: int, obsidian_filename: str) -> None:
    """Send engagement alert to A0 on Telegram for validation."""
    message = f"""*🧿 A'Space OS V2 — Raffinage YouTube*

[+] *Nouvelle Ressource Clarifiée !*
*Titre* : {video_title}
*Chaîne* : {channel_name}
*Serendipity Score* : {score}/10
*Fichier Obsidian* : `{obsidian_filename}`

*D.E.A.L Actionnabilité* :
- Draft SOP généré dans Geordi's Guides
- Liens transverses câblés vers les 8 domaines de Spock et la Roue de la vie.

_Réponds GO pour sceller et automatiser cette ressource._
"""
    send_telegram_message(message)

if __name__ == "__main__":
    # Test send
    from datetime import datetime
    print("Testing Telegram Notification...")
    test_title = "Building a Sovereign Compounding Knowledge Graph"
    notify_a0_engagement(test_title, "Karpathy AI", 9, "resource_building_sovereign_compounding.md")
    
    test_sop = "- Étape 1: Exécuter le pipeline de capture brute\n- Étape 2: Lancer l'orchestrateur de clarification sémantique\n- Étape 3: Valider le draft sur Telegram"
    generate_affine_deal_drafts(test_title, "Karpathy AI", test_sop)
