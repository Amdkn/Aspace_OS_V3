"""CubeFarm integration for A'Space OS V3 Kernel.

ADR-0388: CubeFarm is an instrument of Ryan, bounded by FactoryExecution envelopes.
It is NOT a new institutional agent.
"""
import dataclasses
import json
from typing import Optional, Dict, Any, List, Union

VALID_CLASSIFICATIONS = {
    "UI/RUNTIME REUSABLE",
    "SHARED CAPABILITY CONSUMER",
    "BUSINESS-ONLY",
    "TECH PRIMITIVE",
    "QUARANTINE",
}

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

    def to_json(self) -> str:
        return json.dumps(dataclasses.asdict(self))

    @classmethod
    def from_json(cls, data: str) -> "FactoryExecution":
        return cls(**json.loads(data))


@dataclasses.dataclass
class InnovationCandidate:
    candidate_id: str
    title: str
    source_issue: str
    classification: str
    target_surface: str
    rationale: str
    portability_notes: str

    def __post_init__(self):
        if self.classification not in VALID_CLASSIFICATIONS:
            raise ValueError(f"Invalid classification {self.classification!r}. Must be one of {VALID_CLASSIFICATIONS}")

    def to_dict(self) -> Dict[str, Any]:
        return dataclasses.asdict(self)


class MigrationMatrix:
    """Systematically evaluates and registers reusable Business OS innovations for A'Space CubeFarm fork (#402)."""

    REQUIRED_CANDIDATES = [
        InnovationCandidate(
            candidate_id="uupm_multi_theme",
            title="UUPM/Multi-Theme and reusable design/configuration primitives",
            source_issue="#400",
            classification="UI/RUNTIME REUSABLE",
            target_surface="cubefarm_wall_ui",
            rationale="Visual styling tokens and design system primitives are presentation-only and can be safely re-themed for CubeFarm walls.",
            portability_notes="Port UUPM design tokens and theme switching primitives without duplicating underlying business domain logic."
        ),
        InnovationCandidate(
            candidate_id="living_office_dashboard_patterns",
            title="Reusable dashboard/projection patterns suitable for the Living Office",
            source_issue="#403",
            classification="UI/RUNTIME REUSABLE",
            target_surface="living_office_wall",
            rationale="Dashboard grid, card layouts, and projection panels provide spatial layout structures without owning core domain state.",
            portability_notes="Reusable UI layout structures projected in Living Office."
        ),
        InnovationCandidate(
            candidate_id="shared_capability_surfaces",
            title="Capability/tool surfaces only as consumers of #333",
            source_issue="#333",
            classification="SHARED CAPABILITY CONSUMER",
            target_surface="agent_os_capability_fabric",
            rationale="Surfaces consume registered capabilities via Agent OS capability fabric (#333); never duplicate Business executors.",
            portability_notes="Consumes capabilities via SurfaceFabric routing."
        ),
        InnovationCandidate(
            candidate_id="typed_state_evidence_widgets",
            title="Evidence/runtime-status widgets rendering Agent/Life/Business state",
            source_issue="#416",
            classification="SHARED CAPABILITY CONSUMER",
            target_surface="cubefarm_tri_wall",
            rationale="Widgets consume typed adapters from Agent, Life, and Business OS to project status on CubeFarm walls.",
            portability_notes="Renders state from typed adapters; strictly read-only or capability-driven."
        ),
        InnovationCandidate(
            candidate_id="auth_session_ux",
            title="Reusable auth/session UX primitives",
            source_issue="#417",
            classification="QUARANTINE",
            target_surface="credential_authority_boundary",
            rationale="Must not duplicate #417 credential authority or token treasury. Quarantined from independent execution in CubeFarm.",
            portability_notes="Keep auth/session UX strictly quarantined to enforce #417 single source of truth."
        ),
    ]

    def __init__(self, candidates: Optional[List[InnovationCandidate]] = None):
        self.candidates: Dict[str, InnovationCandidate] = {}
        initial_list = candidates if candidates is not None else self.REQUIRED_CANDIDATES
        for c in initial_list:
            self.register_candidate(c)

    def register_candidate(self, candidate: InnovationCandidate) -> None:
        self.candidates[candidate.candidate_id] = candidate

    def get_candidate(self, candidate_id: str) -> Optional[InnovationCandidate]:
        return self.candidates.get(candidate_id)

    def filter_by_classification(self, classification: str) -> List[InnovationCandidate]:
        return [c for c in self.candidates.values() if c.classification == classification]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "matrix_version": "2026-10-02",
            "candidates": [c.to_dict() for c in self.candidates.values()]
        }


