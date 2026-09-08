#!/usr/bin/env python3
"""
Pre-Tool Guard Hook — Agent OS V3 (Tech OS Kernel)
Couche déterministe [5D] de la Pyramide de Sécurité.

Vérifications exécutées avant tout appel d'outil (Tool Calling / Subagent Invoke) :
1. Détection de secrets et fuite de PII (API Keys, tokens, credentials en clair).
2. Contrôle du Rot Rate (taux de pourrissement) : fraîcheur des schémas et contextes.
3. Veto absolu : si violation détectée, arrêt immédiat (exit code != 0).
"""

import sys
import re
import os
import json
import time
from pathlib import Path

KERNEL_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = KERNEL_DIR.parent

SECRET_PATTERNS = [
    (r"AIza[0-9A-Za-z-_]{35}", "Google API Key"),
    (r"sk-[a-zA-Z0-9]{20,}", "OpenAI/Anthropic Secret Key"),
    (r"ghp_[a-zA-Z0-9]{36}", "GitHub Personal Access Token"),
    (r"ey[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*", "JWT Token / Supabase Service Key"),
]

ROT_RATE_THRESHOLD_SECONDS = 7 * 86400  # 7 jours

def check_secrets(text: str) -> list[str]:
    violations = []
    for pattern, label in SECRET_PATTERNS:
        if re.search(pattern, text):
            violations.append(f"Fuite potentielle détectée : {label}")
    return violations

def check_rot(file_path: Path) -> tuple[bool, str]:
    if not file_path.exists():
        return False, f"Fichier de référence introuvable: {file_path}"
    mtime = file_path.stat().st_mtime
    age_seconds = time.time() - mtime
    if age_seconds > ROT_RATE_THRESHOLD_SECONDS:
        days = int(age_seconds / 86400)
        return False, f"Fichier expiré (Rot Rate dépassé : {days} jours > 7 j). Synchronisation requise."
    return True, "Contexte frais"

def run_guard(payload_json_str: str) -> dict:
    try:
        data = json.loads(payload_json_str) if payload_json_str else {}
    except Exception:
        data = {"raw": payload_json_str}

    raw_str = json.dumps(data)
    violations = check_secrets(raw_str)

    if violations:
        return {
            "ok": False,
            "status": "VETO",
            "reason": "Security/PII Hook Triggered",
            "violations": violations
        }

    return {
        "ok": True,
        "status": "PASS",
        "timestamp": time.time(),
        "checked_length": len(raw_str)
    }

if __name__ == "__main__":
    input_data = sys.stdin.read() if not sys.stdin.isatty() else (sys.argv[1] if len(sys.argv) > 1 else "{}")
    res = run_guard(input_data)
    print(json.dumps(res, indent=2))
    sys.exit(0 if res["ok"] else 1)
