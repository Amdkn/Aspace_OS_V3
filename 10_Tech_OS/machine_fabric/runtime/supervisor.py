from __future__ import annotations
import ctypes, json, os, signal, socket, subprocess, sys, time
from pathlib import Path
from urllib.request import urlopen

MUTEX_NAME=r"Local\ASpace_DC_Sovereign_v1"
PROXY_VARS=("HTTP_PROXY","HTTPS_PROXY","ALL_PROXY","http_proxy","https_proxy","all_proxy","LLMTRIM_PROXY","NO_PROXY","no_proxy")

def atomic_json(path:Path,data:dict):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix(path.suffix+".tmp")
    tmp.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    os.replace(tmp,path)

def discover_repo(start:Path)->Path|None:
    for p in [start,*start.parents]:
        if (p/"10_Tech_OS"/"machine_fabric"/"gateway"/"gateway.py").exists():
            return p
    return None

DEFAULT_ROOT=Path(os.environ.get("ASPACE_DC_ROOT") or (Path.home()/".aspace"/"dc")).resolve()
ROOT=DEFAULT_ROOT
CONFIG=ROOT/"config.json"
cfg={}
if CONFIG.exists():
    try:cfg=json.loads(CONFIG.read_text(encoding="utf-8-sig"))
    except Exception:cfg={}
repo_env=os.environ.get("ASPACE_DC_REPO_ROOT") or cfg.get("repo_root")
WT=(Path(repo_env).resolve() if repo_env else discover_repo(Path(__file__).resolve()))
if WT is None:
    raise RuntimeError("A'Space DC repo_root unavailable; run dc.ps1 install from the repository first")
ALLOWED_ROOT=Path(os.environ.get("ASPACE_DC_ALLOWED_ROOT") or cfg.get("allowed_root") or Path.home()).resolve()
DATA=ROOT/"data"; LOGS=ROOT/"logs"; RUN=ROOT/"run"
PY=Path(sys.executable).resolve()
for p in (DATA,LOGS,RUN):p.mkdir(parents=True,exist_ok=True)

def clean_env():
    env=os.environ.copy()
    for key in PROXY_VARS:env.pop(key,None)
    env["NO_PROXY"]="127.0.0.1,localhost"; env["no_proxy"]="127.0.0.1,localhost"
    return env

def acquire_mutex():
    if sys.platform!="win32":return None
    k=ctypes.windll.kernel32
    h=k.CreateMutexW(None,False,MUTEX_NAME)
    if not h:raise OSError("CreateMutexW failed")
    if k.GetLastError()==183:
        print(json.dumps({"ok":True,"state":"ALREADY_RUNNING"}),flush=True)
        raise SystemExit(0)
    return h

def release_mutex(h):
    if h and sys.platform=="win32":
        try:ctypes.windll.kernel32.ReleaseMutex(h)
        finally:ctypes.windll.kernel32.CloseHandle(h)

def free_port():
    s=socket.socket(); s.bind(("127.0.0.1",0)); p=s.getsockname()[1]; s.close(); return p

def wait_http(url,timeout=12):
    end=time.time()+timeout; last=None
    while time.time()<end:
        try:
            with urlopen(url,timeout=1.5) as r:return json.loads(r.read().decode("utf-8","replace"))
        except Exception as e:last=e; time.sleep(.15)
    raise RuntimeError(f"timeout waiting for {url}: {last}")

def wait_tcp(port,timeout=12):
    end=time.time()+timeout; last=None
    while time.time()<end:
        try:
            with socket.create_connection(("127.0.0.1",port),timeout=.8):return
        except OSError as e:last=e; time.sleep(.15)
    raise RuntimeError(f"timeout waiting for 127.0.0.1:{port}: {last}")

