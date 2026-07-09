---
source: LLM_Wiki_A0
date: 2026-06-11
type: comparison
domain: A0_Sovereign / Browser_Automation / MCP_Selection
tags: [#Playwright #Chrome_DevTools #MCP #Puppeteer #Capability_Matrix]
---

# Playwright MCP vs Chrome DevTools MCP — D1 Capability Matrix

**Companion sources:**
- [[source_chrome_devtools_mcp]] — Chrome DevTools MCP D1 source
- [[concept_playwright_cli_vs_mcp]] — architectural decision context

**A0 decision status (2026-06-11)** : **NOT YET DECIDED**. Both MCPs available. Install gated on A0 explicit GO.

---

## TL;DR

| | Playwright MCP | Chrome DevTools MCP |
|---|---|---|
| **Browser** | Chromium + Firefox + WebKit | Chrome only |
| **Engine** | Playwright | Puppeteer |
| **Tools** | 23 core + opt-in caps | ~50 across 9 categories |
| **Token economy** | MCP mode = heavy / CLI = light | MCP mode = heavy / CLI = light |
| **Cross-browser** | ✅ | ❌ |
| **Perf traces** | ❌ | ✅ (3 tools + CrUX) |
| **Lighthouse** | ❌ | ✅ |
| **Heap snapshots** | ❌ | ✅ (8 tools) |
| **Auto-connect to running Chrome** | ❌ | ✅ (`--autoConnect`) |
| **Coding-agent optimized** | ✅ (a11y tree, no vision) | ✅ (Chrome-specific) |
| **Token-economy CLI option** | ✅ (microsoft/playwright-cli) | ✅ (cli.md, no separate skill repo) |
| **A0 sovereignty flags needed** | None | 3 opt-outs (--no-usage-statistics, --no-performance-crux, CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS) |

**Verdict** : **70% redondant, 30% complémentaire**. Install both if A0 has bandwidth; install only Playwright MCP if budget-constrained; install only Chrome DevTools MCP if A0's L0 perf/memory use case is acute.

---

## Full Capability Matrix (D1 verified)

### Browser & Engine

| Capability | Playwright MCP | Chrome DevTools MCP |
|------------|----------------|---------------------|
| Engine | Playwright (Node.js) | Puppeteer (Node.js) |
| Chromium | ✅ | ✅ |
| Firefox | ✅ | ❌ |
| WebKit (Safari) | ✅ | ❌ |
| Edge | ✅ (Chromium-based) | ✅ (Chromium-based) |
| Mobile emulation | ✅ | ✅ (emulate tool) |
| iPhone Safari (real) | ✅ (WebKit) | ❌ |

### Core Automation (overlap = HIGH)

| Capability | Playwright MCP | Chrome DevTools MCP |
|------------|----------------|---------------------|
| Click | `browser_click` | `click` |
| Fill | `browser_fill_form`, `browser_type` | `fill`, `fill_form`, `type_text` |
| Navigate | `browser_navigate` | `navigate_page` |
| Tabs/pages | `browser_tabs` | `list_pages`, `new_page`, `select_page`, `close_page` |
| Screenshots | `browser_take_screenshot` | `take_screenshot` |
| Console | `browser_console_messages` | `get_console_message`, `list_console_messages` |
| Network | `browser_network_request(s)` (opt-in) | `get_network_request`, `list_network_requests` |
| Snapshot (a11y tree) | `browser_snapshot` | `take_snapshot` |
| Evaluate JS | `browser_evaluate`, `browser_run_code_unsafe` | `evaluate_script` |
| Drag, drop, hover, press_key | ✅ all | ✅ all |
| Upload file | `browser_file_upload` | `upload_file` |
| Resize | `browser_resize` | `resize_page` |
| Dialog handling | `browser_handle_dialog` | `handle_dialog` |
| Wait | `browser_wait_for` | `wait_for` |

**Redundancy verdict** : for ~12 of these common operations, both MCPs work equivalently. Choose by browser scope.

### Differentiator Capabilities (the 30% non-overlapping)

| Capability | Playwright MCP | Chrome DevTools MCP | A'Space use case |
|------------|----------------|---------------------|------------------|
| **Performance traces** | ❌ | ✅ 3 tools + CrUX field data | L0 deploy-verify, L2 e2e-pr LCP/CLS check |
| **Lighthouse audit** | ❌ | ✅ `lighthouse_audit` | L0 deploy-verify post-deploy score |
| **Heap snapshots** | ❌ | ✅ 8 variants | L2 debugging memory leaks in heavy apps |
| **Chrome extensions** | ❌ | ✅ 5 tools (install, trigger, etc.) | Niche — testing internal extension |
| **Auto-connect running Chrome** | ❌ | ✅ `--autoConnect` | L2 linkedin-prospect uses A0's signin state |
| **WebMCP** | ❌ | ✅ 2 tools | Emerging — TBD |
| **Screencast (live stream)** | ❌ | ✅ `screencast_start/stop` | Real-time LLM context |
| **PDF export** | ✅ `browser_pdf_save` (opt-in) | ❌ | L0 archive compliance |
| **Storage (cookies, localStorage)** | ✅ opt-in | Not listed | Equivalent or different |
| **DevTools annot/highlight** | ✅ opt-in (`browser_annotate`, etc.) | Not listed | Visual debug |
| **Vision-based (pixel input)** | ✅ opt-in (`browser_mouse_*`) | ✅ `click_at` | Equivalent |
| **Tracing (record/replay)** | ✅ opt-in (start/stop tracing, video) | Via perf trace | Different abstraction |
| **PDF** | ✅ opt-in | ❌ | L0 archive |

### Coding-Agent Optimization

| Aspect | Playwright MCP | Chrome DevTools MCP |
|--------|----------------|---------------------|
| **LLM-friendly design** | ✅ accessibility tree (no vision) | ✅ Chrome-specific tools |
| **CLI option for token economy** | ✅ [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | ✅ `chrome-devtools <tool>` (cli.md) |
| **CLI Skill repo** | ✅ official (microsoft/playwright-cli) | ⚠️ no separate Skill repo, just `docs/cli.md` |
| **State model** | MCP = persistent, CLI = stateless | Both modes available |
| **MCP vs CLI positioning** | README: "CLI+SKILLS is better for high-throughput coding agents" | Not explicit, but CLI mode provided |
| **Recommended for token-economy** | ✅ confirmed by maintainers | ⚠️ implied by CLI mode existence |

### Sovereignty / Privacy (D3)

| Aspect | Playwright MCP | Chrome DevTools MCP |
|--------|----------------|---------------------|
| **Telemetry by default** | Unknown (need to check) | ✅ YES (Google, opt-out available) |
| **Sends data to 3rd party** | Likely minimal | ✅ CrUX API + npm update checks + usage stats |
| **Opt-out flags** | TBD | ✅ `--no-usage-statistics`, `--no-performance-crux`, `CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS` |
| **Self-hostable** | ✅ (npx, no SaaS dependency) | ✅ (npx, no SaaS dependency besides CrUX) |
| **A0 sovereignty concern** | Low | Medium (needs explicit opt-out config) |

---

## Decision Tree for A0

```
Need cross-browser (Firefox/Safari)?
  → YES: Playwright MCP (or CLI)
  → NO: continue ↓

Need perf traces, Lighthouse, heap snapshots, or auto-connect to running Chrome?
  → YES: Chrome DevTools MCP (in ADDITION to Playwright MCP)
  → NO: continue ↓

Want minimal tool surface for token-economy batch Q/A?
  → YES: Playwright CLI + future Skill (microsoft/playwright-cli)
  → NO: continue ↓

A0 sovereignty concern about Google telemetry?
  → YES: Install Chrome DevTools MCP with --no-usage-statistics --no-performance-crux
  → NO: default install OK
```

**A0's A'Space current state** (2026-06-11) :
- `plugin:playwright:playwright` ✅ connected (built-in, 23 tools)
- Chrome DevTools MCP ❌ not installed
- Playwright CLI ❌ not installed
- microsoft/playwright-cli Skill ❌ not installed

**Path forward** (gated on A0) :
1. **Minimal** : keep current Playwright MCP, document concept page (DONE 2026-06-11), defer all
2. **Add Chrome DevTools MCP** : install with sovereignty flags for niche L0 perf
3. **Full path** : also install Playwright CLI for batch Q/A when needed, plus 7 L0/L1/L2 Skills (VETOed 2026-06-11)

---

## D1 Sources

- Playwright MCP README : https://github.com/microsoft/playwright-mcp (retrieved 2026-06-11)
- Chrome DevTools MCP README : https://github.com/ChromeDevTools/chrome-devtools-mcp (retrieved 2026-06-11)
- Chrome DevTools CLI docs : https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/cli.md (retrieved 2026-06-11)
- YouTube transcript (Captain America / Flash Product Q/A, shared by A0 in chat 2026-06-11)
- All claims marked ✅ are D1-verified from the above sources.
- All claims marked ⚠️ are HYPOTHESE non verifiee per ADR-META-001 D1.
