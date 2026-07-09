---
name: l0-watchdog-scrape
description: >
  Batch watchdog scrape across all L0 surfaces (VPS, Supabase, Vercel) for the
  Shadow L0 heartbeat pulse. USE THIS SKILL whenever the user (A0) wants to:
  generate the weekly L0 health report, scrape 5m-tick data, detect drift in
  infra metrics, dump container status / disk usage / DB connection counts /
  Supabase replication lag, or run a "Friday L0 review". Bakes in CLI batch
  preference over MCP (per Microsoft README — "CLI invocations are more
  token-efficient" for state-independent Q/A), the WAKE→PROBE→DECIDE→EXECUTE→
  OBSERVE→LEARN→SIGNAL→SLEEP tick cycle from `HEARTBEAT_PROTOCOL.md`, no daemon
  (1 process per tick — no hot session), 5m/15m/on-demand cadence awareness,
  D1 proof (paste exact output, not "looks fine"), no secrets in any log
  (variable names only, never values), and `_TRASH/` for old logs. ROI: ~70
  min/sem saved vs manual check.
when_to_use: |
  - User says "weekly L0 report", "watchdog scrape", "infra pulse", "Friday review"
  - A tick fires on the 5m/15m cadence and the agent needs the rollup view
  - A0 wants to compare this week vs last week (drift detection)
  - A0 suspects something is slow / failing and wants evidence across all L0
inputs: |
  1. Time window (default: last 7 days for weekly; last 24h for daily)
  2. Surfaces to include (default: all — VPS, Supabase, Vercel; A0 can subset)
  3. Optional: comparison baseline (e.g. "compare to 2026-06-04 weekly report")
outputs: |
  1. 1 markdown report at `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/reports/l0_pulse_<date>.md`
  2. Append 1 line to `wiki/log.md` with the report path
  3. If anomalies detected, surface a 1-paragraph "anomalies" section for A0
---

# /l0-watchdog-scrape — Batch L0 health rollup

> **Doctrine** : Shadow L0 is tick-driven and ephemeral. 1 process per tick,
> no daemon. CLI > MCP for batch Q/A. Tick cycle = WAKE→PROBE→DECIDE→EXECUTE→
> OBSERVE→LEARN→SIGNAL→SLEEP.
>
> **Canon refs** : `Shadow_L0/HEARTBEAT_PROTOCOL.md` · `Shadow_L0/WORKFLOW.md` ·
> ADR-META-001 · ADR-RICK-001 (OpenHarness / Donna DLQ).

## When to trigger

| Signal | Action |
|---|---|
| Scheduled tick (5m watchdog / 15m inbox scan) | Roll up the tick data into the daily buffer |
| A0 says "Friday L0 review" or "weekly infra" | Generate the weekly report |
| A0 asks "is the prod healthy?" | Generate the ad-hoc full surface scrape |
| A0 wants to compare two weeks | Run twice (this week + last week), diff in the report |
| A0 wants to investigate a specific symptom | Switch to `/l0-deploy-verify` (interactive) — this skill is batch, not debug |

## CLI batch — the canonical commands

### VPS surface (ssh aspace-vps)

```bash
# Container status (which services are up, restart count)
ssh aspace-vps "docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'"

# Disk usage
ssh aspace-vps "df -h / /srv /var/lib/docker 2>/dev/null | grep -v tmpfs"

# Memory + load average
ssh aspace-vps "free -h && uptime"

# Top 5 CPU consumers
ssh aspace-vps "ps -eo pid,pcpu,pmem,comm --sort=-pcpu | head -6"

# Last 50 lines of watchdog log (if any)
ssh aspace-vps "tail -50 /var/log/aspace-watchdog.log 2>/dev/null || echo 'no watchdog log'"
```

### Supabase surface (psql via docker exec)

```bash
# DB size + connection count
ssh aspace-vps "docker exec supabase-db psql -U postgres -d postgres -c \"
SELECT pg_size_pretty(sum(pg_database_size(oid))) AS total_db_size
FROM pg_database WHERE datname IN ('postgres', 'abc_os');
SELECT count(*) AS active_connections, state FROM pg_stat_activity GROUP BY state;
\""

# Replication lag (self-hosted = usually 0)
ssh aspace-vps "docker exec supabase-db psql -U postgres -d postgres -c \"
SELECT client_addr, state, sent_lsn, replay_lsn,
       (sent_lsn - replay_lsn) AS byte_lag
FROM pg_stat_replication;
\""

# Slowest queries (top 5 from pg_stat_statements)
ssh aspace-vps "docker exec supabase-db psql -U postgres -d postgres -c \"
SELECT substring(query, 1, 80) AS query, calls, mean_exec_time
FROM pg_stat_statements
ORDER BY mean_exec_time DESC LIMIT 5;
\""

# RLS-protected tables count
ssh aspace-vps "docker exec supabase-db psql -U postgres -d postgres -c \"
SELECT schemaname, count(*) AS tables, sum(CASE WHEN rowsecurity THEN 1 ELSE 0 END) AS rls_on
FROM pg_tables WHERE schemaname IN ('abc_os', 'l2_mesh', 'public') GROUP BY schemaname;
\""
```

### Vercel surface (REST API)

```bash
# Last 10 deployments
curl -sS -H "Authorization: Bearer $VERCEL_TOKEN" \
  "https://api.vercel.com/v6/deployments?projectId=prj_HSw4IBR2omI5qegmEinOksr6xzo0&limit=10" \
  | jq '.deployments[] | {uid, state, createdAt, target}'

# Env var count per scope
curl -sS -H "Authorization: Bearer $VERCEL_TOKEN" \
  "https://api.vercel.com/v9/projects/prj_HSw4IBR2omI5qegmEinOksr6xzo0/env" \
  | jq '.envs | group_by(.key) | map({key: .[0].key, scopes: [.[].target]})'
```

**Secret handling** : `VERCEL_TOKEN` is in `User` env scope. Never echo it
back. Use `jq` to filter output and never include `Authorization` headers in
saved reports.

## Report structure (1 file per run)

Path: `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/reports/l0_pulse_<YYYY-MM-DD>.md`

```markdown
---
report_type: l0_pulse
date: YYYY-MM-DD
window: last_7d | last_24h | ad_hoc
surfaces_scraped: [vps, supabase, vercel]
agent: <session id>
---

# L0 Pulse — YYYY-MM-DD

## TL;DR

<1-3 bullets: GREEN | YELLOW | RED, with the top 1-2 anomalies if any>

## VPS

### Containers

| Name | Status | Ports | Uptime |
|---|---|---|---|
| <paste from docker ps> |

### Resources

- Disk: <df -h output>
- Memory: <free -h output>
- Load: <uptime output>
- Top 5 CPU: <ps output>

## Supabase

### DB health

- Total size: <pg_size_pretty>
- Connections: <active/idle counts>
- Replication lag: <bytes>
- Slowest queries: <top 5>
- RLS coverage: <table counts>

## Vercel

### Deployments (last 10)

| UID | State | Created | Target |
|---|---|---|---|
| <paste> |

### Env var coverage

| Key | dev | preview | production |
|---|---|---|---|
| <from jq> |

## Anomalies (if any)

<1 paragraph: what's different from last week, what to investigate>

## Next step

<1-2 sentences: e.g. "All GREEN. No action needed." or "Supabase connections at 80/100 — consider PgBouncer. Escalate to A0.">
```

## Anti-patterns (do NOT)

| Anti-pattern | Why | Fix |
|---|---|---|
| Keep a hot session running for 30 min to "watch" infra | Violates "1 process per tick, no daemon" | Run, dump, exit. Re-tick in 5 min. |
| Use Playwright MCP for a curl-able REST endpoint | Token waste; MCP = interactive only | Use `curl` + `jq` |
| Echo the full Vercel token in the report | Test Key Pragma violation | Use `$VERCEL_TOKEN` env var, redact any echoed header |
| Roll a single 7-day query instead of daily ticks | Loses granularity, harder to diff | Save daily, roll up at week end |
| Mark "GREEN" without pasting the output | D1 violation — assertion ≠ evidence | Paste `docker ps`, `df -h`, `pg_stat_*` verbatim |
| Skip the diff vs last week | Drift hides in plain sight | Always run a second pass with last week's path |
| Auto-purge old reports | No-Hard-Delete doctrine | Move to `_TRASH/<date>_` if size > 50 MB |

## Tick cadence (from `HEARTBEAT_PROTOCOL.md`)

| Cadence | Use case | This skill's role |
|---|---|---|
| `every 5m always` | Watchdog tick | Aggregate to daily buffer (not full report) |
| `every 15m work-hours` | Mon-Fri 09-19 | Aggregate to daily buffer |
| `on-demand` | A0 explicit | Full report, full format |
| `daily 06:00` | Memory consolidation | Save yesterday's daily buffer as `l0_pulse_<date>.md` |
| `weekly Friday 17:00` | Weekly review | Save weekly rollup as `l0_pulse_week_<date>.md` |

**Critical** : this skill is the BATCH half. For interactive debug (a single
container won't start, a specific env var is missing), use `/l0-deploy-verify`
or `/aspace-supabase-mastery` instead.

## See also

- `Shadow_L0/HEARTBEAT_PROTOCOL.md` — full tick cycle + cadence table
- `/l0-deploy-verify` — interactive gate (single deploy, single surface)
- `/aspace-supabase-mastery` — deep Supabase queries (migrations, RLS, schema)
- `/vercel-deploy-from-github` — the deploy side
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/reports/` — where reports accumulate
