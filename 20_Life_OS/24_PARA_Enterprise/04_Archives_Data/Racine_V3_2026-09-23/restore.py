"""Restore archived root entries. Dry-run by default; --apply performs restoration."""
import argparse, hashlib, json, pathlib
base = pathlib.Path(__file__).resolve().parent
p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--apply", action="store_true")
a = p.parse_args()
m = json.loads((base/"manifest.json").read_text(encoding="utf-8"))
root = pathlib.Path(m["root"])
problems = []
for item in m["entries"]:
    src, dst = base/item["destination"], root/item["source"]
    if dst.exists():
        problems.append("Original path occupied: "+str(dst))
    for f in item["files"]:
        q = src/f["relative"] if item["type"]=="directory" else src
        if not q.is_file():
            problems.append("Missing: "+str(q))
            continue
        with q.open("rb") as stream:
            digest = hashlib.file_digest(stream,"sha256").hexdigest()
        if digest != f["sha256"]:
            problems.append("Changed: "+str(q))
for item in m["metadata_updates"]:
    q=root/item["path"]
    if not q.is_file() or hashlib.sha256(q.read_bytes()).hexdigest()!=item["after_sha256"]:
        problems.append("Live metadata changed; manual reconciliation needed: "+str(q))
if problems:
    raise SystemExit("\n".join(problems))
if not a.apply:
    print("RESTORE_READY: "+str(len(m["entries"]))+" entries. Use --apply to restore.")
else:
    for item in m["entries"]:
        (base/item["destination"]).rename(root/item["source"])
    for item in m["metadata_updates"]:
        (root/item["path"]).write_bytes((base/item["backup"]).read_bytes())
    m["state"]="restored"
    (base/"manifest.json").write_text(json.dumps(m,indent=2),encoding="utf-8")
    print("RESTORED: no files deleted.")
