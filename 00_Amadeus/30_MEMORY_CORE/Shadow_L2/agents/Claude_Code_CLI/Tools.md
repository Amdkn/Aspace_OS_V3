---
source: Shadow_L2
date: 2026-05-19
type: agent-tools
agent: Claude_Code_CLI
layer: L2
tags: [#Tools, #ClaudeCode, #L2, #BusinessPulse]
---

# Tools.md — Surface capability Claude Code L2

## CLI tools

- `Read`, `Write`, `Edit`, `Glob`, `Grep`, `Bash` (Trust Zone only)
- `WebFetch` (on-demand vendor docs)

## MCP servers L2 (full surface)

| Server | Usage L2 |
|---|---|
| `vercel` | list_deployments, get_deployment_build_logs, get_runtime_logs |
| `supabase` | get_logs, get_advisors, list_projects, execute_sql (read-only mode) |
| `hostinger-api` | VPS_*, DNS_get*, billing_*, domains_get* |
| `airtable` (MCP A'Space) | list_records, search_records, list_bases |
| `clickup` | clickup_filter_tasks, get_task, list_lists, list_views |
| `notion` | notion-search, notion-fetch |
| `context7` | Doc vendor (vercel, supabase, etc.) à la demande |
| `mcp-registry` | suggest_connectors si nouveau besoin |
| `apollo` (MCP) | apollo_mixed_companies_search (lead research) |
| `gmail` MCP | search_threads (only read for L2 inbox monitoring) |

## Skills L2

- `/airtable-enrich` (propose ONLY — A0 must validate run)
- `/quality-gate` (read-only audit)
- `/security-scan` (AgentShield)
- `/code-review` (PR review)
- `/checkpoint` (sauvegarder état mission longue)
- `/save-session` / `/resume-session`
- `/skill-creator` (réflexe : si pattern L2 répété, proposer skill)

## Env vars consommées

```
ANTHROPIC_BASE_URL=https://api.minimax.io/anthropic
ANTHROPIC_API_KEY=<MiniMax Token Plan key>
AIRTABLE_BEARER_AUTH=<A'Space Airtable token>
VERCEL_TOKEN=<read-only token preferably>
HOSTINGER_API_TOKEN
CLICKUP_TEAM_ID
ASPACE_ROOT
```

## Forbidden tools L2

- Pas de write MCP (Notion/ClickUp/Airtable PATCH/POST/DELETE) sans signoff
- Pas de `vercel deploy --prod`, `vercel rollback`
- Pas de `hostinger DNS write` sans snapshot préalable (per anti-pattern §12.7)
- Pas de `gh pr merge`
- Pas de `supabase apply_migration`, `execute_sql` mutating

## Inbounds

- `./Heartbeat.md`
- `./Agent.md`
