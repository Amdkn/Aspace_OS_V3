---
type: handoff_spec
date: 2026-06-28
author: A0 Jumeau Numérique (sub-agent F6 invocation)
status: SPEC_READY_FOR_P4_GO
posture: C — SPEC ONLY, no execution, no settings.json edit
sister_canon:
  - wiki/hand_offs/l0_mcp_pivots_premortem_live.md
  - wiki/hand_offs/l0_mcp_pivots_premortem_pending_actions.md
target_skill: ~/.claude/skills/l0-watchdog-scrape/SKILL.md
target_surfaces: 4 MCP pivots (Supabase ×3, Vercel ×3, Airtable ×2, ClickUp ×2)
activation_gate: L0 P4 GO (Hermes runtime dry-run) + A0 HITL
coupling: F4 (watchdog cron) ↔ F6 (this spec) — shared cron + shared Donna DLQ
---

# F6 — Wiring Spec for `l0-watchdog-scrape` → 4 MCP Pivots

> **Posture C**: This is a SPEC ONLY. No settings.json edit, no skill mutation,
> no cron create, no MCP restart, no .cmd invocation. The skill manifest at
> `~/.claude/skills/l0-watchdog-scrape/SKILL.md` was read this turn (D1) and
> is referenced faithfully below. P4 activation is the next-step gate.

## 1. D1 receipts (what was verified this turn)

| Path | Verified | Note |
|---|---|---|
| `C:\Users\amado\.claude\skills\l0-watchdog-scrape\SKILL.md` | ✓ Read | 220 lines. Already wired for VPS/Supabase/Vercel via SSH + curl. 4 MCP pivots are an EXTENSION, not a rewrite. |
| `wiki\hand_offs\l0_mcp_pivots_premortem_pending_actions.md` | ✓ Read | 49 lines. F6 entry is lines 30-35. Recommandation = différer à L0 P4 (coupled F4). |
| Sister canon `l0_mcp_pivots_premortem_live.md` | ✓ Glob hit | referenced by pending file, NOT re-read this turn (would require re-loading full canon; trust sister pointer) |
| Skill manifest output path | D1 verified | Skill's canonical output is `wiki/reports/l0_pulse_<YYYY-MM-DD>.md` (line 26, line 122). **NOT** `wiki/hand_offs/`. F6 introduces a SECONDARY artifact (heartbeat) — kept distinct from rollup report. |
| Skill cadence | D1 verified | Lines 199-207: 5m / 15m / on-demand / daily 06:00 / weekly Friday 17:00. F6 piggybacks on F4's 6h cadence — NOT a new cadence. |
| 4 MCP pivots count | D1 verified | 3 Supabase servers + 3 Vercel + 2 Airtable + 2 ClickUp = **10 servers** (per task brief). The skill currently mentions "Supabase, Vercel" (L0 surfaces) but does NOT name Airtable/ClickUp (L2 surfaces). |
| Donna DLQ coupling | D1 verified | Skill manifest references `ADR-RICK-001 (OpenHarness / Donna DLQ)` in line 38 canon refs block. |

## 2. Wiring design (no execution — READ-ONLY spec)

### 2.1 Entry point

- **Skill**: `~/.claude/skills/l0-watchdog-scrape/` (existente, non mutée)
- **Manifest**: `~/.claude/skills/l0-watchdog-scrape/SKILL.md` (220 lines)
- **Invocation pattern**: per skill manifest, the canonical tick cycle is
  `WAKE → PROBE → DECIDE → EXECUTE → OBSERVE → LEARN → SIGNAL → SLEEP`
  (line 33, citing `Shadow_L0/HEARTBEAT_PROTOCOL.md`). F6 piggybacks the
  PROBE step on this cycle.

### 2.2 Target surfaces (the 4 MCP pivots)

