#!/usr/bin/env python3
"""Deterministic Jules refill/reconciliation loop for Tech OS.
No LLM is required to find READY work or launch Jules.
"""
from __future__ import annotations
import json, os, re, subprocess, sys, time, urllib.request
from pathlib import Path
from fleet_ownership import reserve, bind_session, require_running_owner, dispatch_lock, resolve_work

ROOT=Path(r"C:\Users\amado\ASpace_OS_V3")
PRD_ROOT=ROOT/"10_Tech_OS"/"PRD_Autonomy"
JULES="http://127.0.0.1:43118"
SOURCE="sources/github/Amdkn/Aspace_OS_V3"
MAX_ACTIVE=15
MAX_DISPATCH_PER_TICK=3
# One persistent Jules lane per S3 companion. Capacity is hierarchical, not a 20/30/50 pool.
CORE_LIMITS={"KERNEL":5,"LIFE":5,"BUSINESS":5}
PROJECTS=("Tech OS — Kernel Core","Tech OS — Buzz Core","Tech OS — Life Core")
TERMINAL={"COMPLETED","FAILED","CANCELLED","CANCELED"}
SKIP_MARKERS=("[SOLARPUNK]","[BEDROCK]","[FLEET]")
KERNEL_MAP={
 "KER-19":("K2_SYSTEM1_DECISION","KPRD-020"),
 "KER-20":("K2_SYSTEM1_DECISION","KPRD-021"),
 "KER-21":("K2_SYSTEM1_DECISION","KPRD-022"),
 "KER-22":("K4_SERVING_COMPUTE","KPRD-041"),
 "KER-24":("K1_ORCHESTRATION_RELAY","KPRD-010"),
 "KER-25":("K6_OBSERVABILITY_AGENT_OS","KPRD-060"),
 "KER-23":("K7_INTEGRATION_CONVERGENCE","KPRD-070"),
}

def run(*args):
 p=subprocess.run(list(args),capture_output=True,text=True,encoding="utf-8")
 if p.returncode:
  raise RuntimeError((p.stderr or p.stdout).strip())
 return p.stdout

def orca_json(*args):
 return json.loads(run("orca",*args,"--json"))

def http_json(path,method="GET",body=None,timeout=10):
 data=None if body is None else json.dumps(body).encode()
 req=urllib.request.Request(JULES+path,data=data,method=method,
                            headers={"Content-Type":"application/json"})
 with urllib.request.urlopen(req,timeout=timeout) as r:
  return json.load(r)

def ensure_proxy():
 try:
  return bool(http_json("/health",timeout=2).get("ok"))
 except Exception:
  subprocess.Popen(["powershell.exe","-NoProfile","-WindowStyle","Hidden",
                    "-File",str(ROOT/"10_Tech_OS"/"kernel"/"start_jules_proxy.ps1")],
                   creationflags=getattr(subprocess,"CREATE_NO_WINDOW",0))
  for _ in range(10):
   time.sleep(1)
   try:
    if http_json("/health",timeout=2).get("ok"): return True
   except Exception: pass
  return False

def list_issues():
 out=[]
 for project in PROJECTS:
  data=orca_json("linear","list-issues","--project",project)
  out.extend(data["result"]["issues"])
 seen={}
 for x in out: seen[x["identifier"]]=x
 return list(seen.values())

def context(issue_id):
 return orca_json("linear","issue",issue_id,"--relations")["result"]

def blocker_ids(ctx):
 return [r["relatedIssue"]["identifier"] for r in ctx.get("relations",[])
         if r.get("relationship")=="blockedBy"]

def status_of(issue_id):
 return orca_json("linear","issue",issue_id)["result"]["issue"]["state"]["type"]

def classify(issue):
 iid=issue["identifier"]; title=issue["title"]
 if iid in KERNEL_MAP: return KERNEL_MAP[iid]
 m=re.search(r"\[(KPRD-\d+)\]\[(K\d+)\]",title)
 if m: return ("KERNEL_"+m.group(2),m.group(1))
 m=re.search(r"\[(FPRD-\d+)\]\[(F\d+)\]",title)
 if m: return ("FORGE_"+m.group(2),m.group(1))
 m=re.search(r"\[(LPRD-\d+)\]\[(L\d+)\]",title)
 if m: return ("LIFE_"+m.group(2),m.group(1))
 return (None,None)

def is_ready(issue):
 if issue["state"]["type"] not in {"backlog","started"}: return False
 if any(m in issue["title"] for m in SKIP_MARKERS): return False
 pole,prd=classify(issue)
 if not pole: return False
 ctx=context(issue["identifier"])
 for bid in blocker_ids(ctx):
  if status_of(bid)!="completed": return False
 return True

def all_sessions():
 return http_json("/sessions").get("sessions",[])

def active_sessions():
 return [s for s in all_sessions() if s.get("state") not in TERMINAL]

