import importlib

class IntelligenceRouter:
    def __init__(self):
        self._needle_module = None
        for module_name in ["cactus_needle3", "needle3"]:
            try:
                self._needle_module = importlib.import_module(module_name)
                break
            except ImportError:
                continue

    def extract(self, *args, **kwargs):
        if not self._needle_module:
            raise RuntimeError("Needle 3 capability adapter not installed")
        if hasattr(self._needle_module, 'EXTRACT'):
            return self._needle_module.EXTRACT(*args, **kwargs)
        return getattr(self._needle_module, 'extract')(*args, **kwargs)

    def act(self, *args, **kwargs):
        if not self._needle_module:
            raise RuntimeError("Needle 3 capability adapter not installed")
        if hasattr(self._needle_module, 'ACT'):
            return self._needle_module.ACT(*args, **kwargs)
        return getattr(self._needle_module, 'act')(*args, **kwargs)

    def embed(self, *args, **kwargs):
        if not self._needle_module:
            raise RuntimeError("Needle 3 capability adapter not installed")
        if hasattr(self._needle_module, 'EMBED'):
            return self._needle_module.EMBED(*args, **kwargs)
        return getattr(self._needle_module, 'embed')(*args, **kwargs)

    def decide(self, *args, evidence=None, **kwargs):
        if not evidence:
            raise PermissionError("DECIDE capability requires explicit evidence")
        if not self._needle_module:
            raise RuntimeError("Needle 3 capability adapter not installed")
        if hasattr(self._needle_module, 'DECIDE'):
            return self._needle_module.DECIDE(*args, evidence=evidence, **kwargs)
        return getattr(self._needle_module, 'decide')(*args, evidence=evidence, **kwargs)
