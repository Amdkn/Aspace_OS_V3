"""symphony_pilot_runtime.py — Phase 2 Runtime dispatcher (≤80 lignes, stdlib only).

Doctrine: ADR-META-001 D1-D8 + ADR-SOBER-002 KISS. Pas de pip install requis.
Fix 2026-06-23 : state-bus.v2 JSONL append-only (D4 respect) + heartbeat.jsonl sibling cross-check.
"""
import json, os, subprocess, sys, time, urllib.request, urllib.error
from pathlib import Path

P = "79df867c-06b5-4e61-b3f1-68aa886c39a3"
API = "https://api.plane.so/api/v1"
WS = "aspace-core"
S = Path("C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/state.jsonl")  # Fix 1: JSONL append-only
H = Path("C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/heartbeat.jsonl")  # Fix 3: sibling cross-check
L = Path("C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md")
TICK = [0]  # Fix 1: monotonic tick counter (in-memory, atomic increment)
# D6 #7 NEW fix (2026-06-23) : routing matrix hardcoded on sequence_id 1-12 (12 items Q3 2026 Rocks)
# mais Plane Today state contient sequence_id 21-28 (parent Rock + Day 1-7 sub-issues Tactics).
# Refactor: match_a3_route() pattern matching on issue TITLE (D3 nuance : 12 items Q3 canon = Rocks,
# 8 issues Plane = Tactics journalières Day 1-7 + parent Rock).
def match_a3_route(issue):
    title = issue.get("name", "")
    seq = issue.get("seq", 0)
    # Parent Rock canonique (sequence_id 21) → A1 Beth + A2 Discovery + A3 Tilly (B1 governance)
    if seq == 21: return ("Beth", "Discovery", "Tilly")
    # Day 1 (06/22 Lun) — A0 brief sign-off + Plane setup → A1 Morty + A2 Cerritos + A3 Tendi (B1 setup)
    if "Day 1" in title and ("brief" in title or "Plane setup" in title): return ("Morty", "Cerritos", "Tendi")
    # Day 2 (06/23 Mar) — A1 Beth audit MCP drift + SOBER-002 → A1 Beth + A2 Discovery + A3 Tilly (B1 audit)
    if "Day 2" in title or "A1 Beth audit" in title: return ("Beth", "Discovery", "Tilly")
    # Day 3 (06/24 Mer) — A3 Protostar DEAL Define+Eliminate → A1 Beth + A2 Protostar + A3 Rok-Tahk (B1 DEAL)
    if "Day 3" in title or "DEAL" in title: return ("Beth", "Protostar", "Rok-Tahk")
    # Day 4 (06/25 Jeu) — A3 Protostar Zero SPEC skill /symphony-pilot → A1 Beth + A2 Protostar + A3 Zero (B1 Automate)
    if "Day 4" in title or "Zero SPEC" in title: return ("Beth", "Protostar", "Zero")
    # Day 5 (06/26 Ven) — A3 Chapel measures D11 + /routine design → A1 Morty + A2 Curie-SNW + A3 Chapel (B1 Measure)
    if "Day 5" in title or "Chapel" in title: return ("Morty", "Curie-SNW", "Chapel")
    # Day 6 (06/27 Sam) — Synthèse A0 + Décision Phase B GO/NO-GO → A1 Beth + A2 Discovery + A3 Tilly (B1 milestone)
    if "Day 6" in title or "Synthèse A0" in title: return ("Beth", "Discovery", "Tilly")
    # Day 7 (06/28 Dim) — REST + Retro + Seed W+1 → A1 Beth + A2 Cerritos + A3 Rutherford (B1 review)
    if "Day 7" in title or "REST" in title or "Seed W+1" in title: return ("Beth", "Cerritos", "Rutherford")
    # W1-W9 Rocks cycle Q3 2026 (sequence_id 8-19) → fallback A1 Morty + A2 Curie-SNW + A3 Una (B1 12WY)
    if 8 <= seq <= 19: return ("Morty", "Curie-SNW", "Una")
    # Default fallback : A3 Boimler triage (Cerritos clarify)
    return ("Morty", "Cerritos", "Boimler")