def _session_age_s(s):
 raw=s.get("updateTime") or s.get("createTime")
 if not raw: return 10**12
 try:
  import datetime as _dt
  t=_dt.datetime.fromisoformat(str(raw).replace("Z","+00:00"))
  return max(0.0, (_dt.datetime.now(_dt.timezone.utc)-t).total_seconds())
 except Exception:
  return 10**12

def duplicate(active, issue_id, work_id=None):
 for s in active:
  blob = s.get("title","") + " " + s.get("prompt","")
  if issue_id in blob: return True
  if work_id and f"Work_id: {work_id}" in blob: return True
 return False

def core_for(pole):
 if pole.startswith("KERNEL_") or pole.startswith("K"): return "KERNEL"
 if pole.startswith("LIFE_"): return "LIFE"
 if pole.startswith("FORGE_"): return "BUSINESS"
 return "BUSINESS"

COMPANION_BY_CORE_ROLE={
 "KERNEL":{"SPEC":"YAZ","BUILD":"RYAN","SPAWN":"GRAHAM"},
 "LIFE":{"SPEC":"AMY","BUILD":"RORY","SPAWN":"RIVER"},
 "BUSINESS":{"SPEC":"CLARA","BUILD":"NARDOLE","SPAWN":"BILL"},
}
ROLE_HINTS={
 "SPEC":("spec","prd","adr","policy","contract","design","schema"),
 "BUILD":("implement","build","runtime","adapter","api","ui","fix","test","integration"),
 "SPAWN":("spawn","replicate","benchmark","evidence","dataset","artifact","registry","observability"),
}

def role_for(issue,pole):
 title=(issue.get("title") or "").lower()
 desc=(issue.get("description") or "").lower()
 blob=title+" "+desc
 scores={r:sum(1 for k in ks if k in blob) for r,ks in ROLE_HINTS.items()}
 best=max(scores,key=scores.get)
 return best if scores[best] else "BUILD"

def companion_for(issue,pole):
 core=core_for(pole)
 return COMPANION_BY_CORE_ROLE[core][role_for(issue,pole)]

def active_core_counts(active):
 out={"KERNEL":0,"LIFE":0,"BUSINESS":0}
 for s in active:
  title=s.get("title","")
  if "ASPACE:KERNEL" in title or "| KPRD-" in title: out["KERNEL"]+=1
  elif "ASPACE:LIFE" in title or "| LPRD-" in title: out["LIFE"]+=1
  elif "ASPACE:BUSINESS" in title or "ASPACE:FORGE" in title or "| FPRD-" in title: out["BUSINESS"]+=1
 return out

def active_companion_session(active,companion):
 needle=f"| {companion} |"
 for s in active:
  if needle in (s.get("title") or ""):
   return s
 return None

def reusable_session(issue_id):
    # Jules API exposes no session-retask/update primitive. A finished session
    # cannot be recycled for a different task; jules_send_message applies only
    # to an active session. Therefore never pretend a terminal session is reusable.
    return None

def write_prd(issue,pole,prd):
 folder=PRD_ROOT/pole
 folder.mkdir(parents=True,exist_ok=True)
 path=folder/f"{prd}_{issue['identifier']}.md"
 text=f"""# {prd} — {issue['identifier']} — {issue['title']}

Pole: {pole}
Linear: {issue['identifier']}
Source: {SOURCE}
State at dispatch: {issue['state']['name']}

## Mandate
{issue.get('description') or 'No description.'}

## Execution contract
- Work only inside the bounded mandate.
- Preserve Kernel/WorkGraph authority boundaries.
- Run focused tests/build/audit relevant to changed files.
- Do not use destructive git cleanup/reset.
- Create a PR with evidence when complete.
- Do not mutate unrelated domains.
"""
 path.write_text(text,encoding="utf-8")
 return path

def comment(issue_id,text):
 p=subprocess.run(["orca","linear","comment","add",issue_id,"--body-file","-","--json"],
                  input=text,text=True,capture_output=True,encoding="utf-8")
 if p.returncode: raise RuntimeError(p.stderr or p.stdout)

def set_progress(issue_id, work_id, session_id, observation):
 require_running_owner(work_id, session_id, observation)
 run("orca","linear","status","set",issue_id,"--to","In Progress","--json")

def _doctor_for_core(core):
 return {"KERNEL":"DOCTOR13","LIFE":"DOCTOR11","BUSINESS":"DOCTOR12"}[core]

def _send_to_session(session_id,prompt):
 return http_json(f"/sessions/{session_id}/messages","POST",{"prompt":prompt},30)

