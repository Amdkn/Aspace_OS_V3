import os
import json
import hashlib
from datetime import datetime, timezone

class GWSAdapter:
    """
    Mocked Google Workspace Sheets (GWS) Adapter for Workbook 1lqI1uJhqK9K45kibmZzpKTrnI5VHiAxSLu20RU3zTA0
    Implements 13 canonical tabs, deterministic row IDs, idempotent dedup, and local receipts.
    """
    WORKBOOK_ID = "1lqI1uJhqK9K45kibmZzpKTrnI5VHiAxSLu20RU3zTA0"

    CANONICAL_TABS = [
        "00_Control", "01_Channels", "02_Videos", "03_CitationCandidates",
        "04_Papers", "05_VideoPaperEdges", "06_PaperRelations", "07_Artifacts",
        "08_InnovationFeatures", "09_CapabilityCandidates", "10_ReviewQueue",
        "11_Runs", "12_Dashboard"
    ]

    def __init__(self, receipt_dir="gws_receipts"):
        self.receipt_dir = receipt_dir
        os.makedirs(self.receipt_dir, exist_ok=True)
        # In memory state of the workbook to simulate read/write postconditions
        self.workbook_state = {tab: {} for tab in self.CANONICAL_TABS}

    def generate_row_id(self, tab, keys):
        """Generate a deterministic row ID based on composite keys."""
        key_str = f"{tab}_{'_'.join(str(k) for k in keys)}"
        return hashlib.sha256(key_str.encode('utf-8')).hexdigest()[:16]

    def _save_local_receipt(self, batch_id, payload, result):
        """Durable local receipt for audit and recovery."""
        receipt = {
            "batch_id": batch_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "workbook": self.WORKBOOK_ID,
            "payload": payload,
            "result": result
        }
        receipt_path = os.path.join(self.receipt_dir, f"receipt_{batch_id}.json")
        with open(receipt_path, 'w', encoding='utf-8') as f:
            json.dump(receipt, f, indent=2)

    def write_batch(self, payloads):
        """
        Idempotent batch write across multiple tabs.
        Payloads: list of dicts: {"tab": "...", "keys": [...], "data": {...}}
        Returns success boolean and error details.
        """
        batch_id = datetime.now(timezone.utc).strftime("%Y%md%H%M%S")
        written_count = 0

        try:
            for item in payloads:
                tab = item.get("tab")
                if tab not in self.CANONICAL_TABS:
                    raise ValueError(f"Invalid tab {tab}")

                keys = item.get("keys", [])
                data = item.get("data", {})

                row_id = self.generate_row_id(tab, keys)
                data["_row_id"] = row_id

                # Idempotent: overwrite or ignore based on logic. We overwrite here.
                if row_id not in self.workbook_state[tab]:
                    written_count += 1

                self.workbook_state[tab][row_id] = data

            self._save_local_receipt(batch_id, payloads, {"status": "SUCCESS", "written": written_count})
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
            actual = len(self.workbook_state.get(tab, {}))
            if actual != expected:
                return False, f"Tab {tab} has {actual} rows, expected {expected}"
        return True, None
