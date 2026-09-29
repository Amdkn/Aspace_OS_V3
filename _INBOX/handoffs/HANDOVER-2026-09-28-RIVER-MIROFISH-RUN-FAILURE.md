# HANDOVER — 2026-09-28 — RIVER / MIROFISH RUN FAILURE → AUTH CAPABILITY NEED

## Result
The bounded MiroFish run was actually executed after RuntimePreflight PASS.

Run:
- `run_e822ad0b523e`
- immutable evidence: `20_Life_OS/28_Blueprints/fractal_simulation/runs/river_canary_20260929T000442Z/`
- upstream: `SCTY-Inc/mirofish-cli@3e98e776cdfc9556c12ace82a60e9d3da5bd41e7`
- max rounds requested: 1
- process-group supervision: yes
- exit: `1`
- failed step: **ontology**
- rounds executed: **0**
- `report/verdict.json`: **absent**

Therefore `SOH-142` remains **Backlog / UNTESTED**. No SIMULATED or STRUCTURAL_RISK projection is justified yet.

## Provider discrimination completed
1. WSL Codex `0.150.1`: direct canary reproduced HTTP **401 Unauthorized / missing authentication**.
2. Windows Codex `0.153.4`: `codex login status` reports ChatGPT login, but execution proves the refresh token is invalidated; the existing local configuration also expects `FREELLMAPI_API_KEY`, which was not read or reused.
3. Claude Code `2.1.222` default: configured `z-ai/glm-5.3-flash[1m]` is inaccessible (404).
4. Claude Code explicit `haiku`: terminates `aborted_streaming` with zero tokens.

No supported provider is currently end-to-end healthy.

## CapabilityNeed
Type: `authenticated_supported_llm_provider`.
Boundary: human authentication/configuration, not MiroFish code.

Preferred recovery:
- reauthenticate **one** provider only;
- preferred candidate: Windows Codex because the binary is installed, selected, and its failure is now explicit;
- after authentication, run a tiny provider canary; only exit 0 reopens the MiroFish cell.

Do not:
- patch MiroFish to manufacture a pass;
- retrieve/reuse historical API keys;
- send this to Jules as a code patch;
- mutate Linear/Supabase;
- rerun installation diagnostics.

## Exact reentry
Reuse the same seed hashes:
- world: `0239c2d4dce2ff4a708f4c04faa66c2a2c7e073117ab0a32425ce9726b1137ed`
- scenarios: `60d40c61225689f1f10697ef41e2134bd08fb415eb8b43294d3f161cb053333e`

Then rerun exactly one MiroFish round using process-group supervision.
Success gate remains: immutable run + `report/verdict.json` + exit 0 + HarnessExecutionReceipt.
Return success evidence to Rory for reconciliation, then Amy presentation.

## Evidence
- `10_Tech_OS/reports/river_mirofish_runtime_preflight_20260928.json`
- `10_Tech_OS/reports/river_mirofish_run_receipt_20260928.json`
- failed immutable run directory above.
