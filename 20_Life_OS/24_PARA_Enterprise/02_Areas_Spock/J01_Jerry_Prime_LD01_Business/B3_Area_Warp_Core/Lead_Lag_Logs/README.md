# B3 Area Warp Core — Lead/Lag Logs

## Overview

The Area-level Lead/Lag log tracks Area ecosystem health — not individual Picard project health. Each entry captures the aggregate state of Jerry's LD01 Business Area across all active Picard projects and B2 domains.

**Lead indicators** measure leading signals of Area health (standards updated, Picard projects onboarded, B2 managers activated).
**Lag indicators** measure trailing outcomes (active projects, MRR, NPS, portfolio value).

---

## Area-Level Lead Indicators

| Indicator | Definition | Target | Frequency |
|-----------|------------|--------|-----------|
| **Standards Updated** | AREA_STANDARD.md reviewed and versioned | Quarterly | Weekly check |
| **Picard Projects Onboarded** | New Picard project added to Area with full B1/B2/B3 fractal | 2–3 by Year 1 | Monthly |
| **B2 Managers Activated** | B2 domain manager with live KR scorecard and Area Rock | 8/8 by Year 1 | Monthly |
| **Cerritos Routing Fidelity** | Ideas route correctly within 24h across all Area projects | > 95% | Weekly |
| **Zero-Jerry Offers** | Offers running without Jerry involvement | 1 by W4, 3 by Year 1 | Monthly |

---

## Area-Level Lag Indicators

| Indicator | Definition | Target | Frequency |
|-----------|------------|--------|-----------|
| **Active Picard Projects** | Projects with live B1/B2/B3 structure | 2+ by Year 1 | Monthly |
| **Area MRR** | Sum of all Picard project MRR | > 10% MoM | Weekly |
| **Area NPS** | Weighted average NPS across all projects | > 50 | Monthly |
| **Pipeline Coverage** | Pipeline value / Area MRR | > 3x | Weekly |
| **Runway** | Cash / Monthly Burn | > 12 months | Weekly |

---

## Entry Format

```
## Week [W##] — [Date]

**Lead Metrics**
- Standards Updated: [Yes/No] — [Notes]
- Picard Projects Onboarded: [Count] — [Notes]
- B2 Managers Activated: [X/8] — [Notes]
- Cerritos Routing Fidelity: [X%] — [Notes]
- Zero-Jerry Offers: [Count] — [Notes]

**Lag Metrics**
- Active Picard Projects: [Count] — [Notes]
- Area MRR: $[Amount] — [MoM Change] — [Zone]
- Area NPS: [Score] — [Zone]
- Pipeline Coverage: [X]x — [Zone]
- Runway: [N] months — [Zone]

**Zone Assessment**
[GREEN / ORANGE / RED] — [Brief rationale]

**Decisions Needed**
1. [Decision] — [B2 Owner] — [Deadline]

**B2 Owner Review**
- Growth/Guardians: [Status] — [Blockers]
- Sales/Illuminati: [Status] — [Blockers]
- Product/Avengers: [Status] — [Blockers]
- Ops/Batman: [Status] — [Blockers]
- IT/Kang Dynasty: [Status] — [Blockers]
- Finance/Thunderbolts: [Status] — [Blockers]
- People/X-Men: [Status] — [Blockers]
- Legal/Eternals: [Status] — [Blockers]
```

---

## Zone Definitions

| Zone | Trigger |
|------|---------|
| **GREEN** | All lead metrics on track; lag metrics at or above target |
| **ORANGE** | Any lead metric behind schedule OR lag metric 10–25% below target |
| **RED** | Any lead metric >2 weeks behind schedule OR lag metric >25% below target OR runway <9 months |

---

*B3 owner: Jerry Prime (Area steward)*
*Source: AREA_STANDARD.md Area Scorecard + Cerritos Handoff Protocol*
*Next review: 2026-08-21*