---
name: abc-os-write-back-protocol
description: Enforce the 6-step write-back protocol after EVERY abc-os mission (commit, custom domain wire, i18n migration, Supabase apply, >30 min task). Writes to wiki/log.md + MEMORY.md index + new memory files when doctrines/patterns emerge + AGENTS.md when contracts change + handoff file when mission is significant. Use this skill whenever you just completed: a commit in any abc-* repo, a custom domain wire / DNS change, an i18n migration, a Supabase apply, a scaffold/template work, or any mission > 30 min on the abc-os stack. Even if you think the change is "small" — write it back. The wiki is living memory, and unrecorded work is lost work. Triggers include "commit abc-*", "wire abc-os.kalybana.com", "ship i18n", "apply migration", "D1 verify done". DO NOT use for: pure Q&A turns, mid-task mid-flight sub-agent work, or anything < 5 min of work. This is the Hermes-style self-improvement pattern at write-time.
metadata:
  type: skill
  domain: memory-protocol
  layer: L2 (Business OS) ↔ L0 (Memory Core)
  anchors:
    - ADR-META-001 (D1 Verify-Before-Assert, D3 Nuance over Literal, D7 A0 escalation cost)
    - ADR-MEM-001 (Living memory: log.md is append-only, MEMORY.md is the index, no duplication)
    - feedback-autonomous-skill-creation (Phase 2 Hermes-style — write-back IS the work that compounds)
  precedent: 2026-06-13 — 3× fires (Build Hub e3da5be, i18n 5a19439, custom domain abc-os.kalybana.com wire)
  creation: Phase 2 autonomous (A0 doctrine update 2026-06-13)
---

# abc-os-write-back-protocol

The non-negotiable post-mission ritual for abc-os. Every commit, wire, migration, i18n change, or > 30 min mission on the abc-os stack writes back to **3-5 memory files** before the orchestrator reports to A0. Without this ritual, the next Claude Code session has no context — A0's wiki is the only persistent memory across sessions, and unrecorded work is lost work.

**Why this exists as a skill** : 3 missions in the 2026-06-13 session all needed the same write-back (Build Hub commit, i18n migration, custom domain wire). Each one was ~3-5 min of "now I write to log.md, update MEMORY.md, save the new memory file, etc." The pattern fires 100% of the time on every abc-os mission. Baked into a skill, every future invocation saves ~3-5 min + guarantees no step is forgotten. This is the **Hermes-style write-time self-improvement** — every mission strengthens the memory of the OS.

**Why Phase 2 (autonomous)** : A0 doctrine update 2026-06-13 ([[feedback-autonomous-skill-creation]]) — when this skill triggers, the agent MUST run it without asking A0 for GO. The cost of A0 escalation (D7, ~100×) far exceeds the cost of a 3-5 min ritual. A0 reviews post-hoc in the session report.

## When to trigger (3 conditions — any 1 fires)

1. **Commit in any `abc-*` repo** : git log shows a new SHA on `apps/abc-os-community/`, `apps/abc-build-hub/`, or any repo under `30_Business_OS/10_Projects/abc/`. Even `chore:` or `docs:` commits count.
2. **Mission > 30 min** : any task that took meaningful sub-agent work. Includes: DNS/domain wires, framework migrations (i18n, Tailwind v4, Next.js 15), Supabase applies, scaffold creation.
3. **New doctrine / pattern / contract emerged** : the agent learned something that future sessions need. Examples: Hostinger API has no `POST /records` (use PUT zone-replacement), next-intl EN-first migration pattern, kalybana.com is on Hostinger DNS despite NS report, MCP tokens live on VPS at `~/.claude.json`.

**Do NOT use for** : pure Q&A turns, mid-task mid-flight sub-agent work (wait for the task to complete), any work < 5 min, or any non-abc-os work (other projects have their own write-back rituals).

## The 5-step write-back ritual

When this skill triggers, the orchestrator (A2) follows these 5 steps in order. **Steps are not optional** — the only "optional" step is Step 3 (new memory file), which only fires when a new doctrine/pattern emerged.

### Step 1 — Append to `wiki/log.md` (always)

File: `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\log.md`

Append a `**YYYY-MM-DD**` block at the top (after the most recent entry, before the H2 sections). Format:

```markdown
**YYYY-MM-DD** : <one-line summary>. <repos touched, commits, evidence links>.

```

- One line is enough for routine work
- Multi-line is OK for major missions (cross-repo, doctrine changes, new SKILL.md)
- Always include the SHA or evidence path so the next session can `git log`/Re-Read to verify

### Step 2 — Update `MEMORY.md` index (always)

File: `C:\Users\amado\.claude\projects\C--Users-amado\memory\MEMORY.md`

