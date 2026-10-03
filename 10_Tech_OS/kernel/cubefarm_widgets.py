"""CubeFarm Evidence Widgets.

Migrated from 80_Agent-OS/capability_fabric/browser_bridge.py consumer patterns.
Provides reusable evidence/runtime-status widgets to render Agent/Life/Business state
inside the CubeFarm Living Office projection without duplicating shared capabilities.
"""
from typing import Dict, Any, Optional
import datetime
import uuid
from dataclasses import dataclass, field

@dataclass
class BrowserEvidenceState:
    session_id: str
    surface_name: str
    actor_identity: str
    is_authenticated: bool
    last_rendered: str = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat())
    evidence_payloads: list = field(default_factory=list)

class CubeFarmBrowserWidget:
    """
    Renders browser surface evidence (from BrowserBridge) into the CubeFarm projection.
    Does NOT duplicate authentication or tool execution logic.
    """
    def __init__(self, widget_id: str):
        self.widget_id = widget_id
        self._states: Dict[str, BrowserEvidenceState] = {}

    def render_surface_state(self, session_id: str, surface_name: str, actor_identity: str, is_authenticated: bool) -> BrowserEvidenceState:
        """Projects current surface auth state into the widget."""
        state = BrowserEvidenceState(
            session_id=session_id,
            surface_name=surface_name,
            actor_identity=actor_identity,
            is_authenticated=is_authenticated,
        )
        self._states[session_id] = state
        return state

    def append_evidence(self, session_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Appends execution evidence to the widget display state."""
        state = self._states.get(session_id)
        if not state:
            return {"status": "FAILED", "error": f"No widget state for session {session_id}"}

        state.evidence_payloads.append(payload)
        state.last_rendered = datetime.datetime.now(datetime.timezone.utc).isoformat()

        return {
            "status": "SUCCESS",
            "widget_id": self.widget_id,
            "session_id": session_id,
            "evidence_count": len(state.evidence_payloads)
        }

    def get_display_tree(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Returns the fully hydrated widget state for rendering in CubeFarm Office."""
        state = self._states.get(session_id)
        if not state:
            return None
        return {
            "widget_id": self.widget_id,
            "session_id": state.session_id,
            "surface": state.surface_name,
            "actor": state.actor_identity,
            "auth_indicator": "GREEN" if state.is_authenticated else "RED",
            "timeline": state.evidence_payloads,
            "last_refresh": state.last_rendered
        }
