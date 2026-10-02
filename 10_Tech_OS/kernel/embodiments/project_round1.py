from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC_PATH = HERE / "doctor13_round1.json"
USER = Path(os.environ.get("USERPROFILE", r"C:\Users\amado"))
ADE_JSON = USER / ".aspace" / "orca" / "ADE_REGISTRY.json"
ADE_YAML = USER / ".aspace" / "orca" / "ADE_REGISTRY.yaml"
LAUNCHER_ROOT = USER / ".aspace" / "launchers" / "hermes-bots"
HERMES_PROFILES = USER / ".hermes" / "profiles"
LOCAL_EMBODIMENTS = USER / ".aspace" / "embodiments"
NAMES = ("Ryan", "Yaz", "Graham")
PROFILE = {"Ryan": "ryan", "Yaz": "yaz", "Graham": "graham"}


def sha256(path: Path) -> str | None:
    if not path.exists() or not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def git(args: list[str], cwd: Path) -> tuple[int, str]:
    p = subprocess.run(
        ["git", *args],
        cwd=str(cwd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return p.returncode, p.stdout.strip()


def load_spec() -> dict:
    return json.loads(SPEC_PATH.read_text(encoding="utf-8"))


def backup(paths: list[Path]) -> Path:
    stamp = datetime.now().astimezone().strftime("%Y%m%d-%H%M%S%z")
    dst = USER / ".aspace" / "backups" / f"embodiment-round1-{stamp}"
    dst.mkdir(parents=True, exist_ok=False)
    for src in paths:
        if src.exists():
            shutil.copy2(src, dst / src.name)
    return dst


def project_local_manifests(spec: dict) -> list[Path]:
    written: list[Path] = []
    for name in NAMES:
        h = spec["holons"][name]
        worktree = Path(h["home"]["workspace"])
        manifest = {
            "schema_version": 1,
            "source": {
                "wargame_issue": spec["wargame_issue"],
                "canonical_spec": str(SPEC_PATH).replace("\\", "/"),
                "projected_at": datetime.now().astimezone().isoformat(),
            },
            "identity": h["identity"],
            "home": h["home"],
            "runtime_affinity": h["runtime_affinity"],
            "presence": h["presence"],
            "continuity": {
                "active_work_id": None,
                "correlation_id": None,
                "current_binding": None,
                "session_lineage": [],
                "recent_receipts": [],
                "return_to": None,
            },
            "physical_fingerprint": {
                "AGENTS.md": sha256(worktree / "AGENTS.md"),
                "CLAUDE.md": sha256(worktree / "CLAUDE.md"),
                "GEMINI.md": sha256(worktree / "GEMINI.md"),
                "MEMORY.md": sha256(worktree / "MEMORY.md"),
            },
        }
        out = LOCAL_EMBODIMENTS / name / "manifest.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        written.append(out)
    return written


def repair_hermes_routing() -> Path:
    launchers = [LAUNCHER_ROOT / f"{name}.cmd" for name in NAMES]
    backup_dir = backup([ADE_JSON, ADE_YAML, *launchers])

    registry = json.loads(ADE_JSON.read_text(encoding="utf-8-sig"))
    for name in NAMES:
        if name not in registry["roles"]:
            raise RuntimeError(f"Missing ADE role {name}")
        registry["roles"][name]["profile"] = PROFILE[name]
    ADE_JSON.write_text(
        json.dumps(registry, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    yaml_text = ADE_YAML.read_text(encoding="utf-8-sig")
    replacements = {
        "ryan_build_l0": "ryan",
        "yaz_spec_l0": "yaz",
        "graham_spawn_l0": "graham",
    }
    for old, new in replacements.items():
        yaml_text = yaml_text.replace(f"profile: {old}", f"profile: {new}")
    ADE_YAML.write_text(yaml_text, encoding="utf-8")

    for name in NAMES:
        launcher = LAUNCHER_ROOT / f"{name}.cmd"
        text = launcher.read_text(encoding="utf-8-sig")
        text2, count = re.subn(r"(?<=\s-p\s)[^\s]+", PROFILE[name], text, count=1)
        if count != 1:
            raise RuntimeError(f"Could not rewrite profile in {launcher}")
        launcher.write_text(text2, encoding="utf-8")

    return backup_dir


def validate(spec: dict) -> dict:
    result = {
        "wargame_issue": spec["wargame_issue"],
        "round": spec["round"],
        "checked_at": datetime.now().astimezone().isoformat(),
        "holons": {},
        "shared_prompt_findings": {},
        "round1_status": "PASS",
        "next_gate": "CONTEXT_COMPILER_AND_HARNESS_ADAPTERS",
    }

    registry = json.loads(ADE_JSON.read_text(encoding="utf-8-sig"))
    claude_hashes = {}
    agents_hashes = {}
    gemini_hashes = {}
    memory_hashes = {}

    for name in NAMES:
        h = spec["holons"][name]
        worktree = Path(h["home"]["workspace"])
        profile = PROFILE[name]
        launcher = LAUNCHER_ROOT / f"{name}.cmd"
        manifest = LOCAL_EMBODIMENTS / name / "manifest.json"

        rc, branch = git(["status", "--short", "--branch"], worktree) if worktree.exists() else (1, "")
        launcher_text = launcher.read_text(encoding="utf-8-sig") if launcher.exists() else ""

        checks = {
            "worktree_exists": worktree.exists(),
            "canonical_profile_exists": (HERMES_PROFILES / profile / "IDENTITY.md").exists()
            and (HERMES_PROFILES / profile / "SOUL.md").exists(),
            "ade_registry_profile_matches": registry["roles"].get(name, {}).get("profile") == profile,
            "launcher_profile_matches": bool(re.search(rf"\s-p\s+{re.escape(profile)}(?:\s|$)", launcher_text)),
            "local_manifest_exists": manifest.exists(),
            "git_status_readable": rc == 0,
        }
        if not all(checks.values()):
            result["round1_status"] = "FAIL"

        claude_hashes[name] = sha256(worktree / "CLAUDE.md")
        agents_hashes[name] = sha256(worktree / "AGENTS.md")
        gemini_hashes[name] = sha256(worktree / "GEMINI.md")
        memory_hashes[name] = sha256(worktree / "MEMORY.md")

        result["holons"][name] = {
            "profile": profile,
            "checks": checks,
            "git_status": branch,
            "institutional_state": h["identity"]["institutional_state"],
            "embodiment_state": "READY_ROUND1" if all(checks.values()) else "DEGRADED",
            "runtime_state": "NOT_STARTED_BY_ROUND1",
        }

    def collision(mapping: dict[str, str | None]) -> bool:
        vals = [v for v in mapping.values() if v]
        return len(vals) == len(NAMES) and len(set(vals)) == 1

    result["shared_prompt_findings"] = {
        "AGENTS.md_identical_all_three": collision(agents_hashes),
        "CLAUDE.md_identical_all_three": collision(claude_hashes),
        "GEMINI.md_identical_all_three": collision(gemini_hashes),
        "MEMORY.md_identical_all_three": collision(memory_hashes),
        "claude_code_adapter": "BLOCKED_SHARED_IDENTITY_PROJECTION"
        if collision(claude_hashes)
        else "NEEDS_ADAPTER_VALIDATION",
        "antigravity_adapter": "PARTIAL_NEEDS_IDENTITY_PROJECTION"
        if len(set(v for v in gemini_hashes.values() if v)) < len(NAMES)
        else "NEEDS_ADAPTER_VALIDATION",
        "codex_adapter": "PARTIAL_UNBOUND_NATIVE_AGENTS",
        "hermes_orca": "READY_FOR_NON_DESTRUCTIVE_START_CANARY"
        if result["round1_status"] == "PASS"
        else "DEGRADED",
    }

    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", action="store_true")
    ap.add_argument("--repair-hermes-routing", action="store_true")
    ap.add_argument("--validate", action="store_true")
    args = ap.parse_args()

    spec = load_spec()

    if args.repair_hermes_routing:
        print("BACKUP", repair_hermes_routing())

    if args.project:
        for p in project_local_manifests(spec):
            print("PROJECTED", p)

    if args.validate:
        result = validate(spec)
        evidence = HERE / "doctor13_round1_evidence.json"
        evidence.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result["round1_status"] == "PASS" else 2

    if not (args.project or args.repair_hermes_routing or args.validate):
        ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
