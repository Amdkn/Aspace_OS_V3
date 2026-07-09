---
name: bridge-12wy-plane-gtd
description: |
  Convert 12 Week Year canon (Life OS V0.6.2) into Plane.so GTD Cerritos Airlock.
  When the user asks to bridge 12WY → Plane, create GTD states, sync Rocks/Plans,
  or execute Cerritos 5-stage GTD (Capture/Clarify/Organize/Reflect/Engage) on
  12WY cycle Q3 2026 canon. Use when a Sprint goal requires converting
  Strategic Plan + Tactical Rock into actionable GTD steps in Plane IDE.

  Triggers:
    - "bridge 12WY Plane", "convert Rocks to GTD", "Plane Cerritos sync"
    - "12WY → Plane", "Rocks → GTD steps", "Strategy Tactics → Airlock"
    - "create GTD states Plane", "seed 12 Rocks Plane", "Tactic → Today action"
  Doctrine: A0 board observer, A1 Morty supervises, D4 append-only.

  AMENDMENT 2026-06-22 : Skip Step 2 (states already live via MCP boot).
  Use MCP `symphony-plane__plane_create_issue` directly (not REST Python
  which gets Cloudflare 403). See §Amendment D6 below.
---

# /bridge-12wy-plane-gtd — Bridge 12 Week Year canon ↔ Plane.so GTD Cerritos

## Amendment D6 (2026-06-22) — D4 falsification close

**Original SKILL.md** prescrivait `scripts/create_plane_gtd_states.py` (REST API Python) pour créer 5 GTD states custom.

**D6 root cause investigation** :
1. **D6 #1 (cp1252)** : emoji 🔧 crash Windows console → fix `PYTHONIOENCODING=utf-8`
2. **D6 #2 (Cloudflare bot protection)** : HTTP 403 `error code: 1010` à toutes les POST `/states/` — REST API direct bypass Cloudflare
3. **D6 #3 (D4 falsification)** : smoke test `mcp__symphony-plane__plane_create_issue` révèle 4 GTD states canon DÉJÀ LIVE : `Inbox`, `Next Actions`, `Today`, `Waiting For` (créés au boot MCP Vague 4 SaaS Cloud 2026-06-21)

**D4 amendment** : Step 2 (create states) SUPPRIMÉ, Step 3 utilise directement MCP `plane_create_issue`.

---

## Purpose

Transformer le canon **12WY Life OS V0.6.2** (12 Rocks canon + 12 W1-W12 Tactics)
en **Issues Plane** mappées sur les **GTD states Cerritos** (Inbox / Next Actions / Today / Waiting For / Review) — Mariner → Boimler → Tendi → Rutherford → Freeman routing.

## Canon source (D1 verified)

| Source | Path | Verbatim |
|---|---|---|
| 12WY app | `_Life-OS-2026-clone/src/apps/twelve-week/TwelveWeekApp.tsx` | "Planning" tab + Time Use tab (Una H10 + Ortegas H1) |
| Cerritos GTD | `AGENTS.md` l.126-129 | "Manager of Chaos. Law: 'Capture every loose end, no task left behind'" |
| Rocks canon | `wiki/hand_offs/handoff_plan_fancy-hugging-bengio.md` §4 | 12 items Q3 2026 verbatim A0 |
| Bridge D6 | `wiki/hand_offs/d1_receipts_rocks_field_canon_2026-06-22.md` | Rocks = polymorphic JSONB sub-key |
| Plane canon | `wiki/hand_offs/cerritos_plane_integration_2026-06-21.md` l.83 | "GTD states custom NOT created" (obsolète post-boot MCP) |
| D6 amendment | `wiki/hand_offs/handoff_bridge_12wy_plane_gtd_2026-06-22.md` | 12 Rocks live + D6 root causes |

## Workflow (amended 2026-06-22)

### Step 1 — D1 verify Plane token in `.mcp.json` (Test Key Pragma canon)

