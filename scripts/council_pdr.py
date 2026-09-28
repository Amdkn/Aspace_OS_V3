#!/usr/bin/env python3
"""Create a bounded A'Space PDR packet for Doctor/Companion/Jules delegation."""
from __future__ import annotations
import argparse, json, re
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
POLES=json.loads((ROOT/"10_Tech_OS"/"council"/"PDR_POLES.json").read_text(encoding="utf-8"))
OUT=ROOT/"_INBOX"/"pdr"

def slug(s:str)->str:
    return re.sub(r"[^A-Za-z0-9._-]+","-",s).strip("-")[:80]

def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--origin",required=True)
    ap.add_argument("--pole",required=True,choices=sorted(POLES["capability_poles"]))
    ap.add_argument("--kind",required=True,choices=POLES["work_kinds"])
    ap.add_argument("--outcome",required=True)
    ap.add_argument("--repo-boundary",required=True)
    ap.add_argument("--accept",action="append",required=True)
    ap.add_argument("--dependency",action="append",default=[])
    ap.add_argument("--evidence",action="append",default=[])
    ap.add_argument("--rollback",default="Revert bounded branch/commit; no irreversible side effect authorized.")
    ap.add_argument("--jules-fit",choices=["yes","no","conditional"],default="conditional")
    ap.add_argument("--return-to",required=True)
    a=ap.parse_args()
    pole=POLES["capability_poles"][a.pole]
    ts=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    pid=f"PDR-{ts}-{slug(a.origin)}"
    packet={"schema":"aspace.pdr.v1","pdr_id":pid,"created_at":ts,"origin":a.origin,
      "capability_pole":a.pole,"doctor":pole["doctor"],"work_kind":a.kind,"outcome":a.outcome,
      "repo_boundary":a.repo_boundary,"dependencies":a.dependency,"acceptance":a.accept,
      "evidence_expected":a.evidence,"rollback_boundary":a.rollback,"jules_fit":a.jules_fit,
      "return_to":a.return_to,"status":"READY"}
    OUT.mkdir(parents=True,exist_ok=True)
    path=OUT/(pid+".json")
    path.write_text(json.dumps(packet,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps({"pdr_id":pid,"path":str(path),"doctor":pole["doctor"],"pole":a.pole,"jules_fit":a.jules_fit},indent=2))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
