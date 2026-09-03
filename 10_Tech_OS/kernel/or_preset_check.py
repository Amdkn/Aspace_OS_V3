#!/usr/bin/env python3
"""Verifie l'acces a l'API OpenRouter presets pour t_24db1c81 (run 18).
Lit la cle dans le .env du profil, ne l'imprime jamais."""
import json, os, sys, urllib.request

env_path = r"C:\Users\amado\AppData\Local\hermes\profiles\yaz_spec_l0\.env"
key = None
with open(env_path, encoding="utf-8") as f:
    for line in f:
        if line.strip().startswith("OPENROUTER_API_KEY="):
            key = line.split("=", 1)[1].strip().strip('"').strip("'")
            break
if not key:
    print("NO_KEY")
    sys.exit(2)
print("key_loaded=yes prefix=%s...%s" % (key[:8], key[-4:]))

req = urllib.request.Request(
    "https://openrouter.ai/api/v1/presets",
    headers={"Authorization": "Bearer " + key},
)
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        body = r.read().decode()
        print("status=200")
        data = json.loads(body)
        items = data.get("data", data)
        if isinstance(items, list):
            print("preset_count=%d" % len(items))
            for p in items[:20]:
                if isinstance(p, dict):
                    print("preset:", p.get("slug") or p.get("id"), "| model:", (p.get("model") or ""))
        else:
            print(json.dumps(data)[:800])
except urllib.error.HTTPError as e:
    print("HTTPError", e.code, e.read().decode()[:300])