def create_or_continue_session(issue,pole,prd,active,work_id=None):
 brief=write_prd(issue,pole,prd)
 core=core_for(pole)
 role=role_for(issue,pole)
 companion=companion_for(issue,pole)
 doctor=_doctor_for_core(core)
 prompt=f"""A'Space E-Myth execution lane.
Core: {core}. Manager: {doctor}. Companion owner: {companion}. Role: {role}.
Execute {prd} for {issue['identifier']}: {issue['title']}.
Read the PRD brief at {brief.relative_to(ROOT).as_posix()}.
Linear mandate:
{issue.get('description') or ''}
{f'Work_id: {work_id}' if work_id else ''}
Rules:
- Stay inside this Companion role and Core.
- If requirements are materially ambiguous or need human interaction, STOP implementation and propose an ADR clarification for the Doctor/Rick review path.
- Preserve Kernel/WorkGraph authority boundaries.
- Run focused tests/build/audit relevant to changed files.
- Do not use destructive git cleanup/reset.
- Create/continue a PR with durable evidence.
"""
 lane=active_companion_session(active,companion)
 if lane:
  raise ValueError("Companion lane is occupied; never retask an unrelated live session")
 title=f"ASPACE:{core} | {companion} | {role}"
 body={"prompt":prompt,"source":SOURCE,"startingBranch":"main",
       "title":title,"automationMode":"AUTO_CREATE_PR","requirePlanApproval":False}
 created=http_json("/sessions","POST",body,30)
 created["continued"]=False
 return created

def tick():
 with dispatch_lock():
  return _tick()


def _tick():
 if not ensure_proxy():
  raise RuntimeError("Jules proxy unavailable after bounded recovery")
 issues=list_issues()
 active=active_sessions()
 capacity=max(0,MAX_ACTIVE-len(active))
 ready=sorted((x for x in issues if is_ready(x)),
              key=lambda x:(x.get("priority",4),x.get("createdAt","")))
 launched=[]
 skipped=[]
 counts=active_core_counts(active)
 for issue in ready:
  if len(launched)>=MAX_DISPATCH_PER_TICK: break
  iid=issue["identifier"]
  try:
   work_id=resolve_work(iid)
  except ValueError as exc:
   skipped.append({"issue":iid,"reason":str(exc)})
   continue
  if duplicate(active,iid,work_id): continue
  pole,prd=classify(issue)
  core=core_for(pole)
  companion=companion_for(issue,pole)
  existing_lane=active_companion_session(active,companion)
  if not existing_lane and (not capacity or counts.get(core,0) >= CORE_LIMITS[core]):
   continue
  if existing_lane:
   skipped.append({"issue":iid,"reason":"Companion lane occupied"})
   continue
  try:
   work_id=reserve(iid)
  except ValueError as exc:
   skipped.append({"issue":iid,"reason":str(exc)})
   continue
  # The durable attempt and atomic claim precede any external mutation.
  # Network ambiguity deliberately keeps ownership for supervisor reconciliation.
  session=create_or_continue_session(issue,pole,prd,active,work_id)
  sid=str(session.get("id") or session.get("sessionId") or session.get("name") or "").removeprefix("sessions/")
  bind_session(work_id,sid)
  observation=http_json(f"/sessions/{sid}")
  projected=False
  try:
   set_progress(iid,work_id,sid,observation)
   projected=True
  except ValueError as exc:
   skipped.append({"issue":iid,"work_id":work_id,"reason":str(exc)})
  companion=companion_for(issue,pole)
  role=role_for(issue,pole)
  continued=bool(session.get("continued"))
  action="continued" if continued else "created"
  comment(iid,f"Jules lane {action}: {prd} / {pole} / {companion} / {role}\nSession: {sid}\nWorkGraph work_id: {work_id}\nExecuting: {projected}\nSource: {SOURCE}\nDispatcher: kernel_fleet_tick.py")
  launched.append({"issue":iid,"prd":prd,"pole":pole,"core":core,"companion":companion,"role":role,"session":sid,"continued":continued,"work_id":work_id,"projected_in_progress":projected})
  if not continued:
   active.append({"title":f"ASPACE:{core} | {companion} | {role}","prompt":iid,"state":"ACTIVE","id":sid})
   counts[core]=counts.get(core,0)+1
   capacity-=1
 report={"ok":True,"active":len(active),"launched":launched,"skipped":skipped,
         "core_limits":CORE_LIMITS,"core_active":counts,
         "ready":[x["identifier"] for x in ready],"capacity_after":capacity,
         "sessions":[{"id":s.get("id"),"title":s.get("title"),
                      "state":s.get("state"),"url":s.get("url"),
                      "updateTime":s.get("updateTime")} for s in active]}
 out=ROOT/"10_Tech_OS"/"reports"/"jules_kernel_fleet.json"
 out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
 print(json.dumps(report,ensure_ascii=False,indent=2))
 return 0

if __name__=="__main__":
 try: raise SystemExit(tick())
 except Exception as e:
  print(json.dumps({"ok":False,"error":str(e)},ensure_ascii=False),file=sys.stderr)
  raise
