---
id: B3_WARP_CORE_EXECUTION_MARINA_CLEANING_BOS_SOP
layer: L2-Business-Pulse-B3
status: ACTIVE
created: 2026-05-21
---

# B3 Warp Core Execution — 05 marina Cleaning BOS & SOP

## Warp Core Doctrine

### What B3 Does

- **Executes** Rocks assigned by B2 managers within W1–W12 cycle
- **Logs** Lead/Lag metrics weekly per W1–W12 format
- **Produces** SOP artifacts as primary deliverable proofs
- **Calls** blockers with evidence within 24h of detection
- **Implements** WHO delegations from B2 with full outcome accountability
- **Schedules** crew with weather buffer compliance

### What B3 Does NOT Do

- Rewrite strategy (B1 owns vision)
- Redefine Rock scope (B2 owns Rocks)
- Alter B2 domain standards (J01 Area Standard is fixed)
- Escalate without first logging Lead/Lag evidence
- Execute tasks that B2 has not assigned or ratified

**Core rule**: B3 is the engine, not the steering wheel. If you feel the need to redirect, that is a B2 or B1 conversation, not a B3 action.

---

## 12WY Cycle Tracking Template

### Cycle Format: W1–W4 (21-day sprints for marina Cleaning)

```
12WY CYCLE: _____  |  Start: __________  |  End: __________

ROCK TRACKING
────────────────────────────────────────────────────────────
Rock # | Description | B2 Owner | Start State | End State | Deadline | Status
────────────────────────────────────────────────────────────
R1     |             |          |             |           |          |
R2     |             |          |             |           |          |
R3     |             |          |             |           |          |
R4     |             |          |             |           |          |
────────────────────────────────────────────────────────────

WEEKLY LEAD/LAG LOG
────────────────────────────────────────────────────────────
Week | Lead Indicator              | Lag Indicator             | Notes
────────────────────────────────────────────────────────────
W1D1 |                             |                            |
W1D2 |                             |                            |
W2D1 |                             |                            |
W2D2 |                             |                            |
W3D1 |                             |                            |
W3D2 |                             |                            |
W4D1 |                             |                            |
W4D2 |                             |                            |
────────────────────────────────────────────────────────────
```

---

## Lead vs Lag Definitions — marina Cleaning Specific

| Type | Definition | Examples |
|------|-----------|----------|
| **Lead** | Forward-looking, predictive | Crew shifts scheduled, SOPs drafted, contracts in negotiation, weather windows identified |
| **Lag** | Rear-looking, confirmed | SOPs live and crew-trained, jobs completed on-time, client NPS score, contracts signed, invoices sent |
| **SOP Lead** | SOP creation progress | Safety SOP drafted, quality checklist in review, scheduling SOP outline |
| **SOP Lag** | SOP live and deployed | Safety SOP crew-trained (sign-off), quality checklist in use (photo evidence), client walkthrough SOP delivered |

**Rule**: Log Leads every Monday. Log Lags every Friday. Never substitute Leads for Lags.
**marina rule**: Weather is always a Lead factor — 48h lookahead required on every weekly log.

---

## Lead/Lag Log Format

### Per-week entry must include:

```
W#D# — [Date]
Lead: [Specific metric] = [value]  (was [previous value])
      Weather window: [Yes/No] — [days available this week]
      Crew scheduling: [shifts scheduled vs shifts needed]
Lag:  [Specific metric] = [value]  (was [previous value])
      SOP status: [which SOPs are live, crew-trained, in use]
      Jobs completed: [on-time / total]
Artifact: [link or reference to SOP document, checklist photo, crew sign-off sheet]
Blocker: [Yes/No] — if Yes: [weather / equipment / client / seasonal description] + [escalated to B2 on date]
```

### Quality bar for log entries:
- Specific numbers, not vague progress ("2 crew shifts completed" not "busy week")
- Delta from prior week required ("up from 2" not just "2")
- Weather buffer status required in every lead entry (seasonal dependency)
- SOP-specific artifact proof required for any SOP Lag entry (crew sign-off, photo of checklist in use)
- Blocker must include seasonal/weather context for marina operations

---

## Artifact Proof Requirements

Every Rock milestone requires at minimum ONE artifact proof. For marina cleaning SOP work, SOP artifacts are primary.

