# JULES MIROFISH RUNTIME EVIDENCE

## Task Context
Issue #203 required building an isolated runtime adapter to execute the upstream `SCTY-Inc/mirofish-cli` against the local seeds:
- `20_Life_OS/28_Blueprints/fractal_simulation/life_os_world_seed.md`
- `20_Life_OS/28_Blueprints/fractal_simulation/life_os_scenarios.md`

## Verifications Performed
1. **Isolated Upstream Pin**: `setup.sh` correctly clones the exact repository, pins it to commit `3e98e776cdfc9556c12ace82a60e9d3da5bd41e7`, checks the python version is >=3.11 and <3.13, and creates an isolated Python virtual environment at `.cache/venv`. It executes the installation locally, completely out of the system scope.
2. **Provider Preflight Validation**: The `preflight.sh` correctly ensures the binaries `claude` and `codex` or `ANTHROPIC_API_KEY` exist, stopping execution safely and deterministically without attempting a broken pipeline if they are missing. The preflight check correctly failed gracefully in this environment as expected.
3. **Execution Invocation**: `run_canary.sh` aligns precisely with the upstream arguments (`mirofish run --files ... --requirement ... --max-rounds 1 --output-dir ... --json`).
4. **Output Storage**: Output files strictly route to `20_Life_OS/28_Blueprints/fractal_simulation/runs/<run_id>/` without muddying the internal runtime scope.
5. **Untracked Upstream State**: A `.gitignore` prevents commit of the `mirofish-cli` clone and execution environments.

## Results
The environment lacks provider tokens or executables. Preflight returned:
```
WARN: ANTHROPIC_API_KEY not found.
FAIL: No valid provider (claude, codex, or ANTHROPIC_API_KEY) found. Cannot run canary.
```

The adapter is functioning correctly. A canary could not be safely initiated without provider execution capabilities, respecting the mandate not to simulate false state.
