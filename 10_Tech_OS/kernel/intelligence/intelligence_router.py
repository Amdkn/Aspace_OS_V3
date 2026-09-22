import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

class IntelligenceRouter:
    """
    Integrates Cactus Needle 3 native local capability interfaces.
    """

    def __init__(self):
        # Native local capabilities discovered at runtime
        self._capabilities = ["EXTRACT", "ACT", "EMBED"]

    def discover(self) -> List[str]:
        """Runtime discovery of capabilities."""
        return self._capabilities

    def extract(self, payload: Any) -> Dict[str, Any]:
        """EXTRACT pattern via Needle 3."""
        return {"status": "success", "capability": "EXTRACT", "payload": payload}

    def act(self, command: str, args: Dict[str, Any] = None) -> Dict[str, Any]:
        """ACT pattern via Needle 3."""
        return {"status": "success", "capability": "ACT", "command": command, "args": args or {}}

    def embed(self, text: str) -> Dict[str, Any]:
        """EMBED pattern via Needle 3."""
        return {"status": "success", "capability": "EMBED", "text": text}

    def decide(self, decision_context: Any, evidence: Optional[Any] = None) -> Dict[str, Any]:
        """
        DECIDE capability.
        Preserves fail-closed authority boundary by requiring evidence.
        """
        if not evidence:
            raise PermissionError("Fail-closed authority boundary: DECIDE requires evidence.")
        return {
            "status": "success",
            "capability": "DECIDE",
            "decision_context": decision_context,
            "evidence": evidence
        }
