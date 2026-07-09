---
source: LLM_Wiki_A0
date: 2026-06-11
type: summary
domain: A0_Sovereign / Browser_Automation / DevTools
tags: [#Chrome_DevTools #MCP #Puppeteer #Performance #Heapsnapshot #Lighthouse #Claude_Agent]
---

# Chrome DevTools MCP — D1 Source Page

**Source:** Google Chrome DevTools team — https://github.com/ChromeDevTools/chrome-devtools-mcp
**Companion docs:** https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/cli.md
**License:** Apache-2.0 (per Playwright MCP observation; same family)
**Verdict for A'Space:** **COMPLÉMENTAIRE** to Playwright MCP, **pas redondant** (full breakdown: [[comparison_playwright_mcp_vs_chrome_devtools_mcp]])

---

## Core Thesis

> *"Chrome DevTools for coding agents. Lets AI coding assistants (Claude, Cursor, Copilot, Antigravity) control and inspect a live Chrome browser for automation, debugging, and performance analysis."*

The project uses **Puppeteer** (not Playwright) for browser automation. The differentiator is **deep Chrome DevTools Protocol access** — performance traces, heap snapshots, Lighthouse audits, real-user CrUX field data.

---

## Three Operating Modes

| Mode | Use case | Surface |
|------|----------|---------|
| **MCP server** (default) | Agent calls tools via MCP protocol | ~50 tools across 9 categories |
| **CLI** (`chrome-devtools <tool>`) | Scripts, shell pipelines, non-MCP workflows | Same tools via command line |
| **Slim** (`--slim --headless`) | Basic tasks only | 3 tools: navigate, evaluate_script, take_screenshot |

CLI key commands (from `docs/cli.md`):
- `chrome-devtools status | start | stop`
- `chrome-devtools list_pages | navigate_page | new_page | close_page`
- `chrome-devtools take_screenshot | click | fill`
- `chrome-devtools lighthouse_audit` ⭐ unique
- `--output-format=json` for programmatic use

**Daemon model** (CLI): first tool call auto-starts the MCP server + browser in background, persistent across calls. State survives between commands.

---

## Tool Inventory (D1 verified)

| Category | Count | Examples |
|----------|-------|----------|
| Input automation | 10 | click, drag, fill, fill_form, handle_dialog, hover, press_key, type_text, upload_file, click_at |
| Navigation | 6 | close_page, list_pages, navigate_page, new_page, select_page, wait_for |
| Emulation | 2 | emulate, resize_page |
| **Performance** ⭐ | 3 | performance_analyze_insight, performance_start_trace, performance_stop_trace |
| Network | 2 | get_network_request, list_network_requests |
| Debugging | 8 | evaluate_script, get_console_message, lighthouse_audit, list_console_messages, take_screenshot, take_snapshot, screencast_start/stop |
| **Memory** ⭐ | 8 | take_heapsnapshot (multiple variants) |
| Chrome extensions | 5 | install, list, reload, trigger_action, uninstall |
| Third-party | 2 | (specific integrations) |
| **WebMCP** ⭐ | 2 | (new emerging protocol) |

**~50 tools total** vs Playwright MCP's 23 core + opt-in. Chrome DevTools has more tools but Chrome-only.

---

## Browser Support

- **Officially:** Google Chrome + Chrome for Testing
- **Unofficially:** other Chromium browsers "may work, not guaranteed"
- **NOT supported:** Firefox, Safari, WebKit

**Implication A'Space** : if any L0/L1/L2 Skill needs cross-browser (e.g., iPhone Safari testing mentioned in YouTube transcript), Chrome DevTools MCP cannot cover that use case. Playwright remains the only option.

---

## Connection Modes (D1)

The server can either launch its own Chrome or connect to a running instance:

| Mode | Flag | Use case |
|------|------|----------|
| **Auto-connect** (Chrome 144+) | `--autoConnect` | Share state between manual and agent testing |
| **Remote debugging** | `--browserUrl=http://127.0.0.1:9222` | Sandboxed envs where LLM is separate from Chrome |
| **WebSocket** | `--wsEndpoint` + optional `--wsHeaders` | Authenticated WS connections |
| **Isolated profile** | `--isolated` | Independent temp Chrome profile per session |
| **Persistent profile** | default | Reuse cookies, signins, localStorage |

**A0 use case potential** : `--autoConnect` would let an L2 Sales Skill use **your real Chrome** (with your LinkedIn signin, your CRM cookies) without re-auth — significant productivity win if A0 wants agent-driven lead capture from already-authenticated sessions.

---

## Privacy / Telemetry (D1 honest)

**By default** (per README):
- Usage statistics sent to Google (tool invocation success rates, latency, env info)
- Update checks against npm registry
- Performance trace URLs may be sent to **Google CrUX API** for real-user field data

**Opt-outs**:
- `--no-usage-statistics` or `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS` or `CI` env var
- `CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS`
- `--no-performance-crux`

**Sovereignty flag (D3 nuance)** : for A0's sovereign OS context, default settings send data to Google. **Disable all 3 flags** before installing in Trust Zone. Worth documenting in any future Skill that wraps this MCP.

---

## What's Unique vs Playwright MCP (the 30%)

Capabilities **Playwright MCP does not have** but Chrome DevTools MCP does:

1. **Performance traces** with auto-analysis + CrUX field data fusion
2. **Lighthouse audit** (LCP, CLS, FCP, TBT, accessibility score)
3. **Heap snapshots** (8 variants — useful for memory leak debugging)
4. **Chrome extensions testing** (install, trigger, uninstall)
5. **Auto-connect to running Chrome** (share signin state)
6. **WebMCP** (emerging protocol — 2 tools)
7. **Screencast** (live stream browser to LLM context)

These map to specific A'Space use cases — see [[comparison_playwright_mcp_vs_chrome_devtools_mcp]].

---

## Install Path (Gated on A0)

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest",
        "--no-usage-statistics",
        "--no-performance-crux"
      ],
      "env": {
        "CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS": "1"
      }
    }
  }
}
```

Or via CLI: `claude mcp add chrome-devtools npx chrome-devtools-mcp@latest`

**Sovereignty config** (required for A0 Trust Zone):
- `--no-usage-statistics` (disables Google usage stats)
- `--no-performance-crux` (disables Google CrUX API field data fusion)
- `CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS=1` (disables npm update checks)

**Status (2026-06-11)** : ✅ **INSTALLED**. A0 GO at 2026-06-11. Edit applied to `C:\Users\amado\.mcp.json` with all 3 sovereignty flags. D1 verify via `node -e "require('...mcp.json')"` → JSON parse OK, 5 servers listed. Task #20 closed. **Activation** : requires Claude Code restart (`.mcp.json` is read at session start). After restart, `mcp__plugin_chrome-devtools_chrome-devtools__*` tools should appear in tool list. First smoke test recommended: `lighthouse_audit` on `https://abc.kalybana.com` (L0 deploy-verify use case).

---

## Related Wiki Pages

- [[concept_playwright_cli_vs_mcp]] — the architectural choice for A'Space
- [[comparison_playwright_mcp_vs_chrome_devtools_mcp]] — full capability matrix
- [[source_codex_session_jerry_summer_hermes_emyth_2026-06-03]] — earlier L2 design context

## Sources

- https://github.com/ChromeDevTools/chrome-devtools-mcp
- https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/cli.md
- WebFetched 2026-06-11 by Claude (CC agent session)
