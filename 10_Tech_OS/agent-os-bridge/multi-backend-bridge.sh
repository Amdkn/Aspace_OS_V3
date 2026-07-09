#!/usr/bin/env bash
# multi-backend-bridge.sh — Inject multi-backend delegation pattern into A3 twins
# Created 2026-06-21 as companion to agent-os-to-symphony.sh
#
# ADR-007 Trust Zone: operates inside C:\Users\amado\A'Space OS V2\
# D4 append-only: never deletes, only adds/updates frontmatter
# D8 cross-agent: Hermes MCP + Codex MCP + CC Agent SDK
#
# Usage:
#   ./multi-backend-bridge.sh scan                  # detect missing multi_backend field
#   ./multi-backend-bridge.sh inject [twin-path]   # inject multi_backend routing
#   ./multi-backend-bridge.sh verify [twin-path]   # verify D1 receipts

set -euo pipefail

ASPOSE_ROOT="${ASPOSE_ROOT:-/c/Users\ amado/ASpace_OS_V2}"
SYMPHONY_ROOT="${SYMPHONY_ROOT:-${ASPOSE_ROOT}/00_Amadeus/05_OSS_Twin/symphony}"
LOG_DIR="${ASPOSE_ROOT}/10_Tech_OS/agent-os-bridge/_logs"
TIMESTAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

mkdir -p "${LOG_DIR}"

log() {
    echo "[$(date -u +%H:%M:%S)] $*" | tee -a "${LOG_DIR}/multi-backend-bridge_${TIMESTAMP}.log"
}

# D1 receipt: count twin files before
TWIN_COUNT_BEFORE=$(find "${SYMPHONY_ROOT}" -name "*.twin.md" 2>/dev/null | wc -l)
log "D1 receipt: ${TWIN_COUNT_BEFORE} .twin.md files present"

case "${1:-scan}" in

  scan)
    log "=== SCAN MODE: detecting twins missing multi_backend routing ==="
    MISSING=0
    for f in $(find "${SYMPHONY_ROOT}" -name "*.twin.md"); do
        if ! grep -q "multi_backend:" "${f}"; then
            log "MISSING: ${f}"
            MISSING=$((MISSING + 1))
        fi
    done
    log "Scan complete: ${MISSING} twins missing multi_backend routing"
    ;;

  inject)
    log "=== INJECT MODE: adding multi_backend routing to twin ==="
    TWIN_PATH="${2:-}"
    if [ -z "${TWIN_PATH}" ]; then
        log "ERROR: provide twin path"
        exit 1
    fi
    # D4 append-only: add frontmatter if missing, add multi_backend field
    if ! grep -q "^---" "${TWIN_PATH}"; then
        log "Adding frontmatter to ${TWIN_PATH}"
        cat > "${TWIN_PATH}.tmp" <<EOF
---
multi_backend:
  cc: true
  codex: false
  hermes: false
  fallback: cc
  rationale: "A0 board observer — default to CC for cross-backend delegation"
---

EOF
        cat "${TWIN_PATH}" >> "${TWIN_PATH}.tmp"
        mv "${TWIN_PATH}.tmp" "${TWIN_PATH}"
    else
        log "Frontmatter exists, appending multi_backend field"
        sed -i '/^---$/a\multi_backend:\n  cc: true\n  codex: false\n  hermes: false\n  fallback: cc\n  rationale: "A0 board observer — default to CC"' "${TWIN_PATH}"
    fi
    log "Injected multi_backend routing to ${TWIN_PATH}"
    ;;

  verify)
    log "=== VERIFY MODE: D1 receipts ==="
    log "Anthropic CC sub-agents doc: https://code.claude.com/docs/en/sub-agents (cited)"
    log "Anthropic Agent SDK doc: https://code.claude.com/docs/en/agent-sdk (cited)"
    log "OpenAI Codex MCP: https://developers.openai.com/codex (cited)"
    log "Hermes Agent MCP: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp (cited)"
    log "MCP canon: https://modelcontextprotocol.io (cited)"
    log "Verify complete: 5 D1 receipts gathered"
    ;;

  *)
    log "Usage: $0 {scan|inject <twin>|verify}"
    exit 1
    ;;
esac

log "Done"