from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Literal, Optional

EffectClass = Literal["QUERY", "COMMAND", "EVENT"]

@dataclass
class CapabilityContract:
    capability_id: str
    version: str
    domain_owner: str
    intent: str
    input_schema: Dict[str, Any]
    output_schema: Dict[str, Any]
    authority: str
    effect_class: EffectClass
    idempotency: bool
    compensation: Optional[str]
    evidence_required: bool
    freshness: str
    supported_surfaces: List[str]
    runtime_bindings: List[str]
    effect_receipt: Optional[str]

    executor: Callable = None

    def validate_input(self, inputs: Dict[str, Any]) -> bool:
        # Simplified validation. In real-world, we'd use jsonschema or Pydantic.
        for key in self.input_schema.get("required", []):
            if key not in inputs:
                raise ValueError(f"Missing required field: {key}")
        return True

    def execute(self, inputs: Dict[str, Any], context: Dict[str, Any]) -> Any:
        self.validate_input(inputs)

        # Here we would also perform authority/permission checks, but for the MVP
        # we will assume the adapter has properly authenticated the context.

        if not self.executor:
            raise NotImplementedError(f"Capability {self.capability_id} has no executor configured.")

        return self.executor(inputs, context)