**NE PAS redemander token à A0.** Lire directement :

```bash
grep -A 5 "symphony-plane" "C:/Users/amado/.mcp.json"
```

D1 receipts attendu :
```json
"symphony-plane": {
  "command": "C:/Python314/python.exe",
  "args": ["C:/.../mcp-plane.py"],
  "env": {
    "PLANE_API_KEY": "plane_api_...",
    "PLANE_BASE_URL": "https://api.plane.so/api/v1",
    "PLANE_WORKSPACE_SLUG": "aspace-core",
    "PLANE_PROJECT_ID": "79df867c-06b5-4e61-b3f1-68aa886c39a3"
  }
}
```

### Step 2 — ~~Create 5 GTD states~~ SKIP (D6 falsification)

**SKIP** — 5 states canon déjà live via MCP boot (Vague 4 SaaS Cloud 2026-06-21). Vérifier via smoke test :
- Tool : `mcp__symphony-plane__plane_create_issue` avec `state="Next Actions"` (valid string, pas UUID)
- Si validation error révèle liste states → 4-5 states canon déjà live

### Step 3 — Seed 12 Rocks canon Q3 2026 via MCP

Tool : `mcp__symphony-plane__plane_create_issue` × 12 sequential calls.

```python
ROCKS_Q3_2026 = [
    ("W1", "SOB Abdaty: pitch OMK Services BOS + ABC OS-Community", "high"),
    ("W1", "Cycle bookends 2026: S13 tampon + S0 cycle 4", "medium"),
    ("W2", "Auto-research LLM Wiki/Skills/Dox Phase 2", "high"),
    ("W2", "Token plan MiniMax + Ollama frugality", "high"),
    ("W3", "YouTube PARA classification 12 transcripts", "medium"),
    ("W3", "Hermes orchestration use case prod", "medium"),
    ("W4", "Agent OS = interface spec/workflow Symphony", "medium"),
    ("W4", "Business OS sync via A3 Life OS (B1/B2/B3)", "high"),
    ("W6", "A3 Life OS org chart + delegation matrix", "high"),
    ("W7", "Solaris + OMK + ABC parallel dev B1/B2/B3", "medium"),
    ("W8", "Memory Core VPS migration (D4 Checkpoint Profond)", "high"),
    ("W9", "12WY Q3 retrospective + cycle 4 brief", "medium"),
]
```

**Pour chaque Rock** :
- `name` : `"{W#} Rock: {title}"`
- `description` : `12WY Q3 2026 cycle — {W#} Rock canon verbatim A0 plan §4. Doctrine: A0 board observer passif, A1 Morty Focus supervises, Cerritos 5-stage GTD routing. Definition of Done: per Una spec l.76 = observable artifact. Source: wiki/hand_offs/handoff_plan_fancy-hugging-bengio.md §4.`
- `state` : `Next Actions` (Boimler Clarify default canon)

**D1 receipts** (post-execution 2026-06-22) : 12 Issues live sequence_id 8-19, capture UUIDs table dans handoff canon.

### Step 4 — Tactic → Today actions bridge (optionnel, prochaine session)

Pour chaque Tactic dans `_Life-OS-2026-clone/src/stores/fw-12wy.store.ts`, créer 1 Plane sub-issue :
- `state=Today` si `week === ACTIVE_WEEK` (W3 = 06/22-06/28)
- `state=Next Actions` sinon
- `parent_id = <corresponding Rock Issue ID>`

### Step 5 — Module grouping (optionnel)

Créer Module Plane "12WY Cycle Q3 2026" via REST API (POST `/modules/`) — pas critique, peut rester en flat issues.

### Step 6 — D4 append-only close canon

Update `wiki/hand_offs/handoff_bridge_12wy_plane_gtd_2026-06-22.md` (déjà créé 2026-06-22) avec :
- 12 Rock Issue UUIDs (D1 receipts canon)
- Bridge activation timestamp
- D6 lessons shipped

## Acceptance Criteria

