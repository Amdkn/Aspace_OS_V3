from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]
SPEC = HERE / "doctor13_round1.json"
CONSTITUTION = REPO_ROOT / "10_Tech_OS" / "kernel" / "COMPANIONS_CONSTITUTION.json"
USER = Path(os.environ.get("USERPROFILE", r"C:\Users\amado"))
LOCAL_ROOT = USER / ".aspace" / "embodiments"
HERMES_PROFILES = USER / ".hermes" / "profiles"

NAMES = ("Ryan", "Yaz", "Graham")
PROFILE = {"Ryan": "ryan", "Yaz": "yaz", "Graham": "graham"}


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def companion_record(name: str, constitution: dict) -> dict:
    for item in constitution.get("companions", []):
        if item.get("name") == name:
            return item
    raise KeyError(f"No companion constitution record for {name}")


def role_material(name: str) -> dict:
    profile = HERMES_PROFILES / PROFILE[name]

    def text(filename: str) -> str:
        p = profile / filename
        return p.read_text(encoding="utf-8-sig") if p.exists() else ""

    return {
        "profile": PROFILE[name],
        "identity": text("IDENTITY.md"),
        "soul": text("SOUL.md"),
        "memory_pointer": text("MEMORY.md"),
    }


def compile_envelope(
    *,
    actor: str,
    harness: str,
    mission_ref: str,
    intent: str,
    correlation_id: str | None,
    work_id: int | None,
    return_to: str | None,
    simulation: bool,
) -> dict:
    if actor not in NAMES:
        raise ValueError(f"Unsupported Round2 actor: {actor}")

    if not simulation:
        missing = [
            key
            for key, value in {
                "correlation_id": correlation_id,
                "work_id": work_id,
                "return_to": return_to,
            }.items()
            if value in (None, "")
        ]
        if missing:
            raise ValueError("Consequential envelope requires durable mission identity: " + ", ".join(missing))

    spec = load_json(SPEC)
    constitution = load_json(CONSTITUTION)
    manifest_path = LOCAL_ROOT / actor / "manifest.json"
    manifest = load_json(manifest_path)
    companion = companion_record(actor, constitution)
    role = role_material(actor)

    authority = {
        "tier": companion["organization_tier"],
        "doctor": companion["doctor"],
        "home_core": companion["home_core"],
        "authority": companion["authority"],
        "forbidden_authority": companion["forbidden_authority"],
        "adr_triggers": companion["adr_triggers"],
        "cross_core_reach": companion["cross_core_reach"],
    }

    mission = {
        "mission_ref": mission_ref,
        "intent": intent,
        "correlation_id": correlation_id,
        "work_id": work_id,
        "return_to": return_to,
        "mode": "READ_ONLY_SIMULATION" if simulation else "BOUNDED_EXECUTION",
    }

    context_sources = {
        "constitution": str(CONSTITUTION).replace("\\", "/"),
        "embodiment_manifest": str(manifest_path).replace("\\", "/"),
        "home_workspace": manifest["home"]["workspace"],
        "hermes_profile": PROFILE[actor],
        "github_wargame": "Amdkn/Aspace_OS_V3#318",
    }

    envelope = {
        "schema": "MissionContextEnvelope.v1",
        "compiled_at": datetime.now().astimezone().isoformat(),

        "actor": {
            "name": actor,
            "identity_id": companion["id"],
            "stewardship_anchor": manifest["identity"]["stewardship_anchor"],
            "institutional_state": manifest["identity"]["institutional_state"],
        },
        "authority": authority,
        "mission": mission,
        "runtime": {
            "requested_harness": harness,
            "primary_affinity": manifest["runtime_affinity"]["round1_primary"],
            "fallbacks_certified": manifest["runtime_affinity"]["fallbacks_certified"],
        },
        "delegation": {
            "manager": companion["doctor"],
            "next_peer": companion.get("handoffs", {}).get("next"),
            "internal_subagents_are_organs_not_institutional_peers": True,
        },
        "role_material": {
            "profile": role["profile"],
            "identity_sha256": hashlib.sha256(role["identity"].encode("utf-8")).hexdigest(),
            "soul_sha256": hashlib.sha256(role["soul"].encode("utf-8")).hexdigest(),
            "memory_pointer_sha256": hashlib.sha256(role["memory_pointer"].encode("utf-8")).hexdigest(),
        },
        "context_sources": context_sources,
        "execution_laws": [
            "Identity is not reconstructed from the runtime prompt.",
            "Read the local Embodied Holon manifest before acting.",
            "Runtime/session loss does not change institutional identity.",

            "Keep the same authority envelope across runtime changes.",
            "Consequential mutation requires durable work identity and return_to.",
            "Evidence before completion; UNKNOWN is not success.",
        ],
    }

    identity_basis = {
        "actor": envelope["actor"],
        "authority": envelope["authority"],
        "delegation": envelope["delegation"],
        "context_sources": envelope["context_sources"],
    }
    envelope["identity_hash"] = digest(identity_basis)
    envelope["authority_hash"] = digest(authority)

    envelope["context_hash"] = digest(
        {
            "identity_hash": envelope["identity_hash"],
            "authority_hash": envelope["authority_hash"],
            "mission": mission,
            "role_material": envelope["role_material"],
        }
    )
    return envelope


def write_envelope(actor: str, envelope: dict, activate: bool) -> Path:
    actor_root = LOCAL_ROOT / actor
    out_dir = actor_root / "envelopes"
    out_dir.mkdir(parents=True, exist_ok=True)
    key = envelope["context_hash"][:16]
    out = out_dir / f"{key}.json"
    out.write_text(json.dumps(envelope, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if activate:
        current = actor_root / "CURRENT.json"
        current.write_text(json.dumps(envelope, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Compile a bounded A'Space MissionContextEnvelope.")
    ap.add_argument("--actor", choices=NAMES, required=True)
    ap.add_argument("--harness", required=True)
    ap.add_argument("--mission-ref", required=True)
    ap.add_argument("--intent", required=True)
    ap.add_argument("--correlation-id")
    ap.add_argument("--work-id", type=int)
    ap.add_argument("--return-to")
    ap.add_argument("--simulation", action="store_true")
    ap.add_argument("--activate", action="store_true")
    args = ap.parse_args()

    envelope = compile_envelope(
        actor=args.actor,
        harness=args.harness,
        mission_ref=args.mission_ref,
        intent=args.intent,
        correlation_id=args.correlation_id,
        work_id=args.work_id,
        return_to=args.return_to,
        simulation=args.simulation,
    )
    out = write_envelope(args.actor, envelope, activate=args.activate)
    print(json.dumps({
        "status": "COMPILED",
        "actor": args.actor,
        "harness": args.harness,
        "mode": envelope["mission"]["mode"],
        "identity_hash": envelope["identity_hash"],
        "authority_hash": envelope["authority_hash"],
        "context_hash": envelope["context_hash"],
        "path": str(out),
        "activated": args.activate,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
