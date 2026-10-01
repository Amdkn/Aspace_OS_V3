import json,os,socket,subprocess,sys,tempfile,time,unittest,urllib.request
from pathlib import Path
HERE=Path(__file__).parent
DAEMON=HERE/"session_daemon.py"
WORKER=HERE/"user_session_worker.py"

def free_port():
    s=socket.socket(); s.bind(("127.0.0.1",0)); p=s.getsockname()[1]; s.close(); return p

def get(url):
    with urllib.request.urlopen(url,timeout=2) as r:return json.loads(r.read().decode())
def post(url,p):
    b=json.dumps(p).encode(); q=urllib.request.Request(url,data=b,method="POST",headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(q,timeout=2) as r:return json.loads(r.read().decode())
def wait_health(url,pred,timeout=5):
    end=time.time()+timeout
    while time.time()<end:
        try:
            h=get(url)
            if pred(h):return h
        except Exception:pass
        time.sleep(.1)
    raise AssertionError("health timeout")
class T(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory(); b=Path(self.t.name); self.db=b/"m1.db"; self.log=b/"worker.jsonl"; self.dp=free_port(); self.wp=free_port()
        self.daemon=subprocess.Popen([sys.executable,str(DAEMON),"--db",str(self.db),"--port",str(self.dp)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        self.assertTrue(self.daemon.stdout.readline().strip())
        self.worker=self.start_worker("session-A")
    def start_worker(self,sid):
        p=subprocess.Popen([sys.executable,str(WORKER),"--daemon",f"http://127.0.0.1:{self.dp}","--port",str(self.wp),"--session-id",sid,"--log",str(self.log)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        line=p.stdout.readline().strip(); self.assertTrue(line); self.worker_info=json.loads(line); return p
    def tearDown(self):
        for p in [getattr(self,"worker",None),getattr(self,"daemon",None)]:
            if p and p.poll() is None:
                p.terminate()
                try:p.wait(2)
                except subprocess.TimeoutExpired:p.kill();p.wait(2)
            if p:
                if p.stdout:p.stdout.close()
                if p.stderr:p.stderr.close()
        self.t.cleanup()
    def test_health_degrades_when_worker_dies_and_fence_increments(self):
        h=wait_health(f"http://127.0.0.1:{self.dp}/health",lambda x:x["worker"]=="UP"); f1=h["fencing_token"]
        old_worker=self.worker
        old_worker.terminate(); old_worker.wait(2)
        if old_worker.stdout: old_worker.stdout.close()
        if old_worker.stderr: old_worker.stderr.close()
        h2=wait_health(f"http://127.0.0.1:{self.dp}/health",lambda x:x["worker"]=="DOWN",timeout=5)
        self.assertEqual(h2["aggregate"],"DEGRADED")
        self.worker=self.start_worker("session-A-reconnect")
        h3=wait_health(f"http://127.0.0.1:{self.dp}/health",lambda x:x["worker"]=="UP")
        self.assertGreater(h3["fencing_token"],f1)
    def test_same_operation_reconnect_returns_receipt_without_reexecute(self):
        base=f"http://127.0.0.1:{self.wp}/native"
        claim={"type":"claim","operation_id":"browser-op-0001","fingerprint":"fingerprint-0000001","action":"browser.dom.action"}
        first=post(base,claim); self.assertTrue(first["execute"])
        receipt=post(base,{"type":"complete","operation_id":"browser-op-0001","fingerprint":"fingerprint-0000001","evidence":{"before":"BEFORE","after":"AFTER","selector":"#target"}})
        self.assertEqual(receipt["state"],"SUCCEEDED")
        second=post(base,claim); self.assertFalse(second["execute"]); self.assertTrue(second["replayed"]); self.assertEqual(second["receipt"]["effect_digest"],receipt["effect_digest"])
    def test_duplicate_claim_before_completion_never_double_claims(self):
        base=f"http://127.0.0.1:{self.wp}/native"
        claim={"type":"claim","operation_id":"browser-op-running","fingerprint":"fingerprint-running","action":"browser.dom.action"}
        a=post(base,claim); b=post(base,claim)
        self.assertTrue(a["execute"]); self.assertFalse(b["execute"]); self.assertEqual(b["state"],"RUNNING")
    def test_concurrent_hello_task_claim_tabs_ordering(self):
        import concurrent.futures
        # Simulate concurrent requests from extension
        base=f"http://127.0.0.1:{self.wp}/native"
        
        # 1. Queue a pending task
        daemon_exec=f"http://127.0.0.1:{self.dp}/execute"
        task_req = {"operation_id":"op-concurrent","fingerprint":"fp-concurrent","action":"browser.dom.action"}
        def execute_task():
            # This will block until completed or timeout, we don't care about the result here
            try: post(daemon_exec, task_req)
            except Exception: pass
        
        import threading
        t = threading.Thread(target=execute_task, daemon=True)
        t.start()
        
        time.sleep(0.5) # Wait for task to be pending
        
        # 2. Issue concurrent hello and tabs, simulating extension pingLoop overlapping
        hello_req = {"type":"hello", "request_id": "req-hello"}
        tabs_req = {"type":"tabs", "request_id": "req-tabs"}
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            fut_hello = executor.submit(post, base, hello_req)
            fut_tabs = executor.submit(post, base, tabs_req)
            hello_resp = fut_hello.result()
            tabs_resp = fut_tabs.result()
            
        self.assertEqual(hello_resp.get("request_id"), "req-hello")
        self.assertEqual(tabs_resp.get("request_id"), "req-tabs")
        
        self.assertTrue("tasks" in hello_resp and len(hello_resp["tasks"]) > 0)
        
        # 3. Extension receives tasks and processes them sequentially with await
        # Claim
        claim_req = {"type":"claim", "operation_id":"op-concurrent", "fingerprint":"fp-concurrent", "action":"browser.dom.action", "request_id": "req-claim"}
        claim_resp = post(base, claim_req)
        self.assertEqual(claim_resp.get("request_id"), "req-claim")
        self.assertTrue(claim_resp["execute"])
        
        # Second claim should fail execute (simulate duplicate claim)
        claim_req2 = {"type":"claim", "operation_id":"op-concurrent", "fingerprint":"fp-concurrent", "action":"browser.dom.action", "request_id": "req-claim2"}
        claim_resp2 = post(base, claim_req2)
        self.assertEqual(claim_resp2.get("request_id"), "req-claim2")
        self.assertFalse(claim_resp2["execute"])
        self.assertEqual(claim_resp2["state"], "RUNNING")
        
        # Complete
        comp_req = {"type":"complete", "operation_id":"op-concurrent", "fingerprint":"fp-concurrent", "evidence":{}, "request_id": "req-comp"}
        comp_resp = post(base, comp_req)
        self.assertEqual(comp_resp.get("request_id"), "req-comp")
        self.assertEqual(comp_resp["state"], "SUCCEEDED")
if __name__=="__main__":unittest.main(verbosity=2)
