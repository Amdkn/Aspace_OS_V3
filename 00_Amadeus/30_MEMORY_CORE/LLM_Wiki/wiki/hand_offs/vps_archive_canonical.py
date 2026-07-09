#!/usr/bin/env python3
"""vps_archive_canonical.py — Build a canonical-source TGZ of the VPS for local extraction.

Excludes noise (node_modules, .git/objects, caches, .npm, .nvm, build artifacts).
Keeps source code, .md docs, configs, services, caddy, scripts.

USAGE on VPS:
  python3 /tmp/vps_archive_canonical.py
  # Output: /tmp/vps-canonical-2026-06-17.tgz
"""
import os
import sys
import tarfile
import time
from pathlib import Path

OUT = Path("/tmp/vps-canonical-2026-06-17.tgz")
NOW = time.strftime("%Y-%m-%dT%H:%M:%SZ")

# Directories to INCLUDE (canonical source)
INCLUDES = [
    "/home/amadeus/50_SERVICES",
    "/home/amadeus/.claude",
    "/home/amadeus/.config",
    "/home/amadeus/.hermes",
    "/home/amadeus/.local/share",
    "/home/amadeus/.ssh",
    "/home/amadeus/cli-printing-press",
    "/home/amadeus/hermes-desktop",
    "/home/amadeus/hermes-office",
    "/home/amadeus/hermes-workspace",
    "/home/amadeus/agent-os",
    "/home/amadeus/.antigravity",
    "/home/amadeus/.antigravity_cockpit",
    "/home/amadeus/.antigravity-ide",
    "/home/amadeus/.antigravitycli",
    "/home/amadeus/.agent",
    "/home/amadeus/.agents",
    "/home/amadeus/.codex",
    "/home/amadeus/.codex-agents",
    "/home/amadeus/.copilot",
    "/home/amadeus/.cursor",
    "/home/amadeus/.gemini",
    "/home/amadeus/.kimi",
    "/home/amadeus/.mcp_servers",
    "/home/amadeus/.opencode",
    "/home/amadeus/.openclaw",
    "/home/amadeus/.openharness",
    "/home/amadeus/.skills",
    "/home/amadeus/.vscode-server/cli",
    "/home/amadeus/50_SERVICES",
    "/home/amadeus/go/src",
    "/home/amadeus/projects",
    "/home/amadeus/work",
    "/srv/aspace/00_ORIGIN",
    "/srv/aspace/10_FORGE",
    "/srv/aspace/20_RUNTIME",
    "/srv/aspace/30_MEMORY_CORE",
    "/srv/aspace/40_SKILLS",
    "/srv/aspace/90_SETUP",
    "/srv/aspace/dashboard",
    "/srv/aspace/hermes-workspace",
    "/srv/aspace/main",
    "/srv/aspace/services",
    "/srv/aspace/supabase",
    "/srv/aspace/vault",
    "/srv/aspace/web",
    "/etc/caddy",
    "/etc/systemd/system",
    "/var/lib/caddy/.local/share/caddy",
    "/opt",
]

