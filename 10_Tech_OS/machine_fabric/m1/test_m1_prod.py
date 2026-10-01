import json,os,socket,subprocess,sys,tempfile,time,unittest,urllib.request,shutil
from pathlib import Path
from unittest.mock import patch

HERE=Path(__file__).parent.resolve()
DAEMON=HERE/"session_daemon.py"
WORKER=HERE/"user_session_worker.py"
INSTALLER=HERE/"installer.py"

sys.path.insert(0, str(HERE))
import installer

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
        self.t=tempfile.TemporaryDirectory()
        b=Path(self.t.name)
        self.db=b/"m1.db"
        self.log=b/"worker.jsonl"
        self.dp=free_port()
        self.wp=free_port()

        self.daemon=subprocess.Popen([sys.executable,str(DAEMON),"--db",str(self.db),"--port",str(self.dp)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        self.assertTrue(self.daemon.stdout.readline().strip())

        self.worker=self.start_worker("session-A")

    def start_worker(self,sid):
        p=subprocess.Popen([sys.executable,str(WORKER),"--daemon",f"http://127.0.0.1:{self.dp}","--port",str(self.wp),"--session-id",sid,"--log",str(self.log)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        line=p.stdout.readline().strip()
        self.assertTrue(line)
        return p

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

    def test_worker_and_daemon_reconnect(self):
        h=wait_health(f"http://127.0.0.1:{self.dp}/health",lambda x:x["worker"]=="UP")
        f1=h["fencing_token"]

        old_worker=self.worker
        old_worker.terminate(); old_worker.wait(2)
        if old_worker.stdout: old_worker.stdout.close()
        if old_worker.stderr: old_worker.stderr.close()

        h2=wait_health(f"http://127.0.0.1:{self.dp}/health",lambda x:x["worker"]=="DOWN",timeout=5)
        self.assertEqual(h2["aggregate"],"DEGRADED")

        self.worker=self.start_worker("session-A-reconnect")
        h3=wait_health(f"http://127.0.0.1:{self.dp}/health",lambda x:x["worker"]=="UP")
        self.assertGreater(h3["fencing_token"],f1)

    def test_claim_complete_and_replay(self):
        base=f"http://127.0.0.1:{self.wp}/native"

        hello_resp = post(base, {"type": "hello"})
        self.assertTrue(hello_resp["ok"])

        claim={"type":"claim","operation_id":"browser-op-test-1","fingerprint":"fingerprint-1","action":"browser.dom.action"}
        first=post(base,claim)
        self.assertTrue(first["execute"])

        receipt=post(base,{"type":"complete","operation_id":"browser-op-test-1","fingerprint":"fingerprint-1","evidence":{"before":"BEFORE","after":"AFTER","selector":"#target"}})
        self.assertEqual(receipt["state"],"SUCCEEDED")

        second=post(base,claim)
        self.assertFalse(second["execute"])
        self.assertTrue(second["replayed"])
        self.assertEqual(second["receipt"]["effect_digest"], receipt["effect_digest"])

if __name__=="__main__":
    unittest.main(verbosity=2)
