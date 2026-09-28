#!/usr/bin/env bash
set -e

RUNTIME_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CACHE_DIR="$RUNTIME_DIR/.cache"
MIROFISH_DIR="$CACHE_DIR/mirofish-cli"
VENV_DIR="$CACHE_DIR/venv"
# Pinning to the HEAD of main branch as discovered (or the latest stable commit)
UPSTREAM_URL="https://github.com/SCTY-Inc/mirofish-cli.git"
UPSTREAM_COMMIT="3e98e776cdfc9556c12ace82a60e9d3da5bd41e7"

echo "Setting up MiroFish runtime..."

# Require Python >=3.11, <3.13
PY_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
if awk "BEGIN {exit !($PY_VERSION >= 3.11 && $PY_VERSION < 3.13)}"; then
    echo "Python version $PY_VERSION is valid."
else
    echo "ERROR: Python version must be >=3.11 and <3.13. Found: $PY_VERSION"
    exit 1
fi

mkdir -p "$CACHE_DIR"

if [ ! -d "$MIROFISH_DIR" ]; then
    echo "Cloning upstream MiroFish ($UPSTREAM_URL)..."
    git clone "$UPSTREAM_URL" "$MIROFISH_DIR"
else
    echo "MiroFish repository already exists at $MIROFISH_DIR."
fi

echo "Pinning to commit $UPSTREAM_COMMIT..."
cd "$MIROFISH_DIR"
git fetch origin
git checkout "$UPSTREAM_COMMIT"
cd "$RUNTIME_DIR"

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating isolated Python venv at $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    echo "Python venv already exists."
fi

echo "Installing requirements..."
source "$VENV_DIR/bin/activate"
pip install hatchling hatch-vcs uv
# We can also just use uv for faster and reliable installation
uv pip install -e "$MIROFISH_DIR"

echo "Setup complete."
