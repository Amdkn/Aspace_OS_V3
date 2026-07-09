#!/usr/bin/env python
# =============================================================================
# Symphony × Agent OS — UI Server (Grafana-lite) on http://127.0.0.1:8080
# =============================================================================
# Serves:
#   GET  /                       → dashboard (ui/index.html)
#   GET  /static/<file>          → CSS/JS from ui/
#   GET  /api/snapshot           → JSON: running/retrying/donna/cost summary
#   GET  /api/pulse?last=N       → last N lines of pulse.log (parsed JSONL)
#   GET  /api/standards          → list of standards with descriptions
#   GET  /api/standards/<name>   → raw .md content of a standard
#   GET  /api/cost               → aggregated cost per phase
#   GET  /api/phase-stats        → duration per phase (bar chart data)
#   POST /api/tick               → trigger demo tick (re-run symphony-tick-demo.sh)
# =============================================================================

import http.server
import json
import os
import socketserver
import subprocess
import sys
import time
import urllib.parse
from collections import defaultdict
from pathlib import Path

# --- Paths --------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
SYMPHONY_ROOT = SCRIPT_DIR.parent
UI_DIR = SCRIPT_DIR / "ui"
AGENT_OS_DIR = SYMPHONY_ROOT / "agent-os"
PULSE_LOG = AGENT_OS_DIR / "pulse.log"
INDEX_FILE = AGENT_OS_DIR / "standards" / "index.yml"
DEMO_TICK_SH = SCRIPT_DIR / "symphony-tick-demo.sh"
DEMO_TICK_PS1 = SCRIPT_DIR / "symphony-tick-demo.ps1"
PYTHON = r"C:\Python314\python.exe"

# --- Phase metadata ------------------------------------------------------------
PHASE_COLORS = {
    "WAKE":    "#6b7280",
    "PROBE":   "#3b82f6",
    "DECIDE":  "#06b6d4",
    "EXECUTE": "#10b981",
    "OBSERVE": "#f59e0b",
    "LEARN":   "#8b5cf6",
    "SIGNAL":  "#f97316",
    "SLEEP":   "#475569",
}
PHASE_ORDER = ["WAKE", "PROBE", "DECIDE", "EXECUTE", "OBSERVE", "LEARN", "SIGNAL", "SLEEP"]

# --- Helpers -------------------------------------------------------------------
def read_pulse_lines():
    """Read all JSONL lines from pulse.log, skip blanks, parse, return list."""
    if not PULSE_LOG.exists():
        return []
    out = []
    for line in PULSE_LOG.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out

# --- Intelligence (ADR-SYMPH-003 D2/D4 enforcement) -----------------------------
EXPECTED_STANDARDS_PER_PHASE = {
    "PROBE":   ["candidate-record-rule.md"],
    "DECIDE":  ["mission-contract.md", "soa-routing.md", "sla-triple.md", "tick-handoff.md"],
    "EXECUTE": ["mission-contract.md", "gate-decisions.md", "forbidden-words.md", "expected-proof.md", "writeback-policy.md"],
    "OBSERVE": ["forbidden-words.md", "gate-decisions.md", "sla-triple.md"],
    "SIGNAL":  ["writeback-policy.md", "expected-proof.md"],
}
DECISION_PHASES = ["PROBE", "DECIDE", "EXECUTE", "OBSERVE", "SIGNAL"]
SLA_WARN_AVG_DURATION_MS = 1500  # flag if a phase avg > 1.5s (heuristic)

