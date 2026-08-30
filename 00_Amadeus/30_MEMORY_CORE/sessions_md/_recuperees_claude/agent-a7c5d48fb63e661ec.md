---
session: agent-a7c5d48fb63e661ec
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\_ARCHIVE_2026-06-16_sessions\projects\C--Users-amado\6404fbdc-82fd-45da-b403-173b831aecb8\subagents\agent-a7c5d48fb63e661ec.jsonl
debut: 2026-05-19T10:23:18.274Z
fin: 2026-05-19T10:26:09.940Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "Scan ECC skill files for patterns relevant to A'Space OS. Read the SKILL.md frontmatter (first 10-15 lines eac…"
---

## >>> UTILISATEUR #1

Scan ECC skill files for patterns relevant to A'Space OS. Read the SKILL.md frontmatter (first 10-15 lines each) of these skills:

1. C:\Users\amado\ECC\skills\agent-harness-construction\SKILL.md
2. C:\Users\amado\ECC\skills\agentic-os\SKILL.md
3. C:\Users\amado\ECC\skills\autonomous-loops\SKILL.md
4. C:\Users\amado\ECC\skills\configure-ecc\SKILL.md
5. C:\Users\amado\ECC\skills\continuous-learning-v2\SKILL.md
6. C:\Users\amado\ECC\skills\security-review\SKILL.md
7. C:\Users\amado\ECC\skills\verification-loop\SKILL.md
8. C:\Users\amado\ECC\skills\database-migrations\SKILL.md
9. C:\Users\amado\ECC\skills\mcp-server-patterns\SKILL.md
10. C:\Users\amado\ECC\skills\clickhouse-io\SKILL.md
11. C:\Users\amado\ECC\skills\postgres-patterns\SKILL.md
12. C:\Users\amado\ECC\skills\e2e-testing\SKILL.md
13. C:\Users\amado\ECC\skills\agentic-engineering\SKILL.md
14. C:\Users\amado\ECC\skills\cost-tracking\SKILL.md
15. C:\Users\amado\ECC\skills\context-budget\SKILL.md
16. C:\Users\amado\ECC\skills\tdd-workflow\SKILL.md
17. C:\Users\amado\ECC\skills\eval-harness\SKILL.md
18. C:\Users\amado\ECC\skills\deep-research\SKILL.md
19. C:\Users\amado\ECC\skills\fastapi-patterns\SKILL.md
20. C:\Users\amado\ECC\skills\docker-patterns\SKILL.md
21. C:\Users\amado\ECC\skills\deployment-patterns\SKILL.md
22. C:\Users\amado\ECC\skills\autonomous-agent-harness\SKILL.md
23. C:\Users\amado\ECC\skills\agent-introspection-debugging\SKILL.md
24. C:\Users\amado\ECC\skills\github-ops\SKILL.md
25. C:\Users\amado\ECC\skills\gitlab-ci-cd\SKILL.md (if exists)
26. C:\Users\amado\ECC\skills\coding-standards\SKILL.md

Extract from each: name, description, key capabilities, and tag/keyword hints.

Return a structured markdown table:

| Skill | Name | Description | Key capabilities | Tags |
|-------|------|-------------|-------------------|------|

Also note which skills would be highest priority for:
- A'Space OS L0 (Rick's Tech OS: hooks, MCP, autonomous loops)
- A'Space OS L1 (Life Fleet: verification, heartbeat, test)
- A'Space OS L2 (Business Pulse: database ops, Supabase/Baserow, CRM)

Report only what you found — no synthesis or recommendations.

### assistant

