---
adr: ADR-MCP-001
title: God Mode CLI Stack — Bash-invoked CLIs replace MCP modal fatigue
date: 2026-05-17
status: ACCEPTED
deciders: A0 Amadeus, Claude Code (Opus 4.7), Codex (Shadow L0)
related:
  - ADR-RICK-002 (Paperclip deprecation → Hermes promotion → retrogradation)
  - SDD-009 (Shadow L2 Business OS)
  - 00_Amadeus/30_MEMORY_CORE/Shadow_L2/02_god-mode-cli-stack-20260516.md
  - 00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/concepts/concept_god_mode_cli_stack.md
tags: [#MCP #CLI #Shadow_L2 #Bypass_Permissions #Printing_Press #Karpathy]
---

# ADR-MCP-001 — God Mode CLI Stack

## Context

Until 2026-05-17 the agent surface for external services (Notion, Airtable, ClickUp, Vercel, Supabase, Apollo, Hostinger, Google Workspace) was provided by **MCP Desktop connectors** registered through the Claude Desktop UI. Each tool call triggered a permission modal, fragmenting agentic workflows and capping execution speed for any non-trivial task. A0 named this **"modal fatigue"** and demanded a different surface.

Three reference patterns informed the decision:

1. **Notion `ntn` CLI** — the first major SaaS vendor to ship an official CLI (OAuth-keychain-stored, Windows-unsupported as of 2026-05).
2. **Karpathy AutoResearch** (cf. [[source_karpathy-autoresearch]]) — proof that **autonomous research loops** require a **bounded-cost, friction-free executor surface**.
3. **Printing Press v4.8.0** (`mvanhorn/cli-printing-press`) — auto-generation of Cobra CLIs + MCP servers from any OpenAPI spec or docs URL, with agent-native flags (`--agent`, `--compact`, typed exit codes, SQLite cache).

## Decision

A'Space adopts a **three-layer agent surface trinity** :

| Layer | Acteur | Rôle | Permission model |
|---|---|---|---|
| **MCP Desktop UUID** | A0 humain | Bac à sable manuel — expérimentation interactive | Modales acceptées |
| **CLI via Bash** | Shadow L0 Executor Mesh (Codex, Claude Code, Gemini) | Canal souverain agentique | `bypassPermissions` + wildcards explicites |
| **`.claude.json` mcpServers** | — | Fallback dormant si CLIs cassent | Pas d'auth en clair |

**Priority rule** : `CLI officiel > Printing Press generated > MCP fallback`.

## Implementation State (2026-05-17)

| Service | CLI | Status |
|---|---|---|
| Vercel | `vercel` 54.1.0 (npm) | ✅ Installed |
| Google Workspace (Gmail/Drive/Calendar/Sheets/Docs/Chat/Admin) | `gws` 0.22.5 (npm) | ✅ Installed |
| Supabase | `supabase` 2.98.2 (GitHub binary) | ✅ Installed |
| Printing Press | `printing-press` 4.8.0 (GitHub binary Windows AMD64) | ✅ Installed |
| ClickUp | `clickup-pp-cli` 1.0.0 (Printing Press from OpenAPI YAML) | ✅ Generated + compiled (19.8 MB) |
| GitHub | `gh` 2.83.2 | ✅ Existed |
| Context7 | `ctx7` | ✅ Existed |
| Notion | `notion-pp-cli` (official release `notion-current`) | ✅ Downloaded (13.6 MB, full REST coverage) |
| Airtable | `airtable-pp-cli` | 🟡 Phase 5 pending |
| Apollo | `apollo-pp-cli` | 🟡 Phase 5 pending |
| Hostinger | `hostinger-pp-cli` | 🟡 Phase 5 pending (Postman collection alt) |

Bypass wildcards added to `C:\Users\amado\.claude\settings.json` :
```
Bash(vercel:*), Bash(supabase:*), Bash(gws:*), Bash(printing-press:*),
Bash(ntn:*), Bash(ctx7:*), Bash(gh:*), Bash(*-pp-cli:*), Bash(*-pp-mcp:*)
```

## Consequences

### Positive

- **Zero modal fatigue** for agentic workflows — agents now operate at terminal speed.
- **Versionable** : CLI binaries + .claude.json are git-trackable; Desktop connectors are not.
- **Auditable** : every CLI call leaves a Bash transcript in session log.
- **Reversible** : remove a wildcard from settings.json or uninstall a CLI; nothing exotic.
- **Composable** : CLIs pipe (`vercel ls --json | jq`) ; MCP cannot.
- **Karpathy-aligned** : matches AutoResearch's "frozen reference + agent-mutable surface + bounded cost" pattern at the OS layer (cf. [[concept_autonomous_research_loop]]).

### Negative / Risks

- **Quota self-reference** : Printing Press generation with `--docs` (no direct OpenAPI) invokes `claude` CLI internally → consumes the same Anthropic/MiniMax quota the orchestrating agent is using. Mitigation : delegate batch generations to Codex (`shadow_l0_exec`) which has its own quota.
- **Maintenance** : 12+ CLIs to keep updated. Mitigation : `winget upgrade --all` + npm/scoop scheduled refresh.
- **Auth duplication** : Desktop connector OAuth and CLI OAuth/PAT are separate stores. Mitigation : document each service's auth path in `Shadow_L2/`.
- **`.claude.json` mcpServers dormant** can drift. Mitigation : annual review or remove when CLI proven stable.

### Out of Scope (not decided here)

- Replacement of Hermes runtime (covered by ADR retrogradation, see LLM_Wiki log 2026-05-17).
- Tier-2 CLIs (Discord, Telegram, Twilio, Stripe) — addressed when L2 sectors require them.

## Validation Criteria

1. ✅ A bypass-allowed Bash invocation of `vercel --version`, `gws --version`, `supabase --version`, `printing-press --version` succeeds without modal.
2. ✅ At least one Printing Press generated CLI produces a working binary (ClickUp validated).
3. ⏳ Phase 5 batch of remaining 4 CLIs completed by Codex or Claude Code.
4. ⏳ `ANTHROPIC_API_KEY` exposed in `settings.json` rotated and moved to env var (separate Rick task).

## References

- Karpathy AutoResearch : https://github.com/karpathy/autoresearch
- Karpathy LLM Wiki gist : https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Printing Press : https://github.com/mvanhorn/cli-printing-press (v4.8.0)
- Notion CLI `ntn` : https://developers.notion.com/cli/get-started/overview
- Google Workspace CLI : https://github.com/googleworkspace/cli (v0.22.5)
- Shadow L2 working doc : `30_MEMORY_CORE/Shadow_L2/02_god-mode-cli-stack-20260516.md`

## Inbounds

- ADR-RICK-002 (Hermes/Paperclip predecessor decisions)
- LLM_Wiki/wiki/log.md (2026-05-17 entry)
- LLM_Wiki/wiki/concepts/concept_god_mode_cli_stack.md
