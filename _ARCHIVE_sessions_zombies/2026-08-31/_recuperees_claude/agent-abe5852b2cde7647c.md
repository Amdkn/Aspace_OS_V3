---
session: agent-abe5852b2cde7647c
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\de35c5f1-6944-47f6-b8bc-849452b0313a\subagents\agent-abe5852b2cde7647c.jsonl
debut: 2026-07-25T20:04:48.027Z
fin: 2026-07-25T20:06:08.145Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "You are a B2 Spec sub-agent. Read this brief, then execute. ## Mission Produce the **Domain 05 People B2 Spec*…"
---

## >>> UTILISATEUR #1

You are a B2 Spec sub-agent. Read this brief, then execute.

## Mission

Produce the **Domain 05 People B2 Spec** — canonical specification for the Superman (B2 Manager) × Guardians of the Galaxy (B3 squad) Business OS domain.

## Context

- A'Space OS V2 — Business OS E-Myth fractal
- Domain 05 = **People** (classical HR, culture, onboarding, talent) per A+ brief directive 2026-07-25
- B2 Lead = **Superman** (Manager E-Myth People domain)
- B3 Squad = **Guardians of the Galaxy** (6 members: Star-Lord LEAD, Gamora, Rocket, Groot, Drax, Mantis)
- Focus : classical HR, culture, onboarding, talent, ecosystem
- Horizon : H3 quarterly people culture review (consistent with sister domain H3 patterns)
- Sister canon : `ADR-CANON-001` (D6 MISMATCH FLAG: canon maps Superman × Guardians → Growth, brief directive → People classical HR) + `ADR-CANON-002` (RATIFIED 2026-07-15) + `ADR-LANDING-AESTHETIC-001` (RATIFIED 2026-07-25) + `ADR-RH-META-GOUVERNANCE-001` (PROPOSED) + `ADR-AAAS-FINANCE-CANON-001` (Saru H3)
- Coach OS Web Desktop = current implementation surface
- Sister domain 02 Ops (ADR-OPS-001 PROPOSED 2026-07-25) + Domain 03 Growth (ADR-GROWTH-001 PROPOSED 2026-07-25) + Domain 04 Cognition (ADR-COGNITION-001 PROPOSED 2026-07-25)
- Domain 01 RH & Méta-Gouv = GREEN LANTERN × X-MEN = exemplar pattern

## Sister context (cite explicitly)

- `ADR-CANON-001` (Roster 04: per canon Superman × Guardians = Growth H3, D6 MISMATCH with brief directive People)
- `ADR-CANON-002` (Workflow RH&A, X-Men = SPAWN + AMÉLIORATION)
- `ADR-RH-META-GOUVERNANCE-001` (PROPOSED) — 8-domain re-cast exemplar, re-canonicalises People as classical HR separate from RH & Méta-Gouv
- `ADR-LANDING-AESTHETIC-001` (RATIFIED 2026-07-25) — 8 invariants positifs
- `ADR-AAAS-FINANCE-CANON-001` (RATIFIED) — Saru H3 runway reference
- Sister domain 04 Cognition = 8-domain re-cast pattern (D6 flagged sister canon amendment)

## Focus topics (per A+ directive 2026-07-25 + sister canon 05 context)

- **Classical HR** : culture, onboarding, talent, retention
- **Cohort management** : ecosystem of clients (Client 2/3 per A+ directive)
- **Onboarding journeys** : Session 0 prep, coach OS surface
- **Talent pipeline** : recruitment, retention, performance reviews
- **People ops** : SOPs, dashboards, employee NPS, churn-risk

## Deliverable (return in your final response as markdown)

### 1. B2 Superman Manager Role Spec
- Mission (1 sentence)
- Horizon : H3 quarterly people culture review
- Key deliverables (3-5 bullets)
- Anti-patterns (3 D6 root causes Superman actively defends against) — focus: culture hoarding, talent churn, performance theatre

### 2. B3 Guardians Squad Roster (6 members)
For each member, give:
- Real name + superhero name
- Domain skill (1-2 lines, People lens)
- Sister B2 (Superman)
- 1 concrete output per 12WY cycle
- X-Men Coach role mapping (per `/youtube-to-B1filter` §13 + new `ADR-RH-META-GOUVERNANCE-001` §2):
  - Star-Lord (Peter Quill, LEAD) = **Professor X** (stratégique, top funnel, brand narrative, hook-grade storytelling)
  - Gamora (Gamora Zen Whoberi) = **Wolverine** (sharpened growth, killed-bad-channels, lethal efficiency)
  - Rocket (Rocket Raccoon) = **Wolverine** (weapons-grade analytics, experimental growth, R&D funnels)
  - Groot (Groot) = **Storm** (loyal retention, evergreen channels, slow & steady growth)
  - Drax (Arthur Douglas) = **Cyclops** (literal A/B testing, no-subtlety measurement, blunt funnel audit)
  - Mantis (Mantis) = **Professor X** (empathy-grade onboarding, emotional triggers, user love)

