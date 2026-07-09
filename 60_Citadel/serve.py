"""
serve.py — Citadelle A0 local server (P0 + P1 + P2).

Endpoints :
  Pages UI (Bridge, Décisions, Agents, Frameworks, Domaines, Memory):
    GET /, /decisions, /agents, /frameworks, /domains, /memory

  API data:
    GET /api/health
    GET /api/data/{01,04,06,07,08,09,10,11}_* (alias /api/<slug>)
    GET /api/decisions/list, /api/decisions/status

  API POST (ratification P1):
    POST /api/decisions/ratify (append-only decision file, sans canonic edit)
    POST /api/decisions/apply   (canonic edit gated by enable_write_canonic.flag)

DOCTRINE ANTI-ULTRON :
  - Lecture seule sur sources canoniques.
  - Écriture bornée : data/*.json (overwrite idempotent) + decisions/*.json (append-only D4) + logs/*.log.
  - Auto-start GATED par flag (install-autostart.ps1 refuse sans flag).
  - Watchdog GATED par flag (watchdog.ps1 refuse sans flag).
  - Pas d'auto-approval. Pas de batch. Pas de réveille dormants.

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P0+P1+P2
"""
from __future__ import annotations

import json
import logging
import os
import re
import sys
import time
import uuid
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
STATIC_DIR = ROOT / "static"
DECISIONS_DIR = ROOT / "decisions"
LOG_FILE = ROOT / "logs" / "citadel.log"
ENABLE_CANONIC_FLAG = DECISIONS_DIR / "enable_write_canonic.flag"
ENABLE_AUTOSTART_FLAG = DECISIONS_DIR / "enable_autostart.flag"
ENABLE_WATCHDOG_FLAG = DECISIONS_DIR / "enable_watchdog.flag"
ENABLE_ZORA_FLAG = DECISIONS_DIR / "enable_zora.flag"
ENABLE_SUBMISSIONS_FLAG = DECISIONS_DIR / "enable_submissions.flag"
CMS_DIR = ROOT / "cms"  # visitor submissions gated append-only
CRON_OUTPUT_DIR = ROOT / "cron" / "output"
MAX_BODY_BYTES = 1_048_576  # 1 MiB cap

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("citadel")

CITADEL_HOST = os.environ.get("CITADEL_HOST", "127.0.0.1")
CITADEL_PORT = int(os.environ.get("CITADEL_PORT", "8770"))


def canonic_writes_enabled() -> bool:
    """12WY-ON-PAUSE bypass — Tony Stark pré-ratification 12 sem."""
    twelve_wy_pause = DECISIONS_DIR / "12WY_ON_PAUSE.flag"
    if twelve_wy_pause.exists():
        return True  # Tony pré-ratifié
    return ENABLE_CANONIC_FLAG.exists()


def autostart_enabled() -> bool:
    """12WY-ON-PAUSE bypass — Tony Stark pré-ratification 12 sem (ADR-WARMODE-001)."""
    twelve_wy_pause = DECISIONS_DIR / "12WY_ON_PAUSE.flag"
    if twelve_wy_pause.exists():
        return True
    return ENABLE_AUTOSTART_FLAG.exists()


def watchdog_enabled() -> bool:
    """12WY-ON-PAUSE bypass — Tony Stark pré-ratification 12 sem (ADR-WARMODE-001)."""
    twelve_wy_pause = DECISIONS_DIR / "12WY_ON_PAUSE.flag"
    if twelve_wy_pause.exists():
        return True
    return ENABLE_WATCHDOG_FLAG.exists()


def submissions_enabled() -> bool:
    return ENABLE_SUBMISSIONS_FLAG.exists()


def zora_enabled() -> bool:
    """12WY-ON-PAUSE bypass — Tony Stark pré-ratification 12 sem (ADR-WARMODE-001)."""
    twelve_wy_pause = DECISIONS_DIR / "12WY_ON_PAUSE.flag"
    if twelve_wy_pause.exists():
        return True
    return ENABLE_ZORA_FLAG.exists()


