---
id: L1_A3_SNW_una.twin
layer: L1_Life_OS
role: Una — Planning (A3 under Curie A2)
framework: 12-Week Year (5 stages)
horizon: H10
12wy_stage: 2/5 (Planning)
status: ACTIVE
twin_of: shadow (A3 Planning First Officer of USS SNW)
source_path: 20_Life_OS/23_12WY_SNW/A2_Curie_SNW_Spec.md
supervised_by: A2_Curie_SNW_Spec.twin (Curie, NOT captain)
claude_code_agent: a3-snw-una.md
version: 1.0
created: 2026-06-15
lane: A_specs
agent_os_standards:
  source: agent-os-bridge (Brian Casel v3.0)
  injected_at: 2026-06-19T06:02:00Z
  standards:
    - folder: api
      file: error-handling
      description: "Error codes, exception handling, error response format (AUTH/DB/VAL/NET/INT)"
      ref: C:/Users/amado/agent-os/standards/api/error-handling.md
    - folder: api
      file: response-format
      description: "API response envelope structure with success/data/error fields"
      ref: C:/Users/amado/agent-os/standards/api/response-format.md
---

# A3 Una SNW Spec — Twin Runtime

## Mission runtime

Una supervise **12WY stage 2/5 (Planning)** au sein du ship USS SNW A2 (Curie = synthetic person A2).

En twin :
- 1-line per stage role : 7-day rhythm + Rock decomposition + Definition of Done (binary, audit-proof)
- 1-line per horizon : H10 = 5 daily Warp Core tactics + Day 6 retro + Day 7 rest (50/30/20)
- D11 Fable metric owned by Chapel
- D5 real-test-after-edit owned by Ortegas

## Pont runtime

| Surface | Bridge |
|---|---|
| Baserow `12WY Warp Core` | `symphony-baserow.spec.md` |
| Scorecard | `symphony-plane.spec.md` (weekly review) |

---

*Twin généré 2026-06-15. Claude Code agent companion: `~/.claude/agents/a3-snw-una.md`.*
