#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,threading,time,urllib.request,uuid
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from urllib.parse import urlparse

def post(url,payload):
    b=json.dumps(payload).encode(); req=urllib.request.Request(url,data=b,method="POST",headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=3) as r: return r.status,json.loads(r.read().decode())
class State:
    def __init__(self,daemon,session_id,log):
        self.daemon=daemon.rstrip("/"); self.session_id=session_id; self.log=log; self.worker_id="worker-"+uuid.uuid4().hex[:12]; self.stop=False
        _,r=post(self.daemon+"/worker/register",{"worker_id":self.worker_id,"session_id":session_id,"capabilities":["browser.tabs.read","browser.dom.read","browser.dom.action"]})
        self.fence=r["fencing_token"]; self.lease_id=r["lease_id"]
        threading.Thread(target=self.heartbeat,daemon=True).start()
    def write(self,obj):
        with open(self.log,"a",encoding="utf-8") as f: f.write(json.dumps(obj,ensure_ascii=False)+"\n")
    def heartbeat(self):
        while not self.stop:
            try: post(self.daemon+"/worker/heartbeat",{"worker_id":self.worker_id,"fencing_token":self.fence})
            except Exception: pass
            time.sleep(.8)
    def native(self,msg):
        self.write({"dir":"in","msg":msg,"worker_id":self.worker_id,"fence":self.fence})
        typ=msg.get("type")
        if typ=="hello": out={"ok":True,"worker_id":self.worker_id,"fencing_token":self.fence,"capabilities":["browser.tabs.read","browser.dom.action"]}
        elif typ=="tabs": out={"ok":True,"tab_count":len(msg.get("tabs") or [])}
        elif typ=="claim":
            payload=dict(msg); payload.update({"worker_id":self.worker_id,"fencing_token":self.fence}); _,out=post(self.daemon+"/browser/claim",payload)
        elif typ=="complete":
            payload=dict(msg); payload.update({"worker_id":self.worker_id,"fencing_token":self.fence}); _,out=post(self.daemon+"/browser/complete",payload)
        else: out={"ok":False,"error":"UNKNOWN_MESSAGE"}
        self.write({"dir":"out","msg":out,"worker_id":self.worker_id,"fence":self.fence}); return out

class App(ThreadingHTTPServer):
    daemon_threads=True
    def __init__(self,addr,state): super().__init__(addr,H); self.state=state
class H(BaseHTTPRequestHandler):
    server:App
    def log_message(self,*a): pass
    def sendj(self,p):
        b=json.dumps(p,separators=(",",":")).encode(); self.send_response(200); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_POST(self):
        if urlparse(self.path).path!="/native": self.send_error(404); return
        n=int(self.headers.get("Content-Length","0")); msg=json.loads(self.rfile.read(n).decode()); self.sendj(self.server.state.native(msg))
def main():
    p=argparse.ArgumentParser(); p.add_argument("--daemon",required=True); p.add_argument("--port",type=int,required=True); p.add_argument("--session-id",default="interactive"); p.add_argument("--log",required=True); a=p.parse_args()
    s=State(a.daemon,a.session_id,a.log); print(json.dumps({"worker_id":s.worker_id,"fencing_token":s.fence,"port":a.port}),flush=True)
    try: App(("127.0.0.1",a.port),s).serve_forever()
    finally:s.stop=True
if __name__=="__main__": main()
