#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

HERE=Path(__file__).resolve().parent
M0=HERE.parent/"m0"
sys.path.insert(0,str(M0))
import amf_m0 as m0  # reuses canonical operation fingerprint + receipt law

try:
    import psutil
except Exception:
    psutil=None

ADAPTER_ID="amf.process.broker.v1"
CAPS={
    "machine.process.start":"start",
    "machine.process.interact":"write_stdin",
    "machine.process.read":"read",
    "machine.process.stop":"stop",
}
RISK={
    "machine.process.start":"consequential",
    "machine.process.interact":"consequential",
    "machine.process.read":"read",
    "machine.process.stop":"consequential",
}

class ProcessError(RuntimeError):
    status=400
    code="PROCESS_ERROR"
class Conflict(ProcessError):
    status=409
    code="OPERATION_ID_FINGERPRINT_CONFLICT"
class Denied(ProcessError):
    status=403
    code="DENIED"
class NotFound(ProcessError):
    status=404
    code="NOT_FOUND"

def canon(v): return m0.canonical_json(v)
def iso(): return m0.now_iso()
def digest(v): return "sha256:"+m0.sha256_bytes(canon(v).encode())

def pid_alive(pid:int)->bool:
    if psutil is not None:
        try:return psutil.pid_exists(pid) and psutil.Process(pid).is_running()
        except Exception:return False
    try:
        os.kill(pid,0); return True
    except Exception:return False

def kill_tree(pid:int):
    if os.name=="nt":
        subprocess.run(["taskkill","/PID",str(pid),"/T","/F"],capture_output=True,text=True,timeout=15)
    elif psutil is not None:
        try:
            p=psutil.Process(pid)
            for c in p.children(recursive=True):
                try:c.kill()
                except Exception:pass
            p.kill()
        except Exception:pass
    else:
        try:
            if os.name!="nt": os.killpg(os.getpgid(pid),9)
        except Exception:pass

