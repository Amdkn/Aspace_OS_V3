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
        self.worker.terminate(); self.worker.wait(2)
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
if __name__=="__main__":unittest.main(verbosity=2)
