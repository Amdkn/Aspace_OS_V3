# HANDOVER — 2026-09-28 — RIVER / MIROFISH RUNTIME PREFLIGHT → RUN CELL

## Origin and state
- Consumed Rory Project Source transfer **“Transfert MiroFish à River”** and physical handover `HANDOVER-2026-09-28-RIVER-HARNESS-WORKFLOW-MIROFISH.md`.
- Linear `SOH-142` remains **Backlog / UNTESTED**; GitHub continuity is #200.
- River worktree was reconciled cleanly to `origin/Amdkn/River@ce5bff73bd974b0f1b7611d8859542588dd40992` before this cell.
- No simulation, verdict, Linear mutation or Supabase mutation has occurred.

## Verifiable result — RuntimePreflight PASS
- Upstream: `SCTY-Inc/mirofish-cli@3e98e776cdfc9556c12ace82a60e9d3da5bd41e7`.
- WSL: `Ubuntu-24.04`; managed Python `3.11.16`; no global Python/deadsnakes change.
- Runtime venv: `/home/amdkn7/aspace_runtime/mirofish-cli-3e98e776/.venv311`, about 1.7G.
- MiroFish entrypoint PASS; OASIS import PASS; `torch=2.2.2+cpu`; `cuda=False`; `mcp=1.27.0`.
- Provider: actual `/home/amdkn7/.local/bin/codex`, `codex-cli 0.150.1`.
- Runtime-local diagnostic shim only: `.shim/codex-cli -> codex`; `mirofish doctor` = **all checks passed**.
- Evidence: `10_Tech_OS/reports/river_mirofish_runtime_preflight_20260928.json`.

## FLOW defects discovered and bounded
- README/pyproject claim Python 3.12, but `camel-oasis==0.2.5` requires Python <3.12.
- README claims `mirofish --version`; current CLI requires a subcommand.
- Doctor checks `codex-cli`, while the real LLM client executes `codex exec --skip-git-repo-check`.
- Unconstrained pip chose `mcp 2.2.0`; upstream `uv.lock` pins `mcp 1.27.0`, required for OASIS `FastMCP`.
- Critical: DC `force_terminate` killed the parent session but left child pip processes alive; two installs overlapped and contaminated the first venv with CUDA. The venv was discarded and rebuilt cleanly.
- New invariant for River harnessing: **parent liveness != child/background truth**; cancellation must target the whole process group.

## Exact next cell
Run one round only (max two if bounded diagnostic evidence requires it) using the canonical seeds in the shared root:
`20_Life_OS/28_Blueprints/fractal_simulation/life_os_world_seed.md` and `life_os_scenarios.md`.
Required chain: `SimulationRequest -> HarnessSelector -> RuntimePreflight(PASS) -> MiroFishRun -> ArtifactWait -> HarnessExecutionReceipt -> RoryReconcile -> AmyPresent`.
Required outputs: immutable run directory, `report/verdict.json`, exact command, stdout/stderr/exit, runtime/provider fingerprint and receipt.
Only Rory may project `UNTESTED -> SIMULATED` or `STRUCTURAL_RISK`; simulation never closes IPBD.