class UUPMThemeAdapter:
    """Proven Port 1: Visual / Configuration Primitive.

    Provides UUPM theme definitions and design tokens for CubeFarm wall UI without
    touching business state.
    """

    SUPPORTED_THEMES = {
        "dark_mode_oled": {
            "name": "Dark Mode OLED",
            "bg_color": "#000000",
            "surface_color": "#111111",
            "text_color": "#f8f9fa",
            "accent_color": "#3b82f6",
            "border_radius": "8px",
            "glassmorphism": False,
        },
        "glassmorphism": {
            "name": "Glassmorphism",
            "bg_color": "rgba(15, 23, 42, 0.75)",
            "surface_color": "rgba(255, 255, 255, 0.05)",
            "text_color": "#ffffff",
            "accent_color": "#8b5cf6",
            "border_radius": "16px",
            "glassmorphism": True,
        },
        "soft_ui": {
            "name": "Soft UI Evolution",
            "bg_color": "#e0e5ec",
            "surface_color": "#e0e5ec",
            "text_color": "#2d3748",
            "accent_color": "#3182ce",
            "border_radius": "12px",
            "glassmorphism": False,
        },
        "minimalist": {
            "name": "Minimalist Clean",
            "bg_color": "#ffffff",
            "surface_color": "#f7fafc",
            "text_color": "#1a202c",
            "accent_color": "#000000",
            "border_radius": "4px",
            "glassmorphism": False,
        },
    }

    def __init__(self, active_theme: str = "dark_mode_oled"):
        if active_theme not in self.SUPPORTED_THEMES:
            raise ValueError(f"Unsupported theme: {active_theme!r}. Supported: {list(self.SUPPORTED_THEMES.keys())}")
        self.active_theme = active_theme

    def get_theme_tokens(self) -> Dict[str, Any]:
        return self.SUPPORTED_THEMES[self.active_theme]

    def set_theme(self, theme_key: str) -> Dict[str, Any]:
        if theme_key not in self.SUPPORTED_THEMES:
            raise ValueError(f"Unsupported theme: {theme_key!r}. Supported: {list(self.SUPPORTED_THEMES.keys())}")
        self.active_theme = theme_key
        return self.get_theme_tokens()

    def render_wall_container_style(self) -> Dict[str, str]:
        tokens = self.get_theme_tokens()
        style = {
            "backgroundColor": tokens["bg_color"],
            "color": tokens["text_color"],
            "borderRadius": tokens["border_radius"],
            "border": f"1px solid {tokens['accent_color']}",
        }
        if tokens["glassmorphism"]:
            style["backdropFilter"] = "blur(12px)"
        return style


class CubeFarmStateProjectionAdapter:
    """Proven Port 2: Shared Capability Projection.

    Connects to SurfaceFabric (#333) as a capability consumer to project unified
    Agent, Life, and Business state on CubeFarm wall surfaces. Emits structured receipts.
    """

    def __init__(self, actor_id: str = "Ryan", return_to: str = "#388/#403"):
        self.actor_id = actor_id
        self.return_to = return_to

    def project_state(
        self,
        wall_id: str,
        agent_state: Dict[str, Any],
        life_state: Dict[str, Any],
        business_state: Dict[str, Any],
        fabric_surface: str = "agent_os"
    ) -> Dict[str, Any]:
        """Builds a typed wall projection and return evidence receipt without mutating business truth."""
        projection = {
            "wall_id": wall_id,
            "actor_id": self.actor_id,
            "surface_binding": fabric_surface,
            "layers": {
                "agent_os": agent_state,
                "life_os": life_state,
                "business_os": business_state,
            },
            "receipt": {
                "status": "PRODUCED",
                "consumer_role": "SHARED_CAPABILITY_CONSUMER",
                "return_to": self.return_to,
                "fencing": "CUBEFARM_BOUNDED_PROJECTION",
            }
        }
        return projection