| Artifact Type | Acceptable | Not Acceptable |
|--------------|-----------|----------------|
| SOP Document | Dated Google Doc/Notion/PDF with version number, crew sign-off page | Undated text file |
| Crew Training | Training sign-off sheet with crew member name and date | Verbal confirmation |
| Quality Checklist | Photo of completed checklist with date stamp and location | Blank checklist template |
| Weather Log | Screenshot of weather service showing 48h lookahead for scheduled crew shifts | Forecast without date |
| Client Walkthrough | Signed client acceptance form with date | Draft email |
| Job Completion | Job ticket with client sign-off, on-time flag, crew IDs | Unconfirmed verbal completion |

**Naming convention**: `Artifact_[Rock#]_[SOPName]_[BriefDescription]_[Date]`
**Storage**: `B3_Warp_Core_Execution/Artifact_Proofs/[SOP-Domain]/`

---

## Subfolder Structure

```
B3_Warp_Core_Execution/
├── README.md (this file)
├── Lead_Lag_Logs/
│   ├── W1_Operations_Assessment_SOP_Framework/
│   ├── W2_First_SOPs_Live/
│   ├── W3_Client_Contracts/
│   └── W4_Operational_Efficiency_Baseline/
└── Artifact_Proofs/
    ├── Safety_SOP/
    ├── Quality_Inspection_SOP/
    ├── Client_Walkthrough_SOP/
    ├── Scheduling_SOP/
    ├── Contract_Compliance/
    ├── Equipment_Maintenance_SOP/
    └── NPS_Tracking/
```

---

## Blocker Note Protocol — marina Seasonal Considerations

When a blocker is detected:

### Weather Blocker (Primary Risk)
1. **Within 24h**: Log the weather blocker with:
   - Weather event description (rain, wind speed, storm)
   - Scheduled shifts affected (number and dates)
   - Weather forecast for next 48h and 7-day outlook
   - Alternative schedule proposed (reschedule vs cancel vs reassign)

2. **Escalate to B2 within 48h** if unresolved:
   - Format: `[Weather Block] | Rock [#] | Date detected | Shifts affected [N] | Alternative proposed [Y/N]`

### Seasonal Blocker
- Off-season planning gaps (September–April planning for next season)
- Contract renewal timing (Q4 contract renewals before off-season)
- Equipment storage and winterization scheduling

### Standard Blocker Protocol
1. Attempt minimum 2 solutions before escalating
2. Document what was tried in blocker log
3. Use out-of-band communication for critical blockers
4. Do NOT escalate without first logging Lead/Lag evidence

---

## Completion Evidence Standard

A Rock is complete when:

| Requirement | Evidence |
|------------|----------|
| Start state achieved | Artifact showing baseline at start (inventory list, contract audit doc) |
| End state achieved | Artifact showing end state — SOP document with version + date + crew sign-off |
| Deadline met | Dated artifact within 48h of deadline |
| B2 sign-off | B2 manager acknowledgment in writing |
| Lag metrics updated | Lag log updated with final values (SOPs live count, jobs on-time rate, NPS baseline) |
| Weather contingency logged | 48h lookahead documented in weekly log for the week of SOP deployment |

**Incomplete = not done.** A Rock that is 90% complete with no SOP artifact proof is 0% complete.

**marina-specific completion rule**: SOP must be crew-trained AND client-delivered to count as complete. A draft SOP in a Google Doc is not a lag indicator.

---

## SOP Delivery Timeline (W1–W4)

| Week | SOP Name | B3 Deliverable | Crew Training | Client Delivery |
|------|----------|----------------|--------------|-----------------|
| W1 | Safety SOP | Draft v1 with water protocol | Sign-off scheduled | N/A (internal) |
| W2 | Quality Inspection SOP | Draft v1 with checklist template | Sign-off + photo evidence | N/A (internal) |
| W2 | Client Walkthrough SOP | Draft v1 with acceptance form | Sign-off | First client delivery |
| W3 | Scheduling SOP | Draft v1 with weather buffer | Sign-off | N/A (internal) |
| W4 | Equipment Maintenance SOP | Draft v1 with maintenance log | Sign-off | N/A (internal) |

---

*Warp Core owner: Summer B3 lead*
*Source: SUMMERS_VERSE_MANIFEST.md + J01_Area_Standard.md*
*Next review: 2026-08-21*