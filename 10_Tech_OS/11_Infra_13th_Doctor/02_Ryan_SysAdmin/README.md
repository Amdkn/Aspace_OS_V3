# 02_Ryan_SysAdmin (The Mechanic)

**The Maintenance & Health Layer.**
Ryan keeps the engine running smooth.

---

## 🔧 Agent: Ryan Sinclair [A3]
*   **Role**: **System Administrator (Maintenance)**.
*   **Archetype**: The Mechanic.
*   **Mission**: "Don't let the TARDIS rust."

## 🛠️ The Toolkit
1.  **APT Auto-Update**:
    *   **Target**: Security patches (Unattended Upgrades).
2.  **Logrotate**:
    *   **Rule**: Logs < 100MB. Keep 7 days.
3.  **Glances / Htop**:
    *   **Monitor**: CPU < 80%, RAM < 90%.

## 📜 The Script: `ryan_protocol.sh`
*   **Frequency**: Weekly (Sunday 03:00 AM).
*   **Action**: `apt update && upgrade`, `npm cache clean`, `journalctl --vacuum`.
*   **Reboot**: Only if `/var/run/reboot-required` exists.
