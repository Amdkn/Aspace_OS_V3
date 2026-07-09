---
name: mythos
preamble-tier: 0
version: 1.0.0
description: |
  META-ROUTER. Auto-invoked at session start and on any user prompt that touches
  Life OS (L1) or Business OS (L2) work. Loads 3 canonical frameworks
  (superpowers, GSD Core, gstack) and dispatches to the right one based on
  domain. Native integration — no slash command needed; the skill description
  trigger handles routing. The 3 frameworks are CLONED at
  C:\Users\amado\.agent-frameworks\{superpowers,gsd-core,gstack}\ and symlinked
  to canonical CC paths.
allowed-tools:
  - Read
  - Edit
  - Write
  - Grep
  - Glob
  - Bash
  - Agent
  - TodoWrite
  - Skill
triggers:
  - mythos
  - /mythos
  - life OS
  - business OS
  - L1 orchestration
  - L2 orchestration
  - harness engineering
  - loop engineering
  - wargame
  - multi-goal
  - swarm-orchestrator
  - fable-mode
  - 12wy
  - /loop
  - meta-router
related:
  - superpowers/skills/using-superpowers/SKILL.md (A2/A3 process bootstrap)
  - gsd-core/README.md (A3/B3 phase loop)
  - gstack/SKILL.md (A0/B1 CEO/Eng/QA/Review router)
  - ../../ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md (canon)
doctrine_anchors:
  - ADR-META-001 (D1-D8 verify before assert)
  - ADR-SOBER-002 (anti-paperclip)
  - superpowers: "If a skill applies, you don't have a choice. You must use it."
  - gstack: "When in doubt, invoke the skill. A false positive is cheaper than a false negative."
  - gsd: "Heavy work runs in fresh subagents. Solve context rot."
---

# /mythos — Meta-Router (A0 Jumeau Numérique orchestrating Life OS + Business OS)

## When this skill fires

ANY user message that touches:
- **Life OS (L1)** : Life Wheel, Ikigai, 12WY, PARA, GTD, DEAL, habit, health, family
- **Business OS (L2)** : OMK, Nexus, Solaris, Orbiter, ICP, franchise, pricing, ICP, AaaS, B1/B2/B3 domains
- **Cross-layer** : wargame, multi-goal, swarm, loop, fable, dispatch, parallel agents, sub-agent orchestration

→ /mythos loads at session start, dispatches the right framework, and stays out of the way.

## Why this exists

A0 (Amadeus Jumeau Numérique) does NOT do A2/A3 work directly. /mythos is the **meta-router** that:
1. Loads `superpowers:using-superpowers` → all A2/A3 process skills auto-invoke
2. Loads `gsd-core` 5-phase loop → all A3/B3 orchestration runs in fresh subagent context
3. Loads `gstack` router → all A0/B1 vision tools (CEO/Eng/QA/Review/Ship) auto-invoke
4. Maps the request to the right framework based on Life OS vs Business OS domain
5. Persists `STATE.md` + `CONTEXT.md` so the next session continues without re-derivation

## Preamble (run first)

```bash
# Verify the 3 framework clones exist
test -d "C:/Users/amado/.agent-frameworks/superpowers" && echo "SUPERPOWERS: OK" || echo "SUPERPOWERS: MISSING"
test -d "C:/Users/amado/.agent-frameworks/gsd-core" && echo "GSD: OK" || echo "GSD: MISSING"
test -d "C:/Users/amado/.agent-frameworks/gstack" && echo "GSTACK: OK" || echo "GSTACK: MISSING"

# Detect domain
_DOMAIN="unknown"
case "$1 $2 $3" in
  *wargame*|*fable*|*mythos*|*loop*) _DOMAIN="cross" ;;
  *"life"*|*"12wy"*|*"para"*|*"gtd"*|*"deal"*|*"ikigai"*|*"habit"*|*"health"*|*"family"*) _DOMAIN="life" ;;
  *"omk"*|*"nexus"*|*"solaris"*|*"orbiter"*|*"icp"*|*"franchise"*|*"pricing"*|*"aaas"*|*"outbound"*) _DOMAIN="business" ;;
esac
echo "DOMAIN: $_DOMAIN"
```

