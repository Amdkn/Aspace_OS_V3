---
name: github-cli-orchestration
description: Orchestrate GitHub operations via the `gh` CLI (v2.83+). Use this skill when the user says "open a PR", "create a release", "list my repos", "check CI status", "merge this branch", or any GitHub API operation from a local checkout. Triggers on "gh", "github", "PR", "pull request", "release", "issue", "workflow run", "actions". NO MCP — `gh` is the only GitHub integration (the official `@modelcontextprotocol/server-github` is deprecated). `gh auth status` MUST pass before any operation. Token comes from `GH_TOKEN` or `GITHUB_TOKEN` env var (User scope), set via Test Key Pragma.
---

# /github-cli-orchestration — GitHub ops via `gh` CLI

## Why CLI not MCP
- `@modelcontextprotocol/server-github` was **DEPRECATED** on npm (last published 2025-04-08, marked unsupported).
- The replacement `github-mcp-server@1.8.7` is third-party (jungchihoon) and exposes 40+ tools — over the 100-tool IDE limit when combined with the rest of the .mcp.json.
- `gh` CLI is the official GitHub tool (v2.83.2 installed, GitHub-maintained) and is sufficient for 95% of operations.
- For the 5% that need raw GraphQL/REST, use `gh api` (wraps `gh auth token` automatically).

## Preconditions (verify first, fail loud if missing)

| Check | Command | Pass criterion |
|---|---|---|
| `gh` installed | `gh --version` | `2.83.x` or newer |
| Auth OK | `gh auth status` | `Logged in to github.com as <user> (oauth_token)` |
| Working dir is a git repo | `git -C <dir> rev-parse --is-inside-work-tree` | `true` |
| `origin` is a GitHub URL | `git -C <dir> remote get-url origin` | starts with `https://github.com/` or `git@github.com:` |
| Default branch known | `gh repo view --json defaultBranchRef --jq .defaultBranchRef.name` | returns `main` / `master` / etc. |

> **Why these matter**: `gh` uses the `origin` remote to know which repo the operation targets. If `origin` is wrong (e.g. still pointing at a fork after a rename), `gh pr create` will open a PR on the WRONG repo.

## Common operations (one-liners, copy-paste)

### Repo discovery

```bash
gh repo list <org> --limit 50 --json name,isPrivate,updatedAt
gh repo view <org>/<repo> --json name,description,url,defaultBranchRef
gh api graphql -F query='{ repository(owner:"<org>",name:"<repo>"){ stargazerCount pushedAt } }'
```

### Pull Requests

```bash
# List open PRs in current repo
gh pr list --state open --json number,title,author,headRefName,baseRefName,url

# Create a PR (from current branch → default branch)
gh pr create --title "feat: <desc>" --body "<body>" --base main --head <branch>

# View a PR (with checks + reviews)
gh pr view <number> --json title,body,state,statusCheckRollup,reviews,comments

# Merge a PR (squash by default; --admin bypasses branch protection in emergencies)
gh pr merge <number> --squash --delete-branch

# Check CI status for a PR
gh pr checks <number>
```

### Issues

```bash
# List open issues
gh issue list --state open --label <label> --json number,title,author,labels,updatedAt

# Create an issue
gh issue create --title "Bug: <desc>" --body "<body>" --label "bug,priority-high"

# Close an issue
gh issue close <number> --comment "Fixed in <PR-or-commit>"
```

### Releases

```bash
# Create a release with auto-generated notes
gh release create v1.2.3 --generate-notes --title "v1.2.3"

# Upload a binary to a release
gh release upload v1.2.3 ./dist/binary.zip

# List recent releases
gh release list --limit 10
```

### Workflows (GitHub Actions)

```bash
# Trigger a workflow run
gh workflow run deploy.yml -f environment=production

# List recent runs for a workflow
gh run list --workflow deploy.yml --limit 10

# Watch a run live
gh run watch <run-id>

# Download artifacts from a run
gh run download <run-id> --dir ./artifacts
```

### Raw API (GraphQL + REST)

```bash
# REST: get a specific file's contents
gh api repos/<org>/<repo>/contents/<path> --jq '.content' | base64 -d

# GraphQL: complex query (e.g. issue dependency graph)
gh api graphql -F query='{ repository(owner:"X",name:"Y"){ ... } }'
```

## Auth & token rotation

- `gh auth login` interactive — DO NOT run this for A0. Use Test Key Pragma.
- `GH_TOKEN` env var (User scope) takes precedence over `gh auth login`'s keyring. To rotate:
  1. A0 generates a new fine-grained PAT on https://github.com/settings/tokens?type=beta
  2. A0 pastes it in chat with "github token test"
  3. Agent runs: `[Environment]::SetEnvironmentVariable("GH_TOKEN", "<new>", "User")`
  4. Verify: `gh auth status` → expect `Logged in to github.com as <user> (GH_TOKEN)`
  5. A0 revokes the old token on GitHub.

## Gotchas (D6 root causes already paid for)

| Symptom | Root cause | Fix |
|---|---|---|
| `gh pr create` opens in wrong repo | `origin` points to a fork/old URL | `git remote set-url origin https://github.com/<correct-org>/<repo>.git` |
| `gh api` returns 403 with fine-grained PAT | PAT missing the `Contents: Read` scope for the endpoint | Re-create PAT with correct scope, OR use the user's OAuth token (default `gh auth login`) |
| `gh workflow run` no-op silently | Workflow file has no `workflow_dispatch` trigger | Add `on: workflow_dispatch:` to the YAML |
| `gh run watch` hangs forever | Run is queued, not started | Add `--exit-status` and `--interval 30` to make it bounded |
| Token expires mid-session (PAT 30/60/90 day) | No warning in `gh auth status` for PATs | Add a calendar reminder; rotate proactively |

## What this skill does NOT do

- ❌ Create a new GitHub org (UI-only on github.com)
- ❌ Manage GitHub Apps (use the `gh app` subcommand, or the web UI)
- ❌ Bulk edit issue labels (use `gh issue edit --add-label` in a bash loop, but be careful with rate limits)
- ❌ Operate on GitHub Enterprise self-hosted (different auth flow — ask A0)

## Related

- Skill `vercel-deploy-from-github` — uses `gh` to read repo metadata before Vercel deploy
- ADR-META-001 D5 — every `gh` call should be followed by a verification (HTTP code, exit code, response shape)
