# Bill DISCOVER — Scout vs Deep-Capture Contract

## Principle
Discovery has two different jobs and they must not collapse into one context-hungry step.

### Layer S0 — SCOUT
Goal: identify **what deserves investigation now**.

Preferred candidate: `last30days`.

Inputs:
- research question
- recency window / as-of
- source allowlist
- budget
- known entities/aliases

Outputs:
- candidate sources
- timestamps/recency
- engagement/momentum as *signal only*
- source health/status
- gaps
- recommended deep-capture action

Forbidden:
- asserting truth from engagement
- architectural mutation
- memory promotion
- side effects beyond bounded research cache

### Layer S1 — DEEP CAPTURE
Goal: establish **what the selected source actually supports**.

Primitives:
- WATCH for video transcript + targeted frames
- TranscriptAPI fallback
- yt-dlp/ffmpeg local media evidence
- paper/PDF extraction
- repo/commit/issue inspection
- primary documentation

Outputs:
- source-native evidence
- claim refs
- contradictions
- provenance
- confidence

### Layer S2 — DISCOVERY PACKET
Goal: turn evidence into an A'Space-consumable research object.

Outputs:
- claims
- novelty vs V3
- contradictions/cautions
- candidate capabilities
- CapabilityNeeds
- evidence refs
- handover

## Routing rule
`SCOUT` proposes where to look.
`DEEP CAPTURE` proves what is there.
`Graham` decides what may persist.
`Clara/Ryan/Nardole` decide what may change.

No layer inherits authority merely because an upstream score is high.
