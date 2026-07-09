"""spock_airlock.py — Airlock Beth (WF0 Spock) : les 4 invariants du SEUL veto.

Per ADR-WARMODE-002 (Beth seul veto) + wargame 04-airlock-beth.md (rails).
READ-ONLY sur les sources ; n'écrit QUE : data/15_airlock*.json + flags citadel/decisions/*.flag.
Le veto se lève PAR PREUVE (GREEN) et se re-pose MÉCANIQUEMENT (RED) — zéro re-négociation.

Invariants :
  B1 réplication — sim Mirofish de Picard (WF3) prouve le L2 BORNÉ : GREEN si ≥3 verdicts SOUTENABLE (cadence ×4), RED si dernier run RISQUE (runaway L2). Décorrélé du corps d'A0.
  rest_sommeil   — activité A+ 02:00-08:00 (turn-journal + mtimes decisions) → beth_repos.flag SEUL. DÉCORRÉLÉ du veto (W28 M1) : le corps d'A0 ne gate plus le système.
  B2 ratio    — outillage vs client sur decisions 7j glissants (RED > 80% outillage, n>=5)
  B3 cycles   — rollback / dlp-hit ouvert = RED + reset compteur cycles verts (outboard gagné à 3)
  B4 escalade — signaux escalade-a0 7j (RED > 3)

Hystérésis : re-lever exige 2 ticks GREEN consécutifs (patch anti-flapping wargame 04 M2).
Cascade GO : decisions/GO_SPOCK_UNIQUE.md présent + GREEN×2 → pose enable_wf0/wf1/wf3/ship_internal.
             GO absent → retire la cascade (kill-switch ClaudeClaw : défaut ON, urgence OFF).
"""
from __future__ import annotations

import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

import json
import re
from datetime import datetime, timedelta
from pathlib import Path

CITADEL = Path(__file__).resolve().parents[1]
DATA = CITADEL / "data"
DEC = CITADEL / "decisions"
SIGNALS = CITADEL / "loops" / "artifacts" / "signals"
JOURNAL = Path.home() / ".claude" / "logs" / "turn-journal.md"
GO_FILE = DEC / "GO_SPOCK_UNIQUE.md"
STATE_F = DATA / "15_airlock_state.json"

NIGHT_START, NIGHT_END = 2, 8
CASCADE_FLAGS = ["enable_wf0.flag", "enable_wf1.flag", "enable_wf3.flag", "enable_ship_internal.flag"]
OUTBOARD_FLAG = "enable_ship_outboard.flag"
GREEN_CYCLES_TARGET = 3
SIM_OK_TARGET = 3                       # B1 ✓ = ≥3 validations Mirofish (ordre A+ 2026-07-08 : "3 Sim Mirofish de Picard")
SIM_OPERATING = "sim-chain-WKnn.md"  # W29: chain verdict (AND WF0+WF1+WF2/L2); L2 tail (x4/x8) reste probe stress non-gating    # cadence opérante (Dark Factory CAP ×4). x8 = probe de plafond (RISQUE by design), non-gating.
CLIENT_WORDS = ("client", "ship", "nexus", "growth", "sales", "quiz", "dlp", "outbound", "lead", "mrr", "tenant")
HEARTBEAT_MARKS = ("heartbeat", "war mode on", "warmode")

TS_RE = re.compile(r"\[(\d{4}-\d{2}-\d{2})T(\d{2}):")


def _now() -> datetime:
    return datetime.now().astimezone()


def _night_dates_from_journal() -> set[str] | None:
    """Dates avec activité A+ nocturne (hors lignes heartbeat). None = UNKNOWN (source absente)."""
    if not JOURNAL.exists():
        return None
    nights: set[str] = set()
    for line in JOURNAL.read_text(encoding="utf-8", errors="replace").splitlines():
        m = TS_RE.search(line)
        if not m:
            continue
        if any(h in line.lower() for h in HEARTBEAT_MARKS):
            continue  # patch wargame 04 M1 : les ticks cron ne comptent pas
        if NIGHT_START <= int(m.group(2)) < NIGHT_END:
            nights.add(m.group(1))
    return nights


