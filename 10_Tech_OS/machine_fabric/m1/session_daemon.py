#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sqlite3, threading, time, uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

SCHEMA_HEALTH="aspace.machine.health.v1"
SCHEMA_RECEIPT="aspace.machine.receipt.v1"
POLICY_VERSION="amf-policy-v1"
LEASE_TTL=2.0

def now(): return time.time()
def iso():
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).isoformat()
def canon(v): return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sha(v): return hashlib.sha256(v.encode()).hexdigest()

class Store:
    def __init__(self,path):
        self.path=Path(path).resolve(); self.path.parent.mkdir(parents=True,exist_ok=True); self.lock=threading.RLock(); self._init()
    def con(self):
        c=sqlite3.connect(self.path,timeout=10); c.row_factory=sqlite3.Row
        c.execute("pragma journal_mode=WAL"); c.execute("pragma synchronous=FULL"); c.execute("pragma busy_timeout=5000"); return c
    def _init(self):
        c=self.con()
        try:
            c.executescript("""
            create table if not exists meta(key text primary key,value text not null);
            create table if not exists worker(
              worker_id text primary key, session_id text not null, fence integer not null,
              lease_id text not null, lease_expires real not null, capabilities text not null,
              registered_at text not null, heartbeat_at text not null);
            create table if not exists browser_operation(
              operation_id text primary key, fingerprint text not null, state text not null,
              fence integer not null, action text not null, request_json text not null,
              receipt_json text, claimed_at text not null, finished_at text);
            """); c.commit()
        finally:c.close()
    def next_fence(self):
        with self.lock:
            c=self.con()
            try:
                r=c.execute("select value from meta where key='fence'").fetchone()
                n=int(r["value"]) + 1 if r else 1
                c.execute("insert into meta(key,value) values('fence',?) on conflict(key) do update set value=excluded.value",(str(n),)); c.commit(); return n
            finally:c.close()
    def register(self,worker_id,session_id,capabilities):
        fence=self.next_fence(); lease_id="lease-"+uuid.uuid4().hex[:16]; t=now(); ts=iso()
        c=self.con()
        try:
            c.execute("insert or replace into worker values(?,?,?,?,?,?,?,?)",(worker_id,session_id,fence,lease_id,t+LEASE_TTL,canon(capabilities),ts,ts)); c.commit()
        finally:c.close()
        return {"worker_id":worker_id,"session_id":session_id,"fencing_token":fence,"lease_id":lease_id,"lease_ttl_seconds":LEASE_TTL}
    def heartbeat(self,worker_id,fence):
        c=self.con()
        try:
            r=c.execute("select fence from worker where worker_id=?",(worker_id,)).fetchone()
            if not r or int(r["fence"])!=int(fence): return False
            c.execute("update worker set lease_expires=?,heartbeat_at=? where worker_id=?",(now()+LEASE_TTL,iso(),worker_id)); c.commit(); return True
        finally:c.close()
    def current_worker(self):
        c=self.con()
        try:
            r=c.execute("select * from worker where lease_expires>? order by fence desc limit 1",(now(),)).fetchone()
            return dict(r) if r else None
        finally:c.close()
    def latest_worker(self):
        c=self.con()
        try:
            r=c.execute("select * from worker order by fence desc limit 1").fetchone()
            return dict(r) if r else None
        finally:c.close()
    def execute_op(self,msg):
        op=msg["operation_id"]; fp=msg["fingerprint"]; action=msg.get("action","browser.dom.action")
        current=self.current_worker()
        if not current: return 503,{"error":"NO_WORKER","state":"UNAVAILABLE"}
        fence=int(current["fence"])
        c=self.con()
        try:
            r=c.execute("select * from browser_operation where operation_id=?",(op,)).fetchone()
            if r:
                if r["fingerprint"]!=fp: return 409,{"error":"OPERATION_ID_FINGERPRINT_CONFLICT"}
                if r["receipt_json"]: return 200,json.loads(r["receipt_json"])
            else:
                c.execute("insert into browser_operation(operation_id,fingerprint,state,fence,action,request_json,claimed_at) values(?,?,?,?,?,?,?)",(op,fp,"PENDING",fence,action,canon(msg),iso())); c.commit()
        finally:c.close()

        start = time.time()
        while time.time() - start < 9.0:
            c=self.con()
            try:
                r=c.execute("select receipt_json, state from browser_operation where operation_id=?",(op,)).fetchone()
                if r and r["receipt_json"]:
                    return 200,json.loads(r["receipt_json"])
            finally:c.close()
            time.sleep(0.1)

        return 504,{"error":"TIMEOUT","state":"PENDING"}

    def pending(self):
        c=self.con()
        try:
            rows=c.execute("select request_json from browser_operation where state='PENDING'").fetchall()
            return 200,{"tasks":[json.loads(r["request_json"]) for r in rows]}
        finally:c.close()

    def claim(self,msg):
        op=msg["operation_id"]; fp=msg["fingerprint"]; wid=msg["worker_id"]; fence=int(msg["fencing_token"])
        current=self.current_worker()
        if not current or current["worker_id"]!=wid or int(current["fence"])!=fence:
            return 409,{"error":"STALE_WORKER","execute":False}
        c=self.con()
        try:
            r=c.execute("select * from browser_operation where operation_id=?",(op,)).fetchone()
            if r:
                if r["fingerprint"]!=fp: return 409,{"error":"OPERATION_ID_FINGERPRINT_CONFLICT","execute":False}
                if r["receipt_json"]:
                    return 200,{"execute":False,"replayed":True,"receipt":json.loads(r["receipt_json"])}
                if r["state"] == "PENDING":
                    c.execute("update browser_operation set state='RUNNING', claimed_at=? where operation_id=?", (iso(), op)); c.commit()
                    return 200,{"execute":True,"replayed":False,"state":"RUNNING","fencing_token":fence}
                return 200,{"execute":False,"replayed":True,"state":r["state"],"fencing_token":int(r["fence"])}
            c.execute("insert into browser_operation(operation_id,fingerprint,state,fence,action,request_json,claimed_at) values(?,?,?,?,?,?,?)",(op,fp,"RUNNING",fence,msg.get("action","browser.dom.action"),canon(msg),iso())); c.commit()
            return 200,{"execute":True,"replayed":False,"state":"RUNNING","fencing_token":fence}
        finally:c.close()
    def complete(self,msg):
        op=msg["operation_id"]; fence=int(msg["fencing_token"]); current=self.current_worker()
        if not current or int(current["fence"])!=fence: return 409,{"error":"STALE_WORKER"}
        c=self.con()
        try:
            r=c.execute("select * from browser_operation where operation_id=?",(op,)).fetchone()
            if not r: return 404,{"error":"UNKNOWN_OPERATION"}
            if int(r["fence"])!=fence: return 409,{"error":"FENCE_MISMATCH"}
            if r["receipt_json"]: return 200,json.loads(r["receipt_json"])
            evidence=msg.get("evidence") or {}
            effect_digest="sha256:"+sha(canon(evidence))
            receipt={
              "schema":SCHEMA_RECEIPT,"operation_id":op,"fingerprint":r["fingerprint"],"state":"SUCCEEDED",
              "capability":"browser.dom.action","adapter":"amf.m1.chrome-native-messaging",
              "policy":{"decision":"ALLOW","policy_version":POLICY_VERSION},
              "effect_digest":effect_digest,
              "evidence":[canon(evidence),"worker="+current["worker_id"],"lease="+current["lease_id"]],
              "finished_at":iso()
            }
            c.execute("update browser_operation set state='SUCCEEDED',receipt_json=?,finished_at=? where operation_id=?",(canon(receipt),receipt["finished_at"],op)); c.commit()
            return 200,receipt
        finally:c.close()

