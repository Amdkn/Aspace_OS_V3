"""Shared Browser Harness Bridge / SurfaceDriver contract for A'Space OS V3.

Provides a single SurfaceDriver contract and BrowserBridge base that represents
browser-auth AI surfaces (ChatGPT Web, Qwen Web, Kimi, DeepSeek, Z.ai, etc.)
without duplicating core browser/auth/session or tool calling logic.
"""
from __future__ import annotations

import abc
import datetime
import uuid
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional


@dataclass
class BrowserAuthSession:
    session_id: str
    surface_name: str
    user_identity: str
    cookies_present: bool
    is_authenticated: bool
    created_at: str = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat())


class SurfaceDriver(abc.ABC):
    """Abstract SurfaceDriver contract for browser-auth surfaces."""

    def __init__(self, surface_name: str):
        self.surface_name = surface_name
        self._auth_sessions: Dict[str, BrowserAuthSession] = {}

    def authenticate_session(self, session_id: str, user_identity: str, auth_tokens: Dict[str, str]) -> BrowserAuthSession:
        """Shared session authentication logic."""
        session = BrowserAuthSession(
            session_id=session_id,
            surface_name=self.surface_name,
            user_identity=user_identity,
            cookies_present=bool(auth_tokens),
            is_authenticated=bool(auth_tokens),
        )
        self._auth_sessions[session_id] = session
        return session

    def get_session(self, session_id: str) -> Optional[BrowserAuthSession]:
        return self._auth_sessions.get(session_id)

    def execute_tool_call(
        self,
        session_id: str,
        tool_name: str,
        arguments: Dict[str, Any],
        correlation_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Shared bridge orchestration: native harness -> browser-auth bridge -> web model -> tool call."""
        session = self.get_session(session_id)
        if not session or not session.is_authenticated:
            return {
                "status": "FAILED",
                "error": f"Session '{session_id}' on surface '{self.surface_name}' is not authenticated.",
            }

        corr_id = correlation_id or f"corr-{uuid.uuid4().hex[:8]}"

        # Render prompt / payload for web model via adapter-specific transformation
        raw_payload = self.format_web_prompt(tool_name, arguments)

        # Dispatch via browser surface adapter method
        adapter_response = self._dispatch_to_web_surface(session, raw_payload)

        # Parse tool response/call from web model
        parsed_result = self.parse_web_response(adapter_response)

        return {
            "status": "SUCCESS",
            "surface": self.surface_name,
            "session_id": session_id,
            "correlation_id": corr_id,
            "tool_name": tool_name,
            "result": parsed_result,
        }

    @abc.abstractmethod
    def format_web_prompt(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        """Transform tool request into web model prompt/payload for this specific surface."""
        pass

    @abc.abstractmethod
    def _dispatch_to_web_surface(self, session: BrowserAuthSession, payload: str) -> Dict[str, Any]:
        """Per-surface web driver/transport execution."""
        pass

    @abc.abstractmethod
    def parse_web_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """Parse raw web surface model output into structured tool result."""
        pass


class ChatGPTWebAdapter(SurfaceDriver):
    """Per-surface adapter for ChatGPT Web (codex-chatgpt-web proof pattern)."""

    def __init__(self):
        super().__init__("chatgpt_web")

    def format_web_prompt(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        return f"[ChatGPTWeb] ToolCall: {tool_name} with args {arguments}"

    def _dispatch_to_web_surface(self, session: BrowserAuthSession, payload: str) -> Dict[str, Any]:
        return {
            "raw_text": f"ChatGPT Response for session {session.session_id}: Executed {payload}",
            "status_code": 200,
        }

    def parse_web_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        return {"output": response.get("raw_text", ""), "parsed": True}


class QwenWebAdapter(SurfaceDriver):
    """Per-surface adapter for Qwen Web surface."""

    def __init__(self):
        super().__init__("qwen_web")

    def format_web_prompt(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        return f"[QwenWeb] ToolCall: {tool_name} with args {arguments}"

    def _dispatch_to_web_surface(self, session: BrowserAuthSession, payload: str) -> Dict[str, Any]:
        return {
            "raw_text": f"Qwen Response for session {session.session_id}: Executed {payload}",
            "status_code": 200,
        }

    def parse_web_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        return {"output": response.get("raw_text", ""), "parsed": True}
