---
id: ADR-INFRA-MCP-001
title: Agentic MCP Mastery — dox-layered "god mode" for the 5 production MCPs
status: ACCEPTED
date: 2026-06-10
deciders: A0 Amadeus (Go — "maitrise agentique en god mode pour Hostinger/Github/Dokploy/Vercel/Supabase avec rotation dynamique"), Claude Code (A2 design + execution)
refines: ADR-META-001 (Doctrine Anti-Paresse, D1-D8), ADR-INFRA-001 (Unified Governance Console)
related: [ADR-SUPABASE-001, ADR-OMK-001, ADR-INFRA-002, ADR-INFRA-003, ADR-CANON-001, /mcp-mastery, /aspace-supabase-mastery, /vercel-deploy-from-github, /picard-audit-and-prod-workflow]
domain: L0 Tech OS / 13th Doctor infra / MCP orchestration
tags: [#ADR #mcp #dox #god_mode #vault #rotation #autonomous #hitl #dox_tree]
---

# ADR-INFRA-MCP-001 — Agentic MCP Mastery (dox-layered god mode)

## Status
**ACCEPTED** (A0 Go, 2026-06-10). Immutable. Codifies the doctrine selected on 2026-06-10 in the
session preceding the execution trigger *"peut tu cloner, configurer et rendre l'utilisation de DOX autonome!?"*.

## Context

A0 wants **autonomous use + autonomous configuration of the 5 production MCPs** (hostinger,
github, dokploy, vercel, supabase) **with dynamic key rotation**, **documented in ADR + log wiki +
Memory Core README**.

Naive reading: a single "god mode" toggle that auto-approves everything. That reading breaks the
Airlock Protocol and the Doctrine Anti-Paresse (no human-in-the-loop = no sovereignty on
destructive ops).

Refined reading: **"god mode" is a stack of 4 independent layers**, each tunable:

1. **Dox tree** (context layer) — a tree of `AGENTS.md` files is a *binding work contract per
   subtree*. The agent walks the tree before any edit. Source: https://github.com/agent0ai/dox
   (cloned to `10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery_dox/`, 4 files, AGENTS.md canon
   section shape = Purpose/Ownership/Local Contracts/Work Guidance/Verification/Child DOX Index).
2. **Max perms** (config layer) — `settings.json` `allowedTools` / `mcp__<name>__*` whitelists
   the 5 MCPs so the runtime never prompts for them.
3. **Doc-first auto-approve** (semantic layer) — once a leaf `AGENTS.md` is in context AND the
   op is non-destructive AND not prod, the agent executes without asking.
4. **HITL gate** (safety layer) — destructive ops, prod env-var changes, key rotations ALWAYS
   require A0 sign-off, regardless of layers 1–3.

A0's answer to "what vault pattern?" = **vault centralisé** (Windows env User scope + `.env` on
the VPS, never in `.md`/`.json`/git). A0's answer to "what to build?" = **one orchestrator
skill + one ADR + one log entry + one README update**.

The previous session's failures (Dokploy deploy, Supabase connection) traced back to **no
binding work contract for the 5 MCPs**: every agent had to re-derive the contract from
memory, which is exactly what dox exists to prevent.

## Decision

### D1 — Dox tree as the binding work contract

Create a dox tree at `ASpace_OS_V2/10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/` with 6 files:

- `AGENTS.md` (root) — inventory, vault table, rotation policy, contract check, child index.
- `01_hostinger/AGENTS.md` — DNS, domains, VPS.
- `02_github/AGENTS.md` — repos, PRs, webhooks, releases.
- `03_dokploy/AGENTS.md` — apps, deployments, Traefik.
- `04_vercel/AGENTS.md` — projects, env vars, domains.
- `05_supabase/AGENTS.md` — schemas, RLS, PostgREST.

Each file follows the dox section shape (Purpose / Ownership / Local Contracts / Work
Guidance / Verification / Child DOX Index). Reference framework cloned at
`06_MCP_Mastery_dox/AGENTS.md` (dox v1, Agent Zero, MIT).

### D2 — Orchestrator skill: `/mcp-mastery`

Create `~/.claude/skills/mcp-mastery/SKILL.md` (and mirror to `~/.gemini/skills/` if/when
A0 chooses). The skill:
- Forces a dox tree walk (root + relevant child) before any MCP op.
- Lists the 4 layers of god mode in its body so the user can see what's active.
- Encodes the 5-second contract check.
- Encodes the vault smoke test (5 calls in parallel).
- Encodes the destructive-op gate (HITL list).