## Routing rules

| If request mentions | Domain | Route to | Auto-invoke |
|---|---|---|---|
| "build me a feature", "implement X", "let's add" | cross | superpowers | `brainstorming` (hard-gate, no code before design) |
| "fix this bug", "why is this broken", "wtf" | cross | superpowers | `systematic-debugging` |
| "review my diff", "check the code", "pre-landing" | cross | superpowers | `requesting-code-review` |
| "write tests for X", "add TDD" | cross | superpowers | `test-driven-development` |
| "run multiple agents", "parallel", "swarm" | cross | superpowers | `dispatching-parallel-agents` |
| "plan this work", "break it down" | cross | superpowers | `writing-plans` |
| "verify", "is this done", "check completeness" | cross | superpowers | `verification-before-completion` |
| "ship a phase", "milestone", "5-phase" | life+business | gsd-core | `gsd-discuss-phase` → `gsd-plan-phase` → `gsd-execute-phase` |
| "fresh context", "delegate to subagent", "isolated worktree" | life+business | gsd-core | `gsd-execute-phase` (200K context per executor) |
| "is this worth building", "idea", "brainstorm" | business | gstack | `/office-hours` |
| "spec this out", "backlog item", "PRD" | business | gstack | `/spec` |
| "strategy", "scope", "think bigger" | business | gstack | `/plan-ceo-review` |
| "architecture", "lock the plan", "design" | business | gstack | `/plan-eng-review` |
| "design system", "brand", "visual" | business | gstack | `/design-consultation` |
| "audit security", "OWASP", "vulnerabilities" | business | gstack | `/cso` |
| "test the site", "QA", "browser test" | business | gstack | `/qa` |
| "review code", "diff check" | business | gstack | `/review` |
| "ship", "deploy", "PR", "land" | business | gstack | `/ship` or `/land-and-deploy` |
| "monitor prod", "post-deploy" | business | gstack | `/canary` |
| "weekly retro", "what did we ship" | business | gstack | `/retro` |
| "performance", "benchmark", "page speed" | business | gstack | `/benchmark` |
| "health check", "code quality dashboard" | business | gstack | `/health` |
| "save progress", "checkpoint" | cross | gstack | `/context-save` |
| "resume", "where was I" | cross | gstack | `/context-restore` |
| "second opinion", "codex review" | cross | gstack | `/codex` |
| "Life Wheel pulse", "drift in LD0X" | life | ASpace-A3 | `a3-discovery-{book,culber,saru,tilly,...}` |
| "Ikigai GO/NO-GO", "authorize this" | life | ASpace-A2 | `a2-uss-orville-meaning` |
| "GTD capture/clarify/organize/reflect/engage" | life | ASpace-A2 | `a2-uss-cerritos-chaos` |
| "PARA placement", "where does this go" | life | ASpace-A3 | `a3-cerritos-tendi` |
| "12WY Rock", "weekly plan", "focus block" | life | ASpace-A2 | `a2-uss-snw-execution` |
| "OMK domain audit" (People/Ops/Product/Growth/Sales/IT/Finance/Legal) | business | ASpace-B2 | `b2-0X-{greenlantern,batman,flash,superman,johnjones,cyborg,wonderwoman,aquaman}` |

## D1 receipts (D1 verified 2026-07-09)

- **superpowers** = obra/superpowers @ 250,237 ★, MIT, 14 skills, multi-plugin (claude/codex/cursor/kimi/opencode/pi). Acceptance test: "Let's make a react todo list" → `brainstorming` auto-fires.
- **GSD Core** = open-gsd/gsd-core @ 6,217 ★, MIT, JS. Install: `npx @opengsd/gsd-core@latest`. 5-phase loop solves context rot via fresh subagent 200K contexts + STATE.md/CONTEXT.md persistence.
- **gstack** = garrytan/gstack @ 120,638 ★, MIT, 23 skills. Install: `git clone --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && ./setup`. Boil the Ocean principle, "Boil the Ocean" ethos: do the complete thing when AI marginal cost → 0.

## Auto-invocation mechanism (D2: this is the key insight)