class Engine:
    def __init__(self,db,allowed_root,allowed_exes):
        self.db=Path(db).resolve(); self.db.parent.mkdir(parents=True,exist_ok=True)
        self.allowed_root=Path(allowed_root).resolve(); self.allowed_root.mkdir(parents=True,exist_ok=True)
        self.allowed_exes={str(Path(x).resolve()).lower() for x in allowed_exes}
        self.scope="process:root:"+str(self.allowed_root)
        self.handles={}
        self.lock=threading.RLock()
        self._init()
        self._reconcile_sessions()

    def con(self):
        c=sqlite3.connect(self.db,timeout=10); c.row_factory=sqlite3.Row
        c.execute("pragma journal_mode=WAL"); c.execute("pragma synchronous=FULL"); c.execute("pragma busy_timeout=5000")
        return c
    def _init(self):
        c=self.con()
        try:
            c.executescript("""
            create table if not exists operation(
              operation_id text primary key, fingerprint text not null, capability text not null,
              action text not null, state text not null, request_json text not null,
              receipt_json text, claimed_at text not null, finished_at text);
            create table if not exists process_session(
              session_id text primary key, start_operation_id text not null, executable text not null,
              argv_json text not null, cwd text not null, pid integer not null, state text not null,
              stdout_ref text not null, stderr_ref text not null, started_at text not null, finished_at text);
            """); c.commit()
        finally:c.close()
    def _reconcile_sessions(self):
        c=self.con()
        try:
            rows=c.execute("select session_id,pid,state from process_session where state='RUNNING'").fetchall()
            for r in rows:
                if not pid_alive(int(r["pid"])):
                    c.execute("update process_session set state='EXITED',finished_at=? where session_id=?",(iso(),r["session_id"]))
            c.commit()
        finally:c.close()
    def _validate(self,op):
        required={"schema","operation_id","capability","action","authority","fingerprint","precondition","replay"}
        if required-set(op): raise ProcessError("missing operation fields")
        if op["schema"]!=m0.OP_SCHEMA: raise ProcessError("invalid operation schema")
        if op["capability"] not in CAPS or CAPS[op["capability"]]!=op["action"]: raise ProcessError("capability/action mismatch")
        if op["fingerprint"]!=m0.semantic_fingerprint(op): raise ProcessError("fingerprint mismatch")
        auth=op["authority"]
        if auth.get("risk_class")!=RISK[op["capability"]]: raise Denied("risk class mismatch")
        if self.scope not in (auth.get("scopes") or []): raise Denied("process root scope missing")
        if op["replay"]!="return_receipt": raise ProcessError("process v0 only supports return_receipt")
        if not isinstance(op.get("payload",{}),dict): raise ProcessError("payload must be object")
    def _claim(self,op):
        c=self.con()
        try:
            r=c.execute("select * from operation where operation_id=?",(op["operation_id"],)).fetchone()
            if r:
                if r["fingerprint"]!=op["fingerprint"]: raise Conflict(op["operation_id"])
                if r["receipt_json"]:
                    rec=json.loads(r["receipt_json"]); rec["replayed"]=True; return rec
                return {"schema":m0.RECEIPT_SCHEMA,"operation_id":op["operation_id"],"fingerprint":op["fingerprint"],"state":r["state"],"capability":op["capability"],"adapter":ADAPTER_ID,"policy":{"decision":"ALLOW","policy_version":m0.POLICY_VERSION},"effect_digest":None,"evidence":["operation already claimed"],"replayed":True}
            c.execute("insert into operation(operation_id,fingerprint,capability,action,state,request_json,claimed_at) values(?,?,?,?,?,?,?)",(op["operation_id"],op["fingerprint"],op["capability"],op["action"],"CLAIMED",canon(op),iso())); c.commit(); return None
        finally:c.close()
    def _persist(self,op,receipt):
        c=self.con()
        try:
            c.execute("update operation set state=?,receipt_json=?,finished_at=? where operation_id=?",(receipt["state"],canon(receipt),receipt.get("finished_at") or iso(),op["operation_id"])); c.commit()
        finally:c.close()
        return receipt
    def _receipt(self,op,state,evidence,result=None,effect=None):
        r={"schema":m0.RECEIPT_SCHEMA,"operation_id":op["operation_id"],"fingerprint":op["fingerprint"],"state":state,"capability":op["capability"],"adapter":ADAPTER_ID,"policy":{"decision":"ALLOW","policy_version":m0.POLICY_VERSION},"effect_digest":effect,"evidence":evidence,"finished_at":iso()}
        if result is not None:r["result"]=result
        return r
    def _session(self,sid):
        c=self.con()
        try:r=c.execute("select * from process_session where session_id=?",(sid,)).fetchone()
        finally:c.close()
        if not r:raise NotFound("unknown session")
        return dict(r)
    def execute(self,op):
        self._validate(op)
        with self.lock:
            prior=self._claim(op)
            if prior:return prior
            try:
                cap=op["capability"]
                if cap=="machine.process.start":rec=self._start(op)
                elif cap=="machine.process.interact":rec=self._interact(op)
                elif cap=="machine.process.read":rec=self._read(op)
                elif cap=="machine.process.stop":rec=self._stop(op)
                else:raise ProcessError("unsupported capability")
            except ProcessError as e:
                rec=self._receipt(op,"DENIED" if isinstance(e,Denied) else "FAILED",[str(e)])
            except Exception as e:
                rec=self._receipt(op,"FAILED",[type(e).__name__+": "+str(e)])
            return self._persist(op,rec)
    def _start(self,op):
        p=op["payload"]; argv=p.get("argv")
        if not isinstance(argv,list) or not argv:raise ProcessError("argv list required")
        exe=str(Path(argv[0]).resolve()).lower()
        if exe not in self.allowed_exes:raise Denied("executable not allowlisted")
        cwd=Path(p.get("cwd") or self.allowed_root).resolve()
        try:cwd.relative_to(self.allowed_root)
        except ValueError:raise Denied("cwd outside allowed root")
        if "shell" in p:raise Denied("shell field forbidden")
        sid="proc-"+op["fingerprint"][:18]
        outdir=self.allowed_root/".amf-process"/sid; outdir.mkdir(parents=True,exist_ok=True)
        stdout=outdir/"stdout.log"; stderr=outdir/"stderr.log"
        of=stdout.open("ab",buffering=0); ef=stderr.open("ab",buffering=0)
        try:
            kw={"cwd":str(cwd),"stdin":subprocess.PIPE,"stdout":of,"stderr":ef,"shell":False,"env":os.environ.copy()}
            if os.name=="nt":kw["creationflags"]=getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 512)
            else:kw["start_new_session"]=True
            proc=subprocess.Popen([str(x) for x in argv],**kw)
        finally:of.close();ef.close()
        self.handles[sid]=proc
        c=self.con()
        try:
            c.execute("insert into process_session values(?,?,?,?,?,?,?,?,?,?,?)",(sid,op["operation_id"],str(Path(argv[0]).resolve()),canon(argv),str(cwd),proc.pid,"RUNNING",str(stdout),str(stderr),iso(),None));c.commit()
        finally:c.close()
        evidence={"session_id":sid,"pid":proc.pid,"argv":argv,"cwd":str(cwd)}
        return self._receipt(op,"SUCCEEDED",[canon(evidence)],{"session_id":sid,"pid":proc.pid,"stdout_ref":str(stdout),"stderr_ref":str(stderr)},digest(evidence))
    def _interact(self,op):
        p=op["payload"]; sid=p.get("session_id"); text=p.get("text")
        if not isinstance(sid,str) or not isinstance(text,str):raise ProcessError("session_id/text required")
        row=self._session(sid)
        if row["state"]!="RUNNING" or not pid_alive(int(row["pid"])):raise ProcessError("process not running")
        proc=self.handles.get(sid)
        if not proc or not proc.stdin:
            raise ProcessError("INTERACTION_UNAVAILABLE_AFTER_RESTART")
        data=(text+("\n" if p.get("newline",True) else "")).encode()
        proc.stdin.write(data);proc.stdin.flush()
        ev={"session_id":sid,"stdin_bytes_written":len(data)}
        return self._receipt(op,"SUCCEEDED",[canon(ev)],ev,digest(ev))
    def _read(self,op):
        p=op["payload"]; sid=p.get("session_id"); stream=p.get("stream","stdout"); tail=int(p.get("tail_bytes",65536))
        if stream not in {"stdout","stderr"}:raise ProcessError("invalid stream")
        row=self._session(sid); ref=Path(row[stream+"_ref"]); data=ref.read_bytes()[-max(1,min(tail,1_000_000)):] if ref.exists() else b""
        alive=pid_alive(int(row["pid"]))
        result={"session_id":sid,"stream":stream,"text":data.decode("utf-8",errors="replace"),"running":alive,"pid":int(row["pid"])}
        return self._receipt(op,"SUCCEEDED",[str(ref)],result,digest(result))
    def _stop(self,op):
        sid=op["payload"].get("session_id"); row=self._session(sid); pid=int(row["pid"])
        proc=self.handles.get(sid)
        if proc and proc.stdin:
            try:proc.stdin.close()
            except Exception:pass
        if pid_alive(pid):kill_tree(pid)

        end=time.time()+5
        while pid_alive(pid) and time.time()<end:time.sleep(.1)
        if pid_alive(pid):
            try:
                import signal
                os.kill(pid, signal.SIGKILL)
                time.sleep(0.5)
            except Exception:
                pass
        if pid_alive(pid):raise ProcessError("process tree still alive")

        if proc:
            try:proc.wait(timeout=2)
            except Exception:pass
        c=self.con()
        try:c.execute("update process_session set state='STOPPED',finished_at=? where session_id=?",(iso(),sid));c.commit()
        finally:c.close()
        self.handles.pop(sid,None)
        ev={"session_id":sid,"pid":pid,"tree_alive":False}
        return self._receipt(op,"SUCCEEDED",[canon(ev)],ev,digest(ev))
    def health(self):
        c=self.con()
        try:rows=c.execute("select session_id,pid,state from process_session where state='RUNNING'").fetchall()
        finally:c.close()
        detached=[r["session_id"] for r in rows if pid_alive(int(r["pid"])) and r["session_id"] not in self.handles]
        
        presence = {
            "active": True,
            "orphaned_sessions": len(detached),
            "tracking": len(self.handles)
        }
        
        degraded_reason = "ORPHANED_SESSIONS_DETECTED" if detached else None

        return {"schema":m0.HEALTH_SCHEMA,"daemon":"UP","worker":"NOT_REQUIRED","transport":"LOCAL","capabilities":{"machine.process.start":"AVAILABLE","machine.process.read":"AVAILABLE","machine.process.stop":"AVAILABLE","machine.process.interact":"DEGRADED" if detached else "AVAILABLE"},"aggregate":"DEGRADED" if detached else "ONLINE","detached_sessions":detached, "presence": presence, "degraded_reason": degraded_reason}

