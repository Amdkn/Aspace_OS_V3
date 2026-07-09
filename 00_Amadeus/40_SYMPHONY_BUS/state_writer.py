#!/usr/bin/env python3
# state_writer.py — Helper Python : lock atomique + write JSON pour bus sémantique 40_SYMPHONY_BUS/
# D1 receipt 2026-06-21 : canon plan fancy-hugging-bengio §23.1 + §23.2
# Loi : mkdir(.state.lock) + tempfile + rename atomique + rmdir(.state.lock) en finally
# Garde-fou : si state.json > 10 KB → warning + rotation vers state.json.prev

import json
import os
import sys
import tempfile
import time
import shutil
from pathlib import Path
from datetime import datetime, timezone

BUS_DIR = Path(__file__).resolve().parent
STATE_JSON = BUS_DIR / "state.json"
STATE_PREV = BUS_DIR / "state.json.prev"
LOCK_DIR = BUS_DIR / ".state.lock"
SCHEMA_VERSION = "state-bus.v1"


def _acquire_lock(retries: int = 3, backoff_ms=(100, 300, 900)) -> bool:
    """Atomique : mkdir(.state.lock). Retry avec backoff exponentiel si collision."""
    for attempt in range(retries):
        try:
            LOCK_DIR.mkdir()
            return True
        except FileExistsError:
            wait = backoff_ms[min(attempt, len(backoff_ms) - 1)] / 1000.0
            time.sleep(wait)
    return False


def _release_lock() -> None:
    if LOCK_DIR.exists():
        try:
            LOCK_DIR.rmdir()
        except OSError:
            pass


def _now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def init_state() -> dict:
    """Crée un state.json vierge si absent. Idempotent."""
    STATE_JSON.parent.mkdir(parents=True, exist_ok=True)
    if not STATE_JSON.exists():
        blank = {
            "$schema": SCHEMA_VERSION,
            "status": "INIT",
            "created": _now_iso(),
            "updated": _now_iso(),
            "agent_id": "A0_Amadeus",
            "session_id": "fancy-hugging-bengio",
            "cycle": "Q3-2026",
            "week": "W1",
            "stage": "captured",
            "agent_path": "A1:Morty > A2:Cerritos > A3:Mariner",
            "para_bucket": None,
            "12wy_discipline": None,
            "life_wheel_domain": None,
            "raw_input_hash": None,
            "raw_input_preview": None,
            "next_step": "A3:Boimler",
            "tokens_used": 0,
            "tokens_budget": 15000,
            "drift_flag": False,
            "extra": {},
            "metadata": {},
        }
        STATE_JSON.write_text(json.dumps(blank, indent=2, ensure_ascii=False), encoding="utf-8")
    return json.loads(STATE_JSON.read_text(encoding="utf-8"))


def _sync_to_supabase(snapshot: dict) -> None:
    """U1 sink (U1-b ratified 2026-07-03) : push state → Supabase REST v1 idempotent upsert.

    Source canon: wiki/hand_offs/proposal_u1_supabase_symphony_state_2026-07-03.md
    section "Modification state_writer.py (1 fonction à ajouter)".
    Idempotent via session_id ON CONFLICT. Graceful no-op si env vars
    SUPABASE_URL / SUPABASE_SERVICE_KEY absents. Best-effort : ne raise jamais
    (l'écriture state.json locale est déjà persistée avant l'appel).
    """
    import urllib.request
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_SERVICE_KEY")
    if not (url and key):
        return  # graceful no-op si pas configuré (U1-c en attente)
    payload = {k: v for k, v in snapshot.items() if k not in ("$schema",)}
    req = urllib.request.Request(
        f"{url}/rest/v1/symphony_state?on_conflict=session_id",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "apikey": key,
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=2).read()
    except Exception as e:
        print(f"[symphony_bus] Supabase sync skipped: {e}", file=sys.stderr)


def write_state(updates: dict) -> dict:
    """Merge updates dans state.json. Lock atomique + tempfile + rename."""
    if not _acquire_lock():
        raise RuntimeError(f"Lock {LOCK_DIR} held after 3 retries — abort")

    try:
        if not STATE_JSON.exists():
            init_state()
        current = json.loads(STATE_JSON.read_text(encoding="utf-8"))
        current.update(updates)
        current["updated"] = _now_iso()
        current["$schema"] = SCHEMA_VERSION

        # Garde-fou taille : si > 10 KB, rotation prev
        serialized = json.dumps(current, indent=2, ensure_ascii=False)
        if len(serialized.encode("utf-8")) > 10_240:
            if STATE_JSON.exists():
                shutil.copy2(STATE_JSON, STATE_PREV)
            sys.stderr.write("[state_writer] WARN: state.json > 10KB, rotated to state.json.prev\n")

        # Écriture atomique : tempfile dans le même dir + rename
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=str(BUS_DIR), delete=False, suffix=".tmp"
        ) as tf:
            tf.write(serialized)
            tmp_name = tf.name
        os.replace(tmp_name, STATE_JSON)

        # U1 sink (D5 receipt) : append au sidecar NDJSON.
        _sync_to_supabase(current)
        return current
    finally:
        _release_lock()


def read_state() -> dict:
    """Lit state.json sans lock (read-only safe)."""
    if not STATE_JSON.exists():
        return init_state()
    return json.loads(STATE_JSON.read_text(encoding="utf-8"))


def main():
    if len(sys.argv) < 2:
        print("Usage: state_writer.py [--init | --read | --write KEY=VAL ...]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "--init":
        state = init_state()
        print(f"[state_writer] init OK : {STATE_JSON}")
        print(json.dumps(state, indent=2, ensure_ascii=False))
    elif cmd == "--read":
        state = read_state()
        print(json.dumps(state, indent=2, ensure_ascii=False))
    elif cmd == "--write":
        updates = {}
        for arg in sys.argv[2:]:
            if "=" in arg:
                k, v = arg.split("=", 1)
                updates[k] = v
        state = write_state(updates)
        print(f"[state_writer] write OK : {list(updates.keys())}")
        print(json.dumps(state, indent=2, ensure_ascii=False))
    else:
        print(f"[state_writer] unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
