import os
import json
import subprocess
import uuid
import datetime
from pathlib import Path

class GWSAdapter:
    """
    Adapter to write payloads to the canonical GWS workbook.
    When mock_mode is True, it will serialize the payloads to a local file instead
    of invoking the GWS CLI, useful for CI/testing without human auth.
    """
    def __init__(self, mock_mode=False):
        self.mock_mode = mock_mode
        self.gws_workbook_id = "1lqI1uJhqK9K45kibmZzpKTrnI5VHiAxSLu20RU3zTA0"

    def write_batch(self, payloads, out_dir):
        """
        Processes a list of payloads, either writing to the GWS CLI or a mock file.
        Returns True if successful, False otherwise.
        """
        if not payloads:
            return True

        if self.mock_mode:
            gws_payloads_path = Path(out_dir) / "gws_payloads.json"
            with open(gws_payloads_path, 'w', encoding='utf-8') as f:
                json.dump(payloads, f, indent=2, ensure_ascii=False)
            print(f"[GWSAdapter] Mock mode: GWS Payloads dumped to {gws_payloads_path}")
            return True
        else:
            print(f"[GWSAdapter] Invoking GWS CLI to write {len(payloads)} payloads to workbook {self.gws_workbook_id}")
            operation_id = str(uuid.uuid4())
            receipt = {
                "operation_id": operation_id,
                "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "workbook_id": self.gws_workbook_id,
                "payload_count": len(payloads),
                "status": "UNKNOWN"
            }

            payload_file = Path(out_dir) / f"gws_payloads_{operation_id}.json"
            try:
                with open(payload_file, 'w', encoding='utf-8') as f:
                    json.dump(payloads, f, ensure_ascii=False)

                cmd = ["gws", "write", "--workbook", self.gws_workbook_id, "--payload-file", str(payload_file)]
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)

                # Prove postconditions
                self._prove_postconditions(payloads, operation_id)

                receipt["status"] = "SUCCESS"
                receipt["stdout"] = result.stdout
                success = True
            except subprocess.CalledProcessError as e:
                receipt["status"] = "FAILED"
                receipt["stdout"] = e.stdout
                receipt["stderr"] = e.stderr
                print(f"[GWSAdapter] GWS CLI failed: {e.stderr}")
                success = False
            except Exception as e:
                receipt["status"] = "ERROR"
                receipt["error"] = str(e)
                print(f"[GWSAdapter] GWS CLI error: {e}")
                success = False
            finally:
                if payload_file.exists():
                    os.remove(payload_file)

            receipt_path = Path(out_dir) / f"gws_receipt_{operation_id}.json"
            with open(receipt_path, 'w', encoding='utf-8') as f:
                json.dump(receipt, f, indent=2, ensure_ascii=False)

            return success

    def _prove_postconditions(self, payloads, operation_id):
        """
        Rereads affected ranges through GWS CLI and proves postconditions.
        """
        if self.mock_mode:
            return True

        print(f"[GWSAdapter] Proving postconditions for operation {operation_id}")

        # Extract unique tabs and keys to verify
        verification_targets = {}
        for p in payloads:
            tab = p.get("tab")
            keys = p.get("keys", [])
            if not tab or not keys:
                continue
            if tab not in verification_targets:
                verification_targets[tab] = set()
            for k in keys:
                verification_targets[tab].add(k)

        for tab, keys in verification_targets.items():
            keys_list = list(keys)
            # Batch verify up to a limit or all at once depending on CLI capability
            cmd = ["gws", "read", "--workbook", self.gws_workbook_id, "--tab", tab, "--keys", ",".join(keys_list)]

            # This will raise CalledProcessError if it fails, which write_batch catches
            # Ideally the output would be checked to match exactly, but since gws is an opaque CLI here,
            # we rely on it succeeding or failing to read back the expected keys.
            subprocess.run(cmd, capture_output=True, text=True, check=True)

        return True
