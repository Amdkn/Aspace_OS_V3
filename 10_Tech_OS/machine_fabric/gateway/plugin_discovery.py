import importlib.util
import inspect
import logging
import os
import sys
from typing import Dict, List, Type

from machine_fabric.gateway.plugin_sdk import GatewayPlugin


logger = logging.getLogger(__name__)


def discover_plugins(plugin_dir: str) -> Dict[str, GatewayPlugin]:
    """
    Discovers and instantiates GatewayPlugins from the specified directory.
    Returns a dictionary mapping capability IDs to plugin instances.
    """
    plugins: Dict[str, GatewayPlugin] = {}

    if not os.path.exists(plugin_dir) or not os.path.isdir(plugin_dir):
        logger.warning(f"Plugin directory {plugin_dir} does not exist.")
        return plugins

    # Add the plugin dir to sys.path so plugins can import each other if needed
    if plugin_dir not in sys.path:
        sys.path.insert(0, plugin_dir)

    for filename in os.listdir(plugin_dir):
        if filename.endswith(".disabled"):
            logger.info(f"Skipping disabled plugin file: {filename}")
            continue

        if not filename.endswith(".py") or filename == "__init__.py":
            continue

        filepath = os.path.join(plugin_dir, filename)
        module_name = f"gateway_plugins.{filename[:-3]}"

        try:
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)

                for name, obj in inspect.getmembers(module, inspect.isclass):
                    # Ensure it's a subclass of GatewayPlugin but not the base class itself
                    if issubclass(obj, GatewayPlugin) and obj is not GatewayPlugin:
                        try:
                            plugin_instance = obj()
                            manifest = plugin_instance.manifest()
                            capability_id = manifest.get("capability_id")
                            if not capability_id:
                                logger.error(f"Plugin {name} in {filename} must define a capability_id in manifest.")
                                continue

                            plugins[capability_id] = plugin_instance
                            logger.info(f"Successfully loaded plugin: {capability_id} ({name}) from {filename}")
                        except Exception as e:
                            logger.error(f"Failed to instantiate plugin {name} from {filename}: {e}")
        except Exception as e:
            logger.error(f"Failed to load plugin module {filename}: {e}")

    return plugins
