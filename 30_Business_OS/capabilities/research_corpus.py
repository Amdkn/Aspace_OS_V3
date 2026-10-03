from typing import Dict, Any
import importlib
capability_module = importlib.import_module("80_Agent-OS.capability_fabric.capability")
define_tool = capability_module.define_tool
ToolContext = capability_module.ToolContext
ToolResult = capability_module.ToolResult

def business_research_executor(payload: Dict[str, Any], ctx: ToolContext) -> ToolResult:
    """
    Business OS domain execution logic for research corpus analysis.
    Maintains Business OS domain ownership while consuming shared Capability Fabric.
    """
    topic = payload.get("topic", "general_business")
    depth = payload.get("depth", 1)

    return ToolResult(
        status="SUCCESS",
        observed_effect=f"Executed Business OS research synthesis on topic '{topic}' (depth: {depth})",
        data={
            "domain_owner": "Business OS",
            "topic": topic,
            "depth": depth,
            "findings": [
                f"Business insight 1 regarding {topic}",
                f"Business insight 2 regarding {topic}"
            ]
        }
    )

BUSINESS_RESEARCH_CAPABILITY = define_tool(
    capability_id="business_research_corpus",
    intent="Analyze and synthesize business research topics in Research Atlas",
    domain_owner="Business OS",
    executor_fn=business_research_executor,
    version="1.0",
    input_schema={
        "type": "object",
        "properties": {
            "topic": {"type": "string"},
            "depth": {"type": "integer"}
        }
    },
    output_schema={
        "type": "object",
        "properties": {
            "findings": {"type": "array", "items": {"type": "string"}}
        }
    },
    authority="Business OS Strategy Policy",
    effect_class="QUERY",
    supported_surfaces=["mcp", "api", "cli", "harness", "skill"]
)

def register_business_capabilities(registry):
    registry.register(BUSINESS_RESEARCH_CAPABILITY)
