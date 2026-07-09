---
source: Shadow_L1
date: 2026-05-19
type: heartbeat-tasks
status: DRAFT_DISABLED
layer: L1
executor: Claude_Code_CLI on MiniMax Token Plan
inherits: ./HEARTBEAT_PROTOCOL.md
phase_enabled: false
tags: [#Heartbeat, #ShadowL1, #LifeOS, #ClaudeCode, #MiniMax, #Tasks]
---

# HEARTBEAT.md — Shadow L1 Task Block

> Lu à chaque tick par `heartbeat-tick-l1.ps1`. Détermine quels checks sont dus.
> `phase_enabled: false` = aucun tick ne s'exécute tant que A0 n'a pas validé la
> readiness gate finale dans `HEARTBEAT_PROTOCOL.md §12`.

## Tasks

```yaml
tasks:
  - name: life-os-scorecard-gap
    interval: 2h
    active_hours: "07:00-22:00"
    anomaly_ids: [L1-A01, L1-A02]
    prompt: |
      Read Baserow Life OS tables: LD02_Rocks, LD03_Tactiques_W1_W4, LD04_Scorecard.
      Detect Rocks active without tactics AND tactics without scorecard rows.
      If gap detected, append to A0_inbox/anomalies-YYYY-MM-DD.md (max 1 entry/day).
      Otherwise emit HEARTBEAT_OK.

  - name: plane-sync-gap
    interval: 4h
    active_hours: "07:00-22:00"
    anomaly_ids: [L1-A04]
    requires_source_ready: plane_workspace
    prompt: |
      If Plane API responds 200 (currently 403 — skip), compare Baserow active
      tactics vs Plane work-items. Alert only on missing operational tickets.
      If Plane unreachable: HEARTBEAT_OK silently (already known blocker).

  - name: sunday-review-prep
    interval: 24h
    active_hours: "06:30-09:00"
    anomaly_ids: [L1-A07]
    prompt: |
      If today.weekday in [Saturday, Sunday-06:30..09:00]: generate
      outbox/sunday-review-prep-YYYY-MM-DD.md with checklist:
        - LD04 Scorecard W{current} review
        - Rocks status H1/H10/H30
        - Tactiques closed vs opened delta
        - Time Use coverage gaps
      Otherwise HEARTBEAT_OK.

  - name: cognitive-load-watch
    interval: 6h
    active_hours: "07:00-22:00"
    anomaly_ids: [L1-A06]
    prompt: |
      Count open tactics in LD03 status=ACTIVE. If > 12, append cognitive
      overload alert to A0_inbox. Suggest top-3 deprioritization candidates
      based on horizon (H90 first). Otherwise HEARTBEAT_OK.

  - name: time-use-visibility
    interval: 24h
    active_hours: "07:00-09:00"
    anomaly_ids: [L1-A09]
    prompt: |
      Check Time Use Calendar Tracker last entry. If > 7 days ago, alert A0
      that time visibility is lost. Otherwise HEARTBEAT_OK.

  - name: obsidian-gtd-inbox-pressure
    interval: 12h
    active_hours: "07:00-22:00"
    anomaly_ids: [L1-A08]
    prompt: |
      Count files in 25_GTD_Cerritos/inbox/. If > 30, suggest a GTD
      processing session in A0_inbox. Otherwise HEARTBEAT_OK.

  - name: zora-domain-drift
    interval: 24h
    active_hours: "08:00-09:00"
    anomaly_ids: [L1-A05]
    prompt: |
      For each LD00 ZORA domain marked ACTIVE, check LD04 scorecard
      progression over last 14 days. If domain has zero scorecard
      activity, append to weekly review prep file. Otherwise HEARTBEAT_OK.
```

## Aggregation Rule

Un tick exécute UN seul check (round-robin par `interval` dû). Pas de checks composés.
L'agrégation d'anomalies se fait dans le digest quotidien `A0_inbox/anomalies-YYYY-MM-DD.md`.

## Disable Mechanism

Pour désactiver un check sans le supprimer : ajouter `enabled: false` au niveau de la task.

## Inbounds

- `./HEARTBEAT_PROTOCOL.md`
- `./agents/Claude_Code_CLI/Heartbeat.md`
