#!/usr/bin/env bash
# ============================================================
# A'Space OS V3 — install.sh (clone-friendly bootstrap)
# NO SECRETS. Scaffolds a placeholder settings + validates structure.
# ============================================================
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "==> A'Space OS V3 install (root: $ROOT)"

# --- 1. Toolchain checks ------------------------------------
fail=0
check_ver() { # name  cmd  min_major
  local name="$1" cmd="$2" min="$3" ver major
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "  [MISSING] $name ($cmd) not found"; fail=1; return
  fi
  ver="$("$cmd" --version 2>&1 | grep -oE '[0-9]+\.[0-9]+(\.[0-9]+)?' | head -1)"
  major="${ver%%.*}"
  if [ "${major:-0}" -lt "$min" ]; then
    echo "  [TOO OLD] $name $ver (need >= $min)"; fail=1
  else
    echo "  [OK] $name $ver"
  fi
}
echo "==> Checking toolchain"
check_ver "Node.js" node 22
check_ver "Python"  python3 3   # major 3; minor >=10 checked below
if command -v python3 >/dev/null 2>&1; then
  pyminor="$(python3 -c 'import sys;print(sys.version_info.minor)' 2>/dev/null || echo 0)"
  [ "${pyminor:-0}" -lt 10 ] && { echo "  [TOO OLD] Python 3.$pyminor (need >= 3.10)"; fail=1; }
fi
[ "$fail" -eq 0 ] || { echo "==> Toolchain check FAILED. Install the missing/updated tools and re-run."; exit 1; }

# --- 2. Scaffold placeholder settings (NO real tokens) ------
CFG="50_Claude_Code_Config"
EXAMPLE="$CFG/settings.example.json"
if [ ! -f "$EXAMPLE" ]; then
  echo "==> Writing placeholder $EXAMPLE"
  mkdir -p "$CFG"
  cat > "$EXAMPLE" <<'JSON'
{
  "_comment": "PLACEHOLDER ONLY — copy to ~/.claude/settings.json and set YOUR OWN tokens. Never commit real values.",
  "env": {
    "SUPABASE_URL": "https://YOUR-PROJECT.supabase.co",
    "SUPABASE_ANON_KEY": "SET_YOUR_OWN",
    "AIRTABLE_BEARER_AUTH": "SET_YOUR_OWN",
    "GH_TOKEN": "SET_YOUR_OWN",
    "VERCEL_TOKEN": "SET_YOUR_OWN",
    "HOSTINGER_API_TOKEN": "SET_YOUR_OWN"
  },
  "hooks": {}
}
JSON
else
  echo "==> $EXAMPLE already present (leaving as-is)"
fi

# --- 3. Wire config into ~/.claude (skills/rules/agents/hooks)
echo "==> To wire Claude Code config, run:"
echo "     mkdir -p ~/.claude"
for d in skills rules agents hooks; do
  echo "     cp -r $CFG/$d ~/.claude/$d"
done
echo "     cp $EXAMPLE ~/.claude/settings.json   # then edit with YOUR tokens"

# --- 4. Validate structure ----------------------------------
echo "==> Validating structure"
bash scripts/verify_structure.sh

echo "==> Done. Read V3-INIT.md for the full VPS bootstrap (Citadel WF0 + MCPs)."
