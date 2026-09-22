import importlib

class IntelligenceRouter:
    def __init__(self):
        self.needle_module = None
        for module_name in ['cactus_needle3', 'needle3']:
            try:
                self.needle_module = importlib.import_module(module_name)
                break
            except ImportError:
                continue

    def route(self, capability, *args, **kwargs):
        if capability == 'DECIDE':
            evidence = kwargs.get('evidence')
            if not evidence:
                raise PermissionError("DECIDE capability requires explicit evidence")

        if not self.needle_module:
            raise RuntimeError("Cactus Needle 3 adapter not found")

        if not hasattr(self.needle_module, capability.lower()):
            raise NotImplementedError(f"Capability {capability} is not supported by the adapter")

        func = getattr(self.needle_module, capability.lower())

        return func(*args, **kwargs)

    def extract(self, *args, **kwargs):
        return self.route('EXTRACT', *args, **kwargs)

    def act(self, *args, **kwargs):
        return self.route('ACT', *args, **kwargs)

    def embed(self, *args, **kwargs):
        return self.route('EMBED', *args, **kwargs)

    def decide(self, *args, **kwargs):
        return self.route('DECIDE', *args, **kwargs)
