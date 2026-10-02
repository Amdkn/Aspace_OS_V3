from typing import Dict, Any, Callable, List
from dataclasses import dataclass, field
import datetime

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
