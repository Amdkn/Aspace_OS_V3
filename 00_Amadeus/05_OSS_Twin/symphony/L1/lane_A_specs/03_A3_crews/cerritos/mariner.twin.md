---
id: L1_A3_Cerritos_mariner.twin
layer: L1_Life_OS
role: Mariner — Capture (A3 under Holo Deck A2)
framework: GTD (5 stages)
horizon: H1
gtd_stage: Capture
status: ACTIVE
twin_of: 20_Life_OS/25_GTD_Cerritos/01_mariner/
source_path: 20_Life_OS/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md
supervised_by: A2_HoloDeck_Cerritos_Spec.twin (Holo Deck, NOT Captain Freeman)
claude_code_agent: a3-cerritos-mariner.md
version: 1.0
created: 2026-06-15
lane: A_specs
---

# A3 Mariner Cerritos Spec — Twin Runtime

## Mission runtime

Mariner supervise **GTD stage Capture** au sein du ship USS Cerritos A2 (Holo Deck = simulation room A2).

En twin :
- 1-line per GTD stage : Capture raw input, no judgment, no clarifying yet (speed > polish).
- 1-line per horizon : H1 immediate ("before A0 forgets"), sub-10-second capture, zero A0 escalation.
- D4 `_TRASH_<date>/` soft-delete pattern (append-only to `wiki/inbox/`, no overwrite).
- D7 no clarifying questions back to A0 — capture is fire-and-forget to Boimler.
- D8 cross-agent inbox compatible (`wiki/inbox/` raw format, readable Codex/Gemini/Hermes).

## Pont runtime

| Surface | Bridge |
|---|---|
| Plane workspace | `symphony-plane.spec.md` |
| Obsidian `@context` | `symphony-obsidian.spec.md` |

---

*Twin généré 2026-06-15. Claude Code agent companion: `~/.claude/agents/a3-cerritos-mariner.md`.*
