#!/bin/bash
# 01_Yaz_SecOps (The Shield)
# Runs every 6 hours.
# Mission: Scan logs, ban IPs, check UFW status.

echo "--- YAZ PROTOCOL STARTED ---"
date

# 1. Check UFW Status
ufw status verbose | grep "Active" > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ UFW is Active."
else
    echo "🚨 UFW is DOWN. Reactivating..."
    ufw enable
fi

# 2. Check Fail2Ban
fail2ban-client status sshd > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Fail2Ban is Watching."
else
    echo "🚨 Fail2Ban is DOWN. Restarting..."
    systemctl restart fail2ban
fi

# 3. Scan Auth Logs for Anomalies (Simple Grep)
echo "🔍 Scanning /var/log/auth.log for failures..."
grep "Failed password" /var/log/auth.log | tail -n 5

echo "--- YAZ PROTOCOL COMPLETE ---"
