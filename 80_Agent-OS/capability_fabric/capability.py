from typing import Dict, Any, Callable, List, Optional
from dataclasses import dataclass, field
import datetime

@dataclass
class ToolContext:
    user_id: Optional[str] = None
    tenant_id: Optional[str] = None
    session_id: Optional[str] = None
    correlation_id: Optional[str] = None
    surface: str = "cli"
    permissions: List[str] = field(default_factory=list)

@dataclass
class ToolResult:
    status: str
    observed_effect: str
    data: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None

@dataclass
class EffectReceipt:
    capability_id: str
    correlation_id: str
    observed_effect: str
    provenance: str
    status: str
    observed_at: str = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat())
    evidence_refs: List[str] = field(default_factory=list)
    data: Dict[str, Any] = field(default_factory=dict)

@dataclass
class CapabilityContract:
    capability_id: str
    version: str
    domain_owner: str
    intent: str
    input_schema: Dict[str, Any]
    output_schema: Dict[str, Any]
    authority: str
    effect_class: str # QUERY | COMMAND | EVENT
    supported_surfaces: List[str]
    executor: Callable[[Dict[str, Any], str], EffectReceipt]

def define_tool(
    capability_id: str,
    intent: str,
    domain_owner: str,
    executor_fn: Callable[[Dict[str, Any], ToolContext], ToolResult],
    version: str = "1.0",
    input_schema: Optional[Dict[str, Any]] = None,
    output_schema: Optional[Dict[str, Any]] = None,
    authority: str = "Domain Policy",
    effect_class: str = "QUERY",
    supported_surfaces: Optional[List[str]] = None
) -> CapabilityContract:
    """
    Business OS 'defineTool' equivalent adapted for shared Agent OS Capability Fabric.
    Wraps domain executor functions into canonical CapabilityContract with automatic EffectReceipt handling.
    """
    surfaces = supported_surfaces or ["cli", "api", "mcp", "harness", "skill", "in_app"]
    inp_schema = input_schema or {"type": "object", "properties": {}}
    out_schema = output_schema or {"type": "object", "properties": {}}

    def wrapped_executor(payload: Dict[str, Any], correlation_id: str) -> EffectReceipt:
        ctx = ToolContext(correlation_id=correlation_id)
        try:
            res = executor_fn(payload, ctx)
            return EffectReceipt(
                capability_id=capability_id,
                correlation_id=correlation_id,
                observed_effect=res.observed_effect,
                provenance=f"{domain_owner} / {capability_id}",
                status=res.status,
                data=res.data
            )
        except Exception as e:
            return EffectReceipt(
                capability_id=capability_id,
                correlation_id=correlation_id,
                observed_effect=f"Execution error: {str(e)}",
                provenance=f"{domain_owner} / {capability_id}",
                status="FAILED",
                data={"error": str(e)}
            )

    return CapabilityContract(
        capability_id=capability_id,
        version=version,
        domain_owner=domain_owner,
        intent=intent,
        input_schema=inp_schema,
        output_schema=out_schema,
        authority=authority,
        effect_class=effect_class,
        supported_surfaces=surfaces,
        executor=wrapped_executor
    )
