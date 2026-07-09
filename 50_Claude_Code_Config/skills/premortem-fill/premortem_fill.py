#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
premortem_fill.py — D6 inventory + auto-fill for a target.

Doctrine:
- D1 verify before assert (no claim without file read)
- SAFE_AUTO executes, A0_GO_REQUIRED queues, BLOCKED flags
- Anti-forgetting via SessionStart hook that scans pending_actions.md files

Usage:
    python premortem_fill.py <target> [--type plugin|mcp|service|system] [--dry-run]

Phase 2 (Hermes-style self-improvement) per CLAUDE.md §Skill Creator Reflex.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ─────────────────────────────────────────────────────────────────────────────
# Paths (constants — no hardcoded user paths beyond A0's known location)
# ─────────────────────────────────────────────────────────────────────────────

HOME = Path(os.environ.get("USERPROFILE") or os.path.expanduser("~"))
CLAUDE_DIR = HOME / ".claude"
SETTINGS_JSON = CLAUDE_DIR / "settings.json"
MCP_JSON = HOME / ".mcp.json"
MEMORY_MD = CLAUDE_DIR / "projects" / "c--Users-amado" / "memory" / "MEMORY.md"
MINDSETS_DIR = CLAUDE_DIR / "mindsets"
HANDOFFS_DIR = (
    HOME / "ASpace_OS_V2" / "00_Amadeus" / "30_MEMORY_CORE" / "LLM_Wiki" / "wiki" / "hand_offs"
)
HOOK_SCRIPT = CLAUDE_DIR / "hooks" / "sessionstart-premortem-pending-detector.ps1"

# ─────────────────────────────────────────────────────────────────────────────
# ANSI helpers
# ─────────────────────────────────────────────────────────────────────────────

GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
CYAN = "\033[36m"
DIM = "\033[2m"
RESET = "\033[0m"


def log(level: str, msg: str) -> None:
    prefix = {
        "info": f"{CYAN}[premortem-fill]{RESET}",
        "ok": f"{GREEN}[premortem-fill ✓]{RESET}",
        "warn": f"{YELLOW}[premortem-fill ⚠]{RESET}",
        "err": f"{RED}[premortem-fill ✗]{RESET}",
    }[level]
    print(f"{prefix} {msg}")


# ─────────────────────────────────────────────────────────────────────────────
# D1 Inventory helpers
# ─────────────────────────────────────────────────────────────────────────────


def safe_read_json(path: Path) -> dict[str, Any] | None:
    """D1: read JSON file safely, return None if not parseable."""
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        log("warn", f"could not parse {path}: {e}")
        return None


def safe_read_text(path: Path) -> str | None:
    if not path.exists():
        return None
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def run_cmd(cmd: str, timeout: int = 10) -> tuple[int, str, str]:
    """Run a shell command, return (returncode, stdout, stderr)."""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=timeout
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return 124, "", "TIMEOUT"
    except OSError as e:
        return 1, "", str(e)


def get_npm_globals() -> list[str]:
    rc, out, _ = run_cmd("npm ls -g --depth=0 2>/dev/null")
    if rc != 0:
        return []
    return [
        line.strip().lstrip("+-").strip().split("@", 1)[0]
        for line in out.splitlines()
        if "@" in line and not line.startswith("npm")
    ]


def get_user_env_vars() -> dict[str, str]:
    """Get User-scope env vars on Windows via PowerShell."""
    if sys.platform != "win32":
        return dict(os.environ)
    rc, out, _ = run_cmd(
        "powershell -NoProfile -Command \"[System.Environment]::GetEnvironmentVariables('User') | ConvertTo-Json -Compress\""
    )
    if rc != 0 or not out.strip():
        return {}
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return {}


def grep_files(pattern: str, paths: list[Path]) -> list[tuple[Path, int, str]]:
    """Grep pattern in files, return list of (path, line_number, matching_line)."""
    matches = []
    for p in paths:
        if not p.exists() or p.is_dir():
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if re.search(pattern, line, re.IGNORECASE):
                matches.append((p, i, line.strip()))
    return matches


# ─────────────────────────────────────────────────────────────────────────────
# Phase 1 — D1 Inventory
# ─────────────────────────────────────────────────────────────────────────────


