#!/usr/bin/env bash
# run-autoplan.sh — wrapper sobre pour /gstack-autoplan sur un signal du projet
# Sister : plan-lightning-l0l1l2 §4 L1-5 + gstack-mapping.md
# Date : 2026-07-05
#
# Usage :
#   ./run-autoplan.sh <chemin/vers/signal.md>
#
# Prérequis : avoir sourcé gstack-env.sh (PATH ajusté + c3 auto-update OFF)
#
# Output : .plans/<basename-signal>.plan.yaml (append-only)
#
# Doctrine :
#   - Ne jamais exécuter /gstack-ship (outboard A+) sans GO
#   - Ne jamais écrire dans ~/.claude/CLAUDE.md (c1)
#   - Auto-update OFF (c3)
#   - /browse OPTION (c2) — chrome MCP par défaut

set -euo pipefail

SIGNAL="${1:?Usage: $0 <chemin/vers/signal.md>}"

# Source le wrapper gstack-env si pas déjà fait
if [ -z "${GSTACK_HOME:-}" ]; then
  source "$(dirname "$0")/gstack-env.sh"
fi

# D1 verify signal existe
[ -f "$SIGNAL" ] || { echo "D6 ERROR: signal introuvable: $SIGNAL" >&2; exit 2; }

SIGNAL_BASE=$(basename "$SIGNAL" .md)
SIGNAL_DIR=$(dirname "$SIGNAL")
PLAN_OUT="${SIGNAL_DIR}/.plans/${SIGNAL_BASE}.plan.yaml"

mkdir -p "$(dirname "$PLAN_OUT")"

echo "[run-autoplan] signal=$SIGNAL"
echo "[run-autoplan] HOME=$GSTACK_HOME"
echo "[run-autoplan] PATH=$PATH"
echo "[run-autoplan] output=$PLAN_OUT"
echo ""
echo "[run-autoplan] === APPEL /gstack-autoplan ==="
echo ""
echo "(Invocation manuelle requise par A+ via le slash command /gstack-autoplan,"
echo " branchement sur le signal ci-dessus. Ce wrapper prépare l'environnement,"
echo " ne déclenche PAS l'invoke automatiquement — l'HITL sur /gstack-ship reste sacré.)"
echo ""
echo "Pour lancer le pipeline manuellement :"
echo "  /gstack-autoplan"
echo "  → lis le signal: $SIGNAL"
echo "  → run CEO review → design review → eng review → DX review"
echo "  → output: $PLAN_OUT (canon D4 append-only)"
echo ""
echo "D1 receipt attendu : plan.yaml créé avec frontmatter OKF + sections"
echo "(Preflight = Decisions, Criteria, Design, Engineering, DX, Decision-principles)"