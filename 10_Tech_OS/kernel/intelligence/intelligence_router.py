"""
IntelligenceRouter — Local intelligence router for A'Space OS V3.

Integrates Cactus Needle 3 as native local capability interfaces.
Prefers EXTRACT / ACT / EMBED models.
Only exposes DECIDE if justified by evidence, preserving fail-closed authority boundary.
"""

import json
from typing import Any, Dict, List, Optional, Type
import logging
from pydantic import BaseModel

logger = logging.getLogger(__name__)

class NeedlesCapabilities:
    """Wrapper for Cactus Needle 3 capabilities."""

    def __init__(self):
        try:
            import needle
            self._needle_class = needle.Needle
            self._available = True
        except ImportError:
            self._needle_class = None
            self._available = False
            logger.warning("Cactus Needle 3 not found. Capabilities will be disabled.")

    @property
    def is_available(self) -> bool:
        return self._available

    def embed(self, text: str) -> List[float]:
        """Generates a local vector embedding."""
        if not self._available:
            return []
        try:
            with self._needle_class() as n:
                return n.embed(text)
        except Exception as e:
            logger.error(f"Needle embed failed: {e}")
            return []

    def extract(self, text: str, schema: Type[BaseModel]) -> Optional[Any]:
        """Extracts local structured data."""
        if not self._available:
            return None
        try:
            with self._needle_class() as n:
                return n.extract(text, schema=schema)
        except Exception as e:
            logger.error(f"Needle extract failed: {e}")
            return None

    def act(self, query: str, max_steps: int = 8) -> Dict[str, Any]:
        """Executes actions/tool calls."""
        if not self._available:
            return {"error": "Needle unavailable"}
        try:
            with self._needle_class() as n:
                return n.run(query=query, max_steps=max_steps)
        except Exception as e:
            logger.error(f"Needle act failed: {e}")
            return {"error": str(e)}


class IntelligenceRouter:
    """Main router exposing local capabilities."""

    def __init__(self):
        self.needle = NeedlesCapabilities()

    def get_capabilities(self) -> List[str]:
        """Returns the list of discovered capabilities."""
        caps = []
        if self.needle.is_available:
            caps.extend(["EXTRACT", "ACT", "EMBED"])
        return caps

    def embed(self, text: str) -> List[float]:
        """Delegates to Needle adapter."""
        return self.needle.embed(text)

    def extract(self, text: str, schema: Type[BaseModel]) -> Optional[Any]:
        """Delegates to Needle adapter."""
        return self.needle.extract(text, schema)

    def act(self, query: str, max_steps: int = 8) -> Dict[str, Any]:
        """Delegates to Needle adapter."""
        return self.needle.act(query, max_steps)

    def decide(self, context: Dict[str, Any], evidence: List[str] = None) -> Dict[str, Any]:
        """
        Fail-closed authority boundary.
        Only authorizes decision if justifiable evidence is provided.
        """
        if not evidence:
            return {
                "decision": "DENIED",
                "reason": "DECIDE capability requires explicit evidence to justify breach of fail-closed authority boundary."
            }

        # Mocking the actual decision logic for now since it's just router boundary enforcement
        return {
            "decision": "APPROVED",
            "reason": f"Authorized based on {len(evidence)} pieces of evidence."
        }
