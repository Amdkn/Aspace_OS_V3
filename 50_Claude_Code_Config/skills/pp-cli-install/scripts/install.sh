#!/usr/bin/env bash
# pp-cli-install (Linux/macOS variant)
# Mirror of install.ps1 for portability. On Windows, prefer install.ps1.
# Usage:
#   ./install.sh <service> [--spec <url> | --docs <url>] [--force]

set -euo pipefail

SERVICE="${1:-}"
shift || true
SPEC_URL=""
DOCS_URL=""
FORCE=0

while [[ $# -gt 0 ]]; do
    case "$1" in
        --spec) SPEC_URL="$2"; shift 2 ;;
        --docs) DOCS_URL="$2"; shift 2 ;;
        --force) FORCE=1; shift ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

if [[ -z "$SERVICE" ]]; then
    echo "Usage: $0 <service> [--spec URL | --docs URL] [--force]"
    exit 1
fi

# Platform detection for bin dir
case "$(uname -s)" in
    Darwin) BIN_DIR="$HOME/Library/Application Support/pp-clis" ;;
    *)      BIN_DIR="$HOME/.local/bin/pp-clis" ;;
esac
mkdir -p "$BIN_DIR"

PP_EXE="$(command -v printing-press || echo "$HOME/.local/bin/printing-press")"
CLI_NAME="${SERVICE}-pp-cli"
CLI_EXE="$BIN_DIR/$CLI_NAME"

if [[ -f "$CLI_EXE" && $FORCE -eq 0 ]]; then
    echo "[pp-cli-install] $CLI_NAME already installed at $CLI_EXE (use --force to reinstall)"
    "$CLI_EXE" --version | head -1 || true
    exit 0
fi

# Probe upstream
CATEGORIES=(ai auth cloud commerce developer-tools devices education food-and-dining marketing media-and-entertainment monitoring other payments productivity project-management sales-and-crm social-and-messaging travel)
FOUND_CAT=""
for cat in "${CATEGORIES[@]}"; do
    if curl -sf "https://api.github.com/repos/mvanhorn/printing-press-library/contents/library/$cat/$SERVICE" -o /dev/null; then
        FOUND_CAT="$cat"
        echo "[pp-cli-install] Found in category: $cat"
        break
    fi
done

OS_TAG="$(uname -s | tr '[:upper:]' '[:lower:]')"
ARCH_TAG="$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/')"

if [[ -n "$FOUND_CAT" ]]; then
    URL="https://github.com/mvanhorn/printing-press-library/releases/download/${SERVICE}-current/${SERVICE}-pp-cli-${OS_TAG}-${ARCH_TAG}"
    echo "[pp-cli-install] Downloading $URL"
    curl -fsSL -o "$CLI_EXE" "$URL"
    chmod +x "$CLI_EXE"
else
    echo "[pp-cli-install] Not in upstream; generating locally."
    if [[ ! -x "$PP_EXE" ]]; then
        echo "[pp-cli-install] ERROR: printing-press not installed"; exit 2
    fi
    OUT_DIR="$HOME/printing-press/library/$SERVICE"
    if [[ -n "$SPEC_URL" ]]; then
        "$PP_EXE" generate --spec "$SPEC_URL" --name "$SERVICE" --output "$OUT_DIR"
    elif [[ -n "$DOCS_URL" ]]; then
        echo "[pp-cli-install] WARN: --docs consumes LLM quota"
        "$PP_EXE" generate --docs "$DOCS_URL" --name "$SERVICE" --output "$OUT_DIR"
    else
        echo "[pp-cli-install] ERROR: need --spec or --docs for unknown service"; exit 2
    fi
    pushd "$OUT_DIR" > /dev/null
    go mod tidy
    for d in cmd/*/; do
        name=$(basename "$d")
        echo "[pp-cli-install] Building $name"
        go build -o "$name" "./cmd/$name"
        cp "$name" "$BIN_DIR/"
        chmod +x "$BIN_DIR/$name"
    done
    popd > /dev/null
fi

echo "[pp-cli-install] Smoke test --help"
"$CLI_EXE" --help | head -5

# Note: settings.json registration is Windows-only; skipped on Linux/macOS.
# Wiki log append could be added here if running in A'Space WSL.

echo "[pp-cli-install] DONE — $CLI_NAME installed at $CLI_EXE"
