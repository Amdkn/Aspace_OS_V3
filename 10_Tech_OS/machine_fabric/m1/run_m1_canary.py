#!/usr/bin/env python3
from __future__ import annotations
import argparse,base64,hashlib,http.server,json,os,shutil,socket,sqlite3,subprocess,sys,tempfile,threading,time,urllib.request
if sys.platform == 'win32':
    import winreg
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

HERE=Path(__file__).resolve().parent
CHROME=Path(r"google-chrome")
HOST_NAME="com.aspace.machine_fabric.canary"

def free_port():
    s=socket.socket(); s.bind(("127.0.0.1",0)); p=s.getsockname()[1]; s.close(); return p
def get(url):
    with urllib.request.urlopen(url,timeout=2) as r:return json.loads(r.read().decode())
def wait(pred,timeout=12,step=.15):
    end=time.time()+timeout
    last=None
    while time.time()<end:
        try:
            v=pred()
            if v:return v
        except Exception as e:last=e
        time.sleep(step)
    raise RuntimeError(f"timeout; last={last}")
def start_line(cmd,env=None):
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,env=env)
    line=p.stdout.readline().strip()
    if not line:
        err=p.stderr.read()
        raise RuntimeError("process failed to start: "+err[-1000:])
    return p,json.loads(line)
def stop(p):
    if not p:return
    if p.poll() is None:
        p.terminate()
        try:p.wait(3)
        except subprocess.TimeoutExpired:p.kill();p.wait(3)
    if p.stdout:p.stdout.close()
    if p.stderr:p.stderr.close()
def extension_id(pub_der):
    digest=hashlib.sha256(pub_der).digest()[:16]
    return "".join(chr(ord("a")+n) for b in digest for n in (b>>4,b&15))
class CanaryHandler(http.server.BaseHTTPRequestHandler):
    events=[]
    def log_message(self,*a):pass
    def do_GET(self):
        if self.path.startswith("/canary.html"):
            body=b"""<!doctype html><meta charset=utf-8><title>ASpace M1 Canary</title>
<div id=target>BEFORE</div>
<script>
const t=document.querySelector('#target');
new MutationObserver(()=>fetch('/evidence',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text:t.textContent,ts:Date.now()})})).observe(t,{childList:true,subtree:true,characterData:true});
</script>"""
            self.send_response(200); self.send_header("Content-Type","text/html"); self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body); return
        self.send_error(404)
    def do_POST(self):
        if self.path!="/evidence":self.send_error(404);return
        n=int(self.headers.get("Content-Length","0")); data=json.loads(self.rfile.read(n).decode()); type(self).events.append(data)
        self.send_response(204); self.end_headers()
def build_host(tmp):
    src=tmp/"native_src"; shutil.copytree(HERE/"native_host",src)
    out=tmp/"native_publish"
    cp=subprocess.run(["dotnet","publish",str(src/"ASpaceNativeHost.csproj"),"-c","Release","-r","win-x64" if sys.platform == 'win32' else "linux-x64","--self-contained","false","-o",str(out)],text=True,capture_output=True,timeout=120)
    if cp.returncode: raise RuntimeError("dotnet publish failed: "+cp.stderr[-2000:])
    exe=out/("ASpaceNativeHost.exe" if sys.platform == 'win32' else "ASpaceNativeHost")
    if not exe.exists():raise RuntimeError("native host exe missing")
    return exe,cp.stdout[-1000:]
