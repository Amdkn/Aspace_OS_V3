# Script : pulse.py (Le Signal du Heraut)
# Architecte : Amadeus | Consultant : Rick Supreme

import os
import requests
import json
import time

# Configuration via variables d'environnement (injectees par Dokploy)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
OPENCLAW_API_URL = os.getenv("OPENCLAW_API_URL", "http://localhost:11434/api/notify")

def send_heartbeat():
    message = (
        "📡 *A'Space Heartbeat* : Rick Supreme est ÉVEILLÉ.\n"
        "🛸 Atelier L0 Activé | Infrastrucure Dokploy UP.\n"
        "--- ANTIGRAVITY STRATEGIC TERMINAL ACTIVE ---"
    )
    
    # 1. Tentative via OpenClaw Gateway (pour logs internes)
    try:
        requests.post(OPENCLAW_API_URL, json={"msg": message}, timeout=5)
    except Exception as e:
        print(f"Note: OpenClaw Gateway inaccessible ({e})")

    # 2. Envoi Direct Telegram (Souveraineté)
    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
        try:
            requests.post(url, json=payload, timeout=10)
            print("Signal envoyé avec succès sur Telegram.")
        except Exception as e:
            print(f"Erreur Telegram direct : {e}")
    else:
        print("Variables TELEGRAM_BOT_TOKEN ou TELEGRAM_CHAT_ID manquantes. Pulse silencieux.")

if __name__ == "__main__":
    send_heartbeat()