def intelligence_report():
    """Analyse pulse.log against ADR-SYMPH-003 D2 (per-phase standards minimum) and D4 (cost guard).

    Returns a dict with: violations, drift, trends, suggestions.
    """
    lines = read_pulse_lines()
    if not lines:
        return {
            "violations": [],
            "drift": {"used": [], "unused": [], "total_standards": 0},
            "trends": {"ticks_analyzed": 0, "avg_cost_usd": 0.0, "avg_total_duration_ms": 0},
            "suggestions": [{"level": "info", "text": "No ticks yet. Click ▶ Trigger tick to start."}],
        }

    # Group by tick_id, ordered
    by_tick = defaultdict(list)
    for ln in lines:
        by_tick[ln.get("tick_id", "unknown")].append(ln)
    tick_ids = list(by_tick.keys())
    last_tick_id = tick_ids[-1]
    last_tick = by_tick[last_tick_id]

    # === D2 violations: decision phase with 0 standards ===
    violations = []
    for phase in DECISION_PHASES:
        expected = EXPECTED_STANDARDS_PER_PHASE.get(phase, [])
        phase_lines = [ln for ln in last_tick if ln.get("phase") == phase]
        if not phase_lines:
            violations.append({
                "level": "warn",
                "type": "D2_missing_phase",
                "phase": phase,
                "expected": expected,
                "got": [],
                "message": f"D2 violation: {phase} phase absent from last tick (expected ≥1 line)",
            })
            continue
        injected = set()
        for ln in phase_lines:
            for s in ln.get("standards_injected", []) or []:
                injected.add(s)
        if not injected and phase != "PROBE":
            # PROBE may have 0 (criterion list is implicit), but the others shouldn't
            violations.append({
                "level": "warn",
                "type": "D2_no_standards",
                "phase": phase,
                "expected": expected,
                "got": [],
                "message": f"D2 violation: {phase} has 0 standards injected (expected ≥1 of {expected})",
            })
        else:
            # Check at least one expected standard is present
            missing = [e for e in expected if e not in injected]
            if missing and phase in ("DECIDE", "EXECUTE"):
                violations.append({
                    "level": "info",
                    "type": "D2_partial_coverage",
                    "phase": phase,
                    "expected": expected,
                    "got": sorted(injected),
                    "message": f"D2 partial: {phase} missing expected standards: {missing}",
                })

    # === Drift: which standards exist but not used in last tick? ===
    all_standards = set()
    for std in standards_list():
        all_standards.add(f"{std['name']}.md")
    used_in_last = set()
    for ln in last_tick:
        for s in ln.get("standards_injected", []) or []:
            used_in_last.add(s)
    unused = sorted(all_standards - used_in_last)

    # === Trends: avg cost + duration across all ticks ===
    costs = []
    durations = []
    for tid in tick_ids:
        for ln in by_tick[tid]:
            if ln.get("cumulative_cost_usd") is not None and ln.get("phase") == "SLEEP":
                costs.append(ln["cumulative_cost_usd"])
            if ln.get("phase") == "SLEEP" and ln.get("decision"):
                # SLEEP line has the total in its decision
                import re as _re
                m = _re.search(r"total_duration_ms=(\d+)", ln.get("decision", ""))
                if m:
                    durations.append(int(m.group(1)))
    avg_cost = round(sum(costs) / len(costs), 4) if costs else 0.0
    avg_duration = int(sum(durations) / len(durations)) if durations else 0
    last_cost = costs[-1] if costs else 0.0
    last_duration = durations[-1] if durations else 0

    cost_trend = "stable"
    if len(costs) >= 2:
        if last_cost > avg_cost * 1.2:
            cost_trend = "up"
        elif last_cost < avg_cost * 0.8:
            cost_trend = "down"
    dur_trend = "stable"
    if len(durations) >= 2:
        if last_duration > avg_duration * 1.2:
            dur_trend = "up"
        elif last_duration < avg_duration * 0.8:
            dur_trend = "down"

    # === Per-phase average duration across all ticks ===
    per_phase_avg = defaultdict(list)
    for ln in lines:
        if ln.get("duration_ms") and ln.get("phase"):
            per_phase_avg[ln["phase"]].append(ln["duration_ms"])
    per_phase_stats = {}
    for p, ds in per_phase_avg.items():
        avg = sum(ds) / len(ds)
        per_phase_stats[p] = {
            "avg": round(avg, 1),
            "count": len(ds),
            "warn": avg > SLA_WARN_AVG_DURATION_MS,
        }

    # === Suggestions (human-readable, prioritized) ===
    suggestions = []
    critical = [v for v in violations if v["level"] == "warn"]
    info = [v for v in violations if v["level"] == "info"]
    if critical:
        suggestions.append({
            "level": "warn",
            "text": f"⚠ {len(critical)} D2 violation(s) in last tick — see Standards Coverage",
        })
    if unused:
        suggestions.append({
            "level": "info",
            "text": f"📚 {len(unused)} standard(s) exist but not used in last tick: {', '.join(unused[:3])}{'…' if len(unused) > 3 else ''}",
        })
    if cost_trend == "up":
        suggestions.append({
            "level": "warn",
            "text": f"💰 Cost trending up (${last_cost:.4f} > ${avg_cost:.4f} avg) — check EXECUTE phase",
        })
    if dur_trend == "up":
        suggestions.append({
            "level": "warn",
            "text": f"⏱ Duration trending up ({last_duration}ms > {avg_duration}ms avg)",
        })
    slow_phases = [p for p, s in per_phase_stats.items() if s["warn"]]
    if slow_phases:
        suggestions.append({
            "level": "info",
            "text": f"🐢 Slow phases: {', '.join(slow_phases)} (avg > {SLA_WARN_AVG_DURATION_MS}ms)",
        })
    if not suggestions:
        suggestions.append({
            "level": "ok",
            "text": "✅ All clear — last tick compliant with ADR-SYMPH-003 D2/D4",
        })
    # Sort: warn first
    suggestions.sort(key=lambda s: {"warn": 0, "info": 1, "ok": 2}.get(s["level"], 3))

    return {
        "violations": violations,
        "drift": {
            "used": sorted(used_in_last),
            "unused": unused,
            "total_standards": len(all_standards),
        },
        "trends": {
            "ticks_analyzed": len(tick_ids),
            "avg_cost_usd": avg_cost,
            "avg_total_duration_ms": avg_duration,
            "last_cost_usd": last_cost,
            "last_total_duration_ms": last_duration,
            "cost_trend": cost_trend,
            "duration_trend": dur_trend,
            "per_phase": per_phase_stats,
        },
        "suggestions": suggestions,
    }

