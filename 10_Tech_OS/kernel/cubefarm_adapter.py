"""CubeFarm integration for A'Space OS V3 Kernel.

ADR-0388: CubeFarm is an instrument of Ryan, bounded by FactoryExecution envelopes.
It is NOT a new institutional agent.

Issue #400: Recover UUPM / Business OS Multi-Theme into A'Space CubeFarm fork topology.
- Upstream topology = leonvanzyl/cubefarm
- Fork topology = Amdkn/cubefarm (Amdkn-owned fork)
- Bounded UI theme capability projection (identity/authority semantics and cosmology remain separate)
"""
import dataclasses
import json
from typing import Optional, Dict, Any, List

CUBEFARM_FORK_TOPOLOGY = {
    "upstream_repo": "leonvanzyl/cubefarm",
    "fork_repo": "Amdkn/cubefarm",
    "upstream_syncable": True,
    "direct_upstream_main_customization": False,
    "theme_capability_bounded": True,
}

# Recovered exact UUPM / Business OS Multi-Theme catalogue tokens from prior implementation
UUPM_THEME_CATALOGUE: Dict[str, Dict[str, str]] = {
    "dark-oled": {
        "theme_id": "dark-oled",
        "name": "Dark OLED",
        "style_category": "OLED Dark Mode",
        "bg_surface": "#000000",
        "text_color": "#f8fafc",
        "text_muted": "#94a3b8",
        "panel_border": "#1e293b",
        "accent_color": "#38bdf8",
        "on_accent": "#0f172a",
        "surface_hover": "#0f172a",
    },
    "warm-paper": {
        "theme_id": "warm-paper",
        "name": "Warm Paper",
        "style_category": "Minimalist Editorial",
        "bg_surface": "#fbf9f5",
        "text_color": "#1c1917",
        "text_muted": "#78716c",
        "panel_border": "#e7e5e4",
        "accent_color": "#ea580c",
        "on_accent": "#ffffff",
        "surface_hover": "#f5f5f4",
    },
    "cyberpunk": {
        "theme_id": "cyberpunk",
        "name": "Cyberpunk UI",
        "style_category": "Neon Cyberpunk",
        "bg_surface": "#09090b",
        "text_color": "#00ffcc",
        "text_muted": "#a1a1aa",
        "panel_border": "#ff007f",
        "accent_color": "#ff007f",
        "on_accent": "#000000",
        "surface_hover": "#18181b",
    },
    "aurora": {
        "theme_id": "aurora",
        "name": "Aurora UI",
        "style_category": "Vibrant Aurora",
        "bg_surface": "#0f172a",
        "text_color": "#f1f5f9",
        "text_muted": "#64748b",
        "panel_border": "#334155",
        "accent_color": "#818cf8",
        "on_accent": "#0f172a",
        "surface_hover": "#1e293b",
    },
    "editorial": {
        "theme_id": "editorial",
        "name": "Editorial Art",
        "style_category": "Art & Literature",
        "bg_surface": "#f8f6f0",
        "text_color": "#2a2421",
        "text_muted": "#8c827a",
        "panel_border": "#d8d0c5",
        "accent_color": "#9e2a2b",
        "on_accent": "#ffffff",
        "surface_hover": "#eee8de",
    },
    "liquid-glass": {
        "theme_id": "liquid-glass",
        "name": "Liquid Glass",
        "style_category": "Glassmorphism",
        "bg_surface": "rgba(15, 23, 42, 0.75)",
        "text_color": "#f8fafc",
        "text_muted": "#94a3b8",
        "panel_border": "rgba(255, 255, 255, 0.15)",
        "accent_color": "#06b6d4",
        "on_accent": "#ffffff",
        "surface_hover": "rgba(255, 255, 255, 0.05)",
    },
}


@dataclasses.dataclass
class CubeFarmThemeConfig:
    active_theme_id: str
    custom_accent: Optional[str] = None
    override_css_vars: Dict[str, str] = dataclasses.field(default_factory=dict)

    def get_effective_tokens(self) -> Dict[str, str]:
        base = UUPM_THEME_CATALOGUE.get(
            self.active_theme_id, UUPM_THEME_CATALOGUE["dark-oled"]
        ).copy()
        if self.custom_accent:
            base["accent_color"] = self.custom_accent
        base.update(self.override_css_vars)
        return base

    def validate_bounds(self) -> bool:
        """Enforces Wargame constraint: UI Theme cannot modify core identity, authority, or agent/queue cosmology."""
        tokens = self.get_effective_tokens()
        # Theme must only project CSS variables / visual style properties
        allowed_keys = {
            "theme_id",
            "name",
            "style_category",
            "bg_surface",
            "text_color",
            "text_muted",
            "panel_border",
            "accent_color",
            "on_accent",
            "surface_hover",
        }
        return set(tokens.keys()).issubset(allowed_keys)


@dataclasses.dataclass
class FactoryExecution:
    actor_id: str
    doctor: str
    work_id: Optional[int]
    mission_id: Optional[str]
    issue_ref: Optional[str]
    operation_id: str
    correlation_id: str
    authority_envelope: Dict[str, Any]
    affected_resources: List[str]
    allowed_repos: List[str]
    allowed_effects: List[str]
    forbidden_effects: List[str]
    budget_lease: int
    session_limit: int
    runtime_choice: str
    qa_policy: str
    evidence_head: str
    return_to: str
    fencing_token: str
    theme_config: Optional[CubeFarmThemeConfig] = None

    def to_json(self) -> str:
        data = dataclasses.asdict(self)
        return json.dumps(data)

    @classmethod
    def from_json(cls, data: str) -> "FactoryExecution":
        raw = json.loads(data)
        theme_raw = raw.pop("theme_config", None)
        if theme_raw and isinstance(theme_raw, dict):
            raw["theme_config"] = CubeFarmThemeConfig(**theme_raw)
        return cls(**raw)
