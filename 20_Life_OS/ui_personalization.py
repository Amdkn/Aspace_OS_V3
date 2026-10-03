from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
import datetime

@dataclass
class UUPMProfile:
    """
    User Universal Profile Model (UUPM) primitive for Life OS personalization.
    Preserves Life OS ownership without imposing Business OS assumptions.
    """
    user_id: str
    active_theme: str = "aurora"
    preferences: Dict[str, Any] = field(default_factory=dict)
    life_wheel_focus: List[str] = field(default_factory=list)
    gtd_default_context: str = "General"
    last_active: str = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat())

class MultiThemeEngine:
    """
    Multi-Theme engine supporting themes (e.g. aurora, glass, terminal, brutalism, dark-oled).
    """
    SUPPORTED_THEMES = ["aurora", "glass", "terminal", "brutalism", "dark-oled", "warm-direction"]

    def __init__(self, default_theme: str = "aurora"):
        if default_theme not in self.SUPPORTED_THEMES:
            raise ValueError(f"Theme '{default_theme}' not supported.")
        self.current_theme = default_theme

    def apply_theme(self, profile: UUPMProfile, theme_name: str) -> Dict[str, Any]:
        if theme_name not in self.SUPPORTED_THEMES:
            raise ValueError(f"Theme '{theme_name}' not in supported themes: {self.SUPPORTED_THEMES}")

        profile.active_theme = theme_name
        profile.last_active = datetime.datetime.now(datetime.timezone.utc).isoformat()

        return {
            "status": "SUCCESS",
            "user_id": profile.user_id,
            "active_theme": profile.active_theme,
            "applied_at": profile.last_active
        }
