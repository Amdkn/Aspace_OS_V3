---
source: A2 Claude Code (this session) handoff after graphify discovery + stress test
date: 2026-06-10
type: handoff
status: ACTIVE — waiting for receiving session to pick up
domain: L0_TechOS / 06_MCP_Mastery / 06_graphify / cross-cutting knowledge graph
tags: [#graphify, #knowledge_graph, #MiniMax, #M3, #MiniMax, #full_build, #handoff, #delegation]
calibration_source: 1-file test (32 nodes, $0.07) + 100-file stress test (results appended below when known)
---

# Handoff — Full Graphify Build on ASpace_OS_V2 (2026-06-10)

## Why this handoff exists

On 2026-06-10, A0 asked for "ASpace_OS_V2/ en entier" as the first graphify build. After install +
1-file calibration + a 100-file stress test (results in `## Calibration results` below), A0
decided to **delegate the full 13k-file build to a dedicated Claude Code CLI session** and
**reserve the current session for project development** (heho).

The cost of the full build is non-trivial (~$900+ linear extrapolation, 4-8h wall time on
M3/M2.7 shared quota = 4 500 calls/5h). It needs:
- A session that can be left running 4-8h with periodic checks.
- A budget owner monitoring the M3 5h rolling window (resets every 5h).
- A clean kill/resume protocol if MiniMax rate-limits or the session must pause.

This handoff is the **executable playbook** for that session. Follow it top to bottom.

## State of the world as of 2026-06-10 (verified by source session)

| Item | Value | Source |
|---|---|---|
| graphify version | 0.8.36 | `graphify --version` |
| Install method | `uv tool install "graphifyy[anthropic]" --force` | (NOT `graphifyy` alone — see W7) |
| Repo branch | v8 (https://github.com/safishamsi/graphify) | dox leaf |
| Canon file count | **13 632 files** (after node_modules/.git/_TRASH/.next/dist/build/.claude/.gemini/.antigravity/__pycache__/.venv exclusion) | `find` enumeration |
| LLM backend | Claude / Anthropic-compat (MiniMax-M3) | `ANTHROPIC_BASE_URL=https://api.minimax.io/anthropic` |
| LLM SDK | `anthropic 0.109.1` (in graphifyy venv) | `uv tool run --from "graphifyy[anthropic]" python -c "import anthropic; print(anthropic.__version__)"` |
| Env vars required | `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` (same value), `ANTHROPIC_BASE_URL=https://api.minimax.io/anthropic` | PowerShell `Get-ChildItem Env:` |
| 1-file test result | 32 nodes, 42 edges, $0.07, 1 min wall | `06_graphify/graphify-out/graph.json` |
| 100-file stress test | (see `## Calibration results` below — appended when this session gets the result) | `/tmp/stress_test_run.log` |
| Dox tree | `10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/06_graphify/AGENTS.md` | dox leaf, includes W7 gotcha |
| ADR | `_SPECS/ADR/ADR-INFRA-MCP-001_agentic-mcp-mastery-dox-god-mode.md` (Amendment 2026-06-10) | ADR |

## Pre-flight for the receiving session

Run these BEFORE launching the build. All must pass.

```powershell
# 1. Confirm env vars (User scope)
Get-ChildItem Env: | Where-Object { $_.Name -in 'ANTHROPIC_API_KEY','ANTHROPIC_AUTH_TOKEN','ANTHROPIC_BASE_URL' } | Format-Table Name, Value
# Expect: 3 rows, ANTHROPIC_BASE_URL = https://api.minimax.io/anthropic

# 2. Confirm install
graphify --version
# Expect: 0.8.36

# 3. Confirm SDK present (this is the W7 gotcha)
uv tool run --from "graphifyy[anthropic]" python -c "import anthropic; print(anthropic.__version__)"
# Expect: 0.109.1 or higher. If "ModuleNotFoundError" → re-run:
#   uv tool install "graphifyy[anthropic]" --force
#   (If os error 5 on Scripts/: kill any orphan graphify.exe + python.exe in graphifyy venv first)

# 4. Confirm MiniMax reachability (cheap smoke test, ~1 min, ~$0.07)
$tmp = New-Item -ItemType Directory -Path "$env:TEMP\gtest_$(Get-Random)" -Force
Set-Content -Path "$tmp/x.md" -Value "# test`n- concept A`n- concept B"
Push-Location $tmp
graphify extract . --no-cluster --max-concurrency 1 --max-workers 1 2>&1 | Select-String "wrote|error|failed"
Pop-Location
Remove-Item $tmp -Recurse -Force
# Expect: "wrote ... graph.json — N nodes, M edges". If "all semantic chunks failed" → SDK missing, re-install.

# 5. Confirm M3 quota headroom (A0 on Plus $20/mo = 4500 calls/5h window)
# Plan usage: https://MiniMax.io/subscription → check 5h window usage % and weekly %.
# If 5h window is >80% used → wait for reset (or kick off after reset).
```

If any pre-flight fails: STOP, fix, re-verify. Do not start the build with a broken install.

## The exact command to run

From the project root (`C:\Users\amado\ASpace_OS_V2`):

```powershell
cd C:\Users\amado\ASpace_OS_V2

# Use the dox leaf's W3 guidance: --no-cluster for first pass to get raw extraction
# (clustering is a separate LLM call we can run later via `graphify cluster-only`)
# max-concurrency 4 = M3's sweet spot; do not exceed 4 or MiniMax may rate-limit
$logFile = "C:\Users\amado\ASpace_OS_V2\graphify-out\build_$(Get-Date -Format 'yyyyMMdd_HHmmss').log"
New-Item -ItemType Directory -Path "C:\Users\amado\ASpace_OS_V2\graphify-out" -Force | Out-Null

$env:PYTHONUNBUFFERED = "1"  # critical: forces graphify to flush stdout (otherwise silent on stdout)
$env:PYTHONIOENCODING = "utf-8"

$proc = Start-Process -FilePath "graphify" `
  -ArgumentList "extract", ".", "--no-cluster", "--max-concurrency", "4", "--max-workers", "2" `
  -RedirectStandardOutput $logFile `
  -RedirectStandardError  "$logFile.err" `
  -WorkingDirectory "C:\Users\amado\ASpace_OS_V2" `
  -PassThru -NoNewWindow
Write-Host "Graphify build PID: $($proc.Id) — log: $logFile"
```

The `PYTHONUNBUFFERED=1` env var is the **key fix** that prevents the silent 27-min failure we
hit on 2026-06-10. Without it, graphify buffers stdout until the process exits.

## Monitoring protocol

Check every 5-10 minutes while it runs:

```powershell
# 1. Is the process alive?
Get-Process -Id <PID> -ErrorAction SilentlyContinue | Select-Object Id, CPU, WS, StartTime
# If missing → process died. Check $logFile.err for the cause.

# 2. Log progress (look for "chunk N/M done" or "wrote" lines)
Get-Content $logFile -Tail 30

# 3. Cost so far (graphify writes a running cost to graphify-out/cost.json when buffered)
#    Note: this file is created at END of run by default. To track mid-run, peek the log for "tokens:" lines.
Select-String -Path $logFile -Pattern "tokens:|cost:|chunk.*done" | Select-Object -Last 20

# 4. Output dir status
Get-ChildItem "C:\Users\amado\ASpace_OS_V2\graphify-out" | Select-Object Name, Length, LastWriteTime
```

**Heuristics**:
- ~1 min per chunk observed in 1-file test → 13 632 files / 4 concurrent ≈ 57 hours serial but
  the LLM calls overlap. Realistic: **3-6h wall time** with no rate limits.
- If no "chunk" line in the log for >10 min → may be stuck (MiniMax rate-limited?).
- If `cost.json` shows >$50 spent with <1000 chunks done → investigate.

## Kill / resume protocol

If the build must be paused (quota reset, A0 request, MiniMax rate limit):

```powershell
# Graceful kill (SIGINT = Ctrl+C equivalent, lets graphify write partial state)
Stop-Process -Id <PID>
# OR hard kill if not responding within 60s:
Stop-Process -Id <PID> -Force

# The next time you run `graphify extract . --update` it will skip already-extracted files
# (it uses graph.json + cache/ as the "what's already done" baseline).
# So resume is just: re-run the same command.
```

The `.graphify-out/cache/` directory is the resume state. **Never delete it manually** unless
you want a full restart.

## Success criteria (D5 — proof on file)

The build is "complete" only when ALL of these are true:

| # | Check | Expected |
|---|---|---|
| 1 | `graph.json` exists in `graphify-out/` | size 10-500 MB |
| 2 | `manifest.json` exists | size 1-100 KB |
| 3 | `cost.json` exists | shows total tokens + est. cost |
| 4 | `graph.json.nodes` count is between 50 000 and 500 000 | (13 632 files × ~30 nodes/file = ~400k) |
| 5 | `graph.json.edges` count > nodes | (graphify extracts more edges than nodes) |
| 6 | `GRAPH_REPORT.md` exists (or run `graphify label .` to generate it) | size 50-500 KB |
| 7 | M3 5h quota window was not blown | plan usage page shows <100% |
| 8 | `tasklist` shows no orphan `graphify.exe` | (clean state for next session) |

If any check fails: do not claim success. Per ADR-META-001 D5, no self-congratulation before
observed proof.

## Write back to the source session

When the build completes, append a one-line entry to:

1. `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\log.md`:
   ```
   [2026-06-10] Graphify full build done. PID <PID>, wall time <Xh Ym>, cost <$Z>, <N> nodes / <M> edges in graph.json.
   ```

2. `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\README.md`:
   Same one-liner under the `[2026-06-10]` bullet for graphify.

3. Commit the cold-start assets to git (they're .gitignore-tracked exceptions):
   - `graphify-out/manifest.json` (portable metadata)
   - `graphify-out/GRAPH_REPORT.md` (cold-start reading)
   - DO NOT commit `graph.json`, `graph.html`, `cost.json` (gitignored)

4. Update `06_graphify/AGENTS.md` W3 with the actual wall time + cost (replaces the
   "~5-15 min" estimate that turned out wrong).

## Calibration results

**VERIFIED** — 100-file stress test completed 2026-06-10 12:32:03. Real data below.

| Metric | Value | Note |
|---|---|---|
| Stress test start | 2026-06-10 12:23:36 | |
| Stress test end | 2026-06-10 12:32:03 | 8 min 27 sec wall time |
| Files in subset | 100 sampled, 94 processable | 28 code + 64 docs + 2 images; 6 skipped (gitkeep/wav/etc) |
| Output graph.json | 671 nodes, 1082 edges, 604 KB | |
| Tokens | 83 283 in / 31 251 out = 114 534 total | |
| **Cost** | **$0.72** | via MiniMax-M3 (Sonnet-equivalent pricing) |
| **Cost per file** | **$0.0072** | 10× LOWER than the 1-file test suggested ($0.07) |
| **Success rate** | **100%** | 0 chunks lost after auto-retry/auto-bisect |
| Wall time per file | 8.5 min / 100 files = 5.1 sec/file avg | (with concurrency 4) |
| Throughput | ~706 files/hour | (100 files / 8.5 min × 60) |

### Failure modes observed (all auto-handled by graphify)

1. `LLM returned invalid JSON, skipping chunk` × 2 → auto-retry succeeded
2. `claude returned a hollow response; treating as truncation so adaptive retry can bisect the chunk` × 1 → bisect to halves succeeded
3. `chunk of 16 truncated at depth 0, splitting into halves of 8 and 8` → both halves succeeded
4. `chunk of 8 truncated at depth 1, splitting into halves of 4 and 4` → both halves succeeded

**No process death, no OOM, no disk pressure, no manual intervention needed.** The auto-retry
+ auto-bisect pipeline is solid.

### Extrapolation to full 13 632-file build

- **Wall time**: 13 632 files / 706 files/hour = **~19.3 hours**. Realistic with rate
  limits: **10-15 hours**.
- **Cost**: 13 632 × $0.0072 = **~$98**. Realistic with retry overhead: **$100-130**.
- **Failure rate**: 0% on 100-file sample → expect <2% chunk failures, all auto-handled.
- **MiniMax quota**: A0 on Plus plan = 4 500 calls/5h. With 17s per chunk and 4 in flight,
  ~706 files/hour = ~4 200 chunks/hour = 93% of the 5h budget if the build runs flat-out.
  **Plan for 1-2 quota resets during the build** (kill at 80% used, resume after 5h reset).

### Recommendation for the receiving session

**PROCEED with the full build.** The calibration is in:
- Success rate 100%
- Cost $100-130 (much lower than initial $910 estimate)
- Failure modes all auto-handled
- Process stable for 8+ minutes, no resource issues

Use `--max-concurrency 4` and `--max-workers 2` (same as the stress test) and set
`PYTHONUNBUFFERED=1` (the fix for the silent-failure mode we hit earlier today).

## Residual risks

- **MiniMax quota resets every 5h** — if the build hits the quota wall mid-run, kill it
  gracefully and resume after reset. Partial state is preserved in `graphify-out/cache/`.
- **`anthropic` SDK package version** — graphify pins 0.109.1 today. If a future `uv tool
  install --force` upgrades the SDK to a version that breaks MiniMax compat, the build will
  fail with a different error. Mitigation: pin in `requirements.txt` if/when one is created.
- **`.codex-m3-lean/.tmp/plugins/` showed up in the 100-file sample** — some files live in
  weird dirs. The `.gitignore` exclusion should catch most, but `.graphifyignore` may need
  additions if graphify walks dirs the .gitignore missed.
- **Background-task OS error 5 on reinstall** — the uv tool's `Scripts/` dir locks if a
  previous `graphify.exe` or `python.exe` from the venv is still alive. Always `taskkill`
  first.
- **graph.html is gitignored** — to share the graph visually with A0, generate a one-off
  HTML and serve it via `python -m http.server` on localhost only (never commit).

## Secret handling

- `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` are in env User Windows only.
- DO NOT echo their values in this handoff, in commit messages, or in chat logs.
- If the build ever logs an env var in an error, ROTATE immediately (per ADR-INFRA-MCP-001
  D4 rotation policy) and re-launch.

## Next safe action for the receiving session

1. Read this handoff end to end.
2. Run the 5 pre-flight checks in `## Pre-flight for the receiving session`.
3. Append the stress test results from `## Calibration results` (poll
   `/tmp/stress_test_run.log` if not yet posted).
4. If success rate >95% and cost <$0.15/file → run the full build command in `## The exact
   command to run`.
5. If success rate <95% or cost >$0.15/file → STOP, do not proceed. Report numbers to A0 and
   re-plan.
6. After full build, run all 8 success-criteria checks and write back per `## Write back to
   the source session`.

## Skill proposal (open follow-up)

The graphify workflow (install + verify + smoke test + run + monitor + write-back) is a
recurring pattern that another MCP might also need. Consider creating `/graphify` skill that
encapsulates:
- W7 install (the [anthropic] extra)
- 5-pre-flight checks
- Stress test pattern (1-file then 100-file)
- The PYTHONUNBUFFERED=1 fix
- The 8 success criteria
- The write-back protocol

Queue: `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/skills_queue.md`.