# Exclusion patterns (relative path substrings or absolute prefixes)
EXCLUDE_PATTERNS = [
    "node_modules",
    "/.git/objects",
    "/.git/lfs",
    "/.git/logs",
    "/.git/refs",
    "/.git/hooks",
    "/.git/info",
    "dist/",
    "build/",
    ".next/",
    ".nuxt/",
    ".cache/",
    "/.cache/",
    "/.npm/",
    "/.npm",
    "/.nvm/",
    "/.nvm",
    "/.local/share/Trash",
    "/.local/share/gvfs",
    "/.local/share/Steam",
    "/.local/share/wayland",
    "/.local/share/xorg",
    "/.antigravity-server",
    "/.antigravity-server/",
    "/vscode-server/extensions",
    "/.vscode-server/extensions",
    "/ms-playwright",
    "/ms-playwright-go",
    "/puppeteer/",
    "/camoufox/",
    "/electron/",
    "gems/",
    "/venv_",
    "/.venv/",
    "/site-packages",
    "/.cargo/registry",
    "/go-build",
    "/go/pkg",
    "/uv/archive",
    "/uv/builds",
    "/uv/sdists",
    "/uv/simple",
    "/uv/wheels",
    "/.claude/projects",
    "/.claude/file-history",
    "/.claude/worktrees",
    "/.claude/plugins",
    "/.claude/remote",
    "/.claude/backups",
    "/.claude/session-data",
    "node_modules",
    "**/__pycache__",
    "**/.pytest_cache",
    "**/.mypy_cache",
    "**/.ruff_cache",
    "**/.ipynb_checkpoints",
    "/paperclip-deprecated-20260513",
    "/dashboard/node_modules",
    "/dashboard/.next",
    "/supabase/.git",
    "/supabase/docker",
    "/supabase/apps",
    "/hermes-workspace/.git",
    "/hermes-workspace/node_modules",
    "/hermes-workspace/electron",
    "/hermes-workspace/public",
    "/hermes-workspace/screenshots",
    "/web/Life-OS-2026/node_modules",
    "/vault/30_MEMORY_CORE",
    "/vault/00_ORIGIN",
    "/vault/session-auth",
    "/30_MEMORY_CORE/LLM_Wiki",
    "/30_MEMORY_CORE/graphify-out",
    "/30_MEMORY_CORE/Claude Export",
    "/30_MEMORY_CORE/_TRASH",
    "/_TRASH",
    "/alerts",
    "/docs/",
    "/main/.git",
    "/openclaw",
    "/hermes-agent/node_modules",
    "/hermes-agent/dist",
    "/hermes-agent/.git",
    "/.hermes/hermes-agent/node_modules",
    "/.hermes/hermes-agent/dist",
    "/.hermes/hermes-agent/.git",
    "/.hermes/checkpoints",
    "/.hermes/registry",
    "/.openharness/autopilot/runs",
    "/.openharness/plugins",
    "/.hermes/hermes-agent/data",
    "/.hermes/registry",
    "/skills/.cache",
    "/.skills",
]

# Specific files to exclude (absolute paths)
EXCLUDE_FILES = [
    "/home/amadeus/.bash_history",
    "/home/amadeus/.python_history",
    "/home/amadeus/.lesshst",
    "/home/amadeus/.viminfo",
    "/home/amadeus/.wget-hsts",
    "/home/amadeus/.gitconfig.lock",
]

# Max file size to include (skip huge logs/dumps)
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500 MB


def should_exclude(path: Path, is_dir: bool) -> bool:
    p = str(path)
    for pat in EXCLUDE_PATTERNS:
        if pat in p:
            return True
    for f in EXCLUDE_FILES:
        if p == f:
            return True
    return False


def add_directory(tar, src_root: Path, arcname_prefix: str):
    """Add a directory tree to tar, respecting exclusions and max file size."""
    if not src_root.exists():
        print(f"  SKIP (not found): {src_root}")
        return 0

    count = 0
    for root, dirs, files in os.walk(src_root, followlinks=False):
        root_path = Path(root)
        # Filter dirs in-place to skip them
        dirs[:] = [d for d in dirs if not should_exclude(root_path / d, True)]
        for f in files:
            fpath = root_path / f
            if should_exclude(fpath, False):
                continue
            try:
                if fpath.stat().st_size > MAX_FILE_SIZE:
                    print(f"  SKIP (too large): {fpath}")
                    continue
            except OSError:
                continue
            # arcname: strip leading / and prepend prefix
            rel = fpath.relative_to(src_root)
            arcname = f"{arcname_prefix}/{rel}"
            try:
                tar.add(fpath, arcname=arcname, recursive=False)
                count += 1
            except OSError as e:
                print(f"  SKIP (error): {fpath} - {e}")
    return count


def main():
    if OUT.exists():
        OUT.unlink()
    print(f"Building {OUT} (started {NOW})")
    t0 = time.time()
    total = 0
    with tarfile.open(OUT, "w:gz", compresslevel=6) as tar:
        for src in INCLUDES:
            src_path = Path(src)
            # Strip leading / for arcname prefix
            arcname_prefix = src.lstrip("/")
            print(f"  Adding {src}...")
            n = add_directory(tar, src_path, arcname_prefix)
            total += n
            print(f"    {n} files")
    elapsed = round(time.time() - t0, 1)
    size_mb = OUT.stat().st_size / 1024 / 1024
    print(f"\nDONE: {OUT}")
    print(f"  files: {total}")
    print(f"  size: {size_mb:.1f} MB")
    print(f"  elapsed: {elapsed}s")


if __name__ == "__main__":
    main()
