from typing import Any, Dict

from plugin_sdk import GatewayPlugin, PluginContext


class DemoPingPlugin(GatewayPlugin):
    """
    A simple demo plugin that replies to a ping payload to verify the plugin SDK execution flow.
    """
    
    def manifest(self) -> Dict[str, Any]:
        return {
            "capability_id": "machine.demo.ping",
            "version": "1.0.0",
            "permissions": ["loopback daemon"],
            "description": "Demo plugin for testing plugin routing."
        }
        
    def health(self) -> Dict[str, Any]:
        return {
            "aggregate": "ONLINE",
            "detail": "Demo plugin is alive."
        }
        
    def inspect(self, payload: Dict[str, Any]) -> bool:
        # Requires an explicit ping message
        return payload.get("message") == "ping"
        
    def execute(self, context: PluginContext) -> Dict[str, Any]:
        return {
            "state": "SUCCEEDED",
            "evidence": {
                "message": "pong",
                "received_operation": context.operation_id
            }
        }