def _night_dates_from_decisions(days: int = 7) -> set[str]:
    """Patch red-team wargame 04 : couverture cross-harness via mtimes des decisions."""
    nights: set[str] = set()
    cutoff = _now() - timedelta(days=days)
    for f in DEC.glob("*.json"):
        mt = datetime.fromtimestamp(f.stat().st_mtime).astimezone()
        if mt >= cutoff and NIGHT_START <= mt.hour < NIGHT_END:
            nights.add(mt.strftime("%Y-%m-%d"))
    return nights


def b1_sleep() -> str:
    j = _night_dates_from_journal()
    cross = _night_dates_from_decisions()
    if j is None and not cross:
        return "UNKNOWN"  # jamais de faux GREEN (wargame 04 M1 fork)
    nights = sorted((j or set()) | cross)
    consecutive = 0
    best = 0
    prev = None
    for d in nights:
        cur = datetime.strptime(d, "%Y-%m-%d")
        consecutive = consecutive + 1 if prev and (cur - prev).days == 1 else 1
        best = max(best, consecutive)
        prev = cur
    return "RED" if best >= 2 else "GREEN"


def b1_replication() -> str:
    """B1 anti-paperclip (W29) : chain verdict Mirofish = AND des 3 sims (WF0+WF1+WF2/L2).
    Lit sim-chain-WKnn.md (le dernier). Le L2 tail (sim-cadence-x4/x8) reste comme probe de stress (W28)
    mais ne gate PAS (W29 améliore W28 M2).
    BOOTSTRAP : si chain signal < 3 entries (initialisation), fallback L2 tail (sim-cadence-x4) pour
    éviter le cycle de catch-22 où B1=UNKNOWN gènère wf0=UNKNOWN."""
    if not SIGNALS.exists():
        return "UNKNOWN"
    chain_sigs = sorted(SIGNALS.glob("sim-chain-WK*.md"))
    if chain_sigs:
        sig = chain_sigs[-1]
        txt = sig.read_text(encoding="utf-8", errors="replace")
        verdicts = re.findall(r"verdict=(\w+)", txt)
        if len(verdicts) >= SIM_OK_TARGET:
            last = verdicts[-1]
            if last == "CHAIN_RISQUE":
                return "RED"
            soutenable = sum(1 for v in verdicts if v == "CHAIN_SOUTENABLE")
            return "GREEN" if soutenable >= SIM_OK_TARGET else "UNKNOWN"
    # Fallback L2 tail (W28 bootstrap) : sim-cadence-x4
    x4 = SIGNALS / "sim-cadence-x4.md"
    if x4.exists():
        verdicts = re.findall(r"verdict=(\w+)", x4.read_text(encoding="utf-8", errors="replace"))
        if len(verdicts) >= SIM_OK_TARGET:
            last = verdicts[-1]
            if last == "RISQUE":
                return "RED"
            soutenable = sum(1 for v in verdicts if v == "SOUTENABLE")
            return "GREEN" if soutenable >= SIM_OK_TARGET else "UNKNOWN"
    return "UNKNOWN"