def _read_user_env(name):
    """D6 #15 + #36 NEW fix : Git Bash subprocess ne voit PAS env vars User scope Windows.
    Fallback = PowerShell ABSOLUTE PATH (C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe)
    pour éviter PATH minimal SYSTEM = FileNotFoundError silencieux.
    PowerShell `[Environment]::GetEnvironmentVariable` lit aussi HKCU\\Volatile Environment
    que winreg direct ne voit pas."""
    try:
        import subprocess as _sp
        _ps = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
        r = _sp.run([_ps, "-NoProfile", "-Command",
                     f"[Environment]::GetEnvironmentVariable('{name}','User')"],
                    capture_output=True, text=True, timeout=15)
        v = (r.stdout or "").strip()
        return v if v and "Exception" not in v else None
    except Exception: return None

def hdr():
    # D6 #6 + #15 fix (2026-06-23) : env var via os.environ puis fallback registry User scope
    t = (os.environ.get("PLANE_API_KEY") or os.environ.get("PLANE_API_TOKEN")
         or _read_user_env("PLANE_API_KEY") or _read_user_env("PLANE_API_TOKEN"))
    if not t: raise SystemExit("FATAL PLANE_API_KEY introuvable (os.environ + registry User scope)" )
    # D6 #21 NEW fix (2026-06-23) : Plane API rejette (403) sans User-Agent
    return {"X-API-Key": t, "Content-Type": "application/json", "User-Agent": "SymphonyPilot/1.0"}

def poll():
    # D6 fix 2026-06-23 : Plane self-hosted ignore ?state__name=X filter (retourne TOUS les 160 issues).
    # D1 receipt : state__name=Today / state=Today / state__group=backlog / no filter = tous 160.
    # Fix : query states endpoint, cache Today UUID, use ?state=<UUID> filter.
    today_id = _today_state_id()
    if today_id:
        url = f"{API}/workspaces/{WS}/projects/{P}/issues/?state={today_id}&limit=50"
    else:
        # Fallback graceful : si state discovery fail, retourne [] (vs 160 inutile)
        return []
    req = urllib.request.Request(url, headers=hdr())
    with urllib.request.urlopen(req, timeout=30) as r:
        return [{"id":i["id"],"seq":i.get("sequence_id",0),"title":i.get("name","")} for i in json.loads(r.read()).get("results",[])]

_TODAY_STATE_CACHE = {"id": None, "ts": 0}
def _today_state_id():
    """Discover Today state UUID via /states/ endpoint. Cache 5min (D6 avoid re-query)."""
    now = time.time()
    if _TODAY_STATE_CACHE["id"] and (now - _TODAY_STATE_CACHE["ts"]) < 300:
        return _TODAY_STATE_CACHE["id"]
    try:
        req = urllib.request.Request(f"{API}/workspaces/{WS}/projects/{P}/states/", headers=hdr())
        with urllib.request.urlopen(req, timeout=15) as r:
            states = json.loads(r.read())
            if isinstance(states, dict): states = states.get("results", states)
            for s in (states or []):
                if s.get("name") == "Today":
                    _TODAY_STATE_CACHE["id"] = s["id"]
                    _TODAY_STATE_CACHE["ts"] = now
                    return s["id"]
    except Exception as e:
        print(f"[poll] Today state discovery failed: {e}", file=sys.stderr)
    return None

