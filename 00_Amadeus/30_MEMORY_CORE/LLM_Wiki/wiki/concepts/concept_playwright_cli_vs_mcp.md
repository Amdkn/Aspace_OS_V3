---
source: LLM_Wiki_A0
date: 2026-06-11
type: concept
domain: A0_Sovereign / Browser_Automation / Coding_Agent_Pattern
tags: [#Playwright #CLI #MCP #Skill #Token_Economy #Coding_Agent]
---

# Playwright CLI+SKILLS vs Playwright MCP — Architectural Choice

**Companion sources:**
- [[source_chrome_devtools_mcp]] — the alternative browser-automation MCP
- [[comparison_playwright_mcp_vs_chrome_devtools_mcp]] — full matrix
- YouTube transcript (Captain America / Flash Product Q/A 2026-06-11) — informal original source

**A0 status (2026-06-11)** : **VETO** on Skill Creator invocation. Documentation only. 7 Skills L0/L1/L2 restent candidats pour session future.

---

## Core Thesis

> *"Modern coding agents increasingly favor CLI-based workflows exposed as SKILLs over MCP because CLI invocations are more token-efficient."*
> — README microsoft/playwright-mcp, retrieved 2026-06-11

Playwright's own maintainers (Microsoft) **explicitly position CLI+SKILLS as the better choice for coding agents**, with MCP reserved for specialized stateful loops. This is the architectural foundation for any L0/L1/L2 wrapper Skill A0 designs.

---

## The Two Patterns

### Pattern A — MCP server (the 23 tools we already have)

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

- **Surface:** ~23 core tools + opt-in via `--caps` (config, network, storage, devtools, vision, pdf, testing)
- **State model:** persistent browser context across tool calls
- **Best for:** exploratory automation, self-healing tests, long-running autonomous workflows
- **Trade-off:** larger tool schemas + verbose accessibility trees loaded into model context → **more tokens per call**
- **Current A'Space:** `plugin:playwright:playwright` built-in (✅ connected, 23 tools)

### Pattern B — CLI + SKILL wrapper (token-economy mode)

```bash
# Direct CLI calls via Bash tool
npx playwright test --reporter=list
npx playwright codegen https://example.com
npx playwright screenshot https://example.com out.png
npx playwright open https://example.com
```

- **Surface:** CLI commands + a **Skill file** that orchestrates them with domain context
- **State model:** each call is independent; no persistent browser across Bash calls
- **Best for:** Q/A scripts, batch testing, CI/CD pipelines, atomic verifications
- **Trade-off:** loses stateful introspection; needs orchestration Skill to chain commands
- **Companion Skill:** [playwright-cli](https://github.com/microsoft/playwright-cli) (Microsoft, official)

---

## D1 — Microsoft's official positioning (verbatim)

From the Playwright MCP README, retrieved 2026-06-11:

> *"If you are using a **coding agent**, you might benefit using the [CLI+SKILLS](https://github.com/microsoft/playwright-cli) instead."*

On CLI advantages:
> *"CLI invocations are more token-efficient: they avoid loading large tool schemas and verbose accessibility trees into the model context, allowing agents to act through concise, purpose-built commands."*

On when MCP still wins:
> *"MCP remains relevant for specialized agentic loops that benefit from persistent state, rich introspection, and iterative reasoning over page structure, such as exploratory automation, self-healing tests, or long-running autonomous workflows."*

On long-term positioning:
> *"CLI+SKILLS is better suited for high-throughput coding agents that must balance browser automation with large codebases, tests, and reasoning within limited context windows."*

**D3 nuance** : the README frames MCP and CLI+SKILLS as **complementary, not competing**. A0's A'Space can use BOTH:
- MCP for interactive/exploratory (already built-in)
- CLI+SKILLS for batch Q/A (requires Skill wrapper)

---

## HYPOTHESE vs D1 (honest)

| Claim | Source | D1 status |
|-------|--------|-----------|
| MCP loads "large tool schemas" into context | Microsoft README | ✅ official |
| MCP loads "verbose accessibility trees" | Microsoft README | ✅ official |
| CLI is "more token-efficient" than MCP | Microsoft README | ✅ official claim, **unspecified magnitude** |
| "60-80% token economy" specific number | YouTube video (Captain America) | ⚠️ **HYPOTHESE non verifiee** — YouTuber opinion, not Microsoft |
| "MCP performs worse" generally | YouTube video | ⚠️ **HYPOTHESE non verifiee** — likely depends on use case |
| CLI is better for "high-throughput" agents | Microsoft README | ✅ official |
| MCP is better for "stateful, iterative" loops | Microsoft README | ✅ official |

**D5 honesty** : the architectural pattern is solid (D1). The specific token-savings number is hearsay. Treat "CLI is more token-efficient" as a direction, not as a 60-80% guarantee.

---

## The 7 Skills L0/L1/L2 vision (DEFERRED per A0 VETO 2026-06-11)

**Status:** A0 VETOed Skill Creator invocation. 7 Skills restent **concepts**, pas créés. Reprise gated sur A0 future intent.

### Mapping (D3 layer awareness)

| Skill | Couche | Guardian | Pattern | ROI estimé |
|-------|--------|----------|---------|-----------|
| `/l0-deploy-verify` | L0 | Rick / 13th Doctor | MCP (interactive) | ~15 min/sem |
| `/l0-watchdog-scrape` | L0 | 13th Doctor | CLI (batch) | ~70 min/sem |
| `/l1-research-pulse` | L1 | Beth / Discovery | CLI (batch) | ~45 min/sem |
| `/l1-weekly-snapshot` | L1 | Beth / SNW | MCP (interactive) | ~20 min/sem |
| `/l2-competitor-pulse` | L2 | Summer / Growth | CLI (batch) | ~20 min/sem |
| `/l2-e2e-pr` | L2 | Flash / Product | MCP (interactive) | ~30 min/sem |
| `/l2-linkedin-prospect` | L2 | John Jones / Sales | CLI + Chrome DevTools MCP for `--autoConnect` | ~60 min/sem |

**Total ROI** : ~4-5h/sem sauvées une fois opérationnel. Hystérésis : doit être exécuté sur vraies données A'Space pour confirmer.

### Decision rule for future Skill design

> **Default rule** : use CLI+SKILLS for batch Q/A (state-independent), use MCP for interactive exploration (state-dependent).
>
> **Override** : use Chrome DevTools MCP when the task requires perf traces, Lighthouse audits, heap snapshots, or auto-connect to a running Chrome (see [[source_chrome_devtools_mcp]]).

---

## Why A0 VETOed (D3 intent reading)

A0's actual message (2026-06-11, in French):
> *"Skill Creator VETO je voulais explorer les opportuniter avec Playwright documente le pour plustard et fait des recherces sur Chrome Dev tool MCp et CLI"*

Translated: "Skill Creator VETO, I wanted to explore the opportunities with Playwright, document it for later, and do research on Chrome DevTools MCP and CLI"

**Real intent** (D3 nuance over literal):
- Don't build the Skills now → **A0 is in exploration mode, not execution mode**
- Document Playwright properly so future sessions can pick it up → **knowledge capture priority over action**
- Research Chrome DevTools to see if it changes the calculus → **input needed before any Skill decision**

This is a **healthy Exploration-before-Commitment** pattern. A0 is not blocking the work, just sequencing: research first, document, decide later.

---

## Related Wiki Pages

- [[source_chrome_devtools_mcp]] — D1 facts on the alternative MCP
- [[comparison_playwright_mcp_vs_chrome_devtools_mcp]] — full matrix
- [[concept_sdd]] — the SDD pattern, could apply to Skill design
- [[source_karpathy-autoresearch]] — pattern of measurable improvement loops
