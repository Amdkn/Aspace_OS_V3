#!/bin/bash
# cloud-bootstrap/scripts/bootstrap.sh
# Phase H (2026-06-20) — automated bootstrap of canonical OMK schema.
# Uses the same SQL files as the canon, applied via mcp__supabase-omk__apply_migration.
#
# Usage: invoked by the cloud-bootstrap skill (Claude agent).
# This script is a REFERENCE for the agent — the agent uses mcp__supabase tools
# directly because the script can't access MCP without the agent runtime.

set -euo pipefail

PROJECT_ID="${1:-ndvqwcapwcnpdvknxcjw}"  # OMK SERVICES CUSTOMERS default
SQL_DIR="C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/omk/apps/dashboard/sql"

echo "Bootstrapping OMK canonical schema on project $PROJECT_ID"
echo "SQL files from: $SQL_DIR"
echo ""
echo "⚠️  This script is a REFERENCE for the cloud-bootstrap skill."
echo "    The skill invokes mcp__supabase-omk__apply_migration directly."
echo ""

# Order matters: schema → RLS → roles → hook → seed
# (See SKILL.md for the rationale.)
declare -a MIGRATIONS=(
  "omk_saas_schema_canon:02_omk_saas_schema.sql"
  "omk_saas_rls_policies:03_rls_policies.sql"
  "omk_saas_pg_roles_provisioning:06_provision_pg_roles_omk.sql"
  "omk_saas_jwt_custom_access_token_hook:04_jwt_hook.sql"
  "omk_saas_seed_dev_acme_demo:05_seed_dev.sql"
  "omk_saas_add_legal_docs_sales_leads:phase_d_addendum.sql"
)

for migration in "${MIGRATIONS[@]}"; do
  name="${migration%%:*}"
  file="${migration##*:}"
  path="$SQL_DIR/$file"

  if [ ! -f "$path" ]; then
    echo "  ⚠️  Skipping $name — file not found: $path"
    continue
  fi

  echo "  → Applying $name ($file)"
  # The agent reads this file and passes the content to mcp__supabase-omk__apply_migration
  # via the query parameter. Direct invocation requires the MCP runtime.
  echo "     file size: $(wc -c < "$path") bytes"
done

echo ""
echo "✅ All 6 migrations prepared. The cloud-bootstrap skill will apply them via MCP."
echo ""
echo "⚠️  A0 manual steps required after this script runs:"
echo "    1. Wire JWT custom_access_token_hook in Auth dashboard (D6 #64)"
echo "    2. Add 'omk_saas' to PGRST_DB_SCHEMAS in Settings → API (D6 #68)"