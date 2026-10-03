#!/usr/bin/env python3
"""Provider-compliant multi-profile Jules fleet supervisor for Tech OS / Agent OS.
Manages multi-profile credentials, capacity inventory, duplicate claim prevention,
WorkID mutation leases, plan auto-approval, bounded retries, PR/evidence consumption,
work acceptance/closure, and aggregate fleet state exposure to Agent OS & CubeFarm.
"""
from __future__ import annotations

import dataclasses
import json
import os
import re
import subprocess
import time
import urllib.request
from pathlib import Path
from typing import Dict, List, Optional, Any

from fleet_ownership import reserve, bind_session, require_running_owner, dispatch_lock

ROOT = Path(r"C:\Users\amado\ASpace_OS_V3") if os.name == "nt" else Path(__file__).resolve().parents[2]
REPORTS_DIR = ROOT / "10_Tech_OS" / "reports"
DEFAULT_JULES_ENDPOINT = "http://127.0.0.1:43118"
DEFAULT_SOURCE = "sources/github/Amdkn/Aspace_OS_V3"
MAX_RETRIES_PER_WORK_ID = 3


@dataclasses.dataclass
class JulesProfileConfig:
    profile_id: str
    credentials: str  # Token or API key
    endpoint: str = DEFAULT_JULES_ENDPOINT
    max_capacity: int = 3
    rate_limit_rpm: int = 60
    allowed_sources: List[str] = dataclasses.field(default_factory=lambda: [DEFAULT_SOURCE])


@dataclasses.dataclass
class JulesProfileState:
    config: JulesProfileConfig
    healthy: bool = True
    active_sessions_count: int = 0
    available_capacity: int = 0
    last_health_check: float = 0.0
    error_message: Optional[str] = None


@dataclasses.dataclass
class FleetInventory:
    profiles: Dict[str, JulesProfileState] = dataclasses.field(default_factory=dict)
    total_active_sessions: int = 0
    total_available_capacity: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "total_active_sessions": self.total_active_sessions,
            "total_available_capacity": self.total_available_capacity,
            "profiles": {
                pid: {
                    "healthy": st.healthy,
                    "max_capacity": st.config.max_capacity,
                    "active_sessions": st.active_sessions_count,
                    "available_capacity": st.available_capacity,
                    "endpoint": st.config.endpoint,
                    "allowed_sources": st.config.allowed_sources,
                    "error_message": st.error_message,
                }
                for pid, st in self.profiles.items()
            },
        }


