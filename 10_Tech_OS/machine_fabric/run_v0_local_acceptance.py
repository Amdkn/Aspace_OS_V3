#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os,subprocess,sys,time,winreg
from pathlib import Path

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
REPORTS=REPO/"10_Tech_OS"/"reports"

def run(name,cwd,argv,timeout=120):
    t=time.perf_counter()
    cp=subprocess.run(argv,cwd=str(cwd),text=True,capture_output=True,timeout=timeout)
    return {"name":name,"returncode":cp.returncode,"seconds":round(time.perf_counter()-t,3),"stdout_tail":cp.stdout[-5000:],"stderr_tail":cp.stderr[-5000:]}

def find_cft(explicit=None):
    if explicit:
        p=Path(explicit).resolve()
        if p.exists():return p
    env=os.environ.get("ASPACE_CHROME_FOR_TESTING")
    if env and Path(env).exists():return Path(env).resolve()
    root=Path.home()/"Aspace_Quarantine"/"chrome-for-testing"
    if root.exists():
        xs=sorted(root.glob("*/chrome-win64/chrome.exe"),reverse=True)
        if xs:return xs[0].resolve()
    return None

def registry_clean():
    try:
        k=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Google\Chrome\NativeMessagingHosts\com.aspace.machine_fabric.canary")
        winreg.CloseKey(k);return False
    except FileNotFoundError:return True

def lingering_count():
    ps="$p=Get-CimInstance Win32_Process | Where-Object { $_.Name -match '^(python|pythonw|ASpaceNativeHost)\\.exe$' -and $_.CommandLine -match 'session_daemon.py|user_session_worker.py|ASpaceNativeHost.exe|aspace-m1-canary' }; @($p).Count"
    cp=subprocess.run(["powershell","-NoProfile","-Command",ps],text=True,capture_output=True,timeout=15)
    try:return int(cp.stdout.strip().splitlines()[-1])
    except Exception:return -1

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out",required=True);ap.add_argument("--chrome-for-testing");a=ap.parse_args()
    cft=find_cft(a.chrome_for_testing)
    steps=[]
    steps.append(run("M0",HERE/"m0",[sys.executable,"test_amf_m0.py"],60))
    steps.append(run("P1-P4",HERE/"harness_runtime"/"runtime",[sys.executable,"test_harness_runtime.py"],90))
    steps.append(run("M1-unit",HERE/"m1",[sys.executable,"test_m1.py"],60))
    m1_report=REPORTS/"amf_m1_chrome_evidence_20260929.json"
    if cft:
        steps.append(run("M1-chrome",HERE/"m1",[sys.executable,"run_m1_canary.py","--out",str(m1_report),"--chrome",str(cft)],90))
    else:
        steps.append({"name":"M1-chrome","returncode":2,"seconds":0,"stdout_tail":"","stderr_tail":"Chrome for Testing missing"})
    steps.append(run("M2-adapter",HERE/"m2",[sys.executable,"test_m2.py"],60))
    m2_report=REPORTS/"amf_m2_remote_evidence_20260929.json"
    steps.append(run("M2-preflight",HERE/"m2",[sys.executable,"tailscale_serve_adapter.py","--out",str(m2_report)],30))
    m1=json.loads(m1_report.read_text(encoding="utf-8")) if m1_report.exists() else {}
    m2=json.loads(m2_report.read_text(encoding="utf-8")) if m2_report.exists() else {}
    core_names={"M0","P1-P4","M1-unit","M1-chrome","M2-adapter","M2-preflight"}
    tests_green=all(x["returncode"]==0 for x in steps if x["name"] in core_names)
    local_pass=tests_green and m1.get("result")=="PASS" and registry_clean() and lingering_count()==0
    remote_state="PASS" if m2.get("live_canary")=="PASS" else ("OPEN_DEPENDENCY" if m2.get("result")=="DEPENDENCY_MISSING" else "OPEN")
    result={
      "schema":"aspace.machine.v0-continuous-evidence.v1",
      "result":"LOCAL_V0_PASS_REMOTE_OPEN" if local_pass and remote_state!="PASS" else ("PASS" if local_pass and remote_state=="PASS" else "FAIL"),
      "local_v0_pass":local_pass,
      "remote_gate":remote_state,
      "chrome_for_testing":str(cft) if cft else None,
      "steps":steps,
      "m1_summary":{"result":m1.get("result"),"checks":m1.get("checks"),"receipt":m1.get("receipt")},
      "m2_summary":m2,
      "cleanup":{"temporary_native_host_registry_absent":registry_clean(),"lingering_owned_processes":lingering_count()},
      "gate_sequence":["M0 durable mutation","P1-P4 Harness Runtime","M1 worker+Chrome","M2 private remote live canary"],
      "promotion":"BLOCKED_ONLY_BY_REMOTE_LIVE_CANARY_AND_INDEPENDENT_REVIEW" if local_pass and remote_state!="PASS" else "SEE_RESULT",
      "finished_at":time.time()
    }
    out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"result":result["result"],"remote_gate":remote_state,"steps":[[x["name"],x["returncode"],x["seconds"]] for x in steps],"cleanup":result["cleanup"],"out":str(out)},indent=2))
    return 0 if local_pass else 1
if __name__=="__main__":raise SystemExit(main())
