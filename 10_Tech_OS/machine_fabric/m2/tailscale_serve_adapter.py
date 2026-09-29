#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os,shutil,subprocess,tempfile,time
from pathlib import Path
from typing import Any

SCHEMA="aspace.machine.remote-transport-evidence.v1"

class RemoteTransportError(RuntimeError):pass

def find_tailscale(explicit=None):
    candidates=[]
    if explicit:candidates.append(explicit)
    which=shutil.which("tailscale")
    if which:candidates.append(which)
    candidates += [
      r"C:\Program Files\Tailscale\tailscale.exe",
      r"C:\Program Files (x86)\Tailscale\tailscale.exe",
      str(Path.home()/r"AppData\Local\Tailscale\tailscale.exe")
    ]
    for raw in candidates:
        p=Path(raw)
        if p.exists():return [str(p.resolve())]
    return None

class TailscaleServeAdapter:
    def __init__(self,cli):
        if not cli:raise RemoteTransportError("tailscale CLI unavailable")
        self.cli=[str(x) for x in cli]
    def run(self,args,timeout=20):
        cp=subprocess.run(self.cli+list(args),text=True,capture_output=True,timeout=timeout)
        return {"returncode":cp.returncode,"stdout":cp.stdout,"stderr":cp.stderr,"argv":self.cli+list(args)}
    def status(self):
        r=self.run(["serve","status","--json"])
        if r["returncode"]!=0:return {"state":"UNAVAILABLE","command":r}
        try:data=json.loads(r["stdout"] or "{}")
        except json.JSONDecodeError:return {"state":"DEGRADED","command":r,"error":"invalid status json"}
        return {"state":"AVAILABLE","config":data,"command":r}
    def snapshot(self,path):
        p=Path(path).resolve()
        r=self.run(["serve","get-config",str(p),"--all"])
        if r["returncode"]!=0:raise RemoteTransportError("get-config failed: "+r["stderr"][-500:])
        return p
    def restore(self,path):
        p=Path(path).resolve()
        r=self.run(["serve","set-config",str(p),"--all"])
        if r["returncode"]!=0:raise RemoteTransportError("set-config failed: "+r["stderr"][-500:])
        return r
    def start_private(self,backend_port,https_port=443):
        if not (1<=int(backend_port)<=65535 and 1<=int(https_port)<=65535):raise ValueError("invalid port")
        target=f"http://127.0.0.1:{int(backend_port)}"
        args=["serve","--bg",f"--https={int(https_port)}",target]
        if any("funnel" in x.lower() for x in args):raise RemoteTransportError("public Funnel forbidden")
        r=self.run(args,timeout=30)
        if r["returncode"]!=0:raise RemoteTransportError("serve start failed: "+(r["stderr"] or r["stdout"])[-800:])
        return r
    def stop_private(self,https_port=443):
        r=self.run(["serve",f"--https={int(https_port)}","off"])
        if r["returncode"]!=0:raise RemoteTransportError("serve stop failed: "+r["stderr"][-500:])
        return r

def preflight(explicit=None):
    cli=find_tailscale(explicit)
    if not cli:
        return {"schema":SCHEMA,"result":"DEPENDENCY_MISSING","dependency":"tailscale","installed":False,"live_canary":"OPEN","reason":"No Tailscale CLI/service installed on this Windows host.","public_bind":False}
    a=TailscaleServeAdapter(cli); s=a.status()
    return {"schema":SCHEMA,"result":"READY" if s["state"]=="AVAILABLE" else "BLOCKED","dependency":"tailscale","installed":True,"cli":cli,"status":s,"live_canary":"OPEN","public_bind":False}

def main():
    p=argparse.ArgumentParser();p.add_argument("--out");p.add_argument("--tailscale");a=p.parse_args()
    r=preflight(a.tailscale);r["at"]=time.time()
    text=json.dumps(r,indent=2)+"\n"
    if a.out:
        q=Path(a.out);q.parent.mkdir(parents=True,exist_ok=True);q.write_text(text,encoding="utf-8")
    print(text,end="")
    return 0
if __name__=="__main__":raise SystemExit(main())
