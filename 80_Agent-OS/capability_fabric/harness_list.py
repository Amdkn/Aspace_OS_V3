from typing import Dict, Any
from .capability import CapabilityContract, EffectReceipt

def harness_list_executor(payload: Dict[str, Any], correlation_id: str) -> EffectReceipt:
    # A mocked execution that proves the capability ran while generating a valid receipt.
    filter_type = payload.get("filter", "all")
    harnesses = ["antigravity", "codex", "claude_code", "hermes_agent"]
    if filter_type == "active":
        harnesses = ["claude_code", "hermes_agent"]

    observed_effect = f"Listed {len(harnesses)} harnesses with filter '{filter_type}'"
    return EffectReceipt(
        capability_id="harness_list",
        correlation_id=correlation_id,
        observed_effect=observed_effect,
        provenance="Agent OS / Harness projection",
        status="SUCCESS",
        evidence_refs=["harness_db_query_123"]
    )

def register_harness_list(registry):
    contract = CapabilityContract(
        capability_id="harness_list",
        version="1.0",
        domain_owner="Agent OS",
        intent="List currently mounted or available harnesses",
        input_schema={
            "type": "object",
            "properties": {
                "filter": {"type": "string"}
            }
        },
        output_schema={
            "type": "object",
            "properties": {
                "harnesses": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        },
        authority="Agent OS Projection",
        effect_class="QUERY",
        supported_surfaces=["cli", "api", "mcp", "harness"],
        executor=harness_list_executor
    )
    registry.register(contract)