The skill is a thin wrapper. The contract lives in the dox tree.

### D3 — Vault centralisé (Windows env User)

All 5 keys/tokens in `[Environment]::SetEnvironmentVariable('NAME','value','User')`. Never
in `.md`/`.json`/git/MCP args/chat after rotation. The C3 table in the root `AGENTS.md` is
the live status — last_verified date, source provider, status (clean / ⚠️ exposed).

### D4 — Rotation policy

| Trigger | Action |
|---------|--------|
| Key appeared in chat / commit / transcript | Rotate within the same session |
| Quarterly (every 90 days) | Scheduled rotation, even if not exposed |
| Employee offboarding / device lost | Immediate rotation of all 5 |
| Provider-side leak alert | Immediate rotation of the affected key |

Rotation protocol = Test-Key Pragma (A'Space OS V2 doctrine): A0 pastes the new key, agent
sets the env var, agent runs a non-destructive smoke test, A0 revokes the old key, agent
updates C3 + appends to `## Rotations` below.

### D5 — Destructive ops HITL

The 4-layer model does **not** disable HITL. Layer 4 (HITL gate) is permanent. A0 remains
the only one who can sign off on:
- `DELETE` / `DROP` of a domain, repo, project, schema, deployment, or database.
- Production env-var changes (Vercel prod, Dokploy prod).
- Rotation of any of the 5 vault keys.
- Webhook or DNS record changes that affect production traffic.

### D6 — Verification

A change is "complete" only when D5 proof is on file: live smoke test result, or `git log`,
or a real query. Self-congratulation without proof = blocking violation of ADR-META-001 D5.

## Consequences

**Positive:** one binding work contract for the 5 MCPs; vault never leaks into chat/code/git;
HITL preserved for destructive ops; full doc chain (ADR + log + README + 6 AGENTS.md); reusable
pattern for future MCPs (any new MCP = new child folder under `06_MCP_Mastery/`).

**Cost:** the agent must read the dox tree before every op (~3 file Reads, ~5s overhead);
updating the dox tree is a discipline (the W4 contract in the root + the closeout in
dox's own AGENTS.md); mirrors to Gemini (when applicable) doubles the maintenance.

**Risk:** the dox tree can drift if A0 / A2 doesn't enforce the "update nearest owning doc
after every meaningful change" rule. Mitigation: the root `AGENTS.md` W4 + `/mcp-mastery`
skill's "After every meaningful change" section are the audible reminder. Quarterly audit
of the dox tree = governance task for A2.

**Tooling:** `/mcp-mastery` skill, the 6 AGENTS.md files, `~/.claude/settings.json` max-perms
config (when A0 applies it), the root vault status table.

## Rotations

| Date | MCP | Old → New | Trigger | Verified by |
|------|-----|-----------|---------|-------------|
| — | — | — | — | (none yet — table starts 2026-06-10) |

## Amendments

### 2026-06-10 (same day) — graphify added as 6th child MCP

A0 approved the addition of **graphify** (https://github.com/safishamsi/graphify, v8 branch,
0.8.36 installed via `uv tool install graphifyy`) as the **cross-cutting knowledge graph** layer
of the mastery tree. Rationale: the original 5 MCPs (hostinger/github/dokploy/vercel/supabase)
are all *vertical silos* — none answers the question *"what connects X to Y across L0/L1/L2?"*.
Graphify fills that gap.

- New child: `06_MCP_Mastery/06_graphify/AGENTS.md` (Purpose/Ownership/Local Contracts/Work
  Guidance/Verification/Child DOX Index).
- Vault: no dedicated token. Reuses `ANTHROPIC_API_KEY` + `ANTHROPIC_BASE_URL=https://api.minimax.io/anthropic`
  (MiniMax-M3 Anthropic-compat endpoint).
- Outputs: `graphify-out/graph.html` (interactive), `graphify-out/GRAPH_REPORT.md` (cold-start
  asset, committable), `graphify-out/graph.json` (programmatic, gitignored).
- Dox contract: every prior reference to "5 production MCPs" in this ADR is now "6 production
  MCPs". Root `AGENTS.md` inventory table, C3 vault state, and Child DOX Index all updated.

First build: `graphify .` on `ASpace_OS_V2/` (verified canon-only = 13 658 files after
node_modules/.git/_TRASH/.next/dist/build exclusion). Expected 5–15 min. See
`06_graphify/AGENTS.md` W3 for scope discipline and W6 for LLM backend config.