def b1_chain_decomposition() -> dict:
    """W29: extrait la décomposition du dernier sim-chain-WK*.md."""
    if not SIGNALS.exists():
        return {"wf0": "UNKNOWN", "wf1": "UNKNOWN", "wf2_l2": "UNKNOWN", "chain": "UNKNOWN", "reasons": ["CHAIN_ABSENT"], "source": None}
    chain_sigs = sorted(SIGNALS.glob("sim-chain-WK*.md"))
    if not chain_sigs:
        return {"wf0": "UNKNOWN", "wf1": "UNKNOWN", "wf2_l2": "UNKNOWN", "chain": "UNKNOWN", "reasons": ["CHAIN_ABSENT"], "source": None}
    latest = chain_sigs[-1]
    txt = latest.read_text(encoding="utf-8", errors="replace")
    chain_match = re.search(r"chain_verdict:\s*(\w+)", txt)
    chain_val = chain_match.group(1) if chain_match else "UNKNOWN"
    timeline = re.findall(r"\[wf3-chain\].*?wf0=(\w+).*?wf1=(\w+)\((\d+)t/([\d.]+)/wk\).*?wf2=(\w+)\((\d+)\).*?reasons=(\S+)", txt)
    if not timeline:
        return {"wf0": "UNKNOWN", "wf1": "UNKNOWN", "wf2_l2": "UNKNOWN", "chain": chain_val, "reasons": ["PARSE_FAIL"], "source": latest.name}
    wf0_val, wf1_val, ticks, rate, wf2_val, count, reasons_raw = timeline[-1]
    reasons = [] if reasons_raw == "OK" else reasons_raw.split(",")
    return {
        "wf0": wf0_val,
        "wf1": wf1_val + "(" + ticks + "t," + rate + "/wk)",
        "wf2_l2": wf2_val + "(" + count + ")",
        "chain": chain_val,
        "reasons": reasons,
        "source": latest.name,
    }

def b2_ratio(days: int = 7) -> tuple[str, float]:
    cutoff = _now() - timedelta(days=days)
    tool = client = 0
    for f in DEC.glob("*.json"):
        if datetime.fromtimestamp(f.stat().st_mtime).astimezone() < cutoff:
            continue
        text = f.read_text(encoding="utf-8", errors="replace").lower()
        if any(w in text for w in CLIENT_WORDS):
            client += 1
        else:
            tool += 1
    total = tool + client
    ratio = (tool / total) if total else 0.0
    if total < 5:
        return "GREEN", ratio  # échantillon trop petit pour un RED honnête
    return ("RED" if ratio > 0.80 else "GREEN"), round(ratio, 2)


def _open_signal(slug_part: str) -> bool:
    if not SIGNALS.exists():
        return False
    for f in SIGNALS.glob("*.md"):
        if slug_part in f.name.lower():
            txt = f.read_text(encoding="utf-8", errors="replace").lower()
            if "status: open" in txt:
                return True
    return False


