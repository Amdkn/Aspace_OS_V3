#!/usr/bin/env bash
# =============================================================================
# Symphony Tick Demo — Bash (one-tick simulation, mock Airtable record)
# =============================================================================
# Walks the 8 phases (WAKE→SLEEP) for WORKFLOW.solaris-airtable-clients.
# Injects standards from agent-os/standards/index.yml.
# Writes 8 JSONL lines to agent-os/pulse.log.
#
# Usage:  bash symphony/scripts/symphony-tick-demo.sh
# Env:    SYMPHONY_ROOT (defaults to parent of this script)
# =============================================================================

set -euo pipefail

# --- Resolve paths -----------------------------------------------------------
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SYMPHONY_ROOT="${SYMPHONY_ROOT:-$(dirname "$SCRIPT_DIR")}"
INDEX_FILE="$SYMPHONY_ROOT/agent-os/standards/index.yml"
PULSE_LOG="$SYMPHONY_ROOT/agent-os/pulse.log"
PYTHON="${PYTHON:-C:/Python314/python.exe}"

# cygpath -w converts POSIX paths (Git Bash) to Windows-style for native Windows tools like Python.
# On a real Unix box, cygpath is missing — fall back to the POSIX path.
if command -v cygpath >/dev/null 2>&1; then
    WIN_INDEX_FILE="$(cygpath -w "$INDEX_FILE")"
    WIN_PULSE_LOG="$(cygpath -w "$PULSE_LOG")"
else
    WIN_INDEX_FILE="$INDEX_FILE"
    WIN_PULSE_LOG="$PULSE_LOG"
fi

# --- Helpers -----------------------------------------------------------------
# iso_utc: returns ISO 8601 UTC with milliseconds, e.g. 2026-06-06T18:30:00.123Z
iso_utc() {
    # Git Bash on Windows: %3N works in GNU date
    date -u +"%Y-%m-%dT%H:%M:%S.%3NZ"
}

# ms_since: ms between two iso_utc strings (a, b) where a <= b
ms_since() {
    local a="$1" b="$2"
    PYTHONIOENCODING=utf-8 "$PYTHON" -c "
from datetime import datetime
def p(s): return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S.%fZ')
print(int((p('$b') - p('$a')).total_seconds() * 1000))
"
}

# pulse: append a JSONL line to pulse.log. Args: phase decision extras_json
pulse() {
    local phase="$1" decision="$2" extras="${3:-{\}}"
    local ts
    ts="$(iso_utc)"
    PYTHONIOENCODING=utf-8 "$PYTHON" -c "
import json, sys
ts = sys.argv[1]
phase = sys.argv[2]
decision = sys.argv[3]
extras = json.loads(sys.argv[4])
base = {
    'ts': ts,
    'tick_id': '$TICK_ID',
    'workflow_id': '$WORKFLOW_ID',
    'issue_id': '$ISSUE_ID' if '$PHASE_HAS_ISSUE' == '1' else None,
    'phase': phase,
    'aspace_layer': 'L2',
    'soc_target_domain': '$SOC_DOMAIN' if phase in ('DECIDE','EXECUTE','OBSERVE','LEARN','SIGNAL') else None,
    'cumulative_cost_usd': $CUM_COST if phase in ('EXECUTE','OBSERVE','LEARN','SIGNAL','SLEEP') else None,
    'cost_delta_usd': $DELTA_COST if phase in ('EXECUTE','OBSERVE') else None,
    'standards_injected': $STANDARDS_JSON if phase in ('DECIDE','EXECUTE','OBSERVE') else None,
    'decision': decision,
    'evidence_url': '$EVIDENCE_URL' if phase in ('EXECUTE','OBSERVE','SIGNAL') and '$EVIDENCE_URL' != '' else None,
    'error': None,
}
# drop Nones for cleaner lines
base = {k: v for k, v in base.items() if v is not None}
base.update(extras)
print(json.dumps(base, ensure_ascii=False), file=sys.stderr)
" "$ts" "$phase" "$decision" "$extras" 1>&2
    # Python prints to stderr to keep stdout free; capture and append
    local line
    line="$(PYTHONIOENCODING=utf-8 "$PYTHON" -c "
import json, sys
ts = sys.argv[1]
phase = sys.argv[2]
decision = sys.argv[3]
extras = json.loads(sys.argv[4])
base = {
    'ts': ts,
    'tick_id': '$TICK_ID',
    'workflow_id': '$WORKFLOW_ID',
    'issue_id': '$ISSUE_ID' if '$PHASE_HAS_ISSUE' == '1' else None,
    'phase': phase,
    'aspace_layer': 'L2',
    'soc_target_domain': '$SOC_DOMAIN' if phase in ('DECIDE','EXECUTE','OBSERVE','LEARN','SIGNAL') else None,
    'cumulative_cost_usd': $CUM_COST if phase in ('EXECUTE','OBSERVE','LEARN','SIGNAL','SLEEP') else None,
    'cost_delta_usd': $DELTA_COST if phase in ('EXECUTE','OBSERVE') else None,
    'standards_injected': $STANDARDS_JSON if phase in ('DECIDE','EXECUTE','OBSERVE') else None,
    'decision': decision,
    'evidence_url': '$EVIDENCE_URL' if phase in ('EXECUTE','OBSERVE','SIGNAL') and '$EVIDENCE_URL' != '' else None,
    'error': None,
}
base = {k: v for k, v in base.items() if v is not None}
base.update(extras)
print(json.dumps(base, ensure_ascii=False))
" "$ts" "$phase" "$decision" "$extras")"
    echo "$line" >> "$PULSE_LOG"
}