def _a3_system_prompt(a3: str) -> str:
    """D6 #44 NEW (2026-06-23) : A3 role → system_prompt canonique (H1/H3/H10/H30/H90)."""
    table = {
        "a3-discovery-tilly": "Tu es A3 Tilly (H30 Cognition twin). Audite learning/focus/knowledge. /goal: auditer 30j cognition. /loop toutes les 5 min. /compact si window > 80%.",
        "a3-discovery-culber": "Tu es A3 Culber (H10 Health twin). /goal: pulse santé. /loop weekly.",
        "a3-discovery-saru": "Tu es A3 Saru (H3 Finance twin). /goal: runway check.",
        "a3-discovery-stamets": "Tu es A3 Stamets (H30 Social twin). /goal: network pulse.",
        "a3-discovery-burnham": "Tu es A3 Burnham (H10 Family twin). /goal: family check.",
        "a3-discovery-reno": "Tu es A3 Reno (H10 Creativity twin). /goal: creative pulse.",
        "a3-discovery-georgiou": "Tu es A3 Georgiou (H90 Impact twin). /goal: legacy audit.",
        "a3-discovery-book": "Tu es A3 Book (H1 Business twin). /goal: P&L weekly.",
        "a3-protostar-dal": "Tu es A3 Dal (Define). /goal: define pattern.",
        "a3-protostar-rok-tahk": "Tu es A3 Rok-Tahk (Eliminate). /goal: kill waste.",
        "a3-protostar-zero": "Tu es A3 Zero (Automate). /goal: create automation.",
        "a3-protostar-gwyn": "Tu es A3 Gwyn (Liberate). /goal: measure bandwidth saved.",
        "a3-cerritos-mariner": "Tu es A3 Mariner (Capture). /goal: inbox triage.",
        "a3-cerritos-boimler": "Tu es A3 Boimler (Clarify). /goal: triage actionability.",
        "a3-cerritos-freeman": "Tu es A3 Freeman (Engage). /goal: pick next action.",
        "a3-cerritos-tendi": "Tu es A3 Tendi (Organize). /goal: PARA placement.",
        "a3-cerritos-rutherford": "Tu es A3 Rutherford (Reflect). /goal: weekly review.",
    }
    return table.get(a3, f"Tu es A3 twin {a3}. /goal: execute intention. /loop iteratif. /compact si nécessaire.")

def spawn(a3: str, prompt: str, to: int = 1800) -> tuple:
    """D6 #44 NEW (2026-06-23) : claude-code-sdk async query (A3 role → system_prompt).
    Remplace subprocess.run(claude.cmd) par async SDK natif (D8 cross-agent).
    Le sub-agent a /goal specifique + peut utiliser /loop /compact dans sa session.
    to=1800s = 30 min (per A0 vision: Sub Agents travaillent 30 min avec /goal /loop /compact)."""
    import asyncio as _aio
    try:
        import claude_code_sdk as _cc
        _tok = _read_user_env("ANTHROPIC_API_KEY") or ""
        opts = _cc.ClaudeCodeOptions(
            model="claude-sonnet-4-20250514",
            max_turns=20,  # permet /loop interne 20 itérations (~30 min wall)
            system_prompt=_a3_system_prompt(a3),
            env={
                "ANTHROPIC_BASE_URL": "https://api.minimax.io",
                "ANTHROPIC_API_KEY": _tok,
                "ANTHROPIC_AUTH_TOKEN": _tok,
            },
        )
        async def _run():
            text_parts = []
            async for msg in _cc.query(prompt=prompt, options=opts):
                t = type(msg).__name__
                if t == "AssistantMessage":
                    for blk in getattr(msg, "content", []) or []:
                        if hasattr(blk, "text"):
                            text_parts.append(blk.text)
                elif t == "ResultMessage":
                    if getattr(msg, "is_error", False):
                        return False, "\n".join(text_parts)[:500], f"result_error: {getattr(msg,'result','')}"[:200]
            return True, "\n".join(text_parts)[:500], ""
        ok, out, err = _aio.run(_aio.wait_for(_run(), timeout=to))
        return ok, out, err
    except _aio.TimeoutError: return False, "", f"timeout after {to}s (30min budget exhausted)"
    except Exception as e: return False, "", f"spawn_err: {type(e).__name__}: {str(e)[:200]}"

def write_state(cycle,week,stage,path,drift,nxt):
    """Fix 1 : JSONL append-only au lieu de OVERWRITE (D4 no-self-contradiction)."""
    S.parent.mkdir(parents=True,exist_ok=True)
    TICK[0]+=1
    entry = {"schema":"state-bus.v2","tick":TICK[0],"cycle":cycle,"week":week,"stage":stage,"agent_path":path,"drift_flag":drift,"next_step":nxt,"ts":int(time.time()),"ts_iso":time.strftime('%Y-%m-%dT%H:%M:%S%z')}
    with S.open("a",encoding="utf-8") as f: f.write(json.dumps(entry,ensure_ascii=False)+"\n")
    # Fix 3 : heartbeat.jsonl sibling cross-check
    with H.open("a",encoding="utf-8") as f: f.write(json.dumps({"tick":TICK[0],"ts":entry["ts_iso"],"stage":stage,"drift":drift},ensure_ascii=False)+"\n")

