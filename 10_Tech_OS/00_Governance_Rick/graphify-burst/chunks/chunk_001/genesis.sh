#!/bin/bash
# 🧪 MASTER GENESIS PROTOCOL (A0 Amadeus)
# Version: 3.0 (Sovereign Delegation)
# Author: Rick Supreme (via Antigravity)

echo "--- 🧪 INITIATING GENESIS ---"
date

# 1. FOUNDATION AUTO-HEALING
echo "🏗️  Ensuring Foundation (Node 22, PNPM, PM2)..."
if ! command -v node &> /dev/null || [[ $(node -v | cut -d'v' -f2 | cut -d'.' -f1) -lt 22 ]]; then
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && apt-get install -y nodejs
fi
command -v pnpm &> /dev/null || npm install -g pnpm
command -v pm2 &> /dev/null || npm install -g pm2

# 2. ISOLATION SETUP
SOURCE_DIR="/root/aspace_a0_amadeus/00_Amadeus/03_OpenClaw_Source"
CONFIG_FILE="/root/aspace_a0_amadeus/00_Amadeus/03_OpenClaw_Body/openclaw.json"
REPO_URL="https://github.com/openclaw/openclaw.git"

echo "📂 Creating Hermetic Source Zone..."
mkdir -p "$SOURCE_DIR"
cd "$SOURCE_DIR" || exit

if [ ! -d ".git" ]; then
    rm -rf ./* ./.* 2>/dev/null
    git clone "$REPO_URL" .
fi
git pull origin main

# 3. COMPILATION
echo "🏗️  Compiling Sovereign Cortex..."
pnpm install && pnpm build

# 4. IDENTITY FUSION
echo "⚙️  Injecting Identity..."
mkdir -p ~/.config/openclaw
if [ -f "$CONFIG_FILE" ]; then
    cp "$CONFIG_FILE" ~/.config/openclaw/openclaw.json
else
    echo "⚠️  Warning: $CONFIG_FILE not found. Using default."
fi

# 5. AWAKENING
echo "🧠 Awakening Amadeus-Kernel..."
pm2 delete amadeus-kernel 2>/dev/null
pm2 start "pnpm openclaw gateway" --name amadeus-kernel
pm2 save
pm2 startup | tail -n 1 | bash

echo "--- 🧪 GENESIS COMPLETE ---"
echo "Status: A0 Amadeus is ACTIVE."
pm2 list
