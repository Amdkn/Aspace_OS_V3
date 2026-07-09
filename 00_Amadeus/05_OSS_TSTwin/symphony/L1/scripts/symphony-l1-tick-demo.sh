#!/usr/bin/env bash
# ----------------------------------------------------------------------------
# symphony-l1-tick-demo.sh
# Simulates a L1 Life OS morning brief tick (8 phases, 18-field pulse.log).
# Mirrors the L2 demo but scoped to Life OS agents A1/A2/A3 + 4 trackers.
# Bash version (Git Bash compatible on Windows).
# ----------------------------------------------------------------------------

set -euo pipefail

# Resolve paths (Git Bash on Windows produces /c/Users/...; cygpath -w for tools that need Windows paths)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
L1_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PULSE_LOG="$L1_ROOT/agent-os/pulse.log"

# Mock MiniMax 2.7 rates (USD per 1k tokens, input/output blended)
RATE_IN=0.0002
RATE_OUT=0.0012

# Tick metadata
TICK_ID="L1_morning-$(date -u +%Y%m%dT%H%M%S)"
WORKFLOW_ID="L1_morning_brief"
TS0="$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ)"
CUMULATIVE_COST=0.0
SLA_MAX_COST=0.05

# 8 phases of the L1 morning brief
phases=("WAKE" "PROBE" "DECIDE" "EXECUTE" "OBSERVE" "LEARN" "SIGNAL" "SLEEP")
declare -A STANDARDS
STANDARDS[WAKE]='01_agent-hierarchy-contract.md|02_beth-5-states-machine.md'
STANDARDS[PROBE]='08_affine-kanban-gtd.md|04_crew-bridge-protocol.md'
STANDARDS[DECIDE]='03_vessel-captain-protocol.md|10_handoff-json-outbox-l1.md'
STANDARDS[EXECUTE]='04_crew-bridge-protocol.md|08_affine-kanban-gtd.md|11_canon-vs-runtime-drift.md'
STANDARDS[OBSERVE]='02_beth-5-states-machine.md|09_stop-authority-protocol.md'
STANDARDS[LEARN]='06_obsidian-vault-linkage.md|11_canon-vs-runtime-drift.md'
STANDARDS[SIGNAL]='01_agent-hierarchy-contract.md|02_beth-5-states-machine.md'
STANDARDS[SLEEP]='01_agent-hierarchy-contract.md'

declare -A DECISIONS
DECISIONS[WAKE]='beth_state=GREEN'
DECISIONS[PROBE]='2min_rule:3_cards_processed'
DECISIONS[DECIDE]='route:Cerritos->Tendi;Discovery->Tilly'
DECISIONS[EXECUTE]='affine_cards_moved:5,drift_audit:OK'
DECISIONS[OBSERVE]='reflect:ORANGE_warn(cerritos_load=high)'
DECISIONS[LEARN]='lesson:cerritos_load_pattern'
DECISIONS[SIGNAL]='report_to_beth:state=ORANGE'
DECISIONS[SLEEP]='close:tick_complete,a0_pending'

declare -A VESSELS
VESSELS[WAKE]='null'
VESSELS[PROBE]='Cerritos'
VESSELS[DECIDE]='Cerritos'
VESSELS[EXECUTE]='Cerritos'
VESSELS[OBSERVE]='Discovery'
VESSELS[LEARN]='Enterprise'
VESSELS[SIGNAL]='null'
VESSELS[SLEEP]='null'

declare -A CREWS
CREWS[WAKE]='Beth'
CREWS[PROBE]='Boimler'
CREWS[DECIDE]='Mercer'
CREWS[EXECUTE]='Tendi'
CREWS[OBSERVE]='Tilly'
CREWS[LEARN]='Archer'
CREWS[SIGNAL]='Beth'
CREWS[SLEEP]='Amadeus'

declare -A LDS
LDS[WAKE]='null'
LDS[PROBE]='null'
LDS[DECIDE]='null'
LDS[EXECUTE]='null'
LDS[OBSERVE]='LD04'
LDS[LEARN]='null'
LDS[SIGNAL]='null'
LDS[SLEEP]='null'

declare -A STATES
STATES[WAKE]='GREEN'
STATES[PROBE]='GREEN'
STATES[DECIDE]='GREEN'
STATES[EXECUTE]='GREEN'
STATES[OBSERVE]='ORANGE'
STATES[LEARN]='ORANGE'
STATES[SIGNAL]='ORANGE'
STATES[SLEEP]='ORANGE'

# Init pulse.log (append-only; header note already in schema-pulse-log-l1.md)
mkdir -p "$(dirname "$PULSE_LOG")"
touch "$PULSE_LOG"

echo "=== L1 Morning Brief Tick ==="
echo "tick_id: $TICK_ID"
echo "workflow_id: $WORKFLOW_ID"
echo "pulse.log: $PULSE_LOG"
echo ""

# Loop through 8 phases
for PHASE in "${phases[@]}"; do
  TS_PHASE="$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ)"
  DUR_MS=$((RANDOM % 1000 + 200))
  COST_DELTA=$(awk -v r="$RATE_IN" -v d="$DUR_MS" 'BEGIN{printf "%.6f", (r * d / 1000)}')
  CUMULATIVE_COST=$(awk -v a="$CUMULATIVE_COST" -v b="$COST_DELTA" 'BEGIN{printf "%.6f", a + b}')

  STD_JSON="[\"$(echo "${STANDARDS[$PHASE]}" | sed 's/|/","/g')\"]"
  VESSEL="${VESSELS[$PHASE]}"
  CREW="${CREWS[$PHASE]}"
  LD="${LDS[$PHASE]}"
  STATE="${STATES[$PHASE]}"
  DECISION="${DECISIONS[$PHASE]}"

  LINE=$(cat <<EOF
{"ts":"$TS_PHASE","tick_id":"$TICK_ID","workflow_id":"$WORKFLOW_ID","issue_id":null,"phase":"$PHASE","duration_ms":$DUR_MS,"standards_injected":$STD_JSON,"decision":"$DECISION","evidence_url":null,"cost_delta_usd":$COST_DELTA,"cumulative_cost_usd":$CUMULATIVE_COST,"aspace_layer":"L1","soc_target_domain":null,"error":null,"vessel_id":$([ "$VESSEL" = "null" ] && echo "null" || echo "\"$VESSEL\""),"crew_id":"$CREW","ld_id":$([ "$LD" = "null" ] && echo "null" || echo "\"$LD\""),"agent_state":"$STATE"}
EOF
)

  echo "$LINE" >> "$PULSE_LOG"
  echo "[$PHASE] ${CREW}/${VESSEL} state=${STATE} cost=\$${CUMULATIVE_COST}"

  # SLA check
  EXCEEDED=$(awk -v c="$CUMULATIVE_COST" -v m="$SLA_MAX_COST" 'BEGIN{print (c > m) ? 1 : 0}')
  if [ "$EXCEEDED" = "1" ]; then
    echo "BUDGET_EXCEEDED: cumulative=\$${CUMULATIVE_COST} > sla=\$${SLA_MAX_COST}" >&2
    exit 2
  fi

  sleep 0.1
done

echo ""
echo "=== Tick Complete ==="
echo "Total cost: \$${CUMULATIVE_COST} USD (mock MiniMax 2.7 rates)"
echo "8/8 phases emitted, gate=PASS"
echo "pulse.log: $(wc -l < "$PULSE_LOG") lines total"