class CitadelHandler(BaseHTTPRequestHandler):
    server_version = "CitadelleA0/0.3"

    def log_message(self, fmt: str, *args) -> None:
        log.info("%s - %s", self.address_string(), fmt % args)

    def _send_json(self, payload, status=200):
        body = json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path: Path, content_type: str):
        if not path.exists():
            self.send_error(404, f"{path.name} not found")
            return
        try:
            body = path.read_bytes()
        except OSError as e:
            log.error("read %s failed: %s", path, e)
            self.send_error(500, "read failed")
            return
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _now_iso(self):
        return time.strftime("%Y-%m-%dT%H:%M:%S%z")

    def _read_body(self):
        n = int(self.headers.get("Content-Length", "0") or "0")
        if n <= 0 or n > MAX_BODY_BYTES:
            return None
        try:
            raw = self.rfile.read(n)
            return json.loads(raw.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError, OSError) as e:
            log.warning("bad body: %s", e)
            return None

    def do_GET(self):
        url = urlparse(self.path)
        path = url.path.rstrip("/") or "/"

        # Pages UI
        page_map = {
            "/": ("bridge.html", "text/html; charset=utf-8"),
            "/index.html": ("bridge.html", "text/html; charset=utf-8"),
            "/decisions": ("decisions.html", "text/html; charset=utf-8"),
            "/decisions.html": ("decisions.html", "text/html; charset=utf-8"),
            "/agents": ("agents.html", "text/html; charset=utf-8"),
            "/agents.html": ("agents.html", "text/html; charset=utf-8"),
            "/frameworks": ("frameworks.html", "text/html; charset=utf-8"),
            "/frameworks.html": ("frameworks.html", "text/html; charset=utf-8"),
            "/domains": ("domains.html", "text/html; charset=utf-8"),
            "/domains.html": ("domains.html", "text/html; charset=utf-8"),
            "/memory": ("memory.html", "text/html; charset=utf-8"),
            "/memory.html": ("memory.html", "text/html; charset=utf-8"),
            "/zora": ("zora.html", "text/html; charset=utf-8"),
            "/zora.html": ("zora.html", "text/html; charset=utf-8"),
            "/harnesses": ("harnesses.html", "text/html; charset=utf-8"),
            "/harnesses.html": ("harnesses.html", "text/html; charset=utf-8"),
            "/patterns": ("patterns.html", "text/html; charset=utf-8"),
            "/patterns.html": ("patterns.html", "text/html; charset=utf-8"),
            "/warmode": ("warmode.html", "text/html; charset=utf-8"),
            "/warmode.html": ("warmode.html", "text/html; charset=utf-8"),
        }
        if path in page_map:
            fname, ctype = page_map[path]
            return self._send_file(STATIC_DIR / fname, ctype)

        # CMS dynamic item page: /c/<collection>/<item_id>
        cm = re.match(r"^/c/([\w-]+)/([\w.\-]+)/?$", path)
        if cm:
            return self._send_file(STATIC_DIR / "item.html", "text/html; charset=utf-8")
        # Collection index: /c/<collection>
        cm2 = re.match(r"^/c/([\w-]+)/?$", path)
        if cm2:
            list_map = {
                "01_harnesses": "/harnesses", "04_skills": "/skills", "06_connections": "/connections",
                "07_decisions": "/decisions", "08_agents": "/agents", "09_frameworks": "/frameworks",
                "10_domains": "/domains", "11_memory": "/memory", "13_patterns": "/patterns",
            }
            target = list_map.get(cm2.group(1))
            if target:
                self.send_response(302)
                self.send_header("Location", target)
                self.end_headers()
                return
            return self._send_json({"error": f"no list page for {cm2.group(1)}"}, status=404)

        # API GET
        api_map = {
            "/api/health": None,
            "/api/data/01_harnesses": "01_harnesses.json",
            "/api/data/04_skills": "04_skills.json",
            "/api/data/06_connections": "06_connections.json",
            "/api/data/07_decisions": "07_decisions.json",
            "/api/data/08_agents": "08_agents.json",
            "/api/data/09_frameworks": "09_frameworks.json",
            "/api/data/10_domains": "10_domains.json",
            "/api/data/11_memory": "11_memory.json",
            "/api/data/12_zora": "12_zora.json",
            "/api/data/13_patterns": "13_patterns.json",
            "/api/data/13_harnesses_live": "13_harnesses_live.json",
            "/api/data/14_warmode": "14_warmode.json",
            "/api/warmode": "14_warmode.json",
            "/api/harnesses": "01_harnesses.json",
            "/api/skills": "04_skills.json",
            "/api/connections": "06_connections.json",
            "/api/decisions": "07_decisions.json",
            "/api/agents": "08_agents.json",
            "/api/frameworks": "09_frameworks.json",
            "/api/domains": "10_domains.json",
            "/api/memory": "11_memory.json",
            "/api/zora": "12_zora.json",
            "/api/patterns": "13_patterns.json",
            "/api/harnesses/live": "13_harnesses_live.json",
        }
        if path in api_map:
            fname = api_map[path]
            if fname is None:
                return self._send_json({
                    "status": "ok",
                    "service": "citadelle-a0",
                    "version": "0.4",
                    "pillar": "P0 + P1 + P2 + P3 backend",
                    "doctrine": "lecture seule — anti-Ultron — dormants affichés — append-only décisions",
                    "flags": {
                        "canonic_writes": canonic_writes_enabled(),
                        "autostart": autostart_enabled(),
                        "watchdog": watchdog_enabled(),
                        "zora": zora_enabled(),
                    },
                    "pages": ["/", "/decisions", "/agents", "/frameworks", "/domains", "/memory", "/zora", "/harnesses"],
                    "endpoints": [
                        "/api/health", "/api/harnesses", "/api/harnesses/live", "/api/skills", "/api/connections",
                        "/api/decisions", "/api/agents", "/api/frameworks", "/api/domains", "/api/memory",
                        "/api/zora", "/api/zora/last-run",
                    ],
                    "timestamp": self._now_iso(),
                })
            return self._send_json(self._load_data(fname))

        if path == "/api/zora/last-run":
            return self._send_json(self._zora_last_run())

        if path == "/api/decisions/list":
            return self._send_json({
                "decision_files": self._list_decisions(),
                "count": len(self._list_decisions()),
            })
        if path == "/api/decisions/status":
            return self._send_json({
                "flags": {
                    "canonic_writes_enabled": canonic_writes_enabled(),
                    "autostart_enabled": autostart_enabled(),
                    "watchdog_enabled": watchdog_enabled(),
                    "zora_enabled": zora_enabled(),
                },
                "decision_dir": str(DECISIONS_DIR),
                "decision_count": len(self._list_decisions()),
                "timestamp": self._now_iso(),
            })

        # CMS dynamic item endpoint: /api/data/<collection>/item/<item_id>
        cm = re.match(r"^/api/data/([\w-]+)/item/([\w.\-]+)/?$", path)
        if cm:
            return self._cms_get_item(cm.group(1), cm.group(2))

        # CMS status endpoint
        if path == "/api/cms/status":
            return self._send_json({
                "submissions_enabled": submissions_enabled(),
                "cms_dir": str(CMS_DIR),
                "collections": sorted([p.stem.replace(".json", "") for p in DATA_DIR.glob("*.json")]),
                "timestamp": self._now_iso(),
            })

        self.send_error(404, f"not found: {path}")

    def do_POST(self):
        url = urlparse(self.path)
        path = url.path.rstrip("/") or "/"

        if path == "/api/decisions/ratify":
            return self._handle_ratify()
        if path == "/api/decisions/apply":
            return self._handle_apply()
        if path == "/api/cms/submit":
            return self._handle_submit()

        self.send_error(404, f"POST not found: {path}")

    def _load_data(self, filename: str):
        p = DATA_DIR / filename
        if not p.exists():
            return {"error": f"{filename} not found — run collectors first", "path": str(p)}
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            return {"error": str(e), "path": str(p)}

    def _list_decisions(self):
        out = []
        if not DECISIONS_DIR.exists():
            return out
        for f in sorted(DECISIONS_DIR.glob("*.json")):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                out.append({"filename": f.name, "path": str(f), **data})
            except (json.JSONDecodeError, OSError):
                out.append({"filename": f.name, "path": str(f), "error": "unreadable"})
        return out

    def _zora_last_run(self) -> dict:
        if not CRON_OUTPUT_DIR.exists():
            return {"last_run": "never", "doctrine": "lecture seule — pas de fichier créé"}
        runs = sorted(CRON_OUTPUT_DIR.glob("zora-*.json"))
        if not runs:
            return {"last_run": "never", "doctrine": "lecture seule — pas de fichier créé"}
        last = runs[-1]
        try:
            data = json.loads(last.read_text(encoding="utf-8"))
            return {"last_run": last.name, "path": str(last), **data}
        except (json.JSONDecodeError, OSError) as e:
            return {"last_run": last.name, "error": str(e), "path": str(last)}

    def _handle_ratify(self):
        body = self._read_body()
        if body is None:
            return self._send_json({"error": "invalid JSON body"}, status=400)
        adr_id = body.get("adr_id", "").strip()
        decision = body.get("decision", "").strip().lower()
        rationale = body.get("rationale", "").strip()
        decided_by = body.get("decided_by", "A0").strip()
        if not re.match(r"^ADR-LD01-\d{3}$", adr_id):
            return self._send_json({"error": f"invalid adr_id: {adr_id}"}, status=400)
        # P3 backend (2026-07-04): cross-check canon before ratify — refuse invented ADRs
        canon_dir = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\30_decisions")
        if not (canon_dir / f"{adr_id}_*.md").glob.__self__.parent.exists():
            pass  # always exists; kept for clarity
        if not list(canon_dir.glob(f"{adr_id}_*.md")):
            return self._send_json({
                "error": f"canon ADR not found for {adr_id}",
                "canon_dir": str(canon_dir),
                "hint": "ADR must exist on disk before ratification (anti-fabrication)",
            }, status=404)
        if decision not in ("ratify", "reject"):
            return self._send_json({"error": f"invalid decision: {decision} (must be ratify|reject)"}, status=400)
        if not rationale:
            return self._send_json({"error": "rationale required"}, status=400)

        ts = datetime.now()
        ts_slug = ts.strftime("%Y-%m-%dT%H-%M-%S")
        filename = f"{ts_slug}_{adr_id}_{decision}.json"
        path = DECISIONS_DIR / filename
        payload = {
            "id": str(uuid.uuid4())[:8],
            "adr_id": adr_id,
            "decision": decision,
            "rationale": rationale,
            "decided_by": decided_by,
            "decided_at": ts.isoformat(),
            "gate_2_P1": True,
            "canonic_writes_enabled_at_decide_time": canonic_writes_enabled(),
            "status": "DECIDED",
        }
        try:
            path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        except OSError as e:
            log.error("write %s failed: %s", path, e)
            return self._send_json({"error": str(e)}, status=500)
        log.info("DECISION %s %s by %s (%d b rationale) → %s", decision, adr_id, decided_by, len(rationale), filename)
        return self._send_json({
            "ok": True,
            "decision_file": filename,
            "path": str(path),
            "canonic_writes_enabled": canonic_writes_enabled(),
            "next_step": "Run POST /api/decisions/apply to apply (requires enable_write_canonic.flag)" if not canonic_writes_enabled() else "Canonic edits enabled — apply will mutate ADR status",
        }, status=201)

    def _handle_apply(self):
        if not canonic_writes_enabled():
            return self._send_json({
                "error": "canonic writes disabled — create decisions/enable_write_canonic.flag (A0 HITL) to enable",
                "gate": "P1 will need Gate #2 GO canon explicitly",
            }, status=403)
        body = self._read_body()
        if body is None:
            return self._send_json({"error": "invalid JSON body"}, status=400)
        fname = body.get("decision_file", "").strip()
        if not fname or "/" in fname or "\\" in fname:
            return self._send_json({"error": f"invalid decision_file: {fname}"}, status=400)
        path = DECISIONS_DIR / fname
        if not path.exists():
            return self._send_json({"error": f"{fname} not found"}, status=404)
        try:
            decision_data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            return self._send_json({"error": str(e)}, status=500)

        adr_id = decision_data.get("adr_id", "")
        decision = decision_data.get("decision", "")
        adr_dir = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\30_decisions")
        adr_files = list(adr_dir.glob(f"{adr_id}_*.md")) if adr_dir.exists() else []
        if not adr_files:
            return self._send_json({"error": f"canon ADR file not found for {adr_id}"}, status=404)
        adr_path = adr_files[0]
        try:
            content = adr_path.read_text(encoding="utf-8")
        except OSError as e:
            return self._send_json({"error": str(e)}, status=500)
        new_status = "RATIFIED" if decision == "ratify" else "REJECTED"
        new_content = re.sub(
            r"(\*\*Statut\*\*\s*:\s*\*\*)PROPOSED(\*\*)",
            rf"\g<1>{new_status}\g<2>",
            content,
            count=1,
        )
        # Also patch YAML frontmatter status:
        if "status: PROPOSED" in new_content:
            new_content = new_content.replace("status: PROPOSED", f"status: {new_status}", 1)
        if new_content == content:
            return self._send_json({"error": f"could not locate PROPOSED in {adr_id}"}, status=409)
        try:
            adr_path.write_text(new_content, encoding="utf-8")
        except OSError as e:
            return self._send_json({"error": str(e)}, status=500)
        log.info("APPLIED %s → %s (%s)", fname, adr_id, new_status)
        return self._send_json({
            "ok": True,
            "adr_id": adr_id,
            "new_status": new_status,
            "canon_path": str(adr_path),
            "decision_file": fname,
        })

    def _cms_get_item(self, collection: str, item_id: str):
        """GET /api/data/<collection>/item/<item_id>
        Loads collection JSON, finds item by id (field varies by collection).
        Returns 404 if not found.
        """
        f = DATA_DIR / f"{collection}.json"
        if not f.exists():
            return self._send_json({"error": f"collection not found: {collection}"}, status=404)
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            return self._send_json({"error": str(e)}, status=500)

        # Universal key candidates (collection-agnostic): name, path, id, label, jerry_domain, agent_id, file
        candidates = ("name", "path", "id", "label", "jerry_domain", "agent_id", "filename", "title")
        # 1. tiered structures (08_agents has data.tiers[A/B][item_id])
        if isinstance(data, dict) and "tiers" in data:
            for tier_name, tier_list in data["tiers"].items():
                for it in tier_list or []:
                    for c in candidates:
                        if c in it and str(it[c]) == item_id:
                            return self._send_json({"matched_tier": tier_name, "item": it})
            # Try composite keys like "b1-jerry-emyth"
            for tier_name, tier_list in data["tiers"].items():
                for it in tier_list or []:
                    if f"{tier_name}-{it.get('name','')}" == item_id:
                        return self._send_json({"matched_tier": tier_name, "item": it})
        # 2. flat arrays (all_agents, frameworks, domains, etc.)
        for arr_key in ("all_agents", "frameworks", "domains", "all_skills", "entities", "items", "patterns", "memory_principles", "all_decisions"):
            if arr_key in data and isinstance(data[arr_key], list):
                for it in data[arr_key]:
                    if isinstance(it, dict):
                        for c in candidates:
                            if c in it and str(it[c]) == item_id:
                                return self._send_json({"matched_key": arr_key, "item": it})
        # 3. summary-based (decision_count, etc.) — can't return single item
        return self._send_json({"error": f"item not found in {collection}: {item_id}", "hint": "check collection schema"}, status=404)

    def _handle_submit(self):
        """POST /api/cms/submit
        Body: { "collection": "08_agents", "fields": { "name": "...", "note": "..." } }
        Gated by enable_submissions.flag. Writes append-only JSON in cms/<collection>/<ts>.json
        """
        if not submissions_enabled():
            return self._send_json({
                "error": "submissions disabled — create decisions/enable_submissions.flag (A0 HITL) to enable",
                "gate": "visitor-submission P3 anti-Ultron",
            }, status=403)
        body = self._read_body()
        if body is None:
            return self._send_json({"error": "invalid JSON body"}, status=400)
        collection = body.get("collection", "").strip()
        fields = body.get("fields", {})
        if not collection or not isinstance(fields, dict) or not fields:
            return self._send_json({"error": "collection and fields required"}, status=400)
        if not re.match(r"^[\w-]+$", collection):
            return self._send_json({"error": f"invalid collection: {collection}"}, status=400)
        ts = datetime.now()
        ts_slug = ts.strftime("%Y-%m-%dT%H-%M-%S")
        sub_dir = CMS_DIR / collection
        try:
            sub_dir.mkdir(parents=True, exist_ok=True)
            item_id = f.get("name", f"item-{ts_slug}") if False else ts_slug
            path = sub_dir / f"{ts_slug}_{fields.get('name','item')}.json"
            payload = {
                "id": str(uuid.uuid4())[:8],
                "submitted_at": ts.isoformat(),
                "collection": collection,
                "fields": fields,
                "submissions_enabled_at_decide_time": submissions_enabled(),
                "status": "SUBMITTED",
            }
            path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        except OSError as e:
            log.error("CMS submit write failed: %s", e)
            return self._send_json({"error": str(e)}, status=500)
        log.info("CMS SUBMIT to %s by visitor → %s", collection, path.name)
        return self._send_json({
            "ok": True,
            "submission_file": path.name,
            "path": str(path),
            "collection": collection,
        }, status=201)


def main() -> int:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    STATIC_DIR.mkdir(parents=True, exist_ok=True)
    DECISIONS_DIR.mkdir(parents=True, exist_ok=True)
    CRON_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    httpd = ThreadingHTTPServer((CITADEL_HOST, CITADEL_PORT), CitadelHandler)
    log.info("Citadelle A0 serving on http://%s:%d (P0 + P1 + P2 + P3 backend)", CITADEL_HOST, CITADEL_PORT)
    log.info("Pages: / /decisions /agents /frameworks /domains /memory /zora /harnesses")
    log.info("Endpoints API: 11 data + ratify/apply decisions + zora/last-run")
    log.info("Doctrine: lecture seule — append-only — gates anti-Ultron actifs")
    log.info("Flags: canonic_writes=%s autostart=%s watchdog=%s zora=%s",
             canonic_writes_enabled(), autostart_enabled(), watchdog_enabled(), zora_enabled())
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        log.info("Citadelle A0 stopped (KeyboardInterrupt)")
    return 0


if __name__ == "__main__":
    sys.exit(main())