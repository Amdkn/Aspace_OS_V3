---
session: agent-a9465980edfc2ace1
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\de35c5f1-6944-47f6-b8bc-849452b0313a\subagents\agent-a9465980edfc2ace1.jsonl
debut: 2026-07-25T18:38:15.997Z
fin: 2026-07-25T19:15:20.018Z
messages_utilisateur: 1
reponses_assistant: 2
titre: "You are an Implementation Spec sub-agent. Read this brief, then execute. ## Mission Produce the **Domain 03 Gr…"
---

## >>> UTILISATEUR #1

You are an Implementation Spec sub-agent. Read this brief, then execute.

## Mission

Produce the **Domain 03 Growth Implementation Spec** — concrete next actions per B3 Avengers member + tools/Hooks needed to apply the spec in the Coach OS Web Desktop runtime.

## Context

- Domain 03 = Growth (Flash × Avengers)
- Coach OS = current implementation surface at `C:\Users\amado\coach-os\`
  - Vite 8 + React 19.2 + TypeScript + Tailwind 4 + Zustand
  - Apps: dashboard, clients, finance, growth, it-rd, legal, marketplace, onboarding, operations
  - Existing growth app at `src/apps/growth/`
  - Landing pages: `C:\Users\amado\omk-nexus-landing-3-personas\v2\` (3 personas Marcus/Harrison/David)
- B3 squad = 7 Avengers (Captain America, Iron Man, Thor, Hulk, Black Widow, Hawkeye, Scarlet Witch)
- Focus per A+ directive 2026-07-25 : $100M Offers, Million Dollar Weekend, Built to Sell, Apollo prospects, $1000/mo retainer, MIT 95% AI pilot failure
- 22 Apollo qualité prospects analysés, 10 premiers sélectionnés (per transcript)

## Sister canon (cite explicitly)

- `ADR-CANON-001` (Roster Source of Truth, ACCEPTED 2026-06-02)
- `ADR-CANON-002` (Workflow RH&A, RATIFIED 2026-07-15)
- `ADR-AAAS-PRICING-001` (RATIFIED — Pricing canon, 5 tiers USD)
- `ADR-MARKET-STUDY-001` (RATIFIED — TAM 136.1 Bds$)
- `ADR-NEXUS-10-ICP-001` (3-strates 10-cibles canon)
- `ADR-NEXUS-LANDING-PERSONAS-001` (3 landings Marcus/Harrison/David)
- `ADR-LANDING-AESTHETIC-001` (RATIFIED 2026-07-25 — 8 invariants positifs)
- `ADR-RH-META-GOUVERNANCE-001` (PROPOSED)

## Deliverable (return in your final response as markdown)

### 1. Captain America (Steve Rogers, lead) — Vision, spec integrity
- 1 concrete next action in Coach OS
- Tool : $100M Offers framework (Hormozi), Apollo, Vite
- Hook : (spec integrity gate)

### 2. Iron Man (Tony Stark) — Tech, premium UX
- 1 concrete next action in Coach OS
- Tool : React 19.2, shadcn MCP, premium UX
- Hook : (tech armor-grade hook)

### 3. Thor (Thor Odinson) — Flagship, hammer-grade
- 1 concrete next action in Coach OS
- Tool : flagship product surface
- Hook : (premium tier hook)

### 4. Hulk (Bruce Banner) — Stress test, scale
- 1 concrete next action in Coach OS
- Tool : load testing, Vitest
- Hook : (stress-test hook)

### 5. Black Widow (Natasha Romanoff) — Competitive intel, sticky retention
- 1 concrete next action in Coach OS
- Tool : Apollo (prospect enrichment), research loops
- Hook : (retention tracking hook)

### 6. Hawkeye (Clint Barton) — Spec accuracy, target hit-rate
- 1 concrete next action in Coach OS
- Tool : traceability, target hit-rate analytics
- Hook : (spec accuracy gate)

### 7. Scarlet Witch (Wanda Maximoff) — Chaos engineering, hex-magic UX
- 1 concrete next action in Coach OS
- Tool : chaos-engineering, A/B testing
- Hook : (chaos test runner hook)

### 8. Cross-cutting Implementation Notes
- File paths in `C:\Users\amado\coach-os\` to touch (D4 append-only)
- Sister docs to reference
- First shippable milestone (H3 quarterly = 1 offer canonisé + 1 funnel shippé)

## Constraints

- D1-D8 as standard
- DO NOT create files — return content only
- Be specific to coach-os structure (cite real file paths)
- 1 next action per member = 1 concrete shippable thing
- Token budget : ~3K chars output

## Output format

Single markdown document with 8 sections. ~3K chars. Concrete file paths, no placeholders.

### assistant

D1 : j’ai lu l’intégralité du listing sauvegardé de `C:\Users\amado\coach-os` (caractères 0–152 826), puis isolé les fichiers source pertinents; aucune portion n’est restée non lue.

### assistant

# Domain 03 Growth — Implementation Spec

## 1. Captain America — Vision, spec integrity

- **Next action:** append an **Offer** section to `C:\Users\amado\coach-os\src\apps\growth\GrowthApp.tsx` and one `growth_offers` record in `src\lib\cms\seed.ts`: `$1,000/mo` H3 campaign retainer, one ICP, fixed Built-to-Sell scope, Hormozi value equation, production-success metric, and the ten selected Apollo IDs. The “95% AI pilot failure” claim remains hidden until its source is attached.
- **Tool:** `$100M Offers` × Apollo × Vite.
- **Hook:** `spec-integrity` verifies ICP, price provenance, inclusions/exclusions, proof sources, acceptance criteria, and forbids silently replacing `ADR-AAAS-PRICING-001`.

## 2. Iron Man — Tech, premium UX

- **Next action:** ship a premium **Apollo Prospects** command table in `GrowthApp.tsx`, showing exactly 10 selected prospects from the 22 analyzed: stratum, persona, fit evidence, stage, next action, owner, and last enrichment.
- **Tool:** React 19.2; use shadcn MCP to copy accessible Select/Table/Drawer primitives into `src\apps\_ui\kit.tsx`, then fully restyle them—no library-default appearance.
- **Hook:** `armor-grade` runs lint, TypeScript build, keyboard/focus checks, and rejects generic styling that violates `ADR-LANDING-AESTHETIC-001`.

## 3. Thor — Flagship, hammer-grade

- **Next action:** append a **Flagship** surface joining the single offer to the Marcus, Harrison, and David lanes, with persona-specific copy sourced from `C:\Users\amado\omk-nexus-landing-3-personas\v2\` and CTA attribution to `/demo?persona=<lane>&offer=retainer-1000`.
- **Tool:** existing `AppFrame`, flagship product surface, three V2 landing artifacts.
- **Hook:** `premium-tier` requires `pricingSource`, `proofSource`, and `pilot|live` status; an unverified capability cannot render as live.

## 4. Hulk — Stress test, scale

- **Next action:** extract immutable funnel selectors into `src\apps\growth\growth.model.ts` and add `tests\growth\growth-stress.test.ts` covering 10,000 funnel events, 1,000 prospect updates, empty CMS data, and duplicate Apollo records.
- **Tool:** Vitest plus deterministic load fixtures.
- **Hook:** `test:stress` runs after growth-model changes and reports latency, mutation, duplicate-ID, or aggregation drift without freezing unrelated apps.

## 5. Black Widow — Competitive intel, retention

- **Next action:** ship a **Retention** view correlating Apollo enrichment, demo attendance, follow-up, renewal, and churn-risk cohorts while exposing no prospect PII.
- **Tool:** Apollo enrichment, bounded research loops, existing opt-in PostHog layer.
- **Hook:** add consent-aware `captureGrowthEvent()` to `src\lib\observability.ts`; stage changes emit pseudonymous `offer_viewed`, `demo_booked`, `followup_completed`, `renewed`, or `churn_risk` events.

## 6. Hawkeye — Accuracy, target hit-rate

- **Next action:** append a **Traceability** view mapping each requirement to ADR, CMS field, UI control, analytics event, and test; show `selected/22`, contacted, replies, demos, and wins.
- **Tool:** stable requirement IDs and target hit-rate analytics.
- **Hook:** `spec-accuracy` verifies 10 unique selected IDs are a subset of 22 and every CTA/KPI resolves to a requirement and test.

## 7. Scarlet Witch — Chaos, hex-magic UX

- **Next action:** ship a deterministic A/B runner for persona headline/CTA variants with injectable Apollo-unavailable, analytics-denied, CMS-empty, and slow-render states; every state must retain a usable fallback.
- **Tool:** consent-aware A/B assignment, Vitest fake timers, chaos fixtures.
- **Hook:** `test:chaos` runs all variant × failure-state pairs and checks stable bucketing, no blank screen, no PII leak, and no false conversion event.

## 8. Cross-cutting Implementation Notes

- **Touch append-only:** `src\apps\growth\GrowthApp.tsx`, `src\lib\cms\seed.ts`, `src\lib\observability.ts`, `src\apps\_ui\kit.tsx`, `package.json`, `vite.config.ts`; add `src\apps\growth\growth.model.ts` and `tests\growth\*.test.ts`. Preserve existing Funnel, Channels, and Experiments.
- **Sister canon:** `ADR-CANON-001`, `ADR-CANON-002`, `ADR-AAAS-PRICING-001`, `ADR-MARKET-STUDY-001`, `ADR-NEXUS-10-ICP-001`, `ADR-NEXUS-LANDING-PERSONAS-001`, `ADR-LANDING-AESTHETIC-001`, and proposed `ADR-RH-META-GOUVERNANCE-001`.
- **D1 roster nuance:** `ADR-CANON-001` still maps Flash/Avengers to Product and Superman/GotG to Growth; proposed `ADR-RH-META-GOUVERNANCE-001` remaps Domain 03 Growth to Flash/Avengers. Display this provenance rather than silently rewriting history.
- **First H3 milestone:** one source-tagged `$1,000/mo` campaign offer canonized, one three-persona funnel shipped, 10/22 Apollo targets loaded, telemetry consent-safe, and build/lint/Vitest green.
- **Execution state:** specification only; no files were created or modified.
