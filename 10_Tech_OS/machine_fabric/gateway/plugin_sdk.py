from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class PluginError(Exception):
    """Base exception for plugin failures."""
    pass


class PluginContext:
    """Provides execution context to the plugin."""
    def __init__(self, operation_id: str, action: str, payload: Dict[str, Any]):
        self.operation_id = operation_id
        self.action = action
        self.payload = payload
        self.state: Dict[str, Any] = {}


class MockPluginContext(PluginContext):
    """A mock context for testing plugins."""
    def __init__(self, operation_id: str = "mock-op", action: str = "execute", payload: Optional[Dict[str, Any]] = None):
        super().__init__(operation_id, action, payload or {})
        self.log: List[str] = []

    def record_log(self, message: str):
        self.log.append(message)


class GatewayPlugin(ABC):
    """
    Base class for a Gateway Plugin.
    Provides typed hooks for inspecting, preparing, executing, observing, reconciling, and cleaning up operations.
    """

    @abstractmethod
    def manifest(self) -> Dict[str, Any]:
        """
        Returns the capability manifest, including:
        - capability_id (e.g., 'machine.plugin.demo')
        - version (e.g., '0.1.0')
        - permissions
        """
        pass

    @abstractmethod
    def health(self) -> Dict[str, Any]:
        """
        Returns the health contract of the plugin.
        Expected keys: 'aggregate' (e.g., 'ONLINE', 'DEGRADED', 'UNKNOWN'), 'detail'.
        """
        pass

    def inspect(self, payload: Dict[str, Any]) -> bool:
        """
        Inspects the payload to determine if it is valid for this plugin.
        Returns True if valid, False otherwise.
        """
        return True

    def prepare(self, context: PluginContext) -> None:
        """
        Prepares for execution (e.g., allocating resources, parsing payload).
        Can raise PluginError.
        """
        pass

    @abstractmethod
    def execute(self, context: PluginContext) -> Dict[str, Any]:
        """
        Executes the main operation.
        Returns a partial receipt dictionary (e.g., {"state": "SUCCEEDED", "evidence": {...}}).
        """
        pass

    def observe(self, context: PluginContext, partial_receipt: Dict[str, Any]) -> None:
        """
        Observes the result of the execution.
        Can mutate the receipt or record side effects.
        """
        pass

    def reconcile(self, context: PluginContext, receipt: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reconciles the execution state. Ensure the returned receipt is complete.
        """
        return receipt

    def cleanup(self, context: PluginContext) -> None:
        """
        Cleans up resources after execution, observation, and reconciliation.
        Executed even if an exception occurs in earlier steps.
        """
        pass
