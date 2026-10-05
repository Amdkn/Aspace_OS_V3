#!/usr/bin/env python3
"""Idempotent bootstrap of A'Space Gateway into native GitHub primitives.

This script is intentionally repository-scoped. It uses GITHUB_TOKEN for
repository-native primitives and reports project/wiki permission gaps instead
of fabricating success.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.github.com"
GRAPHQL = "https://api.github.com/graphql"
REPO = os.environ["GITHUB_REPOSITORY"]
OWNER = os.environ["GITHUB_REPOSITORY_OWNER"]
TOKEN = os.environ["GITHUB_TOKEN"]
PROJECTS_TOKEN = os.environ.get("ASPACE_PROJECTS_TOKEN") or None
REPO_NAME = REPO.split("/", 1)[1]

GATEWAY_ISSUES = [542, 543, 544, 545, 546, 547]
MILESTONE_TITLE = "V4 — A'Space Gateway / Native Control Plane v0"
DISCUSSION_TITLE = "[RFC][GATEWAY] A'Space Gateway — Native GitHub Control Plane & Federation"


class ApiError(RuntimeError):
    pass


def api(method: str, path: str, payload: dict | None = None):
    url = path if path.startswith("http") else f"{API}/{path.lstrip('/')}"
    data = None if payload is None else json.dumps(payload).encode()
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "aspace-native-github-control-plane",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            raw = response.read()
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        raise ApiError(f"{method} {url} -> {exc.code}: {body}") from exc


def graphql(query: str, variables: dict, token: str | None = None):
    data = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(
        GRAPHQL,
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {token or TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "aspace-native-github-control-plane",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read())
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        raise ApiError(f"POST {GRAPHQL} -> {exc.code}: {body}") from exc

    errors = (result or {}).get("errors")
    if errors:
        raise ApiError(f"GraphQL errors: {json.dumps(errors, ensure_ascii=False)}")
    return result["data"]


def ensure_milestone() -> int:
    milestones = api("GET", f"repos/{REPO}/milestones?state=all&per_page=100")
    existing = next((m for m in milestones if m["title"] == MILESTONE_TITLE), None)
    if existing:
        number = existing["number"]
    else:
        created = api(
            "POST",
            f"repos/{REPO}/milestones",
            {
                "title": MILESTONE_TITLE,
                "description": (
                    "Bounded convergence for A'Space Gateway v0: protocol, "
                    "identity/presence/session, GitHub control-plane bridge, "
                    "runtime/surface federation and sovereign canary."
                ),
            },
        )
        number = created["number"]

    for issue in GATEWAY_ISSUES:
        api("PATCH", f"repos/{REPO}/issues/{issue}", {"milestone": number})
    return number


def ensure_discussion() -> str:
    q = """
    query($owner:String!,$name:String!){
      repository(owner:$owner,name:$name){
        id
        discussionCategories(first:50){nodes{id name}}
        discussions(first:100,orderBy:{field:UPDATED_AT,direction:DESC}){
          nodes{title url}
        }
      }
    }
    """
    repo = graphql(q, {"owner": OWNER, "name": REPO_NAME})["repository"]
    existing = next((d for d in repo["discussions"]["nodes"] if d["title"] == DISCUSSION_TITLE), None)
    if existing:
        return existing["url"]

    categories = repo["discussionCategories"]["nodes"]
    category = next((c for c in categories if c["name"] == "Ideas"), None)
    category = category or next((c for c in categories if c["name"] == "General"), None)
    if not category:
        raise ApiError("No Ideas or General discussion category is available")

    body = """# A'Space Gateway RFC

Mission: #542

Use this Discussion for alternatives, protocol questions, external patterns,
serendipity and architectural debate that are **not yet executable cells**.

## Fixed boundary

Gateway = connectivity + protocol + presence + session + delivery + federation.

Gateway is not:
- the institutional brain;
- the Capability Fabric;
- HostPolicy;
- WorkGraph;
- Temporal Truth;
- AMF;
- the Reflex Fabric.

Promote an idea from this Discussion to an Issue only when it has a concrete
effect, owner, acceptance criterion and return_to.

