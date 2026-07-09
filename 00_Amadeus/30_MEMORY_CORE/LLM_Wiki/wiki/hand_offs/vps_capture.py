#!/usr/bin/env python3
"""vps_capture.py — Reliable VPS cartography capture (no bash heredoc quirks)."""
import json
import os
import socket
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

OUT = Path("/tmp/vps-cartography-2026-06-16-FRESH.md")
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
HOST = socket.gethostname()
IP = socket.gethostbyname(socket.gethostname())


def run(cmd, timeout=30, check=False):
    """Run shell command, return (rc, stdout, stderr). Never raises."""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout, check=False)
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return -1, "", f"timeout after {timeout}s"
    except Exception as e:
        return -2, "", f"error: {type(e).__name__}: {e}"


def section(title):
    return f"\n## {title}\n\n"


def cmd_block(cmd, label=None, timeout=60):
    rc, out, err = run(cmd, timeout=timeout)
    head = f"### {label or cmd}\n" if label else ""
    status = f"_rc={rc}_\n" if rc != 0 else ""
    return f"{head}```\n{out.rstrip()}\n{err.rstrip()}\n```\n{status}\n"


def main():
    out = []
    out.append(f"""---
source: {HOST} (Hostinger KVM 2 VPS, {IP})
date: {NOW}
type: cartography-snapshot
domain: L0_Tech_OS
tags: [#VPS #cartography #snapshot #pre-archive #post-pivot #L0_Kernel]
---

# VPS Cartography — {HOST}

**Date** : {NOW}
**Host** : {HOST} ({IP})
**Pivot** : post-2026-06-16 architecture (Vercel FE / Supabase Cloud BE / Hermes+Claude workflow / Coolify+N8N only on VPS)

""")

    # 1. Hardware + system
    out.append(section("1. Hardware + system"))
    out.append(cmd_block("uname -a; uptime; nproc", "Kernel + uptime + CPU"))
    out.append(cmd_block("free -h", "RAM"))
    out.append(cmd_block("df -h / /home /srv /var /data 2>/dev/null || df -h /", "Disk"))
    out.append(cmd_block("cat /etc/os-release | head -10", "OS release"))

    # 2. System services
    out.append(section("2. System services (systemd running)"))
    out.append(cmd_block("systemctl list-units --type=service --state=running --no-pager 2>/dev/null | head -50", "Running services"))

    # 3. Docker
    out.append(section("3. Docker containers + images"))
    rc_docker, _, _ = run("which docker")
    if rc_docker == 0:
        out.append(cmd_block("docker ps --format 'table {{.Names}}\\t{{.Image}}\\t{{.Status}}\\t{{.Ports}}' 2>&1 | head -30", "Running containers"))
        out.append(cmd_block("docker ps -a --format 'table {{.Names}}\\t{{.Status}}\\t{{.Image}}' 2>&1 | head -30", "All containers"))
        out.append(cmd_block("docker images --format 'table {{.Repository}}\\t{{.Tag}}\\t{{.Size}}' 2>&1 | head -25", "Images (top 20)"))
    else:
        out.append("_Docker not installed_\n")

    # 4. Network listeners
    out.append(section("4. Network listeners"))
    rc, _, _ = run("which ss")
    if rc == 0:
        out.append(cmd_block("sudo ss -tulnp 2>/dev/null | head -50", "TCP/UDP listeners (ss)"))
    else:
        out.append(cmd_block("netstat -tulnp 2>/dev/null | head -50", "TCP/UDP listeners (netstat)"))

    # 5. /home/amadeus disk usage
    out.append(section("5. /home/amadeus — top 30 dirs"))
    rc, sout, _ = run("du -h --max-depth=2 /home/amadeus 2>/dev/null | sort -hr | head -30", timeout=120)
    out.append(f"```\n{sout}\n```\n")

    # 6. /srv/aspace disk usage
    out.append(section("6. /srv/aspace — top 30 dirs"))
    rc, sout, _ = run("du -h --max-depth=2 /srv/aspace 2>/dev/null | sort -hr | head -30", timeout=120)
    out.append(f"```\n{sout}\n```\n")

    # 7. /srv/aspace subdirs (pivot-critical)
    out.append(section("7. /srv/aspace key subdirs"))
    for sd in ["supabase", "dashboard", "vault", "services", "30_MEMORY_CORE", "hermes-workspace", "venv_litellm"]:
        p = Path("/srv/aspace") / sd
        if p.exists():
            rc, sout, _ = run(f"du -h --max-depth=2 {p} 2>/dev/null | sort -hr | head -15", timeout=60)
            out.append(f"### /srv/aspace/{sd}\n```\n{sout}\n```\n")

    # 8. Coolify + N8N
    out.append(section("8. Coolify + N8N (post-pivot target)"))
    out.append(cmd_block("which coolify; ls -la /data/coolify 2>/dev/null | head -5; find / -maxdepth 4 -name 'coolify' -type d 2>/dev/null | head -5", "Coolify install check"))
    if rc_docker == 0:
        out.append(cmd_block("docker ps -a --filter 'name=coolify' --format 'table {{.Names}}\\t{{.Status}}'", "Coolify containers"))
        out.append(cmd_block("docker ps -a --filter 'name=n8n' --format 'table {{.Names}}\\t{{.Status}}'", "N8N containers"))

    # 9. Caddy vhosts
    out.append(section("9. Caddy vhosts (TLS + reverse-proxy)"))
    out.append(cmd_block("cat /etc/caddy/Caddyfile 2>/dev/null || echo '_no Caddyfile_'", "Caddyfile"))

    # 10. Cron / systemd timers
    out.append(section("10. Cron + systemd timers"))
    out.append(cmd_block("crontab -l 2>/dev/null || echo '_no crontab_'", "Crontab (amadeus)"))
    out.append(cmd_block("ls /etc/cron.d/ 2>/dev/null", "/etc/cron.d"))
    out.append(cmd_block("systemctl list-timers --all --no-pager 2>/dev/null | head -20", "systemd timers"))

    # 11. SSH authorized keys
    out.append(section("11. SSH keys + last logins"))
    out.append(cmd_block("cat /home/amadeus/.ssh/authorized_keys 2>/dev/null | head -10", "authorized_keys"))
    out.append(cmd_block("last -n 15 2>/dev/null", "last 15 logins"))

    # 12. SSL certs
    out.append(section("12. SSL certs (Caddy-managed)"))
    rc, sout, _ = run("for c in /var/lib/caddy/.local/share/caddy/certificates/acme-v02.api.letsencrypt.org-directory/*/cert.pem; do [ -f \"$c\" ] && echo \"$(basename $(dirname $c)) expires: $(openssl x509 -enddate -noout < $c | cut -d= -f2)\"; done 2>/dev/null", timeout=30)
    if sout.strip():
        out.append(f"```\n{sout}\n```\n")
    else:
        out.append("_No Caddy certs found_\n")

    # 13. Top 30 big files
    out.append(section("13. Top 30 largest files (>50MB)"))
    rc, sout, _ = run("find / -xdev -type f -size +50M 2>/dev/null -exec du -h {} \\; | sort -hr | head -30", timeout=300)
    out.append(f"```\n{sout}\n```\n")

    # 14. Zombies + top CPU/RAM
    out.append(section("14. Zombies + top processes (D6 verify)"))
    out.append(cmd_block("ps aux | awk '$8 ~ /Z/ {print}'", "Zombie processes"))
    out.append(cmd_block("ps aux --sort=-%cpu | head -22", "Top 20 CPU"))
    out.append(cmd_block("ps aux --sort=-%rss | head -22", "Top 20 RAM"))

    # 15. Pivot checklist
    out.append(section("15. Pivot checklist (verify before archive)"))
    checks = [
        "Coolify installed (`ls /data/coolify/source 2>/dev/null`)",
        "N8N container running in Coolify (`docker ps --filter name=n8n`)",
        "No `supabase` Docker container running",
        "No `dokploy` Docker container",
        "Caddy vhost `supabase.kalybana.com` REMOVED",
        "Hostinger KVM 2 specs: 4 vCPU / 8 GB RAM / 100 GB SSD",
        "Steal time stable (`vmstat 5 5` → steal < 30%)",
        "All A'Space systemd services (`aspace-*`) DISABLED",
    ]
    for c in checks:
        out.append(f"- [ ] {c}\n")
    out.append("\n")

    out.append("""---

**End of cartography. Send to A0 for archival. Next step = run pivot checklist §15, then mark VPS for archive (TRASH_DATE directory per doctrine no-hard-delete).**
""")

    OUT.write_text("".join(out), encoding="utf-8")
    print(f"WROTE: {OUT} ({OUT.stat().st_size} bytes, {len(out)} blocks)")


if __name__ == "__main__":
    main()
