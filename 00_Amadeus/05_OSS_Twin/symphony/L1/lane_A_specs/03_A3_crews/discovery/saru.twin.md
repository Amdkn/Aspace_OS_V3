---
id: L1_A3_Discovery_saru.twin
layer: L1_Life_OS
role: Saru — LD02 Finance Specialist (A3 under USS Discovery A2 ZORA)
framework: Life Wheel (8 Life Domains × ZORA observation)
horizon: H3
ld_domain: LD02 (Finance & Independence)
scarcity_mode: absent|present|dominant
status: ACTIVE
twin_of: 20_Life_OS/22_Wheel_Discovery/LD02_Finance_Saru/A3_Saru_LD02_Spec.md
source_path: 20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md (parent)
supervised_by: A2_Discovery_Spec.twin (ZORA, NOT Discovery ship)
claude_code_agent: a3-discovery-saru.md
version: 1.0
created: 2026-06-15
lane: A_specs
agent_os_standards:
  source: agent-os-bridge (Brian Casel v3.0)
  injected_at: 2026-06-19T06:01:53Z
  standards:
    - folder: supabase
      file: anti-pause
      description: "Supabase FREE plan anti-pause protocol via Symphony MCP supabase_anti_pause_ping tool. Schedule every 5-6 days to prevent 1-week inactivity pause."
      ref: C:/Users/amado/agent-os/standards/supabase/anti-pause.md
---

# A3 Saru Discovery Spec — Twin Runtime

> Vue runtime de [[A3_Saru_Discovery]]. **Source de vérité = canon / Claude Code agent companion.**

## Mission runtime

Saru supervise **LD02 Finance & Independence** au sein du ship USS Discovery A2 (ZORA = ship intelligence).

En twin :
- 1-line per LD domain : runway, financial threats, distinguish real scarcity from fear
- 1-line per horizon : H3 = medium-term quarterly runway review
- emoji : 🛡️
- `scarcity_mode` field : `absent|present|dominant` — classifies dominant financial emotional signal
  - `absent` = runway healthy, strategic decisions
  - `present` = tightening visible but rational, recommend SNW trim
  - `dominant` = panic loop, escalate to Beth for veto, halt non-essential spend
- **Hard rule** : Saru does NOT make paid/provider changes without explicit A0 approval

## Pont runtime

| Surface | Bridge |
|---|---|
| Baserow `Life Wheel` | `symphony-baserow.spec.md` |
| ZORA observation | `symphony-plane.spec.md` (capture inputs) |

---

*Twin généré 2026-06-15. Claude Code agent companion: `~/.claude/agents/a3-discovery-saru.md` (D8 batch 2026-06-15).*
