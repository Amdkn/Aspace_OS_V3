"""intelligence_router.py - Route capabilities to Needle 3 using runtime discovery."""

import importlib

class IntelligenceRouter:
    """Native local capability interface adapter for Needle 3."""

    def __init__(self):
        self._needle = None
        self._load_adapter()

    def _load_adapter(self):
        """Discovers and loads the needle3 or cactus_needle3 package at runtime."""
        try:
            self._needle = importlib.import_module("cactus_needle3")
        except ImportError:
            try:
                self._needle = importlib.import_module("needle3")
            except ImportError:
                self._needle = None

    def extract(self, *args, **kwargs):
        """EXTRACT capability."""
        if not self._needle:
            raise RuntimeError("Needle 3 adapter is not installed.")
        return getattr(self._needle, "extract", lambda *a, **kw: None)(*args, **kwargs)

    def act(self, *args, **kwargs):
        """ACT capability."""
        if not self._needle:
            raise RuntimeError("Needle 3 adapter is not installed.")
        return getattr(self._needle, "act", lambda *a, **kw: None)(*args, **kwargs)

    def embed(self, *args, **kwargs):
        """EMBED capability."""
        if not self._needle:
            raise RuntimeError("Needle 3 adapter is not installed.")
        return getattr(self._needle, "embed", lambda *a, **kw: None)(*args, **kwargs)

    def decide(self, *args, **kwargs):
        """DECIDE capability. Enforces fail-closed authority boundary by requiring evidence."""
        if not self._needle:
            raise RuntimeError("Needle 3 adapter is not installed.")
        if "evidence" not in kwargs or not kwargs["evidence"]:
            raise PermissionError("DECIDE capability requires explicit evidence to be provided.")
        return getattr(self._needle, "decide", lambda *a, **kw: None)(*args, **kwargs)
