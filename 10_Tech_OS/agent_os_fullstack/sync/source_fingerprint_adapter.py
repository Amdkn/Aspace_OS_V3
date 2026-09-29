import subprocess
import os
from datetime import datetime, timezone
from typing import List, Optional
from ..api.projection_gateway import SourceFingerprint, NestedSourceFingerprint

def _run_git_cmd(cmd: List[str], cwd: str) -> Optional[str]:
    try:
        result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def gather_fingerprint(repo_root: str, world_id: str = "agent_os") -> SourceFingerprint:
    """
    Gathers git source state including nested repositories (e.g. desktop).
    """
    fp = SourceFingerprint(world_id=world_id, observed_at=datetime.now(timezone.utc).isoformat())

    # Parent repo
    parent_head = _run_git_cmd(['git', 'rev-parse', 'HEAD'], repo_root)
    parent_branch = _run_git_cmd(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], repo_root)
    parent_status = _run_git_cmd(['git', 'status', '--porcelain'], repo_root)
    parent_repo = _run_git_cmd(['git', 'config', '--get', 'remote.origin.url'], repo_root)

    fp.parent_head = parent_head or "unknown"
    fp.parent_branch = parent_branch
    fp.parent_dirty = bool(parent_status)
    fp.parent_repo = parent_repo or "unknown"

    # Nested repos (submodules or just nested git folders)
    # Using git ls-files to find gitlinks, or simply checking known paths like agent-os/desktop
    desktop_path = os.path.join(repo_root, "agent-os", "desktop")
    if os.path.exists(os.path.join(desktop_path, ".git")):
        nested_head = _run_git_cmd(['git', 'rev-parse', 'HEAD'], desktop_path)
        nested_status = _run_git_cmd(['git', 'status', '--porcelain'], desktop_path)
        nested_branch = _run_git_cmd(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], desktop_path)

        # Check what parent thinks the committed gitlink is
        committed_gitlink = None
        ls_tree = _run_git_cmd(['git', 'ls-tree', 'HEAD', 'agent-os/desktop'], repo_root)
        if ls_tree:
            parts = ls_tree.split()
            if len(parts) >= 3 and parts[1] == 'commit':
                committed_gitlink = parts[2]

        fp.nested.append(NestedSourceFingerprint(
            path="agent-os/desktop",
            observed_head=nested_head or "unknown",
            dirty=bool(nested_status),
            branch=nested_branch,
            committed_gitlink=committed_gitlink,
            worktree=desktop_path
        ))

    return fp
