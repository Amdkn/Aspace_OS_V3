"""wf3_sim_runner.py — MiroFish Predictive Swarm (WF3, SIMULATION seulement).

Per contrat loops/domains/wf3-mirofish/README.md + wargame kit (SUCCESS-ASPACE).
GATE : decisions/enable_wf3.flag (posé UNIQUEMENT par la cascade GO_SPOCK_UNIQUE) — exit 2 sinon.

Simulateur DÉTERMINISTE (pas de LLM, pas de prophétie) : modélise un cycle 12WY compressé
sous les soupapes du wargame 02 M3 (saturation, compaction, WIP limit) et produit des
signals `sim-*.md` avec prédiction + CONDITIONS D'INVALIDATION. WF2 les consomme comme
hypothèses (tag sim), jamais comme faits (D1). Sandbox : simspace/ isolé, nettoyé après run.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

CITADEL = Path(__file__).resolve().parents[1]
DEC = CITADEL / "decisions"
SIGNALS = CITADEL / "loops" / "artifacts" / "signals"
SIMSPACE = CITADEL / "cron" / "simspace"
WORKLOG = CITADEL / "loops" / "logs" / "worklog.md"
DATA = CITADEL / "data"  # W29: needed by run_chain

VARIATIONS = [
    # compression xN = N semaines de charge pliées en 1 ; la capacité NE scale PAS (bornée agents/tokens)
    {"slug": "cadence-x4", "compression": 4, "wip_limit": 20, "arrivals_per_wk": 12, "capacity_per_wk": 60},
    {"slug": "cadence-x8", "compression": 8, "wip_limit": 20, "arrivals_per_wk": 12, "capacity_per_wk": 60},
]


def _now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def gate() -> bool:
    return (DEC / "enable_wf3.flag").exists()


def simulate(v: dict) -> dict:
    """13 WK compressées : arrivées vs capacité sous soupapes (wargame 02 M3)."""
    queue = 0
    done = 0
    saturations = 0
    conservation_ticks = 0
    ticks_per_wk = 7  # ticks-jours réels
    cap_per_tick = v["capacity_per_wk"] / ticks_per_wk          # capacité bornée (ne scale pas)
    arr_per_tick = v["arrivals_per_wk"] * v["compression"] / ticks_per_wk  # la compression EST la charge
    for wk in range(1, 14):
        for _ in range(ticks_per_wk):
            queue += arr_per_tick
            # soupape (a) : saturation si la charge du tick dépasse 1.5x la capacité
            effective_cap = cap_per_tick
            if queue > v["wip_limit"]:
                # soupape (c) : stop intake, drain d'abord
                saturations += 1
                effective_cap = cap_per_tick * 1.0  # drain sans intake
                queue -= min(queue, effective_cap)
                done += min(queue + effective_cap, effective_cap)
                continue
            if arr_per_tick > cap_per_tick * 1.5:
                conservation_ticks += 1
                effective_cap = cap_per_tick / 2  # mode conservation : fréquence /2
            work = min(queue, effective_cap)
            queue -= work
            done += work
    return {
        "done": round(done, 1), "queue_residuelle": round(queue, 1),
        "saturations_wip": saturations, "ticks_conservation": conservation_ticks,
        "deal_wk13_atteignable": queue < v["wip_limit"] / 2,
    }


def write_signal(v: dict, r: dict) -> Path:
    SIGNALS.mkdir(parents=True, exist_ok=True)
    p = SIGNALS / f"sim-{v['slug']}.md"
    verdict = "SOUTENABLE" if r["deal_wk13_atteignable"] and r["saturations_wip"] < 10 else "RISQUE"
    entry = (f"- [{_now()}] [wf3-mirofish] run déterministe : done={r['done']} · queue_fin={r['queue_residuelle']} · "
             f"saturations={r['saturations_wip']} · conservation={r['ticks_conservation']} · verdict={verdict}\n")
    if p.exists():
        txt = p.read_text(encoding="utf-8")
        p.write_text(txt + entry, encoding="utf-8")  # append-only, seen implicite = count timeline
    else:
        p.write_text(f"""---
type: signal
status: open
tag: sim
sources: [cron/wf3_sim_runner.py]
seen: 1
---
# sim-{v['slug']} — prédiction MiroFish (SIMULATION, pas un fait)

