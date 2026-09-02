---
session: agent-a2c06d4e24fa2963b
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\de35c5f1-6944-47f6-b8bc-849452b0313a\subagents\agent-a2c06d4e24fa2963b.jsonl
debut: 2026-07-25T21:49:13.881Z
fin: 2026-07-25T21:50:07.831Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "You are an Implementation Spec sub-agent. Read this brief, then execute. ## Mission Produce the **Domain 01 RH…"
---

## >>> UTILISATEUR #1

You are an Implementation Spec sub-agent. Read this brief, then execute.

## Mission

Produce the **Domain 01 RH & Méta-Gouvernance Implementation Spec** — concrete next actions per Green Lantern B2 + 8 X-Men B3 members + tools/Hooks needed to apply the Foundational Exemplar Pattern in the Coach OS Web Desktop runtime.

## Context

- Domain 01 = RH & Méta-Gouvernance (Green Lantern × X-Men) — **FOUNDATIONAL EXEMPLAR PATTERN** for all 7 sister ADRs
- Coach OS = current implementation surface at `C:\Users\amado\coach-os\`
  - Vite 8 + React 19.2 + TypeScript + Tailwind 4 + Zustand
  - Apps: dashboard, clients, finance, growth, it-rd, legal, marketplace, onboarding, operations
  - **No existing "rh-meta-gouv" or "governance" app yet** — must be created
- B3 squad = 8 X-Men (Cyclops LEAD, Jean Grey, Wolverine, Storm, Beast, Rogue, Gambit, Nightcrawler)
- Focus per A+ directive 2026-07-25 : HR + meta-gouvernance (cross-domain policy, agent patterns, organizational adaptation)
- Sister canon : ADR-CANON-001 (Roster 01), ADR-CANON-002, ADR-RH-META-GOUVERNANCE-001 (PROPOSED — being canonicalized), ADR-AGENT-BENCH-SCHEMA-001 (PROPOSED), ADR-LANDING-AESTHETIC-001

## Deliverable (return in your final response as markdown)

### 1. Green Lantern (B2) — H1/H10 Gatekeeper scope
- 1 concrete next action in Coach OS
- Tool : Green Lantern gatekeeper hook, H1/H10 reversible scope action
- Hook : (Green Lantern gatekeeper hook)

### 2. Cyclops (LEAD) — Strategic vision, mentalist-grade coaching
- 1 concrete next action in Coach OS
- Tool : Cyclops coach review surface, strategic vision
- Hook : (Cyclops coach hook)

### 3. Jean Grey — Phoenix scope, scope creep detection
- 1 concrete next action in Coach OS
- Tool : Phoenix scope detector, power discipline
- Hook : (Jean Grey Phoenix hook)

### 4. Wolverine — Adamantium durability, edge cases
- 1 concrete next action in Coach OS
- Tool : adamantium durability test, regression testing
- Hook : (Wolverine adamantium hook)

### 5. Storm — Atmospheric, multi-domain adaptation
- 1 concrete next action in Coach OS
- Tool : atmospheric weather, multi-domain adaptation
- Hook : (Storm atmospheric hook)

### 6. Beast — R&D, methodology research
- 1 concrete next action in Coach OS
- Tool : R&D pipeline, methodology research
- Hook : (Beast R&D hook)

### 7. Rogue — Knowledge transfer, identity preservation
- 1 concrete next action in Coach OS
- Tool : knowledge transfer, identity preservation
- Hook : (Rogue knowledge transfer hook)

### 8. Gambit — Tactical precision, ops X-Men
- 1 concrete next action in Coach OS
- Tool : tactical precision, ops X-Men
- Hook : (Gambit tactical hook)

### 9. Nightcrawler — Bridging, talent mobility
- 1 concrete next action in Coach OS
- Tool : bridging, talent mobility
- Hook : (Nightcrawler bridging hook)

### Cross-cutting Implementation Notes
- File paths in `C:\Users\amado\coach-os\` to touch (D4 append-only)
- Sister docs to reference (7 sister ADRs round 1)
- First shippable milestone (H1/H10 cross-cutting = 1 X-Men Coach review pipeline SPAWN-canonized)

## Constraints

- D1-D8 as standard
- DO NOT create files — return content only
- Be specific to coach-os structure (cite real file paths)
- 1 next action per member = 1 concrete shippable thing
- Plus 1 B2 (Green Lantern) next action
- Token budget : ~4K chars output (9 members)

## Output format

Single markdown document with 10 sections. ~4K chars. Concrete file paths, no placeholders.

### assistant

# Domain 01 RH & Méta-Gouvernance — Implementation Spec

> Coach OS runtime at `C:\Users\amado\coach-os\` (Vite 8 + React 19.2 + TS + Tailwind 4 + Zustand)
> Foundational Exemplar for 7 sister ADRs (D1 receipts expected).

## 1. Green Lantern (B2) — H1/H10 Gatekeeper scope

**Action:** Scaffold the `rh-meta-gouv` Coach OS app wired to the Green Lantern gatekeeper hook so cross-domain policy writes (ADR proposals, agent pattern updates, org chart changes) are emitted as Outbox notifications scoped to H1/H10 only (H30/H90 deferred to the 7 sister domains).

**Tool:** `CoachGatekeeper` Zustand store slice exposing `propose(scope: 'H1'|'H10', payload: PolicyProposal)`, backed by `coach-os/src/apps/rh-meta-gouv/store.ts` with `pnpm zustand` `@coach-os-rh` short-id.

**Hook:** `Stop` hook at `coach-os/.claude/settings.json` checks `git diff --stat` for `src/apps/rh-meta-gouv/**` and emits a `coach-gate.log` line per **D1** (verbatim file path + bytes changed), writes to `coach-os/.claude/coach-gate.log` (D4 append-only).

**File paths:**
- `C:\Users\amado\coach-os\src\apps\rh-meta-gouv\App.tsx` (new)
- `C:\Users\amado\coach-os\src\apps\rh-meta-gouv\store.ts` (new)
- `C:\Users\amado\coach-os\src\apps\rh-meta-gouv\PolicyProposal.ts` (new — `PolicyProposal` type)
- `C:\Users\amado\coach-os\src\apps\registry.ts` (patch — add `rh-meta-gouv` entry)
- `C:\Users\amado\coach-os\.claude\settings.json` (patch — add `Stop` hook)

## 2. Cyclops (LEAD) — Strategic vision

**Action:** Build the `CyclopsCoach` review surface that runs a **mentalist-grade** weekly review (H1/H10/H30) of all 7 sister ADRs aggregated from `wiki/hand_offs/adr_proposals_*.md` and surfaces strategic-misalignment risks with a 1-line `REQ-ALIGN` per ADR.

**Tool:** `CyclopsCoachReview.tsx` rendering `alignScore` (0–100) + `strategicDrift` flags per ADR, fed by `useAdrCanon()` Zustand selector.

**Hook:** `PreToolUse` hook on `Write|Edit` of `src/apps/rh-meta-gouv/**` — fires `cyclops-coach align-check` (D1-receipts: regex match on ADR-id → resolve `wiki/hand_offs/adr_proposals_<id>.md` → emit `alignScore` to `coach-os/.claude/cyclops-coach.log`).

**File paths:**
- `C:\Users\amado\coach-os\src\apps\rh-meta-gouv\coach\CyclopsCoachReview.tsx`
- `C:\Users\amado\coach-os\src\apps\rh-meta-gouv\coach\useAdrCanon.ts`
- `C:\Users\amado\coach-os\src\apps\rh-meta-gouv\coach\alignScore.ts` (pure fn: `score(adr) → number`)

## 3. Jean Grey — Phoenix scope, scope creep detection

**Action:** Implement `PhoenixScope` detector that flags any `rh-meta-gouv` write whose payload diff exceeds the H1/H10 reversible lane (e.g., touching `C:\Users\amado\agent-os\` or `C:\Users\amado\ASpace_OS_V2\` from inside Coach OS — anti-pattern per ADR-SOBER-002).

**Tool:** `phoenixScopeCheck(payload, baseline)` returning `{ ok: boolean, reason?: 'cross-canon' | 'lane-escape' | 'untracked-secret' }`.

**Hook:** `PreToolUse` hook on `Write` for `rh-meta-gouv/**` payloads — runs `phoenixScopeCheck` first; on `ok: false` writes `coach-os/.claude/phoenix-scope.log` + blocks with exit 2 (consistent with `rules/ecc/web/hooks.md` 800-line guard pattern).

**File paths:**
- `C:\Users\amado\coach-os\src\apps\rh-meta-gouv\phoenix\PhoenixScope.ts`
- `C:\Users\amado\coach-os\src\apps\rh-meta-gouv\phoenix\scopeBaseline.ts` (tracks canonical paths)

## 4. Wolverine — Adamantium durability

**Action:** Add the `Adamantium` regression-test suite asserting that `PolyrepoCleaner` (Coach OS D1-verify-before-assert § "never hand-roll desktop-web as stub slop") cannot write outside `coach-os/**`. Test corpus = 8 sibling apps (dashboard, clients, finance, growth, it-rd, legal, marketplace, onboarding, operations) each asserting forged path attempts throw.

**Tool:** `vitest` config at `coach-os/vitest.config.ts` + `apps/rh-meta-gouv/__tests__/adamantium.test.ts` (8 specs × 3 injection vectors = 24 cases).

**Hook:** `PostToolUse` hook on `Write|Edit` of `src/**` — runs `pnpm vitest run adamantium` scoped to touched file; gates commit on green (D1 receipt = `vitest passed X/24` in `coach-os/.claude/wolverine.log`).

**File paths:**
- `C:\Users\amado\coach-os\src\apps\rh-meta-gouv\__tests__\adamantium.test.ts`
- `C:\Users\amado\coach-os\vitest.config.ts` (patch, add `rh-meta-gouv` test pool)

## 5. Storm — Atmospheric multi-domain adaptation

**Action:** Build `StormAtmosphere` runtime that re-renders the `rh-meta-gouv` dashboard with **domain-aware weather** — each of the 8 lifecycle domains (LD01-LD08) gets a `WeatherChip` (sunny / cloudy / storm) driven by `Agent OS` standard `global/coding-style` flags + recent edit frequency from `wiki/hand_offs/`.

**Tool:** `useAtmosphere(domain: 'LD01'|...|'LD08')` hook returning `WeatherState`, animated via `transform`/`opacity` only (per `rules/ecc/web/performance.md` compositor-friendly stance).

**Hook:** `PostToolUse` hook on `Write|Edit` anywhere in `coach-os/src/**` — recomputes `WeatherState` for affected domain, writes 1-line to `coach-os/.claude/storm.log` (D4 append-only).

**File paths:**
- `C:\Users\amado\coach-os\src\apps\rh-meta-gouv\atmosphere\StormAtmosphere.tsx`
- `C:\Users\amado\coach-os\src\apps\rh-meta-gouv\atmosphere\useAtmosphere.ts`
- `C:\Users\amado\coach-os\src\apps\rh-meta-gouv\atmosphere\WeatherChip.tsx`

## 6. Beast — R&D methodology research

**Action:** Stand up `BeastLab` — a methodology-research surface that ingests the 23 Mindsets canon (`ASpace_OS_V2/00_Amadeus/02_Mindsets/`), 5 Loops ADR-LD07-Pocock / Herk / Jason / AI-Impact, and emits a `methodologyDiff` per new ADR proposal showing drift-vs-canon in 1-line.

**Tool:** `BeastLab.tsx` with `useMethodologyDiff(adrId)` selector hashing against `mindsets.ts` corpus.

**Hook:** Daily `CronCreate` (D7 cost-of-escalation — no A0 GO needed; per CLAUDE.md "agents create skills at end-of-session WITHOUT A0 GO") firing `pnpm beast:scan` → writes `coach-os/.claude/beast-diff.log` (D1 receipt: `#ADRs scanned / #drifted / #clean`).

**File paths:**
- `C:\Users\amado\coach-os
