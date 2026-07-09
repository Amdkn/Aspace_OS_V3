"""
telegram_warmode_push.py — Pousse le digest War Mode vers Telegram (observabilité, pas HITL).

A+ observe sans intervenir. Ce script ne DEMANDE rien à Telegram — il POUSSE (one-way).
Régénère le digest via collector_14_warmode, puis envoie via Bot API sendMessage.

Requiert (Test Key Pragma, env User scope) :
  TELEGRAM_BOT_TOKEN  — le token du bot A'Space
  TELEGRAM_CHAT_ID    — le chat où pousser (A+ doit avoir écrit au bot 1× pour l'obtenir)

Sans ces 2 valeurs → écrit le digest dans un outbox local + explique comment câbler.
Pur stdlib, lecture seule sur les canons, jamais de secret loggé.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

CITADEL = Path(__file__).resolve().parent.parent
COLLECTOR = CITADEL / "collectors" / "collector_14_warmode.py"
DIGEST = CITADEL / "data" / "14_warmode_digest.txt"
OUTBOX = CITADEL / "data" / "14_warmode_telegram_outbox.txt"

# Source locale agnostique (Test Key Pragma) : les creds Telegram vivent dans .minimax,
# le script les lit au runtime. JAMAIS hardcodé, JAMAIS loggé en clair.
MINIMAX = Path.home() / ".minimax"
BINDINGS = MINIMAX / "channel-bindings.yaml"
OWNER = MINIMAX / "channel-owner.yaml"


def creds_from_minimax() -> tuple[str | None, str | None]:
    """Lit bot_token (channel-bindings) + chat_id (channel-owner) depuis .minimax."""
    token = chat = None
    try:
        for line in BINDINGS.read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.match(r"^\s*telegram:mavis:(\d{6,}:[A-Za-z0-9_-]{20,}):\s*$", line)
            if m:
                token = m.group(1)
                break
    except OSError:
        pass
    try:
        m = re.search(r"ownerSenderId:\s*'?(\d{4,})'?", OWNER.read_text(encoding="utf-8", errors="replace"))
        if m:
            chat = m.group(1)
    except OSError:
        pass
    return token, chat


def refresh_digest() -> str:
    subprocess.run([sys.executable, str(COLLECTOR)],
                   env={**os.environ, "PYTHONIOENCODING": "utf-8"},
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return DIGEST.read_text(encoding="utf-8") if DIGEST.exists() else "(digest vide)"


# Exfil guard (ClaudeClaw Mission Control pattern) : scan AVANT tout envoi externe.
# Un agent socially-engineered/buggé ne doit jamais échapper un secret vers Telegram.
_EXFIL = [
    re.compile(r"sk-ant-[A-Za-z0-9_-]{10,}"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bsbp_[a-f0-9]{40}\b"),
    re.compile(r"\b\d{8,10}:[A-Za-z0-9_-]{35}\b"),  # telegram bot token
    re.compile(r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}"),  # JWT
]


def exfil_scan(text: str) -> str:
    """Remplace tout secret détecté par [REDACTED] avant envoi (jamais de fuite)."""
    out = text
    for pat in _EXFIL:
        out = pat.sub("[REDACTED]", out)
    return out


def send_telegram(token: str, chat_id: str, text: str) -> tuple[bool, str]:
    text = exfil_scan(text)  # garde exfiltration : rien ne part sans scan
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({"chat_id": chat_id, "text": text,
                                   "disable_web_page_preview": "true"}).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=data), timeout=10) as r:
            ok = json.loads(r.read()).get("ok", False)
            return ok, ("sent" if ok else "api returned ok=false")
    except Exception as e:  # noqa: BLE001 — one-way best-effort, never crash war mode
        return False, f"{type(e).__name__}: {e}"


def main() -> int:
    text = refresh_digest()
    # 1) env vars (Test Key Pragma durable) ; 2) fallback .minimax local agnostique
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat = os.environ.get("TELEGRAM_CHAT_ID")
    if not (token and chat):
        mt, mc = creds_from_minimax()
        token = token or mt
        chat = chat or mc
        if mt or mc:
            print(f"[telegram] creds .minimax : token={'OK' if mt else '--'} chat_id={'OK' if mc else '--'}")
    if token and chat:
        ok, msg = send_telegram(token, chat, text)
        print(f"[telegram] {'OK' if ok else 'FAILED'}: {msg}")
        return 0 if ok else 1
    # Pas câblé : outbox local + instructions (jamais de secret ici)
    OUTBOX.write_text(text, encoding="utf-8")
    print("[telegram] NON CÂBLÉ — digest écrit dans data/14_warmode_telegram_outbox.txt")
    print("Pour activer le push (Test Key Pragma, env User scope) :")
    print("  setx TELEGRAM_BOT_TOKEN <token>   (bot @BotFather)")
    print("  setx TELEGRAM_CHAT_ID <chat_id>   (écris 1× au bot, /api/getUpdates donne le chat_id)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
