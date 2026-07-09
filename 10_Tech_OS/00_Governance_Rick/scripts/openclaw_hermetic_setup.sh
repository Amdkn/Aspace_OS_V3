#!/bin/bash
# 🧪 OPENCLAW HERMETIC SETUP (The Isolated Cortex)
# Author: Rick Supreme (via Antigravity)
# Target: A0 Amadeus - Isolated Operation

echo "--- 🧪 STARTING HERMETIC INSTALLATION ---"
date

TARGET_DIR="/root/aspace_a0_amadeus/00_Amadeus/03_OpenClaw_Body"
REPO_URL="https://github.com/openclaw/openclaw.git"

# 1. PREPARE DIRECTORY
echo "📂 Preparing isolated cage..."
mkdir -p "$TARGET_DIR"
cd "$TARGET_DIR" || exit

# 2. CLONE OR UPDATE SOURCE
if [ ! -d ".git" ]; then
    echo "🔭 Cloning OpenClaw source..."
    git clone "$REPO_URL" .
else
    echo "🔄 Updating OpenClaw source..."
    git pull origin main
fi

# 3. BUILD LOCALLY (Hermetic Isolation)
echo "📦 Installing internal dependencies (pnpm)..."
pnpm install

echo "🏗️  Building Sovereign Cortex..."
pnpm build

# 4. LINK COMMAND (Optional entry point)
echo "🔗 Linking local command..."
# Create a local shim if needed, or just use the local dist entry point.
# For now, we rely on running it from the directory or using pnpm exec.

echo "--- 🧪 HERMETIC CONSTRUCTION COMPLETE ---"
echo "Status: OpenClaw source is built and isolated in $TARGET_DIR."
echo "Next step: Run 'pnpm openclaw onboard' to initialize identity."
