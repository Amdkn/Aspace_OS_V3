---
source: LLM_Wiki_A0
date: 2026-05-17
type: concept
domain: A0_Sovereign / Shadow_L0 / Agent_Identity
tags: [#concept #AgentCapsule #Soul #Heartbeat #Tools #Context #ShadowL0]
---

# Concept: Agent Capsule

An Agent Capsule is the file-based replacement for runtime-bound agent identity.

It lets Codex CLI, Gemini CLI, and Claude Code CLI share the same agent identity without depending on Hermes, OpenClaw, or Paperclip AI.

---

## Required Files

```text
Soul.md
Agent.md
Heartbeat.md
Tools.md
Context.md
```

## Semantics

| File | Purpose |
|---|---|
| `Soul.md` | Identity, voice, boundaries, non-negotiables |
| `Agent.md` | Layer, role, supervisor, deliverables, escalation line |
| `Heartbeat.md` | Cadence, stale threshold, last check, proof target |
| `Tools.md` | Allowed tools, forbidden tools, CLI profile, MCP scope |
| `Context.md` | Active mission, tracker links, wiki links, current constraints |

---

## Directory Pattern

```text
wiki/agent_capsules/<layer>/<agent_slug>/
  Soul.md
  Agent.md
  Heartbeat.md
  Tools.md
  Context.md
```

## Relation To Shadow L0 Executor Mesh

The [[entity_shadow_l0_executor_mesh]] reads or receives capsule context before execution.

Symphony should pass the capsule path in the payload:

```json
{
  "agent_capsule": "wiki/agent_capsules/L0/rick_c137",
  "executor_profile": "shadow_l0_safe",
  "proof_required": ["changed_files", "validation_command", "residual_risk"]
}
```

---

## Template Location

```text
wiki/agent_capsules/_TEMPLATE/
```

---

## Related

- [[entity_shadow_l0_executor_mesh]]
- [[entity_symphony_router]]
- [[entity_rick]]

---

## Inbounds

- [[concept_agent_capsule]]

*Last updated: 2026-05-17*
