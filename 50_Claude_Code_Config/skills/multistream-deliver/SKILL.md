---
name: multistream-deliver
description: >
  Decompose a multi-deliverable request into N independent work streams and
  execute them in parallel via the Agent tool with run_in_background=true.
  USE THIS SKILL whenever the user (A0) wants to: ship several loosely-coupled
  artifacts at once ("fais 1, 2, 3, 4", "do X, Y, Z in parallel", "ship these N"),
  bundle a sprint into parallel streams, or unblock a multi-ticket queue.
  Bakes in Doctrine Anti-Paresse (D1-D8), HITL gate compliance (DROP/DELETE/prod),
  D1 verification of every sub-agent's claims before writeback, no hard-delete
  (use _TRASH), no secrets in .md/.json/git, and the 4-file writeback contract
  (handoff + wiki log + README + project AGENTS.md).
when_to_use: |
  - User says "do X, Y, Z in parallel", "fais 1, 2, 3, 4", "ship N at once"
  - A request bundles ≥3 loosely-coupled artifacts (e.g. spec + scaffold + script + commit)
  - Each artifact fits in ≤1 sub-agent run (~5-15 min of focused work)
  - User has pre-authorized HITL gates they care about
  - Sub-agents are independent (no shared file writes during the parallel window)
---

# /multistream-deliver — Parallel Multi-Stream Work Delivery

## 1. When to use this skill

**Trigger**: A0 emits an Intention that bundles **≥3 independent artifacts** (e.g. "ship the spec + scaffold + script + Vercel config in parallel"). Each artifact is a coherent unit of work that one sub-agent (A3) can complete in a single focused run.

**Do NOT use** when:
- The work is **sequential by nature** (output of A feeds input of B) — parallelize only the independent slices
- It's a **single deliverable** with internal subtasks — use a single sub-agent, not a swarm
- The artifacts share file-write targets (race condition — sequence instead)

**Why parallel**: ~3-5× wall-clock speedup vs sequential sub-agents, with ~1.2-1.5× token overhead. The savings compound when each stream has its own HITL gate (the gates fan out in parallel instead of blocking one after another).

## 2. The 4-phase pattern (canonique)

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│ 1. DECOMPOSE│ →  │ 2. LAUNCH    │ →  │ 3. D1-VERIFY│ →  │ 4. WRITEBACK │
│             │    │   (parallel) │    │             │    │   (batched)  │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
   map streams      N× Agent tool       ls/find/cat/git    1× Edit/Write
   identify gates   run_in_bg=true      prove each claim   × 4 files
   verify indep     isolated prompts    NO assertions      no secrets