def recent_decisions(n=5):
    """Last N decisions (from EXECUTE/OBSERVE/SIGNAL phases), with their gate classification."""
    lines = read_pulse_lines()
    decisions = []
    for ln in lines:
        if ln.get("phase") in ("EXECUTE", "OBSERVE", "SIGNAL") and ln.get("decision"):
            gate = "PASS" if "PASS" in ln["decision"] and "BLOCKED" not in ln["decision"] else \
                   "BLOCKED" if "BLOCKED" in ln["decision"] else \
                   "CONDITIONAL" if "CONDITIONAL" in ln["decision"] else \
                   "info"
            decisions.append({
                "ts": ln.get("ts"),
                "tick_id": ln.get("tick_id"),
                "phase": ln.get("phase"),
                "issue_id": ln.get("issue_id"),
                "decision": ln["decision"],
                "gate": gate,
            })
    return decisions[-n:][::-1]  # most recent first



def read_index():
    """Read standards/index.yml via PyYAML or simple manual parse."""
    if not INDEX_FILE.exists():
        return {}
    try:
        import yaml
        return yaml.safe_load(INDEX_FILE.read_text(encoding="utf-8")) or {}
    except ImportError:
        return {}

def read_standard(name):
    """Read a single standard .md by name (root or subfolder)."""
    candidates = [
        AGENT_OS_DIR / "standards" / f"{name}.md",
        AGENT_OS_DIR / "standards" / "l0" / f"{name}.md",
        AGENT_OS_DIR / "standards" / "l1" / f"{name}.md",
        AGENT_OS_DIR / "standards" / "l2" / f"{name}.md",
    ]
    for path in candidates:
        if path.exists():
            return {
                "name": name,
                "path": str(path.relative_to(SYMPHONY_ROOT)),
                "content": path.read_text(encoding="utf-8"),
            }
    return None