### 3. 12WY 3 Rocks (monthly rocks for H3 horizon)
- **Rock 1** (4 weeks) : 1 onboarding journey canonised (Session 0, ecosystem entry)
- **Rock 2** (4 weeks) : 1 talent pipeline shippé (recruit → onboard → retain)
- **Rock 3** (4 weeks) : 1 Ownerbook MANIFEST update (people standardisation, churn-risk dashboard)

### 4. Domain 05 Deliverable Matrix
- Tools : which tools each member uses (onboarding flows, NPS surveys, talent pipeline, retention metrics)
- Workflows : recruit → onboard → perform → retain (the HR cycle)
- Metrics : 2-3 measurables (retention rate, onboarding completion, employee NPS)
- Stop conditions : when to escalate B1

### 5. SOUL Schema (sister ADR-AGENT-BENCH-SCHEMA-001 PROPOSED)
- system_prompt (essence of Superman × Guardians)
- action_space_bounding
- research_loop_config
- gatekeeper_approval (Green Lantern scope H1/H10)

## Constraints (D-receipts + anti-patterns)

- D1 verify-before-assert : no claim about existing canon without proof
- D2 research-first : cite ADR-CANON-001 §2 (Superman × Guardians mapping) + ADR-CANON-001 Reconciliation Addendum
- D3 nuance : cite sister docs explicitly (ADR-CANON-002, ADR-LANDING-AESTHETIC-001, ADR-RH-META-GOUVERNANCE-001)
- D4 append-only : no overwrites of canon
- D5 proof-before-claim : every field must be derivable
- D6 root cause : if you see a gap in canon, name it explicitly (D6 MISMATCH FLAG: canon = Growth, brief = People)
- D7 non-escalation : no blocking questions to A0
- D8 cross-agent : cite sister agents if relevant

## Output format

Return a **single markdown document** structured as above (5 sections). Aim for 6-10K chars. Be specific, no placeholders. Cite sister ADRs explicitly.

DO NOT create any files yourself — return the content in your response. The cron dispatcher will write the ADR draft.

### assistant

# Domain 05 People — B2 Spec
## Superman (B2 Manager) × Guardians of the Galaxy (B3 Squad)

> **Sister canon** : `ADR-CANON-001` §2 (Superman × Guardians = Growth H3 canon) + `ADR-CANON-001 Reconciliation Addendum` (re-cast mechanism) + `ADR-RH-META-GOUVERNANCE-001` (PROPOSED, 8-domain re-cast exemplar).
>
> **D6 MISMATCH FLAG (named explicitly, D6)** : canon canon maps Superman × Guardians → **Growth** H3, but A+ brief directive 2026-07-25 routes the same hero pair → **People** (classical HR, culture, onboarding, talent). The reconciliation lives in the Addendum: Superman × Guardians is **re-cast** as People per A+ directive, sister to `ADR-RH-META-GOUVERNANCE-001` PROPOSED (the canonical 8-domain re-cast exemplar, per Domain 04 Cognition pattern).

---

## 1. B2 Superman Manager Role Spec

**Mission** : Superman B2 owns the People domain — classical HR, culture, onboarding, talent, retention — and translates it into a quarterly operating cadence that compounds workforce quality every H3 cycle.

**Horizon** : **H3** quarterly people culture review (12 weeks = 1 quarter = 1 SOB cycle, sister to Saru H3 runway reference `ADR-AAAS-FINANCE-CANON-001`).

**Key deliverables** (3-5) :
- **D1** Quarterly People Culture Review (Ownerbook `01_People/MANIFEST.md` patch, 1×/H3, D4 append-only).
- **D2** Onboarding journey canonisation (1×/H3 minimum, Session 0 → ecosystem entry into Coach OS Web Desktop).
- **D3** Talent pipeline standardisation (recruit → onboard → retain loop, 1×/H3 shipped).
- **D4** People ops dashboard (NPS, retention rate, churn-risk score) wired into Coach OS Web Desktop.
- **D5** B3 Guardians squad orchestration (6 sprints × 1 cycle, scrums-by-batch per `summers` skill).

