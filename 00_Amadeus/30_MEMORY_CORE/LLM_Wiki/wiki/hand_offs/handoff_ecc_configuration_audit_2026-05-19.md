---
source: Codex / configure-ecc skill audit
date: 2026-05-19
type: handoff
domain: ECC / Claude Code Skills / Codex Skills / Skill Reflex
tags: [#ECC, #Skills, #ClaudeCode, #Codex, #SkillReflex]
status: active-handoff
---

# Handoff - ECC Configuration Audit

## Summary

The `$configure-ecc` skill was invoked from Codex. The installation is partially healthy but asymmetric:

- Codex has ECC skills installed as top-level Codex skills.
- Claude has a large ECC corpus nested under `C:\Users\amado\.claude\skills\ecc\`.
- Claude did not have `configure-ecc` as a top-level skill before this audit.

Codex copied `configure-ecc` to:

`C:\Users\amado\.claude\skills\configure-ecc\SKILL.md`

This makes the installer/wizard itself discoverable by Claude Code.

## Evidence

| Check | Result |
|---|---|
| `C:\Users\amado\.codex\skills` top-level skills with `SKILL.md` | 134 |
| `C:\Users\amado\.claude\skills` top-level skills with `SKILL.md` after fix | 8 |
| `C:\Users\amado\.claude\skills\ecc\<skill>\SKILL.md` nested ECC skills | 181 |
| `C:\Users\amado\.claude\skills\configure-ecc\SKILL.md` | present after fix |

## Interpretation

Claude Code likely discovers top-level skills under `~/.claude/skills/<skill>/SKILL.md`.

Therefore, the nested ECC install at `~/.claude/skills/ecc/<skill>/SKILL.md` may act as an archive or library, but not necessarily as active Claude slash-skills.

The safe correction is not to flatten all 181 skills blindly. Some may conflict with existing top-level Claude skills, and many are not needed for A'Space right now.

## Recommended Next Action

Run a controlled ECC stocktake:

1. List nested ECC skills.
2. Compare with top-level Claude skills and top-level Codex skills.
3. Select only the A'Space relevant subset to promote top-level for Claude Code.
4. Preserve `~/.claude/skills/ecc/` as source library until promotion is validated.

High-priority Claude top-level candidates:

- `archive-and-document`
- `skill-reflex-orchestrator`
- `shadow-l0-handoff-brief` equivalent for Claude
- `agentic-os`
- `agent-harness-construction`
- `enterprise-agent-ops`
- `production-audit`
- `project-flow-ops`
- `knowledge-ops`
- `terminal-ops`
- `cost-aware-llm-pipeline`
- `token-budget-advisor`

## Secret Handling

No API key, bearer token, endpoint key, or provider secret was copied or printed during this audit.

## Residual Risk

- Exact Claude Code skill discovery semantics were inferred from local skill layout and existing active skills, not rechecked against current official docs in this pass.
- A future flattening should avoid overwriting any existing top-level Claude skill without diffing first.