```

### Phase 1 — DECOMPOSE (do this yourself, in your main thread)

Before launching anything, draw the dependency graph on paper (or in your head):

1. **List all artifacts** A0 is asking for.
2. **Identify file-write targets** per artifact. Two streams writing the same file = race. Either sequence them, or split the file before launch.
3. **Tag each stream with HITL gates** (DROP/DELETE, prod env-var change, role provisioning, etc.). A0's pre-typed "GO on everything" is a **human authorization**, but the script's own gate prompt still requires the safety word at runtime (e.g. `GO-PROD`).
4. **Group independent streams** into the parallel batch. Dependent streams are out of this batch.
5. **Pick the D1 verification per stream** — what `ls` / `find` / `cat` / `git log` / `npx tsc` call will prove the claim? Write it down BEFORE launch so you don't trust the sub-agent's assertions.

### Phase 2 — LAUNCH (parallel sub-agents)

For each independent stream, fire one **Agent** tool call with `run_in_background: true`:

- **Self-contained prompt**: include the file path, the spec, the constraints, the expected output format, and the D1 verification command.
- **HITL awareness**: tell the sub-agent which gates it must respect (e.g. "use placeholders, no real keys", "commit but don't push if it requires force").
- **No cross-references**: each sub-agent works as if alone. The orchestrator (you) stitches results.
- **Tight scope**: ~5-15 min of focused work per sub-agent. Bigger than that and you lose the parallelism win (one slow stream blocks the writeback).

### Phase 3 — D1-VERIFY (you, in the main thread)

For every sub-agent's claim ("I created 25 files", "tsc clean", "4 commits pushed"), **run the proof yourself**. No exceptions.

| Claim type | D1 proof |
|---|---|
| "Files created" | `ls -la <dir>` or `find <dir> -type f \| wc -l` |
| "TypeScript compiles" | `npx tsc --noEmit` (capture exit code) |
| "Git commit X" | `git log --oneline -10` or `git show --stat <sha>` |
| "SQL file X has Y lines" | `wc -l <file>` or `grep -c <pattern> <file>` |
| "Skill Z exists" | `ls -la <skill-dir> && wc -l <skill>/SKILL.md` |
| "Vercel env vars set" | `mcp__vercel__list_env_variables` (cannot fake this) |

If D1 fails, **do not write back the failure as success**. Send the sub-agent back to fix, or roll forward with a different proof.

### Phase 4 — WRITEBACK (one batched step)

The 4-file writeback is **always the same**, in this order:

1. **Handoff** at `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_<proj>_<date>.md` — append a new "Status update" section with the D1-verified deliverables.
2. **Wiki log** at `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` — prepend (or append, if other agents are appending) a one-liner per stream.
3. **Memory README** at `00_Amadeus/30_MEMORY_CORE/README.md` — prepend a one-line bullet for the session.
4. **Project AGENTS.md / CLAUDE.md** — close the relevant ticket in the affected app's Work Guidance.

Why batched: scattered writebacks create N commit messages and N file-modification timestamps that are hard to audit. One batched writeback = one atomic record of "all 4 streams closed at HH:MM".

## 3. Critical constraints (doctrines baked in)

### D1 — Verify-Before-Assert
**Never** claim a sub-agent's output without running the proof yourself in the same turn. A sub-agent that says "done" is not the same as a `ls` that shows the files.

### D2 — Research FIRST
Before decomposing, read the relevant ADR / spec / existing code. Don't decompose a request that contradicts an unreviewed decision.

### D3 — Nuance over Literal
"GO on everything" from A0 does **not** mean bypass the script's safety prompts. The script's `read -p "Type GO-PROD"` still needs the literal `GO-PROD`. Pre-authorization is the human signal; the tool gate is a separate system.

### D4 — No self-contradiction cascade
If a sub-agent's claim contradicts another sub-agent's claim (e.g. "I created `0000_grants.sql`" vs "the migrations dir is empty"), **stop and D1-verify both** before writing back either.

### D5 — No self-congratulation
Don't write "✅ All streams successful!" until the D1 proofs are in your context, not in the sub-agent's transcript.

### D6 — Persistent symptom → collect exact command/message
If a sub-agent hits a recurring error (rate-limit, missing file, etc.), do not re-theorize. Collect the exact `stderr` and surface it.

### D7 — A0 escalation cost ~100×
Going back to A0 with a "wait, the migrations don't exist" is **100× cheaper** than going back with "I applied 0000+0001+0002 to the wrong schema because I didn't verify the path". D1 is the discount.

### D8 — Cross-agent respect
Codex / Gemini may be touching adjacent files. The orchestrator's role is not to "win" but to coordinate. If another agent's work is in your way, surface it cleanly, don't overwrite.

### HITL gates that ALWAYS persist
Even with A0's blanket "GO", these are non-bypassable:
- **DROP / DELETE / TRUNCATE** on prod schemas → script-level `read -p` confirmation
- **Service-role JWT** in any Vercel env → hard guard in `apply-vercel-env.ps1` (`SECRET` / `SERVICE_ROLE` / `PASSWORD` substrings rejected)
- **Postgres role provisioning** (`CREATE ROLE`) → one-time per role, A0 ratifies the role name first
- **Prod env-var changes** → Read-Host prompt in PowerShell, type `GO-PROD` to confirm
- **Project delete / domain removal** → HITL with screenshot of current state

### No hard-delete (→ _TRASH)
Any "delete file X" op is a "move file X to _TRASH/<date>_" op. Even for `rm -rf` of build artifacts — `mv` to a dated subdir first, then `rm -rf` the dated subdir after 7 days.

### No secrets in .md / .json / git
Keys, tokens, passwords live in:
- Windows env vars (User scope) — durable
- Test Key Pragma (in chat, for one-shot verification)
- Masked SecureString in `.ps1` (for prod services)
- **Never** in `.env` files that get committed, never in commit messages, never in `wiki/log.md` narratives

## 4. Sub-agent prompt template

Copy-paste this and adapt:

```text
You are stream <N>/<TOTAL> of a parallel multistream-deliver run for project <PROJ>.

Goal: <ONE-LINER DELIVERABLE>

Context:
- Repo root: <PATH>
- Spec / ADR / precedent: <LINKS>
- Constraints (read these first):
  - <DOCTRINE 1>
  - <DOCTRINE 2>
  - <HITL GATE, if any>

Deliverables (concrete):
- <FILE 1> — <description>
- <FILE 2> — <description>
- <COMMIT or EXTERNAL OP> — <description>

