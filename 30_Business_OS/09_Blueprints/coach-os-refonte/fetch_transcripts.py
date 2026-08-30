# -*- coding: utf-8 -*-
"""Recupere les transcripts YouTube via le MCP HTTP transcriptapi.com.

Pourquoi un script plutot que l'outil MCP en session : un transcript de
conference fait 10 a 20 k tokens. Dix-huit d'entre eux satureraient n'importe
quel contexte avant meme le debut de l'analyse. Ici ils vont sur disque, et
les agents delegues les lisent fichier par fichier.

Piege paye : Cloudflare renvoie 403 (error 1010, browser_signature_banned)
sur le User-Agent par defaut d'urllib. Il faut un UA de navigateur.
"""
import json, urllib.request, urllib.error, pathlib, sys, time

URL = "https://transcriptapi.com/mcp"
TOK = "sk_Ajtxu29isCP9YMAGpPG6IMQ1rKnsI4VnaYvcHOQnxJo"
UA  = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
       "(KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36")
OUT = pathlib.Path(__file__).parent / "transcripts"

IDS = """KwhgfwOSToQ l0FLhNqBOic VGN22pPpb-8 il1c1a2FufU lXZb21CfeIY Ib5t2RLtxvM
YnNF55QV0zs 8G_1-3IO4ZQ jt1Pbr_n6oU Sir59K8ZDPU Q0VkgCyNVUg 9QebvrrY3KY
khVX_BUnEwU 9HbzAWnKbo4 hmjRc6KJ-hw PZsJfBVDZZc xIt_mTQp6mY 31GUkCBD-Uc""".split()

H = {"Content-Type": "application/json",
     "Accept": "application/json, text/event-stream",
     "Authorization": "Bearer " + TOK, "User-Agent": UA}

def post(payload):
    req = urllib.request.Request(URL, data=json.dumps(payload).encode(), headers=H)
    raw = urllib.request.urlopen(req, timeout=180).read().decode("utf-8", "replace")
    for line in raw.splitlines():                      # transport SSE
        if line.startswith("data:"):
            return json.loads(line[5:].strip())
    return json.loads(raw) if raw.strip() else {}

def text_of(res):
    out = []
    for c in res.get("result", {}).get("content", []):
        if c.get("type") == "text":
            out.append(c["text"])
    return "\n".join(out)

def main():
    post({"jsonrpc": "2.0", "id": 1, "method": "initialize",
          "params": {"protocolVersion": "2025-06-18", "capabilities": {},
                     "clientInfo": {"name": "amdk", "version": "1"}}})
    post({"jsonrpc": "2.0", "method": "notifications/initialized"})
    OUT.mkdir(parents=True, exist_ok=True)
    index = []
    for i, vid in enumerate(IDS, 1):
        dest = OUT / f"{vid}.md"
        if dest.exists() and dest.stat().st_size > 500:
            print(f"[{i:2}/18] {vid} deja present"); continue
        url = f"https://www.youtube.com/watch?v={vid}"
        try:
            r = post({"jsonrpc": "2.0", "id": 100 + i, "method": "tools/call",
                      "params": {"name": "get_youtube_transcript",
                                 "arguments": {"video_url": url, "send_metadata": True,
                                               "format": "text", "include_timestamp": False}}})
            body = text_of(r)
            if not body.strip():
                print(f"[{i:2}/18] {vid} VIDE -> {json.dumps(r)[:200]}"); continue
            dest.write_text(body, encoding="utf-8")
            index.append((vid, len(body)))
            print(f"[{i:2}/18] {vid} {len(body):>7} caracteres")
        except urllib.error.HTTPError as e:
            print(f"[{i:2}/18] {vid} HTTP {e.code} {e.read()[:120]}")
        except Exception as e:
            print(f"[{i:2}/18] {vid} ECHEC {type(e).__name__}: {e}")
        time.sleep(1)
    print("\ntotal recupere :", len(list(OUT.glob('*.md'))), "sur", len(IDS))

if __name__ == "__main__":
    main()
