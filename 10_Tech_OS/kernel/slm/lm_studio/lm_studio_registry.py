import time
import json
import logging
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

class LMStudioRegistry:
    def __init__(self, base_url="http://localhost:1234/v1"):
        self.base_url = base_url
        self.ttl = 300 # 5 minutes default TTL
        self.loaded_models = {}

    def get_available_models(self):
        try:
            req = Request(f"{self.base_url}/models", method="GET")
            with urlopen(req) as response:
                data = json.loads(response.read().decode())
                return data.get("data", [])
        except (URLError, HTTPError) as e:
            logging.error(f"Error fetching models: {e}")
            return None

    def load_model(self, model_id):
        try:
            data = json.dumps({"model": model_id}).encode('utf-8')
            req = Request(f"{self.base_url}/models", data=data, method="POST")
            req.add_header('Content-Type', 'application/json')
            with urlopen(req) as response:
                pass
            logging.info(f"Loaded model: {model_id}")
            self.loaded_models[model_id] = time.time()
            return True
        except (URLError, HTTPError) as e:
            logging.error(f"Error loading model {model_id}: {e}")
            return False

    def unload_model(self, model_id):
        try:
            data = json.dumps({"model": model_id}).encode('utf-8')
            req = Request(f"{self.base_url}/unload", data=data, method="POST")
            req.add_header('Content-Type', 'application/json')
            with urlopen(req) as response:
                pass
            logging.info(f"Unloaded model: {model_id}")
            if model_id in self.loaded_models:
                del self.loaded_models[model_id]
            return True
        except (URLError, HTTPError) as e:
            logging.error(f"Error unloading model {model_id}: {e}")
            return False

    def enforce_ttl(self):
        current_time = time.time()
        for model_id, load_time in list(self.loaded_models.items()):
            if current_time - load_time > self.ttl:
                logging.info(f"Model {model_id} TTL expired. Unloading...")
                self.unload_model(model_id)

    def update_model_access(self, model_id):
        if model_id in self.loaded_models:
            self.loaded_models[model_id] = time.time()

    def get_health(self):
        models = self.get_available_models()
        if models is None:
            return {
                "status": "unhealthy",
                "available_models": 0,
                "loaded_models": len(self.loaded_models),
                "resource_estimate_gb": 0
            }

        # Basic resource estimation (dummy calculation for now as it depends on API response)
        resource_estimate = len(models) * 4 # Assuming 4GB per model roughly

        return {
            "status": "healthy",
            "available_models": len(models),
            "loaded_models": len(self.loaded_models),
            "resource_estimate_gb": resource_estimate
        }
