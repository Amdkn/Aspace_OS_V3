---
id: B3_WARP_CORE_EXECUTION_RILCOT_MEMBERS_SPACE_OS
layer: L2-Business-Pulse-B3
status: ACTIVE
created: 2026-05-21
---

# B3 Warp Core Execution — 03 RILCOT Members Space & OS

## Warp Core Doctrine

### What B3 Does

- **Executes** Rocks assigned by B2 managers within W1–W12 cycle
- **Logs** Lead/Lag metrics weekly per W1–W12 format
- **Produces** artifact proofs for every Rock milestone
- **Calls** blockers with evidence within 24h of detection
- **Implements** WHO delegations from B2 with full outcome accountability
- **Facilitates** member knowledge exchange sessions and documents outcomes

### What B3 Does NOT Do

- Rewrite strategy (B1 owns vision)
- Redefine Rock scope (B2 owns Rocks)
- Alter B2 domain standards (J01 Area Standard is fixed)
- Escalate without first logging Lead/Lag evidence
- Execute tasks that B2 has not assigned or ratified

**Core rule**: B3 is the engine, not the方向盘. If you feel the need to redirect, that is a B2 or B1 conversation, not a B3 action.

---

## 12WY Cycle Tracking Template

### Cycle Format: W1–W12 (84-day quarters)

```
12WY CYCLE: RILCOT_W1  |  Start: 2026-05-21  |  End: 2026-08-13

ROCK TRACKING
────────────────────────────────────────────────────────────
Rock # | Description                         | B2 Owner | Start State | End State | Deadline | Status
────────────────────────────────────────────────────────────
R1     | Member space core offer validated    | Avengers |             |           |          |
R2     | OS platform core scoped             | Kang Dyn |             |           |          |
R3     | Member journey map documented       | Batman   |             |           |          |
R4     | First artifact proof set delivered  | Warp Core|             |           |          |
────────────────────────────────────────────────────────────

WEEKLY LEAD/LAG LOG
────────────────────────────────────────────────────────────
Week | Lead Indicator                      | Lag Indicator              | Notes
────────────────────────────────────────────────────────────
W1   |                                     |                            |
W2   |                                     |                            |
W3   |                                     |                            |
W4   |                                     |                            |
W5   |                                     |                            |
W6   |                                     |                            |
W7   |                                     |                            |
W8   |                                     |                            |
W9   |                                     |                            |
W10  |                                     |                            |
W11  |                                     |                            |
W12  |                                     |                            |
────────────────────────────────────────────────────────────
```

### Lead vs Lag Definitions — RILCOT Specific

| Type | Definition | Examples |
|------|-----------|----------|
| **Lead** | Forward-looking, predictive | Members onboarded, sessions booked, knowledge shared, referrals generated |
| **Lag** | Rear-looking, confirmed | Active members count, MRR received, NPS score, knowledge artifacts produced |

**Rule**: Log Leads every Monday. Log Lags every Friday. Never substitute Leads for Lags.

---

## Lead/Lag Log Format

### Per-week entry must include:

```
W# — [Date]
Lead: [Specific metric] = [value]  (was [previous value])
Lag:  [Specific metric] = [value]  (was [previous value])
Artifact: [link or reference to proof artifact]
Blocker: [Yes/No] — if Yes: [description] + [escalated to B2 on date]
```

### Quality bar for log entries:
- Specific numbers, not vague progress ("3 peer sessions hosted" not "lots of activity")
- Delta from prior week required ("up from 20 to 25 active members" not just "25 members")
- Artifact proof required for any Lag entry
- Blocker must include date escalated and B2 acknowledgment

---

## Artifact Proof Requirements

Every Rock milestone requires at minimum ONE artifact proof.

| Artifact Type | Acceptable | Not Acceptable |
|--------------|-----------|----------------|
| Document | Google Doc, Notion page, PDF with date | Undated screenshot |
| Recording | Zoom with transcript, Loom | Raw video without context |
| System output | Screenshot of member platform, dashboard, analytics | Photo of laptop screen |
| Email | Thread with timestamp, confirmed receipt | Draft email |
| Member agreement | Signed or timestamped member tier agreement | Verbal commitment |

**Naming convention**: `Artifact_[Rock#]_[BriefDescription]_[Date]`
**Storage**: `B3_Warp_Core_Execution/Artifact_Proofs/[DomainFolder]/`

---

## Blocker Note Protocol

When a blocker is detected:

1. **Within 24h**: Log the blocker in Lead/Lag with:
   - Blocker description (specific, not vague)
   - Date first detected
   - Which Rock is affected
   - What has been tried to unblock

2. **Escalate to B2 within 48h** if unresolved after initial attempt
   - Format: `[Blocker ID] | Rock [#] | Detected [date] | Tried [X, Y] | Requesting [specific help]`

3. **Do NOT wait** for weekly log to report a blocker. Use out-of-band communication for critical blockers.

4. **Do NOT** escalate without first attempting to unblock:
   - Attempt minimum 2 solutions before escalating
   - Document what was tried in blocker log

---

## Completion Evidence Standard

A Rock is complete when:

| Requirement | Evidence |
|------------|----------|
| Start state achieved | Artifact showing baseline at start |
| End state achieved | Artifact showing end state (before/after) |
| Deadline met | Dated artifact within 48h of deadline |
| B2 sign-off | B2 manager acknowledgment in writing |
| Lag metrics updated | Lag log updated with final values |

**Incomplete = not done.** A Rock that is 90% complete with no artifact proof is 0% complete.

---

## RILCOT-Specific B3 Focus Areas

### Member Knowledge Exchange Facilitation
- Host peer learning sessions
- Document member knowledge contributions
- Maintain knowledge base artifacts
- Track member engagement metrics

### Member Onboarding OS
- Execute member journey map steps
- Track onboarding completion rates
- Escalate onboarding friction points
- Produce onboarding improvement proposals

### Community Activation Execution
- Execute referral program campaigns
- Track member referral metrics
- Document community health indicators
- Execute Solaris experience tier elements

---

## Lead_Lag_Logs & Artifact_Proofs Folders

```
B3_Warp_Core_Execution/
├── Lead_Lag_Logs/
│   ├── W1_Lead_Lag_Log.md
│   ├── W2_Lead_Lag_Log.md
│   ├── W3_Lead_Lag_Log.md
│   └── W4_Lead_Lag_Log.md
└── Artifact_Proofs/
    ├── G1_Growth_Guardians/
    ├── G2_Sales_Illuminati/
    ├── G3_Product_Avengers/
    ├── G4_Ops_FantasticFour/
    ├── G5_IT_KangDynasty/
    ├── G6_Finance_Thunderbolts/
    ├── G7_People_XMen/
    └── G8_Legal_Eternals/
```

---

*Warp Core owner: Summer B3 lead*
*Source: SUMMERS_VERSE_MANIFEST.md + J01_Area_Standard.md*
*Next review: 2026-08-21*