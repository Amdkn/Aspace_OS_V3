---
target: F4 — Watchdog MCP-dédié (cron 6h scrapant ✗ Failed)
date: 2026-06-28
author: A0 jumeau numérique (Opus) — sub-agent F4 spec writer
spec_status: READY_FOR_P4_GO — **NOT executed this turn** (Posture C strict)
related_canon:
  - l0_mcp_pivots_premortem_live.md (F4 = A0_GO_REQUIRED, sister)
  - l0_mcp_pivots_premortem_pending_actions.md (F4 queue entry)
  - ADR-META-005_hooks-automation.md (Hook 1 + Hook 4 VETO Rick, scope doctrine)
  - ADR-SOBER-002 (anti-paperclip — no A1→B1 cron without A0 HITL)
  - .claude/mindsets/Rick_Mindset.md (S1 sobriety kernel)
  - .claude/mindsets/Donna_DLQ.md (L0 dead letter queue canon, 14 capsules dormant)
  - skill canon: `~/.claude/skills/l0-watchdog-scrape/SKILL.md` (F6 sister, not wired)
  - ADR-META-006_d6-root-causes-catalog.md (D6 #1 airtable/clickup post-CC-restart 2026-06-23)
sister_specs:
  - F6 = heartbeat skill `l0-watchdog-scrape` wiring spec (DEFERRED, coupled activation)
activation_gate: P4 GO from A0 required (Hermes runtime dry-run + watchdog live)
auto_refresh: re-spec on D6 #N entry linking to F4 OR on F6 spec land
---

# F4 — MCP Watchdog Spec (Read-Only, NOT Executed)

## 0. Mission (1 line)

Scrape les 10 serveurs MCP actifs de `.mcp.json` toutes les 6h, capturer tout
`✗ Failed` runtime, route vers Donna DLQ et alerte A0 au **prochain** SessionStart
digest (pas de push — Posture C).

## 1. Posture C — Strict Execution Constraints

| Constraint | Status |
|---|---|
| Cron created this turn | ❌ **NO** |
| `~/.claude/settings.json` edited | ❌ **NO** |
| `.mcp.json` edited | ❌ **NO** |
| `~/.claude-server-commander-logs/` scraped | ❌ **NO** (manual probe deferred to P4 GO) |
| Actual MCP probe run | ❌ **NO** |
| Spec written (this file) | ✅ yes |
| Pending-actions annotation (D4) | ✅ yes (sister file updated) |

**Rationale** : Anti-paperclip per ADR-SOBER-002 + Rick S1 sobriety doctrine.
No A1→B1 cron crosses the gate without explicit A0 HITL per cron. The P4
activation ceremony is the gate — this spec IS the gate artifact.

## 2. Design Spec (Read-Only)

### 2.1 Cadence

- **Every 6h** (00:00 / 06:00 / 12:00 / 18:00 local + user's TZ America/New_York)
- **Heartbeat anchor** : aligns with Shadow L0 `HEARTBEAT_PROTOCOL.md` tick
  cycle (WAKE→PROBE→DECIDE→EXECUTE→OBSERVE→LEARN→SIGNAL→SLEEP).
- **No daemon** : 1 process per tick (per `l0-watchdog-scrape` doctrine).
- **No hot session** : cron spawns, runs, exits. No long-lived background.

### 2.2 Probe Surface (10 MCP servers from `.mcp.json`)

| Family | Server name | Probe method |
|---|---|---|
| Supabase | `supabase` | JSON-RPC `tools/list` ping + project liveness |
| Supabase | `supabase-omk` | JSON-RPC `tools/list` ping + project liveness |
| Supabase | `supabase-abc` | JSON-RPC `tools/list` ping + project liveness |
| Vercel | `vercel` | JSON-RPC `tools/list` ping + token scope |
| Vercel | `vercel-omk` | JSON-RPC `tools/list` ping + token scope |
| Vercel | `vercel-abc` | JSON-RPC `tools/list` ping + token scope |
| Airtable | `airtable` | JSON-RPC `tools/list` ping + base access |
| Airtable | `plugin_airtable_airtable` | JSON-RPC `tools/list` ping + base access |
| ClickUp | `clickup` | JSON-RPC `tools/list` ping + workspace access |
| ClickUp | `2c79bb4b-...-clickup` | JSON-RPC `tools/list` ping + workspace access |

**Probe standard** : for each server, fire a `{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}`
JSON-RPC envelope with a **3-second timeout**. Capture response status code +
`✗ Failed` substring in any text field.

### 2.3 Failure Capture Logic

```
for each mcp_server in .mcp.json:
    response = probe(server, timeout=3000ms)
    if response.status == "✗ Failed" or response.error:
        append_to_dlq(server_name, response.error, ts)
        flag_for_next_session_digest(server_name, response.error)
```

### 2.4 DLQ Target — Donna DLQ (L0 canonical)

- **Path** : `~/.hermes/disposition.md` → append-only line per failure
- **Format** :
  ```
  2026-06-28T18:00:00-04:00 | F4-WATCHDOG | <server_name> | <error_snippet> | retry_count=N
  ```
- **DLQ doctrine** : `Donna_DLQ.md` — Dead Letter Queue is **inspection-only**
  on M3 (no auto-retry). A0 reviews at SessionStart. Retry decision is human.
- **Capsules** : linked to L0_A1_Rick canon (14 dormant capsules — F4 failures
  become capsule #15 if persistent).

### 2.5 HITL Channel — NOT Push

- **NO Telegram push** (per Telegram HITL canon 2026-06-25 = artefacts
  différés, MCP `✗ Failed`, **DORMANT** until 4 gates pending close).
- **NO SAPI TTS** (per TTS doctrine — `feedback_tts_and_communication.md`,
  SAPI Hortense reserved for `Stop` hook, not watchdog).
- **Channel** : SessionStart digest captures DLQ new lines + the most-recent
  per-server status, surfaces as a `F4-WATCHDOG REPORT` section in the digest.

### 2.6 Idempotency

- **State file** : `~/.hermes/watchdog_state.json` (per-server last-seen-status,
  last-probe-ts). Lives next to disposition.md. NOT in `.mcp.json`.
- **Dedupe** : only append to DLQ if status CHANGED since last tick (delta-only).
  Reduces DLQ noise from 6h-flapping servers.

## 3. NOT-Executed Section (explicit)

This spec handoff writes **ONLY** canon artifacts. The following are
**deferred to P4 activation ceremony** (after A0 GO):

1. Cron creation (Windows Task Scheduler OR WSL systemd timer OR Hermes
   scheduler — TBD at P4, not now).
2. Probe script authoring (PowerShell or Python — TBD at P4).
3. State file initialization (`~/.hermes/watchdog_state.json`).
4. DLQ directory creation (`~/.hermes/disposition.md` parent).
5. First actual probe of any MCP server.
6. Hooks wiring (e.g., adding watchdog probe to `hooks.SessionStart` chain —
   F6 territory, sister-coupled).

**0 cron created this turn. 0 settings.json edit. 0 .mcp.json edit.**

## 4. Activation Readiness — P4 GO from A0 Required

### Pre-conditions for P4 ceremony

- [ ] A0 reads this spec, signs off on cadence + DLQ + HITL choices
- [ ] A0 chooses execution substrate (Task Scheduler / WSL systemd / Hermes)
- [ ] F6 sister spec lands (heartbeat skill `l0-watchdog-scrape` wiring) OR
  A0 accepts F4 standalone without F6
- [ ] D6 catalog has a new entry `D6 #N — F4-WATCHDOG first run` reserved
- [ ] A0 picks timezone for 6h ticks (ET recommended, matches A0 location)

### What P4 ceremony produces

1. The cron (or equivalent) is **created** with Posture C disclaimer
2. First probe runs, results captured in DLQ
3. D6 catalog entry lands with P4 GO timestamp + first probe receipts
4. Pending-actions F4 entry flips from `A0_GO_REQUIRED` → `LIVE`
5. Sister canon `l0_mcp_pivots_premortem_live.md` §"F4 Status" updates

### Coupled to F6 (sister)

F4 (watchdog cron) and F6 (heartbeat skill wiring) are complementary:
- F4 = continuous 6h pulse
- F6 = SessionStart digest enrichment (richer F4 context at session open)

A0 may approve F4 alone (minimum useful), F6 alone (less useful without F4),
or both together (full Surface). Spec recommends **F4 first, F6 follow-on
1-2 weeks later** to validate cadence.

## 5. Limitations & Open Risks

### 5.1 Cron Windows vs WSL vs Hermes

3 substrate candidates, none yet chosen:

| Substrate | Pros | Cons |
|---|---|---|
| Windows Task Scheduler | Native, already installed | No logs in `~/.hermes/`, separate audit trail |
| WSL systemd timer | Linux-native, integrates with `~/.hermes/` | WSL service flakiness (D6 known) |
| Hermes scheduler | Native to runtime, single audit | Requires Hermes always-up (anti-fragility risk) |

**Recommendation** : WSL systemd (middle path) — **subject to P4 A0 decision**.

### 5.2 JSON-RPC Variant Per MCP

MCP servers may use:
- **stdio** (most common — `.cmd` binary spawning)
- **SSE** (Server-Sent Events, streamable HTTP)
- **streamable-http** (HTTP chunked)
- **OAuth-discovery** (the 2026-06-21 D6 #4 lesson — `mcp-remote@latest` hang)

The probe must handle all 4. **Implementation deferred to P4** — 1-line
rejection on unhandled variant = safe-fail (logged to DLQ, no crash).

### 5.3 False-positive Risk

6h cadence on flapping servers = DLQ noise. Mitigation :
- **Status-change dedupe** (2.6 above) — only DLQ on delta
- **3-strikes rule** : 3 consecutive failed probes = persistent failure (capsule
  candidate), < 3 = transient noise (DLQ only, no capsule)
- **Configurable threshold** (P4 A0 decides default = 3)

### 5.4 Cost

- ~10 HTTP probes × 3s timeout × 4 ticks/day = **120s compute/day** ≈ 0.3%
  of daily CC quota. Negligible. **D7 cost-of-escalation satisfied** — this
  cron is cheaper than the A0 escalation it prevents.

## 6. Sister Links & Anti-Amnesia

- **Sister live** : `l0_mcp_pivots_premortem_live.md` §F4 = A0_GO_REQUIRED
- **Sister queue** : `l0_mcp_pivots_premortem_pending_actions.md` (annotation
  added this turn per D4 append-only)
- **Sister canon** : `Donna_DLQ.md` (14 capsules dormant, F4 → capsule #15)
- **Sister spec** : F6 heartbeat skill wiring (DEFERRED, coupled)
- **Doctrine** : `Rick_Mindset.md` (S1 sobriety) + `ADR-SOBER-002` (anti-paperclip)

## 7. D1 Receipt (spec write verification)

- **Spec file created** : `mcp_watchdog_spec_2026-06-28.md` — 1 file
- **Sister updated** : `l0_mcp_pivots_premortem_pending_actions.md` — 1
  annotation appended under F4 section (D4 append-only)
- **Cron count** : 0
- **Settings.json edits** : 0
- **`.mcp.json` edits** : 0
- **Actual MCP probes** : 0
- **DO NOT edit RATIFIED ADRs** : respected — no `_SPECS/ADR/L0_Tech_OS/` or
  `_SPECS/ADR/L1_Life_OS/` file modified this turn

## 8. Next Run Triggers

Re-spec (or re-invoke this spec handoff as reference) when:
- A0 opens P4 ceremony
- F6 spec lands (link sister reference)
- New MCP server added to `.mcp.json` (extend probe surface table §2.2)
- D6 catalog entry linking to F4 (update §"Anti-amnesia")
- A0 changes posture (e.g., allows push-notify → revise §2.5 HITL channel)

---

**END OF SPEC — READY FOR P4 A0 GO**
