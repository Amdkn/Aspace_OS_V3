"""KER-44 constitution validation. Pure, deterministic, fail closed."""
import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
NAMES = ["Ryan", "Yaz", "Graham", "Bill", "Clara", "Nardole", "Amy", "Rory", "River"]
FORBIDDEN = {"change_A0_finality", "promote_own_work", "bypass_gate",
             "claim_Doctor_authority", "mutate_worldstate_directly"}
ALLOWED = {"propose", "execute_scoped", "emit_evidence"}
ROLES = ["Rick", "Doctor13", "Doctor11", "Doctor12", *NAMES]
HOME = {name: ("Doctor13" if i < 3 else "Doctor12" if i < 6 else "Doctor11")
        for i, name in enumerate(NAMES)}

def load_constitution(path=None):
    return json.loads(Path(path or HERE / "COMPANIONS_CONSTITUTION.json").read_text(encoding="utf-8"))

def validate_constitution(document):
    errors = []
    companions = document.get("companions", [])
    if not isinstance(companions, list) or len(companions) != 9:
        raise ValueError("Exactly nine companion records required")
    if [c.get("name") for c in companions] != NAMES:
        errors.append("Canonical companion identities and order required")
    if any(type(c.get("position")) is not int for c in companions) or [c.get("position") for c in companions] != list(range(1, 10)):
        errors.append("Positions must be unique integers 1..9 in canonical order")
    ids = [c.get("id") for c in companions]
    if len(set(ids)) != 9 or not all(isinstance(x, str) and x for x in ids):
        errors.append("Unique stable identities required")
    topology = document.get("topology", {})
    if topology.get("horizontal") != NAMES + ["WorldState", "Ryan"]:
        errors.append("Canonical loop must close River -> WorldState -> Ryan")
    if topology.get("vertical") != ["A0_Amadeus", "S1_Rick", "Doctors_S2", "Companions_S3"]:
        errors.append("Vertical authority topology changed")
    lanes = []
    for c in companions:
        name = c.get("name")
        required = ["operator", "primary_invariant", "home_core", "adr_triggers",
                    "typed_io", "owned_artifacts", "persistent_lane", "effectors",
                    "watch_signals", "handoffs", "observability"]
        for field in required:
            if not c.get(field):
                errors.append(f"{name}: missing {field}")
        if " of " not in c.get("operator", ""):
            errors.append(f"{name}: X-of-X operator required")
        if c.get("doctor") != HOME.get(name):
            errors.append(f"{name}: home stewardship mismatch")
        if c.get("organization_tier") != "Companion S3":
            errors.append(f"{name}: forbidden organizational authority")
        if "cognitive" not in c.get("system_1_system_2", "").lower():
            errors.append(f"{name}: cognitive capabilities must not become tiers")
        if c.get("home_exclusive") is not False or set(c.get("cross_core_reach", [])) != {"L0", "L1", "L2"}:
            errors.append(f"{name}: home core cannot restrict cross-core reach")
        if not FORBIDDEN.issubset(set(c.get("forbidden_authority", []))):
            errors.append(f"{name}: forbidden authority protection missing")
        grants = set(c.get("authority", []))
        if not grants or not grants.issubset(ALLOWED) or grants & FORBIDDEN:
            errors.append(f"{name}: forbidden authority grant")
        if c.get("name", "").lower() in c.get("effectors", []) or c.get("id") in c.get("effectors", []):
            errors.append(f"{name}: harness cannot be identity")
        if c.get("typed_io") != {"input": "WorkGraphProjection.v1", "output": "EvidenceDelta.v1"}:
            errors.append(f"{name}: typed I/O contract mismatch")
        if name in NAMES:
            nxt = NAMES[NAMES.index(name)+1] if name != "River" else "WorldState"
            if c.get("handoffs", {}).get("next") != nxt:
                errors.append(f"{name}: broken handoff")
        lanes.append(c.get("persistent_lane"))
    if len(set(lanes)) != 9:
        errors.append("Persistent lanes must be unique")
    roles = document.get("projection_roles", {})
    if set(roles) != set(ROLES):
        errors.append("Rick, three Doctors and nine Companions required")
    for name, role in roles.items():
        expected_tier = "S1" if name == "Rick" else "S2" if name.startswith("Doctor") else "S3"
        expected_layers = {"Doctor13": ["L0"], "Doctor11": ["L1"], "Doctor12": ["L2"]}.get(name, ["L0","L1","L2"])
        if role.get("tier") != expected_tier or role.get("layers") != expected_layers:
            errors.append(f"{name}: role authority/scope mismatch")
    if errors:
        raise ValueError("; ".join(errors))
    return document

def validate():
    parser = argparse.ArgumentParser()
    parser.add_argument("--constitution", type=Path)
    args = parser.parse_args()
    try:
        validate_constitution(load_constitution(args.constitution))
    except (ValueError, TypeError, KeyError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        return 1
    print(json.dumps({"ok": True, "companions": 9, "roles": 13, "closed_loop": True}))
    return 0

if __name__ == "__main__":
    raise SystemExit(validate())
