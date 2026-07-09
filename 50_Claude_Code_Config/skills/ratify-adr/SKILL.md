---
name: ratify-adr
description: >
 Streamlined airlock ratification for A'Space ADRs in `_SPECS/ADR/`. USE THIS SKILL
 whenever the user (A0) wants to: ratify / close / accept a *PROPOSED* ADR, convert
 PROPOSED → ACCEPTED, run the "airlock3-tours" in1 multi-question AskUserQuestion
 call, mark decisions ratified with strikethrough+✅ in the ADR body, write-back
 the4 canonical files (ADR + registry + wiki log + README), or surface the first
 P1.1 blockers of the Validation Plan. Trigger on "ratify the ADR", "close the
 airlock", "accept this ADR", "GO tel quel on ADR-XXX", "ratify ADR-ABCOS-001",
 "passage en ACCEPTED", "ADR ratified by A0", or any PROPOSED ADR being closed.
 Bakes in the4-file write-back contract (immutable ADR, append-only wiki log,
 registry index, README bullet), Doctrine Anti-Paresse (D1-D8), Test Key Pragma
 (never paste keys in output), No-Hard-Delete (always _TRASH), and HITL gates on
 destructive ops. ADR canon lives at `_SPECS/ADR/` and is immutable — this skill
 EDITS the ADR frontmatter/body, never the canonical Decision section.
when_to_use: |
 - User says "ratify this ADR", "accept this ADR", "close the airlock", "GO on ADR-XXX"
 - A *PROPOSED* ADR exists at `_SPECS/ADR/ADR-XXX_*.md` with `status: PROPOSED`
 in frontmatter AND a "Décisions à arbitrer" / "Décisions arbitrées" / "Tour3"
 / "Veto Review" section with multiple sub-decisions
 - The airlock3-tours has already been run in conversation (Tour1 clarification,
 Tour2 organization, Tour3 awaiting A0 GO/VETO/MODIFY)
 - User explicitly says "GO tel quel", "VETO sur X", "MODIFY Y", or any close-out
 verdict per sub-decision
inputs: |
1. Absolute path to a `*PROPOSED*.md` ADR under `_SPECS/ADR/`
2. Implicit: A0's verdict from the conversation context (already-expressed GO/VETO/MODIFY
 per sub-decision). If verdict is unclear, STOP and re-ask via AskUserQuestion (HITL).
outputs: |
1. Edited ADR — `status: PROPOSED` → `ACCEPTED`, `ratified_by` frontmatter added,
 "Décisions à arbitrer" → "Décisions arbitrées par A0", strikethrough ~~d~~ + ✅
 annotation on ratified sub-decisions,3 Validation Plan boxes checked.
2. Updated registry (e.g. `_SPECS/REGISTRY/supabase_schemas.md`) with the new
 entity/schema/decision flagged as ACCEPTED.
3. Appended wiki log entry at `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md`
 in canonical format `- **YYYY-MM-DD** : ✅ **<ADR-ID> ACCEPTED — <title>** : ...`.
4. Appended bullet at `00_Amadeus/30_MEMORY_CORE/README.md` (same date).
5. Next-step surface: first P1.1 blockers +2-4 path options for A0 to pick.
---

# /ratify-adr — streamlined airlock ratification

