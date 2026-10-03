from typing import Any, Dict
from .capability import CapabilityContract, EffectReceipt


def capability_inspect_executor(payload: Dict[str, Any], correlation_id: str) -> EffectReceipt:
    from .registry import CapabilityRegistry
    from .harness_list import register_harness_list

    registry = CapabilityRegistry()
    register_harness_list(registry)
    register_capability_inspect(registry)
    caps = registry.list_capabilities(surface_filter=payload.get("surface"))
    if payload.get("capability_id"):
        caps = [c for c in caps if c.capability_id == payload["capability_id"]]
    data = [{
        "capability_id": c.capability_id,
        "version": c.version,
        "domain_owner": c.domain_owner,
        "intent": c.intent,
        "authority": c.authority,
        "effect_class": c.effect_class,
        "supported_surfaces": c.supported_surfaces,
    } for c in caps]
    return EffectReceipt(
        capability_id="capability_inspect",
        correlation_id=correlation_id,
        observed_effect=f"Inspected {len(data)} capabilities",
        provenance="Agent OS Capability Registry",
        status="SUCCESS",
        evidence_refs=["capability_registry_query"],
        data={"capabilities": data},
    )


def register_capability_inspect(registry):
    registry.register(CapabilityContract(
        capability_id="capability_inspect",
        version="1.0",
        domain_owner="Agent OS",
        intent="Inspect registered Agent OS shared capabilities and contracts",
        input_schema={"type":"object","properties":{"capability_id":{"type":"string"},"surface":{"type":"string"}}},
        output_schema={"type":"object"},
        authority="Agent OS Projection",
        effect_class="QUERY",
        supported_surfaces=["cli","api","mcp","harness","browser_bridge"],
        executor=capability_inspect_executor,
    ))