If new memory files were created, add 1-line pointer entries under the appropriate section. If no new files, **at least** re-Read `MEMORY.md` to confirm the session is reflected (the index is living — sessions that don't show up are dead sessions).

```markdown
- [Skill name](file.md) — one-line hook
```

### Step 3 — New memory file (only if new doctrine/pattern emerged)

File: `C:\Users\amado\.claude\projects\C--Users-amado\memory\<name>.md`

When the mission produced a **reusable insight** (not just a one-off change), save it as a memory file with frontmatter:

```markdown
---
name: <short-kebab-case-slug>
description: <one-line summary — used to decide relevance in future conversations, so be specific>
metadata:
  node_type: memory
  type: project | reference | feedback
  originSessionId: <UUID of current session>
---

<body — 200-500 words max, with **Why:** and **How to apply:** sections for project/feedback types>
```

Then add the pointer in `MEMORY.md` (Step 2). The rule of thumb: if you'd re-derive the same insight in 6 months without the memory, save it.

### Step 4 — Update `AGENTS.md` contract (only if contract changed)

If the mission changed a contract (e.g., new MCP server, new port, new DNS endpoint, new skill created, new ADR supersedes an old one), update the relevant `AGENTS.md` in `ASpace_OS_V2/`. Common targets:

- `10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/<service>/AGENTS.md` — MCP contract
- `10_Tech_OS/11_Infra_13th_Doctor/00_Governance_Rick/AGENTS.md` — governance
- `30_Business_OS/10_Projects/abc/apps/<app>/AGENTS.md` — app contract

The rationale in the AGENTS.md update is **the load-bearing piece** — without rationale, the next session re-derives the contract and you pay 10× the cost.

### Step 5 — Handoff file (only if mission is significant)

File: `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_<context>_dev_<DATE>.md`

Create a handoff when: a new skill was created, an ADR was added/changed, a new project/app was scaffolded, the next session would otherwise lose > 10 min re-deriving context. Format:

```markdown
# Handoff — <Context> <DATE>

## What shipped
- <list of artifacts>

## Open follow-ups
- <list of next-session work>

## Doctrine anchors
- <list of relevant ADRs/memories>

## Verification receipts (D1)
- <raw counts, URLs, evidence>
```

If a handoff from a similar context already exists, append a "P_N <Context> Status" section rather than creating a new file (per `abc-os-backend-delegation` precedent).

## Doctrine anchors (cite in every invocation)

- **D1 Verify-Before-Assert** (ADR-META-001): every write-back file is verified by Re-Read or D1 query before reporting done. Raw evidence, not "I wrote it".
- **D3 Nuance over Literal**: if the write-back location changed (e.g., MEMORY.md moved), adapt the path but preserve the semantic intent.
- **D7 A0 escalation cost**: don't ask A0 "should I run this skill?" — run it. A0 reviews post-hoc.
- **ADR-MEM-001 (Living memory)**: log.md is append-only (never edit past entries), MEMORY.md is the index (no duplication — files are the truth), memory files are short and dense (not novels).
- **Phase 2 (autonomous skill creation)**: writing this skill is itself an example of Phase 2 — the agent created it at end of session without A0 GO.

## Time cost & ROI

- Per invocation: ~3-5 min (Read 3-5 files, Edit 3-5 files, verify with Re-Read)
- Per session (3-5 missions): ~15-25 min
- Sessions saved: future sessions pick up context in < 30 sec instead of re-deriving ~10-15 min of work
- ROI: ~5-10× per session, scales linearly with session count

The skill pays for itself on the **2nd mission of any session** (the first one re-derives the pattern, every subsequent one is the ritual).

## Anti-patterns to flag (orchestrator failure modes)

- **Skip the ritual because "it's a small change"** — every change compounds. The wiki is the only persistent memory across sessions.
- **Write to log.md but not to MEMORY.md** — log.md is the timeline, MEMORY.md is the index. Both are required (or `MEMORY.md` gets stale and the next session can't find the work).
- **Save a memory file for one-off trivia** — if it's not reusable in 6 months, don't save it. Log.md is the place for one-offs.
- **Edit a past log entry** — log.md is append-only. If you made a mistake, add a correction entry, don't rewrite history.
- **Create a new handoff file when an existing one fits** — append a P_N section to the existing handoff. Multiple handoffs for the same context pollute the index.
- **Skip D1 verify** — if you wrote to log.md, Re-Read it. If you wrote a memory file, Re-Read it. D1 is not optional.

## Related

- [[abc-os-backend-delegation]] — sibling skill. Includes a Step 5 (write-back) that's the ancestor of this whole protocol.
- [[feedback-autonomous-skill-creation]] — doctrine that says this skill fires autonomously at end of session.
- [[project-hostinger-api]] — example of a Step 3 memory file created by this protocol (2026-06-13).
- [[reference-vps-mcp-token]] — example of a Step 3 reference file (2026-06-13).
- [[project-kalybana-dns]] — example of a Step 3 project file (2026-06-13).