def snapshot():
    """Build a snapshot dict from current pulse.log state."""
    lines = read_pulse_lines()
    if not lines:
        return {
            "status": "idle",
            "tick_count": 0,
            "last_tick_id": None,
            "workflow_id": None,
            "aspace_layer": "L2",
            "running": [],
            "retrying": [],
            "donna_escalations_pending": 0,
            "cumulative_cost_usd_total": 0.0,
            "phases_seen": {},
            "standards_used": set(),
            "last_decision": None,
        }
    # Group by tick_id
    by_tick = defaultdict(list)
    for ln in lines:
        by_tick[ln.get("tick_id", "unknown")].append(ln)

    last_tick_id = list(by_tick.keys())[-1]
    last_tick_lines = by_tick[last_tick_id]

    # Find SLEEP line for total
    total_cost = 0.0
    last_sleep = None
    for ln in last_tick_lines:
        if ln.get("cumulative_cost_usd") is not None:
            total_cost = max(total_cost, ln["cumulative_cost_usd"])
        if ln.get("phase") == "SLEEP":
            last_sleep = ln

    # Aggregate across all ticks
    all_cost = 0.0
    for ln in lines:
        if ln.get("cumulative_cost_usd") is not None:
            all_cost = max(all_cost, ln["cumulative_cost_usd"])

    # Phases seen
    phases_seen = defaultdict(int)
    for ln in lines:
        phases_seen[ln.get("phase", "UNKNOWN")] += 1

    # Standards used
    standards_used = set()
    for ln in lines:
        for s in ln.get("standards_injected", []):
            standards_used.add(s)

    # Last decision (from EXECUTE or OBSERVE)
    last_decision = None
    for ln in last_tick_lines:
        if ln.get("phase") in ("EXECUTE", "OBSERVE", "SIGNAL"):
            last_decision = ln.get("decision")

    return {
        "status": "ok",
        "tick_count": len(by_tick),
        "last_tick_id": last_tick_id,
        "workflow_id": last_tick_lines[0].get("workflow_id") if last_tick_lines else None,
        "aspace_layer": "L2",
        "running": [],  # in this static demo, no live tick
        "retrying": [],
        "donna_escalations_pending": 0,
        "cumulative_cost_usd_total": round(all_cost, 4),
        "phases_seen": dict(phases_seen),
        "standards_used": sorted(standards_used),
        "last_decision": last_decision,
        "last_sleep_decision": last_sleep.get("decision") if last_sleep else None,
    }

def phase_stats():
    """Compute per-phase aggregates (avg duration, total cost, count) from pulse.log."""
    lines = read_pulse_lines()
    by_phase = defaultdict(lambda: {"count": 0, "total_duration_ms": 0, "total_cost_delta": 0.0})
    for ln in lines:
        p = ln.get("phase")
        if not p:
            continue
        s = by_phase[p]
        s["count"] += 1
        s["total_duration_ms"] += ln.get("duration_ms", 0) or 0
        if ln.get("cost_delta_usd") is not None:
            s["total_cost_delta"] += ln["cost_delta_usd"]
    out = []
    for p in PHASE_ORDER:
        s = by_phase.get(p, {"count": 0, "total_duration_ms": 0, "total_cost_delta": 0.0})
        out.append({
            "phase": p,
            "count": s["count"],
            "avg_duration_ms": round(s["total_duration_ms"] / s["count"], 1) if s["count"] else 0,
            "total_duration_ms": s["total_duration_ms"],
            "total_cost_delta": round(s["total_cost_delta"], 4),
            "color": PHASE_COLORS.get(p, "#6b7280"),
        })
    return out

def standards_list():
    """List all standards with name + description + path."""
    data = read_index()
    out = []
    for folder, files in data.items():
        for name, meta in files.items():
            path = f"agent-os/standards/{name}.md" if folder == "root" else f"agent-os/standards/{folder}/{name}.md"
            full = AGENT_OS_DIR / "standards" / (name + ".md" if folder == "root" else f"{folder}/{name}.md")
            out.append({
                "name": name,
                "folder": folder,
                "path": path,
                "exists": full.exists(),
                "size_bytes": full.stat().st_size if full.exists() else 0,
                "description": meta.get("description", ""),
            })
    return out

