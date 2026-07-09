---
title: Forbidden Words (Lexicon Guard)
---

> The output of any Symphony-driven agent is scanned against a
> forbidden word list. **No exceptions, no "but in this context…"**.

## Two sources

```yaml
# Global (every Symphony agent)
forbidden_lexicon_global:
  - "synergie"
  - "disrupter"
  - "innover"
  - "révolutionner"
  - "game-changer"
  - "best-of-breed"

# Per-workflow (Airtable field "Forbidden Words")
forbidden_lexicon_workflow:
  - source: airtable
    field: "Forbidden Words"   # comma-separated text
    example: "synergie, disrupter, scale, pivot"  # workflow-specific
```

## Two scopes

1. **Output scope** — the proof artifact (proposal, brief, summary).
   Hard fail = `BLOCKED` with `error: "forbidden_lexicon"`.
2. **Reasoning scope** — chain-of-thought / pulse.log internal text.
   Soft fail = `CONDITIONAL` with `warning: "lexicon_match_in_thoughts"`.

(Reasoning scope is checked but doesn't fail the tick — the agent might
be _thinking about_ the forbidden words in order to avoid them.)

## Check timing

- **Before writeback** — always
- **Before `greenlight_required: true` decision** — always
- **At agent output parsing** — always

## Check implementation

- Case-insensitive substring match (not whole-word — catches
  "synergies" too)
- Strip punctuation before match
- Allow technical uses (e.g., "innovation pipeline" in a tech doc
  footnote about lexique is fine if the agent is quoting the lexique
  itself — `meta_match: true` exemption)

## Why this exists

A0's pattern: "less is more". Buzzwords signal the agent is
hallucinating expertise. Catching them at the lexique = cheap insurance
against the agent producing marketing-fluff instead of business
substance.

## Anti-patterns

- ❌ Silently rewriting the forbidden word to a synonym (e.g.,
  "synergie" → "collaboration") — the agent should rephrase the
  **idea**, not substitute the word
- ❌ Adding "synergie" to a stop-list-comment in the prompt as
  workaround — doesn't fix the output
- ❌ Ignoring the lexique in "draft" mode — even drafts are read by
  humans

## Cross-refs

- `mission-contract.md` — `forbidden_words` field
- `gate-decisions.md` — `BLOCKED` on output scope fail
- `writeback-policy.md` — `allowed_draft_outputs` is checked separately
