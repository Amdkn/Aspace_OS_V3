import json
import os
from typing import Dict, Any
from .capability import CapabilityContract, EffectReceipt

def capability_inspect_executor(payload: Dict[str, Any], correlation_id: str) -> EffectReceipt:
    # Notice: capability_inspect is an Agent OS shared QUERY capability
    # Payload may filter by capability_id or surface
    capability_id_filter = payload.get("capability_id")
    surface_filter = payload.get("surface")

    # Import registry from parent or context if available, or build dynamic snapshot
    from .registry import CapabilityRegistry
    from .harness_list import register_harness_list

    registry = CapabilityRegistry()
    register_harness_list(registry)
    register_capability_inspect(registry)

    capabilities = registry.list_capabilities(surface_filter=surface_filter)

    if capability_id_filter:
        capabilities = [cap for cap in capabilities if cap.capability_id == capability_id_filter]

    inspected = []
    for cap in capabilities:
        inspected.append({
            "capability_id": cap.capability_id,
            "version": cap.version,
            "domain_owner": cap.domain_owner,
            "intent": cap.intent,
            "authority": cap.authority,
            "effect_class": cap.effect_class,
            "supported_surfaces": cap.supported_surfaces,
            "input_schema": cap.input_schema,
            "output_schema": cap.output_schema,
        })

    observed_effect = f"Inspected {len(inspected)} capabilities"
    if capability_id_filter:
        observed_effect += f" matching id '{capability_id_filter}'"
    if surface_filter:
        observed_effect += f" supporting surface '{surface_filter}'"

    return EffectReceipt(
        capability_id="capability_inspect",
        correlation_id=correlation_id,
        observed_effect=observed_effect,
        provenance="Agent OS Capability Registry",
        status="SUCCESS",
        evidence_refs=["capability_registry_query"],
        data={"capabilities": inspected}
    )

def register_capability_inspect(registry):
    contract = CapabilityContract(
        capability_id="capability_inspect",
        version="1.0",
        domain_owner="Agent OS",
        intent="Inspect registered Agent OS shared capabilities and contracts",
        input_schema={
            "type": "object",
            "properties": {
                "capability_id": {"type": "string"},
                "surface": {"type": "string"}
            }
        },
        output_schema={
            "type": "object",
            "properties": {
                "capabilities": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "capability_id": {"type": "string"},
                            "version": {"type": "string"},
                            "domain_owner": {"type": "string"},
                            "intent": {"type": "string"},
                            "authority": {"type": "string"},
                            "effect_class": {"type": "string"},
                            "supported_surfaces": {
                                "type": "array",
                                "items": {"type": "string"}
                            }
                        }
                    }
                }
            }
        },
        authority="Agent OS Projection",
        effect_class="QUERY",
        supported_surfaces=["cli", "api", "mcp", "harness", "browser_bridge"],
        executor=capability_inspect_executor
    )
    registry.register(contract)