What you must NOT do:
- <PROHIBITION 1>
- <PROHIBITION 2>

Verification (D1) you should run yourself before reporting done:
- <command 1> → expected output
- <command 2> → expected output

Report format (return as your final message):
- Files created: <list with absolute paths>
- Verification results: <paste the command output>
- Any deviations from spec: <list, or "none">
- Suggested writeback line: <one sentence for the handoff>
```

## 5. Anti-patterns

| Anti-pattern | Why it fails | Fix |
|---|---|---|
| `run_in_background: false` for "parallel" streams | Streams run sequentially in the main thread | Always `true` for the parallel batch |
| Trusting sub-agent's "done" without D1 | D4 violation; cascading errors | Run the proof command yourself |
| Two streams writing the same file | Last-write-wins, silent corruption | Sequence the streams, or split the file before launch |
| Bundle dependent work as "parallel" | B's input is A's output; parallelism is fake | Sequence: A first, then B (or A's slice in parallel, B's slice after) |
| Skip the writeback because "the handoff is long" | A0 loses the audit trail | Always 4-file writeback, even for small streams |
| One big sub-agent doing all 4 streams | No parallelism win, single point of failure | One sub-agent per stream |
| Sub-agent includes the secret in its report | Doctrine Test Key Pragma violation | Mask the secret (`sk-****`) before pasting |
| Pasting `ls` output with secret filenames in handoff | Leaks secret names to git | Rename or `sed 's/sk-[a-zA-Z0-9]*/sk-REDACTED/g'` |

## 6. Worked example — P1.0-P1.4 abc-os-community (2026-06-10)

**A0's intent**: "Fais 1, 2, 3, 4 avec Claude en oublient Codex qui est cassé. Crée /ratify-adr skill."

**Decomposition** (4 streams, all independent, no shared file writes):

| # | Stream | Output | Sub-agent scope | D1 proof |
|---|--------|--------|-----------------|----------|
| 1 | `/ratify-adr` skill | SKILL.md (237L) + example | Write the skill at `~/.claude/skills/ratify-adr/` | `wc -l SKILL.md examples/*.md` |
| 2 | Frontend tickets | 4 commits on `Amdkn/02-ABC-OS/main` | Rename `/build` → `/build-hub`, add AGENTS.md, rewrite README, gate `/sandbox` to non-prod | `git log --oneline -10` |
| 3 | supabase-aspace MCP DRAFT | Spec (288L) + scaffold (25 files) | Write spec at `_SPECS/MCP/`, scaffold at `~/.mcp_servers/supabase-aspace/`, `tsc --noEmit` clean | `wc -l spec` + `find scaffold -type f \| wc -l` + `npx tsc --noEmit` |
| 4 | P1.4 Vercel env vars | 4 files in commit `4eb18bf` | `.env.example` (no secrets), `apply-vercel-env.ps1` (HITL-gated), `scripts/README.md`, `.gitignore` allowlist | `git show --stat 4eb18bf` + `grep -c "SECRET\|SERVICE_ROLE\|PASSWORD" .env.example` (expect 0) |

**Key insight**: each stream touches a different file set, so no race condition. All 4 launched in parallel via 4 Agent tool calls with `run_in_background: true`. Total wall-clock: ~10 min (vs ~40 min sequential).

**Writeback** (one batched step):
- Handoff: `handoff_abc_os_community_dev_2026-06-10.md` — added "P1 Backend Status" section
- Wiki log: 3 prepended entries (P1.0-P1.3, frontend, MCP DRAFT)
- README: 1 bullet
- (No project AGENTS.md update — the work was on apps, not on the project root)

## 7. When NOT to use this skill

- **Single artifact with internal subtasks** — use a single sub-agent, not a swarm
- **Strictly sequential pipeline** — sequence normally
- **Sub-agents with shared file-write targets** — sequence or split the file
- **Exploratory research** — use the Explore agent, not a parallel batch
- **A0 has not pre-authorized HITL gates** — the parallel speedup evaporates if each sub-agent has to wait for A0's per-stream GO

## 8. See also

- ADR-META-001 (Doctrine Anti-Paresse) — D1-D8
- ADR-INFRA-002 (Repo-Home/Junction) — file-write isolation between streams
- `~/.claude/skills/skill-creator/SKILL.md` — for creating/improving skills like this one
- `~/.claude/skills/ratify-adr/SKILL.md` — the canonical worked example (Stream 1 of the 2026-06-10 run)
- `~/.claude/rules/ecc/common/agents.md` — when to use Agent vs other tools
