from typing import Any, Dict, List, Optional

class IntelligenceRouter:
    """
    Integrates Cactus Needle 3 as native local capability interfaces.
    Prefers EXTRACT/ACT/EMBED and only exposes DECIDE if evidence justifies it.
    Preserves fail-closed authority boundary.
    """

    def __init__(self):
        self.base_capabilities = ["EXTRACT", "ACT", "EMBED"]

    def discover_capabilities(self, evidence: Optional[Dict[str, Any]] = None) -> List[str]:
        """
        Runtime discovery of available capabilities.
        DECIDE is only available if evidence is provided and justifies it.
        """
        caps = list(self.base_capabilities)
        if evidence is not None and self._validate_evidence(evidence):
            caps.append("DECIDE")
        return caps

    def _validate_evidence(self, evidence: Dict[str, Any]) -> bool:
        """
        Simple validation logic to justify DECIDE capability.
        Requires valid justification evidence.
        """
        return evidence.get("justified", False) is True

    def route(self, capability: str, params: Dict[str, Any], evidence: Optional[Dict[str, Any]] = None) -> Any:
        """
        Routes the capability request. Enforces fail-closed authority boundary.
        """
        available_caps = self.discover_capabilities(evidence)
        if capability not in available_caps:
            raise PermissionError(f"Capability {capability} denied. Fail-closed authority boundary enforced.")

        if capability == "EXTRACT":
            return self._handle_extract(params)
        elif capability == "ACT":
            return self._handle_act(params)
        elif capability == "EMBED":
            return self._handle_embed(params)
        elif capability == "DECIDE":
            return self._handle_decide(params)
        else:
            raise ValueError(f"Unknown capability: {capability}")

    def _handle_extract(self, params: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "extracted", "data": params}

    def _handle_act(self, params: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "acted", "data": params}

    def _handle_embed(self, params: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "embedded", "data": params}

    def _handle_decide(self, params: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "decided", "data": params}