class App(ThreadingHTTPServer):
    daemon_threads=True
    def __init__(self,addr,store):
        if addr[0]!="127.0.0.1": raise ValueError("loopback only")
        super().__init__(addr,Handler); self.store=store

class Handler(BaseHTTPRequestHandler):
    server:App
    def log_message(self,*a): pass
    def sendj(self,status,p):
        try:
            b=canon(p).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type","application/json")
            self.send_header("Content-Length",str(len(b)))
            self.send_header("Connection", "close")
            self.end_headers()
            self.wfile.write(b)
            self.wfile.flush()
            self.close_connection = True
        except Exception as e:
            import sys
            print("SENDJ EXCEPTION:", e, file=sys.stderr)
    def body(self):
        n=int(self.headers.get("Content-Length","0")); return json.loads(self.rfile.read(n).decode()) if n else {}
    def do_GET(self):
        try:
            p=urlparse(self.path).path
            if p=="/browser/pending": s,o=self.server.store.pending(); self.sendj(s,o); return
            if p=="/health":
                w=self.server.store.current_worker()
                latest=self.server.store.latest_worker()
                
                presence = {
                    "active": bool(w),
                    "ttl_expired": bool(latest and not w),
                    "last_seen": latest["heartbeat_at"] if latest else None,
                    "session_id": latest["session_id"] if latest else None,
                    "fencing_token": int(latest["fence"]) if latest else None,
                    "worker_id": latest["worker_id"] if latest else None
                }
                
                degraded_reason = None
                if presence["ttl_expired"]: degraded_reason = "WORKER_TTL_EXPIRED_STALE"
                elif not latest: degraded_reason = "NO_WORKER_EVER_REGISTERED"

                resp = {"schema":SCHEMA_HEALTH,"daemon":"UP","worker":"UP" if w else "DOWN","transport":"LOCAL","capabilities":{"browser.tabs.read":"AVAILABLE" if w else "UNAVAILABLE","browser.dom.action":"AVAILABLE" if w else "UNAVAILABLE","browser.debugger.attach":"UNAVAILABLE"},"aggregate":"ONLINE" if w else "DEGRADED","worker_ref":w["worker_id"] if w else None,"fencing_token":int(w["fence"]) if w else None, "presence": presence, "degraded_reason": degraded_reason}
                self.sendj(200, resp)
                return
            self.sendj(404,{"error":"NOT_FOUND"})
        except Exception as e:
            import sys, traceback
            traceback.print_exc(file=sys.stderr)
            self.sendj(500, {"error": "INTERNAL_ERROR", "detail": str(e)})
    def do_POST(self):
        try:
            p=urlparse(self.path).path
            b=self.body()
            if p=="/execute": s,o=self.server.store.execute_op(b); self.sendj(s,o); return
            if p=="/worker/register": self.sendj(200,self.server.store.register(b["worker_id"],b["session_id"],b.get("capabilities") or [])); return
            if p=="/worker/heartbeat": self.sendj(200,{"ok":self.server.store.heartbeat(b["worker_id"],b["fencing_token"])}); return
            if p=="/browser/claim": s,o=self.server.store.claim(b); self.sendj(s,o); return
            if p=="/browser/complete": s,o=self.server.store.complete(b); self.sendj(s,o); return
            self.sendj(404,{"error":"NOT_FOUND"})
        except (ValueError, KeyError, TypeError) as e:
            self.sendj(400, {"error": "BAD_REQUEST", "detail": str(e)})
        except Exception as e:
            import sys, traceback
            traceback.print_exc(file=sys.stderr)
            self.sendj(500, {"error": "INTERNAL_ERROR", "detail": str(e)})

def main():
    p=argparse.ArgumentParser(); p.add_argument("--db",required=True); p.add_argument("--port",type=int,required=True); a=p.parse_args()
    app=App(("127.0.0.1",a.port),Store(a.db)); port = app.server_address[1]
    print(canon({"state":"UP","port":port,"db":str(Path(a.db).resolve())}),flush=True); app.serve_forever()
if __name__=="__main__": main()
