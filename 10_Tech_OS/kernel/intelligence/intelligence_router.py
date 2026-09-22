import sys
import importlib

class IntelligenceRouter:
    """
    IntelligenceRouter integrates local capability interfaces.
    Uses Cactus Needle 3 for EXTRACT, ACT, and EMBED.
    DECIDE capability requires evidence justification (fail-closed).
    """
    def __init__(self):
        self.needle = None
        self._discover_needle()

    def _discover_needle(self):
        # Runtime discovery of Cactus Needle 3
        # Attempt to import "cactus_needle3" or "needle3"
        try:
            self.needle = importlib.import_module("cactus_needle3")
        except ImportError:
            try:
                self.needle = importlib.import_module("needle3")
            except ImportError:
                # Mock or test implementation might be provided later or runtime warning
                pass

    def extract(self, *args, **kwargs):
        if self.needle and hasattr(self.needle, "extract"):
            return self.needle.extract(*args, **kwargs)
        raise NotImplementedError("Needle 3 EXTRACT capability not available or not installed")

    def act(self, *args, **kwargs):
        if self.needle and hasattr(self.needle, "act"):
            return self.needle.act(*args, **kwargs)
        raise NotImplementedError("Needle 3 ACT capability not available or not installed")

    def embed(self, *args, **kwargs):
        if self.needle and hasattr(self.needle, "embed"):
            return self.needle.embed(*args, **kwargs)
        raise NotImplementedError("Needle 3 EMBED capability not available or not installed")

    def decide(self, *args, evidence=None, **kwargs):
        """
        DECIDE capability is strictly fail-closed.
        Must provide explicit evidence justification to be exposed.
        """
        if not evidence:
            raise PermissionError("DECIDE capability is fail-closed and requires explicit evidence justification.")

        if self.needle and hasattr(self.needle, "decide"):
            return self.needle.decide(*args, evidence=evidence, **kwargs)
        raise NotImplementedError("Needle 3 DECIDE capability not available or not installed")