# --- Init ---------------------------------------------------------------------
WORKFLOW_ID="solaris-airtable-clients"
TICK_ID="${WORKFLOW_ID}-$(date -u +%Y-%m-%dT%H-%M-%S)"
ISSUE_ID="recDEMO001"
SOC_DOMAIN="Growth"
PHASE_HAS_ISSUE="0"
EVIDENCE_URL=""
CUM_COST="0.0"
DELTA_COST="0.0"
STANDARDS_JSON="[]"

# Mock Airtable record (passes the 9-criterion filter)
MOCK_RECORD='{
  "id": "recDEMO001",
  "fields": {
    "Name": "Acme Studio (demo)",
    "Status": "Qualified",
    "SOA Domain": "Growth",
    "Owner B2": "Superman",
    "Executor B3": "Guardians",
    "Description": "AI automation agency, looking for content + growth factory",
    "Build Gate": "PASS = signed MSA + first 3 deliverables accepted",
    "Context Pack URL": "https://notion.so/demo-pack",
    "ClickUp Task URL": "https://app.clickup.com/t/abc",
    "Notion SOP URL": "https://notion.so/sop-growth",
    "Forbidden Words": "synergie, disrupter, innover",
    "SLA Max Time": 15,
    "SLA Max Cost": 0.50,
    "SLA Max Retries": 3,
    "Gate Status": "Qualified"
  }
}'

