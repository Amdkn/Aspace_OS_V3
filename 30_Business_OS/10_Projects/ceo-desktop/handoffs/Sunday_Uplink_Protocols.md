---
id: HANDOFF_SUNDAY
role: Sunday (Cadence)
project: ceo-desktop
status: STUB
created: 2026-06-07
activated: null
cadence: weekly (12WY rhythm)
adr_anchors:
  - ADR-FWK-021
  - ADR-INFRA-003
  - ADR-RICK-001
---

# Sunday — Uplink Protocols

> **Stub.** Phase 1 placeholder. Becomes the live weekly cadence channel in Phase 2.

---

## Role

Sunday is the **cadence channel** for the CEO's Desktop. She runs the weekly uplink between A0 (Amadeus), Beth (alignment), Morty (execution), and the OpenHarness runtime (per ADR-RICK-001). Sunday is the heartbeat: every week, she surfaces Beth's decisions, Morty's queue state, and the 8 B2 domain Rocks into one check-in that A0 can read in 90 seconds.

Her protocols define the **weekly template**: what gets posted, in what order, with what evidence links, and what triggers an A0 escalation. The 12WY (12-Week Year) cadence is her clock.

## When These Protocols Go Live

This stub is promoted to a live protocol in **Phase 2**. The activation trigger is the same as Beth's and Morty's: B2 managers named for ≥4 of 8 SOB. At that point, the v0.1 weekly template is drafted (see `README.md` § "Next Steps — Phase 2") and the first uplink is posted.

The first full 12WY cycle completed is the **Phase 3 graduation gate**.

## Phase 1 Content

None. Do not pre-populate the template. The template is shaped by the first real week's evidence, not by a hypothetical one. When Phase 2 starts, the v0.1 template will be defined here with the entry schema, escalation rules, and A0 response protocol.

## Pointer

- Doctrine: `_doctrine/SUMMERS_VERSE_MANIFEST.md`
- Alignment channel: `handoffs/Beth_Alignment_Log.md`
- Execution channel: `handoffs/Morty_Global_Queue.md`
- Harness runtime: ADR-RICK-001 (OpenHarness)
- Project rules: `CLAUDE.md`