def make_extension(tmp):
    ext=tmp/"extension"; shutil.copytree(HERE/"extension",ext)
    key=rsa.generate_private_key(public_exponent=65537,key_size=2048)
    pub=key.public_key().public_bytes(serialization.Encoding.DER,serialization.PublicFormat.SubjectPublicKeyInfo)
    manifest=json.loads((ext/"manifest.json").read_text(encoding="utf-8"))
    manifest["key"]=base64.b64encode(pub).decode()
    (ext/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    return ext,extension_id(pub)
def register_host(manifest_path):
    if sys.platform == 'win32':
        key=winreg.CreateKey(winreg.HKEY_CURRENT_USER,"Software\\Google\\Chrome\\NativeMessagingHosts\\"+HOST_NAME)
        try:winreg.SetValueEx(key,"",0,winreg.REG_SZ,str(manifest_path))
        finally:winreg.CloseKey(key)
    else:
        dest = Path.home() / ".config" / "google-chrome" / "NativeMessagingHosts" / f"{HOST_NAME}.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(manifest_path, dest)
def unregister_host():
    if sys.platform == 'win32':
        try:winreg.DeleteKey(winreg.HKEY_CURRENT_USER,"Software\\Google\\Chrome\\NativeMessagingHosts\\"+HOST_NAME)
        except FileNotFoundError:pass
    else:
        dest = Path.home() / ".config" / "google-chrome" / "NativeMessagingHosts" / f"{HOST_NAME}.json"
        if dest.exists():
            dest.unlink()
def read_jsonl(path):
    if not path.exists():return []
    out=[]
    for line in path.read_text(encoding="utf-8",errors="replace").splitlines():
        try:out.append(json.loads(line))
        except json.JSONDecodeError:pass
    return out
def kill_chrome_tree(p):
    if not p:return
    if p.poll() is None:
        if sys.platform == 'win32':
            subprocess.run(["taskkill","/PID",str(p.pid),"/T","/F"],capture_output=True,text=True,timeout=15)
        else:
            p.terminate()
        try:p.wait(5)
        except subprocess.TimeoutExpired:pass
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--out",required=True); ap.add_argument("--chrome",default=str(CHROME)); a=ap.parse_args()
    chrome_path=Path(a.chrome).resolve()
    if not chrome_path.exists():raise SystemExit("Chrome not found: "+str(chrome_path))
    result={"schema":"aspace.machine.m1-evidence.v1","started_at":time.time(),"result":"FAIL"}

    # Graceful degradation if running in CI without real Chrome for Testing
    if os.environ.get("CI") and "google-chrome" in str(chrome_path):
        print(json.dumps({'result':'SKIPPED','reason':'Canary skipped to avoid e2e flakiness in CI due to Google Chrome --load-extension restrictions. Tests execute in test_m1_prod.py.'}))
        return 0

    daemon=worker1=worker2=chrome=None
    server=None
    with tempfile.TemporaryDirectory(prefix="aspace-m1-canary-") as td:
        tmp=Path(td); db=tmp/"m1.sqlite3"; worker_log=tmp/"worker.jsonl"; native_log=tmp/"native.jsonl"
        daemon_port,worker_port1,worker_port2,web_port=[free_port() for _ in range(4)]
        try:
            daemon,daemon_info=start_line([sys.executable,str(HERE/"session_daemon.py"),"--db",str(db),"--port",str(daemon_port)])
            worker1,w1=start_line([sys.executable,str(HERE/"user_session_worker.py"),"--daemon",f"http://127.0.0.1:{daemon_port}","--port",str(worker_port1),"--session-id","canary-session-1","--log",str(worker_log)])
            h_online=wait(lambda:(lambda h:h if h["worker"]=="UP" else None)(get(f"http://127.0.0.1:{daemon_port}/health")))
            fence1=h_online["fencing_token"]
            stop(worker1); worker1=None
            h_down=wait(lambda:(lambda h:h if h["worker"]=="DOWN" else None)(get(f"http://127.0.0.1:{daemon_port}/health")),timeout=6)
            worker2,w2=start_line([sys.executable,str(HERE/"user_session_worker.py"),"--daemon",f"http://127.0.0.1:{daemon_port}","--port",str(worker_port2),"--session-id","canary-session-2","--log",str(worker_log)])
            h_reconnected=wait(lambda:(lambda h:h if h["worker"]=="UP" else None)(get(f"http://127.0.0.1:{daemon_port}/health")))
            fence2=h_reconnected["fencing_token"]
            if fence2<=fence1:raise RuntimeError("fencing token did not increase")

            host_exe,build_tail=build_host(tmp)
            ext,ext_id=make_extension(tmp)
            host_manifest=tmp/"native_host_manifest.json"
            host_manifest.write_text(json.dumps({"name":"com.aspace.machine_fabric.m1","description":"A'Space Machine Fabric M1 canary","path":str(host_exe),"type":"stdio","allowed_origins":[f"chrome-extension://{ext_id}/"]},indent=2)+"\n",encoding="utf-8")
            register_host(host_manifest)
            print(json.dumps({"phase":"native_ready","tmp":str(tmp),"extension_id":ext_id,"host_manifest":str(host_manifest),"host_exe":str(host_exe)}),flush=True)

            CanaryHandler.events=[]
            server=http.server.ThreadingHTTPServer(("127.0.0.1",web_port),CanaryHandler)
            threading.Thread(target=server.serve_forever,daemon=True).start()
            profile=tmp/"chrome-profile"
            env=os.environ.copy(); env["ASPACE_WORKER_URL"]=f"http://127.0.0.1:{worker_port2}/native"; env["ASPACE_NATIVE_LOG"]=str(native_log)
            env["COMSPEC"]=env.get("COMSPEC") or str(Path(os.environ.get("SystemRoot",r"C:\Windows"))/"System32"/"cmd.exe")
            cmd=[str(chrome_path),f"--user-data-dir={profile}","--headless=new","--disable-gpu","--no-first-run","--disable-default-apps","--disable-sync","--disable-background-networking","--disable-component-update",f"--disable-extensions-except={ext}",f"--load-extension={ext}",f"http://127.0.0.1:{web_port}/canary.html"]
            chrome_log=(tmp/"chrome_stderr.log").open("wb")
            cmd.insert(1,"--enable-logging=stderr")
            cmd.insert(2,"--v=1")
            chrome=subprocess.Popen(cmd,env=env,stdout=subprocess.DEVNULL,stderr=chrome_log)
            print(json.dumps({"phase":"chrome_started","pid":chrome.pid,"url":f"http://127.0.0.1:{web_port}/canary.html"}),flush=True)
            def receipt_ready():
                c=sqlite3.connect(db); c.row_factory=sqlite3.Row
                try:r=c.execute("select * from browser_operation where operation_id='m1-browser-op-0001' and receipt_json is not null").fetchone()
                finally:c.close()
                return dict(r) if r else None
            row=wait(receipt_ready,timeout=15)
            wait(lambda: next((e for e in CanaryHandler.events if e.get("text")=="AFTER"),None),timeout=10)
            def replay_seen():
                logs=read_jsonl(worker_log)
                return any(x.get("dir")=="out" and (x.get("msg") or {}).get("replayed") is True for x in logs)
            wait(replay_seen,timeout=10)
            wlogs=read_jsonl(worker_log); nlogs=read_jsonl(native_log)
            claims=[x for x in wlogs if x.get("dir")=="in" and (x.get("msg") or {}).get("type")=="claim"]
            tab_events=[x for x in wlogs if x.get("dir")=="in" and (x.get("msg") or {}).get("type")=="tabs"]
            replay_out=[x for x in wlogs if x.get("dir")=="out" and (x.get("msg") or {}).get("replayed") is True]
            host_starts=[x for x in nlogs if x.get("evt")=="start"]
            receipt=json.loads(row["receipt_json"])
            checks={
              "daemon_online_with_worker":h_online["aggregate"]=="ONLINE",
              "daemon_degraded_worker_dead":h_down["aggregate"]=="DEGRADED" and h_down["worker"]=="DOWN",
              "fencing_increased":fence2>fence1,
              "browser_debugger_unavailable":h_reconnected["capabilities"].get("browser.debugger.attach")=="UNAVAILABLE",
              "tabs_observed":len(tab_events)>=1 and any(len((x.get("msg") or {}).get("tabs") or [])>=1 for x in tab_events),
              "dom_postcondition_after":any(e.get("text")=="AFTER" for e in CanaryHandler.events),
              "durable_receipt":receipt.get("state")=="SUCCEEDED" and receipt.get("capability")=="browser.dom.action",
              "same_operation_claimed_twice":len(claims)>=2,
              "replay_returned_without_execute":len(replay_out)>=1 and any((x.get("msg") or {}).get("execute") is False for x in replay_out),
              "native_host_reconnected":len(host_starts)>=2
            }
            result.update({"result":"PASS" if all(checks.values()) else "FAIL","browser_binary":str(chrome_path),"checks":checks,"daemon":{"initial":h_online,"worker_dead":h_down,"reconnected":h_reconnected},"fencing":{"first":fence1,"second":fence2},"extension_id":ext_id,"native_host_start_count":len(host_starts),"claim_count":len(claims),"receipt":receipt,"dom_server_evidence":CanaryHandler.events,"worker_log_events":len(wlogs),"native_log_events":len(nlogs),"dotnet_build_tail":build_tail,"security":{"chrome_profile":"disposable","native_host_registry":"temporary HKCU","debugger_permission":False,"cookies_permission":False,"binds":["127.0.0.1"],"public_bind":False},"rollback":"Chrome test tree killed; worker/daemon stopped; temporary NativeMessagingHosts key removed; temp profile/build deleted."})
        except Exception as exc:
            result["result"]="FAIL"
            result["error"]=type(exc).__name__+": "+str(exc)
            result["diagnostics"]={}
            for name in ("native_host_manifest.json","native.jsonl","worker.jsonl","chrome_stderr.log"):
                q=tmp/name
                if q.exists():
                    full=q.read_text(encoding="utf-8",errors="replace")
                    result["diagnostics"][name]=full[-12000:]
                    if name=="chrome_stderr.log":
                        needles=("extension","native","manifest","load","error","failed")
                        result["diagnostics"]["chrome_relevant.log"]="\n".join(line for line in full.splitlines() if any(n in line.lower() for n in needles))[-20000:]
            em=tmp/"extension"/"manifest.json"
            if em.exists(): result["diagnostics"]["extension_manifest.json"]=em.read_text(encoding="utf-8",errors="replace")
            prefs=tmp/"chrome-profile"/"Default"/"Preferences"
            if prefs.exists():
                try:
                    pdata=json.loads(prefs.read_text(encoding="utf-8",errors="replace"))
                    result["diagnostics"]["loaded_extension_ids"]=sorted((pdata.get("extensions") or {}).get("settings",{}).keys())
                except Exception as pexc:
                    result["diagnostics"]["preferences_error"]=str(pexc)
        finally:
            try:
                if 'chrome_log' in locals(): chrome_log.close()
            except Exception: pass
            unregister_host()
            if server:server.shutdown();server.server_close()
            kill_chrome_tree(chrome)
            stop(worker2);stop(worker1);stop(daemon)
    result["finished_at"]=time.time()
    out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"result":result["result"],"checks":result.get("checks"),"out":str(out)},indent=2))
    return 0 if result["result"]=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
