import json
import os
from datetime import datetime, timezone
from typing import Any, Dict

from .capability import CapabilityContract, EffectReceipt


def get_repo_root() -> str:
    current = os.path.abspath(__file__)
    d = os.path.dirname(current)
    while d != os.path.dirname(d):
        if os.path.exists(os.path.join(d, "ASPACE_WORKSPACE_REGISTRY.json")):
            return d
        d = os.path.dirname(d)
    return os.getcwd()


def _parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


def _presence_from_observation(observation: dict[str, Any] | None, *, now: datetime) -> dict[str, Any]:
    if not observation:
        return {
            "presence_state": "DECLARED",
            "evidence_kind": "declared",
            "observed_at": None,
            "expires_at": None,
            "source": "ASPACE_WORKSPACE_REGISTRY.json",
        }

    observed_at = observation.get("observed_at")
    expires_at = observation.get("expires_at")
    state = str(observation.get("state") or observation.get("presence_state") or "UNKNOWN").upper()
    expiry = _parse_time(expires_at)

    if expiry is not None and expiry <= now:
        state = "STALE"
    elif state in {"ONLINE", "AVAILABLE", "ACTIVE"}:
        state = "LIVE"
    elif state not in {"LIVE", "OFFLINE", "STALE", "UNKNOWN", "DEGRADED"}:
        state = "UNKNOWN"

    # Fail closed: a LIVE assertion requires an explicit observation timestamp.
    if state == "LIVE" and _parse_time(observed_at) is None:
        state = "UNKNOWN"

    return {
        "presence_state": state,
        "evidence_kind": "measured",
        "observed_at": observed_at,
        "expires_at": expires_at,
        "source": observation.get("source") or "runtime.json:harnesses",
    }


def harness_list_executor(payload: Dict[str, Any], correlation_id: str) -> EffectReceipt:
    repo_root = get_repo_root()
    registry_path = os.path.join(repo_root, "ASPACE_WORKSPACE_REGISTRY.json")
    runtime_path = os.path.join(
        repo_root, "10_Tech_OS", "machine_fabric", "runtime", "run", "runtime.json"
    )

    declared: dict[str, dict[str, Any]] = {}
    if os.path.exists(registry_path):
        with open(registry_path, "r", encoding="utf-8") as f:
            reg_data = json.load(f)
        for _, actor_data in reg_data.get("execution", {}).items():
            for h_id, h_data in actor_data.get("harnesses", {}).items():
                caps = ["tool_call", "file_edit", "shell"]
                if h_id == "hermes":
                    caps.append("browser")
                if h_id == "antigravity":
                    caps.extend(["browser", "subagents"])
                declared[h_id] = {
                    "id": h_id,
                    "declared_status": h_data.get("status", "non_declare"),
                    "capabilities": caps,
                    "surfaces": ["cli", "api", "mcp"],
                }

    runtime: dict[str, Any] = {}
    if os.path.exists(runtime_path):
        try:
            with open(runtime_path, "r", encoding="utf-8") as f:
                runtime = json.load(f)
        except (OSError, json.JSONDecodeError):
            runtime = {}

    # Global runtime ONLINE is deliberately insufficient. Only an explicit
    # per-harness observation may produce LIVE.
    observations = runtime.get("harnesses", {}) if isinstance(runtime, dict) else {}
    now = datetime.now(timezone.utc)
    harnesses = []
    for h_id, h in declared.items():
        presence = _presence_from_observation(observations.get(h_id), now=now)
        harnesses.append(
            {
                **h,
                **presence,
                "status": presence["presence_state"],
            }
        )

    filter_cap = payload.get("capability")
    if filter_cap:
        harnesses = [h for h in harnesses if filter_cap in h["capabilities"]]

    evidence_refs = [registry_path]
    if os.path.exists(runtime_path):
        evidence_refs.append(runtime_path)

    observed_effect = (
        f"Listed {len(harnesses)} harnesses with capability filter '{filter_cap}'"
        if filter_cap
        else f"Listed {len(harnesses)} harnesses"
    )
    return EffectReceipt(
        capability_id="harness_list",
        correlation_id=correlation_id,
        observed_effect=observed_effect,
        provenance="Agent OS shared harness projection",
        status="SUCCESS",
        evidence_refs=evidence_refs,
        data={"harnesses": harnesses},
    )


def register_harness_list(registry):
    contract = CapabilityContract(
        capability_id="harness_list",
        version="1.1",
        domain_owner="Agent OS",
        intent="List harness declarations and independently measured runtime presence",
        input_schema={
            "type": "object",
            "properties": {"capability": {"type": "string"}},
        },
        output_schema={
            "type": "object",
            "properties": {
                "harnesses": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "status": {"type": "string"},
                            "presence_state": {"type": "string"},
                            "declared_status": {"type": "string"},
                            "capabilities": {"type": "array", "items": {"type": "string"}},
                            "surfaces": {"type": "array", "items": {"type": "string"}},
                            "source": {"type": "string"},
                            "observed_at": {"type": ["string", "null"]},
                            "expires_at": {"type": ["string", "null"]},
                            "evidence_kind": {"type": "string"},
                        },
                    },
                }
            },
        },
        authority="Agent OS Projection",
        effect_class="QUERY",
        supported_surfaces=["cli", "api", "mcp", "harness"],
        executor=harness_list_executor,
    )
    registry.register(contract)
