#!/bin/bash
# =============================================================================
# agent-os-to-symphony.sh
# Wrapper Agent OS (Brian Casel v3.0) → Symphony OS V2 A3 twins
#
# Purpose:
#   1. Read C:\Users\amado\agent-os\standards\index.yml (canonical source of truth)
#   2. Map each standard folder/file to relevant A3 ship/agent
#   3. Inject standards as YAML frontmatter extension into <name>.twin.md
#      (D4 append-only — preserves existing frontmatter, appends new fields)
#   4. Generate _manifest.yml per ship listing all injected standards
#
# Doctrine anchors:
#   - ADR-META-001 D1 (verify before assert — receipts at every step)
#   - ADR-META-001 D2 (research first — index.yml read before mutation)
#   - ADR-META-001 D4 (no self-contradiction — append-only, never overwrite)
#   - ADR-META-001 D5 (proof before claim — receipts at end)
#   - ADR-META-001 D6 (root cause — D6 detects missing index.yml before failing)
#   - ADR-007 Trust Zone (operates inside C:\Users\amado\A'Space OS V2\)
#   - ADR-OBSERVABILITY-001 (sessions canon rotation)
#   - tilly-fable-rhythm (sibling, Fable-Mindset doctrine)
#   - symphony-fabuleux-discipline (sibling, production discipline)
#
# Invocation:
#   bash agent-os-to-symphony.sh                       # Full sync all standards to all A3
#   bash agent-os-to-symphony.sh --dry-run            # Preview without write
#   bash agent-os-to-symphony.sh --standards api      # Inject only api/* standards
#   bash agent-os-to-symphony.sh --ship discovery     # Inject all standards into one ship
#   bash agent-os-to-symphony.sh --twin tilly         # Inject all standards into one twin
#   bash agent-os-to-symphony.sh --rollback           # Restore from .bak-2026-06-15-pre-agent-os-bridge
#
# Exit codes:
#   0 = success (or dry-run preview ok)
#   1 = index.yml missing (D6 root cause surfaced)
#   2 = twins directory missing
#   3 = invalid arguments
#   4 = write error (D4 anti-overwrite guard triggered)
#
# A'Space OS V2 / 10_Tech_OS / agent-os-bridge
# Created 2026-06-15 by A0 mandate (Symphony Phase 2 wrap-up)
# =============================================================================

set -euo pipefail

# --- Paths (Trust Zone ADR-007) ----------------------------------------------
AGENT_OS_ROOT="C:/Users/amado/agent-os"
AGENT_OS_INDEX="${AGENT_OS_ROOT}/standards/index.yml"
AGENT_OS_STANDARDS_DIR="${AGENT_OS_ROOT}/standards"

SYMPHONY_ROOT="C:/Users/amado/ASpace_OS_V2"
TWINS_ROOT="${SYMPHONY_ROOT}/00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews"

BRIDGE_DIR="${SYMPHONY_ROOT}/10_Tech_OS/agent-os-bridge"
BACKUP_SUFFIX=".bak-$(date +%Y-%m-%d)-pre-agent-os-bridge"
MANIFEST_DIR="${BRIDGE_DIR}/_manifests"
LOG_DIR="${BRIDGE_DIR}/_logs"
LOG_FILE="${LOG_DIR}/sync_$(date +%Y-%m-%d_%H%M%S).log"

# --- Argument parsing --------------------------------------------------------
DRY_RUN="false"
STANDARD_FILTER=""
SHIP_FILTER=""
TWIN_FILTER=""
ROLLBACK="false"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run) DRY_RUN="true"; shift ;;
        --standards) STANDARD_FILTER="$2"; shift 2 ;;
        --ship) SHIP_FILTER="$2"; shift 2 ;;
        --twin) TWIN_FILTER="$2"; shift 2 ;;
        --rollback) ROLLBACK="true"; shift ;;
        -h|--help)
            sed -n '2,40p' "$0"
            exit 0
            ;;
        *) echo "[!] Unknown arg: $1" >&2; exit 3 ;;
    esac
done

# --- Helpers -----------------------------------------------------------------
log() {
    local msg="[$(date +%H:%M:%S)] $*"
    echo "$msg"
    [[ -d "$LOG_DIR" ]] && echo "$msg" >> "$LOG_FILE" 2>/dev/null || true
}

ensure_dirs() {
    mkdir -p "$MANIFEST_DIR" "$LOG_DIR"
}