| Test | Expected |
|---|---|
| `grep .mcp.json` Plane config | 5 lignes verbatim, token PAS affiché (security) |
| `mcp__symphony-plane__plane_list_issues` | 19 issues total (7 onboarding + 12 rocks) |
| `mcp__symphony-plane__plane_create_issue` smoke test | validation error → reveals 4-5 states canon |
| 12 sequential `plane_create_issue` calls | 12 UUIDs returned, 0 failures |
| Bridge bi-directionnel (V0.7) | Plane state change → TwelveWeekApp tactic.status sync |

## Doctrine ancrée

- **D1 verify-before-assert** : paths + line numbers + verbatim quotes dans chaque step
- **D2 research-first** : 5 sources canon lues AVANT skill creation
- **D3 nuance over literal** : "Rock" canon UI = "Plan" label, mais backend canon Moran 12WY reste "Rock"
- **D4 append-only** : SKILL.md nouveau, 0 modification ADRs existants
- **D5 proof not narrative** : D1 receipts gathering avant "✅ shipped"
- **D6 root-cause** : 3 D6 lessons (cp1252 + Cloudflare + falsification states déjà live)
- **D7 cost-of-escalation** : 0 AskUserQuestion mid-execution, token récupéré via grep direct
- **D8 cross-agent** : MCP `symphony-plane` = canonical (contourne Cloudflare vs REST Python)

## Anti-patterns interdits

- ❌ Redemander token Plane à A0 (déjà dans `.mcp.json`, Test Key Pragma)
- ❌ Utiliser REST Python direct (`requests`/`urllib`) — Cloudflare 403
- ❌ Créer GTD states via POST `/states/` — déjà live
- ❌ Mapper Rocks → issues sans state canon (utiliser strings "Inbox"/"Next Actions"/"Today"/"Waiting For")
- ❌ Hardcoder PAT dans scripts (env var User scope only, Test Key Pragma)
- ❌ Confondre "Rock" (Moran 12WY UI "Plan") avec "EOS Rock" (Wickman EOS = Q1 2027)

## Related

- `wiki/hand_offs/handoff_bridge_12wy_plane_gtd_2026-06-22.md` — SHIPPED handoff
- `wiki/hand_offs/cerritos_plane_integration_2026-06-21.md` — Plane canon original
- `wiki/hand_offs/d1_receipts_rocks_field_canon_2026-06-22.md` — Rocks D1 receipts
- `_SPECS/ADR/L1_Life_OS/ADR-SNW-001_curie-12wy-goal-orientation.md` — 12WY canon SNW goal
- `_Life-OS-2026-clone/src/apps/twelve-week/TwelveWeekApp.tsx` — UI 12WY V0.6.2
- `_Life-OS-2026-clone/src/stores/fw-12wy.store.ts` — Store 12WY canon
- `AGENTS.md` l.116-129 — SNW canon + Cerritos canon
- `CLAUDE.md` §"Skill Creator Reflex" — Phase 2 doctrine (Hermes-style self-improvement)
- `.mcp.json` l.144 — Plane PAT canon (Test Key Pragma)

## ROI

- **Without skill** : ~30 min/cycle de mapping manuel (12 Rocks + Tactic W1-W12 + GTD routing)
- **With skill** : ~2 min/cycle (1 brief + 12 MCP calls + 1 handoff update)
- **Cycle count** : 12 cycles/year × 28 min saved = **5.6h/year saved**
- **Phase 2 ROI** : A0 board observer peut déléguer totalement à A1 Morty + A2 Cerritos

---

**Created by** : A2 Claude Code orchestrator + A3 Geordi (Resources)
**Date** : 2026-06-22
**Cycle** : 12WY Q3 2026 W3 (06/22-06/28)
**Amended** : 2026-06-22 (D6 falsification close, MCP-based path)
**Doctrine** : Phase 2 Hermes-style self-improvement (CLAUDE.md §"Skill Creator Reflex")