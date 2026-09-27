from pathlib import Path
import base64, hashlib, json, mimetypes, os, re, subprocess, uuid
from datetime import datetime, timezone

ROOT = Path(r"C:\Users\amado\ASpace_OS_V3\00_Amadeus\10_Observers\agent-os")
OUT = Path(r"C:\Users\amado\.aspace\supabase\agent_os_sync")
OUT.mkdir(parents=True, exist_ok=True)
for p in OUT.glob("*.sql"):
    p.unlink()

def git(*args):
    return subprocess.check_output(["git","-C",str(ROOT),*args], text=True, encoding="utf-8", errors="replace").strip()

git_sha = git("rev-parse","HEAD")
branch = git("rev-parse","--abbrev-ref","HEAD")
status_lines = subprocess.check_output(["git","-C",str(ROOT),"status","--porcelain"], text=True, encoding="utf-8", errors="replace").splitlines()
dirty_paths = set()
for line in status_lines:
    p=line[3:].strip().replace("\\","/")
    if " -> " in p:
        p=p.split(" -> ",1)[1]
    dirty_paths.add(p)

patterns = [
    "citadel/data/**/*",
    "citadel/skills/**/*",
    "citadel/decisions/**/*",
    "standards/**/*",
    "profiles/**/*",
    "references/**/*",
]
files=[]
for pat in patterns:
    files += [p for p in ROOT.glob(pat) if p.is_file()]
for name in ("README.md","config.yml","CHANGELOG.md"):
    p=ROOT/name
    if p.exists(): files.append(p)

# Preserve richness, omit only obvious backup/runtime log artifacts.
files=sorted(set(p for p in files if p.suffix.lower() not in {".bak",".log"}))

def kind(rel):
    s=rel.replace("\\","/")
    if s.startswith("citadel/data/"): return "collector_data"
    if s.startswith("citadel/skills/"): return "skill_document"
    if s.startswith("citadel/decisions/"): return "decision_artifact"
    if s.startswith("standards/"): return "standard"
    if s.startswith("profiles/"): return "profile"
    if s.startswith("references/"): return "reference"
    if s=="README.md": return "readme"
    if s=="config.yml": return "config"
    if s=="CHANGELOG.md": return "changelog"
    return "artifact"

def observed_from_json(obj):
    if isinstance(obj,dict):
        v=obj.get("generated_at") or obj.get("created_at") or obj.get("timestamp")
        if isinstance(v,str):
            return v
    return None

assets=[]
entities=[]

def add_entity(etype,key,name,path,payload,obs=None):
    entities.append({
        "entity_type":etype,
        "entity_key":str(key),
        "display_name":str(name) if name is not None else str(key),
        "source_path":path,
        "payload":payload,
        "observed_at":obs,
    })

for p in files:
    rel=p.relative_to(ROOT).as_posix()
    raw=p.read_bytes()
    sha=hashlib.sha256(raw).hexdigest()
    text=raw.decode("utf-8",errors="replace")
    ext=p.suffix.lower()
    cjson=None
    obs=None
    if ext==".json":
        try:
            cjson=json.loads(text)
            obs=None  # raw historical timestamp remains preserved inside content_json
        except Exception:
            cjson=None
    media=mimetypes.guess_type(p.name)[0] or {
        ".md":"text/markdown",".yml":"application/yaml",".yaml":"application/yaml",
        ".py":"text/x-python",".flag":"text/plain",".txt":"text/plain",".json":"application/json"
    }.get(ext,"text/plain")
    lifecycle="active"
    low=rel.lower()
    if "_trash_" in low or "/archive" in low or ".archive" in low: lifecycle="archive"
    elif "/_tmp" in low or Path(rel).name.startswith("_tmp"): lifecycle="temporary"
    assets.append({
        "relative_path":rel,
        "asset_type":kind(rel),
        "media_type":media,
        "sha256":sha,
        "git_sha":git_sha,
        "size_bytes":len(raw),
        "content_text":None if cjson is not None else text,
        "content_json":cjson,
        "metadata":{
            "extension":ext,
            "tracked": True,
            "working_tree_dirty": rel in dirty_paths,
            "lifecycle": lifecycle,
        },
        "observed_at":obs,
    })

    if not isinstance(cjson,dict):
        continue
    if rel.endswith("01_harnesses.json"):
        for k,v in (cjson.get("harnesses") or {}).items():
            add_entity("harness",k,k,rel,v,obs)
    elif rel.endswith("04_skills.json"):
        for v in (cjson.get("skills") or []):
            if isinstance(v,dict):
                key=f"{v.get('harness','unknown')}:{v.get('name','unnamed')}"
                add_entity("skill",key,v.get("name"),rel,v,obs)
    elif rel.endswith("08_agents.json"):
        for tier,arr in (cjson.get("tiers") or {}).items():
            for v in arr or []:
                if isinstance(v,dict):
                    key=f"{tier}:{v.get('name','unnamed')}"
                    add_entity("agent",key,v.get("name"),rel,v,obs)
    elif rel.endswith("09_frameworks.json"):
        for v in (cjson.get("frameworks") or []):
            if isinstance(v,dict):
                add_entity("framework",v.get("name"),v.get("name"),rel,v,obs)
    elif rel.endswith("10_domains.json"):
        for v in (cjson.get("domains") or []):
            if isinstance(v,dict):
                key=v.get("jerry_domain") or v.get("name")
                add_entity("business_domain",key,key,rel,v,obs)
    elif rel.endswith("11_memory.json"):
        for k,v in (cjson.get("entities") or {}).items():
            add_entity("memory_component",k,k,rel,v,obs)
    elif rel.endswith("06_connections.json"):
        for k in ("mcp_servers","crons","heartbeat"):
            if k in cjson:
                add_entity("connection_surface",k,k,rel,cjson[k],obs)

