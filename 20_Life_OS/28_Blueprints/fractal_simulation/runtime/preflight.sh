#!/usr/bin/env bash
set -e

RUNTIME_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CACHE_DIR="$RUNTIME_DIR/.cache"
VENV_DIR="$CACHE_DIR/venv"

echo "Running preflight checks for MiroFish..."

# Check if venv exists
if [ ! -d "$VENV_DIR" ]; then
    echo "ERROR: Venv not found. Run setup.sh first."
    exit 1
fi

source "$VENV_DIR/bin/activate"

# Provider verification
HAS_PROVIDER=0
echo "Checking providers..."

if [ -n "$ANTHROPIC_API_KEY" ]; then
    echo "OK: ANTHROPIC_API_KEY found."
    HAS_PROVIDER=1
else
    echo "WARN: ANTHROPIC_API_KEY not found."
fi

if command -v claude > /dev/null; then
    echo "OK: claude found."
    HAS_PROVIDER=1
fi

if command -v codex > /dev/null; then
    echo "OK: codex found."
    HAS_PROVIDER=1
fi

if [ "$HAS_PROVIDER" -eq 0 ]; then
    echo "FAIL: No valid provider (claude, codex, or ANTHROPIC_API_KEY) found. Cannot run canary."
    echo "Please set up a provider and try again."
    exit 1
fi

# Check mirofish installation
if ! command -v mirofish > /dev/null; then
    echo "FAIL: mirofish not found in venv. Setup may have failed."
    exit 1
fi

echo "Verifying MiroFish entrypoint:"
mirofish --version

echo "Preflight complete. System is ready."
exit 0