def log(line):
    """Fix 2 : timestamp ISO 8601 unique par tick."""
    L.parent.mkdir(parents=True,exist_ok=True)
    with L.open("a",encoding="utf-8") as f: f.write(f"[{time.strftime('%Y-%m-%dT%H:%M:%S%z')}] {line}\n")

# D6 #41 NEW (2026-06-23) : Owner E-myth state UUIDs Plane canoniques
OWNER_STATES = {
    "today":        "078e6b89-c6b0-4e68-af90-301e07713382",
    "in_progress":  "10e14185-c407-4b40-9a4e-8a10d47f7e24",
    "done":         "0d5ea751-afba-4310-beb5-19187f1ca824",
    "backlog":      "11b6d790-0e89-41bf-9b05-7059286b89c1",
}

def _plane_req(method: str, path: str, body=None) -> tuple[bool, str]:
    """D6 #41 NEW : urllib.request PATCH/POST Plane API (D8 cross-agent compat)."""
    try:
        data = json.dumps(body).encode("utf-8") if body else None
        req = urllib.request.Request(f"{API}{path}", data=data, method=method, headers=hdr())
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status in (200, 201), f"HTTP {r.status}"
    except urllib.error.HTTPError as e: return False, f"HTTP {e.code}: {e.reason}"
    except Exception as e: return False, f"err: {type(e).__name__}: {str(e)[:200]}"

def patch_state(issue_id: str, state_uuid: str) -> tuple[bool, str]:
    """D6 #41 NEW : PATCH Plane issue state (Today→In Progress→Done)."""
    return _plane_req("PATCH", f"/workspaces/{WS}/projects/{P}/issues/{issue_id}/", {"state": state_uuid})

def create_sub_issue(parent_id: str, name: str, desc: str, state_uuid: str) -> tuple[bool, str]:
    """D6 #41 NEW : POST Plane sub-issue (parent field link)."""
    body = {"name": name[:250], "description": desc[:1000], "state": state_uuid, "parent": parent_id}
    ok, msg = _plane_req("POST", f"/workspaces/{WS}/projects/{P}/issues/", body)
    return ok, msg

def tick(dry=False,cycle="Q3-2026",week="W2",owner_mode=False):
    s={"polled":0,"dispatched":0,"skipped":0,"drift":False,"tick":TICK[0],"owner_mode":owner_mode}
    log(f"═══ TICK #{TICK[0]+1} @ {time.strftime('%Y-%m-%dT%H:%M:%S%z')} ═══ cycle={cycle} week={week} dry={dry} owner={owner_mode}")
    try: issues=poll()
    except Exception as e: log(f"Pilot FAIL poll: {e}"); s["drift"]=True; write_state(cycle,week,"poll_fail","",True,"manual_investigate"); return s
    s["polled"]=len(issues)
    # D6 #41 NEW (2026-06-23) : Owner mode = ONLY process parent issue (seq=21), skip others (anti-spam)
    if owner_mode:
        issues = [i for i in issues if i["seq"] == 21]
        if not issues:
            log("OWNER mode: no parent seq=21 found in Today state, nothing to do")
            log(f"═══ TICK #{TICK[0]} DONE ═══ polled={s['polled']} dispatched=0 skipped=0 owner_no_parent drift=False")
            return s
    for i in issues:
        r=match_a3_route(i)
        if not r: s["skipped"]+=1; log(f"#{i['seq']} NO_ROUTE_MATCH → skipped"); continue
        a1,a2,a3=r; path=f"A1:{a1} > A2:{a2} > A3:{a3}"
        if dry: s["dispatched"]+=1; log(f"[DRY] #{i['seq']} → {path}"); write_state(cycle,week,"dry_routed",path,False,"await_next_tick"); continue
        ok,out,err = spawn(a3, f"A3 twin `{a3}` intention={i['title']} livrable=state.jsonl append")
        stage = "routed_for_dispatch" if ok == "skipped" else ("executed" if ok else "drift")
        if ok == "skipped":
            s["dispatched"]+=1  # routed = OK pour le runtime orchestrateur
            log(f"#{i['seq']} {path} → {stage} | next: Claude Code Agent tool picks up")
        else:
            s["dispatched"]+=int(ok)
            if not ok: s["drift"]=True
            if err: log(f"#{i['seq']} {path} → {stage} | stderr: {err}")
            else: log(f"#{i['seq']} {path} → {stage}")
        # D6 #41 NEW : Owner mode → PATCH state + POST sub-issues (1er parent uniquement, anti-spam)
        if owner_mode and i["seq"] == 21:  # limiter au Rock canonique parent (seq=21)
            ok_patch, msg_patch = patch_state(i["id"], OWNER_STATES["in_progress"])
            log(f"OWNER PATCH parent {i['id'][:8]}→InProgress: {msg_patch}")
            for tier_label, tier_name in [("A1_decision", a1), ("A2_dispatch", a2), ("A3_execute", a3)]:
                ok_sub, msg_sub = create_sub_issue(
                    i["id"],
                    f"[{tier_label}] {tier_name}: {i['title'][:80]}",
                    f"Tier {tier_label} pour parent #{i['seq']} (route {path}). A3 stdout: {(out or '')[:200]}",
                    OWNER_STATES["backlog"]
                )
                log(f"OWNER POST sub-issue {tier_label}: {msg_sub}")
            # Si spawn OK, PATCH parent vers Done
            if ok == "skipped" or ok:
                ok_done, msg_done = patch_state(i["id"], OWNER_STATES["done"])
                log(f"OWNER PATCH parent {i['id'][:8]}→Done: {msg_done}")
        write_state(cycle,week,stage,path,not ok,"spawn_retry" if not ok else "await_next_tick")
    log(f"═══ TICK #{TICK[0]} DONE ═══ polled={s['polled']} dispatched={s['dispatched']} skipped={s['skipped']} drift={s['drift']}")
    return s

