"""heartbeat_os.py — War Room heartbeat OS-level (24/7, sans session CC).

Remplace la limite du cron CC (7 jours, REPL-idle only) par une schtask Windows.
OBSERVATION ONLY : collector_14 (War Room) + spock_airlock (invariants Beth) + push Telegram.
Le heartbeat regarde, il n'agit pas — sauf l'airlock qui gère SES flags (mécanique ratifiée ADR-L1-WF-001).
"""
from __future__ import annotations

import subprocess
import sys
from datetime import datetime
from pathlib import Path

CITADEL = Path(__file__).resolve().parents[1]
STEPS = [
    CITADEL / "collectors" / "spock_airlock.py",      # 1. invariants d'abord (le digest les lit)
    CITADEL / "collectors" / "collector_14_warmode.py",  # 2. état War Room + digest (inclut ligne airlock)
    CITADEL / "cron" / "telegram_warmode_push.py",    # 3. push observabilité
]


def main() -> int:
    log = CITADEL / "logs" / "heartbeat_os.log"
    log.parent.mkdir(exist_ok=True)
    rc_total = 0
    lines = [f"--- heartbeat_os {datetime.now().astimezone().isoformat(timespec='seconds')} ---"]
    for step in STEPS:
        r = subprocess.run([sys.executable, str(step)], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=120)
        tail = (r.stdout or r.stderr or "").strip().splitlines()
        lines.append(f"[{step.name}] rc={r.returncode} :: {tail[-1] if tail else '(no output)'}")
        rc_total |= (r.returncode if r.returncode not in (0, 2) else 0)  # exit 2 = gate fermé, pas une erreur
    with log.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))
    return rc_total


if __name__ == "__main__":
    raise SystemExit(main())
