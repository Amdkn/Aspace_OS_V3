#!/bin/bash
# 02_Ryan_SysAdmin (The Mechanic)
# Runs Weekly (Sunday 03:00).
# Mission: Updates, Cleaning, Health Check.

echo "--- RYAN PROTOCOL STARTED ---"
date

# 1. System Updates
echo "🔧 Updating Repositories..."
apt-get update -q

echo "🔧 Upgrading Packages..."
apt-get upgrade -y

# 2. Cleaning
echo "🧹 Cleaning APT Cache..."
apt-get autoremove -y
apt-get autoclean

echo "🧹 Cleaning NPM Cache..."
npm cache clean --force

echo "🧹 Vacuuming Journal Logs (Keep 7 days)..."
journalctl --vacuum-time=7d

# 3. Health Check
echo "🏥 Disk Space:"
df -h / | grep /

echo "🏥 Memory Usage:"
free -h

# 4. Reboot Check
if [ -f /var/run/reboot-required ]; then
    echo "🚨 Reboot Required. Scheduling reboot..."
    # reboot
else
    echo "✅ No Reboot Required."
fi

echo "--- RYAN PROTOCOL COMPLETE ---"
