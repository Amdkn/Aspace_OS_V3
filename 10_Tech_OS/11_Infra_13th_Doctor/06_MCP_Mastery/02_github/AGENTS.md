# 02_github — DOX leaf for GitHub MCP

> Parent: `../AGENTS.md`. Framework: `../../06_MCP_Mastery_dox/AGENTS.md`.
> Canon: vault = `GITHUB_PERSONAL_ACCESS_TOKEN` (Windows env User).

## Purpose

The GitHub MCP drives every `Amdkn/*` repo operation: clone, branch, commit, PR, issue,
release, webhook. It is also the source of truth for repo structure (the `30_Business_OS/
10_Projects/<proj>/apps/<role>` Born-Short pattern lives or dies by what GitHub returns).

## Ownership

- A0 Amadeus — approves any push to a public repo, any release tag, any webhook change.
- A2 Claude Code — orchestrates PRs, branches, releases.
- A3 sub-agent — runs `mcp__github__*` and `gh` CLI calls.

## Local Contracts

### Auth

- Env var: `GITHUB_PERSONAL_ACCESS_TOKEN`.
- Required scopes: `repo`, `read:org`, `admin:repo_hook` (webhooks), `workflow` (if GH Actions used).
- MCP server: on-demand via `npx -y @modelcontextprotocol/server-github`.
- Provider: `github.com` (account `Amdkn`).

### Capabilities (used in A'Space)

| Tool | Use |
|------|-----|
| `mcp__github__create_repository` | New project repo (prefer local push from clone instead) |
| `mcp__github__create_branch` | New branch off `main` |
| `mcp__github__create_pull_request` | Open PR (use `gh pr create` if available — same token) |
| `mcp__github__merge_pull_request` | HITL — see W3 |
| `mcp__github__create_issue` | Bug/feature tracking |
| `mcp__github__add_issue_comment` | Status updates |
| `mcp__github__create_webhook` | Vercel deploy hook (see `04_vercel/`) |
| `mcp__github__search_repositories` | Research before new impl (development-workflow D0) |
| `mcp__github__search_code` | Research before new impl |

## Work Guidance

### W1 — Prefer `gh` CLI over MCP for write ops

`gh` is faster, has richer output, and uses the same token. Use the MCP only for discovery
(search_repositories, search_code) or when `gh` is unavailable.

### W2 — Webhook for Vercel auto-deploy

```
URL: https://api.vercel.com/v1/integrations/deploy/prj_<id>
Events: push (main only)
Content-type: application/json
Secret: stored in vault (generate via `openssl rand -hex 32`)
```

Always test the webhook with a `ping` payload before relying on it for production.

### W3 — Merging requires HITL

`merge_pull_request` ALWAYS needs A0 sign-off, even for a one-commit PR. The reason:
GitHub's merge is irreversible without a revert, and a bad merge on `main` triggers a
production deploy via the webhook.

### W4 — Releases need a tag + a changelog

- Tag format: `v<MAJOR>.<MINOR>.<PATCH>` (semver).
- Changelog: `_RELEASES/v<version>.md` in the repo, with sections: Added / Changed / Fixed / Removed.
- Release commit must reference the changelog path in the body.

### W5 — Search before writing

Per `development-workflow.md` D0, run `mcp__github__search_repositories` AND
`mcp__github__search_code` before any new implementation. Cite the result in the PR body.

## Verification

```bash
# Confirm token works:
gh api user
# Expect: 200, login = "Amdkn"

# Confirm PAT scopes:
gh api -H "Accept: application/vnd.github+json" user/token | jq '.scopes'
# Expect: includes "repo", "read:org", "admin:repo_hook"
```

## Child DOX Index

This leaf has no sub-domains. If repo templates, branch protection rules, or org-level
policies become a separate concern, split here.
