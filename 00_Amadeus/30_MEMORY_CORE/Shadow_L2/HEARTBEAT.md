---
source: Shadow_L2
date: 2026-05-19
type: heartbeat-tasks
status: DRAFT_DISABLED
layer: L2
executor: Claude_Code_CLI on MiniMax Token Plan
inherits: ./HEARTBEAT_PROTOCOL.md
phase_enabled: false
tags: [#Heartbeat, #ShadowL2, #BusinessPulse, #ClaudeCode, #MiniMax, #Tasks, #Production]
---

# HEARTBEAT.md — Shadow L2 Task Block

> Lu par `heartbeat-tick-l2.ps1`. `phase_enabled: false` jusqu'à supervised run validé.

## Tasks

```yaml
tasks:
  - name: production-health
    interval: 5m
    active_hours: "24/7"
    anomaly_ids: [L2-A01, L2-A11]
    severity: H1
    cooldown_min: 5
    prompt: |
      Probe configured production health endpoints (solaris, omkservices, marina,
      alykaly). HTTP GET, expect 200. Any non-200 → emit L2-A01 with endpoint
      identifier + status code. Persistence > 30min (check pulse history) → L2-A11
      escalation.

  - name: vercel-deployment-failures
    interval: 10m
    active_hours: "24/7"
    anomaly_ids: [L2-A02]
    severity: H10
    cooldown_min: 30
    prompt: |
      Via MCP list_deployments, check last 60min. If any state=ERROR or CANCELED
      on production target → digest entry with project + deployment ID. Suggest
      get_deployment_build_logs for diagnosis (read-only).

  - name: hostinger-vps-pressure
    interval: 15m
    active_hours: "24/7"
    anomaly_ids: [L2-A03, L2-A04]
    severity: H10
    cooldown_min: 30
    prompt: |
      Via MCP VPS_getMetricsV1, check CPU sustained 15m and disk usage. CPU > 85%
      → L2-A03. Disk > 90% → L2-A04. Include VM hostname + metric value.

  - name: airtable-raw-queue-pressure
    interval: 30m
    active_hours: "08:00-20:00"
    anomaly_ids: [L2-A05]
    severity: H30
    cooldown_min: 120
    prompt: |
      For each A'Space marketing base, count "1-Raw" records older than 24h.
      If > 100 → suggest `/airtable-enrich` batch run. Digest only, no auto-run.

  - name: clickup-overdue-watch
    interval: 30m
    active_hours: "08:00-20:00"
    anomaly_ids: [L2-A06]
    severity: H30
    cooldown_min: 120
    prompt: |
      MCP clickup_filter_tasks for due_date_lt=now AND status!=closed.
      If count > 10 → digest entry with top-5 oldest.

  - name: supabase-advisor-watch
    interval: 1h
    active_hours: "24/7"
    anomaly_ids: [L2-A07, L2-A08]
    severity: H1
    cooldown_min: 5
    prompt: |
      MCP get_advisors for security + performance. Any new finding vs last run
      → L2-A07 (security) or L2-A08 (perf). Capture advisor output verbatim.
      Also sample get_logs for error rate vs baseline (rolling 7d).

  - name: minimax-quota-watch
    interval: 1h
    active_hours: "24/7"
    anomaly_ids: [L2-A09]
    severity: H10
    cooldown_min: 60
    prompt: |
      Best-effort estimate of MiniMax request budget remaining (from response
      headers or local counter). If < 10% → alert A0 and suggest temporary
      switch to Anthropic Opus 4.x for critical reasoning sessions.

  - name: margin-shield
    interval: 6h
    active_hours: "24/7"
    anomaly_ids: [L2-A10]
    severity: H30
    cooldown_min: 360
    prompt: |
      Aggregate known cost signals: MiniMax usage estimate, Vercel usage,
      Hostinger billing snapshot. If any > predefined per-service threshold,
      generate margin-shield-YYYY-MM-DD.md digest. Otherwise HEARTBEAT_OK.

  - name: incident-persistence-check
    interval: 5m
    active_hours: "24/7"
    anomaly_ids: [L2-A11]
    severity: H1
    cooldown_min: 5
    prompt: |
      Scan pulse.log last 60min. Any anomaly_id repeated > 6 times (= persistent
      > 30min) → emit L2-A11 escalation. Draft mission card to the relevant
      Squad inbox (e.g. 02_IT_Cyborg for infra, 04_Product_Flash for app).
```

## Round-robin Rule

À chaque tick, exécuter UN check parmi ceux dont `interval` est dû.
Priorité : checks H1 (production-health, supabase-advisor, incident-persistence)
toujours servis avant H10/H30 si concurrents.

## Anti-Spam Safeguard

Si pulse.log montre > 12 `HEARTBEAT_EXEC` consécutifs sans alerte sur la même
minute fenêtre → automatic backoff à 15min interval pendant 1h (probable bruit).

## Inbounds

- `./HEARTBEAT_PROTOCOL.md`
- `./agents/Claude_Code_CLI/Heartbeat.md`