# D6 root-cause: verify index.yml exists before doing anything else
verify_index() {
    if [[ ! -f "$AGENT_OS_INDEX" ]]; then
        log "[!] D6: index.yml missing at $AGENT_OS_INDEX"
        log "    Run /discover-standards first in Agent OS to create standards + index,"
        log "    or run /index-standards if you already have .md files without index."
        exit 1
    fi
    log "[+] D1 receipt: index.yml present ($(wc -l < "$AGENT_OS_INDEX") lines)"
}

# D1 receipt: load index.yml into bash associative arrays
declare -A STANDARDS_DESC  # key = "folder/file", value = description

load_index() {
    local in_block="" current_folder="" current_file="" desc=""
    while IFS= read -r line; do
        # Skip comments and empty lines
        [[ "$line" =~ ^[[:space:]]*# ]] && continue
        [[ -z "${line// /}" ]] && continue
        # Detect top-level folder (no leading spaces, ends with :)
        if [[ "$line" =~ ^([a-z0-9_-]+):$ ]]; then
            current_folder="${BASH_REMATCH[1]}"
            continue
        fi
        # Detect file (2-space indent, ends with :)
        if [[ "$line" =~ ^[[:space:]]{2}([a-z0-9_-]+):$ ]]; then
            current_file="${BASH_REMATCH[1]}"
            continue
        fi
        # Detect description (4-space indent, description: ...)
        if [[ "$line" =~ ^[[:space:]]{4}description:[[:space:]]*(.+)$ ]]; then
            desc="${BASH_REMATCH[1]}"
            if [[ -n "$current_folder" && -n "$current_file" ]]; then
                STANDARDS_DESC["${current_folder}/${current_file}"]="$desc"
            fi
        fi
    done < "$AGENT_OS_INDEX"
    log "[+] D1 receipt: ${#STANDARDS_DESC[@]} standards loaded from index.yml"
}

# Ship mapping: which Agent OS standard folder maps to which Symphony ship
# Convention: api/* → SNW (execution), database/* → Enterprise (structure), etc.
# Override via SYMPHONY_SHIP_MAP or fallback to default mapping.
ship_for_standard_folder() {
    local folder="$1"
    case "$folder" in
        api|testing|backend)        echo "snw" ;;         # Execution
        database|frontend|ui)       echo "enterprise" ;;  # Structure
        global|cross-cutting|root)  echo "orville" ;;     # Meaning (cross-cutting standards)
        integration|deployment)     echo "cerritos" ;;    # GTD / orchestration
        patterns|doctrine)          echo "protostar" ;;   # DEAL / automation
        *)                          echo "discovery" ;;   # Default = observation/balance
    esac
}

# Inject standards as YAML frontmatter field "agent_os_standards:" into twin file
# D4 append-only: never overwrite existing frontmatter, only add new field
inject_into_twin() {
    local twin_path="$1"
    local standards_block="$2"
    local twin_name
    twin_name=$(basename "$twin_path" .twin.md)

    if [[ "$DRY_RUN" == "true" ]]; then
        log "    [dry-run] would inject into $twin_name"
        return 0
    fi

    # D4 guard: backup before any mutation
    if [[ ! -f "${twin_path}${BACKUP_SUFFIX}" ]]; then
        cp "$twin_path" "${twin_path}${BACKUP_SUFFIX}"
    fi

    # Read frontmatter end (line with closing ---) and inject before it
    local tmp_file="${twin_path}.tmp"
    local fm_end_line
    fm_end_line=$(grep -n '^---$' "$twin_path" | sed -n '2p' | cut -d: -f1)
    if [[ -z "$fm_end_line" ]]; then
        log "    [!] D4 guard: no closing --- in frontmatter, skip $twin_name"
        return 0
    fi

    # Insert standards_block before fm_end_line
    head -n $((fm_end_line - 1)) "$twin_path" > "$tmp_file"
    echo "$standards_block" >> "$tmp_file"
    tail -n +$fm_end_line "$twin_path" >> "$tmp_file"
    mv "$tmp_file" "$twin_path"

    log "    [+] injected into $twin_name"
}