Hypothèse : cycle 12WY compressé ×{v['compression']} (arrivées {v['arrivals_per_wk']}/WK, capacité {v['capacity_per_wk']}/WK, WIP {v['wip_limit']}).
Prédiction : {'DEAL WK13 atteignable' if r['deal_wk13_atteignable'] else 'DEAL WK13 COMPROMIS'} — verdict {verdict}.

**Conditions d'invalidation (forks à triggers, pas prophétie)** :
- SI les arrivées réelles > {v['arrivals_per_wk']}/WK observées 2 WK → re-simuler, prédiction caduque.
- SI un tick réel dure > 2× le budget → la compression ×{v['compression']} est fausse en pratique.
- SI saturations réelles/WK > simulées → adopter la variation inférieure.

## Timeline
{entry}""", encoding="utf-8")
    return p


def run_variations() -> int:
    if not gate():
        print("[wf3] GATE: decisions/enable_wf3.flag absent (posé par cascade GO_SPOCK_UNIQUE) — exit 2")
        return 2
    SIMSPACE.mkdir(exist_ok=True)
    produced = []
    for v in VARIATIONS:
        ws = SIMSPACE / f"sim-{v['slug']}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        ws.mkdir(parents=True)  # sandbox isolé (une sim n'écrit QUE ici + son signal)
        r = simulate(v)
        (ws / "result.json").write_text(json.dumps({"variation": v, "result": r}, indent=2), encoding="utf-8")
        sig = write_signal(v, r)
        produced.append(sig.name)
        shutil.rmtree(ws)  # nettoyage (le signal est la sortie, le worktree est jetable)
    WORKLOG.parent.mkdir(parents=True, exist_ok=True)
    with WORKLOG.open("a", encoding="utf-8") as f:
        f.write(f"- [{_now()}] [wf3-mirofish] {len(produced)} sims déterministes → {', '.join(produced)} (simspace nettoyé)\n")
    print(f"[wf3] {len(produced)} signals produits : {', '.join(produced)}")
    return 0



# === W29 — Chain sim (composition WF0 + WF1 + WF2/L2) ===
# Append-only : W20 sim, W28 L2 tail, W13 lock TOUS préservés.
# Singleton lock cron/wf3.lock (W13 M1) + run_id dedupe (W13 M2).
# Chaque paramêtre porte receipt: ou assumed: (W20 M1).

import hashlib, os, sys, time
from datetime import timedelta

LOCK = CITADEL / "cron" / "wf3.lock"  # W13 M1 singleton
SIM_OK_TARGET = 3
DASH = chr(0x2014); DOT = chr(0xB7); PM = chr(0xB1); RARR = chr(0x2192); TIMES = chr(0xD7); LDQ = chr(0x201C); RDQ = chr(0x201D)  # B1 validé à 3 validations chain (W29)

def _run_id() -> str:
    iso = datetime.now().astimezone().isoformat(timespec="seconds")
    h = hashlib.sha1(os.urandom(8)).hexdigest()[:6]
    return f"{iso}-{h}"

def _acquire_lock(stale_sec: int = 3600) -> str | None:
    """Atomic lock per W13 M1."""
    if LOCK.exists():
        age = time.time() - LOCK.stat().st_mtime
        if age < stale_sec: return None
        LOCK.unlink()
    rid = _run_id()
    LOCK.write_text(rid + "\n", encoding="utf-8")
    return rid

def _release_lock() -> None:
    if LOCK.exists(): LOCK.unlink()

def sim_wf0(state: dict) -> dict:
    """WF0 = state machine (spock_airlock). Pure fonction sur airlock state.
    receipt: D1 15_airlock.json 2026-07-08. assumed: shape stable 7j."""
    inv = state.get("invariants", {}) if isinstance(state, dict) else {}
    b1 = inv.get("B1_replication", "UNKNOWN")
    b2 = inv.get("B2_ratio_outillage", {}).get("status", "UNKNOWN")
    b3 = inv.get("B3_cycles_verts", {}).get("status", "UNKNOWN")
    b4 = inv.get("B4_escalade", "UNKNOWN")
    cascade = state.get("cascade_flags_on", False)
    reasons = []
    if b1 == "RED": reasons.append("wf0.B1_RED")
    if b2 == "RED": reasons.append("wf0.B2_RED")
    if b3 == "RED": reasons.append("wf0.B3_RED")
    if b4 == "RED": reasons.append("wf0.B4_RED")
    if not cascade: reasons.append("wf0.CASCADE_OFF")
    # Fable window (jusqu au 2026-07-12): UNKNOWN accepte comme ok (anti catch-22 bootstrap B1<->chain).
    # Apres la fenetre: UNKNOWN = RED (gating strict).
    fable_open = state.get("fable_window", False) and datetime.now() <= datetime(2026, 7, 12, 23, 59, 59)
    def _val_ok(v): return v == "GREEN" or (fable_open and v == "UNKNOWN")
    ok = (_val_ok(b1) and _val_ok(b2) and _val_ok(b3) and _val_ok(b4) and cascade)
    if ok: value = "GREEN"
    elif any(r.endswith("_RED") or r=="wf0.CASCADE_OFF" for r in reasons): value = "RED"
    else: value = "UNKNOWN"
    return {"value": value, "ok": ok, "reasons": reasons}

def sim_wf1(worklog_path, days: int = 7) -> dict:
    """WF1 = Morty runner schedule. Pure fonction sur worklog [wf1-morty].
    receipt: worklog.md [wf1-morty] 9 lignes 2026-07-08. assumed: 7j fenétre."""
    if not worklog_path.exists():
        return {"ok": False, "reasons": ["wf1.WORKLOG_ABSENT"], "rate_per_wk": 0.0, "ticks": 0}
    cutoff = datetime.now().astimezone() - timedelta(days=days)
    ts_re = re.compile(r"\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:Z|[+-]\d{2}:?\d{2}))")
    ticks = 0
    for line in worklog_path.read_text(encoding="utf-8", errors="replace").splitlines():
        if "[wf1-morty]" not in line: continue
        m = ts_re.search(line)
        if not m: continue
        try: ts = datetime.fromisoformat(m.group(1))
        except ValueError: continue
        if ts >= cutoff: ticks += 1
    rate_per_day = ticks / days
    rate_per_wk = rate_per_day * 7
    threshold = 1.0
    reasons = []
    ok = rate_per_wk >= threshold
    if not ok: reasons.append(f"wf1.RATE_LOW({rate_per_wk:.2f}/wk<{threshold})")
    return {"ok": ok, "reasons": reasons, "rate_per_wk": rate_per_wk, "ticks": ticks}

def sim_wf2_l2() -> dict:
    """WF2/L2 = Book bench queue. Lit sim-cadence-x4.md tail (W28 L2 stress probe).
    receipt: W28 sim-cadence-x4.md L2 tail (8 SOUTENABLE 2026-07-08). assumed: seuil 3 SOUTENABLE."""
    sig = SIGNALS / "sim-cadence-x4.md"
    if not sig.exists():
        return {"ok": False, "reasons": ["wf2.SIG_ABSENT"], "verdict": "UNKNOWN", "soutenable_count": 0}
    txt = sig.read_text(encoding="utf-8", errors="replace")
    verdicts = re.findall(r"verdict=(\w+)", txt)
    if not verdicts:
        return {"ok": False, "reasons": ["wf2.NO_VERDICT"], "verdict": "UNKNOWN", "soutenable_count": 0}
    last = verdicts[-1]
    soutenable_count = sum(1 for v in verdicts if v == "SOUTENABLE")
    reasons = []
    ok = (last == "SOUTENABLE") and (soutenable_count >= SIM_OK_TARGET)
    if last != "SOUTENABLE": reasons.append(f"wf2.LAST_{last}")
    if soutenable_count < SIM_OK_TARGET: reasons.append(f"wf2.COUNT_LOW({soutenable_count}/{SIM_OK_TARGET})")
    return {"ok": ok, "reasons": reasons, "verdict": last, "soutenable_count": soutenable_count}

def chain_verdict(wf0, wf1, wf2) -> dict:
    """W29 : AND des 3 sims. CHAIN_SOUTENABLE si tous ok=True. UNSTABLE interdit (W20)."""
    reasons = []
    reasons.extend(wf0.get("reasons", []))
    reasons.extend(wf1.get("reasons", []))
    reasons.extend(wf2.get("reasons", []))
    if wf0["ok"] and wf1["ok"] and wf2["ok"]:
        return {"value": "CHAIN_SOUTENABLE", "ok": True, "reasons": reasons}
    has_red = any("RED" in r or "LOW" in r or "ABSENT" in r for r in reasons)
    if has_red: return {"value": "CHAIN_RISQUE", "ok": False, "reasons": reasons}
    return {"value": "CHAIN_UNKNOWN", "ok": False, "reasons": reasons}

def _wk_number() -> int:
    base = datetime(2026, 7, 5).date()
    return max(1, (datetime.now().astimezone().date() - base).days // 7 + 1)

def write_chain_signal(wk, chain, wf0, wf1, wf2, run_id):
    SIGNALS.mkdir(parents=True, exist_ok=True)
    p = SIGNALS / f"sim-chain-WK{wk:02d}.md"
    now = _now()
    entry = (f"- [{now}] [wf3-chain] rid={run_id} verdict={chain['value']} {DOT} " + 
             f"wf0={wf0['value']} {DOT} wf1={'OK' if wf1['ok'] else 'LOW'}({wf1['ticks']}t/{wf1['rate_per_wk']:.2f}/wk) {DOT} " + 
             f"wf2={wf2['verdict']}({wf2.get('soutenable_count', 0)}) {DOT} reasons={','.join(chain['reasons']) or 'OK'}\n")
    if p.exists():
        txt = p.read_text(encoding="utf-8")
        p.write_text(txt + entry, encoding="utf-8")
    else:
        p.write_text(f"""---