| # | Skill | Name | Description | Key capabilities | Tags |
|---|-------|------|-------------|-------------------|------|
| 1 | `agent-harness-construction/SKILL.md` | Agent Harness Construction | Design and optimize AI agent action spaces, tool definitions, and observation formatting for higher completion rates. | Action space design, tool definition optimization, observation formatting, agent completion rate improvement | agent-design, tool-definition, harness |
| 2 | `agentic-os/SKILL.md` | Agentic OS | Build persistent multi-agent operating systems on Claude Code. Covers kernel architecture, specialist agents, slash commands, file-based memory, scheduled automation, and state management without external databases. | Kernel config routing, persistent file-based memory, scheduled automation, JSON/markdown data layer, multi-agent workflows | agentic-os, multi-agent, persistent-automation, slash-commands, memory |
| 3 | `autonomous-loops/SKILL.md` | Autonomous Loops | Patterns and architectures for autonomous Claude Code loops — from simple sequential pipelines to RFC-driven multi-agent DAG systems. | Sequential pipelines, RFC-driven DAG orchestration, autonomous loop architectures | autonomous-loops, dag, pipeline |
| 4 | `configure-ecc/SKILL.md` | Configure ECC | Interactive installer for Everything Claude Code — guides users through selecting and installing skills and rules to user-level or project-level directories, verifies paths, and optionally optimizes installed files. | Interactive installation wizard, skill/rule selection, path verification, optimization | ecc, installer, setup |
| 5 | `continuous-learning-v2/SKILL.md` | Continuous Learning v2 | Instinct-based learning system that observes sessions via hooks, creates atomic instincts with confidence scoring, and evolves them into skills/commands/agents. v2.1 adds project-scoped instincts. | Atomic instincts, confidence scoring, project-scoped learning, hook-based observation | learning, instincts, hooks |
| 6 | `security-review/SKILL.md` | Security Review | Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features. | Authentication, authorization, input validation, secrets management, API security, payment features | security, auth, secrets, api |
| 7 | `verification-loop/SKILL.md` | Verification Loop | A comprehensive verification system for Claude Code sessions. | Post-feature verification, pre-PR checks, session validation | verification, testing, quality |
| 8 | `database-migrations/SKILL.md` | Database Migrations | Database migration best practices for schema changes, data migrations, rollbacks, and zero-downtime deployments across PostgreSQL, MySQL, and common ORMs. | Schema changes, data migrations, rollbacks, zero-downtime, Prisma/Drizzle/Kysely/Django/TypeORM/golang-migrate | migrations, postgresql, mysql, orm |
| 9 | `mcp-server-patterns/SKILL.md` | MCP Server Patterns | Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs Streamable HTTP. | MCP server construction, tool/resource/prompt definitions, Zod validation, stdio/HTTP transport, SDK upgrade guidance | mcp, node, typescript, sdk |
| 10 | `clickhouse-io/SKILL.md` | ClickHouse IO | ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads. | MergeTree engine, analytical queries, aggregation/window functions/joins, partition pruning, projections, materialized views | clickhouse, analytics, data-engineering |
| 11 | `postgres-patterns/SKILL.md` | PostgreSQL Patterns | PostgreSQL database patterns for query optimization, schema design, indexing, and security. Based on Supabase best practices. | Query optimization, schema design, indexing, security, Supabase-based | postgresql, supabase, database |
| 12 | `e2e-testing/SKILL.md` | E2E Testing | Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and flaky test strategies. | Playwright, POM, CI/CD integration, artifact management, flaky test strategies | e2e, playwright, testing |
| 13 | `agentic-engineering/SKILL.md` | Agentic Engineering | Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model routing. | Eval-first execution, work decomposition, model tier routing, human quality enforcement | agentic-engineering, eval, cost-aware |
| 14 | `cost-tracking/SKILL.md` | Cost Tracking | Track and report Claude Code token usage, spending, and budgets from a local cost-tracking database. | Token usage tracking, spending reports, budget monitoring by project/tool/session/date | cost, tokens, budget, tracking |
| 15 | `context-budget/SKILL.md` | Context Budget | Audits Claude Code context window consumption across agents, skills, MCP servers, and rules. Identifies bloat, redundant components, and produces prioritized token-savings recommendations. | Context window audit, token overhead analysis, bloat identification, savings recommendations | context, tokens, optimization |
| 16 | `tdd-workflow/SKILL.md` | TDD Workflow | Use this skill when writing new features, fixing bugs, or refactoring code. Enforces test-driven development with 80%+ coverage including unit, integration, and E2E tests. | TDD enforcement, 80%+ coverage, unit/integration/E2E tests | tdd, testing, coverage |
| 17 | `eval-harness/SKILL.md` | Eval Harness | Formal evaluation framework for Claude Code sessions implementing eval-driven development (EDD) principles. | Eval-driven development, pass/fail criteria, session evaluation framework | eval, edd, evaluation |
| 18 | `deep-research/SKILL.md` | Deep Research | Multi-source deep research using firecrawl and exa MCPs. Searches the web, synthesizes findings, and delivers cited reports with source attribution. | Web research, multi-source synthesis, cited reports, firecrawl/exa MCP | research, web-scrap
