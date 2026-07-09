# VPS Keys: The Architect's Manual to the TARDIS

**Objective**: Learn to "See" the Matrix.
**Role**: The Architect (You) inspecting the Technician's work.
**Philosophy**: "Don't trust. Verify."

---

## 🔑 1. Navigation (Moving through the TARDIS)

To build a mental map of your kingdom, you must walk its halls.

### The Compass: `pwd` (Print Working Directory)
*   **Concept**: "Where am I right now?"
*   **Command**: `pwd`
*   **Output**: `/root/aspace_a0_amadeus` means you are in the Core.

### The Eye: `ls` (List)
*   **Concept**: "What is in this room?"
*   **Command**: `ls -F` (Adds symbols: `/` for folders, `*` for executables).
*   **Command**: `ls -la` (The X-Ray. Shows hidden files like `.env` and permissions).
*   **Try**: `ls -F 10_Tech_OS/` -> You should see `11_Infra`, `12_Interface`, `13_Data`.

### The Portal: `cd` (Change Directory)
*   **Concept**: "Teleport me to..."
*   **Command**: `cd 10_Tech_OS` (Go down).
*   **Command**: `cd ..` (Go up one level).
*   **Command**: `cd ~` (Go Home / The Bridge).

---

## 🔋 2. Vital Signs (Checking the Engines)

The 13th Doctor (Infra) needs energy.

### The Scanner: `htop` (Holistic View)
*   **Concept**: The Dashboard of the TARDIS Console.
*   **Action**: Type `htop`.
*   **Look for**:
    *   **CPU Bars**: Are they full (100%)? (Bad). Empty? (Good).
    *   **Mem (RAM)**: This is your "Short Term Memory". If it's full, the system forgets.
    *   **Swap**: The Emergency Reserve. If used, you need more RAM.
*   **Exit**: Press `F10` or `q` to leave.

### The Storage: `df` (Disk Free)
*   **Concept**: "Is the Cargo Hold full?"
*   **Command**: `df -h` (Human readable).
*   **Look for**: The line ending in `/`. If `Use%` is > 80%, Graham (Backup) needs to purge old files.

---

## 👻 3. The Population (Who lives here?)

### The Census: `ps` (Process Status)
*   **Concept**: "Who is working right now?"
*   **Command**: `ps aux | grep node`
*   **Translation**: "Show me all (a) users (u) processes (x) and filter (grep) for 'node' (apps)."
*   **Result**: You should see `OpenClaw` or `react-scripts`.

### The Identity: `whoami` & `hostname`
*   **Concept**: "Who am I logged in as?"
*   **Command**: `whoami` -> Should be `root` (God Mode).
*   **Command**: `hostname` -> Should be `aspace-vps` (Your Territory).

---

## 🛡️ 4. The Shields (Yaz's Domain)

### The Wall: `ufw` (Uncomplicated Firewall)
*   **Concept**: "Are the doors locked?"
*   **Command**: `ufw status`
*   **Expected**:
    *   `22/tcp ALLOW` (SSH - Your Key).
    *   `80, 443 ALLOW` (Web Traffic).
    *   If you see `Anywhere`, be careful.

### The Bouncer: `fail2ban`
*   **Concept**: "Who have we kicked out?"
*   **Command**: `fail2ban-client status sshd`
*   **Result**: Shows how many unauthorized attempts were blocked.

---

## 🎓 The Exercise (Your First Audit)

1.  **Login**: `ssh root@...`
2.  **Go Home**: `cd /root/aspace_a0_amadeus`
3.  **Verify Structure**: `tree -L 2` (or `ls -R` if tree is missing).
    *   *Do you see the 11th, 12th, and 13th Doctor folders?*
4.  **Check Resources**: `htop`
    *   *Is the machine breathing easily?*
5.  **Check Shields**: `ufw status`
    *   *Is Yaz standing guard?*

*This is how a Visionary touches the bare metal.*
