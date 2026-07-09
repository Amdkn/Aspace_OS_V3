---
source: Claude Code A2 (CC-M3)
date: 2026-06-21
type: handoff
domain: L0
tags: [mcp, transcript-api, restart, d6-fix, oauth, thin-proxy]
---

# Handoff — MCP transcript-api restart (2026-06-21)

> **A0 mandate** : "D6 transcript-api MCP restart — quick win, débloque Item 5 du cycle 12WY Q3 2026 (YouTube → Geordi LD01-LD08 pipeline)."
>
> **Status** : ✅ FIXED. `mcp__transcript-api__*` is operational via new Python proxy. A0 needs to **restart Claude Code** to load the updated `.mcp.json`.

---

## §1 — D6 Root cause

**Symptom** (screenshot A0 2026-06-21) : 9 MCPs ✔ Connected, 1 ✗ Failed = `mcp__transcript-api__*`.

**D1 verify** the `.mcp.json` block (line 114-123) :

```json
"transcript-api": {
  "command": "npx",
  "args": [
    "-y",
    "mcp-remote@latest",
    "https://transcriptapi.com/mcp",
    "--header",
    "Authorization: Bearer sk_Ajtxu29isCP9YMAGpPG6IMQ1rKnsI4VnaYvcHOQnxJo"
  ]
}
```

**D6 root cause** : `mcp-remote@latest` is a generic OAuth discovery client. It assumes the upstream is an OAuth-protected MCP server. It hangs on `transcriptapi.com` because:

1. The server **does** declare OAuth via `WWW-Authenticate: Bearer resource_metadata="https://transcriptapi.com/.well-known/oauth-protected-resource"` (D1 verified via `curl -I`).
2. The `.well-known/oauth-authorization-server` endpoint IS reachable (D1 verified) — it advertises authorization_code flow, not client_credentials.
3. **`mcp-remote` waits for an OAuth callback (port 6440) which never arrives** because A0 is not running an OAuth flow — A0 only has a static Bearer key.

D1 evidence: spawned `npx -y mcp-remote@latest` standalone, got:
```
[12216] Fatal error: TypeError: Invalid URL
[26168] Using transport strategy: sse-only
[26168] Using custom headers: {"Authorization":"Bearer sk_..."}
[26168] Discovering OAuth server configuration...
[hangs indefinitely]
```

Meanwhile, **direct Bearer works** (D1 verified):
- `POST /mcp initialize` → `200 OK`, `serverInfo.name="Transcript API" v2.13.1`
- `POST /mcp tools/list` → `200 OK`, **6 tools** : `get_youtube_transcript, search_youtube, get_channel_latest_videos, search_channel_videos, list_channel_videos, list_playlist_videos`
- `POST /mcp tools/call get_channel_latest_videos @mkbhd` → `200 OK`, 28 066 chars of real data (Marques Brownlee channel, 15 latest videos, 2026-06-16 latest)

The Bearer is valid. The server is alive. **Only the client bridge is wrong.**

---

## §2 — Fix shipped

### §2.1 New MCP proxy : `mcp-transcript-api.py`

Created at `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_B_runtime\04_mcps\mcp-transcript-api.py` (158 lines, follows Python coding-style: type annotations, immutable dataclasses not used here, logging, ADR-META-001 D1-D8 anchors, no hardcoded secrets).

**Pattern** : thin stdio↔HTTPS JSON-RPC forwarder. Sibling to the 5 other Symphony Lane B proxies (`mcp-supabase.py`, `mcp-baserow.py`, `mcp-affine.py`, `mcp-obsidian.py`, `mcp-plane.py`).

**Auth** : `TRANSCRIPT_API_KEY` env var User scope (Test Key Pragma, no hardcode). Bearer in `Authorization` header on every upstream POST. Required scope = `mcp:access` (from WWW-Authenticate probe).

**Boot flow** :
1. Probe upstream `tools/list` → cache tool descriptors.
2. Expose them as local MCP `Tool` objects with the same names + inputSchema.
3. Forward every `tools/call` verbatim via `httpx.AsyncClient.post(...)` → decode SSE `data:` line → return as TextContent.

### §2.2 Token in User env scope

```powershell
[Environment]::SetEnvironmentVariable('TRANSCRIPT_API_KEY', 'sk_Ajtxu29isCP9YMAGpPG6IMQ1rKnsI4VnaYvcHOQnxJo', 'User')
```

### §2.3 `.mcp.json` updated

```diff
- "transcript-api": {
-   "command": "npx",
-   "args": ["-y", "mcp-remote@latest", "https://transcriptapi.com/mcp", "--header", "Authorization: Bearer sk_..."]
- }
+ "transcript-api": {
+   "command": "C:/Python314/python.exe",
+   "args": ["-u", "C:/Users/amado/ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony/L1/lane_B_runtime/04_mcps/mcp-transcript-api.py"],
+   "env": { "TRANSCRIPT_API_KEY": "${env:TRANSCRIPT_API_KEY}" }
+ }
```

12 server entries total (was 12 too, transcript-api swap = same slot, just rewritten).

---

## §3 — D1 receipts (verify before assert)

### §3.1 Token set
```
$ [Environment]::SetEnvironmentVariable('TRANSCRIPT_API_KEY','sk_…','User')
TRANSCRIPT_API_KEY set in User scope
```

