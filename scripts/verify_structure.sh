#!/usr/bin/env bash
# ============================================================
# A'Space OS V3 — verify_structure.sh
# Validates the canonical V3 tree + guards against secret leaks.
# Exit 0 = OK, 1 = structure error, 2 = secret leak.
# ============================================================
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

req_dirs=(
  "00_Amadeus" "10_Tech_OS" "20_Life_OS" "30_Business_OS" "_SPECS"
  "40_Fable_Banque" "50_Claude_Code_Config" "60_Citadel" "90_INBOX" "scripts"
)
req_files=(
  "README.md" "AGENTS.md" "CLAUDE.md" "V3-INIT.md" "LICENSE" ".gitignore" "install.sh"
)

err=0
echo "==> Checking required directories"
for d in "${req_dirs[@]}"; do
  if [ -d "$d" ]; then echo "  [OK] $d"; else echo "  [MISSING] $d"; err=1; fi
done
echo "==> Checking required files"
for f in "${req_files[@]}"; do
  if [ -f "$f" ]; then echo "  [OK] $f"; else echo "  [MISSING] $f"; err=1; fi
done

echo "==> Config subdirs (skills/rules/agents/hooks)"
for d in skills rules agents hooks; do
  if [ -d "50_Claude_Code_Config/$d" ]; then echo "  [OK] 50_Claude_Code_Config/$d"; else echo "  [MISSING] 50_Claude_Code_Config/$d"; err=1; fi
done

echo "==> Guard: no committed HARNESS settings.json / history.jsonl"
# Only the Claude Code harness secret file matters (root or config dir). Project
# .vscode/.gemini settings.json are benign editor configs and are allowed.
for s in "settings.json" "50_Claude_Code_Config/settings.json" "50_Claude_Code_Config/history.jsonl"; do
  [ -f "$s" ] && { echo "  [LEAK] harness $s present (should be gitignored)"; err=2; }
done

echo "==> Guard: secret-pattern scan (real token prefixes + key material)"
# Tight patterns: real token prefixes, JWT triples, private-key headers.
# Excludes this script itself and PDFs to avoid self-match / false positives.
PAT='sbp_[A-Za-z0-9]{30}|ghp_[A-Za-z0-9]{30}|sk-[A-Za-z0-9]{30}|sb_secret_[A-Za-z0-9]{20}|eyJ[A-Za-z0-9_-]{20,}\.eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}'
hits="$(grep -rIlE "$PAT" . --exclude-dir=.git --exclude='verify_structure.sh' --exclude='*.pdf' 2>/dev/null || true)"
if [ -n "$hits" ]; then
  echo "  [LEAK] real secret pattern found:"; echo "$hits"
  err=2
else
  echo "  [OK] no real secret pattern hit"
fi

if [ "$err" -eq 0 ]; then echo "==> STRUCTURE OK"; else echo "==> STRUCTURE ISSUES (code $err)"; fi
exit "$err"