| Pivot | Servers | Current skill coverage | F6 addition |
|---|---|---|---|
| **Supabase** | 3 (`supabase`, `supabase-abc`, `supabase-omk`) | ✓ Already covered via SSH+psql (lines 71-100). | Keep CLI batch (per Microsoft README doctrine baked into skill). MCP fallback only if SSH unavailable. |
| **Vercel** | 3 (vercel, vercel-abc, vercel-omk) | ✓ Already covered via REST API + curl (lines 103-114). | Keep curl. MCP fallback only for token introspection. |
| **Airtable** | 2 (airtable + plugin:airtable:airtable) | ✗ Not covered. | Add: `list_bases` ping + `list_tables_for_base` heartbeat on one known base (smoke-test, not full scrape). |
| **ClickUp** | 2 (clickup + ?) | ✗ Not covered. | Add: `get_workspaces` heartbeat + ping one task in `Inbox` state. |

**Total**: 10 MCP servers across 4 pivots. Skill is L0-focused
(VPS/Supabase/Vercel); F6 EXTENDS to L2 (Airtable/ClickUp) — this is the
real novelty of F6.

### 2.3 Invocation vector (per pivot)

The skill manifest at line 50-114 demonstrates the "CLI batch over MCP" doctrine.
F6 follows the same doctrine for the 4 pivots where possible:

```bash
# Supabase pivot — CLI batch preferred (skill manifest §Supabase surface, lines 71-100)
# Per Microsoft README: "CLI invocations are more token-efficient for state-independent Q/A"
# → no MCP call needed for batch scrape; SSH+psql suffices for Supabase.

# Vercel pivot — REST API preferred (skill manifest §Vercel surface, lines 103-114)
# → curl + jq, no MCP call.

# Airtable pivot — MCP ADDITION (NEW in F6)
# mcp__plugin_airtable_airtable__ping   # ← Liveness probe only
# mcp__plugin_airtable_airtable__list_bases   # ← count, no payload

# ClickUp pivot — MCP ADDITION (NEW in F6)
# mcp__clickup__get_workspaces   # ← count only
```

**Doctrine preservation** (per skill manifest anti-patterns, lines 188-197):
- No hot session — 1 process per tick
- CLI > MCP for batch
- D1 evidence paste (no "looks fine")
- No secrets in logs

### 2.4 Schedule trigger (piggyback F4)

F6 does NOT introduce a new cron. It piggybacks on F4's recommended cadence
(per pending actions file, lines 23-28): **6h watchdog cron**.

| Cadence | Source | F6 role |
|---|---|---|
| F4 watchdog 6h | pending_actions F4 Option A | **F6 piggyback** — F4 cron fires, calls `l0-watchdog-scrape`, scrape includes the 4 MCP pivots. |
| Skill's own 5m/15m | `HEARTBEAT_PROTOCOL.md` | Unchanged. F6 is a layer on top, not a replacement. |
| Daily 06:00 | Skill line 206 | Aggregates F6 ping results into the daily buffer. |
| Weekly Friday 17:00 | Skill line 207 | Weekly L0 report. F6 contributes Airtable/ClickUp signal to the rollup. |

**Activation gate for the cron itself** = F4 GO (currently DIFFERÉ à L0 P4,
per pending actions line 28). F6 GO without F4 GO = no fire = safe no-op.

### 2.5 Output paths (two artifacts, kept distinct)

The skill's canonical report path is **`wiki/reports/l0_pulse_<YYYY-MM-DD>.md`**
(skill lines 26 + 122). F6 introduces a SECONDARY artifact for the MCP-specific
heartbeat:

| Artifact | Path | Purpose | Cadence |
|---|---|---|---|
| Full rollup report | `wiki/reports/l0_pulse_<date>.md` | Existing skill output (VPS+Supabase+Vercel) | Per skill (daily/weekly) |
| **F6 heartbeat** | `wiki/hand_offs/l0_heartbeat_<date>.md` | **NEW in F6**: 4-pivot MCP pulse — connection state per server, latency, last-error | Every F4 tick (6h) |
| Donna DLQ entry | Per ADR-RICK-001, OpenHarness DLQ path | Any `✗ Failed` pivot | On failure only |