> **Doctrine** : ADR canon is immutable once created. This skill edits `status`,
> `ratified_by`, the "Décisions arbitrées" section, and Validation Plan checkboxes —
> **NEVER** the Decision section. New decisions spawn new ADRs (Rule #3).
>
> **Canon refs** : `00_Amadeus/01_Identity_Core/AGENTS.md` · `ADR-META-001` ·
> Test Key Pragma · No-Hard-Delete.

## When to trigger

| Signal | Action |
|---|---|
| `*PROPOSED*.md` ADR + A0 verdict in chat | Run the5 steps below |
| ADR has no `status: PROPOSED` in frontmatter | STOP — already ACCEPTED or REJECTED. Reject this skill call. |
| ADR has no "Décisions à arbitrer" / "Tour3" section | Refuse — cannot streamline what doesn't exist. Run classical3-tours first. |
| A0 verdict is ambiguous ("hmm" / "maybe" / silence) | STOP — re-ask via AskUserQuestion before any write. |
| Multiple *PROPOSED* ADRs in `_SPECS/ADR/` | Ratify one at a time. Never batch — airlock is per-ADR. |

## The5-step contract

### Step1 — Extract airlock questions

Parse the ADR's "Décisions à arbitrer" (or equivalent Tour3 / Veto Review) section. Build a question list for one multi-question AskUserQuestion call:

| Slot | Source | Cardinality |
|---|---|---|
| Q1 (always first) | "Ratifier l'ADR entier tel quel?" — header-level ratification | exactly1 |
| Q2..QN | Each sub-decision in the section |1-3 (cap =4 questions total per AskUserQuestion call) |

Rules:
- **Q1 first, sub-decisions follow** — A0 ratifies the WHOLE first, then arbitrates each lever.
- **Max4 questions** — AskUserQuestion hard cap. If more sub-decisions exist, surface
 the top3 by impact (later ones auto-default to "non contesté" per airlock doctrine).
- **Each question gets2-4 options** — typically `GO (tel quel)` / `MODIFY (with note)` /
 `VETO (reject)`. MultiSelect=false (one verdict per question).
- **Header carries options length (1-5 chars)** — keep option labels terse.

If the ADR's section is missing or malformed, STOP. Do not invent sub-decisions.

### Step2 — Streamlined airlock (1 AskUserQuestion call)

```python
AskUserQuestion(
 questions=[
 {"question": "Ratifier ADR-XXX-001 (title)?", "header": "ADR-XXX", "options": [...], "multiSelect": False},
 {"question": "Sub-decision #1 (verbatim from ADR)?", "header": "D1", "options": [...], "multiSelect": False},
 {"question": "Sub-decision #2?", "header": "D2", "options": [...], "multiSelect": False},
 {"question": "Sub-decision #3?", "header": "D3", "options": [...], "multiSelect": False},
 ]
)
```

A0 returns one verdict per question. Capture the responses. **If A0 already expressed
GO/VETO/MODIFY verbatim in chat**, you may skip this step — but DO still surface the
final close-out summary in Step5 (anti-paresse D1: never assume).

### Step3 — Write-back (4 files,2 parallelizable batches)

| Batch | File | Action | Parallel? |
|---|---|---|---|
| **Batch1** | `<ADR-path>` | Edit frontmatter (status, ratified_by) + body (Décisions arbitrées, Validation Plan boxes) | YES — with Batch2 |
| **Batch2** | `_SPECS/REGISTRY/<relevant>.md` | Add row/flag for the new entity (status = ACCEPTED) | YES — with Batch1 |
| **Batch3** | `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` | Prepend `- **YYYY-MM-DD** : ✅ **<ADR-ID> ACCEPTED — <title>** : …` (append-only, top of section) | NO — depends on Batch1 |
| **Batch4** | `00_Amadeus/30_MEMORY_CORE/README.md` | Append bullet same date | NO — depends on Batch3 |

**Within Batch1, edits to the ADR are themselves parallelizable as2 sub-batches:**
- Sub-batch1A: Edit frontmatter (status, ratified_by).
- Sub-batch1B: Edit body ("Décisions à arbitrer" → "Décisions arbitrées par A0"
 with strikethrough + ✅ per ratified sub-decision,3 Validation Plan boxes checked).

**ADR edit contract (immutable canon respected):**

| Field / section | Before | After |
|---|---|---|
| Frontmatter `status` | `PROPOSED` | `ACCEPTED` |
| Frontmatter `ratified_by` | (absent) | `A0 Amadeus (airlock clos YYYY-MM-DD — <verdict_summary>)` |
| Body "Status" block | (open) | `**ACCEPTED** — YYYY-MM-DD. Airlock clos : <verdict summary>` |
| Body sub-decisions | `1. **Decision text**` | `1. ~~**Decision text**~~ : ✅ ratified with value = <chosen option>` |
| Body Validation Plan | `[] item` | `[x] item` for the3 ratification boxes (A0 ratifies, domain arrêté, JWT/impl arrêté) |

**Never edit** : `Context`, `Decision`, `Consequences`, `Related`, `Domain`, `Tags`.
If you find yourself needing to, STOP — that means the ADR was wrongly drafted, not
that it needs silent mutation.

### Step4 — Surface next step

Parse the ADR's `## Validation Plan` section. Identify the **first unchecked box
in the implementation phases (P1.1 typically)**. Surface:

```
First P1.1 blockers of <ADR-ID>:
- <blocker1 verbatim>
- <blocker2 verbatim>
- <blocker3 verbatim>

Path options to clear P1.1 (pick one):
A. <Option A — typically: implement blocker via leaf skill X>
B. <Option B — typically: delegate to A3 sub-agent Y>
C. <Option C — typically: HITL-gated VPS SSH one-shot>
D. <Option D — typically: defer to Phase1.2>
```

A0 picks the path. Do NOT auto-execute any option — always HITL on next-step.

### Step5 — Doctrine compliance check

Before declaring done, verify (D5 — proof, not assertion):

| Check | Verified how |
|---|---|
| ADR `status` = `ACCEPTED` | `grep "^status:" <ADR-path>` |
| `ratified_by` populated | `grep "^ratified_by:" <ADR-path>` |
| Registry updated | `grep "<ADR-ID>" <registry-path>` |
| Wiki log entry present | `grep "<ADR-ID> ACCEPTED" wiki/log.md` |
| README bullet added | `grep "<ADR-ID>"30_MEMORY_CORE/README.md` |
| No keys/secrets pasted | scan all4 files for `api[_-]?key|password|token|secret` +16+ chars |
| Original *PROPOSED* version backed up | `_SPECS/ADR/_TRASH/<ADR-ID>_<date>_before-acceptance.md` (if any structural edits risk loss) |

If any check fails, STOP. Report the gap to A0. Do not declare done.

## Frontmatter contract

Every ADR ratified via this skill must have these6 fields populated:

```yaml
---
id: ADR-XXX-NNN
title: <short, scannable>
status: ACCEPTED # was PROPOSED
date: YYYY-MM-DD # ratification date (may = original date)
ratified_by: A0 Amadeus (airlock clos YYYY-MM-DD — <verdict summary>)
proposed_by: <agent + session>
---
```

`ratified_by` is the **only** new field. Everything else is unchanged.

## Output format (final report to A0)

```
=== ADR-XXX-NNN RATIFIED ===

ADR: <absolute path>
Status: PROPOSED → ACCEPTED
Date: YYYY-MM-DD
Verdict: <summary of Q1 + sub-decisions>

Write-back:
[x] ADR frontmatter + body edited
[x] <registry-path> updated
[x] wiki/log.md entry appended
[x] 30_MEMORY_CORE/README.md bullet added
[x] Doctrine compliance (6/6)

First P1.1 blocker: <verbatim>
Path options: A | B | C | D
Your pick?
```

## Constraints

| Constraint | Enforcement |
|---|---|
| One ADR per invocation | Refuse multi-ADR batch (airlock is per-ADR). |
| Max4 AskUserQuestion slots | If section has >3 sub-decisions, surface top-3 by impact + default rest. |
| No silent Decision section edits | If the canonical Decision needs revision, spawn a NEW ADR (supersedes relationship). |
| No secrets in any output | Scan before each Write — Test Key Pragma is absolute. |
| No hard-delete | If backing up the *PROPOSED* version, move to `_TRASH/`, never `Remove-Item`. |
| Append-only wiki log | Never re-order or rewrite entries. Only prepend today's. |

## See also

- `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md` — D1-D8 binds all agents.
- `00_Amadeus/01_Identity_Core/AGENTS.md` —3-turn airlock doctrine (this skill compresses
 it to1 call, not replaces it).
- `/mcp-mastery` — if ratification triggers a Vault/Supabase/Vercel side-effect.
- `/picard-repo-home` — if ratification unblocks a build-bearing repo migration.
- `_SPECS/ADR/` — full ADR canon. Read1-2 existing ACCEPTED ADRs to mirror style.

---

## Anti-patterns (do NOT)

| Anti-pattern | Why it's bad | What to do instead |
|---|---|---|
| Multi-ADR batch ratification | Airlock is per-ADR; each has its own blast radius | Ratify one at a time |
| Edit the canonical Decision section to "fix" a sub-decision | Violates immutability (Rule #3) | Spawn a new ADR with `supersedes:` field |
| Skip the AskUserQuestion and assume A0's verdict | D1 (Anti-Paresse) — never infer GO from silence | Always surface the call, even if verdict is "obvious" |
| Paste the anon key or service role in chat to "prove" the ratification | Test Key Pragma violation — keys live in env vars only | Cite the verification command, don't paste the secret |
| Rewrite wiki log entries to "clean up" format | Append-only contract — log is the canonical memory | Prepend today's entry; never reorder |
| Move a *REJECTED* or *WITHDRAWN* ADR to `_TRASH` without backup | No-Hard-Delete doctrine — even rejected canon has audit value | Move to `_TRASH/` with the verdict in the filename |
| Surface the next-step blockers and auto-execute option A | Violates HITL — agent never picks the path for A0 | Surface2-4 options, wait for A0 pick |
| Treat `status: ACCEPTED` as a license to skip future validation | Validation Plan boxes still need to be checked off incrementally | Edit only the3 ratification boxes; leave impl boxes unchecked |
| Use Bash sed/awk to bulk-edit ADRs | Loses YAML semantics + audit trail | Use Edit tool with exact `old_string` per file |
| Ratify when `status:` is already `ACCEPTED` | Idempotency bug — re-ratifying corrupts the log | STOP, report "already ratified", point to ratification date |