# Read index.yml, count standards (1 yaml file at root, flat)
STD_COUNT=$(PYTHONIOENCODING=utf-8 "$PYTHON" -c "
import yaml
data = yaml.safe_load(open(r'''$WIN_INDEX_FILE''', encoding='utf-8'))
total = sum(len(v) for v in data.values())
print(total)
")

echo "=== Symphony Tick Demo ==="
echo "Tick ID:     $TICK_ID"
echo "Workflow:    $WORKFLOW_ID"
echo "Issue:       $ISSUE_ID ($SOC_DOMAIN)"
echo "Standards:   $STD_COUNT available in index.yml"
echo "Pulse log:   $PULSE_LOG"
echo ""

# Truncate pulse.log for the demo (don't accumulate stale lines)
> "$PULSE_LOG"

# --- Phase 1: WAKE -----------------------------------------------------------
T0="$(iso_utc)"
PHASE_HAS_ISSUE="0"
pulse "WAKE" "tick start, index loaded, $STD_COUNT standards available" \
    "{\"duration_ms\": 12}"
sleep 0.05
T1="$(iso_utc)"

# --- Phase 2: PROBE ----------------------------------------------------------
# Simulate polling 42 records, applying 9-criterion filter
# Result: 3 eligible, 39 not_eligible
PHASE_HAS_ISSUE="0"
DECISION="polled 42 records, 3 eligible, 39 not_eligible (Status/Build Gate/SLA fail)"
P_DECISION="polled 42 records, 3 eligible (incl. $ISSUE_ID), 39 not_eligible"
pulse "PROBE" "$P_DECISION" \
    "{\"duration_ms\": 1234}"
sleep 0.05
T2="$(iso_utc)"

# --- Phase 3: DECIDE ---------------------------------------------------------
# Select 7 standards for this tick
PHASE_HAS_ISSUE="1"
STANDARDS_JSON='["mission-contract.md","soa-routing.md","gate-decisions.md","forbidden-words.md","sla-triple.md","expected-proof.md","writeback-policy.md"]'
pulse "DECIDE" "build mission_contract v1.0, inject 7 standards, route to orchestrator+researcher+strategist" \
    "{\"duration_ms\": 87}"
sleep 0.05
T3="$(iso_utc)"

# --- Phase 4: EXECUTE --------------------------------------------------------
# Simulate agent call. Use mock cost (MiniMax 2.7 rates)
PHASE_HAS_ISSUE="1"
EVIDENCE_URL="https://airtable.com/$(echo $ISSUE_ID | tr '[:upper:]' '[:lower:]')"
DELTA_COST="0.012"
CUM_COST="0.012"
pulse "EXECUTE" "proof built (4/4 types: summary + recommendation + risks+blockers + gate=PASS)" \
    "{\"duration_ms\": 4521}"
sleep 0.05
T4="$(iso_utc)"

# --- Phase 5: OBSERVE --------------------------------------------------------
# Lexique scan + gate validation
PHASE_HAS_ISSUE="1"
DELTA_COST="0.003"
CUM_COST="0.015"
pulse "OBSERVE" "lexique clean (no forbidden match), gate=PASS, cumulative=0.015 USD" \
    "{\"duration_ms\": 203}"
sleep 0.05
T5="$(iso_utc)"

# --- Phase 6: LEARN ----------------------------------------------------------
PHASE_HAS_ISSUE="1"
pulse "LEARN" "metrics updated, retries=1/3, no Donna escalation, signal_blocker=false" \
    "{\"duration_ms\": 15}"
sleep 0.05
T6="$(iso_utc)"

# --- Phase 7: SIGNAL ---------------------------------------------------------
# Write drafts (1 airtable_update_draft, 1 proof_summary)
PHASE_HAS_ISSUE="1"
EVIDENCE_URL="https://airtable.com/$(echo $ISSUE_ID | tr '[:upper:]' '[:lower:]')"
pulse "SIGNAL" "drafts written: 1x airtable_update_draft (Gate Status=PASS), 1x proof_summary" \
    "{\"duration_ms\": 78}"
sleep 0.05
T7="$(iso_utc)"

# --- Phase 8: SLEEP ----------------------------------------------------------
PHASE_HAS_ISSUE="0"
TOTAL_MS=$(ms_since "$T0" "$T7")
pulse "SLEEP" "tick complete, total_duration_ms=$TOTAL_MS, final_cost=0.015 USD" \
    "{\"duration_ms\": 3}"

# --- Summary -----------------------------------------------------------------
echo ""
echo "=== Tick summary ==="
echo "Lines written:   $(wc -l < "$PULSE_LOG") (expected 8)"
echo "Phases:          WAKE PROBE DECIDE EXECUTE OBSERVE LEARN SIGNAL SLEEP"
echo "Standards used:  7 (mission-contract, soa-routing, gate-decisions, forbidden-words, sla-triple, expected-proof, writeback-policy)"
echo "Total cost:      0.015 USD (mock MiniMax 2.7 rates)"
echo "Total duration:  ${TOTAL_MS}ms"
echo "Final gate:      PASS"
echo ""
echo "=== pulse.log ==="
cat "$PULSE_LOG"
