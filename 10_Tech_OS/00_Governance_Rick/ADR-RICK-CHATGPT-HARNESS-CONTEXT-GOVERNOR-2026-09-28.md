# ADR-RICK — ChatGPT Harness Context Governor

**Date:** 2026-09-28  
**Status:** Accepted  
**Scope:** ChatGPT sessions operating on A'Space V3  
**Gatekeeper:** Rick / S1  
**A0:** Amadeus / Kirby

## Context

Long ChatGPT sessions can become operationally dangerous before they visibly fail: tool-call bursts consume context, large tool outputs crowd out architectural state, local tool surfaces may degrade, and the session may begin reconstructing facts already known instead of progressing.

The failure mode is not "context is limited"; the failure mode is allowing one chat window to become the only compression layer that keeps A'Space coherent.

## Decision

ChatGPT is a frontier orchestration harness, not a disposable conversational scratchpad.

Every A'Space ChatGPT session must:

1. bootstrap from V3 before reconstructing architecture from chat history;
2. maintain a bounded tool-call wave budget;
3. checkpoint durable state before context reliability degrades;
4. switch surfaces when one tool surface is degraded instead of freezing the whole mission;
5. preserve the same evidence/acceptance standard across handovers;
6. never use context pressure as justification for lower-quality, incomplete or technician-only work.

## Local resume bootstrap

When local access is available, first establish:

- root: `C:/Users/amado/ASpace_OS_V3`
- `MEMORY.md`
- `40_Memory_Wiki_OKF/AGENTS.md`
- latest relevant file in `_INBOX/handoffs/`
- `ASPACE_ACTIVE_INTENTS.yaml`
- `ASPACE_WORKSPACE_REGISTRY.json`
- current Git HEAD/status/worktrees
- Supabase IPBD/WorkGraph execution truth
- Linear status for the lane
- GitHub PR/branch evidence

A missing path caused by branch/worktree visibility is repaired at Git level. A new memory directory is never invented.

## Tool-call wave governor

A single session wave has a **soft ceiling of 24 external tool actions**, deliberately below a practical ~50-call burst.

- **0–15 calls:** normal execution.
- **16th call:** create an internal checkpoint: what changed, evidence, unresolved items, next atomic outcome.
- **22nd call:** no new scope. Finish only the current atomic mutation/verification.
- **24th call:** stop new tool calls, persist durable handover/evidence, return a compressed checkpoint and request `GO Vague suivante` if more execution is needed.

The number is a context-safety budget, not a productivity cap. Parallel/batched safe reads are preferred over serial micro-calls.

## Context reliability blockers

Block the **current session wave**, not the user goal, when one or more occur:

- two repeated unrelated tool timeouts/failures with no new evidence;
- tool outputs are repeatedly truncated and required facts are no longer recoverable cheaply;
- the session begins restating or rediscovering facts already present in V3 memory/handover;
- contradictory state appears across surfaces and provenance has not yet been reconciled;
- the next action would mutate multiple surfaces without a durable checkpoint;
- the session crosses the 24-call wave limit;
- a write target is not on the canonical branch/worktree expected by the lane.

On a blocker: persist state, name the next lane/action, and continue in a fresh or peer session. Do not ask A0 to restate known architecture.

## Degraded-surface rule

A failing surface is not a global gate.

Example:
- if Desktop Commander is temporarily degraded, continue through GitHub/Supabase/Linear where the operation is safe and canonical;
- record the degraded surface;
- reconcile local state later before claiming local completion.

No alternate SSOT is created during fallback.

## Acceptance

A replacement ChatGPT session can resume with no hidden conversational dependency, know the local environment, know when to split execution into another wave, and continue at the same evidence standard without A0 repeating the system.