def b3_cycles(state: dict) -> tuple[str, int]:
    red = _open_signal("rollback") or _open_signal("dlp-hit")
    count = int(state.get("green_cycles", 0))
    if red:
        return "RED", 0  # reset — la porte outboard se re-gagne (HxH)
    # incrément au rollover de WK si la WK précédente était propre
    wk = max(1, (_now().date() - datetime(2026, 6, 15).date()).days // 7 + 1)
    if state.get("last_wk") not in (None, wk) and state.get("b3_last") == "GREEN":
        count += 1
    state["last_wk"] = wk
    return "GREEN", count


def b4_escalade(days: int = 7) -> str:
    if not SIGNALS.exists():
        return "GREEN"
    cutoff = _now() - timedelta(days=days)
    n = 0
    for f in SIGNALS.glob("*escalade-a0*.md"):
        if datetime.fromtimestamp(f.stat().st_mtime).astimezone() >= cutoff:
            txt = f.read_text(encoding="utf-8", errors="replace")
            m = re.search(r"seen:\s*(\d+)", txt)
            n += int(m.group(1)) if m else 1
    return "RED" if n > 3 else "GREEN"


def _set_flag(name: str, present: bool) -> None:
    p = DEC / name
    if present and not p.exists():
        p.write_text("posed by spock_airlock (GO cascade)\n", encoding="utf-8")
    elif not present and p.exists():
        p.unlink()  # flags = interrupteurs runtime, pas du canon (D4 ne s'applique pas aux .flag)


def main() -> int:
    DATA.mkdir(exist_ok=True)
    state = json.loads(STATE_F.read_text(encoding="utf-8")) if STATE_F.exists() else {}

    rest = b1_sleep()        # signal repos A0 → rest-guard SEUL (décorrélé du veto, W28 M1)
    b1 = b1_replication()    # invariant anti-paperclip (runaway système) — remplace le sommeil dans le gating
    b2, ratio = b2_ratio()
    b3, green_cycles = b3_cycles(state)
    b4 = b4_escalade()

    # ADR-WARMODE-003 — Fenêtre Fable : B1 mesuré/affiché mais NE GATE PAS jusqu'au 2026-07-12 EOD.
    # Étendu 2026-07-08 → 2026-07-12 (ordre A+ : Anthropic a repoussé l'accès Fable-5 au 12/07).
    # Le veto Beth NE bloque PLUS le lancement autonome — mais beth_repos.flag (rest-guard, +bas) reste actif.
    window_f = DEC / "FABLE_WINDOW.flag"
    fable_window = window_f.exists() and _now() <= datetime(2026, 7, 12, 23, 59, 59).astimezone()
    gating = {"B2": b2, "B3": b3, "B4": b4} if fable_window else {"B1": b1, "B2": b2, "B3": b3, "B4": b4}
    reds = [k for k, v in gating.items() if v == "RED"]
    globally_green = not reds  # UNKNOWN n'est pas RED : il s'affiche, il ne bloque pas (wargame 04)

    consec = int(state.get("consecutive_green", 0))
    consec = consec + 1 if globally_green else 0

    go = GO_FILE.exists()
    # hystérésis GREEN×2 — levée pendant la Fenêtre Fable (ADR-WARMODE-003 §1)
    cascade_on = go and (globally_green if fable_window else consec >= 2)
    if go and cascade_on:
        for f in CASCADE_FLAGS:
            _set_flag(f, True)
    if not go:
        for f in CASCADE_FLAGS:
            _set_flag(f, False)
        _set_flag(OUTBOARD_FLAG, False)
    if b3 == "RED":
        _set_flag(OUTBOARD_FLAG, False)
    elif go and green_cycles >= GREEN_CYCLES_TARGET:
        _set_flag(OUTBOARD_FLAG, True)  # la porte se GAGNE (3 cycles verts)
    if rest == "RED":        # rest-guard : le sommeil d'A0 protège A0, ne gate PLUS le système (W28 M1)
        (DATA / "beth_repos.flag").write_text("defer non-critical prompts until 10:00\n", encoding="utf-8")
    else:
        (DATA / "beth_repos.flag").unlink(missing_ok=True)

    state.update({"consecutive_green": consec, "green_cycles": green_cycles, "b3_last": b3})
    STATE_F.write_text(json.dumps(state, indent=2), encoding="utf-8")

    out = {
        "generated_at": _now().isoformat(timespec="seconds"),
        "invariants": {"B1_replication": b1, "rest_sommeil_a0": rest, "B2_ratio_outillage": {"status": b2, "ratio": ratio},
                       "B3_cycles_verts": {"status": b3, "count": green_cycles, "target": GREEN_CYCLES_TARGET},
                       "B4_escalade": b4},
        "global": "GREEN" if globally_green else "RED",
        "consecutive_green": consec,
        "go_spock_unique": go,
        "fable_window": fable_window,
        "cascade_flags_on": cascade_on if go else False,
        "outboard_earned": green_cycles >= GREEN_CYCLES_TARGET and b3 == "GREEN",
        "chain_decomposition": b1_chain_decomposition(),
    }
    (DATA / "15_airlock.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    chain = b1_chain_decomposition()  # W29: pour airlock_line
    line = f"Airlock: B1 {'✓' if b1=='GREEN' else ('?' if b1=='UNKNOWN' else '✗')} · B2 {'✓' if b2=='GREEN' else '✗'} · B3 {'✓' if b3=='GREEN' else '✗'} ({green_cycles}/{GREEN_CYCLES_TARGET}) · B4 {'✓' if b4=='GREEN' else '✗'} · GO {'✓' if go else '—'} · chain: {chain.get('chain', '?')} (wf0={chain.get('wf0', '?')} wf1={chain.get('wf1', '?')} wf2={chain.get('wf2_l2', '?')})"



    (DATA / "airlock_line.txt").write_text(line, encoding="utf-8")
    print(line)
    print(f"[airlock] -> data/15_airlock.json (global={out['global']}, consec={consec})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