run_id=str(uuid.uuid4())
begin=f"""insert into aspace.sync_run
(id,world_id,source_git_sha,source_branch,source_root,mode,status,metadata)
values ('{run_id}'::uuid,'agent_os','{git_sha}','{branch}',
'C:/Users/amado/ASpace_OS_V3/00_Amadeus/10_Observers/agent-os','snapshot','running',
'{{"working_tree_dirty":{str(bool(status_lines)).lower()},"selected_files":{len(files)}}}'::jsonb)
on conflict (id) do nothing;
"""
(OUT/"000_begin.sql").write_text(begin,encoding="utf-8")

BATCH=18
for i in range(0,len(assets),BATCH):
    aa=assets[i:i+BATCH]
    paths={a["relative_path"] for a in aa}
    ee=[e for e in entities if e["source_path"] in paths]
    payload={"assets":aa,"entities":ee}
    b64=base64.b64encode(json.dumps(payload,ensure_ascii=False,separators=(",",":")).encode("utf-8")).decode("ascii")
    sql=f"""
with payload as (
  select convert_from(decode('{b64}','base64'),'UTF8')::jsonb as j
), asset_rows as (
  select *
  from jsonb_to_recordset((select j->'assets' from payload)) as x(
    relative_path text, asset_type text, media_type text, sha256 text, git_sha text,
    size_bytes bigint, content_text text, content_json jsonb, metadata jsonb, observed_at timestamptz
  )
)
insert into aspace.world_asset
(world_id,sync_run_id,relative_path,asset_type,media_type,sha256,git_sha,size_bytes,
 content_text,content_json,metadata,observed_at,synced_at)
select 'agent_os','{run_id}'::uuid,relative_path,asset_type,media_type,sha256,git_sha,size_bytes,
       content_text,content_json,metadata,observed_at,now()
from asset_rows
on conflict (world_id,relative_path) do update set
  sync_run_id=excluded.sync_run_id,
  asset_type=excluded.asset_type,
  media_type=excluded.media_type,
  sha256=excluded.sha256,
  git_sha=excluded.git_sha,
  size_bytes=excluded.size_bytes,
  content_text=excluded.content_text,
  content_json=excluded.content_json,
  metadata=excluded.metadata,
  observed_at=excluded.observed_at,
  synced_at=now();

with payload as (
  select convert_from(decode('{b64}','base64'),'UTF8')::jsonb as j
), entity_rows as (
  select *
  from jsonb_to_recordset((select j->'entities' from payload)) as x(
    entity_type text, entity_key text, display_name text, source_path text,
    payload jsonb, observed_at timestamptz
  )
)
insert into aspace.world_entity
(world_id,sync_run_id,entity_type,entity_key,display_name,source_path,source_asset_id,
 payload,observed_at,synced_at)
select 'agent_os','{run_id}'::uuid,e.entity_type,e.entity_key,e.display_name,e.source_path,a.id,
       e.payload,e.observed_at,now()
from entity_rows e
join aspace.world_asset a on a.world_id='agent_os' and a.relative_path=e.source_path
on conflict (world_id,entity_type,entity_key) do update set
  sync_run_id=excluded.sync_run_id,
  display_name=excluded.display_name,
  source_path=excluded.source_path,
  source_asset_id=excluded.source_asset_id,
  payload=excluded.payload,
  observed_at=excluded.observed_at,
  synced_at=now();
"""
    (OUT/f"{100+i//BATCH:03d}_batch.sql").write_text(sql,encoding="utf-8")

finish=f"""update aspace.sync_run
set status='completed',
    asset_count=(select count(*) from aspace.world_asset where world_id='agent_os' and sync_run_id='{run_id}'::uuid),
    entity_count=(select count(*) from aspace.world_entity where world_id='agent_os' and sync_run_id='{run_id}'::uuid),
    completed_at=now()
where id='{run_id}'::uuid;
"""
(OUT/"999_finish.sql").write_text(finish,encoding="utf-8")
summary={
  "run_id":run_id,"git_sha":git_sha,"branch":branch,"dirty":bool(status_lines),
  "assets":len(assets),"entities":len(entities),
  "batches":len(list(OUT.glob("*_batch.sql"))),
  "bytes":sum(a["size_bytes"] for a in assets),
}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary))
