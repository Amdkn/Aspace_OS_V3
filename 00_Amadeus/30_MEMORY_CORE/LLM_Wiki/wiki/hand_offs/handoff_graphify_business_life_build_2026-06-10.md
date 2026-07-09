---
source: A2 Claude Code (this session) handoff after Business OS smoke test (9 files, $0.1289)
date: 2026-06-10
type: handoff
status: ACTIVE — waiting for A0 to open new session after M3 quota reset
domain: L0_TechOS / 06_MCP_Mastery / 06_graphify / cross-cutting knowledge graph
tags: [#graphify, #knowledge_graph, #MiniMax, #M3, #Business_OS, #Life_OS, #handoff, #smoke_test, #quota_reset]
predecessor: handoff_graphify_full_build_2026-06-10.md (full repo build, NOT to be confused with this scoped version)
---

# Handoff — Graphify Build on Business OS + Life OS (scoped, 2026-06-10)

## Why this handoff exists

A0 scoped the original full-repo build (13 632 files, ~$100, 10-15h) to **just two sub-directories** for faster turnaround and lower quota exposure:

- `C:\Users\amado\ASpace_OS_V2\30_Business_OS` (844 canonical files after graphify auto-exclusion)
- `C:\Users\amado\ASpace_OS_V2\20_Life_OS` (3 841 canonical files after graphify auto-exclusion)

A0 then said: **"Attendre reset quota"** (wait for M3 5h quota reset, currently 50% used, resets in **2h49** at time of writing). After reset → run Business OS first, then Life OS in sequence.

The reasoning: avoid rate-limit mid-build, and since the build is sequential + non-urgent, the 2h49 wait costs nothing relative to the 7.8h wall time.

## State of the world as of 2026-06-10 (verified by source session)

| Item | Value | Source |
|---|---|---|
| graphify version | 0.8.36 | `graphify --version` |
| Install method | `uv tool install "graphifyy[anthropic]" --force` | (NOT `graphifyy` alone — see W7 from predecessor) |
| Repo branch | v8 (https://github.com/safishamsi/graphify) | dox leaf |
| Smoke test result | **9 files, 59 nodes, 76 edges, $0.1289, 107s wall** | this session |
| Per-file cost | **$0.0143** (verified on 9-file sample) | smoke test |
| Throughput | **~300 files/hour** (max-concurrency 2) | smoke test |
| LLM backend | Claude / Anthropic-compat (MiniMax-M3) | `ANTHROPIC_BASE_URL=https://api.minimax.io/anthropic` |
| LLM SDK | `anthropic 0.109.1` (in graphifyy venv) | `uv tool run --from "graphifyy[anthropic]" python -c "import anthropic; print(anthropic.__version__)"` |
| Env vars | `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_BASE_URL` (User scope) | PowerShell `Get-ChildItem Env:` |
| M3 quota at handoff time | 50% used, reset in 2h49 | A0 reported 2026-06-10 |
| M3 weekly limit | 52% used, reset in 4d6h | A0 reported 2026-06-10 |
| Predecessor handoff | `handoff_graphify_full_build_2026-06-10.md` (full repo, ~$100, 10-15h) | still valid for later |

## Scope (D3 — what to actually point graphify at)

```powershell
# Scope 1 (run first):
"C:\Users\amado\ASpace_OS_V2\30_Business_OS"

# Scope 2 (run after Scope 1 completes):
"C:\Users\amado\ASpace_OS_V2\20_Life_OS"
```

graphify's `_SKIP_DIRS` (in `detect.py`) auto-excludes `node_modules`, `.next`, `dist`, `build`, `.git`, `__pycache__`, `target`, `out`, `site-packages`, `graphify-out`, and ~20 other build/cache dirs. The 206k raw files in Business OS reduce to **844** canonical via this auto-exclusion. **No manual exclusion needed.**

## Pre-flight for the receiving session

```powershell
# 1. Confirm env vars (User scope) — 3 rows expected
Get-ChildItem Env: | Where-Object { $_.Name -in 'ANTHROPIC_API_KEY','ANTHROPIC_AUTH_TOKEN','ANTHROPIC_BASE_URL' } | Format-Table Name, Value

# 2. Confirm install
graphify --version
# Expect: 0.8.36

# 3. Confirm SDK present (W7 gotcha)
uv tool run --from "graphifyy[anthropic]" python -c "import anthropic; print(anthropic.__version__)"
# Expect: 0.109.1 or higher. If "ModuleNotFoundError":
#   uv tool install "graphifyy[anthropic]" --force
#   (If os error 5 on Scripts/: taskkill any orphan graphify.exe + python.exe in graphifyy venv first)

# 4. Confirm M3 quota has reset (https://MiniMax.io/subscription → 5h window)
# Expect: 5h window <50% used. If >80% → STOP, wait for next reset.

# 5. Optional smoke re-check (1 file, ~$0.014, ~10s)
# Skip if M3 quota is fine; the smoke test in this handoff is already verified.
```

If any pre-flight fails: STOP, fix, re-verify. Do not start with broken install or blown quota.

## The exact commands to run

### Build #1 — Business OS (1.4h, ~$12)

```powershell
$env:ASPACE_ROOT = "C:\Users\amado\ASpace_OS_V2"
Set-Location $env:ASPACE_ROOT

$logFile = "$env:ASPACE_ROOT\graphify-out\business_build_$(Get-Date -Format 'yyyyMMdd_HHmmss').log"
New-Item -ItemType Directory -Path "$env:ASPACE_ROOT\graphify-out" -Force | Out-Null

$env:PYTHONUNBUFFERED = "1"   # critical: prevents 27-min silent failure
$env:PYTHONIOENCODING = "utf-8"

$proc = Start-Process -FilePath "graphify" `
  -ArgumentList "extract", "30_Business_OS", "--no-cluster", "--max-concurrency", "4", "--max-workers", "2" `
  -RedirectStandardOutput $logFile `
  -RedirectStandardError  "$logFile.err" `
  -WorkingDirectory $env:ASPACE_ROOT `
  -PassThru -NoNewWindow
Write-Host "Business OS build PID: $($proc.Id) — log: $logFile"
```

**Why `--max-concurrency 4` and not 2**: smoke test used 2 (cautious). The handoff predecessor validated 4 is M3's sweet spot — does not rate-limit. With 4 the wall time drops from 2.8h to **~1.4h**.

### Build #2 — Life OS (6.4h, ~$55)

Run AFTER Build #1 completes. Same flags, just different scope and new log filename:

```powershell
$env:ASPACE_ROOT = "C:\Users\amado\ASpace_OS_V2"
Set-Location $env:ASPACE_ROOT

$logFile = "$env:ASPACE_ROOT\graphify-out\life_build_$(Get-Date -Format 'yyyyMMdd_HHmmss').log"

$env:PYTHONUNBUFFERED = "1"
$env:PYTHONIOENCODING = "utf-8"

$proc = Start-Process -FilePath "graphify" `
  -ArgumentList "extract", "20_Life_OS", "--no-cluster", "--max-concurrency", "4", "--max-workers", "2" `
  -RedirectStandardOutput $logFile `
  -RedirectStandardError  "$logFile.err" `
  -WorkingDirectory $env:ASPACE_ROOT `
  -PassThru -NoNewWindow
Write-Host "Life OS build PID: $($proc.Id) — log: $logFile"
```

## Monitoring protocol (D6 — concrete, idempotent)

```powershell
# Replace <PID> with the actual PID printed at build start.

# 1. Process alive?
Get-Process -Id <PID> -ErrorAction SilentlyContinue | Select-Object Id, CPU, WS, StartTime
# If missing → check $logFile.err for cause

# 2. Tail of stdout (look for "chunk N/M done" or "wrote" lines)
Get-Content $logFile -Tail 30

# 3. Cost so far (parsed from log "tokens: / est. cost:" lines)
Select-String -Path $logFile -Pattern "tokens:|cost:|chunk.*done" | Select-Object -Last 20

# 4. Output dir
Get-ChildItem "$env:ASPACE_ROOT\graphify-out" | Select-Object Name, Length, LastWriteTime
```

**Heuristics**:
- ~12s per file observed in 9-file smoke test → 844 files / 4 concurrent ≈ **1.4h wall time** for Business OS.
- 3 841 / 4 ≈ **6.4h wall time** for Life OS.
- If no "chunk" line in the log for >10 min → may be stuck (M3 rate-limited?).
- If cumulative cost >$15 with <200 chunks done → investigate.

## Kill / resume protocol

```powershell
# Graceful kill (lets graphify write partial state)
Stop-Process -Id <PID>
# OR hard kill if not responding within 60s:
Stop-Process -Id <PID> -Force

# Resume is just: re-run the same `graphify extract ...` command
# graphify skips files already in graph.json + cache/ — no work lost.
```

**Never delete** `.graphify-out/cache/` manually unless you want a full restart.

## Success criteria (D5 — proof on file)

Build is "complete" when ALL of these are true (run for each scope):

| # | Check | Expected for Business OS | Expected for Life OS |
|---|---|---|---|
| 1 | `graph.json` exists in `graphify-out/` | size 5-50 MB | size 25-200 MB |
| 2 | `manifest.json` exists | size 1-50 KB | size 5-100 KB |
| 3 | `cost.json` exists | total ~$12 | total ~$55 |
| 4 | `graph.json.nodes` count is between 5 000 and 50 000 | (844 files × ~25-30 nodes/file ≈ 25k) | (3 841 × ~25-30 ≈ 100k) |
| 5 | `graph.json.edges` count > nodes | (yes, graphify extracts more edges) | (yes) |
| 6 | `GRAPH_REPORT.md` exists (or run `graphify label <path>`) | size 50-500 KB | size 100-1000 KB |
| 7 | M3 5h quota window not blown | usage <100% at end of each build | usage <100% at end of each build |
| 8 | `tasklist` shows no orphan `graphify.exe` | (clean state) | (clean state) |

If any check fails: do not claim success. Per ADR-META-001 D5, no self-congratulation before observed proof.

## Write back to the source session / log

When both builds complete, append to:

1. `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\log.md`:
   ```
   [2026-06-10] Graphify scoped build (Business OS + Life OS) done. Business: PID <PID>, <Xh Ym>, $A, <N1> nodes / <M1> edges. Life: PID <PID>, <Xh Ym>, $B, <N2> nodes / <M2> edges.
   ```

2. `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\README.md`:
   Same one-liner under the `[2026-06-10]` bullet for graphify.

3. Commit cold-start assets to git (gitignored exceptions):
   - `graphify-out/manifest.json` (×2 — one per build)
   - `graphify-out/GRAPH_REPORT.md` (×2)
   - DO NOT commit `graph.json`, `graph.html`, `cost.json`

4. Update `06_graphify/AGENTS.md` W3 with actual wall times + costs (replaces the "~5-15 min" estimate that was wrong for full repo).

5. Mark this handoff as CONSUMED: rename to `handoff_graphify_business_life_build_2026-06-10_CONSUMED.md` and move into `wiki/hand_offs/sessions_archive/` (per no-hard-delete doctrine).

## Residual risks (D6 — explicit)

- **M3 quota reset timing**: if Build #1 takes 1.4h and you start near the end of the 5h window, the window can roll over and double-count some calls. Mitigation: start Build #1 with at least 2h left in the window. Start Build #2 only after Build #1 finishes (so the next 5h window starts clean).
- **`anthropic` SDK 0.109.1** — graphify pins this. If a future `uv tool install --force` upgrades, the build may fail. Mitigation: do not reinstall graphify between Build #1 and Build #2.
- **Long wall time (6.4h for Life OS)** — the session running this must stay alive. Don't close the terminal/IDE during the build. If interrupted, the cache resume (in `.graphify-out/cache/`) is intact and the re-run picks up where it stopped.
- **M3 rate-limit hit mid-build** — auto-retry will catch most (per predecessor handoff: 100% success in 100-file stress test). If the log goes silent for >10 min with no "chunk done" lines, kill and resume.

## Secret handling (no change from predecessor)

- `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` are in env User Windows only.
- DO NOT echo their values in this handoff, in commit messages, or in chat logs.
- If the build ever logs an env var in an error, ROTATE immediately (per ADR-INFRA-MCP-001 D4 rotation policy) and re-launch.

## Next safe action for the receiving session

1. Read this handoff end to end.
2. Check M3 quota on https://MiniMax.io/subscription. If 5h window <50% used, proceed. If >80%, wait for next reset.
3. Run Build #1 (Business OS). Save the PID printed.
4. Monitor every 5-10 min while Build #1 runs. If silent >10 min, kill and resume.
5. After Build #1's 8 success criteria pass, run Build #2 (Life OS). Same monitoring.
6. After Build #2 passes, run the 5 write-back steps above.
7. Total expected: ~$67, ~7.8h wall time, <2% chunk failure rate (all auto-handled).
