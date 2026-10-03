"""CubeFarm UI Primitives for Living Office Projection.

Migrated from 20_Life_OS/ui_personalization.py for reusable Living Office primitives.
Allows multi-theme configuration decoupled from Life OS semantics.
"""
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
import datetime

@dataclass
class CubeFarmThemeProfile:
    """
    Reusable Theme Profile for CubeFarm UI.
    Migrated from UUPMProfile to allow generic usage in the Living Office projection.
    """
    actor_id: str
    active_theme: str = "aurora"
    preferences: Dict[str, Any] = field(default_factory=dict)
    last_active: str = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat())

class CubeFarmMultiThemeEngine:
    """
    Multi-Theme engine supporting Living Office UI themes.
    """
    SUPPORTED_THEMES = ["aurora", "glass", "terminal", "brutalism", "dark-oled", "warm-direction", "factory-industrial"]

    def __init__(self, default_theme: str = "aurora"):
        if default_theme not in self.SUPPORTED_THEMES:
            raise ValueError(f"Theme '{default_theme}' not supported.")
        self.current_theme = default_theme

    def apply_theme(self, profile: CubeFarmThemeProfile, theme_name: str) -> Dict[str, Any]:
        if theme_name not in self.SUPPORTED_THEMES:
            raise ValueError(f"Theme '{theme_name}' not in supported themes: {self.SUPPORTED_THEMES}")

        profile.active_theme = theme_name
        profile.last_active = datetime.datetime.now(datetime.timezone.utc).isoformat()

        return {
            "status": "SUCCESS",
            "actor_id": profile.actor_id,
            "active_theme": profile.active_theme,
            "applied_at": profile.last_active
        }
