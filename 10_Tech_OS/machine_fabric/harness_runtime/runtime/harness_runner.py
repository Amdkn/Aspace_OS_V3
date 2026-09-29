#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os,subprocess
from datetime import datetime,timezone
from pathlib import Path
def now(): return datetime.now(timezone.utc).isoformat()
def write(path,payload):
    path=Path(path); tmp=path.with_suffix(path.suffix+".tmp")
    tmp.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8"); os.replace(tmp,path)
def main():
    p=argparse.ArgumentParser(); p.add_argument("--status",required=True); p.add_argument("--cwd",required=True); p.add_argument("command",nargs=argparse.REMAINDER)
    a=p.parse_args(); cmd=a.command[1:] if a.command and a.command[0]=="--" else a.command
    if not cmd: raise SystemExit("missing command")
    child=subprocess.Popen(cmd,cwd=a.cwd,stdin=subprocess.DEVNULL)
    write(a.status,{"state":"running","runner_pid":os.getpid(),"child_pid":child.pid,"started_at":now(),"command":cmd})
    rc=child.wait(); write(a.status,{"state":"finished","runner_pid":os.getpid(),"child_pid":child.pid,"returncode":rc,"finished_at":now(),"command":cmd}); return rc
if __name__=="__main__": raise SystemExit(main())
