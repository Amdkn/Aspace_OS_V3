"""Bridge capability exposure connecting Browser Harness Bridge to Agent OS Capability Fabric.

Exposes browser surface capabilities across heterogeneous harnesses and holons without copying logic.
"""

from typing import Dict, Any
import os
import sys

# Ensure capability_fabric imports resolve cleanly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from capability_fabric.capability import CapabilityContract, EffectReceipt
from capability_fabric.registry import CapabilityRegistry

from .adapters import ChatGPTWebAdapter, QwenCoderWebAdapter, GenericBrowserSurfaceAdapter
from .surface_matrix import list_registered_surfaces


def get_driver_for_surface(surface_id: str):
    if surface_id == "chatgpt_web":
        return ChatGPTWebAdapter()
    elif surface_id in ("qwen_web", "qwen_coder_web"):
        return QwenCoderWebAdapter()
    elif surface_id in list_registered_surfaces():
        return GenericBrowserSurfaceAdapter(surface_id)
    else:
        raise ValueError(f"Unsupported browser surface: {surface_id}")


def browser_prompt_executor(payload: Dict[str, Any], correlation_id: str) -> EffectReceipt:
    surface_id = payload.get("surface_id", "chatgpt_web")
    prompt = payload.get("prompt", "")
    harness_id = payload.get("harness_id", "hermes")
    holon_id = payload.get("holon_id", "ryan")
    credentials = payload.get("credentials", {"type": "session_cookie", "token": "local_isolated_token"})

    driver = get_driver_for_surface(surface_id)
    session = driver.bootstrap_session(harness_id, holon_id, credentials)
    interaction_id = driver.inject_prompt(session, prompt)
    chunks = driver.capture_stream(session, interaction_id)
    full_response = "".join(chunk.content for chunk in chunks)

    evidence = driver.capture_evidence(
        session=session,
        effect_claimed=f"Inject prompt into {surface_id}",
    )

    return EffectReceipt(
        capability_id="browser_prompt",
        correlation_id=correlation_id,
        observed_effect=evidence.readback_observed,
        provenance=f"Browser Harness Bridge [{surface_id}]",
        status="SUCCESS",
        evidence_refs=[evidence.evidence_ref],
        data={
            "surface_id": surface_id,
            "session_id": session.session_id,
            "harness_id": harness_id,
            "holon_id": holon_id,
            "response_text": full_response,
            "verified": evidence.verified,
        },
    )


def browser_capability_exec_executor(payload: Dict[str, Any], correlation_id: str) -> EffectReceipt:
    surface_id = payload.get("surface_id", "chatgpt_web")
    capability_id = payload.get("capability_id", "generic_exec")
    capability_payload = payload.get("payload", {})
    harness_id = payload.get("harness_id", "codex")
    holon_id = payload.get("holon_id", "clara")
    credentials = payload.get("credentials", {"type": "session_cookie", "token": "local_isolated_token"})

    driver = get_driver_for_surface(surface_id)
    session = driver.bootstrap_session(harness_id, holon_id, credentials)
    exec_result = driver.invoke_capability(session, capability_id, capability_payload, correlation_id)

    return EffectReceipt(
        capability_id="browser_capability_exec",
        correlation_id=correlation_id,
        observed_effect=exec_result.evidence.readback_observed,
        provenance=f"Browser Harness Bridge [{surface_id}]",
        status=exec_result.status,
        evidence_refs=[exec_result.evidence.evidence_ref],
        data={
            "surface_id": surface_id,
            "session_id": exec_result.session_id,
            "harness_id": harness_id,
            "holon_id": holon_id,
            "response_text": exec_result.response_text,
            "verified": exec_result.evidence.verified,
        },
    )


def register_browser_bridge_capabilities(registry: CapabilityRegistry) -> None:
    prompt_contract = CapabilityContract(
        capability_id="browser_prompt",
        version="1.0",
        domain_owner="Agent OS",
        intent="Inject prompt and capture streaming response across browser surfaces",
        input_schema={
            "type": "object",
            "properties": {
                "surface_id": {"type": "string"},
                "prompt": {"type": "string"},
                "harness_id": {"type": "string"},
                "holon_id": {"type": "string"},
            },
            "required": ["surface_id", "prompt"],
        },
        output_schema={
            "type": "object",
            "properties": {
                "response_text": {"type": "string"},
                "session_id": {"type": "string"},
                "verified": {"type": "boolean"},
            },
        },
        authority="Agent OS Capability Fabric",
        effect_class="QUERY",
        supported_surfaces=["cli", "api", "mcp", "harness", "browser"],
        executor=browser_prompt_executor,
    )

    exec_contract = CapabilityContract(
        capability_id="browser_capability_exec",
        version="1.0",
        domain_owner="Agent OS",
        intent="Execute capability through browser bridge requiring evidence readback",
        input_schema={
            "type": "object",
            "properties": {
                "surface_id": {"type": "string"},
                "capability_id": {"type": "string"},
                "payload": {"type": "object"},
                "harness_id": {"type": "string"},
                "holon_id": {"type": "string"},
            },
            "required": ["surface_id", "capability_id"],
        },
        output_schema={
            "type": "object",
            "properties": {
                "response_text": {"type": "string"},
                "verified": {"type": "boolean"},
            },
        },
        authority="Agent OS Capability Fabric",
        effect_class="COMMAND",
        supported_surfaces=["cli", "api", "mcp", "harness", "browser"],
        executor=browser_capability_exec_executor,
    )

    registry.register(prompt_contract)
    registry.register(exec_contract)