class Server(ThreadingHTTPServer):
    daemon_threads=True
    def __init__(self,addr,engine):
        if addr[0]!="127.0.0.1":raise ValueError("loopback only")
        super().__init__(addr,Handler);self.engine=engine
class Handler(BaseHTTPRequestHandler):
    server:Server
    def log_message(self,*a):pass
    def sendj(self,status,p):
        b=canon(p).encode();self.send_response(status);self.send_header("Content-Type","application/json");self.send_header("Content-Length",str(len(b)));self.end_headers();self.wfile.write(b)
    def body(self):
        n=int(self.headers.get("Content-Length","0"));return json.loads(self.rfile.read(n).decode()) if n else {}
    def do_GET(self):
        p=urlparse(self.path).path
        if p=="/health":self.sendj(200,self.server.engine.health());return
        self.sendj(404,{"error":"NOT_FOUND"})
    def do_POST(self):
        if urlparse(self.path).path!="/operations":self.sendj(404,{"error":"NOT_FOUND"});return
        try:self.sendj(200,self.server.engine.execute(self.body()))
        except ProcessError as e:self.sendj(e.status,{"error":e.code,"detail":str(e)})
        except Exception as e:self.sendj(500,{"error":"INTERNAL","detail":str(e)})

def main():
    p=argparse.ArgumentParser();p.add_argument("--db",required=True);p.add_argument("--allowed-root",required=True);p.add_argument("--allow-exe",action="append",required=True);p.add_argument("--port",type=int,required=True);a=p.parse_args()
    e=Engine(a.db,a.allowed_root,a.allow_exe);s=Server(("127.0.0.1",a.port),e);port = s.server_address[1]
    print(canon({"state":"UP","port":port,"health":e.health()}),flush=True);s.serve_forever()
if __name__=="__main__":main()