### §3.2 Proxy smoke (initialize + tools/list)
```
=== initialize ===
<<< transcript-api-mcp v1.26.0
[transcript-api-mcp] INFO: Booting transcript-api MCP proxy → https://transcriptapi.com/mcp
[transcript-api-mcp] INFO: HTTP Request: POST https://transcriptapi.com/mcp "HTTP/1.1 200 OK"
[transcript-api-mcp] INFO: Discovered 6 upstream tool(s): ['get_youtube_transcript', 'search_youtube', 'get_channel_latest_videos', 'search_channel_videos', 'list_channel_videos', 'list_playlist_videos']
[transcript-api-mcp] INFO: Processing request of type ListToolsRequest
{"jsonrpc":"2.0","id":2,"result":{"tools":[…6 tool descriptors with full inputSchema…]}}
```

### §3.3 Proxy live call (D1 receipt : real upstream data)
```
=== tools/call get_channel_latest_videos @mkbhd ===
<<< OK 28066 chars
{
  "content": [{
    "type": "text",
    "text": "{\"content\":{\"channel\":{\"channelId\":\"UCBJycsmduvYEL83R_U4JriQ\",\"title\":\"Marques Brownlee\",…
    \"results\":[{\"videoId\":\"WOzcFkld6_g\",\"title\":\"The Most Interesting Displays In The World!\",
    \"channelId\":\"UCBJycsmduvYEL83R_U4JriQ\",\"author\":\"Marques Brownlee\",
    \"published\":\"2026-06-16T18:17:15+00:00\",…
```

### §3.4 D7 lesson shipped (anti-rederivation)

**D7 lesson #11** : **OAuth discovery client ≠ Bearer client**. When an upstream MCP advertises OAuth via `WWW-Authenticate` but the client only has a static Bearer key, generic OAuth-bridge libraries (`mcp-remote`, `mcp-proxy`) will hang on metadata discovery because they assume the client intends to participate in the OAuth flow. **Fix pattern** = thin JSON-RPC forwarder (httpx POST + SSE decode) with the Bearer injected directly, bypassing the OAuth dance. Same lesson applies to any future MCP where the upstream does OAuth for browser users but accepts static Bearer for server-to-server.

**D7 lesson #12** (extension of #11 in handoff_mcp_durable_config_2026-06-16 §2.6) : **bypass pattern for "OAuth-capable but Bearer-friendly" upstreams** = write a ~150-line Python proxy that POSTs directly with `Authorization: Bearer`. Cost = 30 min one-time. Savings = re-discovering why mcp-remote hangs every time someone wires a new API key. Shipped as canonical Symphony Lane B pattern at `symphony/L1/lane_B_runtime/04_mcps/`.

---

## §4 — A0 action required

1. **Restart Claude Code** to load the updated `.mcp.json` (CC tool registry = static at session start, D6 #4 from `handoff_mcp_add_omk_abc_2026-06-17`).
2. **Verify** post-restart : `mcp__transcript-api__*` should appear in tool list with 6 tools (names above).
3. **Test Key Pragma phase 4** : rotate `sk_Ajtxu29isCP9YMAGpPG6IMQ1rKnsI4VnaYvcHOQnxJo` in `https://transcriptapi.com` console (D7 cost-of-escalation : not urgent, ship the fix first, rotate in next session).
4. **Cycle 12WY Q3 Item 5** : now unblocked. Resume YouTube → Geordi LD01-LD08 pipeline via `mcp__transcript-api__get_youtube_transcript` + `search_youtube` + `get_channel_latest_videos`.

---

## §5 — Files touched (D4 append-only, no hard-delete)

**Created** :
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_B_runtime\04_mcps\mcp-transcript-api.py` (158 lines, the proxy)
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_mcp_transcript_api_restart_2026-06-21.md` (THIS HANDOFF)
- `/tmp/test_mcp_remote.js`, `/tmp/proxy_smoke.ps1`, `/tmp/proxy_call.py`, `/tmp/proxy_call2.ps1`, `/tmp/proxy_call3.py` (transient test harnesses, in /tmp = not committed)

**Modified** :
- `C:\Users\amado\.mcp.json` (line 114-123 : `transcript-api` block rewritten, 12 entries total, structure preserved)

**Env var set** :
- `TRANSCRIPT_API_KEY` User scope (value sk_Ajtxu29isCP9YMAGpPG6IMQ1rKnsI4VnaYvcHOQnxJo, type=string, scope=User)

**Trashed** : n/a (no removals)

**Not modified** (D4 no-tamper) :
- `handoff_mcp_durable_config_2026-06-16.md` (history, DO NOT TOUCH)
- `handoff_mcp_persistence_v2_2026-06-16.md` (history, DO NOT TOUCH)
- `handoff_mcp_supabase_twin_live_2026-06-17.md` (history, DO NOT TOUCH)
- `handoff_mcp_add_omk_abc_2026-06-17.md` (history, DO NOT TOUCH)

---

## §6 — Related

- `handoff_mcp_durable_config_2026-06-16.md` §2.6 — D7 lesson on `_npx\` cache (different root cause, same .mcp.json symptom of "MCP failed").
- `handoff_mcp_persistence_v2_2026-06-16.md` §3 — Symphony Lane B proxy pattern (the architecture this fix follows).
- `handoff_mcp_add_omk_abc_2026-06-17.md` §D6 #4 — CC tool registry = static at session start, A0 must restart.
- `wiki/log.md` — append 1-line entry for this handoff (D4 append-only).
- `MEMORY.md` — append 1-line pointer under "MCP" topic row (D4 append-only).
- Cycle 12WY Q3 2026 (06/15 → 09/07/26) Item 5 : now unblocked.
