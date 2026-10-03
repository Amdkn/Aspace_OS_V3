#!/usr/bin/env python3
"""Provider-compliant multi-profile Jules fleet supervisor.

The supervisor is intentionally profile-agnostic:
- credentials are injected at runtime and never persisted by this module;
- concurrency caps are supplied from measured/provider-safe configuration;
- the official Jules API is used with X-Goog-Api-Key;
- institutional WorkID identity stays separate from Jules session identity.
"""
from __future__ import annotations

import dataclasses
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Callable, Iterable

from fleet_ownership import bind_session, reserve

OFFICIAL_ENDPOINT = "https://jules.googleapis.com/v1alpha"
ACTIVE_STATES = {
    "QUEUED",
    "PLANNING",
    "AWAITING_PLAN_APPROVAL",
    "AWAITING_USER_FEEDBACK",
    "IN_PROGRESS",
}
TERMINAL_STATES = {"COMPLETED", "FAILED", "CANCELLED", "CANCELED"}


@dataclasses.dataclass(frozen=True)
class JulesProfileConfig:
    profile_id: str
    api_key: str
    concurrency_cap: int | None
    allowed_sources: tuple[str, ...]
    endpoint: str = OFFICIAL_ENDPOINT
    enabled: bool = True


@dataclasses.dataclass
class JulesProfileState:
    profile_id: str
    healthy: bool
    active_sessions: int
    concurrency_cap: int | None
    available_capacity: int | None
    source_count: int
    error: str | None = None


@dataclasses.dataclass
class FleetInventory:
    profiles: dict[str, JulesProfileState]

    @property
    def total_active(self) -> int:
        return sum(p.active_sessions for p in self.profiles.values())

    @property
    def total_available(self) -> int | None:
        values = [p.available_capacity for p in self.profiles.values()]
        if any(v is None for v in values):
            return None
        return sum(int(v or 0) for v in values)

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema": "aspace.jules.fleet-inventory.v2",
            "profiles": {k: dataclasses.asdict(v) for k, v in self.profiles.items()},
            "total_active": self.total_active,
            "total_available": self.total_available,
        }


