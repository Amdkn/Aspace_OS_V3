# VPS Audit Protocol (The Truth)

**Role**: Visionary E-Myth Audit.
**Objective**: Understand the current reality of the Infrastructure before commanding change.
**Executor**: Gemini CLI / Technician.

---

## 👁️ 1. Identity & Core (Who are we?)
*   **Command**: `hostname && whoami && date`
*   **Purpose**: Confirm we are on the correct timeline and machine (`aspace-vps`).
*   **Check**: Are timezones aligned (UTC vs Local)?

## 🧠 2. Resource Utilization (Do we have capacity?)
*   **Command**: `htop -C -n 1 | head -n 20`
*   **Command**: `free -h`
*   **Command**: `df -h /`
*   **Purpose**:
    *   **CPU**: Is the 13th Doctor (Processors) overloaded?
    *   **RAM**: Is the Memory Palace full? (Swap usage is a yellow flag).
    *   **Disk**: The Vault. Is it >80% full?

## 🛡️ 3. Security Perimeter (Are the shields up?)
*   **Command**: `ufw status verbose`
*   **Command**: `fail2ban-client status sshd`
*   **Command**: `last -n 10`
*   **Purpose**:
    *   **UFW**: Is Yaz standing at the door? (Only ports 22, 80, 443 should be open).
    *   **Fail2Ban**: How many Daleks have been banned today?
    *   **Last**: Who else has entered the TARDIS?

## 🕸️ 4. Network & Connectivity (The Web)
*   **Command**: `ss -tulpn | grep LISTEN`
*   **Command**: `curl -4 icanhazip.com`
*   **Purpose**:
    *   **Ports**: What services are *actually* listening? (Look for stray Node processes).
    *   **IP**: Confirm our public identity.

## 🐳 5. Container State (The Engines)
*   **Command**: `docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"`
*   **Command**: `docker stats --no-stream`
*   **Purpose**:
    *   **OpenClaw**: Is the Brain running?
    *   **Postgres**: Is the Memory intact?
    *   **Ghosts**: Are there dead containers haunting resources?

## 📜 6. The Verdict (Strategic Assessment)
*   **Technician Action**: Run these commands.
*   **Visionary Action**: Analyze the output. Decide:
    1.  **Maintain**: System is healthy.
    2.  **Purge**: Resources are wasted.
    3.  **Fortify**: Security is lax.

---

*"First, we see. Then, we act."*
