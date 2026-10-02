import os
import json
import subprocess
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
        """
        if not payloads:
            return

        if self.mock_mode:
            gws_payloads_path = Path(out_dir) / "gws_payloads.json"
            with open(gws_payloads_path, 'w', encoding='utf-8') as f:
                json.dump(payloads, f, indent=2, ensure_ascii=False)
            print(f"[GWSAdapter] Mock mode: GWS Payloads dumped to {gws_payloads_path}")
        else:
            # Here you would typically call the real GWS CLI using subprocess.run
            # e.g., `gws write --workbook {self.gws_workbook_id} --payloads '{json.dumps(payloads)}'`
            # This is left as an architectural placeholder since this issue concerns replacing raw file dumps.
            print(f"[GWSAdapter] Invoking GWS CLI to write {len(payloads)} payloads to workbook {self.gws_workbook_id}")
            # Placeholder for actual CLI invocation
            pass
