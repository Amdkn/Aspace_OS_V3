---
name: mcp-mastery
description: >
  Orchestrator for the 5 production MCPs (hostinger, github, dokploy, vercel, supabase) of
  A'Space OS V2. Forces a dox-tree walk before any MCP op: reads
  ASpace_OS_V2/10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/AGENTS.md (root) then the
  child AGENTS.md that owns the target (01_hostinger, 02_github, 03_dokploy, 04_vercel,
  05_supabase). USE THIS SKILL whenever the user (A0) wants to: do anything via the
  hostinger/github/dokploy/vercel/supabase MCPs, change a DNS record, deploy a Vercel or
  Dokploy app, create/modify a Supabase schema, rotate a vault key, check MCP health, or
  review the MCP mastery contract. Reads the dox tree first (binding work contract per
  dox doctrine), then the relevant leaf skill (e.g. /aspace-supabase-mastery, /
  vercel-deploy-from-github, /picard-audit-and-prod-workflow Phase 6 for deploys), then
  executes. Auto-approves non-destructive reads + dev/preview writes; HITL-gates all
  destructive ops + prod env-var changes + key rotations. Doctrine: ADR-INFRA-MCP-001.
---

# /mcp-mastery — orchestrator for the 5 production MCPs

> **Binding contract:** the dox tree at
> `ASpace_OS_V2/10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/`
> is a work contract. Walk it before every op. Update it after every meaningful change.
> Doctrine: [ADR-INFRA-MCP-001](../../ASpace_OS_V2/_SPECS/ADR/ADR-INFRA-MCP-001_agentic-mcp-mastery-dox-god-mode.md).

## When to use this skill

Trigger on any of:
- "deploy … on Vercel / Dokploy"
- "create / update / delete a DNS record"
- "open / merge a PR"
- "create a schema / table / RLS policy / PostgREST exposure"
- "rotate the <X> key / token"
- "check the MCPs / run the smoke tests"
- "what's the state of the vault"
- any `mcp__hostinger__*`, `mcp__github__*`, `mcp__dokploy__*`, `mcp__vercel__*`, `mcp__supabase__*` call

## The 4 layers of dox-layered god mode

| Layer | What it is | Where it lives | How it's enforced |
|-------|-----------|----------------|-------------------|
| 1 — Dox tree | Tree of `AGENTS.md` = binding work contract per subtree | `06_MCP_Mastery/` | This skill forces a Read of root + relevant child before any op |
| 2 — Max perms | `settings.json` allows all 5 MCPs without per-call prompt | `~/.claude/settings.json` | Config-time, not runtime |
| 3 — Doc-first auto-approve | When the dox leaf has been read and the op is non-destructive + non-prod, auto-execute | This skill's W3 | Runtime, per-call |
| 4 — HITL gate | Destructive ops, prod env, key rotation = always prompt A0 | Root `AGENTS.md` W3 | Runtime, per-call |

> "God mode" = layers 1+2+3 active. Layer 4 ALWAYS remains. Auto-pilot without HITL would
> break the Airlock Protocol — too risky for a sovereign OS.

## The 5-second contract check (always do this first)

```
1. Read 06_MCP_Mastery/AGENTS.md                            (root inventory + vault state)
2. Read 06_MCP_Mastery/<relevant_child>/AGENTS.md           (e.g. 03_dokploy/ for a deploy)
3. Read the leaf skill (if one exists):
   - Supabase ops       → /aspace-supabase-mastery
   - Vercel deploy      → /vercel-deploy-from-github
   - Vercel/Dokploy prod → /picard-audit-and-prod-workflow Phase 6
4. Read the relevant leaf skill's AGENTS.md contract
5. THEN call the MCP tool
```

## Vault check (rotate / status / smoke)

```bash
# All 5 in parallel — auto-approved (read-only, no destructive op):
gh api user                                                        # GitHub
mcp__hostinger__listDomains()                                      # Hostinger
mcp__dokploy__list_projects                                        # Dokploy
mcp__vercel__list_teams                                            # Vercel
ssh aspace-vps "cd /srv/aspace/supabase/docker && ANON=\$(grep -E '^ANON_KEY=' .env | cut -d= -f2-) && \
  curl -s -o /dev/null -w 'saas %{http_code}\n' 'http://localhost:8000/rest/v1/organizations' -H \"apikey: \$ANON\" -H 'Accept-Profile: omk_saas' && \
  curl -s -o /dev/null -w 'internal %{http_code}\n' 'http://localhost:8000/rest/v1/agents' -H \"apikey: \$ANON\" -H 'Accept-Profile: omk_internal' && \
  curl -s -o /dev/null -w 'public %{http_code}\n' 'http://localhost:8000/rest/v1/' -H \"apikey: \$ANON\""   # Supabase
```

All green → "autonomous" status confirmed. Any red → STOP, read the child `AGENTS.md` Work
Guidance, do not retry blindly (D6 — persistent symptom → exact command).

## Destructive-op gate (HITL)

STOP and ask A0 before any of:
- `mcp__hostinger__deleteDNSRecord`, `mcp__hostinger__restartVPS`
- `mcp__github__merge_pull_request`, `mcp__github__delete_repository`
- `mcp__dokploy__delete_application`, any prod env-var change
- `mcp__vercel__delete_project`, any prod env-var change, domain removal
- `mcp__supabase__execute_sql` containing `DROP` / `DISABLE ROW LEVEL SECURITY` / `DELETE FROM <prod_table>`
- Any key rotation (all 5)

Use AskUserQuestion with the exact command, the target, and the blast radius in the question.

## After every meaningful change

1. Update the nearest owning `AGENTS.md` (root or child).
2. If the change affected vault state, update `06_MCP_Mastery/AGENTS.md` C3 table.
3. If the change was a key rotation, append to `ADR-INFRA-MCP-001` `## Rotations`.
4. If the change crossed a boundary (new leaf, new MCP, new contract), update the root `Child DOX Index`.
5. Report with proof (D5) — never with assertion.

## Guardrails

- Never echo a vault key in chat, in any file, in any commit, in any log. (Test-key pragma
  is OK during the rotation protocol only; A0 rotates immediately after.)
- Never disable RLS on a `*_saas` or `*_internal` table without an explicit "yes, I know
  I'm exposing all rows" from A0.
- Never delete a domain / repo / project / schema without first confirming there's a
  backup, a fork, or a sibling that survives.
- Never trust a smoke test that returns 200 but empty body — re-verify with a real query.
- Trust the dox tree over this skill text. If they conflict, the tree wins (it's the
  binding contract).