**Anti-patterns — 3 D6 root causes Superman actively defends against** :
- **D6.1 Culture hoarding** : Superman refuses to let culture live in unwritten norms or DMs. Forces every cultural value into a canonical document (Ownerbook MANIFEST) before it ships. Sister cite: `ADR-LANDING-AESTHETIC-001` invariant #4 (honest copy, not aspirational theatre).
- **D6.2 Talent churn** : Superman detects silent attrition signals (missed scrums, delayed rocks, NPS drop > 10 pts) and routes them through Wolverine / Drax audits **before** they cascade. Sister cite: `ADR-META-005` hooks automation for low-risk lane.
- **D6.3 Performance theatre** : Superman rejects vanity metrics (e.g., "number of hires") in favor of retention curves and 90-day NPS. Cyclops-grade blunt measurement > pleasant noise.

**Implementation surface** : Coach OS Web Desktop (`/people/<route>`). Sister cite: `ADR-LANDING-AESTHETIC-001` (RATIFIED 2026-07-25) 8 invariants — applied to every People surface.

---

## 2. B3 Guardians Squad Roster (6 members)

### 2.1 Star-Lord (Peter Quill) — LEAD
- **Domain skill** : Strategic narrative + top-funnel storytelling. Owns brand-grade onboarding hooks and Session 0 prep rituals.
- **Sister B2** : Superman (1:1 delegation, A2/A3 bridge).
- **Output per 12WY cycle** : 1 onboarding journey narrative (PDF + video script) shipped to Coach OS Web Desktop `/onboarding/<journey-id>`.
- **X-Men Coach mapping** : **Professor X** (stratégique, top funnel, brand narrative, hook-grade storytelling).

### 2.2 Gamora (Gamora Zen Whoberi)
- **Domain skill** : Sharpened talent pipeline — kills bad-fit recruitment channels, ruthless filtering, lethal efficiency on time-to-hire.
- **Sister B2** : Superman (sister to Star-Lord).
- **Output per 12WY cycle** : 1 talent funnel audit (channels ranked, dead-channels retired, kept-channels doubled-down).
- **X-Men Coach mapping** : **Wolverine** (sharpened growth, killed-bad-channels, lethal efficiency).

### 2.3 Rocket (Rocket Raccoon)
- **Domain skill** : Weapons-grade people analytics. Experimental retention A/B tests, R&D funnels for unconventional retention plays.
- **Sister B2** : Superman.
- **Output per 12WY cycle** : 1 retention experiment (hypothesis, cohort split, D1-verified outcome).
- **X-Men Coach mapping** : **Wolverine** (weapons-grade analytics, experimental growth, R&D funnels).

### 2.4 Groot (Groot)
- **Domain skill** : Loyal retention + evergreen culture channels. Slow, steady, deep. Owns 90-day and 365-day retention curves.
- **Sister B2** : Superman.
- **Output per 12WY cycle** : 1 evergreen culture artefact (handbook section, ritual, or SOP shipped + measured at 30/90/365 days).
- **X-Men Coach mapping** : **Storm** (loyal retention, evergreen channels, slow & steady growth).

### 2.5 Drax (Arthur Douglas)
- **Domain skill** : Blunt, literal funnel audit. No-subtlety measurement — calls out NPS theatre, headcount vanity, and 360-review gymnastics.
- **Sister B2** : Superman.
- **Output per 12WY cycle** : 1 quarterly people funnel audit (Cyclops-grade blunt scorecard, public to A0).
- **X-Men Coach mapping** : **Cyclops** (literal A/B testing, no-subtlety measurement, blunt funnel audit).

### 2.6 Mantis (Mantis)
- **Domain skill** : Empathy-grade onboarding + emotional triggers. Reads room temperature, prevents churn before retention metrics drop.
- **Sister B2** : Superman.
- **Output per 12WY cycle** : 1 user-love ritual (Session 0 empathy map, NPS-9/-10 thank-you loop, churn-risk pre-mortem).
- **X-Men Coach mapping** : **Professor X** (empathy-grade onboarding, emotional triggers, user love).

**Sister cite** : per `/youtube-to-B1filter` §13 + `ADR-RH-META-GOUVERNANCE-001` §2 mapping table. Lead (Star-Lord) reports to Superman → A3 Picard Orchestrator (`picard` skill, W40+W41 rails canon).

---

## 3. 12WY 3 Rocks (H3 quarterly, 4 weeks each)

### Rock 1 (W1-W4) — 1 Onboarding Journey Canonised
- **Owner** : Star-Lord (LEAD) + Mantis (empathy layer).
- **Deliverable** : 1 complete onboarding journey from Session 0 prep → ecosystem entry, shipped to Coach OS Web Desktop `/onboarding/<journey-id>`, D4 append-only manifest entry.
- **D-receipts** : D1 (visit logs verified), D2 (sister `ADR-CANON-002` §3 RH&A workflow template), D6 (no theatre — every step 