def d1_inventory(target: str) -> dict[str, Any]:
    """D1 verify current state of target across all config surfaces."""
    log("info", f"Phase 1 — D1 inventory of '{target}'")
    state: dict[str, Any] = {
        "target": target,
        "ts": datetime.now(timezone.utc).isoformat(),
    }

    # settings.json
    settings = safe_read_json(SETTINGS_JSON) or {}
    enabled = settings.get("enabledPlugins", {})
    state["enabledPlugins"] = {
        k: v for k, v in enabled.items() if target.lower() in k.lower()
    }
    state["hooks"] = list(settings.get("hooks", {}).keys())

    # .mcp.json
    mcp = safe_read_json(MCP_JSON) or {}
    servers = mcp.get("mcpServers", {})
    state["mcpServers"] = {
        k: v for k, v in servers.items() if target.lower() in k.lower()
    }

    # CLAUDE.md references
    claude_md = safe_read_text(CLAUDE_DIR / "CLAUDE.md")
    if claude_md:
        state["claude_md_refs"] = [
            i for i, line in enumerate(claude_md.splitlines(), 1)
            if target.lower() in line.lower()
        ]

    # MEMORY.md references
    memory_md = safe_read_text(MEMORY_MD)
    if memory_md:
        state["memory_md_refs"] = [
            i for i, line in enumerate(memory_md.splitlines(), 1)
            if target.lower() in line.lower()
        ]

    # Prior handoffs
    if HANDOFFS_DIR.exists():
        matches = list(HANDOFFS_DIR.glob(f"*{target}*"))
        state["prior_handoffs"] = [str(m.relative_to(HOME)) for m in matches]

    # mindsets canon
    if MINDSETS_DIR.exists():
        state["mindsets_canon"] = sorted([
            str(m.relative_to(MINDSETS_DIR)) for m in MINDSETS_DIR.glob(f"*{target}*")
        ])

    # npm globals
    state["npm_globals"] = [
        p for p in get_npm_globals() if target.lower() in p.lower()
    ]

    # env vars
    env = get_user_env_vars()
    state["env_vars"] = {k: "<redacted>" if "TOKEN" in k.upper() or "KEY" in k.upper() else v
                        for k, v in env.items() if target.upper() in k.upper() or target.upper() in k.upper()}

    return state


# ─────────────────────────────────────────────────────────────────────────────
# Phase 2 — Failure Mode Generation (D6)
# ─────────────────────────────────────────────────────────────────────────────