def allow_executables():
    candidates=[
        Path(os.environ.get("COMSPEC",r"C:\Windows\System32\cmd.exe")),
        Path(r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"),
        PY,Path(r"C:\Program Files\Git\cmd\git.exe"),Path(r"C:\Program Files\nodejs\node.exe"),
        Path(r"C:\Program Files\nodejs\npm.cmd"),Path(r"C:\Program Files\nodejs\npx.cmd"),
    ]
    out=[]
    for p in candidates:
        if p.exists() and str(p) not in out:out.append(str(p))
    return out

class Stack:
    def __init__(self,generation:int):
        self.generation=generation; self.children={}; self.handles=[]
        self.ports={k:free_port() for k in ("filesystem","process","session","worker","gateway")}
        self.allow=allow_executables()
    def spawn(self,name,args):
        out=(LOGS/f"{name}.out.log").open("ab",buffering=0); err=(LOGS/f"{name}.err.log").open("ab",buffering=0)
        self.handles += [out,err]
        flags=getattr(subprocess,"CREATE_NO_WINDOW",0)|getattr(subprocess,"CREATE_NEW_PROCESS_GROUP",0)
        p=subprocess.Popen([str(PY),*map(str,args)],cwd=str(WT),env=clean_env(),stdin=subprocess.DEVNULL,stdout=out,stderr=err,creationflags=flags)
        self.children[name]=p; return p
    def start(self):
        mf=WT/"10_Tech_OS"/"machine_fabric"
        paths={"m0":mf/"m0"/"amf_m0.py","process":mf/"process"/"process_broker.py","session":mf/"m1"/"session_daemon.py","worker":mf/"m1"/"user_session_worker.py","gateway":mf/"gateway"/"gateway.py"}
        missing=[str(p) for p in paths.values() if not p.exists()]
        if missing:raise FileNotFoundError("missing runtime components: "+", ".join(missing))
        p=self.ports
        self.spawn("m0",[paths["m0"],"serve","--db",DATA/"m0.sqlite3","--allowed-root",ALLOWED_ROOT,"--port",p["filesystem"]]); wait_http(f"http://127.0.0.1:{p['filesystem']}/health")
        args=[paths["process"],"--db",DATA/"process.sqlite3","--allowed-root",ALLOWED_ROOT]
        for exe in self.allow:args += ["--allow-exe",exe]
        args += ["--port",p["process"]]
        self.spawn("process",args); wait_http(f"http://127.0.0.1:{p['process']}/health")
        self.spawn("session",[paths["session"],"--db",DATA/"session.sqlite3","--port",p["session"]]); wait_http(f"http://127.0.0.1:{p['session']}/health")
        self.spawn("worker",[paths["worker"],"--daemon",f"http://127.0.0.1:{p['session']}","--port",p["worker"],"--session-id","aspace-dc-sovereign","--log",LOGS/"worker.jsonl"])
        deadline=time.time()+12
        while time.time()<deadline:
            h=wait_http(f"http://127.0.0.1:{p['session']}/health",timeout=2)
            if h.get("worker")=="UP":break
            time.sleep(.2)
        self.spawn("gateway",[paths["gateway"],"--amf-url",f"http://127.0.0.1:{p['filesystem']}","--process-url",f"http://127.0.0.1:{p['process']}","--browser-url",f"http://127.0.0.1:{p['session']}","--usage-db",DATA/"gateway_usage.sqlite3","--transport","streamable-http","--host","127.0.0.1","--port",p["gateway"],"--name","aspace-dc-sovereign"])
        wait_tcp(p["gateway"])
        m={"schema":"aspace.dc.runtime.v1","state":"ONLINE","started_at":time.time(),"generation":self.generation,"supervisor_pid":os.getpid(),"repo_root":str(WT),"root":str(ROOT),"allowed_root":str(ALLOWED_ROOT),"ports":p,"pids":{k:v.pid for k,v in self.children.items()},"allow_exe":self.allow,"gateway_url":f"http://127.0.0.1:{p['gateway']}/mcp","health_urls":{"filesystem":f"http://127.0.0.1:{p['filesystem']}/health","process":f"http://127.0.0.1:{p['process']}/health","browser":f"http://127.0.0.1:{p['session']}/health"}}
        atomic_json(RUN/"runtime.json",m); print(json.dumps({"ok":True,"state":"ONLINE","generation":self.generation,"gateway_url":m["gateway_url"]}),flush=True)
    def dead(self):return [k for k,p in self.children.items() if p.poll() is not None]
    def stop(self):
        ps=list(self.children.values())
        for p in ps:
            if p.poll() is None:
                try:p.terminate()
                except Exception:pass
        end=time.time()+4
        while time.time()<end and any(p.poll() is None for p in ps):time.sleep(.1)
        for p in ps:
            if p.poll() is None:
                try:p.kill()
                except Exception:pass
        for h in self.handles:
            try:h.close()
            except Exception:pass
        self.children.clear(); self.handles.clear()

def main():
    mutex=acquire_mutex(); stop=False
    def request_stop(*_):
        nonlocal stop; stop=True
    for sig in (signal.SIGINT,signal.SIGTERM):
        try:signal.signal(sig,request_stop)
        except Exception:pass
    generation=0; stack=None
    try:
        while not stop:
            generation += 1; stack=Stack(generation)
            try:
                stack.start()
                while not stop:
                    dead=stack.dead()
                    if dead:
                        atomic_json(RUN/"last_failure.json",{"dead":dead,"at":time.time(),"generation":generation})
                        break
                    time.sleep(1)
            finally:
                stack.stop()
            if not stop:time.sleep(1)
    finally:
        try:(RUN/"runtime.json").unlink()
        except FileNotFoundError:pass
        release_mutex(mutex)
    return 0

if __name__=="__main__":raise SystemExit(main())
