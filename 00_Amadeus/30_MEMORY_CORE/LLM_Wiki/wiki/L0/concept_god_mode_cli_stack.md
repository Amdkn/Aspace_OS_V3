---
source: LLM_Wiki_A0
date: 2026-05-17
type: concept
domain: A0_Sovereign / Agent_Surface / Shadow_L2
tags: [#GodModeCLI #MCP #CLI #BypassPermissions #Printing_Press #Karpathy #Shadow_L2]
---

# Concept — God Mode CLI Stack

## Definition

The **God Mode CLI Stack** is the agent-surface doctrine that replaces permission-modal MCP connectors with **Bash-invoked CLIs** (auto-bypass-allowed) for all programmatic agentic workflows, while keeping Desktop MCP connectors active for **human manual experimentation**.

## Trinity of Layers

```
┌─────────────────────────────────────────────────────┐
│  A0 (humain)                                         │
│   └─ MCP Desktop UUID — UI bac à sable manuel       │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│  Shadow L0 Executor Mesh                             │
│   ├─ Bash → CLIs souverains (priority path)         │
│   │    ├─ Officiels : vercel, supabase, gws, gh,    │
│   │    │              ctx7, ntn                      │
│   │    └─ Printing Press : *-pp-cli                  │
│   └─ Fallback : `.claude.json` mcpServers (dormant) │
└─────────────────────────────────────────────────────┘
```

## Priority Rule

> `CLI officiel > Printing Press generated > MCP fallback dormant`

## Why It Compounds

The God Mode CLI Stack is the **execution-side mirror** of [[concept_compounding_knowledge|the LLM Wiki pattern]] :

| Concept | What compounds | Pattern |
|---|---|---|
| LLM Wiki | Knowledge across queries | Stop re-deriving |
| AutoResearch | Hypotheses across experiments | Stop re-discovering |
| **God Mode CLI** | **Execution context across sessions** | **Stop re-permitting** |

The three together form A'Space's **autonomous operating doctrine**.

## Operational Properties

| Property | MCP Desktop | CLI Bash (God Mode) | `.claude.json` MCP |
|---|---|---|---|
| Modal prompts | ✅ Required | ❌ None (bypass-allowed wildcard) | ⚠️ Depends on Claude Code settings |
| Versionable | ❌ UI only | ✅ Binary + git config | ✅ JSON file |
| Pipeable | ❌ | ✅ `cli a \| cli b` | ❌ |
| Auditable | Partial | ✅ Full Bash transcript | Partial |
| Auth | OAuth in Desktop | PAT/OAuth/keychain per CLI | OAuth via mcp-remote |
| Speed | Modal latency | Native | Variable |

## Mapping to A'Space Hierarchy

| Layer | CLIs |
|---|---|
| L0 Tech OS (Rick) | `gh`, `vercel`, `supabase`, `printing-press`, `go` |
| L1 Life OS (Beth/Morty) | `gws` (Calendar, Drive, Gmail, Docs) |
| L2 Business OS (Jerry/Summer) | `clickup-pp-cli`, `notion-pp-cli`, `airtable-pp-cli`, `apollo-pp-cli`, `hostinger-pp-cli` |

## Bypass Permissions Pattern

`settings.json` `permissions.allow` enriched with explicit wildcards rather than a single blanket `Bash:*` :

```json
"Bash(vercel:*)",
"Bash(supabase:*)",
"Bash(gws:*)",
"Bash(printing-press:*)",
"Bash(*-pp-cli:*)"
```

→ **Audit trail explicite**, pas un blanket. Each new CLI requires one line, which becomes a tracked grant in `settings.json` history.

## Karpathy Connection

Karpathy's **AutoResearch** ([[source_karpathy-autoresearch]]) demands :

1. A frozen reference (here: Canon + ADRs).
2. An agent-mutable surface (here: `train.py`-equivalent — but at OS level, the **CLI commands** the agent issues).
3. A measurable proxy of progress (here: shipped feature / closed work-item).
4. Bounded experiment cost (here: 1 CLI invocation, ~seconds).

The God Mode CLI Stack **is** the agent-mutable surface for the A'Space-scale AutoResearch loop. Without it, the agent burns its iteration budget on permission modals instead of experiments.

## Risk Mitigation

| Risk | Mitigation |
|---|---|
| Wildcard grants too broad | Use service-prefix wildcards (`Bash(vercel:*)`), never blanket `Bash:*` |
| Auth secrets in CLI configs | Each CLI uses keychain / env vars / OAuth tokens, never `.json` cleartext |
| Self-quota burn (PP `--docs` calls `claude`) | Delegate batch gens to Codex via `shadow_l0_exec` |
| CLI drift / breakage | Annual `winget upgrade` + `npm outdated` + smoke test in CI |
| Fallback rot | `.claude.json` mcpServers reviewed every 90 days |

## Réflecteur d'Adoption — Alignement Codex MiniMax (codexm)

Pour maximiser l'efficacité de l'exécution L0 sans quotas restrictifs d'API, le mesh Codex CLI a été aligné de manière isolée et durable avec MiniMax :
1. **Isolation `$env:CODEX_HOME`** : L'alias PowerShell court `codexm` charge automatiquement `$env:CODEX_HOME = 'C:\Users\amado\ASpace_OS_V2\.codex-m3-lean'` dans le profil PowerShell. Cela empêche le chargement de plugins/hooks globaux gourmands en tokens.
2. **Metadata Models** : Ajout du catalogue `.codex-m3-lean/models.json` pour déclarer les spécificités de `MiniMax-M3` (fenêtre de 512K, parallel tool calls), supprimant le warning de fallback du CLI.
3. **Bypass complet et YOLO** : Injection des flags `-s danger-full-access -a never --dangerously-bypass-approvals-and-sandbox` par défaut sur l'alias, supprimant 100% des prompts de micro-approbations pour éviter les erreurs d'interruption sémantique (erreur 2013).

## Cross-Refs

- [[source_karpathy-autoresearch]] — Pattern parent (research loop).
- [[source_llm-wiki-pattern]] — Sibling concept (memory loop).
- [[concept_autonomous_research_loop]] — Pattern abstraction.
- [[entity_shadow_l0_executor_mesh]] — The mesh that uses this surface.
- [[concept_compounding_knowledge]] — Why bypassing modals compounds.
- ADR-MCP-001 (canonical decision) — `_SPECS/ADR/ADR-MCP-001_god-mode-cli-stack.md`

## Inbounds

- ADR-MCP-001
- Shadow_L2/02_god-mode-cli-stack-20260516.md