def generate_failure_modes(target: str, state: dict[str, Any]) -> list[dict[str, Any]]:
    """D6 root-cause-style: synthesize F1-F15 from state map."""
    log("info", "Phase 2 — generating F1-F15 failure modes")
    modes: list[dict[str, Any]] = []

    # Pillar 1 — Channel hardening
    if not state.get("enabledPlugins") and not state.get("mcpServers"):
        modes.append({
            "id": "F1", "pillar": "Channel hardening",
            "mode": "Plugin disabled in settings.json",
            "evidence": f"enabledPlugins has no entry for {target}",
            "blast": "high",
            "remediation_class": "A0_GO_REQUIRED",
        })
    if state.get("enabledPlugins") and not state.get("mcpServers"):
        modes.append({
            "id": "F2", "pillar": "Channel hardening",
            "mode": "Plugin enabled but no .mcp.json entry",
            "evidence": f"{target} in enabledPlugins but not in mcpServers",
            "blast": "high",
            "remediation_class": "A0_GO_REQUIRED",
        })
    if state.get("mcpServers") and not state.get("npm_globals") and not state.get("env_vars"):
        modes.append({
            "id": "F3", "pillar": "Channel hardening",
            "mode": "MCP server configured but binary missing",
            "evidence": f".mcp.json references {target} but npm global not found",
            "blast": "high",
            "remediation_class": "BLOCKED",
        })

    # Pillar 2 — Watchdog + DLQ
    modes.append({
        "id": "F4", "pillar": "Watchdog + DLQ",
        "mode": "No failure detection mechanism",
        "evidence": "No watchdog cron configured for target",
        "blast": "medium",
        "remediation_class": "A0_GO_REQUIRED",
    })
    modes.append({
        "id": "F5", "pillar": "Watchdog + DLQ",
        "mode": "No DLQ for unrecoverable failures",
        "evidence": f"wiki/hand_offs/{target}_premortem_pending_actions.md does not exist",
        "blast": "low",
        "remediation_class": "SAFE_AUTO",
    })
    modes.append({
        "id": "F6", "pillar": "Watchdog + DLQ",
        "mode": "No heartbeat / health-check cadence",
        "evidence": "No cron entry for target health-check",
        "blast": "low",
        "remediation_class": "A0_GO_REQUIRED",
    })

    # Pillar 3 — Anti-paperclip
    modes.append({
        "id": "F7", "pillar": "Anti-paperclip",
        "mode": "Auto-execution chain risk",
        "evidence": "If target can dispatch sub-agents, verify A0 HITL gate present",
        "blast": "high",
        "remediation_class": "SAFE_AUTO",
    })
    modes.append({
        "id": "F8", "pillar": "Anti-paperclip",
        "mode": "Prompt injection surface",
        "evidence": "If target reads user-supplied content, verify injection guard",
        "blast": "high",
        "remediation_class": "SAFE_AUTO",
    })

    # Pillar 4 — Recovery
    modes.append({
        "id": "F9", "pillar": "Recovery",
        "mode": "No snapshot/rollback mechanism",
        "evidence": "Deep Checkpoint Law not yet documented for target",
        "blast": "medium",
        "remediation_class": "SAFE_AUTO",
    })
    modes.append({
        "id": "F10", "pillar": "Recovery",
        "mode": "No orphan process detection",
        "evidence": "No list_processes cadence at session start",
        "blast": "low",
        "remediation_class": "SAFE_AUTO",
    })

    # Pillar 5 — Activation drift
    if state.get("enabledPlugins") or state.get("mcpServers"):
        modes.append({
            "id": "F11", "pillar": "Activation drift",
            "mode": "Capability exists but never activated",
            "evidence": f"Plugin/MCP configured but no prior activation history",
            "blast": "medium",
            "remediation_class": "A0_GO_REQUIRED",
        })
    if state.get("prior_handoffs"):
        modes.append({
            "id": "F12", "pillar": "Activation drift",
            "mode": "Prior handoff(s) may be dead (fix never executed)",
            "evidence": f"Found {len(state['prior_handoffs'])} prior handoffs — auto-fill would surface pending actions",
            "blast": "medium",
            "remediation_class": "SAFE_AUTO",
        })
    if not state.get("mindsets_canon"):
        modes.append({
            "id": "F13", "pillar": "Activation drift",
            "mode": "Missing Mindset/Dispatch canon files",
            "evidence": f"No mindsets/{target}* files exist",
            "blast": "low",
            "remediation_class": "SAFE_AUTO",
        })

    modes.append({
        "id": "F14", "pillar": "Activation drift",
        "mode": "CLAUDE.md does not reference target",
        "evidence": f"CLAUDE.md has {len(state.get('claude_md_refs', []))} refs for {target}",
        "blast": "low",
        "remediation_class": "SAFE_LOG_ONLY",
    })
    modes.append({
        "id": "F15", "pillar": "Activation drift",
        "mode": "MEMORY.md topic table missing entry",
        "evidence": f"MEMORY.md has {len(state.get('memory_md_refs', []))} refs for {target}",
        "blast": "low",
        "remediation_class": "SAFE_AUTO",
    })

    return modes


# ─────────────────────────────────────────────────────────────────────────────
# Phase 3 + 5 — Auto-fill + write artifacts
# ─────────────────────────────────────────────────────────────────────────────


