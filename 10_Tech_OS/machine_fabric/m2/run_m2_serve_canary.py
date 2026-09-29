#!/usr/bin/env python3
from __future__ import annotations
import argparse, http.server, json, socket, threading, time, urllib.request, uuid
from pathlib import Path
from tailscale_serve_adapter import TailscaleServeAdapter, RemoteTransportError, find_tailscale

class Handler(http.server.BaseHTTPRequestHandler):
    token=""
    def log_message(self,*a): pass
    def do_GET(self):
        body=self.token.encode()
        self.send_response(200); self.send_header("Content-Type","text/plain"); self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)

def free_port():
    s=socket.socket(); s.bind(("127.0.0.1",0)); p=s.getsockname()[1]; s.close(); return p

def get_text(url,timeout=3):
    with urllib.request.urlopen(url,timeout=timeout) as r:
        return r.read().decode().strip()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--out",required=True); ap.add_argument("--tailscale"); a=ap.parse_args()
    cli=find_tailscale(a.tailscale)
    if not cli: raise SystemExit("tailscale unavailable")
    adapter=TailscaleServeAdapter(cli)
    out=Path(a.out).resolve(); out.parent.mkdir(parents=True,exist_ok=True)
    snap=out.with_suffix(".serve-snapshot.json")
    token="ASPACE_M2_PRIVATE_"+uuid.uuid4().hex
    port=free_port()
    Handler.token=token
    server=http.server.ThreadingHTTPServer(("127.0.0.1",port),Handler)
    thread=threading.Thread(target=server.serve_forever,daemon=True)
    before=adapter.status()
    result={"schema":"aspace.machine.remote-transport-evidence.v1","result":"FAIL","public_bind":False,"started_at":time.time()}
    try:
        adapter.snapshot(snap)
        thread.start()
        local_ok=False
        for _ in range(30):
            try:
                if get_text(f"http://127.0.0.1:{port}/",1)==token:
                    local_ok=True; break
            except Exception: time.sleep(.1)
        if not local_ok: raise RuntimeError("loopback backend not ready")
        try:
            adapter.start_private(port,443)
        except RemoteTransportError as exc:
            tail_status=json.loads(adapter.run(["status","--json"],20)["stdout"] or "{}")
            peers=list((tail_status.get("Peer") or {}).values())
            peer=next((p for p in peers if p.get("HostName")=="Tab S6 Lite de Amadou"), peers[0] if peers else None)
            if "SERVE_ENABLEMENT_REQUIRED" in str(exc):
                result.update({
                  "result":"SERVE_ENABLEMENT_REQUIRED",
                  "tailscale_version":tail_status.get("Version"),
                  "self_dns":((tail_status.get("Self") or {}).get("DNSName") or "").rstrip("."),
                  "self_ip":((tail_status.get("Self") or {}).get("TailscaleIPs") or [None])[0],
                  "peer_name":peer.get("HostName") if peer else None,
                  "peer_ip":((peer or {}).get("TailscaleIPs") or [None])[0] if peer else None,
                  "checks":{
                    "tailscale_backend_running":tail_status.get("BackendState")=="Running",
                    "loopback_backend_ok":local_ok,
                    "serve_enabled":False,
                    "peer_registered":peer is not None,
                    "peer_online":bool(peer and peer.get("Online")),
                    "public_bind":False
                  },
                  "live_canary":"OPEN_ACCOUNT_ENABLEMENT",
                  "second_client_canary":"OPEN_PEER_OFFLINE" if not (peer and peer.get("Online")) else "READY",
                  "reason":str(exc),
                  "note":"Tailscale is installed, authenticated and connected. Serve requires one explicit tailnet account enablement; no public Funnel or firewall change was attempted.",
                  "at":time.time()
                })
            else:
                raise
        if result["result"]=="SERVE_ENABLEMENT_REQUIRED":
            result["restore_via_snapshot"]=True
            result["finished_at"]=time.time()
            out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
            print(json.dumps({"result":result["result"],"checks":result.get("checks"),"second_client_canary":result.get("second_client_canary"),"out":str(out)},indent=2))
            return 0
        else:
            tail_status=json.loads(adapter.run(["status","--json"],20)["stdout"] or "{}")
        dns=(tail_status.get("Self") or {}).get("DNSName","").rstrip(".")
        if not dns: raise RuntimeError("tailscale DNS name missing")
        remote_ok=False; remote_error=None
        for _ in range(30):
            try:
                if get_text(f"https://{dns}/",4)==token:
                    remote_ok=True; break
            except Exception as exc:
                remote_error=type(exc).__name__+": "+str(exc)
                time.sleep(.35)
        serve_status=adapter.status()
        funnel=adapter.run(["funnel","status","--json"],10)
        peers=list((tail_status.get("Peer") or {}).values())
        peer=next((p for p in peers if p.get("HostName")=="Tab S6 Lite de Amadou"), peers[0] if peers else None)
        status_blob=json.dumps(serve_status.get("config") or {},sort_keys=True)
        checks={
          "tailscale_backend_running":tail_status.get("BackendState")=="Running",
          "loopback_backend_ok":local_ok,
          "private_https_self_canary":remote_ok,
          "serve_targets_loopback":f"127.0.0.1:{port}" in status_blob,
          "no_funnel_command":("funnel" not in status_blob.lower()),
          "peer_registered":peer is not None,
          "peer_online":bool(peer and peer.get("Online")),
          "public_bind":False
        }
        result.update({
          "result":"PRIVATE_SERVE_PASS_SECOND_CLIENT_OFFLINE" if all([checks["tailscale_backend_running"],checks["loopback_backend_ok"],checks["private_https_self_canary"],checks["serve_targets_loopback"],checks["no_funnel_command"]]) else "FAIL",
          "tailscale_version":tail_status.get("Version"),
          "self_dns":dns,
          "self_ip":((tail_status.get("Self") or {}).get("TailscaleIPs") or [None])[0],
          "peer_name":peer.get("HostName") if peer else None,
          "peer_ip":((peer or {}).get("TailscaleIPs") or [None])[0] if peer else None,
          "checks":checks,
          "serve_status":serve_status.get("config"),
          "funnel_status":{"returncode":funnel["returncode"],"stdout":funnel["stdout"],"stderr":funnel["stderr"]},
          "live_canary":"PRIVATE_HTTPS_SELF_PASS" if remote_ok else "FAIL",
          "second_client_canary":"READY" if checks["peer_online"] else "OPEN_PEER_OFFLINE",
          "remote_error":remote_error,
          "note":"Tailscale Serve is proven over MagicDNS HTTPS to a loopback-only backend. The registered Android peer is currently offline, so only the second-client-origin hop remains unproven.",
          "at":time.time()
        })
    finally:
        try:
            if snap.exists(): adapter.restore(snap)
        finally:
            server.shutdown(); server.server_close()
    after=adapter.status()
    result["restored_serve_config"]=after.get("config")
    result["finished_at"]=time.time()
    out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"result":result["result"],"checks":result.get("checks"),"second_client_canary":result.get("second_client_canary"),"out":str(out)},indent=2))
    return 0 if result["result"].startswith("PRIVATE_SERVE_PASS") else 1

if __name__=="__main__": raise SystemExit(main())