**D1 nuance note**: Task brief asked for heartbeat at
`wiki/hand_offs/l0_heartbeat_<date>.md`. Skill canonical rollup is at
`wiki/reports/l0_pulse_<date>.md`. F6 uses BOTH paths: rollup for the
existing surface (unchanged), heartbeat for the NEW Airtable/ClickUp signal.
No conflict.

### 2.6 Heartbeat file template (proposed, NOT created)

```markdown
---
type: l0_heartbeat
date: YYYY-MM-DD
tick: F4-6h-<N>
pivots_scraped: [supabase, vercel, airtable, clickup]
---

# L0 Heartbeat — YYYY-MM-DD HH:MM

## TL;DR
<1 line: 10/10 servers Connected | N/10 Failed>

## Supabase pivot
| Server | State | Last error |
|---|---|---|
| supabase | ✓ Connected | — |
| supabase-abc | ✓ Connected | — |
| supabase-omk | ✓ Connected | — |

## Vercel pivot
| Server | State | Last error |
|---|---|---|
| vercel | ✓ Connected | — |
| vercel-abc | ✓ Connected | — |
| vercel-omk | ✓ Connected | — |

## Airtable pivot (NEW in F6)
| Server | State | Last error |
|---|---|---|
| airtable | ✓ Connected | — |
| plugin:airtable:airtable | ✗ Failed | <reason> |

## ClickUp pivot (NEW in F6)
| Server | State | Last error |
|---|---|---|
| clickup | ✓ Connected | — |

## DLQ entries (if any)
<list of pivots in ✗ Failed state, routed to Donna per ADR-RICK-001>

## Next step
<GREEN: no action | YELLOW: N/M failed, log only | RED: escalate F4→A0>
```

### 2.7 Failure modes → escalation

| Failure | Detection | Action |
|---|---|---|
| MCP server `✗ Failed` | Heartbeat reports <N/M> connected | Append to `wiki/hand_offs/l0_heartbeat_<date>.md` + Donna DLQ entry |
| Heartbeat write fails | Catch in skill execution | Donna DLQ entry + retry next tick (6h) |
| F4 cron itself dies | Next F4 tick missed (no DLQ arrival) | Donna DLQ + manual A0 HITL |
| `l0-watchdog-scrape` skill manifest drift | Read manifest hash each tick; compare to expected | DLQ + alert A0 (skill mutation unauthorized without P4) |
| Token redaction violation | grep heartbeat for `Authorization`, `$VERCEL_TOKEN`, etc. | Halt + DLQ + revoke key (Test Key Pragma doctrine) |

### 2.8 Coupling to F4 (shared cron + Donna DLQ)

F4 and F6 are **isomorphic pair**:
- F4 = watchdog cron (ticker)
- F6 = watchdog skill wired to 4 MCP pivots (payload)

Both feed the **same Donna DLQ** (per ADR-RICK-001 OpenHarness Incarnation).
F4 detects MCP-startup failures (post-CC-restart); F6 detects MCP-runtime
failures (between restarts). Together = full MCP lifecycle coverage.

## 3. NOT-executed section (explicit)

This turn created **0** of the following:

| Action | Status | Reason |
|---|---|---|
| Edit `~/.claude/settings.json` | **NOT DONE** | Posture C. F4 GO required first. |
| Edit `~/.claude/skills/l0-watchdog-scrape/SKILL.md` | **NOT DONE** | Skill canon; mutation requires separate ADR. |
| Create cron entry | **NOT DONE** | Posture C. F4 GO required first. |
| Edit `.mcp.json` | **NOT DONE** | Server registry static per D6 #4 (2026-06-23 lesson). CC restart required for any change anyway. |
| Invoke any `mcp__*` tool | **NOT DONE** | Sub-agent scope = spec only. |
| Modify RATIFIED ADRs | **NOT DONE** | Per constraints. |
| Modify F2/F4/F11 entries in pending_actions | **NOT DONE** | Scope = F6 only. |

