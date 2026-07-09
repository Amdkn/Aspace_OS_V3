---
source: LLM_Wiki_A0
date: 2026-05-17
type: entity
domain: A0_Sovereign / Autonomous_Agents
tags: [#Karpathy #AutoResearch #Autonomous_Agent #Training_Loop]
---

# AutoResearch (entity)

**Type :** Open-source codebase by Andrej Karpathy.
**Repo :** https://github.com/karpathy/autoresearch — 81.4k ⭐
**Purpose :** Autonomous overnight LLM research via small-but-real training setup + 5-minute experiment loop.

## Identity

AutoResearch is a **methodology embodied as code**. It's not "a library" — it's an **agentic protocol** : human writes `program.md` (research grant), agent rewrites `train.py` (hypothesis), `prepare.py` stays fixed (physics). A 5-minute training budget normalizes the experiment unit so the agent can chain hundreds of trials.

## Why It Matters Here

A'Space's Shadow L0 Executor Mesh (Codex + Gemini + Claude) is **structurally identical** to AutoResearch's agent loop — except instead of a `train.py`, executors iterate on the entire A'Space codebase. AutoResearch is the *minimal proof* that this pattern works.

## Cross-Refs

- [[source_karpathy-autoresearch]] — full source summary
- [[concept_autonomous_research_loop]] — pattern abstraction
- [[entity_shadow_l0_executor_mesh]] — A'Space's incarnation of the same loop
- [[source_llm-wiki-pattern]] — Karpathy's sibling pattern (memory layer)

## Notable Forks Observed

- macOS native (miolini), MLX (trevin-creator), Windows RTX (jsegov), AMD ROCm (andyluo7).

## Inbounds

- [[source_karpathy-autoresearch]]
- [[concept_autonomous_research_loop]]