def write_pending_actions(target: str, modes: list[dict[str, Any]]) -> Path:
    """Write the A0_GO_REQUIRED queue."""
    HANDOFFS_DIR.mkdir(parents=True, exist_ok=True)
    out = HANDOFFS_DIR / f"{target}_premortem_pending_actions.md"
    pending = [m for m in modes if m["remediation_class"] == "A0_GO_REQUIRED"]
    lines = [
        f"# Pending A0 Actions — {target} premortem-fill",
        "",
        f"> Generated: {datetime.now(timezone.utc).isoformat()}",
        f"> Target: **{target}**",
        f"> Count: **{len(pending)} actions pending A0 GO**",
        "",
        "## Pending (DO NOT execute without A0 explicit GO)",
        "",
    ]
    for m in pending:
        lines.append(f"### {m['id']} — {m['mode']}")
        lines.append(f"- **Pillar**: {m['pillar']}")
        lines.append(f"- **Evidence**: {m['evidence']}")
        lines.append(f"- **Blast radius**: {m['blast']}")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("To clear a pending action: A0 replies `GO pour <F-id>` then agent executes.")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def write_live_handoff(target: str, state: dict[str, Any], modes: list[dict[str, Any]]) -> Path:
    """Write the LIVE (refreshed on each run) handoff."""
    HANDOFFS_DIR.mkdir(parents=True, exist_ok=True)
    out = HANDOFFS_DIR / f"{target}_premortem_live.md"
    counts: dict[str, int] = {}
    for m in modes:
        counts[m["remediation_class"]] = counts.get(m["remediation_class"], 0) + 1
    lines = [
        f"# {target} premortem — LIVE",
        "",
        f"> **Last refresh**: {datetime.now(timezone.utc).isoformat()}",
        f"> **Generated by**: `/premortem-fill {target}`",
        f"> Re-invoke skill to refresh this file.",
        "",
        "## D1 State (verified this turn)",
        "",
        f"- `enabledPlugins`: {state.get('enabledPlugins', {})}",
        f"- `mcpServers`: {state.get('mcpServers', {})}",
        f"- `npm_globals`: {state.get('npm_globals', [])}",
        f"- `env_vars` (filtered): {state.get('env_vars', {})}",
        f"- `prior_handoffs`: {state.get('prior_handoffs', [])}",
        f"- `mindsets_canon`: {state.get('mindsets_canon', [])}",
        f"- `CLAUDE.md` refs: {len(state.get('claude_md_refs', []))} lines",
        f"- `MEMORY.md` refs: {len(state.get('memory_md_refs', []))} lines",
        "",
        f"## Failure modes: {len(modes)} generated",
        "",
    ]
    for m in modes:
        icon = {
            "SAFE_AUTO": "✓",
            "SAFE_LOG_ONLY": "📝",
            "A0_GO_REQUIRED": "⏸",
            "BLOCKED": "🚫",
        }.get(m["remediation_class"], "?")
        lines.append(f"### {m['id']} {icon} {m['mode']} [{m['remediation_class']}]")
        lines.append(f"- **Pillar**: {m['pillar']}")
        lines.append(f"- **Evidence**: {m['evidence']}")
        lines.append(f"- **Blast**: {m['blast']}")
        lines.append("")
    lines.append("## Remediation class counts")
    lines.append("")
    for cls, n in sorted(counts.items()):
        lines.append(f"- **{cls}**: {n}")
    lines.append("")
    lines.append("## Sister canon")
    lines.append("")
    for m in state.get("mindsets_canon", []):
        lines.append(f"- `mindsets/{m}`")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("Re-invoke `/premortem-fill " + target + "` to refresh this file. SessionStart hook `sessionstart-premortem-pending-detector.ps1` will surface any pending A0_GO_REQUIRED actions at next session start.")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def update_memory_md(target: str, mindset_path: str | None, live_handoff: Path) -> bool:
    """D4 append-only: add 1-line entry to MEMORY.md topic table."""
    text = safe_read_text(MEMORY_MD)
    if not text:
        log("warn", f"MEMORY.md not found at {MEMORY_MD}")
        return False
    if target.lower() in text.lower() and "premortem-fill" in text:
        log("info", "MEMORY.md already references target — skipping")
        return False
    # Find the table line that mentions Telegram HITL canon (insertion anchor)
    anchor = "| **Telegram HITL canon"
    if anchor not in text:
        anchor = "| **Desktop Commander réactivation"
    if anchor not in text:
        log("warn", "no known anchor found in MEMORY.md — append to end")
        text += (
            f"\n| **{target} premortem-fill** | LIVE handoff auto-refreshed on each run by `/premortem-fill {target}` skill. "
            f"Failure modes F1-F15 + pending A0_GO queue. SessionStart hook surfaces pending actions. "
            f"| `{live_handoff.relative_to(HOME)}` + `skills/premortem-fill/` |\n"
        )
    else:
        new_line = (
            f"| **{target} premortem-fill** | LIVE handoff auto-refreshed by `/premortem-fill {target}` skill. "
            f"F1-F15 + pending A0_GO queue. SessionStart hook for anti-forgetting. "
            f"| `{live_handoff.relative_to(HOME)}` + `skills/premortem-fill/` |\n"
        )
        text = text.replace(anchor, new_line + anchor, 1)
    MEMORY_MD.write_text(text, encoding="utf-8")
    return True


def install_sessionstart_hook() -> tuple[bool, str]:
    """Install the anti-forgetting SessionStart hook if not already present."""
    HOOK_SCRIPT.parent.mkdir(parents=True, exist_ok=True)
    if not HOOK_SCRIPT.exists():
        HOOK_SCRIPT.write_text(HOOK_PS1_CONTENT, encoding="utf-8")
        log("ok", f"installed SessionStart hook: {HOOK_SCRIPT}")
    else:
        log("info", f"SessionStart hook already installed at {HOOK_SCRIPT}")
    # Add to settings.json
    settings = safe_read_json(SETTINGS_JSON) or {}
    hooks = settings.setdefault("hooks", {})
    sess = hooks.setdefault("SessionStart", [])
    hook_cmd = (
        f"powershell -NoProfile -ExecutionPolicy Bypass -File "
        f"{HOOK_SCRIPT}"
    )
    already = any(
        h.get("command") == hook_cmd
        for entry in sess
        if isinstance(entry, dict)
        for h in entry.get("hooks", [])
    )
    if already:
        log("info", "SessionStart hook entry already in settings.json")
        return True, "already_present"
    sess.append({
        "hooks": [{"type": "command", "command": hook_cmd, "shell": "powershell", "async": False}]
    })
    SETTINGS_JSON.write_text(json.dumps(settings, indent=2, ensure_ascii=False), encoding="utf-8")
    return True, "added"


