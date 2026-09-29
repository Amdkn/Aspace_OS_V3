import importlib.util,json,os,socket,subprocess,sys,tempfile,time,unittest,urllib.request
from pathlib import Path
HERE=Path(__file__).parent
P=HERE/"process_broker.py"
s=importlib.util.spec_from_file_location("pb",P);pb=importlib.util.module_from_spec(s);s.loader.exec_module(pb)
FIX=HERE/"interactive_fixture.py"

def op(engine,opid,cap,action,payload,risk=None):
    x={"schema":pb.m0.OP_SCHEMA,"operation_id":opid,"capability":cap,"action":action,"authority":{"risk_class":risk or pb.RISK[cap],"scopes":[engine.scope],"approval_ref":None},"fingerprint":"","precondition":{},"replay":"return_receipt","payload":payload}
    x["fingerprint"]=pb.m0.semantic_fingerprint(x);return x
def wait_text(engine,sid,needle,timeout=5):
    end=time.time()+timeout
    while time.time()<end:
        r=engine.execute(op(engine,"read-"+str(time.time_ns()),"machine.process.read","read",{"session_id":sid}))
        if needle in r["result"]["text"]:return r
        time.sleep(.1)
    raise AssertionError("missing "+needle)
def free_port():
    s=socket.socket();s.bind(("127.0.0.1",0));p=s.getsockname()[1];s.close();return p
def post(url,payload):
    b=json.dumps(payload).encode();q=urllib.request.Request(url,data=b,method="POST",headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(q,timeout=3) as r:return json.loads(r.read().decode())
def get(url):
    with urllib.request.urlopen(url,timeout=3) as r:return json.loads(r.read().decode())

class T(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();self.b=Path(self.t.name);self.root=self.b/"root";self.root.mkdir();self.db=self.b/"p.db";self.e=pb.Engine(self.db,self.root,[sys.executable])
    def tearDown(self):
        c=self.e.con()
        try:rows=c.execute("select session_id,pid from process_session where state='RUNNING'").fetchall()
        finally:c.close()
        for r in rows:
            if pb.pid_alive(int(r["pid"])):pb.kill_tree(int(r["pid"]))
        self.t.cleanup()
    def start(self,opid="start-0001"):
        r=self.e.execute(op(self.e,opid,"machine.process.start","start",{"argv":[sys.executable,str(FIX)],"cwd":str(self.root)}))
        self.assertEqual(r["state"],"SUCCEEDED");return r
    def test_start_replay_interact_read_stop(self):
        a=self.start();sid=a["result"]["session_id"];pid=a["result"]["pid"];wait_text(self.e,sid,"READY")
        b=self.e.execute(op(self.e,"start-0001","machine.process.start","start",{"argv":[sys.executable,str(FIX)],"cwd":str(self.root)}))
        self.assertTrue(b["replayed"]);self.assertEqual(b["result"]["pid"],pid)
        i=self.e.execute(op(self.e,"interact-0001","machine.process.interact","write_stdin",{"session_id":sid,"text":"hello"}));self.assertEqual(i["state"],"SUCCEEDED")
        wait_text(self.e,sid,"ECHO:hello")
        i2=self.e.execute(op(self.e,"interact-0001","machine.process.interact","write_stdin",{"session_id":sid,"text":"hello"}));self.assertTrue(i2["replayed"])
        r=wait_text(self.e,sid,"ECHO:hello");self.assertEqual(r["result"]["text"].count("ECHO:hello"),1)
        st=self.e.execute(op(self.e,"stop-0001","machine.process.stop","stop",{"session_id":sid}));self.assertEqual(st["state"],"SUCCEEDED");self.assertFalse(pb.pid_alive(pid))
    def test_policy_denies_shell_and_nonallowlisted_executable(self):
        x=op(self.e,"deny-shell","machine.process.start","start",{"argv":[sys.executable,str(FIX)],"cwd":str(self.root),"shell":True})
        r=self.e.execute(x);self.assertEqual(r["state"],"DENIED")
        fake=self.root/"fake.exe";fake.write_text("x")
        y=op(self.e,"deny-exe-1","machine.process.start","start",{"argv":[str(fake)],"cwd":str(self.root)})
        self.assertEqual(self.e.execute(y)["state"],"DENIED")
    def test_whole_tree_stop(self):
        a=self.start("start-tree");sid=a["result"]["session_id"];wait_text(self.e,sid,"READY")
        self.e.execute(op(self.e,"spawn-1","machine.process.interact","write_stdin",{"session_id":sid,"text":"spawn"}))
        r=wait_text(self.e,sid,"CHILD:");child=int([x for x in r["result"]["text"].splitlines() if x.startswith("CHILD:")][-1].split(":")[1]);self.assertTrue(pb.pid_alive(child))
        self.e.execute(op(self.e,"stop-tree","machine.process.stop","stop",{"session_id":sid}));time.sleep(.3);self.assertFalse(pb.pid_alive(child))
    def test_broker_restart_truthfully_degrades_interact_but_read_stop_survive(self):
        port=free_port();db=self.b/"restart.db";root=self.b/"restart-root";root.mkdir()
        cmd=[sys.executable,str(P),"--db",str(db),"--allowed-root",str(root),"--allow-exe",sys.executable,"--port",str(port)]
        p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True);self.assertTrue(p.stdout.readline().strip())
        e=pb.Engine(db,root,[sys.executable]);start=op(e,"restart-start","machine.process.start","start",{"argv":[sys.executable,str(FIX)],"cwd":str(root)})
        rec=post(f"http://127.0.0.1:{port}/operations",start);sid=rec["result"]["session_id"];pid=rec["result"]["pid"]
        end=time.time()+4
        while time.time()<end:
            rr=post(f"http://127.0.0.1:{port}/operations",op(e,"rr-"+str(time.time_ns()),"machine.process.read","read",{"session_id":sid}))
            if "READY" in rr["result"]["text"]:break
            time.sleep(.1)
        p.terminate();p.wait(3);p.stdout.close();p.stderr.close();self.assertTrue(pb.pid_alive(pid))
        p2=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True);self.assertTrue(p2.stdout.readline().strip())
        try:
            h=get(f"http://127.0.0.1:{port}/health");self.assertEqual(h["aggregate"],"DEGRADED");self.assertIn(sid,h["detached_sessions"])
            inter=post(f"http://127.0.0.1:{port}/operations",op(e,"after-restart-interact","machine.process.interact","write_stdin",{"session_id":sid,"text":"x"}));self.assertEqual(inter["state"],"FAILED");self.assertIn("INTERACTION_UNAVAILABLE_AFTER_RESTART"," ".join(inter["evidence"]))
            rd=post(f"http://127.0.0.1:{port}/operations",op(e,"after-restart-read","machine.process.read","read",{"session_id":sid}));self.assertIn("READY",rd["result"]["text"])
            st=post(f"http://127.0.0.1:{port}/operations",op(e,"after-restart-stop","machine.process.stop","stop",{"session_id":sid}));self.assertEqual(st["state"],"SUCCEEDED");self.assertFalse(pb.pid_alive(pid))
        finally:
            p2.terminate();p2.wait(3);p2.stdout.close();p2.stderr.close()
if __name__=="__main__":unittest.main(verbosity=2)
