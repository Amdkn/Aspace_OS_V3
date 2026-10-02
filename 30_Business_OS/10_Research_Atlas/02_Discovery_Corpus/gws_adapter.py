import json
from pathlib import Path
from typing import List, Dict, Any

class GWSAdapter:
    def __init__(self, mock_mode: bool = False):
        self.mock_mode = mock_mode

    def write_batch(self, payloads: List[Dict[str, Any]], out_dir: str) -> None:
        if self.mock_mode:
            # Replicate the previous behavior (for tests/CI)
            gws_payloads_path = Path(out_dir) / "gws_payloads.json"
            with open(gws_payloads_path, 'w', encoding='utf-8') as f:
                json.dump(payloads, f, indent=2, ensure_ascii=False)
            print(f"[Discovery] GWS Payloads dumped to {gws_payloads_path}")
        else:
            # Here it would connect to GWS CLI for authenticated batch writes
            raise NotImplementedError("GWS CLI integration is not yet fully implemented for real runs.")