# ─────────────────────────────────────────────────────────────────────────────
# Phase 4 — SessionStart hook content (embedded)
# ─────────────────────────────────────────────────────────────────────────────

HOOK_PS1_CONTENT = r"""# sessionstart-premortem-pending-detector.ps1
# Anti-forgetting hook for /premortem-fill skill.
# At session start, scans wiki/hand_offs/*_premortem_pending_actions.md
# and surfaces ⚠️ warnings so A0 cannot forget pending actions.

$ErrorActionPreference = 'SilentlyContinue'

$homedir = $env:USERPROFILE
$handoffsDir = Join-Path $homedir 'ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs'

if (-not (Test-Path $handoffsDir)) {
    return
}

$pendingFiles = Get-ChildItem -Path $handoffsDir -Filter '*_premortem_pending_actions.md' -ErrorAction SilentlyContinue

if (-not $pendingFiles) {
    return
}

Write-Host ''
Write-Host '⚠️  [premortem-fill] pending A0 actions detected:' -ForegroundColor Yellow

foreach ($f in $pendingFiles) {
    $target = $f.BaseName -replace '_premortem_pending_actions$', ''
    $content = Get-Content $f.FullName -Raw
    # Count "### F" markers
    $count = ([regex]::Matches($content, '### F\d+')).Count
    Write-Host "    - $target : $count pending action(s)" -ForegroundColor Yellow
    Write-Host "      file: $($f.FullName)" -ForegroundColor Gray
}

Write-Host ''
Write-Host '  → run `/premortem-fill <target>` to refresh, or `GO pour <F-id>` to act on a specific pending action.' -ForegroundColor Cyan
Write-Host ''
"""


# ─────────────────────────────────────────────────────────────────────────────
# Main entry
# ─────────────────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(description="premortem-fill — D6 inventory + auto-fill")
    parser.add_argument("target", help="Target name (plugin, MCP, service, system)")
    parser.add_argument("--type", choices=["plugin", "mcp", "service", "system"], default="plugin")
    parser.add_argument("--dry-run", action="store_true", help="Don't write any files, just print state")
    args = parser.parse_args()

    target = args.target.strip()
    log("info", f"Target: {target} (type={args.type})")

    # Phase 1
    state = d1_inventory(target)
    log("ok", f"D1 state: {len(state.get('enabledPlugins', {}))} enabledPlugins, "
        f"{len(state.get('mcpServers', {}))} mcpServers, "
        f"{len(state.get('prior_handoffs', []))} prior handoffs, "
        f"{len(state.get('mindsets_canon', []))} mindsets canon")

    # Phase 2
    modes = generate_failure_modes(target, state)
    log("ok", f"Failure modes: {len(modes)} generated, D1 verified")

    if args.dry_run:
        log("info", "dry-run mode — printing state only")
        print(json.dumps({"state": state, "modes": modes}, indent=2, ensure_ascii=False))
        return 0

    # Phase 3 + 5 — Write artifacts
    pending_path = write_pending_actions(target, modes)
    log("ok", f"Pending actions: {pending_path.relative_to(HOME)}")

    live_path = write_live_handoff(target, state, modes)
    log("ok", f"Live handoff: {live_path.relative_to(HOME)}")

    # MEMORY.md update
    if update_memory_md(target, None, live_path):
        log("ok", "MEMORY.md: updated topic table")
    else:
        log("info", "MEMORY.md: skipped (already references or anchor missing)")

    # SessionStart hook install
    installed, status = install_sessionstart_hook()
    log("ok" if installed else "warn", f"SessionStart hook: {status}")

    # Summary
    counts: dict[str, int] = {}
    for m in modes:
        counts[m["remediation_class"]] = counts.get(m["remediation_class"], 0) + 1
    log("info", "Remediation class counts:")
    for cls in ("SAFE_AUTO", "SAFE_LOG_ONLY", "A0_GO_REQUIRED", "BLOCKED"):
        if counts.get(cls):
            log("info", f"  - {cls}: {counts[cls]}")

    log("info", f"Next run: re-invoke `/premortem-fill {target}` to refresh")
    return 0


if __name__ == "__main__":
    sys.exit(main())