"""Surface Matrix registry for heterogeneous browser-auth surfaces in A'Space.

Defines target surfaces, capabilities, and driver bindings without duplicating core logic.
"""

from typing import Dict, Any, List

SURFACE_MATRIX: Dict[str, Dict[str, Any]] = {
    "chatgpt_web": {
        "display_name": "ChatGPT Web Surface",
        "provider": "OpenAI",
        "auth_type": "browser_session_cookie",
        "driver_class": "ChatGPTWebAdapter",
        "supported_capabilities": [
            "browser_prompt",
            "browser_capability_exec",
            "code_interpreter",
            "file_attachment",
        ],
        "quota_signals_supported": True,
        "readback_mechanism": "dom_selector_and_network_interception",
    },
    "qwen_coder_web": {
        "display_name": "Qwen / Qwen Coder Web Surface",
        "provider": "Alibaba / Qwen",
        "auth_type": "browser_token_bearer",
        "driver_class": "QwenCoderWebAdapter",
        "supported_capabilities": [
            "browser_prompt",
            "browser_capability_exec",
            "code_synthesis",
            "file_attachment",
        ],
        "quota_signals_supported": True,
        "readback_mechanism": "dom_selector_and_response_validation",
    },
    "zai_web": {
        "display_name": "Z.ai Web Surface",
        "provider": "Z.ai",
        "auth_type": "browser_session_cookie",
        "driver_class": "GenericBrowserSurfaceAdapter",
        "supported_capabilities": ["browser_prompt", "browser_capability_exec"],
        "quota_signals_supported": True,
        "readback_mechanism": "dom_selector_validation",
    },
    "kimi_web": {
        "display_name": "Kimi Moonshot Web Surface",
        "provider": "Moonshot",
        "auth_type": "browser_token_bearer",
        "driver_class": "GenericBrowserSurfaceAdapter",
        "supported_capabilities": ["browser_prompt", "browser_capability_exec", "long_context_doc"],
        "quota_signals_supported": True,
        "readback_mechanism": "dom_selector_validation",
    },
    "minimax_web": {
        "display_name": "MiniMax Web Surface",
        "provider": "MiniMax",
        "auth_type": "browser_session_cookie",
        "driver_class": "GenericBrowserSurfaceAdapter",
        "supported_capabilities": ["browser_prompt", "browser_capability_exec"],
        "quota_signals_supported": True,
        "readback_mechanism": "dom_selector_validation",
    },
    "deepseek_web": {
        "display_name": "DeepSeek Web Surface",
        "provider": "DeepSeek",
        "auth_type": "browser_session_cookie",
        "driver_class": "GenericBrowserSurfaceAdapter",
        "supported_capabilities": ["browser_prompt", "browser_capability_exec", "reasoning_chain"],
        "quota_signals_supported": True,
        "readback_mechanism": "dom_selector_validation",
    },
    "gemini_spark_web": {
        "display_name": "Gemini / Spark Web Surface",
        "provider": "Google / Spark",
        "auth_type": "browser_oauth_session",
        "driver_class": "GenericBrowserSurfaceAdapter",
        "supported_capabilities": ["browser_prompt", "browser_capability_exec", "multimodal_search"],
        "quota_signals_supported": True,
        "readback_mechanism": "dom_selector_validation",
    },
    "muse_web": {
        "display_name": "Muse Web Surface",
        "provider": "Muse",
        "auth_type": "browser_session_cookie",
        "driver_class": "GenericBrowserSurfaceAdapter",
        "supported_capabilities": ["browser_prompt", "browser_capability_exec"],
        "quota_signals_supported": True,
        "readback_mechanism": "dom_selector_validation",
    },
}


def get_surface_spec(surface_id: str) -> Dict[str, Any]:
    if surface_id not in SURFACE_MATRIX:
        raise ValueError(f"Unknown surface_id: {surface_id}")
    return SURFACE_MATRIX[surface_id]


def list_registered_surfaces() -> List[str]:
    return list(SURFACE_MATRIX.keys())