type: signal
status: open
tag: sim-chain
sources: [cron/wf3_sim_runner.py]
seen: 1
wk: {wk}
chain_verdict: {chain['value']}
run_id: {run_id}
---
# sim-chain-WK{wk:02d} — chain verdict MiroFish (W29)

Composition (3 sims, AND) :
- WF0 (state machine) = **{wf0['value']}** — receipt: 15_airlock.json
- WF1 (schedule) = **{'OK' if wf1['ok'] else 'LOW'}** ({wf1['ticks']}t, {wf1['rate_per_wk']:.2f}/wk) — receipt: worklog.md
- WF2/L2 (queue) = **{wf2['verdict']}** ({wf2.get('soutenable_count', 0)}) "— receipt: sim-cadence-x4.md (W28 L2 stress probe)

**Chain verdict : {chain['value']}**
Reasons : {', '.join(chain['reasons']) or 'aucune'}

## Timeline
{entry}""", encoding="utf-8")
    return p

def run_chain() -> int:
    """W29 entry : produit signals/sim-chain-WKnn.md (1/WK, append-only)."""
    if not gate():
        print("[wf3-chain] GATE: decisions/enable_wf3.flag absent — exit 2")
        return 2
    rid = _acquire_lock()
    if rid is None:
        print("[wf3-chain] LOCK held (W13 M1) — exit 3")
        return 3
    try:
        airlock_path = DATA / "15_airlock.json"
        airlock_state = {}
        if airlock_path.exists():
            airlock_state = json.loads(airlock_path.read_text(encoding="utf-8"))
        wf0 = sim_wf0(airlock_state)
        wf1 = sim_wf1(WORKLOG)
        wf2 = sim_wf2_l2()
        chain = chain_verdict(wf0, wf1, wf2)
        wk = _wk_number()
        sig = write_chain_signal(wk, chain, wf0, wf1, wf2, rid)
        WORKLOG.parent.mkdir(parents=True, exist_ok=True)
        with WORKLOG.open("a", encoding="utf-8") as f:
            f.write(f"- [{_now()}] [wf3-chain] rid={rid} verdict={chain['value']} {RARR} {sig.name} (wf0={wf0['value']}, wf1={'OK' if wf1['ok'] else 'LOW'}({wf1['ticks']}t), wf2={wf2['verdict']})\n")
        print(f"[wf3-chain] rid={rid} verdict={chain['value']} {RARR} {sig.name}")
        print(f"  wf0={wf0['value']} | wf1={'OK' if wf1['ok'] else 'LOW'}({wf1['ticks']}t/{wf1['rate_per_wk']:.2f}/wk) | wf2={wf2['verdict']}({wf2['soutenable_count']})")
        if chain["reasons"]: print(f"  reasons: {', '.join(chain['reasons'])}")
        return 0
    finally:
        _release_lock()


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "chain":
        return run_chain()
    return run_variations()


if __name__ == "__main__":
    raise SystemExit(main())
