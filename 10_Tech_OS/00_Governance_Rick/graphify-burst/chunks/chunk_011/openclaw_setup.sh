#!/bin/bash
# 04_OpenClaw_Setup (The Brain)
# Mission: Install and configure OpenClaw global service.

echo "--- OPENCLAW SETUP STARTED ---"
date

# 1. Install PNPM if missing (preferred by OpenClaw)
if ! command -v pnpm &> /dev/null; then
    echo "📦 Installing PNPM..."
    npm install -g pnpm
fi

# 2. Install OpenClaw Global
echo "🔭 Installing OpenClaw..."
npm install -g @google/openclaw

# 3. Create Configuration directory if it doesn't exist
mkdir -p ~/.config/openclaw

# 4. Link or Copy the config from the repo (optional, but good for persistence)
# CP_CONFIG_CMD="cp /root/aspace_a0_amadeus/00_Amadeus/03_OpenClaw_Body/openclaw.json ~/.config/openclaw/openclaw.json"
# echo "⚙️ Copying configuration..."
# $CP_CONFIG_CMD

echo "--- OPENCLAW SETUP COMPLETE ---"
echo "Next step: Run 'openclaw auth' if needed, or 'openclaw gateway' to start."
