#!/bin/bash
# deploy_sovereign.sh
# ------------------------------------------------------------------
# PURPOSE: Bootstrap the A'Space Kernel v2.0 on the VPS.
# AUTHOR: Rick Sovereign (via Amadeus)
# ------------------------------------------------------------------

echo "--- 🚀 INITIATING SOVEREIGN DEPLOYMENT ---"

# 1. Define Paths
REPO_ROOT="/root/aspace_a0_amadeus"
TECH_OS="$REPO_ROOT/10_Tech_OS"
GOVERNANCE="$TECH_OS/00_Governance_Rick"
SCRIPTS="$GOVERNANCE/scripts"

# 2. Set Permissions (The Fam)
echo "🛡️  Granting Clearance to The Fam..."
chmod +x "$SCRIPTS/yaz_protocol.sh"
chmod +x "$SCRIPTS/ryan_protocol.sh"
chmod +x "$SCRIPTS/graham_protocol.sh"

# 3. Symlink Critical Utilities
echo "🔗 Linking Protocols to System..."
# Example: Allow running 'sovereign-update' to trigger Ryan
ln -sf "$SCRIPTS/ryan_protocol.sh" /usr/local/bin/sovereign-maintenance
ln -sf "$SCRIPTS/yaz_protocol.sh" /usr/local/bin/sovereign-secops
ln -sf "$SCRIPTS/graham_protocol.sh" /usr/local/bin/sovereign-backup

# 4. Create Directories for Data Layer (12th Doctor)
echo "🏗️  Ensuring Data Sanctums Exist..."
mkdir -p "$TECH_OS/13_Data_12th_Doctor/01_Clara_MCP/sandbox"
mkdir -p "$TECH_OS/13_Data_12th_Doctor/03_Missy_Chaos/vault"

# 5. Check Dependencies
echo "🔍 Checking Dependencies..."
if ! command -v rclone &> /dev/null; then
    echo "❌ Rclone missing. Graham will be sad."
fi
if ! command -v docker &> /dev/null; then
    echo "❌ Docker missing. The TARDIS has no engine."
fi

echo "--- ✅ SOVEREIGN DEPLOYMENT COMPLETE ---"
echo "Run 'sovereign-maintenance' to verify system health."