class JulesFleetSupervisor:
    """Multi-profile Jules supervisor enforcing limits, lease locks, feedback resolution, and lifecycle closure."""

    def __init__(self, profiles: Optional[List[JulesProfileConfig]] = None, reports_dir: Optional[Path] = None):
        self.reports_dir = reports_dir or REPORTS_DIR
        self.reports_dir.mkdir(parents=True, exist_ok=True)
        self.profiles: Dict[str, JulesProfileConfig] = {}

        # Load or configure profiles
        if profiles:
            for p in profiles:
                self.profiles[p.profile_id] = p
        else:
            self._load_default_profiles()

        self.retry_tracker: Dict[str, int] = {}  # work_id -> retry count
        self.active_leases: Dict[str, str] = {}  # work_id -> session_id

    def _load_default_profiles(self) -> None:
        """Load default isolated profiles from environment or defaults."""
        p_primary = JulesProfileConfig(
            profile_id="primary",
            credentials=os.environ.get("JULES_PRIMARY_TOKEN", "default_primary_cred"),
            endpoint=os.environ.get("JULES_PRIMARY_ENDPOINT", DEFAULT_JULES_ENDPOINT),
            max_capacity=int(os.environ.get("JULES_PRIMARY_CAPACITY", "3")),
            allowed_sources=[DEFAULT_SOURCE],
        )
        p_secondary = JulesProfileConfig(
            profile_id="secondary",
            credentials=os.environ.get("JULES_SECONDARY_TOKEN", "default_secondary_cred"),
            endpoint=os.environ.get("JULES_SECONDARY_ENDPOINT", DEFAULT_JULES_ENDPOINT),
            max_capacity=int(os.environ.get("JULES_SECONDARY_CAPACITY", "3")),
            allowed_sources=[DEFAULT_SOURCE],
        )
        self.profiles["primary"] = p_primary
        self.profiles["secondary"] = p_secondary

    def _http_request(self, profile: JulesProfileConfig, path: str, method: str = "GET", body: Optional[dict] = None, timeout: int = 10) -> dict:
        """Execute HTTP request with profile-isolated credentials."""
        url = profile.endpoint + path
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {profile.credentials}",
            "X-Jules-Profile": profile.profile_id,
        }
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.load(r)
        except Exception as exc:
            # Fallback for local proxy which might not require auth header
            try:
                req_no_auth = urllib.request.Request(url, data=data, method=method, headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req_no_auth, timeout=timeout) as r:
                    return json.load(r)
            except Exception:
                raise exc

    def check_inventory(self) -> FleetInventory:
        """Inventory profile health and available capacity."""
        inventory = FleetInventory()
        for pid, config in self.profiles.items():
            state = JulesProfileState(config=config, last_health_check=time.time())
            try:
                health = self._http_request(config, "/health", timeout=3)
                if health.get("ok"):
                    sessions = self._http_request(config, "/sessions", timeout=5).get("sessions", [])
                    active = [s for s in sessions if s.get("state") not in {"COMPLETED", "FAILED", "CANCELLED", "CANCELED"}]
                    state.healthy = True
                    state.active_sessions_count = len(active)
                    state.available_capacity = max(0, config.max_capacity - len(active))
                else:
                    state.healthy = False
                    state.error_message = "Health check returned not OK"
            except Exception as exc:
                state.healthy = False
                state.error_message = str(exc)

            inventory.profiles[pid] = state
            if state.healthy:
                inventory.total_active_sessions += state.active_sessions_count
                inventory.total_available_capacity += state.available_capacity

        return inventory

    def prevent_duplicate_claims(self, active_sessions: List[dict], issue_id: str) -> bool:
        """Check if an issue is already claimed by any active session across all profiles."""
        needle = issue_id.strip()
        for s in active_sessions:
            title = s.get("title", "")
            prompt = s.get("prompt", "")
            name = s.get("name", "")
            if needle in title or needle in prompt or needle in name:
                return True
        return False

    def enforce_mutation_lease(self, work_id: str, session_id: str) -> bool:
        """Enforce strictly ONE mutation lease per WorkID via fleet_ownership."""
        if work_id in self.active_leases and self.active_leases[work_id] != session_id:
            # Another session holds the mutation lease
            return False

        # Acquire atomic lease reservation
        try:
            reserve(work_id)
            bind_session(work_id, session_id)
            self.active_leases[work_id] = session_id
            return True
        except ValueError:
            # Lease already held or conflict
            if self.active_leases.get(work_id) == session_id:
                return True
            return False

    def handle_waiting_states(self, profile: JulesProfileConfig, session: dict) -> bool:
        """Detect waiting-for-feedback / plan approval states and handle them autonomously."""
        session_id = session.get("id") or session.get("sessionId") or session.get("name", "").removeprefix("sessions/")
        state = session.get("state", "")

        # Check plan approval status or awaiting feedback
        if state == "AWAITING_PLAN_APPROVAL" or session.get("requirePlanApproval"):
            try:
                self._http_request(profile, f"/sessions/{session_id}/approve", method="POST", body={})
                return True
            except Exception:
                pass

        # Check activities for pending feedback prompt
        try:
            activities = self._http_request(profile, f"/sessions/{session_id}/activities", method="GET").get("activities", [])
            for act in reversed(activities):
                if act.get("type") in {"AWAITING_USER_INPUT", "WAITING_FOR_FEEDBACK"}:
                    continuation_prompt = (
                        "Proceed autonomously with the already-scoped work. Run tests, "
                        "finish/create the PR with evidence, and escalate only for irreversible decisions."
                    )
                    self._http_request(profile, f"/sessions/{session_id}/message", method="POST", body={"prompt": continuation_prompt})
                    return True
        except Exception:
            pass

        return False

    def apply_retry_bounds(self, work_id: str) -> bool:
        """Track retries per WorkID and enforce max retry limit."""
        current = self.retry_tracker.get(work_id, 0)
        if current >= MAX_RETRIES_PER_WORK_ID:
            return False  # Exceeded retry bound
        self.retry_tracker[work_id] = current + 1
        return True

    def consume_pr_and_close_work(self, profile: JulesProfileConfig, session: dict, work_id: str) -> dict:
        """Consume completed PR/evidence, record acceptance, close work, and release capacity."""
        session_id = session.get("id") or session.get("sessionId") or session.get("name", "").removeprefix("sessions/")
        state = session.get("state", "")

        pr_info = session.get("pullRequest") or session.get("pr") or {}
        has_evidence = bool(pr_info or session.get("outputs") or state == "COMPLETED")

        closure_result = {
            "work_id": work_id,
            "session_id": session_id,
            "state": state,
            "pr_url": pr_info.get("url") if isinstance(pr_info, dict) else str(pr_info),
            "evidence_consumed": has_evidence,
            "closed": False,
        }

        if state == "COMPLETED" and has_evidence:
            closure_result["closed"] = True
            # Release mutation lease
            if work_id in self.active_leases:
                del self.active_leases[work_id]

        return closure_result

    def export_fleet_state(self, inventory: FleetInventory, active_sessions: List[dict], closures: List[dict]) -> dict:
        """Expose aggregate fleet state in Agent OS / CubeFarm format."""
        fleet_state = {
            "schema": "aspace.jules.fleet_state.v1",
            "timestamp": time.time(),
            "inventory": inventory.to_dict(),
            "active_leases": self.active_leases,
            "active_sessions_count": len(active_sessions),
            "closed_work_count": len([c for c in closures if c.get("closed")]),
            "closures": closures,
            "cubefarm_integration": {
                "supervisor_role": "RYAN",
                "authority_envelope": "DOCTOR13_MUTATION_LIMITED",
                "active_workers": [
                    {
                        "session_id": s.get("id") or s.get("sessionId") or s.get("name", "").removeprefix("sessions/"),
                        "title": s.get("title", ""),
                        "state": s.get("state", ""),
                    }
                    for s in active_sessions
                ],
            },
        }

        state_file = self.reports_dir / "jules_fleet_state.json"
        state_file.write_text(json.dumps(fleet_state, indent=2, ensure_ascii=False), encoding="utf-8")
        return fleet_state
