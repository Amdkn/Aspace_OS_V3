#!/usr/bin/env python3
from __future__ import annotations
import argparse,subprocess,sys,time
from pathlib import Path

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--child",action="store_true"); p.add_argument("--artifact")
    p.add_argument("--delay",type=float,default=.4); p.add_argument("--parent-lifetime",type=float,default=5)
    p.add_argument("--child-lifetime",type=float,default=5); a=p.parse_args()
    if a.child:
        time.sleep(a.delay)
        if a.artifact:
            q=Path(a.artifact); q.parent.mkdir(parents=True,exist_ok=True); q.write_text("fixture-artifact\n",encoding="utf-8")
        time.sleep(max(0,a.child_lifetime-a.delay)); return 0
    cmd=[sys.executable,__file__,"--child","--delay",str(a.delay),"--child-lifetime",str(a.child_lifetime)]
    if a.artifact: cmd+=["--artifact",a.artifact]
    subprocess.Popen(cmd,stdin=subprocess.DEVNULL); time.sleep(a.parent_lifetime); return 0

if __name__=="__main__": raise SystemExit(main())
