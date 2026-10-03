from typing import Dict, Any, Optional
from .registry import CapabilityRegistry
from .adapters import AdapterBase

class GenericHarnessAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry, harness_id: str):
        super().__init__(registry, "harness")
        self.harness_id = harness_id

    def execute_harness_capability(self, capability_id: str, payload: Dict[str, Any], correlation_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Invokes a capability on behalf of a specific harness environment.
        Ensures harness uses the single shared CapabilityRegistry executor without duplication.
        """
        res = self.invoke(capability_id, payload, correlation_id)
        if res.get("status") == "SUCCESS" and "receipt" in res:
            res["receipt"]["provenance"] = f"Harness: {self.harness_id} / {res['receipt'].get('provenance', '')}"
            res["harness_id"] = self.harness_id
        return res

class ClaudeCodeHarnessAdapter(GenericHarnessAdapter):
    def __init__(self, registry: CapabilityRegistry):
        super().__init__(registry, "claude_code")

class CodexHarnessAdapter(GenericHarnessAdapter):
    def __init__(self, registry: CapabilityRegistry):
        super().__init__(registry, "codex")

class HermesHarnessAdapter(GenericHarnessAdapter):
    def __init__(self, registry: CapabilityRegistry):
        super().__init__(registry, "hermes")

class AntigravityHarnessAdapter(GenericHarnessAdapter):
    def __init__(self, registry: CapabilityRegistry):
        super().__init__(registry, "antigravity")

class JulesHarnessAdapter(GenericHarnessAdapter):
    def __init__(self, registry: CapabilityRegistry):
        super().__init__(registry, "jules")

class QwenHarnessAdapter(GenericHarnessAdapter):
    def __init__(self, registry: CapabilityRegistry):
        super().__init__(registry, "qwen_coder")
