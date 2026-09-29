#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import shutil
import sys
from pathlib import Path

ALLOWED_PROVIDERS={"claude-cli","codex-cli"}

def read_head(repo: Path) -> str | None:
    head=repo/".git"/"HEAD"
    if not head.exists():
        return None
    value=head.read_text(encoding="utf-8").strip()
    if value.startswith("ref:"):
        ref=repo/".git"/value.split(":",1)[1].strip()
        return ref.read_text(encoding="utf-8").strip() if ref.exists() else value
    return value

def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument("--upstream",type=Path,required=True)
    p.add_argument("--expected-commit",required=True)
    p.add_argument("--provider",required=True)
    p.add_argument("--out",type=Path)
    a=p.parse_args()
    upstream=a.upstream.resolve()
    py_ok=(3,11) <= sys.version_info[:2] < (3,13)
    head=read_head(upstream)
    provider_valid=a.provider in ALLOWED_PROVIDERS
    provider_path=shutil.which(a.provider)
    pyproject=upstream/"pyproject.toml"
    lock=upstream/"uv.lock"
    lock_text=lock.read_text(encoding="utf-8",errors="replace") if lock.exists() else ""
    gpu_markers=[
        "name = \"torch\"",
        "name = \"nvidia-cudnn-cu13\"",
        "name = \"nvidia-nccl-cu13\"",
        "name = \"triton\""
    ]
    result={
        "schema":"aspace.mirofish-adapter-preflight.v1",
        "python_version":".".join(map(str,sys.version_info[:3])),
        "python_range_pass":py_ok,
        "upstream":str(upstream),
        "expected_commit":a.expected_commit,
        "observed_commit":head,
        "source_pin_pass":head==a.expected_commit,
        "provider":a.provider,
        "provider_valid":provider_valid,
        "provider_path":provider_path,
        "provider_alias_pass":bool(provider_path),
        "pyproject_present":pyproject.exists(),
        "uv_lock_present":lock.exists(),
        "heavy_dependency_markers":[m for m in gpu_markers if m in lock_text],
        "global_mutation":False,
        "full_simulation_ready":False
    }
    hard=[
        result["python_range_pass"],
        result["source_pin_pass"],
        result["provider_valid"],
        result["provider_alias_pass"],
        result["pyproject_present"],
        result["uv_lock_present"]
    ]
    result["status"]="READY_FOR_DEPENDENCY_PROFILE" if all(hard) else "BLOCKED"
    result["next"]="Select reproducible lean/full dependency profile before real MiroFish execution."
    text=json.dumps(result,indent=2,ensure_ascii=False)+"\n"
    if a.out:
        a.out.parent.mkdir(parents=True,exist_ok=True)
        a.out.write_text(text,encoding="utf-8")
    print(text,end="")
    return 0 if all(hard) else 2

if __name__=="__main__":
    raise SystemExit(main())
