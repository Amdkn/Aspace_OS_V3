import json,os,sys,tempfile,unittest
from pathlib import Path
from tailscale_serve_adapter import TailscaleServeAdapter,RemoteTransportError

FAKE=r'''import json,sys
from pathlib import Path
args=sys.argv[1:]
log=Path(__file__).with_name("calls.jsonl")
with log.open("a",encoding="utf-8") as f:f.write(json.dumps(args)+"\n")
if args[:3]==["serve","status","--json"]:
    print(json.dumps({"Web":{"svc:test":{"Handlers":{"/":{"Proxy":"http://127.0.0.1:9000"}}}}}));raise SystemExit(0)
if args[:3]==["serve","get-config","--all"]:
    print('{"version":"0.0.1","snapshot":true}');raise SystemExit(0)
if len(args)>=4 and args[:3]==["serve","set-config","--all"]:
    if not Path(args[3]).exists():raise SystemExit(8)
    raise SystemExit(0)
if args and args[0]=="serve":
    if any("funnel" in x.lower() for x in args):raise SystemExit(9)
    raise SystemExit(0)
raise SystemExit(2)
'''
class T(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();self.b=Path(self.t.name);self.fake=self.b/"fake.py";self.fake.write_text(FAKE);self.a=TailscaleServeAdapter([sys.executable,str(self.fake)])
    def tearDown(self):self.t.cleanup()
    def calls(self):
        p=self.b/"calls.jsonl";return [json.loads(x) for x in p.read_text().splitlines()] if p.exists() else []
    def test_status_snapshot_restore(self):
        self.assertEqual(self.a.status()["state"],"AVAILABLE")
        snap=self.a.snapshot(self.b/"snapshot.json");self.assertTrue(snap.exists());self.a.restore(snap)
        calls=self.calls();self.assertIn(["serve","status","--json"],calls);self.assertTrue(any(x[:2]==["serve","get-config"] for x in calls));self.assertTrue(any(x[:2]==["serve","set-config"] for x in calls))
    def test_private_start_is_loopback_and_never_funnel(self):
        self.a.start_private(9000,8443);self.a.stop_private(8443)
        calls=self.calls();start=next(x for x in calls if "--bg" in x)
        self.assertIn("http://127.0.0.1:9000",start);self.assertFalse(any("funnel" in y.lower() for x in calls for y in x))
if __name__=="__main__":unittest.main(verbosity=2)