if __name__=="__main__":
    import argparse; p=argparse.ArgumentParser()
    p.add_argument("--dry-run",action="store_true"); p.add_argument("--once",action="store_true")
    p.add_argument("--poll-interval",type=int,default=1800); p.add_argument("--cycle",default="Q3-2026"); p.add_argument("--week",default="W2")
    # D6 #41 NEW (2026-06-23) : Owner mode = PATCH state + POST sub-issues (anti-observateur passif)
    p.add_argument("--owner-mode",action="store_true")
    # D6 #23 NEW fix (2026-06-23) : accept A0 canonical args (--poll-plane, --a0-go, --state-bus-version, --wiki-log-append) — ignore unknown
    a, _unknown = p.parse_known_args()
    # D6 #28 NEW fix (2026-06-23) : try/except englobant → crash silencieux SYSTEM/HIGHEST subprocess
    # D6 #34 NEW fix (2026-06-23) : except BaseException (incl SystemExit from hdr() raise) au lieu de Exception
    def _safe_tick(label):
        try: return tick(a.dry_run,a.cycle,a.week,a.owner_mode)
        except BaseException as e:
            ts = time.strftime('%Y-%m-%dT%H:%M:%S%z')
            err_line = f"[{ts}] ═══ TICK #{label} CRASH ═══ type={type(e).__name__} msg={str(e)[:300]}"
            try:
                with L.open("a",encoding="utf-8") as f: f.write(err_line+"\n")
                with S.open("a",encoding="utf-8") as f: f.write(json.dumps({"schema":"state-bus.v2","tick":-1,"stage":"tick_crash","drift_flag":True,"error":str(e)[:300],"ts_iso":ts})+"\n")
                with H.open("a",encoding="utf-8") as f: f.write(json.dumps({"tick":-1,"stage":"tick_crash","drift":True,"ts":ts})+"\n")
            except Exception: pass
            print(err_line,file=sys.stderr)
            if isinstance(e, KeyboardInterrupt): raise
            return {"polled":0,"dispatched":0,"skipped":0,"drift":True,"tick":-1,"crash":str(e)[:300]}
    if a.once:
        print(json.dumps(_safe_tick("once"),indent=2)); sys.exit(0)
    n=0
    while True:
        n+=1
        print(json.dumps(_safe_tick(n),indent=2))
        time.sleep(a.poll_interval)