The 3 frameworks all use the **same pattern**: SessionStart hook loads a `using-X` bootstrap that **forces** the agent to check for applicable skills BEFORE any response.

- superpowers: `<EXTREMELY-IMPORTANT>If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill.</EXTREMELY-IMPORTANT>`
- gstack: "When in doubt, invoke the skill. A false positive (invoking a skill that wasn't needed) is cheaper than a false negative."
- gsd: Fresh subagent contexts for heavy work; state survives via `STATE.md` + `CONTEXT.md`.

**/mythos inherits all three.** It runs as the SessionStart hook in `~/.claude/settings.json`, and:
1. First response: announce `Using superpowers + GSD + gstack` to set the discipline context
2. On any user prompt: scan the routing table above, dispatch to the right skill
3. On no match: ask ONE clarifying question (not zero — clarification is a /mythos responsibility)

## Bypass permission (D7 controlled)

When /mythos is active, the following tools are auto-accept (configured in `~/.claude/settings.json` `allowedTools`):

- Read, Edit, Write, Grep, Glob (read/inspect/author canon)
- Bash for safe commands (ls, cat, git status, git diff, git log, npm/pip/bun install, mkdir, mv, cp of new files)
- Agent (sub-agent dispatch)
- TodoWrite (work tracking)
- Skill (skill invocation)
- mcp__* (MCP tools)

**Still gated** (require user confirmation):
- Bash destructive (rm -rf, drop table, git push --force, git reset --hard)
- Network-write to public remotes (git push to public repo, npm publish)
- Any tool that touches secrets/credentials (Write to .env, push that contains tokens)

## Maps to A'Space canon (A0/A1/A2/A3/B1/B2/B3)

| Layer | A'Space role | Framework skill | Why |
|---|---|---|---|
| A0 | Jumeau Numérique (vision H30) | gstack `/plan-ceo-review` + `/office-hours` | CEO scope review, NOT engineering |
| A1 Beth | Veto (Life Preservation) | gstack `/careful` + `/guard` | Restrict edits, gate the kill-switch |
| A1 Morty | Execution (12WY Rock) | gsd-core `gsd-execute-phase` | 5-phase loop, fresh subagents |
| A1 Rick | Sobriété kernel | superpowers `systematic-debugging` | D6 root cause, anti-paperclip |
| A2 superpowers | Manager E-Myth des freelances | superpowers 14 skills | Documented, idempotent, antifragile |
| A2 GSD | A3 vision | gsd-core phase loop | Spec-driven, 200K context per executor |
| A2 gstack | B1 vision | gstack `/plan-eng-review` | Architecture lock-in |
| A3 freelances | Méta-orchestrateurs de tâches | superpowers subagent-driven | "Dispatch one agent per independent problem domain" |
| A3 cerritos/discovery/orville | Life OS sub-orchestrators | ASpace agents (pas frameworks externes) | Native canon A'Space |
| B1 Jerry | SYSTEMIZE | gstack `/plan-eng-review` | Architecture review |
| B1 Summers | SHIP | gstack `/ship` + `/land-and-deploy` | Built to Sell |
| B2 8 domains | E-Myth Managers | ASpace b2-0X-* agents | Native canon A'Space |
| B3 53 nanosquads | E-Myth Techniciens | gstack `/qa` + `/review` | QA + review loop |

## Operational self-improvement (D7)

Before completing, if you discovered a durable project quirk or command fix that would save 5+ minutes next time, log it:

```bash
echo '{"date":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","key":"SHORT_KEY","insight":"DESCRIPTION","confidence":N}' >> C:/Users/amado/.claude/skills/mythos/learnings.jsonl
```

Do not log obvious facts or one-time transient errors.

## Status protocol

Report one of:
- **DONE** — completed with evidence (file paths, D1 receipts).
- **DONE_WITH_CONCERNS** — completed, but list concerns.
- **BLOCKED** — cannot proceed; state blocker and what was tried.
- **NEEDS_CONTEXT** — missing info; state exactly what is needed.

Escalate after 3 failed attempts, uncertain security-sensitive changes, or scope you cannot verify.