# --- HTTP handler --------------------------------------------------------------
class SymphonyHandler(http.server.BaseHTTPRequestHandler):

    def log_message(self, fmt, *args):
        # Quieter logs (suppress per-request noise)
        return

    def _send_json(self, obj, status=200):
        body = json.dumps(obj, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path, content_type="text/plain; charset=utf-8"):
        if not path.exists():
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")
            return
        body = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        path = url.path

        if path == "/" or path == "/index.html":
            return self._send_file(UI_DIR / "index.html", "text/html; charset=utf-8")

        if path.startswith("/static/"):
            rel = path[len("/static/"):]
            for ct, ext in [("text/css", ".css"), ("application/javascript", ".js"),
                            ("image/svg+xml", ".svg"), ("image/png", ".png")]:
                if rel.endswith(ext):
                    return self._send_file(UI_DIR / rel, ct)
            return self._send_file(UI_DIR / rel, "application/octet-stream")

        if path == "/api/snapshot":
            return self._send_json(snapshot())

        if path == "/api/pulse":
            qs = urllib.parse.parse_qs(url.query)
            n = int(qs.get("last", ["50"])[0])
            lines = read_pulse_lines()
            tail = lines[-n:] if len(lines) > n else lines
            return self._send_json({
                "count": len(tail),
                "total_in_file": len(lines),
                "lines": tail,
            })

        if path == "/api/standards":
            return self._send_json(standards_list())

        if path.startswith("/api/standards/"):
            name = path[len("/api/standards/"):]
            std = read_standard(name)
            if std is None:
                return self._send_json({"error": f"standard not found: {name}"}, status=404)
            return self._send_json(std)

        if path == "/api/cost":
            return self._send_json({
                "phases": phase_stats(),
            })

        if path == "/api/phase-stats":
            return self._send_json({
                "phases": phase_stats(),
            })

        if path == "/api/intelligence":
            return self._send_json(intelligence_report())

        if path == "/api/recent-decisions":
            qs = urllib.parse.parse_qs(url.query)
            n = int(qs.get("n", ["5"])[0])
            return self._send_json({"decisions": recent_decisions(n)})

        if path == "/api/health":
            return self._send_json({
                "status": "ok",
                "pulse_log_exists": PULSE_LOG.exists(),
                "pulse_log_lines": len(read_pulse_lines()),
                "standards_count": len(standards_list()),
                "demo_tick_sh_exists": DEMO_TICK_SH.exists(),
            })

        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"Not found")

    def do_POST(self):
        url = urllib.parse.urlparse(self.path)
        if url.path == "/api/tick":
            # Run the demo tick handler in a subprocess (async, don't block)
            try:
                # Use bash version (more portable than PS1 on this machine)
                if DEMO_TICK_SH.exists():
                    # On Windows, run via bash (Git Bash should be in PATH)
                    result = subprocess.Popen(
                        ["bash", str(DEMO_TICK_SH)],
                        cwd=str(SYMPHONY_ROOT),
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                    )
                    return self._send_json({
                        "status": "triggered",
                        "pid": result.pid,
                        "script": str(DEMO_TICK_SH.name),
                        "cwd": str(SYMPHONY_ROOT),
                    })
                else:
                    return self._send_json({"error": "demo tick script not found"}, status=500)
            except Exception as e:
                return self._send_json({"error": str(e)}, status=500)
        self.send_response(404)
        self.end_headers()


# --- Main ----------------------------------------------------------------------
class ReuseTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def main():
    port = int(os.environ.get("SYMPHONY_UI_PORT", "8080"))
    host = os.environ.get("SYMPHONY_UI_HOST", "127.0.0.1")
    print(f"=== Symphony × Agent OS UI Server ===")
    print(f"Listening on http://{host}:{port}")
    print(f"Symphony root:  {SYMPHONY_ROOT}")
    print(f"Pulse log:      {PULSE_LOG}")
    print(f"Standards:      {len(standards_list())} loaded from index.yml")
    print(f"Demo tick:      {DEMO_TICK_SH}")
    print()
    print(f"Open your browser to:  http://{host}:{port}/")
    print(f"Trigger a tick:        POST http://{host}:{port}/api/tick")
    print()
    try:
        with ReuseTCPServer((host, port), SymphonyHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[shutdown] KeyboardInterrupt, exiting cleanly")
    except OSError as e:
        print(f"\n[error] could not bind to {host}:{port}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
