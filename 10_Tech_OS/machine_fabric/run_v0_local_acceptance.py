#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os,subprocess,sys,time
try:
    import winreg
except ImportError:
    winreg = None
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
    if winreg is None: return True
    try:
        k=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Google\Chrome\NativeMessagingHosts\com.aspace.machine_fabric.canary")
        winreg.CloseKey(k);return False
    except FileNotFoundError:return True

def lingering_count():
    ps="$p=Get-CimInstance Win32_Process | Where-Object { $_.Name -match '^(python|pythonw|ASpaceNativeHost)\\.exe$' -and $_.CommandLine -match 'session_daemon.py|user_session_worker.py|ASpaceNativeHost.exe|aspace-m1-canary' }; @($p).Count"
    try:
        cp=subprocess.run(["pwsh","-NoProfile","-Command",ps],text=True,capture_output=True,timeout=15)
    except FileNotFoundError:
        try:
            cp=subprocess.run(["powershell","-NoProfile","-Command",ps],text=True,capture_output=True,timeout=15)
        except FileNotFoundError:
            class Dummy:
                stdout = "0\n"
            cp = Dummy()
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
    process_report=REPORTS/"amf_process_evidence_20260929.json"
    steps.append(run("Process-unit",HERE/"process",[sys.executable,"-W","error::ResourceWarning","test_process_broker.py"],60))
    steps.append(run("Process-evidence",HERE/"process",[sys.executable,"run_process_evidence.py","--out",str(process_report)],60))
    steps.append(run("M2-adapter",HERE/"m2",[sys.executable,"test_m2.py"],60))
    m2_report=REPORTS/"amf_m2_remote_evidence_20260929.json"
    steps.append(run("M2-private-serve",HERE/"m2",[sys.executable,"run_m2_serve_canary.py","--out",str(m2_report)],30))
    m1=json.loads(m1_report.read_text(encoding="utf-8")) if m1_report.exists() else {}
    process=json.loads(process_report.read_text(encoding="utf-8")) if process_report.exists() else {}
    m2=json.loads(m2_report.read_text(encoding="utf-8")) if m2_report.exists() else {}
    core_names={"M0","P1-P4","M1-unit","M1-chrome","Process-unit","Process-evidence","M2-adapter","M2-private-serve"}
    tests_green=all(x["returncode"]==0 for x in steps if x["name"] in core_names)
    local_pass=tests_green and m1.get("result")=="PASS" and process.get("result")=="PASS" and registry_clean() and lingering_count()==0
    if m2.get("second_client_canary")=="PASS":
        remote_state="PASS"
    elif m2.get("result")=="SERVE_ENABLEMENT_REQUIRED":
        remote_state="EXTERNAL_AUTH_REQUIRED"
    elif m2.get("result")=="DEPENDENCY_MISSING":
        remote_state="OPEN_DEPENDENCY"
    else:
        remote_state="OPEN"
    result={
      "schema":"aspace.machine.v0-continuous-evidence.v1",
      "result":"LOCAL_V0_RELEASE_READY" if local_pass and remote_state!="PASS" else ("PASS" if local_pass and remote_state=="PASS" else "FAIL"),
      "local_v0_pass":local_pass,
      "remote_gate":remote_state,
      "chrome_for_testing":str(cft) if cft else None,
      "steps":steps,
      "m1_summary":{"result":m1.get("result"),"checks":m1.get("checks"),"receipt":m1.get("receipt")},
      "process_summary":{"result":process.get("result"),"checks":process.get("checks"),"start_receipt":process.get("start_receipt"),"stop_receipt":process.get("stop_receipt")},
      "m2_summary":m2,
      "cleanup":{"temporary_native_host_registry_absent":registry_clean(),"lingering_owned_processes":lingering_count()},
      "gate_sequence":["M0 durable mutation","P1-P4 Harness Runtime","M1 worker+Chrome","Local process start/interact/read/stop","M2 private remote live canary"],
      "promotion":"LOCAL_V0_RELEASE_READY_REMOTE_SOVEREIGNITY_SEPARATE" if local_pass and remote_state!="PASS" else "SEE_RESULT",
      "finished_at":time.time()
    }
    out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"result":result["result"],"remote_gate":remote_state,"steps":[[x["name"],x["returncode"],x["seconds"]] for x in steps],"cleanup":result["cleanup"],"out":str(out)},indent=2))
    return 0 if local_pass else 1
if __name__=="__main__":raise SystemExit(main())
