#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess,sys,tempfile,time
from pathlib import Path
import process_broker as pb

HERE=Path(__file__).resolve().parent
FIX=HERE/"interactive_fixture.py"

def op(engine,opid,cap,action,payload):
    x={"schema":pb.m0.OP_SCHEMA,"operation_id":opid,"capability":cap,"action":action,"authority":{"risk_class":pb.RISK[cap],"scopes":[engine.scope],"approval_ref":None},"fingerprint":"","precondition":{},"replay":"return_receipt","payload":payload}
    x["fingerprint"]=pb.m0.semantic_fingerprint(x);return x

def wait_text(engine,sid,needle,timeout=5):
    end=time.time()+timeout
    last=None
    while time.time()<end:
        last=engine.execute(op(engine,"e-read-"+str(time.time_ns()),"machine.process.read","read",{"session_id":sid}))
        if needle in last["result"]["text"]:return last
        time.sleep(.1)
    raise RuntimeError("missing "+needle)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out",required=True);a=ap.parse_args()
    suite=subprocess.run([sys.executable,"-W","error::ResourceWarning",str(HERE/"test_process_broker.py")],cwd=str(HERE),text=True,capture_output=True,timeout=60)
    result={"schema":"aspace.machine.process-evidence.v1","suite":{"returncode":suite.returncode,"stdout":suite.stdout[-4000:],"stderr":suite.stderr[-8000:]}}
    with tempfile.TemporaryDirectory(prefix="amf-process-evidence-") as td:
        b=Path(td);root=b/"root";root.mkdir();engine=pb.Engine(b/"process.db",root,[sys.executable])
        start=engine.execute(op(engine,"proc-evidence-start","machine.process.start","start",{"argv":[sys.executable,str(FIX)],"cwd":str(root)}))
        sid=start["result"]["session_id"];pid=start["result"]["pid"];ready=wait_text(engine,sid,"READY")
        replay=engine.execute(op(engine,"proc-evidence-start","machine.process.start","start",{"argv":[sys.executable,str(FIX)],"cwd":str(root)}))
        interact=engine.execute(op(engine,"proc-evidence-interact","machine.process.interact","write_stdin",{"session_id":sid,"text":"hello"}))
        echoed=wait_text(engine,sid,"ECHO:hello")
        spawn=engine.execute(op(engine,"proc-evidence-spawn","machine.process.interact","write_stdin",{"session_id":sid,"text":"spawn"}))
        child_log=wait_text(engine,sid,"CHILD:")
        child_pid=int([x for x in child_log["result"]["text"].splitlines() if x.startswith("CHILD:")][-1].split(":")[1])
        child_before=pb.pid_alive(child_pid)
        stop=engine.execute(op(engine,"proc-evidence-stop","machine.process.stop","stop",{"session_id":sid}))
        time.sleep(.25)
        checks={
          "suite_4_of_4":suite.returncode==0,
          "start_receipt_succeeded":start["state"]=="SUCCEEDED",
          "start_replay_same_pid":replay.get("replayed") is True and replay["result"]["pid"]==pid,
          "interactive_echo_observed":"ECHO:hello" in echoed["result"]["text"],
          "interact_receipt_succeeded":interact["state"]=="SUCCEEDED",
          "child_created":child_before,
          "whole_tree_stop_parent_gone":not pb.pid_alive(pid),
          "whole_tree_stop_child_gone":not pb.pid_alive(child_pid),
          "stop_receipt_succeeded":stop["state"]=="SUCCEEDED",
          "health_after_stop_online":engine.health()["aggregate"]=="ONLINE"
        }
        result.update({"result":"PASS" if all(checks.values()) else "FAIL","checks":checks,"start_receipt":start,"replay_receipt":replay,"interact_receipt":interact,"read_receipt":echoed,"stop_receipt":stop,"child_pid":child_pid,"health_after_stop":engine.health(),"policy_version":pb.m0.POLICY_VERSION,"adapter":pb.ADAPTER_ID,"limitations":["stdin interaction is available only while the broker retains the live handle; after broker restart it is truthfully DEGRADED while read/stop remain recoverable by PID/logs.","No shell=True path is exposed; executable and cwd are bounded by policy."],"rollback":"Stop owned process trees and delete the bounded process ledger/root."})
    out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"result":result["result"],"checks":result.get("checks"),"out":str(out)},indent=2))
    return 0 if result["result"]=="PASS" else 1
if __name__=="__main__":raise SystemExit(main())
