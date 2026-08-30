---
session: agent-a08bab92d5ffa1c0b
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\de35c5f1-6944-47f6-b8bc-849452b0313a\subagents\agent-a08bab92d5ffa1c0b.jsonl
debut: 2026-07-25T21:07:51.277Z
fin: 2026-07-25T21:09:03.966Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "You are an Implementation Spec sub-agent. Read this brief, then execute. ## Mission Produce the **Domain 07 IT…"
---

## >>> UTILISATEUR #1

You are an Implementation Spec sub-agent. Read this brief, then execute.

## Mission

Produce the **Domain 07 IT/R&D Implementation Spec** — concrete next actions per B3 Kang Dynasty member + tools/Hooks needed to apply the spec in the Coach OS Web Desktop runtime.

## Context

- Domain 07 = IT/R&D (Light + Cyborg × Kang)
- D6 nuance : canon single-lead Cyborg vs brief directive dual-lead Light + Cyborg
- Coach OS = current implementation surface at `C:\Users\amado\coach-os\`
  - Vite 8 + React 19.2 + TypeScript + Tailwind 4 + Zustand
  - Apps: dashboard, clients, finance, growth, it-rd, legal, marketplace, onboarding, operations
  - **Existing IT app at `src/apps/it-rd/ItRdApp.tsx`**
- B3 squad = 6 Kang Dynasty (Kang Prime LEAD, Iron Lad, Scarlet Centurion, Immortus, Victor Timely, Rama-Tut)
- Focus per A+ directive 2026-07-25 : API/SDK, infra, DevOps, security, anti-paperclip
- Sister canon : ADR-CANON-001 (Roster 07), ADR-CANON-002, ADR-RH-META-GOUVERNANCE-001, ADR-LANDING-AESTHETIC-001, ADR-SOBER-002 (Anti-Paperclip sister)

## Deliverable (return in your final response as markdown)

### 1. Kang Prime (LEAD) — Architectural prime, multiverse infra
- 1 concrete next action in Coach OS
- Tool : Vite 8 + React 19.2 + TS stack, multiverse infra alignment
- Hook : (architectural prime hook)

### 2. Iron Lad — Youthful dev, greenfield velocity
- 1 concrete next action in Coach OS
- Tool : greenfield prototype surface, proto-grade velocity
- Hook : (bootleg proto-grade hook)

### 3. Scarlet Centurion — Alt-stack experiments, branched pipelines
- 1 concrete next action in Coach OS
- Tool : branched pipeline + alt-stack experiments
- Hook : (scenario-grade testing hook)

### 4. Immortus — Legacy code, long-horizon deprecation
- 1 concrete next action in Coach OS
- Tool : legacy code archive, long-horizon deprecation schedule
- Hook : (atmospheric long-horizon hook)

### 5. Victor Timely — Frontier dev, civic-grade IT
- 1 concrete next action in Coach OS
- Tool : frontier dev surface, civic-grade IT
- Hook : (Phoenix scope frontier-dev hook)

### 6. Rama-Tut — Ancient tech, archaeology-grade refactor
- 1 concrete next action in Coach OS
- Tool : archaeology-grade refactor surface
- Hook : (pharaoh-tier code review hook)

### 7. Cross-cutting Implementation Notes
- File paths in `C:\Users\amado\coach-os\` to touch (D4 append-only)
- Sister docs to reference
- First shippable milestone (H10 quarterly = 1 API/SDK architecture canonisé)

## Constraints

- D1-D8 as standard
- DO NOT create files — return content only
- Be specific to coach-os structure (cite real file paths)
- 1 next action per member = 1 concrete shippable thing
- Token budget : ~3K chars output

## Output format

Single markdown document with 7 sections. ~3K chars. Concrete file paths, no placeholders.

### assistant

# Domain 07 IT/R&D — Implementation Spec (Coach OS Web Desktop)

**Surface:** `C:\Users\amado\coach-os\src\apps\it-rd\ItRdApp.tsx` (CMS-driven, collections `services`/`it_experiments`/`deploys`, 4 sections: Kernel·Experiments·Deploys·+1). Stack: Vite 8 + React 19.2 + TS + Tailwind 4 + Zustand (`useCmsStore`).
**D6 nuance:** canon (ADR-CANON-001) = **single-lead Cyborg (B2-06)**; brief 2026-07-25 directs dual-lead Light+Cyborg. Spec follows canon single-lead + treats "Light" as advisory co-owner (not roster mutation). Flag for A+ ratify, no file created.

### 1. Kang Prime (LEAD) — Architectural prime, multiverse infra
- **Action:** Add a `KernelArchitecture` section reading a new `it_api_contracts` CMS collection → renders the canonical API/SDK surface map (services × endpoints × auth).
- **Tool:** extend `src/lib/cms/cms.store.ts` seed + `src/lib/app-registry.ts` section list; align with Vite 8/React 19.2 client contract.
- **Hook:** *time-grade stability* — PostToolUse guard blocking edits that break `it_api_contracts` schema shape (append-only).

### 2. Iron Lad — Youthful dev, greenfield velocity
- **Action:** Wire the Experiments `idea→building` column to a "one-click scaffold" action seeding a proto `it_experiments` row with template body.
- **Tool:** `useCollectionDrill('it_experiments')` + `KanbanCard onClick` fast-create path.
- **Hook:** *bootleg proto-grade* — PreToolUse allow-fast on `_TRASH_`-tagged proto rows (no ceremony gate).

### 3. Scarlet Centurion — Alt-stack experiments, branched pipelines
- **Action:** Add a `variant` field to `it_experiments` (stack A/B) rendering parallel branched columns in the R&D Kanban.
- **Tool:** `KanbanBoard columns` extension in `ItRdApp.tsx` + `badgeTone.ts` variant color.
- **Hook:** *scenario-grade testing* — Stop hook runs `vite build --mode branch-check` on experiment merge.

### 4. Immortus — Legacy code, long-horizon deprecation
- **Action:** Add `deprecated_at` + `sunset_horizon` to `services`; Kernel badges services past-sunset as `warn`.
- **Tool:** `src/lib/observability.ts` deprecation scan + `SectionHead` action badge.
- **Hook:** *atmospheric long-horizon* — cron-lite watchdog appends deprecation ledger (never hard-delete, `_TRASH_<date>/`).

### 5. Victor Timely — Frontier dev, civic-grade IT
- **Action:** Add a `Deploys` latency/SLA panel reading Vercel/Supabase health via `src/lib/supabase.ts` liveness probe.
- **Tool:** `observability.ts` metrics tile + `deploys` collection status column.
- **Hook:** *Phoenix scope frontier-dev* — PostToolUse type-check (`tsc --noEmit --incremental`, timeout-capped) on frontier edits.

### 6. Rama-Tut — Ancient tech, archaeology-grade refactor
- **Action:** Add a "code archaeology" drill in `DynamicPageView` for each service showing dependency age + refactor debt score.
- **Tool:** `useCmsStore` `services[].debt` field + `CollectionRepeater` sort-by-debt.
- **Hook:** *pharaoh-tier code review* — dispatch `code-reviewer` agent on any `services` edit >50 LOC diff.

### 7. Cross-cutting Implementation Notes
- **Files to touch (D4 append-only):** `src/apps/it-rd/ItRdApp.tsx` (sections), `src/lib/cms/cms.store.ts` (collections `it_api_contracts`, fields), `src/lib/observability.ts` (health/deprecation/SLA scans), `src/lib/app-registry.ts` (section registration), `src/lib/supabase.ts` (probe). No new files; extend existing.
- **Sister docs:** ADR-CANON-001 (Roster 07 single-lead Cyborg — resolve D6 before dual-lead), ADR-CANON-002, ADR-RH-META-GOUVERNANCE-001, ADR-LANDING-AESTHETIC-001 (accent `#7c3aed`), **ADR-SOBER-002 anti-paperclip** (all 6 actions = reversible CMS-field adds, zero maximizer/self-replication surface).
- **First shippable milestone (H10 Q):** *1 API/SDK architecture canonisé* = Kang Prime's `it_api_contracts` collection + `KernelArchitecture` section live in Coach OS, seeded with the canonical service×endpoint×auth map — the anchor all 5 members' work hangs off. Ship = renders in-app, D1-verified via `vite build` green.