class JulesFleetSupervisor:
    def __init__(
        self,
        profiles: Iterable[JulesProfileConfig],
        *,
        reports_dir: Path | None = None,
        max_retries_per_work_id: int = 3,
    ) -> None:
        self.profiles = {p.profile_id: p for p in profiles if p.enabled}
        if not self.profiles:
            raise ValueError("at least one enabled Jules profile is required")
        self.reports_dir = reports_dir
        self.max_retries = max_retries_per_work_id
        self.retry_tracker: dict[str, int] = {}
        self.active_leases: dict[str, str] = {}

    def _request(
        self,
        profile: JulesProfileConfig,
        path: str,
        *,
        method: str = "GET",
        body: dict[str, Any] | None = None,
        timeout: int = 30,
    ) -> dict[str, Any]:
        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": profile.api_key,
        }
        payload = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(
            profile.endpoint.rstrip("/") + "/" + path.lstrip("/"),
            data=payload,
            method=method,
            headers=headers,
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            return json.loads(raw) if raw else {}

    def list_sources(self, profile: JulesProfileConfig) -> list[dict[str, Any]]:
        return list(self._request(profile, "sources?pageSize=100").get("sources", []))

    def list_sessions(self, profile: JulesProfileConfig) -> list[dict[str, Any]]:
        return list(self._request(profile, "sessions?pageSize=100").get("sessions", []))

    def inventory(self) -> FleetInventory:
        states: dict[str, JulesProfileState] = {}
        for profile in self.profiles.values():
            try:
                sources = self.list_sources(profile)
                sessions = self.list_sessions(profile)
                active = sum(1 for s in sessions if s.get("state") in ACTIVE_STATES)
                cap = profile.concurrency_cap
                available = None if cap is None else max(0, cap - active)
                states[profile.profile_id] = JulesProfileState(
                    profile_id=profile.profile_id,
                    healthy=True,
                    active_sessions=active,
                    concurrency_cap=cap,
                    available_capacity=available,
                    source_count=len(sources),
                )
            except Exception as exc:
                states[profile.profile_id] = JulesProfileState(
                    profile_id=profile.profile_id,
                    healthy=False,
                    active_sessions=0,
                    concurrency_cap=profile.concurrency_cap,
                    available_capacity=0,
                    source_count=0,
                    error=str(exc),
                )
        return FleetInventory(states)

    @staticmethod
    def issue_claimed(issue_number: int, sessions: Iterable[dict[str, Any]]) -> bool:
        pattern = re.compile(rf"(?<!\d)#?{issue_number}(?!\d)")
        for session in sessions:
            haystack = " ".join(
                str(session.get(k, "")) for k in ("title", "prompt", "name")
            )
            if pattern.search(haystack):
                return True
        return False

    def enforce_mutation_lease(self, work_id: str, session_id: str) -> bool:
        current = self.active_leases.get(work_id)
        if current and current != session_id:
            return False
        try:
            reserve(work_id)
            bind_session(work_id, session_id)
        except ValueError:
            if current != session_id:
                return False
        self.active_leases[work_id] = session_id
        return True

    def release_mutation_lease(self, work_id: str, session_id: str) -> None:
        if self.active_leases.get(work_id) == session_id:
            self.active_leases.pop(work_id, None)

    def apply_retry_bound(self, work_id: str) -> bool:
        count = self.retry_tracker.get(work_id, 0)
        if count >= self.max_retries:
            return False
        self.retry_tracker[work_id] = count + 1
        return True

    def handle_waiting_state(self, profile: JulesProfileConfig, session: dict[str, Any]) -> bool:
        session_id = str(session.get("id") or session.get("name", "")).removeprefix("sessions/")
        state = session.get("state")
        if state == "AWAITING_PLAN_APPROVAL":
            self._request(profile, f"sessions/{session_id}:approvePlan", method="POST", body={})
            return True
        if state == "AWAITING_USER_FEEDBACK":
            self._request(
                profile,
                f"sessions/{session_id}:sendMessage",
                method="POST",
                body={
                    "prompt": (
                        "Continue autonomously within the existing issue scope. "
                        "Make routine reversible decisions, run tests, create/update the PR, "
                        "and stop only for genuine human-only authority."
                    )
                },
            )
            return True
        return False

    def create_session(
        self,
        profile: JulesProfileConfig,
        *,
        issue_number: int,
        issue_title: str,
        prompt: str,
        source: str,
        starting_branch: str = "main",
    ) -> dict[str, Any]:
        if source not in profile.allowed_sources:
            raise ValueError(f"source not authorized for profile {profile.profile_id}: {source}")
        return self._request(
            profile,
            "sessions",
            method="POST",
            body={
                "prompt": prompt,
                "sourceContext": {
                    "source": source,
                    "githubRepoContext": {"startingBranch": starting_branch},
                },
                "title": f"[FLEET][{profile.profile_id}] #{issue_number} - {issue_title}",
                "requirePlanApproval": False,
                "automationMode": "AUTO_CREATE_PR",
            },
        )

    def refill(
        self,
        work_items: Iterable[dict[str, Any]],
        *,
        source: str,
        prompt_builder: Callable[[dict[str, Any]], str],
    ) -> list[dict[str, Any]]:
        inventory = self.inventory()
        sessions_by_profile = {
            pid: self.list_sessions(self.profiles[pid])
            for pid, st in inventory.profiles.items()
            if st.healthy
        }
        all_active = [
            s
            for sessions in sessions_by_profile.values()
            for s in sessions
            if s.get("state") in ACTIVE_STATES
        ]
        launched: list[dict[str, Any]] = []
        queue = list(work_items)

        for pid, state in inventory.profiles.items():
            if not state.healthy or state.available_capacity in (None, 0):
                continue
            profile = self.profiles[pid]
            slots = int(state.available_capacity or 0)
            for item in list(queue):
                if slots <= 0:
                    break
                issue_number = int(item["issue_number"])
                if self.issue_claimed(issue_number, all_active):
                    queue.remove(item)
                    continue
                session = self.create_session(
                    profile,
                    issue_number=issue_number,
                    issue_title=str(item["title"]),
                    prompt=prompt_builder(item),
                    source=source,
                    starting_branch=str(item.get("starting_branch", "main")),
                )
                launched.append(
                    {
                        "profile_id": pid,
                        "issue_number": issue_number,
                        "session_id": session.get("id"),
                        "state": session.get("state"),
                        "url": session.get("url"),
                    }
                )
                all_active.append(session)
                queue.remove(item)
                slots -= 1
        return launched

    def consume_completed(
        self,
        profile: JulesProfileConfig,
        session: dict[str, Any],
        *,
        work_id: str,
        acceptance: Callable[[dict[str, Any]], bool],
        close_work: Callable[[str, dict[str, Any]], None],
    ) -> dict[str, Any]:
        session_id = str(session.get("id") or session.get("name", "")).removeprefix("sessions/")
        if session.get("state") != "COMPLETED":
            return {"work_id": work_id, "session_id": session_id, "accepted": False}
        accepted = bool(acceptance(session))
        if accepted:
            close_work(work_id, session)
            self.release_mutation_lease(work_id, session_id)
        return {
            "work_id": work_id,
            "session_id": session_id,
            "accepted": accepted,
            "pr": session.get("pullRequest") or session.get("pr"),
        }

    def export_state(self, inventory: FleetInventory, *, path: Path | None = None) -> dict[str, Any]:
        state = {
            "schema": "aspace.jules.fleet-state.v2",
            "observed_at": time.time(),
            "inventory": inventory.to_dict(),
            "active_leases": dict(self.active_leases),
        }
        target = path
        if target is None and self.reports_dir is not None:
            target = self.reports_dir / "jules_fleet_state.json"
        if target is not None:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
        return state
