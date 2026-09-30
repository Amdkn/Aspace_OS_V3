import os
import sys
import json
import shutil
import hashlib
import subprocess
from datetime import datetime, timezone
from pathlib import Path

class GWSAdapter:
    """
    Google Workspace Sheets (GWS) Adapter for Workbook 1lqI1uJhqK9K45kibmZzpKTrnI5VHiAxSLu20RU3zTA0.
    Implements 13 canonical tabs, deterministic row IDs, idempotent dedup, durable local receipts,
    and postcondition readback verification via authenticated GWS CLI (or deterministic mock).
    """
    WORKBOOK_ID = "1lqI1uJhqK9K45kibmZzpKTrnI5VHiAxSLu20RU3zTA0"

    CANONICAL_TABS = [
        "00_Control", "01_Channels", "02_Videos", "03_CitationCandidates",
        "04_Papers", "05_VideoPaperEdges", "06_PaperRelations", "07_Artifacts",
        "08_InnovationFeatures", "09_CapabilityCandidates", "10_ReviewQueue",
        "11_Runs", "12_Dashboard"
    ]

    TAB_COLUMNS = {
        "00_Control": ["key", "value", "updated_at", "run_id", "notes"],
        "01_Channels": ["channel_id", "handle", "title", "uploads_playlist_id", "source_url", "inventory_state", "last_inventory_at", "video_count_seen", "source_run_id"],
        "02_Videos": ["video_id", "channel_id", "published_at", "title", "url", "description_hash", "description_artifact_ref", "description_state", "transcript_state", "keyframes_state", "citation_count", "resolved_paper_count", "deep_capture_state", "first_seen_at", "last_seen_at", "source_run_id"],
        "03_CitationCandidates": ["candidate_id", "video_id", "candidate_kind", "raw_text", "normalized_title", "authors_raw", "url_or_id", "source_span", "extraction_mode", "extract_confidence", "resolver_state", "review_reason", "source_run_id"],
        "04_Papers": ["paper_id", "canonical_id_type", "canonical_id", "doi", "arxiv_id", "openreview_id", "title", "year", "authors", "abstract_hash", "abstract_artifact_ref", "resolver_provider", "resolver_confidence", "review_state", "deep_capture_state", "first_seen_at", "last_seen_at", "source_run_id"],
        "05_VideoPaperEdges": ["edge_id", "video_id", "paper_id", "relation", "candidate_id", "resolution_confidence", "provenance_ref", "source_run_id"],
        "06_PaperRelations": ["edge_id", "source_paper_id", "relation", "target_paper_id", "provider", "confidence", "provenance_ref", "source_run_id"],
        "07_Artifacts": ["artifact_id", "owner_type", "owner_id", "artifact_type", "uri", "sha256", "mime_type", "size_bytes", "capture_method", "captured_at", "source_run_id"],
        "08_InnovationFeatures": ["feature_id", "source_type", "source_id", "problem", "mechanism", "inputs", "outputs", "constraints", "benchmark", "dependencies", "execution_mode", "latency", "cost", "side_effects", "claims", "limitations", "artifact_refs", "agy_run_id", "validation_state", "source_run_id"],
        "09_CapabilityCandidates": ["mapping_id", "feature_id", "capability_atom", "relation_to_nearest", "nearest_capabilities", "os_affinity_kernel", "os_affinity_life", "os_affinity_business", "companion_affinity", "decision_level", "choice", "score", "noul", "host_gate", "mapping_state", "system2_ref", "graham_state", "clara_state", "source_run_id"],
        "10_ReviewQueue": ["review_id", "entity_type", "entity_id", "reason", "priority", "evidence_refs", "proposed_action", "owner_capability", "state", "reviewed_by", "reviewed_at", "source_run_id"],
        "11_Runs": ["run_id", "operation_id", "stage", "tool", "harness", "model", "started_at", "finished_at", "status", "input_hash", "output_ref", "receipt_ref", "error_code", "retry_of"],
        "12_Dashboard": ["metric", "value", "window", "computed_at", "source_ref"]
    }

    TAB_KEYS = {
        "00_Control": "key",
        "01_Channels": "channel_id",
        "02_Videos": "video_id",
        "03_CitationCandidates": "candidate_id",
        "04_Papers": "paper_id",
        "05_VideoPaperEdges": "edge_id",
        "06_PaperRelations": "edge_id",
        "07_Artifacts": "artifact_id",
        "08_InnovationFeatures": "feature_id",
        "09_CapabilityCandidates": "mapping_id",
        "10_ReviewQueue": "review_id",
        "11_Runs": "run_id",
        "12_Dashboard": "metric"
    }

    def __init__(self, receipt_dir="gws_receipts", workbook_id=None, mock_mode=None):
        self.receipt_dir = str(receipt_dir)
        os.makedirs(self.receipt_dir, exist_ok=True)
        self.workbook_id = workbook_id or self.WORKBOOK_ID

        if mock_mode is not None:
            self.mock_mode = mock_mode
        else:
            env_mock = os.environ.get("GWS_MOCK")
            if env_mock is not None:
                self.mock_mode = (env_mock == "1")
            else:
                self.mock_mode = (self._find_gws() is None)

        # In memory state of the workbook to simulate read/write postconditions
        self.workbook_state = {tab: {} for tab in self.CANONICAL_TABS}

    @staticmethod
    def _find_gws():
        return shutil.which("gws") or shutil.which("gws.cmd")

    def _call_gws(self, args, body=None, timeout=45):
        gws_bin = self._find_gws()
        if not gws_bin:
            raise RuntimeError("gws executable not found")
        base = [os.environ.get("COMSPEC") or r"C:\Windows\System32\cmd.exe", "/d", "/c", gws_bin] if (os.name == "nt" and gws_bin.lower().endswith((".cmd", ".bat"))) else [gws_bin]
        cmd = [*base, "sheets", *args]
        if body is not None:
            cmd += ["--json", json.dumps(body, separators=(",", ":"))]
        cp = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, encoding="utf-8")
        if cp.returncode != 0:
            err_msg = (cp.stderr or cp.stdout or "").strip()
            raise RuntimeError(f"GWS CLI error rc={cp.returncode}: {err_msg[-1000:]}")
        raw = cp.stdout.strip()
        return json.loads(raw) if raw else {}

    def generate_row_id(self, tab, keys):
        """Generate a deterministic row ID based on composite keys."""
        key_str = f"{tab}_{'_'.join(str(k) for k in keys)}"
        return hashlib.sha256(key_str.encode('utf-8')).hexdigest()[:16]

    def _save_local_receipt(self, batch_id, payload, result):
        """Durable local receipt for audit and recovery."""
        receipt = {
            "schema": "aspace.discover-ai.gws-receipt.v1",
            "batch_id": batch_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "workbook": self.workbook_id,
            "mock_mode": self.mock_mode,
            "payload": payload,
            "result": result
        }
        receipt_path = os.path.join(self.receipt_dir, f"receipt_{batch_id}.json")
        with open(receipt_path, 'w', encoding='utf-8') as f:
            json.dump(receipt, f, indent=2)
        return receipt_path

    def _read_live_tab(self, tab, range_suffix="A1:Z1000"):
        params = json.dumps({"spreadsheetId": self.workbook_id, "range": f"'{tab}'!{range_suffix}"}, separators=(",", ":"))
        res = self._call_gws(["spreadsheets", "values", "get", "--params", params, "--format", "json"])
        return res.get("values") or []

    def _row_to_list(self, tab, data):
        columns = self.TAB_COLUMNS.get(tab, [])
        row = []
        for col in columns:
            val = data.get(col, "")
            if isinstance(val, (dict, list)):
                val = json.dumps(val, ensure_ascii=False)
            elif val is None:
                val = ""
            row.append(str(val))
        return row

    def write_batch(self, payloads):
        """
        Idempotent batch write across multiple tabs.
        Payloads: list of dicts: {"tab": "...", "keys": [...], "data": {...}}
        Returns success boolean and error details.
        """
        batch_id = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        written_count = 0

        try:
            tab_payloads = {}
            for item in payloads:
                tab = item.get("tab")
                if tab not in self.CANONICAL_TABS:
                    raise ValueError(f"Invalid tab {tab}")

                keys = item.get("keys", [])
                data = dict(item.get("data", {}))

                row_id = self.generate_row_id(tab, keys)
                data["_row_id"] = row_id

                # Idempotent in-memory record
                if row_id not in self.workbook_state[tab]:
                    written_count += 1
                self.workbook_state[tab][row_id] = data

                tab_payloads.setdefault(tab, []).append((row_id, data))

            live_details = {}
            if not self.mock_mode:
                for tab, items in tab_payloads.items():
                    existing_rows = self._read_live_tab(tab)
                    key_col = self.TAB_KEYS.get(tab)
                    columns = self.TAB_COLUMNS.get(tab, [])
                    key_idx = columns.index(key_col) if (key_col in columns) else 0

                    existing_keys = set()
                    if existing_rows and len(existing_rows) > 1:
                        for r in existing_rows[1:]:
                            if len(r) > key_idx:
                                existing_keys.add(str(r[key_idx]))

                    new_rows = []
                    for row_id, data in items:
                        pk_val = str(data.get(key_col, row_id))
                        if pk_val not in existing_keys:
                            new_rows.append(self._row_to_list(tab, data))
                            existing_keys.add(pk_val)

                    if new_rows:
                        params = json.dumps({
                            "spreadsheetId": self.workbook_id,
                            "range": f"'{tab}'!A:Z",
                            "valueInputOption": "RAW",
                            "insertDataOption": "INSERT_ROWS"
                        }, separators=(",", ":"))
                        body = {"majorDimension": "ROWS", "values": new_rows}
                        append_res = self._call_gws(["spreadsheets", "values", "append", "--params", params, "--format", "json"], body=body)
                        live_details[tab] = {"appended": len(new_rows), "response": append_res}
                    else:
                        live_details[tab] = {"appended": 0, "status": "deduplicated"}

            self._save_local_receipt(batch_id, payloads, {
                "status": "SUCCESS",
                "written": written_count,
                "live_details": live_details
            })
            return True, None
        except Exception as e:
            self._save_local_receipt(batch_id, payloads, {"status": "FAILED", "error": str(e)})
            return False, str(e)

    def validate_postconditions(self, expected_counts):
        """
        Verify that the workbook state matches expectations.
        expected_counts: dict of {tab: expected_count}
        """
        for tab, expected in expected_counts.items():
            if self.mock_mode:
                actual = len(self.workbook_state.get(tab, {}))
                if actual != expected:
                    return False, f"Tab {tab} has {actual} rows, expected {expected}"
            else:
                rows = self._read_live_tab(tab)
                actual = max(0, len(rows) - 1) if rows else 0
                if actual < expected:
                    return False, f"Tab {tab} has {actual} rows, expected at least {expected}"
        return True, None

    def run_canary(self):
        """
        Executes end-to-end canary on workbook:
        1. Reads and validates canonical headers for all 13 tabs.
        2. Appends a canary execution run row to 11_Runs.
        3. Rereads 11_Runs and verifies postconditions.
        """
        run_id = f"run-canary-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}"
        op_id = f"op-{run_id}"

        results = {
            "workbook_id": self.workbook_id,
            "mock_mode": self.mock_mode,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "tabs_validated": [],
            "canary_run_id": run_id,
            "stages": {}
        }

        # 1. Header validation
        if not self.mock_mode:
            for tab in self.CANONICAL_TABS:
                rows = self._read_live_tab(tab, "A1:Z1")
                actual_header = rows[0] if rows else []
                expected_header = self.TAB_COLUMNS[tab]
                if actual_header != expected_header:
                    raise RuntimeError(f"Header mismatch in tab {tab}: {actual_header} != {expected_header}")
                results["tabs_validated"].append(tab)

        # 2. Canary run payload
        receipt_ref = os.path.join(self.receipt_dir, f"{run_id}.json")
        payload = [{
            "tab": "11_Runs",
            "keys": [run_id],
            "data": {
                "run_id": run_id,
                "operation_id": op_id,
                "stage": "M0_GWS_CANARY",
                "tool": "gws_adapter.py",
                "harness": "local-gws-cli",
                "model": "deterministic",
                "started_at": datetime.now(timezone.utc).isoformat(),
                "finished_at": datetime.now(timezone.utc).isoformat(),
                "status": "PASS",
                "input_hash": f"sha256:{hashlib.sha256(run_id.encode()).hexdigest()[:16]}",
                "output_ref": receipt_ref,
                "receipt_ref": receipt_ref,
                "error_code": "",
                "retry_of": ""
            }
        }]

        success, err = self.write_batch(payload)
        if not success:
            results["stages"]["write"] = f"FAILED: {err}"
            return False, results
        results["stages"]["write"] = "PASS"

        # 3. Postcondition readback
        ok, err = self.validate_postconditions({"11_Runs": 1})
        if not ok:
            results["stages"]["postconditions"] = f"FAILED: {err}"
            return False, results
        results["stages"]["postconditions"] = "PASS"
        results["status"] = "PASS"
        return True, results

if __name__ == "__main__":
    adapter = GWSAdapter(receipt_dir="canary_receipts", mock_mode=False)
    success, res = adapter.run_canary()
    print(json.dumps(res, indent=2))
    if not success:
        sys.exit(1)