Executable mission: #542
Protocol/identity: #543
GitHub control plane: #544
Runtime/surfaces: #545
Sovereign canary: #546
"""

    m = """
    mutation($repositoryId:ID!,$categoryId:ID!,$title:String!,$body:String!){
      createDiscussion(input:{
        repositoryId:$repositoryId,
        categoryId:$categoryId,
        title:$title,
        body:$body
      }){discussion{url}}
    }
    """
    created = graphql(
        m,
        {
            "repositoryId": repo["id"],
            "categoryId": category["id"],
            "title": DISCUSSION_TITLE,
            "body": body,
        },
    )
    return created["createDiscussion"]["discussion"]["url"]


def project_snapshot(project_number: int):
    q = """
    query($login:String!,$number:Int!){
      user(login:$login){
        projectV2(number:$number){
          id
          title
          items(first:100){
            nodes{
              content{
                ... on Issue{
                  number
                  repository{nameWithOwner}
                }
              }
            }
          }
        }
      }
    }
    """
    data = graphql(
        q,
        {"login": OWNER, "number": project_number},
        token=PROJECTS_TOKEN,
    )
    project = data["user"]["projectV2"]
    if not project:
        raise ApiError(f"Project V2 #{project_number} not found or inaccessible")
    existing = {
        node["content"]["number"]
        for node in project["items"]["nodes"]
        if node.get("content")
        and node["content"].get("repository", {}).get("nameWithOwner") == REPO
        and "number" in node["content"]
    }
    return project["id"], project["title"], existing


def issue_node_id(number: int) -> str:
    q = """
    query($owner:String!,$name:String!,$number:Int!){
      repository(owner:$owner,name:$name){
        issue(number:$number){id}
      }
    }
    """
    return graphql(
        q,
        {"owner": OWNER, "name": REPO_NAME, "number": number},
        token=PROJECTS_TOKEN,
    )["repository"]["issue"]["id"]


def add_project_item(project_id: str, issue_id: str):
    m = """
    mutation($projectId:ID!,$contentId:ID!){
      addProjectV2ItemById(input:{projectId:$projectId,contentId:$contentId}){
        item{id}
      }
    }
    """
    graphql(
        m,
        {"projectId": project_id, "contentId": issue_id},
        token=PROJECTS_TOKEN,
    )


def ensure_projects() -> str:
    """Project Gateway issues into every currently accessible A'Space portfolio.

    Project numbers changed during earlier Project-V2 restructuring, so this
    routine treats historical numbers as candidates instead of canon.
    """
    if not PROJECTS_TOKEN:
        return (
            "external-user-scope: Projects #12 and #9 are already projected "
            "via authenticated gh/DC. Repository GITHUB_TOKEN cannot access "
            "user-level Projects V2. Configure ASPACE_PROJECTS_TOKEN or a "
            "GitHub App installation token for fully native Actions updates."
        )

    results = []
    errors = []

    # #12 = latest known Universal Constructor/Fractal Project from the
    # durable Project bootstrap. #9/#8 are older Foundation/UC references
    # retained only as compatibility candidates.
    plan = {
        12: GATEWAY_ISSUES,
        9: GATEWAY_ISSUES,
        8: [542],
    }

    for project_number, issues in plan.items():
        try:
            project_id, title, existing = project_snapshot(project_number)
        except Exception as exc:
            errors.append(f"#{project_number}: {exc}")
            continue

        added = 0
        for issue in issues:
            if issue in existing:
                continue
            add_project_item(project_id, issue_node_id(issue))
            added += 1
        results.append(f"#{project_number} {title}: +{added}")

    if results:
        suffix = "" if not errors else " | unavailable: " + " ; ".join(errors)
        return "ready (" + "; ".join(results) + ")" + suffix

    raise ApiError("No candidate A'Space Project V2 was accessible: " + " ; ".join(errors))


def run_git(args: list[str], cwd: str | None = None):
    proc = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if proc.returncode:
        raise RuntimeError(
            f"git command failed ({' '.join(args)}):\n{proc.stderr[-2000:]}"
        )
    return proc.stdout


def sync_wiki() -> str:
    source = Path("docs/wiki")
    if not source.exists():
        raise RuntimeError("docs/wiki mirror is missing")

    with tempfile.TemporaryDirectory(prefix="aspace-wiki-") as td:
        wiki_url = f"https://x-access-token:{TOKEN}@github.com/{REPO}.wiki.git"
        clone = subprocess.run(
            ["git", "clone", wiki_url, td],
            text=True,
            capture_output=True,
        )
        if clone.returncode:
            shutil.rmtree(td, ignore_errors=True)
            os.makedirs(td, exist_ok=True)
            run_git(["git", "init"], cwd=td)
            run_git(["git", "branch", "-M", "master"], cwd=td)
            run_git(["git", "remote", "add", "origin", wiki_url], cwd=td)

        for src in source.glob("*.md"):
            shutil.copy2(src, Path(td) / src.name)

        run_git(["git", "config", "user.name", "A'Space GitHub Native Control Plane"], cwd=td)
        run_git(["git", "config", "user.email", "actions@users.noreply.github.com"], cwd=td)
        run_git(["git", "add", "*.md"], cwd=td)

        status = run_git(["git", "status", "--porcelain"], cwd=td).strip()
        if not status:
            return "ready-no-change"

        run_git(["git", "commit", "-m", "docs: sync A'Space Gateway native Wiki"], cwd=td)
        run_git(["git", "push", "origin", "HEAD:master"], cwd=td)
        return "ready"


def comment_receipt(
    milestone_number: int,
    discussion_url: str,
    project_status: str,
    wiki_status: str,
):
    body = f"""## Native GitHub bootstrap receipt

- Milestone: #{milestone_number} — ready
- Discussion: {discussion_url} — ready
- Project V2 projection: {project_status}
- Wiki sync: {wiki_status}
- Mission: #542
- Cells: #543 #544 #545 #546
- Bootstrap: #547

The bootstrap reports permission gaps explicitly; it does not convert them
into fake PASS.
"""
    api("POST", f"repos/{REPO}/issues/547/comments", {"body": body})


def main() -> int:
    milestone = ensure_milestone()
    discussion = ensure_discussion()

    try:
        project_status = ensure_projects()
    except Exception as exc:
        project_status = f"permission-gap: {exc}"

    try:
        wiki_status = sync_wiki()
    except Exception as exc:
        wiki_status = f"permission-gap: {exc}"

    comment_receipt(milestone, discussion, project_status, wiki_status)

    summary = {
        "milestone": milestone,
        "discussion": discussion,
        "project": project_status,
        "wiki": wiki_status,
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))

    # Milestone + Discussion are repository-native required surfaces.
    # Project/Wiki may require token permissions outside GITHUB_TOKEN;
    # those gaps are evidence for the GitHub App / Gateway design.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
