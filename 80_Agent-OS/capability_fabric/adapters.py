from typing import Dict, Any, Optional
import uuid
import json
from .registry import CapabilityRegistry
from .harness_certification import HarnessCertificationEngine, CertificationError, get_harness_mesh_view

class AdapterBase:
    def __init__(self, registry: CapabilityRegistry, surface_name: str):
        self.registry = registry
        self.surface_name = surface_name

    def invoke(
        self,
        capability_id: str,
        payload: Dict[str, Any],
        correlation_id: Optional[str] = None,
        actor_id: Optional[str] = None,
        authority_envelope: Optional[str] = None
    ) -> Dict[str, Any]:
        capability = self.registry.get_capability(capability_id)
        if not capability:
            return {"status": "FAILED", "error": f"Capability {capability_id} not found."}

        if self.surface_name not in capability.supported_surfaces and self.surface_name != "harness":
            return {"status": "FAILED", "error": f"Surface {self.surface_name} not supported by {capability_id}."}

        corr_id = correlation_id or str(uuid.uuid4())

        try:
            receipt = capability.executor(payload, corr_id)
            res = {
                "status": receipt.status,
                "receipt": {
                    "capability_id": receipt.capability_id,
                    "correlation_id": receipt.correlation_id,
                    "observed_effect": receipt.observed_effect,
                    "provenance": receipt.provenance,
                    "observed_at": receipt.observed_at,
                    "evidence_refs": receipt.evidence_refs
                }
            }
            if receipt.data:
                res["data"] = receipt.data
            return res
        except Exception as e:
            return {"status": "UNKNOWN", "error": str(e)}


class CLIAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry):
        super().__init__(registry, "cli")


class APIAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry):
        super().__init__(registry, "api")


class MCPAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry):
        super().__init__(registry, "mcp")


class BrowserBridgeAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry):
        super().__init__(registry, "browser_bridge")


class HarnessMeshAdapter(AdapterBase):
    """Certified Harness Mesh Adapter enforcing external actor identity and 10-point contract checks."""

    def __init__(self, registry: CapabilityRegistry, harness_id: str = "hermes"):
        super().__init__(registry, "harness")
        self.harness_id = harness_id
        self.certification_engine = HarnessCertificationEngine()

    def invoke_certified(
        self,
        *,
        capability_id: str,
        payload: Dict[str, Any],
        actor_id: str,
        authority_envelope: str = "L2_EXECUTE",
        correlation_id: Optional[str] = None,
        runtime_id: str = "rt-sovereign-node-1",
        quota_budget: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        capability = self.registry.get_capability(capability_id)
        if not capability:
            return {"status": "FAILED", "error": f"Capability {capability_id} not found."}

        corr_id = correlation_id or str(uuid.uuid4())
        budget = quota_budget or {"quota": "100_tokens_or_requests", "latency_ms": 15, "reliability_score": 1.0, "cost_cents": 0}

        try:
            receipt = capability.executor(payload, corr_id)

            # 10-point certification validation
            cert_result = self.certification_engine.check_contract(
                harness_id=self.harness_id,
                actor_id=actor_id,
                capability_contract=capability,
                input_payload=payload,
                correlation_id=corr_id,
                authority_envelope=authority_envelope,
                receipt=receipt,
                quota_budget=budget,
                executor_func=capability.executor
            )

            # Structured Agent OS display separating identity, runtime, adapter, capability, budget, evidence
            mesh_view = get_harness_mesh_view(
                actor_id=actor_id,
                runtime_id=runtime_id,
                adapter_type="CertifiedHarnessMeshAdapter",
                harness_id=self.harness_id,
                capability_id=capability_id,
                budget=budget,
                evidence={
                    "observed_effect": receipt.observed_effect,
                    "evidence_refs": receipt.evidence_refs,
                    "provenance": receipt.provenance
                },
                correlation_id=corr_id
            )

            return {
                "status": receipt.status,
                "certification": cert_result,
                "mesh_view": mesh_view,
                "receipt": {
                    "capability_id": receipt.capability_id,
                    "correlation_id": receipt.correlation_id,
                    "observed_effect": receipt.observed_effect,
                    "provenance": receipt.provenance,
                    "observed_at": receipt.observed_at,
                    "evidence_refs": receipt.evidence_refs
                },
                "data": receipt.data
            }

        except CertificationError as ce:
            return {
                "status": "CERTIFICATION_FAILED",
                "harness_id": self.harness_id,
                "error": str(ce)
            }
        except Exception as e:
            return {"status": "UNKNOWN", "error": str(e)}
