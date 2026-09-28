#!/usr/bin/env bash
set -e

RUNTIME_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CACHE_DIR="$RUNTIME_DIR/.cache"
VENV_DIR="$CACHE_DIR/venv"
RUN_ID=$(date +%Y%m%d_%H%M%S)
# Run outputs belong under 20_Life_OS/28_Blueprints/fractal_simulation/runs/<run_id>/
OUTPUT_DIR="$RUNTIME_DIR/../runs/$RUN_ID"

echo "Preparing canary run: $RUN_ID"

if [ ! -d "$VENV_DIR" ]; then
    echo "ERROR: Venv not found. Run setup.sh first."
    exit 1
fi

if ! "$RUNTIME_DIR/preflight.sh"; then
    echo "ERROR: Preflight failed. Cannot run canary."
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

source "$VENV_DIR/bin/activate"

SEED_WORLD="$RUNTIME_DIR/../life_os_world_seed.md"
SEED_SCENARIOS="$RUNTIME_DIR/../life_os_scenarios.md"

echo "Executing MiroFish canary..."
mirofish run \
    --files "$SEED_WORLD" "$SEED_SCENARIOS" \
    --requirement "Execute 1-round structural canary simulation against provided seeds." \
    --max-rounds 1 \
    --output-dir "$OUTPUT_DIR" \
    --json

echo "Canary run complete. Output saved to $OUTPUT_DIR"
exit 0
