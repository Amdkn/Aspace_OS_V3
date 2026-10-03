from typing import Dict, Any, List
import uuid
import datetime
import json
import os
import importlib
from pathlib import Path

# Import from Agent OS capability fabric via importlib due to numeric directory names in python imports
capability_module = importlib.import_module("80_Agent-OS.capability_fabric.capability")
CapabilityContract = capability_module.CapabilityContract
EffectReceipt = capability_module.EffectReceipt

registry_module = importlib.import_module("80_Agent-OS.capability_fabric.registry")
CapabilityRegistry = registry_module.CapabilityRegistry

def gtd_inbox_capture_executor(payload: Dict[str, Any], correlation_id: str) -> EffectReceipt:
    title = payload.get("title")
    category = payload.get("category", "INBOX")
    context = payload.get("context", "General")

    if not title:
        raise ValueError("GTD Inbox item title is required.")

    # Record item locally into Life OS GTD Inbox state
    inbox_dir = Path("20_Life_OS/25_GTD_Cerritos/01_Inbox_Mariner")
    inbox_dir.mkdir(parents=True, exist_ok=True)
    inbox_file = inbox_dir / "inbox_items.json"

    items = []
    if inbox_file.exists():
        try:
            with open(inbox_file, "r", encoding="utf-8") as f:
                items = json.load(f)
        except Exception:
            items = []

    item_id = str(uuid.uuid4())
    captured_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    new_item = {
        "item_id": item_id,
        "title": title,
        "category": category,
        "context": context,
        "captured_at": captured_at,
        "correlation_id": correlation_id
    }
    items.append(new_item)

    with open(inbox_file, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

    return EffectReceipt(
        capability_id="life_gtd_inbox_capture",
        correlation_id=correlation_id,
        observed_effect=f"Captured GTD item '{title}' in category '{category}'",
        provenance="20_Life_OS/25_GTD_Cerritos/01_Inbox_Mariner",
        status="SUCCESS",
        evidence_refs=[str(inbox_file)],
        data={"item": new_item}
    )

def life_wheel_sync_executor(payload: Dict[str, Any], correlation_id: str) -> EffectReceipt:
    scores = payload.get("scores", {}) # e.g., {"health": 8, "career": 7, "finance": 9}
    if not scores:
        raise ValueError("Life Wheel scores dictionary is required.")

    wheel_dir = Path("20_Life_OS/22_Wheel_Discovery")
    wheel_dir.mkdir(parents=True, exist_ok=True)
    wheel_file = wheel_dir / "wheel_state.json"

    wheel_data = {
        "last_updated": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "correlation_id": correlation_id,
        "scores": scores
    }

    with open(wheel_file, "w", encoding="utf-8") as f:
        json.dump(wheel_data, f, indent=2, ensure_ascii=False)

    return EffectReceipt(
        capability_id="life_wheel_sync",
        correlation_id=correlation_id,
        observed_effect=f"Synchronized Life Wheel scores across {len(scores)} dimensions",
        provenance="20_Life_OS/22_Wheel_Discovery",
        status="SUCCESS",
        evidence_refs=[str(wheel_file)],
        data=wheel_data
    )

def register_life_capabilities(registry: CapabilityRegistry) -> None:
    gtd_cap = CapabilityContract(
        capability_id="life_gtd_inbox_capture",
        version="1.0.0",
        domain_owner="20_Life_OS/25_GTD_Cerritos",
        intent="Capture unprocessed item into Life OS GTD Inbox",
        input_schema={
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "category": {"type": "string"},
                "context": {"type": "string"}
            },
            "required": ["title"]
        },
        output_schema={
            "type": "object",
            "properties": {
                "item": {"type": "object"}
            }
        },
        authority="A1_Mariner_Capture",
        effect_class="COMMAND",
        supported_surfaces=["mcp", "api", "cli", "skill", "in_app", "harness"],
        executor=gtd_inbox_capture_executor
    )
    registry.register(gtd_cap)

    wheel_cap = CapabilityContract(
        capability_id="life_wheel_sync",
        version="1.0.0",
        domain_owner="20_Life_OS/22_Wheel_Discovery",
        intent="Sync Life Wheel dimension assessment scores",
        input_schema={
            "type": "object",
            "properties": {
                "scores": {"type": "object"}
            },
            "required": ["scores"]
        },
        output_schema={
            "type": "object",
            "properties": {
                "scores": {"type": "object"},
                "last_updated": {"type": "string"}
            }
        },
        authority="A2_Wheel_Discovery",
        effect_class="COMMAND",
        supported_surfaces=["mcp", "api", "cli", "skill", "in_app", "harness"],
        executor=life_wheel_sync_executor
    )
    registry.register(wheel_cap)
