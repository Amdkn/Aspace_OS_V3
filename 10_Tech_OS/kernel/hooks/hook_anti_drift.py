#!/usr/bin/env python3
"""
Hook Anti-Derive (Anti-Drift & Sovereign Focus Guard) - Agent OS V3
Couche [5D] Validation Gates & Regles Transversales.

Objectifs stricts :
1. Bannir formellement toute fuite en passivite (F6) : formules generiques d'attente.
2. Bannir formellement les bascules de refus generiques en anglais.
3. Imposer le francais strict et l'interdiction du decrochage de Life OS.
"""

import sys
import re
import json

FORBIDDEN_PASSIVE_PATTERNS = [
    r"(?i)\bj'attends\s+(?:vos|tes)\s+(?:ordres|instructions|directives)\b",
    r"(?i)\bque\s+puis-je\s+(?:faire|t'aider)\s+pour\s+vous\b",
    r"(?i)\bcomment\s+puis-je\s+vous\s+aider\s+aujourd'hui\b",
    r"(?i)\bi\s+(?:cannot|must\s+decline|am\s+unable\s+to)\b",
    r"(?i)\bas\s+an\s+ai\b",
    r"(?i)\bi\s+apologize\s+for\s+any\s+confusion\b",
]

def check_text_drift(text: str) -> dict:
    violations = []
    for pattern in FORBIDDEN_PASSIVE_PATTERNS:
        if re.search(pattern, text):
            violations.append(f"Violation detectee: {pattern}")
    return {
        "ok": len(violations) == 0,
        "violations": violations
    }

if __name__ == "__main__":
    content = sys.stdin.read() if not sys.stdin.isatty() else (sys.argv[1] if len(sys.argv) > 1 else "")
    result = check_text_drift(content)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    sys.exit(0 if result["ok"] else 1)
