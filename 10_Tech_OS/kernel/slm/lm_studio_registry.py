import urllib.request
import urllib.error
import json
import time

class LMStudioRegistry:
    def __init__(self, base_url="http://127.0.0.1:1234", max_ram_mb=8192):
        self.base_url = base_url
        self.loaded_models = {}
        self.max_ram_mb = max_ram_mb

    def _request(self, method, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        req = urllib.request.Request(url, method=method)
        if data:
            req.add_header('Content-Type', 'application/json')
            req.data = json.dumps(data).encode('utf-8')
        try:
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode())
        except urllib.error.URLError as e:
            return {"error": str(e)}

    def discover_models(self):
        res = self._request("GET", "/v1/models")
        if "data" in res:
            return res["data"]
        return res

    def estimate_resource_usage(self, model_id):
        # A simple estimation mockup for resource usage.
        # In reality this might interrogate the API or model metadata.
        # Here we mock a simple fixed estimation.
        return {"model": model_id, "estimated_ram_mb": 2048, "context_length": 8192}

    def can_load_model(self, model_id):
        estimation = self.estimate_resource_usage(model_id)
        current_ram = sum([self.estimate_resource_usage(m)["estimated_ram_mb"] for m in self.loaded_models])
        if current_ram + estimation["estimated_ram_mb"] > self.max_ram_mb:
            return False
        return True

    def load_model(self, model_id, ttl=3600):
        if not self.can_load_model(model_id):
            return {"error": "Resource policy violation: max RAM exceeded"}

        res = self._request("POST", "/v1/models/load", {"model": model_id})
        self.loaded_models[model_id] = {"load_time": time.time(), "ttl": ttl}
        return res

    def unload_model(self, model_id):
        res = self._request("POST", "/v1/models/unload", {"model": model_id})
        if model_id in self.loaded_models:
            del self.loaded_models[model_id]
        return res

    def enforce_ttl(self):
        current_time = time.time()
        unloaded = []
        for model_id, info in list(self.loaded_models.items()):
            if current_time - info["load_time"] > info["ttl"]:
                self.unload_model(model_id)
                unloaded.append(model_id)
        return unloaded

    def health_check(self):
        res = self._request("GET", "/v1/models")
        if "error" not in res:
            return True
        return False
