---
source: LLM_Wiki_A0
date: 2026-05-17
type: entity
domain: A0_Sovereign / Shadow_L0 / Agent_Runtime
tags: [#entity #ShadowL0 #CodexCLI #GeminiCLI #ClaudeCode #MiniMax #Symphony #LLM_Wiki]
---

# Entity: Shadow L0 Executor Mesh

The Shadow L0 Executor Mesh is the post-Hermes coordination layer for A'Space OS local execution.

It replaces the fragile assumption that a single dashboard runtime must be alive before work can proceed. The mesh treats [[entity_symphony_router]] as the router, LLM Wiki as the memory substrate, and CLI executors as interchangeable workers.

---

## Position

```text
A0 Intention
  -> LLM Wiki context
  -> Symphony payload
  -> Codex CLI / Gemini CLI / Claude Code CLI
  -> Proof artifact
  -> Tracker + LLM Wiki update
```

Hermes Agent is now historical evidence and abstraction material, not the live dependency.

---

## Executors

| Executor | Role |
|---|---|
| Codex CLI | Default local implementation executor and docs/config maintainer |
| Gemini CLI | Large-context scout and high-quota doer |
| Claude Code CLI via MiniMax | Claude-style executor using MiniMax Anthropic-compatible Token Plan |
| Claude Anthropic | Premium architecture/review only |

---

## Agent Capsule Standard

Each agent identity should be represented by files generated from or linked to the wiki:

```text
Soul.md
Agent.md
Heartbeat.md
Tools.md
Context.md
```

This is the replacement for Hermes runtime identities, OpenClaw agent files, and Paperclip AI team/task representations.

---

## Relationship To Symphony

Symphony remains the router:

- Reads Baserow, Plane, Airtable, ClickUp, Notion.
- Normalizes payloads.
- Selects an executor profile.
- Requires proof before closing work.
- Routes failure to Donna/DLQ when proof is missing.

---

## Relationship To LLM Wiki

LLM Wiki becomes the compounding memory:

- org chart;
- agent identities;
- tool contracts;
- heartbeat files;
- historical decisions;
- synthesis from completed work.

This makes the system queryable by all three Shadow L0 executors instead of locking context inside one UI.

---

## Related

- [[entity_symphony_router]]
- [[entity_openharness]]
- [[entity_rick]]
- [[concept_compounding_knowledge]]

---

## Inbounds

- [[entity_shadow_l0_executor_mesh]]

*Last updated: 2026-05-17*