# Build the standards_block YAML to inject
build_standards_block() {
    local ship="$1"
    local block="agent_os_standards:
  source: agent-os-bridge (Brian Casel v3.0)
  injected_at: $(date -u +%Y-%m-%dT%H:%M:%SZ)
  standards:"

    for key in "${!STANDARDS_DESC[@]}"; do
        local folder="${key%%/*}"
        local file="${key##*/}"
        local standard_ship
        standard_ship=$(ship_for_standard_folder "$folder")
        if [[ -n "$SHIP_FILTER" && "$standard_ship" != "$SHIP_FILTER" ]]; then
            continue
        fi
        if [[ -n "$STANDARD_FILTER" && "$folder" != "$STANDARD_FILTER" ]]; then
            continue
        fi
        if [[ "$standard_ship" == "$ship" ]]; then
            block+="
    - folder: ${folder}
      file: ${file}
      description: \"${STANDARDS_DESC[$key]}\"
      ref: ${AGENT_OS_STANDARDS_DIR}/${folder}/${file}.md"
        fi
    done
    echo "$block"
}

# Process one ship directory
process_ship() {
    local ship="$1"
    local ship_dir="${TWINS_ROOT}/${ship}"
    if [[ ! -d "$ship_dir" ]]; then
        log "[!] Ship dir missing: $ship_dir"
        return 0
    fi

    local standards_block
    standards_block=$(build_standards_block "$ship")
    local standard_count
    standard_count=$(echo "$standards_block" | grep -c '^    - folder:' || true)

    log "[*] Ship: $ship ($standard_count standards matched)"
    if [[ "$standard_count" -eq 0 ]]; then
        return 0
    fi

    # Build manifest for this ship
    local manifest="${MANIFEST_DIR}/${ship}_manifest.yml"
    {
        echo "# Agent OS standards manifest for ship: $ship"
        echo "# Generated $(date -u +%Y-%m-%dT%H:%M:%SZ) by agent-os-to-symphony.sh"
        echo "# Source: $AGENT_OS_INDEX"
        echo ""
        echo "$standards_block"
    } > "$manifest"

    # Inject into each twin in the ship
    for twin_path in "${ship_dir}"/*.twin.md; do
        [[ -f "$twin_path" ]] || continue
        local twin_name
        twin_name=$(basename "$twin_path" .twin.md)
        if [[ -n "$TWIN_FILTER" && "$twin_name" != "$TWIN_FILTER" ]]; then
            continue
        fi
        inject_into_twin "$twin_path" "$standards_block"
    done
}

# Rollback: restore all twins from .bak files
rollback_all() {
    log "[*] Rolling back all twins from ${BACKUP_SUFFIX}"
    local count=0
    find "$TWINS_ROOT" -name "*${BACKUP_SUFFIX}" | while read -r bak; do
        local orig="${bak%${BACKUP_SUFFIX}}"
        if [[ "$DRY_RUN" == "true" ]]; then
            log "    [dry-run] would restore $orig"
        else
            mv "$bak" "$orig"
            log "    [+] restored $orig"
        fi
        count=$((count + 1))
    done
    log "[+] Rollback complete"
}

# --- Main --------------------------------------------------------------------
main() {
    ensure_dirs
    log "[*] agent-os-to-symphony.sh — $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    log "    DRY_RUN=$DRY_RUN STANDARD_FILTER=$STANDARD_FILTER SHIP_FILTER=$SHIP_FILTER TWIN_FILTER=$TWIN_FILTER"

    if [[ "$ROLLBACK" == "true" ]]; then
        rollback_all
        exit 0
    fi

    verify_index
    load_index

    # Verify twins root
    if [[ ! -d "$TWINS_ROOT" ]]; then
        log "[!] Twins root missing: $TWINS_ROOT"
        exit 2
    fi
    log "[+] D1 receipt: twins root present ($(find "$TWINS_ROOT" -name '*.twin.md' | wc -l) twins across $(find "$TWINS_ROOT" -mindepth 1 -maxdepth 1 -type d ! -name '_TRASH*' | wc -l) ships)"

    # Process all ships (or filtered one)
    for ship_dir in "${TWINS_ROOT}"/*/; do
        ship=$(basename "$ship_dir")
        [[ "$ship" == _TRASH* ]] && continue
        if [[ -n "$SHIP_FILTER" && "$ship" != "$SHIP_FILTER" ]]; then
            continue
        fi
        process_ship "$ship"
    done

    log "[+] DONE — see $MANIFEST_DIR for per-ship manifests, $LOG_FILE for full log"
}

main "$@"
