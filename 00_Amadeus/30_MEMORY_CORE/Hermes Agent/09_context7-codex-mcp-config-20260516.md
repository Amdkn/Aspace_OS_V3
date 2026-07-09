---
source: Codex / Shadow L0
date: 2026-05-16
type: mcp-configuration
domain: L0_Tech_OS / Hermes_Agent
tags: [#Codex #Context7 #MCP #DocsDogmatique #ShadowL0]
status: active
---

# Context7 MCP for Codex — 2026-05-16

## Intent

Configure Context7 as a Codex MCP server so Codex can apply the A'Space Docs Dogmatique from Shadow L0:

1. Resolve the official library/project ID.
2. Query current official docs before touching living systems.
3. Treat Context7-backed docs and upstream repos as proof.
4. Mark any fallback to web/vendor/local source explicitly.

This is for Codex itself, not a Hermes runtime hook.

## Codex Configuration

Config file:

```text
C:\Users\amado\.codex\config.toml
```

Installed block:

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
startup_timeout_sec = 40
```

The server was added with:

```powershell
codex mcp add context7 -- npx -y @upstash/context7-mcp
```

Then `startup_timeout_sec = 40` was added manually, following Context7's troubleshooting guidance for slow `npx` startup.

## Verification

Commands run:

```powershell
codex mcp list
codex mcp get context7
npx -y @upstash/context7-mcp --help
```

Observed state:

```text
Name: context7
transport: stdio
command: npx
args: -y @upstash/context7-mcp
status: enabled
auth: unsupported
```

`npx -y @upstash/context7-mcp --help` confirms support for:

```text
--transport <stdio|http>
--port <number>
--api-key <key>
```

## API Key Policy

No Context7 API key was written into Codex config.

Current mode:

```text
Basic unauthenticated Context7 MCP usage via local stdio server.
```

If higher rate limits or private-index access are needed, prefer an environment-variable based setup:

```powershell
setx CONTEXT7_API_KEY "<secret>"
```

Then update the MCP command only if required by Context7 docs. Do not paste the key into chat or docs.

## Operational Rule for Codex

When the task touches Hermes Agent, providers, MCP, hooks, WSL networking, or modern dependencies:

1. Use Context7 first when available.
2. If Context7 is unavailable, use official vendor docs or local upstream source.
3. Cite the source used.
4. For durable changes, document file changed, validation command, residual risk, and secret-handling note.

## Sources

- Context7 official MCP clients docs: `https://context7.com/docs/resources/all-clients`
- Context7 official installation docs: `https://context7.com/docs/installation`
- Local Codex CLI: `codex mcp --help`
- Local Context7 MCP CLI: `npx -y @upstash/context7-mcp --help`

---

*Documenté Docs Dogmatique — Context7 MCP pour Codex Shadow L0 — 2026-05-16 — Codex*