**Created this turn**: 1 markdown file (this handoff) + 1 annotation edit to
the existing pending_actions file (F6 block only).

## 4. Activation readiness (P4 GO required)

F6 is **READY** for P4 activation when:

1. ✅ Skill `l0-watchdog-scrape` exists with manifest (verified D1)
2. ✅ 4 MCP pivots identified with server counts (3+3+2+2 = 10)
3. ✅ Output paths documented and non-conflicting
4. ✅ Failure modes + DLQ routing documented
5. ✅ Coupling with F4 explicit
6. ⏳ **F4 GO** — watchdog cron must be approved first
7. ⏳ **A0 HITL** — final spec sign-off (this handoff IS the spec — awaiting review)
8. ⏳ **Hermes runtime dry-run** — L0 P4 deferred gate

**Recommendation** (per pending_actions F4 line 28 + F6 line 35):
differ F6 to L0 P4. Same activation window as F4. Posture C preserved.

## 5. Coupling notes

| Coupling | Detail |
|---|---|
| F4 ↔ F6 | Shared cron (6h cadence) + shared Donna DLQ. F4 = ticker; F6 = payload. |
| F2 ↔ F6 | Independent. F2 = Supabase plugin canonical OFF (pending). F6 = scrape custom Supabase MCPs (works regardless). |
| F11 ↔ F6 | F11 = `.mcp.json` rollback script. F6 doesn't modify `.mcp.json`, so F11 not blocking. |
| Donna DLQ | Single shared sink for F4 + F6 failures. Per ADR-RICK-001. |
| L0 P4 gate | Single gate for F4 + F6 activation. Co-ship recommended. |

## 6. Risk register (D6 anti-patterns)

| Risk | Mitigation | Source |
|---|---|---|
| Skill manifest drift between D1 read and P4 activation | Re-verify skill hash at P4 | This handoff §2.7 |
| Token leak in heartbeat (Test Key Pragma violation) | grep heartbeat pre-write + key rotation post-test | Skill manifest line 116-118 |
| Hot session / daemon (violates "1 process per tick") | F6 inherits skill's tick cycle; no deviation | Skill line 36, line 190 |
| Auto-purge old heartbeats (no-hard-delete) | `_TRASH/<date>_l0_heartbeat_*.md` only if > 50 MB | Skill line 197 |
| Airtable/ClickUp MCP failure cascade | One pivot fail ≠ all fail; per-server State field | This handoff §2.6 |
| Missing A0 HITL on cron activation | F4 must GO first, F6 piggybacks | This handoff §4 |

## 7. See also

- `~/.claude/skills/l0-watchdog-scrape/SKILL.md` — skill manifest (read D1)
- `wiki/hand_offs/l0_mcp_pivots_premortem_live.md` — sister live pre-mortem
- `wiki/hand_offs/l0_mcp_pivots_premortem_pending_actions.md` — 4-action queue (this file's sister)
- `Shadow_L0/HEARTBEAT_PROTOCOL.md` — tick cycle canon (per skill manifest §Canon refs)
- `_SPECS/ADR/L1_Life_OS/ADR-RICK-001_*.md` — OpenHarness + Donna DLQ
- `_SPECS/ADR/L1_Life_OS/ADR-META-005_*.md` — Hooks automation (relevant for F4 cron registration)
- `_SPECS/ADR/L1_Life_OS/ADR-META-006_*.md` — D6 root-causes catalog (lesson: MCP server registry static post-CC-restart)

---

**STATUS**: SPEC READY FOR P4 GO.
**D1 receipts**: 1 (skill manifest read).
**Files created**: 1 (this handoff).
**Files modified**: 1 (pending_actions F6 annotation).
**settings.json edits**: 0.
**.mcp.json edits**: 0.
**Skill mutations**: 0.
**Cron creates**: 0.
**RATIFIED ADR edits**: 0.
**Posture**: C preserved.