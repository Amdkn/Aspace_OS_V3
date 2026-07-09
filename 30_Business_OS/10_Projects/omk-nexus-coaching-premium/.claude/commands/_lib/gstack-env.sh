# gstack-env.sh — wrapper SOBRE pour exécuter gstack sans toucher .claude/
# Sister : plan-lightning-l0l1l2 §4 L1-2 (clauses c1/c2/c3 enforced)
# Date : 2026-07-05
#
# Usage : source ce fichier AVANT d'invoquer /gstack-autoplan, /gstack-cso, /gstack-ship
#
# Ce qu'il fait :
#   - Expose les binaries gstack depuis agent-os/home-court/gstack/bin/ (home court, ADR-INFRA-002)
#   - Neutralise l'auto-update réseau (c3) : GSTACK_NO_UPDATE=1 + un faux gstack-update-check no-op
#   - /browse reste OPTION (c2) — on garde notre harness mcp__claude-in-chrome__* comme défaut
#   - ZÉRO écriture dans ~/.claude/ (c1 sacred P4)

export GSTACK_HOME="$HOME/agent-os/home-court/gstack"
export GSTACK_BIN="$GSTACK_HOME/bin"
export PATH="$GSTACK_BIN:$PATH"

# c3 — auto-update OFF : neutralise le check réseau
export GSTACK_NO_UPDATE=1
# Crée un wrapper no-op "gstack-update-check" prioritaire sur le PATH
mkdir -p "$GSTACK_HOME/bin-shim"
cat > "$GSTACK_HOME/bin-shim/gstack-update-check" <<'EOF'
#!/usr/bin/env bash
# c3 enforced — auto-update disabled per ADR-WARMODE-002 + plan §4 clause c3
echo ""
EOF
chmod +x "$GSTACK_HOME/bin-shim/gstack-update-check"
export PATH="$GSTACK_HOME/bin-shim:$PATH"

# c2 — /browse reste OPTION (notre harness chrome MCP par défaut)
# Pour utiliser gstack browse quand même : GSTACK_USE_BROWSE=1 source gstack-env.sh

echo "[gstack-env] GSTACK_HOME=$GSTACK_HOME"
echo "[gstack-env] PATH ajusté : $GSTACK_HOME/bin + $GSTACK_HOME/bin-shim"
echo "[gstack-env] c3 auto-update OFF | c2 /browse OPTION (chrome MCP par défaut)"