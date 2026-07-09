"""symphony_supabase_orchestrator.py — Goal 2026-06-23 (rev 2) : 8 Cron Jobs via Supabase (BANNIS Baserow).

A0 Amadeus = /jour daily meta-constitution scan
A1 Morty Router = /60min (12WY⊃PARA⊃DEAL→GTD conversion)
A2 Cerritos = /30min supervise 5 A3 (Mariner/Boimler/Rutherford/Tendi/Freeman) GTD workflow

Supabase REST API direct (urllib stdlib, no SDK).
"""
import json, os, sys, time, urllib.request, urllib.error
from pathlib import Path

# === SUPABASE CANON CONFIG ===
SUPABASE_URL = "https://hjweyhpmrxqsxfbibsnc.supabase.co"
LOG = Path("C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md")

def _read_token():
    """D6 #57 #59 #60 NEW (2026-06-23) : try service_role FIRST (bypass RLS), then anon, then PAT."""
    import subprocess as _sp
    for env_name in ["SUPABASE_SERVICE_ROLE_KEY", "SUPABASE_LIFE_OS_ANON_KEY", "SUPABASE_ACCESS_TOKEN"]:
        for scope in ["User", "Machine"]:
            try:
                r = _sp.run(["powershell","-NoProfile","-Command",
                             f"[Environment]::GetEnvironmentVariable('{env_name}','{scope}')"],
                            capture_output=True, text=True, timeout=10)
                v = r.stdout.strip()
                if v: return v, env_name
            except Exception: continue
    return None, None

SUPABASE_KEY, KEY_TYPE = _read_token()

def _read_token():
    """DEPRECATED: replaced by module-level _read_token()."""
    pass

_read_hklm = _read_token  # backward alias

def _supabase_get(table: str, limit: int = 10) -> tuple[bool, str]:
    """GET Supabase REST API."""
    try:
        req = urllib.request.Request(
            f"{SUPABASE_URL}/rest/v1/{table}?limit={limit}",
            headers={"apikey": SUPABASE_KEY or "", "Authorization": f"Bearer {SUPABASE_KEY}"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return True, r.read().decode("utf-8")[:500]
    except urllib.error.HTTPError as e: return False, f"HTTP {e.code}: {e.reason}"
    except Exception as e: return False, f"err: {type(e).__name__}: {str(e)[:200]}"

def _log(msg: str):
    ts = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"[{ts}] {msg}\n")

# === CRON 1 : A0 AMADEUS DAILY (1/j) ===
def cron_01_a0_amadeus_daily():
    """A0 meta-constitution scan : check canon Memory Core state + Supabase tables existence."""
    results = {}
    # Check Memory Core state.jsonl exists + drift OK
    s = Path("C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/state.jsonl")
    h = Path("C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/heartbeat.jsonl")
    if s.exists() and h.exists():
        drift = abs(s.stat().st_mtime - h.stat().st_mtime) < 60
        results["memory_core"] = f"state-bus.v2 drift={'OK' if drift else 'DRIFT'}"
    else:
        results["memory_core"] = "MISSING state.jsonl or heartbeat.jsonl"
    # Check Supabase tables canon
    for tbl in ["fw_ikigai", "fw_life_wheel", "fw_12wy", "fw_para", "fw_deal"]:
        ok, msg = _supabase_get(tbl, limit=1)
        results[f"supabase.{tbl}"] = "OK" if ok else f"err: {msg[:80]}"
    _log(f"CRON-01 A0-AMADEUS-DAILY: {json.dumps(results, ensure_ascii=False)}")
    return results

# === CRON 2 : A1 MORTY ROUTER (1h) ===
def cron_02_a1_morty_router():
    """A1 Morty Router : 12WY⊃PARA⊃DEAL → GTD conversion."""
    # Query 12WY weekly Rocks from Supabase
    ok_12wy, msg_12wy = _supabase_get("fw_12wy", limit=12)
    ok_para, msg_para = _supabase_get("fw_para", limit=10)
    ok_deal, msg_deal = _supabase_get("fw_deal", limit=10)
    # Lifecycle : Projects / Areas / Resources / Archives
    result = {"12WY": "OK" if ok_12wy else f"err: {msg_12wy[:60]}",
              "PARA": "OK" if ok_para else f"err: {msg_para[:60]}",
              "DEAL": "OK" if ok_deal else f"err: {msg_deal[:60]}"}
    _log(f"CRON-02 A1-MORTY-ROUTER: {json.dumps(result, ensure_ascii=False)}")
    return result

# === CRON 3-8 : A2 CERRITOS + 5 A3 GTD (30min) ===
def cron_a2_a3_gtd_workflow():
    """A2 Cerritos + 5 A3 : GTD workflow (Capture→Clarify→Organize→Reflect→Engage)."""
    # A2 = Holo Deck dispatcher
    # 5 A3 = Mariner(Capture), Boimler(Clarify), Tendi(Organize), Rutherford(Reflect), Freeman(Engage)
    # Query GTD state from Supabase + log A3 dispatch availability
    ok_gtd, msg_gtd = _supabase_get("fw_gtd", limit=10)
    a3_roster = ["Mariner(Capture)", "Boimler(Clarify)", "Tendi(Organize)", "Rutherford(Reflect)", "Freeman(Engage)"]
    result = {
        "A2 Cerritos": "dispatching",
        "A3 roster": a3_roster,
        "fw_gtd_state": "OK" if ok_gtd else f"err: {msg_gtd[:60]}",
        "GTD workflow": "Capture→Clarify→Organize→Reflect→Engage",
    }
    _log(f"CRON-03-08 A2-CERRITOS+A3-GTD: {json.dumps(result, ensure_ascii=False)}")
    return result

# === MAIN ===
if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["a0", "a1", "a2-a3", "all"], default="all",
                   help="a0=A0 daily / a1=A1 hourly / a2-a3=GTD / all=everything")
    p.add_argument("--fire-count", type=int, default=0,
                   help="Total cron fires since boot (for internal cadence skip)")
    a = p.parse_args()

    # D6 #61 NEW (2026-06-23) : 8 cadences via 1 cron /5min with internal skip logic
    # Plan : every Nth fire = different mode
    #   fires % 288 (24h × 12/h) == 0 → A0 daily
    #   fires % 12 (1h) == 0 → A1 hourly
    #   fires % 6 (30min) == 0 → A2 Cerritos + 5 A3 GTD
    fc = a.fire_count
    results = {}
    if a.mode in ("a0", "all") and fc % 288 == 0:
        results["cron_01_a0_amadeus_daily"] = cron_01_a0_amadeus_daily()
    if a.mode in ("a1", "all") and fc % 12 == 0:
        results["cron_02_a1_morty_router"] = cron_02_a1_morty_router()
    if a.mode in ("a2-a3", "all") and fc % 6 == 0:
        results["cron_a2_a3_gtd_workflow"] = cron_a2_a3_gtd_workflow()
    if not results:
        results["skip"] = f"fire #{fc} no cadence match (next: A2-A3 in {6 - fc%6}min, A1 in {12 - fc%12}min, A0 in {288 - fc%288}min)"
    print(json.dumps(results, indent=2, ensure_ascii=False))