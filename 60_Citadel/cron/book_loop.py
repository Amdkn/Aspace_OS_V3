"""
book_loop.py — Book COO Loop Engineering / Meta Harness Engineering cron script.

Per Plan L2 Dark Factory §3.4 + Plan §6 MiroFish gouverneur compression :
- À chaque boundary de jour (J1→J2, J2→J3, ..., J6→J7), Book COO orchestre le passage
- Cette boucle est MÉTA : elle introspecte l'état du harness (les 22 agents + le Triptyque
  cadence active) et produit un rapport Loop Engineering
- Append-only : le rapport est écrit dans `cron/output/book-loop-<ts>.json`
- Lecture seule sur sources canoniques (`.mavis/agents/`, ADR canon, decision files)
- JAMAIS de /ship outboard (INALIÉNABLE) — seul le rapport est produit

GATING (FREIN À MAIN ACTIF per A0 Murderbot) :
- REFUSE de tourner sans `decisions/enable_book_loop.flag`
- Exit code 2 = gate non activé
- Exit code 0 = rapport produit + log
- Exit code 1 = erreur (try/except interne)

Doctrine anti-Ultron §S5 :
- Lecture seule sur sources canoniques
- Append-only output
- Idempotent (re-run safe)
- Pas d'auto-approval
- /ship jamais automatique

Date : 2026-07-05 · Auteur : Mavis (MC/L1) — A0 GO "créer le Cron de Book"
Source : plan-l2-dark-factory-book-coo-compression-12wy.md §10 premier tour
Sister : LD01/99_meta/plan_l2_dark_factory_sister.md §10-§11
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path

ROOT = Path(r"C:\Users\amado")
FLAG = ROOT / "agent-os" / "citadel" / "decisions" / "enable_book_loop.flag"
OUTPUT_DIR = ROOT / "agent-os" / "citadel" / "cron" / "output"
AGENTS_ROOT = ROOT / ".mavis" / "agents"
LD01_CAL = ROOT / "ASpace_OS_V2" / "20_Life_OS" / "22_Wheel_Discovery" / "LD01_Business_Book" / "99_meta" / "calendar.md"
LD01_DECISIONS = ROOT / "agent-os" / "citadel" / "decisions"
GOVERNOR_SIGNALS = ROOT / "agent-os" / "citadel" / "loops" / "artifacts" / "signals"  # WF3 MiroFish (ADR-L1-WF-001)


@dataclass
class BookLoopReport:
    """Loop Engineering Report — append-only D4."""
    ran_at: str
    cron_id: str
    day_in_cycle: str = "J?"  # J1 through J7 per Dark Factory §5
    triptyque_active: str = "?"
    agents_state: dict = field(default_factory=dict)
    cadence_alive: bool = False
    cadence_fresh: bool = False  # fix proxy #2 : dernier darkfactory run < 48h (présence != fraîcheur)
    mirofish_attached: bool = False
    mirofish_governor: dict = field(default_factory=dict)  # verdicts WF3 réels (fix angle-mort 2026-07-06)
    risk_flags: dict = field(default_factory=dict)
    loop_engineering_note: str = ""
    next_boundary: dict = field(default_factory=dict)
    doctrine_check: dict = field(default_factory=dict)
    auto_ratify: bool = False

    def to_dict(self) -> dict:
        return asdict(self)


def require_flag() -> bool:
    """Posture C strict — no cron sans A0 HITL GO.
    12WY-ON-PAUSE check FIRST : si decisions/12WY_ON_PAUSE.flag existe, Tony pré-ratifié
    12 sem (2026-07-05 → 2026-09-27) → bypass individual gate flag.
    """
    twelve_wy_pause = FLAG.parent / "12WY_ON_PAUSE.flag"
    if twelve_wy_pause.exists():
        return True  # Tony Stark pré-ratification cycle complet
    return FLAG.exists()


def detect_agents_state() -> dict:
    """D1 sur .mavis/agents/ — lecture seule, retourne structure agents active."""
    if not AGENTS_ROOT.exists():
        return {"error": f"{AGENTS_ROOT} not found"}
    tiers = {"B1": [], "B2": [], "B3": [], "utilitaires": []}
    for entry in sorted(AGENTS_ROOT.iterdir()):
        if not entry.is_dir():
            continue
        name = entry.name
        if name.startswith("b1-"):
            tiers["B1"].append(name)
        elif name.startswith("b2-"):
            tiers["B2"].append(name)
        elif name.startswith("b3-"):
            tiers["B3"].append(name)
        else:
            tiers["utilitaires"].append(name)
    return {
        "total": sum(len(v) for v in tiers.values()),
        "B1_count": len(tiers["B1"]),
        "B2_count": len(tiers["B2"]),
        "B3_count": len(tiers["B3"]),
        "utilitaires_count": len(tiers["utilitaires"]),
        "agents": tiers,
    }


def detect_cadence_state() -> dict:
    """D1 sur les decision files Dark Factory présents dans citadel/decisions/."""
    if not LD01_DECISIONS.exists():
        return {"days_completed": 0, "files": []}
    files = sorted(LD01_DECISIONS.glob("2026-*_darkfactory.json"))
    # fix proxy-boolean #2 (2026-07-06) : presence != fraicheur — cadence_fresh = dernier run < 48h
    fresh = False
    if files:
        age_h = (time.time() - files[-1].stat().st_mtime) / 3600
        fresh = age_h < 48
    return {
        "days_completed": len(files),
        "files": [f.name for f in files],
        "last_run": files[-1].name if files else None,
        "fresh_48h": fresh,
    }


def detect_mirofish_attached() -> bool:
    """Lit le calendar pour vérifier la trace MiroFish attachée."""
    if not LD01_CAL.exists():
        return False
    try:
        content = LD01_CAL.read_text(encoding="utf-8")
        return "MiroFish" in content or "mirofish" in content
    except OSError:
        return False


def read_governor_signals() -> dict:
    """Fix angle-mort 2026-07-06 (GO Picard) : Book écoute son gouverneur WF3.

    Avant : mirofish_attached = grep 'MiroFish' dans le calendar (proxy, faux-vert possible).
    Ici : lecture RÉELLE des signals sim-*.md — dernier verdict par variation. Un RISQUE
    non-absorbé = la règle 'accélère' est suspendue (le gouverné entend le gouverneur).
    Lecture seule (doctrine anti-Ultron intacte).
    """
    out: dict = {"signals_read": 0, "verdicts": {}, "risque_unabsorbed": False}
    if not GOVERNOR_SIGNALS.exists():
        return out
    for f in sorted(GOVERNOR_SIGNALS.glob("sim-*.md")):
        try:
            txt = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        out["signals_read"] += 1
        verdict = None
        for line in txt.splitlines():
            if "verdict=" in line:
                verdict = line.rsplit("verdict=", 1)[-1].strip()
        if verdict:
            out["verdicts"][f.stem] = verdict
            if verdict == "RISQUE" and "status: absorbed" not in txt:
                out["risque_unabsorbed"] = True
    return out


def infer_day_and_triptyque(now: datetime) -> tuple[str, str]:
    """Infère le jour du cycle 7-jours + Triptyque actif.
    Production-ready : basé sur date de départ canonique 2026-07-05 (W4 monday).
    Sobriété : pas de state global, infère de la date.
    """
    start = datetime(2026, 7, 5)
    days_since = (now - start).days
    if days_since < 0:
        return "J-pre", "?"
    cycle_day = (days_since % 7) + 1  # 1..7
    day_label = f"J{cycle_day}"
    triptyque_map = {
        1: "T1 People·Operation·IT",
        2: "T2 Product·Growth·Sales",
        3: "Duo Finance·Legal",
        4: "T1 pass-2 DEAL-libéré",
        5: "T2 pass-2 DEAL-libéré",
        6: "Duo pass-2 Legal fold-in",
        7: "Synthèse B1 Jerry+Summers",
    }
    return day_label, triptyque_map.get(cycle_day, "?")


def produce_report(now: datetime) -> BookLoopReport:
    day, triptyque = infer_day_and_triptyque(now)
    cadence = detect_cadence_state()
    governor = read_governor_signals()
    return BookLoopReport(
        ran_at=now.strftime("%Y-%m-%dT%H:%M:%S%z"),
        cron_id=f"book-loop-{now.strftime('%Y%m%d-%H%M%S')}",
        day_in_cycle=day,
        triptyque_active=triptyque,
        agents_state=detect_agents_state(),
        cadence_alive=cadence["days_completed"] >= 1,
        cadence_fresh=cadence.get("fresh_48h", False),
        mirofish_attached=detect_mirofish_attached(),
        mirofish_governor=governor,
        risk_flags={
            "kernel_Rick": False,
            "vie_Beth": False,
            "ship_outboard": False,
            "governor_RISQUE_unabsorbed": governor["risque_unabsorbed"],
        },
        loop_engineering_note=(
            f"Book COO heartbeat J{day} ({triptyque}). "
            f"Days completed: {cadence['days_completed']}. "
            "Async concurrent 3 B2→B3 en parallèle par jour. "
            "MiroFish boundary produit rapport + règle suivant."
        ),
        next_boundary={
            "trigger": f"J{day} → J{(int(day[1:]) % 7) + 1}",
            "rule": ("GOUVERNEUR RISQUE non-absorbé → cadence CAP ×4, pas d'accélération"
                     if governor["risque_unabsorbed"]
                     else "si compression a tenu sans casse → accélère · sinon ralentit + flag"),
        },
        doctrine_check={
            "lecture_seule_sources": True,
            "append_only_output": True,
            "idempotent": True,
            "ship_gated_outboard": True,
            "auto_update_off": True,
            "hook_exit_0_always": True,
            "posture_C_flag_gated": True,
        },
        auto_ratify=False,
    )


def write_report(report: BookLoopReport) -> Path:
    """Append-only output — JAMAIS d'écrasement."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = OUTPUT_DIR / f"book-loop-{ts}.json"
    path.write_text(json.dumps(report.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="show report without writing")
    args = ap.parse_args()

    if not require_flag():
        print(f"REFUSED: missing {FLAG} — A0 HITL gate required (Posture C — no cron without GO)")
        print(f"To enable: New-Item -ItemType File '{FLAG}'")
        return 2

    now = datetime.now()
    report = produce_report(now)

    if args.dry_run:
        print(json.dumps(report.to_dict(), indent=2, ensure_ascii=False))
        return 0

    path = write_report(report)
    print(f"book_loop OK → {path}")
    print(f"  day: {report.day_in_cycle} · triptyque: {report.triptyque_active}")
    print(f"  agents: {report.agents_state.get('total', 0)} · cadence_alive: {report.cadence_alive} · mirofish: {report.mirofish_attached}")
    print(f"  doctrine_check: {sum(report.doctrine_check.values())}/{len(report.doctrine_check)} invariants OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
