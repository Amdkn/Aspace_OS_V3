---
id: 12WY_WEEKLY_EXECUTION_TEMPLATE
layer: L2_Business_Pulse
surface: J01_Jerry_Prime_LD01_Business / 12WY_Area_Cadence
status: CANONICAL
created: 2026-06-02
owner: Jerry Prime (B1 Area steward)
tags: [#12wy #weekly #WAM #execution_score #lead_lag #cadence]
---

# 12WY Weekly Execution Template — the WAM + Scorecard

> Copy this block once per week (`Cycle C / Week W##`). The week — not the quarter — is the unit of
> execution. Score the lead measures; the lag outcomes follow. **≥85% execution score = on track.**
> Runs in the Symphony **Baserow Warp Core** (W1–W12), 50/30/20 Top-3 (L2/L1/L0).

---

## Weekly block (copy/fill each week)

```yaml
cycle: "C<n>"            # which 12WY cycle
week: "W##"              # W01..W12
phase: "Foundation | Scaling | Optimization"
date: "YYYY-MM-DD"
command_cycle_gate: "C1 Direction Lock | C2 Domain Activation | C3 Execution Proof | C4 Graduation"  # if a gate is due this week

# --- 1. SCORE LAST WEEK (the one number) ---
last_week:
  tactics_committed: 0
  tactics_completed: 0
  execution_score_pct: 0       # completed / committed  → target >=85
  zone: "GREEN | ORANGE | RED"  # >=85 GREEN · 70-84 ORANGE · <70 RED
  what_worked: ""
  what_slipped: ""             # if a tactic slipped: was the tactic wrong, or the execution?

# --- 2. COMMIT THIS WEEK (lead measures = controllable actions) ---
this_week_top3:                # Warp Core Top-3, 50/30/20
  L2_business_50: ""           # the dominant commitment (this Area)
  L1_life_30: ""
  L0_tech_20: ""
weekly_tactics:                # the lead measures you will be scored on next WAM
  - rock: "<which Area Rock>"
    domain: "Growth|Sales|Product|Ops|IT|Finance|People|Legal"
    tactic: "<controllable action>"
    done: false

# --- 3. LEAD / LAG SNAPSHOT ---
lead_indicators: "<this week's controllable actions count / status>"
lag_indicators:  "MRR <> · NPS <> · pipeline coverage <> · runway(mo) <>"   # pointers to Finance_Pulse / analytics, not copies

# --- 4. BLOCKERS (named, not hidden) ---
blockers:
  - item: ""
    owner_b2: ""
    needs: "missing authority | missing input | cross-domain conflict | DoD ambiguity"
    escalate_to: "peer B2 | Jerry (B1) | A0"   # peer-unblock first

# --- 5. DECISIONS (if any B1 decision was made → log packet) ---
decisions: []   # see B1_Area_Direction/03_DECISION_CHARTER.md output packet
```

---

## The WAM script (~30 min, same slot weekly)

1. **Score** — each B2 owner reports last week's execution score (%, zone). No outcome excuses; the
   number is *execution* (did you do what you committed?).
2. **Diagnose reds** — for any RED/ORANGE: was the **tactic wrong** (→ B2 revises the tactic) or was
   **execution weak** (→ People PE19–PE21: systems/habits/focus, not willpower)?
3. **Commit** — each owner commits this week's lead tactics (the Top-3, 50/30/20).
4. **Blockers** — named, with owner + escalation. Peer-unblock first (B3 rule); Jerry only on meso
   conflict / mandate / North-Star drift (the B1 intervention threshold).
5. **One decision** — if a direction call is needed, log the Decision Charter packet; else defer.

**Anti-patterns (the WAM forbids):** status theatre without a number · hiding a blocker · grading on
the lag outcome instead of the execution score · a Rock with no weekly tactics · >4 Area Rocks.

---

## Zone → action

| Zone | Execution score | Action |
|---|---|---|
| 🟢 GREEN | ≥85% | hold the line; the lag outcomes are coming |
| 🟠 ORANGE | 70–84% | tighten the system (PE19/PE20); re-commit realistically |
| 🔴 RED | <70% | Jerry intervenes; is it the tactic, the capacity, or the Rock? (AREA_STANDARD monthly triggers) |

> A great 12WY isn't a great plan — it's a **boring, repeated, scored week**. The Rocks are in the
> phase folders; this template is the heartbeat that actually moves them.

*B1 owner: Jerry Prime · 12WY (Moran) + AREA_STANDARD P8 + Symphony Baserow Warp Core · 2026-06-02.*
