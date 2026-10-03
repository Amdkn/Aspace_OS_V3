import os
import json
import uuid
import datetime
import importlib
from pathlib import Path

gws_base_module = importlib.import_module("30_Business_OS.10_Research_Atlas.02_Discovery_Corpus.gws_adapter")
GWSAdapter = gws_base_module.GWSAdapter

cap_module = importlib.import_module("80_Agent-OS.capability_fabric.capability")
EffectReceipt = cap_module.EffectReceipt

class LifeGWSAdapter(GWSAdapter):
    """
    Life OS GWS Adapter for syncing Life OS GTD Inbox / Life Wheel items to GWS,
    capturing evidence and proving postconditions / readback.
    """
    def __init__(self, mock_mode=True):
        super().__init__(mock_mode=mock_mode)

    def sync_gtd_inbox_to_gws(self, inbox_items, out_dir="20_Life_OS/evidence"):
        out_path = Path(out_dir)
        out_path.mkdir(parents=True, exist_ok=True)

        payloads = []
        for item in inbox_items:
            payloads.append({
                "tab": "Life_GTD_Inbox",
                "keys": [item.get("item_id")],
                "data": {
                    "title": item.get("title"),
                    "category": item.get("category"),
                    "context": item.get("context"),
                    "captured_at": item.get("captured_at")
                }
            })

        success = self.write_batch(payloads, str(out_path))

        operation_id = str(uuid.uuid4())
        evidence_file = out_path / "life_gws_effect_receipt.json"

        receipt = EffectReceipt(
            capability_id="life_gws_sync",
            correlation_id=operation_id,
            observed_effect=f"Synced {len(payloads)} Life GTD items to GWS workbook {self.gws_workbook_id}",
            provenance="20_Life_OS/gws_life_adapter.py",
            status="SUCCESS" if success else "FAILED",
            evidence_refs=[str(evidence_file)],
            data={
                "workbook_id": self.gws_workbook_id,
                "payload_count": len(payloads),
                "mock_mode": self.mock_mode
            }
        )

        receipt_dict = {
            "capability_id": receipt.capability_id,
            "correlation_id": receipt.correlation_id,
            "observed_effect": receipt.observed_effect,
            "provenance": receipt.provenance,
            "status": receipt.status,
            "observed_at": receipt.observed_at,
            "evidence_refs": receipt.evidence_refs,
            "data": receipt.data
        }

        with open(evidence_file, "w", encoding="utf-8") as f:
            json.dump(receipt_dict, f, indent=2, ensure_ascii=False)

        return receipt
