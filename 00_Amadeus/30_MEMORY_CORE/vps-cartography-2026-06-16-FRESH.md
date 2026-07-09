---
source: srv941028 (Hostinger KVM 2 VPS, 127.0.1.1)
date: 2026-06-17T01:05:58Z
type: cartography-snapshot
domain: L0_Tech_OS
tags: [#VPS #cartography #snapshot #pre-archive #post-pivot #L0_Kernel]
---

# VPS Cartography — srv941028

**Date** : 2026-06-17T01:05:58Z
**Host** : srv941028 (127.0.1.1)
**Pivot** : post-2026-06-16 architecture (Vercel FE / Supabase Cloud BE / Hermes+Claude workflow / Coolify+N8N only on VPS)


## 1. Hardware + system

### Kernel + uptime + CPU
```
Linux srv941028 6.8.0-111-generic #111-Ubuntu SMP PREEMPT_DYNAMIC Sat Apr 11 23:16:02 UTC 2026 x86_64 x86_64 x86_64 GNU/Linux
 01:05:59 up 33 days,  7:49,  7 users,  load average: 56.38, 45.07, 38.91
2

```

### RAM
```
               total        used        free      shared  buff/cache   available
Mem:           7.8Gi       3.4Gi       229Mi        85Mi       4.6Gi       4.4Gi
Swap:          4.0Gi       1.5Gi       2.5Gi

```

### Disk
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        96G   54G   43G  56% /
/dev/sda1        96G   54G   43G  56% /
/dev/sda1        96G   54G   43G  56% /
/dev/sda1        96G   54G   43G  56% /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        96G   54G   43G  56% /

```

### OS release
```
PRETTY_NAME="Ubuntu 24.04.4 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.4 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"

```


## 2. System services (systemd running)

### Running services
```
  UNIT                           LOAD   ACTIVE SUB     DESCRIPTION
  accounts-daemon.service        loaded active running Accounts Service
  aspace-dashboard.service       loaded active running A'Space Mission Control Next.js dashboard
  aspace-rick-watcher.service    loaded active running A'Space OS Rick A1 — Inbox Watcher (A0_TO_A1)
  aspace-watcher@graham.service  loaded active running A'Space OS Inbox Watcher — graham
  aspace-watcher@ryan.service    loaded active running A'Space OS Inbox Watcher — ryan
  aspace-watcher@yaz.service     loaded active running A'Space OS Inbox Watcher — yaz
  avahi-daemon.service           loaded active running Avahi mDNS/DNS-SD Stack
  caddy.service                  loaded active running Caddy
  claude.service                 loaded active running A0 Amadeus — Claude Code Main Agent
  containerd.service             loaded active running containerd container runtime
  cron.service                   loaded active running Regular background program processing daemon
  cups-browsed.service           loaded active running Make remote CUPS printers available locally
  cups.service                   loaded active running CUPS Scheduler
  dbus.service                   loaded active running D-Bus System Message Bus
  docker.service                 loaded active running Docker Application Container Engine
  fail2ban.service               loaded active running Fail2Ban Service
  fwupd.service                  loaded active running Firmware update daemon
  getty@tty1.service             loaded active running Getty on tty1
  ModemManager.service           loaded active running Modem Manager
  multipathd.service             loaded active running Device-Mapper Multipath Device Controller
  NetworkManager.service         loaded active running Network Manager
  opencode.service               loaded active running OpenCode - A'Space Alternative Technician
  polkit.service                 loaded active running Authorization Manager
  qemu-guest-agent.service       loaded active running QEMU Guest Agent
  rsyslog.service                loaded active running System Logging Service
  rtkit-daemon.service           loaded active running RealtimeKit Scheduling Policy Service
  serial-getty@ttyS0.service     loaded active running Serial Getty on ttyS0
  snap.cups.cups-browsed.service loaded active running Service for snap application cups.cups-browsed
  snap.cups.cupsd.service        loaded active running Service for snap application cups.cupsd
  snapd.service                  loaded active running Snap Daemon
  ssh.service                    loaded active running OpenBSD Secure Shell server
  syncthing.service              loaded active running Syncthing — A'Space Vault P2P Sync
  systemd-journald.service       loaded active running Journal Service
  systemd-logind.service         loaded active running User Login Management
  systemd-networkd.service       loaded active running Network Configuration
  systemd-resolved.service       loaded active running Network Name Resolution
  systemd-timesyncd.service      loaded active running Network Time Synchronization
  systemd-udevd.service          loaded active running Rule-based Manager for Device Events and Files
  udisks2.service                loaded active running Disk Manager
  unattended-upgrades.service    loaded active running Unattended Upgrades Shutdown
  upower.service                 loaded active running Daemon for power management
  user@0.service                 loaded active running User Manager for UID 0
  user@1001.service              loaded active running User Manager for UID 1001
  wpa_supplicant.service         loaded active running WPA supplicant

Legend: LOAD   → Reflects whether the unit definition was properly loaded.
        ACTIVE → The high-level unit activation state, i.e. generalization of SUB.
        SUB    → The low-level unit activation state, values depend on unit type.

```


## 3. Docker containers + images

### Running containers
```

timeout after 60s
```
_rc=-1_

### All containers
```

timeout after 60s
```
_rc=-1_

### Images (top 20)
```

timeout after 60s
```
_rc=-1_


## 4. Network listeners

### TCP/UDP listeners (ss)
```
Netid State  Recv-Q Send-Q Local Address:Port  Peer Address:PortProcess                                                    
udp   UNCONN 0      0         127.0.0.54:53         0.0.0.0:*    users:(("systemd-resolve",pid=1690491,fd=16))             
udp   UNCONN 0      0      127.0.0.53%lo:53         0.0.0.0:*    users:(("systemd-resolve",pid=1690491,fd=14))             
udp   UNCONN 0      0            0.0.0.0:21027      0.0.0.0:*    users:(("syncthing",pid=1379,fd=22))                      
udp   UNCONN 0      0            0.0.0.0:4789       0.0.0.0:*                                                              
udp   UNCONN 0      0            0.0.0.0:5353       0.0.0.0:*    users:(("avahi-daemon",pid=2439519,fd=12))                
udp   UNCONN 0      0            0.0.0.0:34512      0.0.0.0:*    users:(("avahi-daemon",pid=2439519,fd=14))                
udp   UNCONN 0      0            0.0.0.0:35193      0.0.0.0:*    users:(("syncthing",pid=1379,fd=21))                      
udp   UNCONN 0      0                  *:7946             *:*    users:(("dockerd",pid=548785,fd=43))                      
udp   UNCONN 0      0                  *:443              *:*    users:(("caddy",pid=1052,fd=8))                           
udp   UNCONN 0      0               [::]:21027         [::]:*    users:(("syncthing",pid=1379,fd=23))                      
udp   UNCONN 0      0               [::]:5353          [::]:*    users:(("avahi-daemon",pid=2439519,fd=13))                
udp   UNCONN 0      0                  *:22000            *:*    users:(("syncthing",pid=1379,fd=15))                      
udp   UNCONN 0      0               [::]:54958         [::]:*    users:(("avahi-daemon",pid=2439519,fd=15))                
udp   UNCONN 0      0               [::]:47421         [::]:*    users:(("syncthing",pid=1379,fd=18))                      
tcp   LISTEN 0      2048       127.0.0.1:9119       0.0.0.0:*    users:(("hermes",pid=4144233,fd=14))                      
tcp   LISTEN 0      4096       127.0.0.1:631        0.0.0.0:*    users:(("cupsd",pid=3663426,fd=7))                        
tcp   LISTEN 0      4096   127.0.0.53%lo:53         0.0.0.0:*    users:(("systemd-resolve",pid=1690491,fd=15))             
tcp   LISTEN 0      4096      127.0.0.54:53         0.0.0.0:*    users:(("systemd-resolve",pid=1690491,fd=17))             
tcp   LISTEN 0      128        127.0.0.1:8642       0.0.0.0:*    users:(("hermes",pid=1624269,fd=19))                      
tcp   LISTEN 0      4096         0.0.0.0:5432       0.0.0.0:*    users:(("docker-proxy",pid=928168,fd=8))                  
tcp   LISTEN 0      4096       127.0.0.1:8384       0.0.0.0:*    users:(("syncthing",pid=1379,fd=14))                      
tcp   LISTEN 0      4096         0.0.0.0:9081       0.0.0.0:*    users:(("docker-proxy",pid=549202,fd=8))                  
tcp   LISTEN 0      4096       127.0.0.1:2019       0.0.0.0:*    users:(("caddy",pid=1052,fd=13))                          
tcp   LISTEN 0      511        127.0.0.1:6080       0.0.0.0:*    users:(("next-server (v1",pid=2400652,fd=21))             
tcp   LISTEN 0      4096         0.0.0.0:8443       0.0.0.0:*    users:(("docker-proxy",pid=930092,fd=8))                  
tcp   LISTEN 0      4096         0.0.0.0:22         0.0.0.0:*    users:(("sshd",pid=1690496,fd=3),("systemd",pid=1,fd=264))
tcp   LISTEN 0      4096         0.0.0.0:8001       0.0.0.0:*    users:(("docker-proxy",pid=929732,fd=8))                  
tcp   LISTEN 0      4096         0.0.0.0:8000       0.0.0.0:*    users:(("docker-proxy",pid=930072,fd=8))                  
tcp   LISTEN 0      511        127.0.0.1:3001       0.0.0.0:*    users:(("MainThread",pid=4095737,fd=21))                  
tcp   LISTEN 0      4096         0.0.0.0:6543       0.0.0.0:*    users:(("docker-proxy",pid=928198,fd=8))                  
tcp   LISTEN 0      4096               *:22000            *:*    users:(("syncthing",pid=1379,fd=13))                      
tcp   LISTEN 0      4096            [::]:5432          [::]:*    users:(("docker-proxy",pid=928178,fd=8))                  
tcp   LISTEN 0      4096            [::]:9081          [::]:*    users:(("docker-proxy",pid=549208,fd=8))                  
tcp   LISTEN 0      4096           [::1]:631           [::]:*    users:(("cupsd",pid=3663426,fd=6))                        
tcp   LISTEN 0      4096               *:443              *:*    users:(("caddy",pid=1052,fd=16))                          
tcp   LISTEN 0      4096            [::]:8443          [::]:*    users:(("docker-proxy",pid=930097,fd=8))                  
tcp   LISTEN 0      4096               *:80               *:*    users:(("caddy",pid=1052,fd=19))                          
tcp   LISTEN 0      4096            [::]:8001          [::]:*    users:(("docker-proxy",pid=929739,fd=8))                  
tcp   LISTEN 0      4096            [::]:8000          [::]:*    users:(("docker-proxy",pid=930078,fd=8))                  
tcp   LISTEN 0      4096               *:7946             *:*    users:(("dockerd",pid=548785,fd=39))                      
tcp   LISTEN 0      4096               *:3010             *:*    users:(("dockerd",pid=548785,fd=61))                      
tcp   LISTEN 0      511            [::1]:3001          [::]:*    users:(("MainThread",pid=4095737,fd=22))                  
tcp   LISTEN 0      4096            [::]:6543          [::]:*    users:(("docker-proxy",pid=928203,fd=8))                  
tcp   LISTEN 0      4096               *:2377             *:*    users:(("dockerd",pid=548785,fd=37))

```


## 5. /home/amadeus — top 30 dirs

```

```

## 6. /srv/aspace — top 30 dirs

```
2.7G	/srv/aspace
1.4G	/srv/aspace/supabase
734M	/srv/aspace/supabase/apps
595M	/srv/aspace/supabase/.git
479M	/srv/aspace/dashboard
470M	/srv/aspace/dashboard/node_modules
278M	/srv/aspace/web/Life-OS-2026
278M	/srv/aspace/web
206M	/srv/aspace/hermes-workspace
204M	/srv/aspace/venv_litellm/lib
204M	/srv/aspace/venv_litellm
107M	/srv/aspace/hermes-workspace/.git
94M	/srv/aspace/vault
83M	/srv/aspace/services
62M	/srv/aspace/services/dokploy-mcp
53M	/srv/aspace/vault/20_RUNTIME
51M	/srv/aspace/hermes-workspace/public
35M	/srv/aspace/vault/00_ORIGIN
29M	/srv/aspace/supabase/examples
20M	/srv/aspace/services/hermes
20M	/srv/aspace/hermes-workspace/electron
18M	/srv/aspace/hermes-workspace/docs
12M	/srv/aspace/30_MEMORY_CORE
11M	/srv/aspace/30_MEMORY_CORE/Gemini_Takeout_2026
9.8M	/srv/aspace/supabase/packages
8.6M	/srv/aspace/dashboard/.next
8.4M	/srv/aspace/hermes-workspace/src
6.0M	/srv/aspace/vault/30_MEMORY_CORE
3.5M	/srv/aspace/logs
3.0M	/srv/aspace/monitoring

```

## 7. /srv/aspace key subdirs

### /srv/aspace/supabase
```
1.4G	/srv/aspace/supabase
734M	/srv/aspace/supabase/apps
595M	/srv/aspace/supabase/.git
593M	/srv/aspace/supabase/.git/objects
365M	/srv/aspace/supabase/apps/www
311M	/srv/aspace/supabase/apps/docs
45M	/srv/aspace/supabase/apps/studio
29M	/srv/aspace/supabase/examples
12M	/srv/aspace/supabase/examples/edge-functions
9.8M	/srv/aspace/supabase/packages
9.4M	/srv/aspace/supabase/apps/ui-library
4.2M	/srv/aspace/supabase/examples/auth
3.5M	/srv/aspace/supabase/packages/ui-patterns
3.4M	/srv/aspace/supabase/examples/slack-clone
3.1M	/srv/aspace/supabase/examples/realtime

```
### /srv/aspace/dashboard
```
479M	/srv/aspace/dashboard
470M	/srv/aspace/dashboard/node_modules
172M	/srv/aspace/dashboard/node_modules/next
125M	/srv/aspace/dashboard/node_modules/@next
23M	/srv/aspace/dashboard/node_modules/typescript
17M	/srv/aspace/dashboard/node_modules/@img
11M	/srv/aspace/dashboard/node_modules/es-abstract
11M	/srv/aspace/dashboard/node_modules/@babel
9.7M	/srv/aspace/dashboard/node_modules/lightningcss-linux-x64-gnu
8.6M	/srv/aspace/dashboard/.next
7.9M	/srv/aspace/dashboard/node_modules/@typescript-eslint
7.6M	/srv/aspace/dashboard/node_modules/@napi-rs
7.2M	/srv/aspace/dashboard/node_modules/react-dom
6.6M	/srv/aspace/dashboard/.next/server
6.2M	/srv/aspace/dashboard/node_modules/zod

```
### /srv/aspace/vault
```
94M	/srv/aspace/vault
53M	/srv/aspace/vault/20_RUNTIME
51M	/srv/aspace/vault/20_RUNTIME/24_Archive
35M	/srv/aspace/vault/00_ORIGIN/alerts
35M	/srv/aspace/vault/00_ORIGIN
6.0M	/srv/aspace/vault/30_MEMORY_CORE/31_Raw_Logs
6.0M	/srv/aspace/vault/30_MEMORY_CORE
808K	/srv/aspace/vault/20_RUNTIME/23_DLQ_Donna
356K	/srv/aspace/vault/20_RUNTIME/22_Active_WIP
224K	/srv/aspace/vault/10_FORGE
92K	/srv/aspace/vault/session-auth
88K	/srv/aspace/vault/10_FORGE/14_Skills
64K	/srv/aspace/vault/10_FORGE/12_Blueprints
40K	/srv/aspace/vault/12_Blueprints
32K	/srv/aspace/vault/22_Active_WIP

```
### /srv/aspace/services
```
83M	/srv/aspace/services
62M	/srv/aspace/services/dokploy-mcp/node_modules
62M	/srv/aspace/services/dokploy-mcp
20M	/srv/aspace/services/hermes
11M	/srv/aspace/services/hermes/skills
9.4M	/srv/aspace/services/hermes/bin
464K	/srv/aspace/services/openclaw
436K	/srv/aspace/services/openclaw/.openclaw
204K	/srv/aspace/services/hermes/agents
112K	/srv/aspace/services/hermes/logs
52K	/srv/aspace/services/supabase
20K	/srv/aspace/services/dokploy-mcp/src
16K	/srv/aspace/services/openclaw/23_DLQ_Donna
16K	/srv/aspace/services/hermes/23_DLQ_Donna
16K	/srv/aspace/services/dokploy-mcp/dist

```
### /srv/aspace/30_MEMORY_CORE
```
12M	/srv/aspace/30_MEMORY_CORE
11M	/srv/aspace/30_MEMORY_CORE/Gemini_Takeout_2026
728K	/srv/aspace/30_MEMORY_CORE/LLM_Wiki
484K	/srv/aspace/30_MEMORY_CORE/LLM_Wiki/raw
196K	/srv/aspace/30_MEMORY_CORE/LLM_Wiki/wiki
44K	/srv/aspace/30_MEMORY_CORE/LLM_Wiki/LLM Wiki
40K	/srv/aspace/30_MEMORY_CORE/Gemini_Takeout_2026/Export Gemini 05
12K	/srv/aspace/30_MEMORY_CORE/wiki
12K	/srv/aspace/30_MEMORY_CORE/system
4.0K	/srv/aspace/30_MEMORY_CORE/incidents
4.0K	/srv/aspace/30_MEMORY_CORE/daily-summaries

```
### /srv/aspace/hermes-workspace
```
206M	/srv/aspace/hermes-workspace
107M	/srv/aspace/hermes-workspace/.git/objects
107M	/srv/aspace/hermes-workspace/.git
51M	/srv/aspace/hermes-workspace/public
20M	/srv/aspace/hermes-workspace/electron
18M	/srv/aspace/hermes-workspace/public/avatars
18M	/srv/aspace/hermes-workspace/docs
17M	/srv/aspace/hermes-workspace/public/assets
11M	/srv/aspace/hermes-workspace/docs/hermesworld
9.2M	/srv/aspace/hermes-workspace/public/screenshots
8.4M	/srv/aspace/hermes-workspace/src
5.7M	/srv/aspace/hermes-workspace/docs/screenshots
4.0M	/srv/aspace/hermes-workspace/src/screens
2.2M	/srv/aspace/hermes-workspace/screenshots
1.5M	/srv/aspace/hermes-workspace/src/components

```
### /srv/aspace/venv_litellm
```
204M	/srv/aspace/venv_litellm/lib/python3.12
204M	/srv/aspace/venv_litellm/lib
204M	/srv/aspace/venv_litellm
108K	/srv/aspace/venv_litellm/bin
8.0K	/srv/aspace/venv_litellm/include
4.0K	/srv/aspace/venv_litellm/include/python3.12

```

## 8. Coolify + N8N (post-pivot target)

### Coolify install check
```

timeout after 60s
```
_rc=-1_

### Coolify containers
```
NAMES     STATUS

```

### N8N containers
```
NAMES     STATUS

```


## 9. Caddy vhosts (TLS + reverse-proxy)

### Caddyfile
```
﻿﻿vnc.148.230.92.235.sslip.io {
	reverse_proxy 127.0.0.1:6080
	header -server
}

hermes-workspace.148.230.92.235.sslip.io {
	reverse_proxy 127.0.0.1:3001
	header -server
}

hermes-dashboard.148.230.92.235.sslip.io {
	@unlock query unlock=hdMQL4i4RzOLvgl25Y6GCdj2N7m8e9k0x29sjVoJLTs
	@admin header_regexp admin Cookie "(?:^|; )aspace_admin=hdMQL4i4RzOLvgl25Y6GCdj2N7m8e9k0x29sjVoJLTs(?:;|$)"
	@desktop_rest header X-Hermes-Session-Token *
	@desktop_ws path /api/ws* /api/pty* /api/pub* /api/events*

	header @unlock Set-Cookie "aspace_admin=hdMQL4i4RzOLvgl25Y6GCdj2N7m8e9k0x29sjVoJLTs; Path=/; Domain=.148.230.92.235.sslip.io; Max-Age=2592000; Secure; HttpOnly; SameSite=Lax"
	redir @unlock /

	handle @desktop_rest {
		reverse_proxy 127.0.0.1:9119 {
			header_up Host 127.0.0.1:9119
			header_up Origin http://127.0.0.1:9119
		}
	}

	handle @desktop_ws {
		reverse_proxy 127.0.0.1:9119 {
			header_up Host 127.0.0.1:9119
			header_up Origin http://127.0.0.1:9119
		}
	}

	handle @admin {
		reverse_proxy 127.0.0.1:9119 {
			header_up Host 127.0.0.1:9119
			header_up Origin http://127.0.0.1:9119
		}
	}

	respond 403
	header -server
}

dokploy.148.230.92.235.sslip.io {
	reverse_proxy 127.0.0.1:3002
	header -server
}


supabase-studio.148.230.92.235.sslip.io {
	@unlock query unlock=hdMQL4i4RzOLvgl25Y6GCdj2N7m8e9k0x29sjVoJLTs
	@admin header_regexp admin Cookie "(?:^|; )aspace_admin=hdMQL4i4RzOLvgl25Y6GCdj2N7m8e9k0x29sjVoJLTs(?:;|$)"

	header @unlock Set-Cookie "aspace_admin=hdMQL4i4RzOLvgl25Y6GCdj2N7m8e9k0x29sjVoJLTs; Path=/; Domain=.148.230.92.235.sslip.io; Max-Age=2592000; Secure; HttpOnly; SameSite=Lax"
	redir @unlock / 302

	handle @admin {
		reverse_proxy 127.0.0.1:8001
	}

	respond "Forbidden" 403
	header -server
}

aspace-dashboard.148.230.92.235.sslip.io {
	@unlock query unlock=hdMQL4i4RzOLvgl25Y6GCdj2N7m8e9k0x29sjVoJLTs
	@admin header_regexp admin Cookie "(?:^|; )aspace_admin=hdMQL4i4RzOLvgl25Y6GCdj2N7m8e9k0x29sjVoJLTs(?:;|$)"

	header @unlock Set-Cookie "aspace_admin=hdMQL4i4RzOLvgl25Y6GCdj2N7m8e9k0x29sjVoJLTs; Path=/; Domain=.148.230.92.235.sslip.io; Max-Age=2592000; Secure; HttpOnly; SameSite=Lax"
	redir @unlock /tokens 302

	handle @admin {
	header Set-Cookie "aspace_admin=hdMQL4i4RzOLvgl25Y6GCdj2N7m8e9k0x29sjVoJLTs; Path=/; Domain=.148.230.92.235.sslip.io; Max-Age=2592000; Secure; HttpOnly; SameSite=Lax"
		reverse_proxy 127.0.0.1:6080
	}

	respond "Forbidden" 403
}

supabase-api.148.230.92.235.sslip.io {
	reverse_proxy 127.0.0.1:8000
	header -server
}


# OMK Dashboard SaaS — wired 2026-06-14
omk.kalybana.com {
	reverse_proxy 127.0.0.1:3010
	header -server
}


# supabase.kalybana.com — wired 2026-06-14 (D7 fix, A2 HITL granted) — CLEAN SYNTAX
supabase.kalybana.com {
	reverse_proxy 127.0.0.1:8000
	header -server
}

```


## 10. Cron + systemd timers

### Crontab (amadeus)
```
_no crontab_

```

### /etc/cron.d
```
docker-image-prune
e2scrub_all
spad-dispatch
sysstat

```

### systemd timers
```
NEXT                                 LEFT LAST                               PASSED UNIT                           ACTIVATES
Wed 2026-06-17 01:17:18 UTC       4min 0s Wed 2026-06-17 01:12:18 UTC       59s ago aspace-resource-monitor.timer  aspace-resource-monitor.service
Wed 2026-06-17 01:17:42 UTC      4min 24s Wed 2026-06-17 01:12:40 UTC       38s ago aspace-supabase-health.timer   aspace-supabase-health.service
Wed 2026-06-17 01:20:00 UTC          6min Wed 2026-06-17 01:10:00 UTC  3min 18s ago sysstat-collect.timer          sysstat-collect.service
Wed 2026-06-17 01:20:47 UTC          7min Wed 2026-06-17 00:20:47 UTC     52min ago aspace-token-scan.timer        aspace-token-scan.service
Wed 2026-06-17 01:22:57 UTC          9min Wed 2026-06-17 01:12:48 UTC       30s ago aspace-cpu-orchestrator.timer  aspace-cpu-orchestrator.service
Wed 2026-06-17 01:37:04 UTC         23min Wed 2026-06-17 00:58:14 UTC     15min ago fwupd-refresh.timer            fwupd-refresh.service
Wed 2026-06-17 05:59:59 UTC      4h 46min Tue 2026-06-16 09:14:17 UTC       15h ago apt-daily.timer                apt-daily.service
Wed 2026-06-17 06:00:00 UTC      4h 46min Tue 2026-06-16 06:00:02 UTC       19h ago aspace-graham-daily.timer      aspace-graham-daily.service
Wed 2026-06-17 06:21:23 UTC       5h 8min Tue 2026-06-16 22:32:26 UTC  2h 40min ago motd-news.timer                motd-news.service
Wed 2026-06-17 06:31:48 UTC      5h 18min Tue 2026-06-16 06:19:21 UTC       18h ago apt-daily-upgrade.timer        apt-daily-upgrade.service
Wed 2026-06-17 08:05:07 UTC            6h Tue 2026-06-16 07:11:03 UTC       18h ago man-db.timer                   man-db.service
Wed 2026-06-17 17:22:59 UTC           16h Tue 2026-06-16 17:22:59 UTC        7h ago update-notifier-download.timer update-notifier-download.service
Wed 2026-06-17 17:32:33 UTC           16h Tue 2026-06-16 17:32:33 UTC        7h ago systemd-tmpfiles-clean.timer   systemd-tmpfiles-clean.service
Thu 2026-06-18 00:00:00 UTC           22h Wed 2026-06-17 00:00:00 UTC  1h 13min ago dpkg-db-backup.timer           dpkg-db-backup.service
Thu 2026-06-18 00:00:00 UTC           22h Wed 2026-06-17 00:00:00 UTC  1h 13min ago logrotate.timer                logrotate.service
Thu 2026-06-18 00:07:00 UTC           22h Wed 2026-06-17 00:07:00 UTC   1h 6min ago sysstat-summary.timer          sysstat-summary.service
Sun 2026-06-21 03:10:09 UTC        4 days Sun 2026-06-14 03:10:05 UTC    2 days ago e2scrub_all.timer              e2scrub_all.service
Mon 2026-06-22 01:05:56 UTC        4 days Mon 2026-06-15 01:31:57 UTC 1 day 23h ago fstrim.timer                   fstrim.service
Sun 2026-06-28 02:37:15 UTC 1 week 4 days Mon 2026-06-15 03:32:34 UTC 1 day 21h ago update-notifier-motd.timer     update-notifier-motd.service

```


## 11. SSH keys + last logins

### authorized_keys
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIH5ZZwkugTrGm/86uMr/wd26HvtYxcA1Z42h/aqufcV7 antigravity-l0-bridge
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHTXXAbM/IDjpPUBOHj/oqgyKXjZChNO/XDzHWLaR/ev amadeus@aspace-l0-vps
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIQ8FccJ7AbReq/ZpSaI+MwYPDfv3MBHJ7VU5jAMZQyx amadeus@pc

```

### last 15 logins
```
amadeus  pts/0        174.102.16.12    Thu May 21 20:45 - 21:44  (00:59)
reboot   system boot  6.8.0-111-generi Thu May 14 17:16   still running
reboot   system boot  6.8.0-111-generi Thu May 14 06:14   still running
amadeus  pts/0        174.102.16.12    Wed May 13 05:39 - 05:40  (00:00)
amadeus  pts/2        174.102.16.12    Tue May 12 17:02 - 22:30  (05:28)
amadeus  pts/5        174.102.16.12    Tue May 12 04:18 - 05:41  (01:22)
amadeus  pts/2        174.102.16.12    Tue May 12 03:53 - 06:09  (02:15)
amadeus  pts/4        174.102.16.12    Tue May 12 00:54 - 03:20  (02:26)
amadeus  pts/14       174.102.16.12    Mon May 11 06:33 - 03:20  (20:47)
amadeus  pts/13       174.102.16.12    Mon May 11 06:32 - 03:20  (20:48)
amadeus  pts/8        174.102.16.12    Sun May 10 23:14 - 01:31  (02:17)
amadeus  pts/7        174.102.16.12    Sun May 10 20:52 - 03:20 (1+06:27)
amadeus  pts/2        174.102.16.12    Sun May 10 19:08 - 01:25 (1+06:17)
amadeus  pts/1        174.102.16.12    Sun May 10 08:01 - 11:00  (02:58)
amadeus  pts/0        174.102.16.12    Sun May 10 07:09 - 12:58  (05:48)

wtmp begins Wed Mar 25 15:01:25 2026

```


## 12. SSL certs (Caddy-managed)

_No Caddy certs found_

## 13. Top 30 largest files (>50MB)

```

```

## 14. Zombies + top processes (D6 verify)

### Zombie processes
```
root     1180746  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1449403  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1449687  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1481430  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1481767  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1482153  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1483339  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1484048  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1484327  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1484606  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1484902  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1485234  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1486408  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1486833  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1487192  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1487508  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1488169  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1489068  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1489516  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1489965  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1490331  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1490675  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1491105  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1491451  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1492148  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1492449  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1492742  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1493053  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1493437  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1493814  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1495409  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1495738  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1496096  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1496384  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1496633  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1497023  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1497330  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1498937  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1499293  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1499933  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1500221  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1500506  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1500869  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1501606  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1502683  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1503010  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1503312  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1503879  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1504161  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1504441  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1504781  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1505220  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1506066  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1506364  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1507069  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1507312  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1507626  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1508027  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1508318  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1509189  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1510756  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1511074  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1511583  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1511914  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1512263  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1512677  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1514260  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1514522  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1514750  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1515133  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1515911  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1516223  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1517880  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1518265  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1518590  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1518936  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1519345  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1521793  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1522093  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1522465  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1522745  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1523069  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1523398  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1525470  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1525800  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1526105  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1526368  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1527015  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1527847  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1528781  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1529045  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1529392  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1529647  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1531554  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1531863  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1532207  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1532454  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1532701  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1532982  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1533273  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1533591  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1533907  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1534347  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1534675  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1536054  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1536510  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1536861  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1537877  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1538317  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1539855  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1540579  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1540854  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1541315  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1542074  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1542520  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1545414  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1545750  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1546049  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1546503  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1548408  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1548853  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1549240  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1549661  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1550017  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1550489  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1550801  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1551699  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1552110  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1552370  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1552620  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1552901  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1553537  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1555432  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1555697  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1556299  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1556555  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1556808  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1557186  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1558359  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1558879  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1559174  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1559513  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1559922  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1560161  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1560417  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1560678  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1561004  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1561306  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1561699  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1563697  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1564015  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1564332  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1564603  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1564933  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1565389  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1566615  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1567352  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1567686  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1567961  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1568327  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1569441  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1569802  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1570286  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1570573  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1570838  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1571458  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1571894  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1572623  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1572924  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1573239  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1573543  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1573868  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1574220  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1574616  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1575029  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1575763  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1576137  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1576430  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1576731  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1577018  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1579500  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1579847  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1580188  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1580549  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1581026  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1581373  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1581725  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1582041  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1582388  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1582986  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1583310  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1583563  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1586537  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1586782  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1587098  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1587412  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1587708  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1588493  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1588840  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1589168  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1589761  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1590050  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1590726  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1591120  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1591475  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1592070  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1592388  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1592649  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1592930  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1593272  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1593692  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1594084  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1595182  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1595452  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1596017  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1596358  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1596668  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1597022  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1597417  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1597766  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1598155  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1599151  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1599405  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1599749  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1599991  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1600324  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1600578  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1600932  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1601304  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1601618  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1602102  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1602401  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1602747  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1603065  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1603316  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1603654  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1604053  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1604379  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1605216  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1605902  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1606629  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1607277  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1607523  0.0  0.0      0     0 ?        Z    Jun14   0:01 [node] <defunct>
root     1607888  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1608258  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1608539  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1608886  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1609707  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1609996  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1610255  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1610556  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1610818  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1611655  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1611994  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1612285  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1612735  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1613398  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1613695  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1614045  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1614378  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1614732  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1615205  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1616895  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1617255  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1617900  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1618243  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1618591  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1618892  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1619569  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1619901  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1620675  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1621094  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1621450  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1621714  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1622082  0.0  0.0      0     0 ?        Z    Jun14   0:02 [node] <defunct>
root     1622409  0.0  0.0      0     0 ?        Z    Jun14   0:03 [node] <defunct>
root     1623878  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1624380  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1624636  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1624897  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1625141  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1625496  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1625772  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1626108  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1627543  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1628003  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1628299  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1628583  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1628902  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1629562  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1629799  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1630110  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1630474  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1630943  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1631692  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1631991  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1632668  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1633428  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1633802  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1634134  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1635558  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1635850  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1636111  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1636457  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1637131  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1637795  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1638170  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1638583  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1638905  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1638962  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1639272  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1639298  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1639533  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1639627  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1639868  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1640209  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1640526  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1640838  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1641371  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1642029  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1642646  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1643009  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1643390  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1643735  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1644107  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1644499  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1644907  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1645981  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1646398  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1646737  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1647026  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1647380  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1647654  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1648112  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1648517  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1648948  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1649314  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1649631  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1649937  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1650788  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1651100  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1651491  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1651942  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1652702  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1653019  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1653299  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1653574  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1654146  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1654479  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1655142  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1655464  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1656536  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1657148  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1657465  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1657864  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1658179  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1660024  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1660356  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1660727  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1661419  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1661766  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1662113  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1662496  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1663236  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1663927  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1664218  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1664574  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1664858  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1665200  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1665549  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1665870  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1666973  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1667778  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1668455  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1669035  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1669308  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1669599  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1669896  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1670362  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1670739  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1672042  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1672676  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1672965  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1673237  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1674258  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1674690  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1674976  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1675666  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1675960  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1676219  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1676918  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1677278  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1677940  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1678716  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1679035  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1679613  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1679933  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1680197  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1680573  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1680839  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1681225  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1681952  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1682347  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1682602  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1683158  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1683527  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1684297  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1685000  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1685365  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1686059  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1686466  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1686791  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1687483  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1687809  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1688181  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1688548  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1688910  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1689214  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1689927  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1690267  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1690843  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1691603  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1691866  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1692175  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1692541  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1692999  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1693367  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1693685  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1694317  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1694667  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1694991  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1695266  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1695553  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1695821  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1696176  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1697308  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1697568  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1697853  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1698113  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1698403  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1698737  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1699108  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1699444  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1700114  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1700375  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1700745  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1701048  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1701325  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1701626  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1702192  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1702858  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1703211  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1704678  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1705006  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1705353  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1705678  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1706125  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1706809  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1707888  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1708194  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1708911  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1709234  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1709472  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1709782  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1710218  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1710591  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1712091  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1712834  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1713234  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1713534  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1714087  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1714958  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1715954  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1716922  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1717226  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1718197  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1718505  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1718901  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1719500  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1720101  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1720428  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1721444  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1721778  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1722010  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1722372  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1722642  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1722981  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1723373  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1724039  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1725495  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1726348  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1726594  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1726977  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1727328  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1727653  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1727937  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1728321  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1728655  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1728939  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1729278  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1729860  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1730114  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1730433  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1731211  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1731657  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1733324  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1733649  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1734051  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1734450  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1734770  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1735066  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1735435  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1735861  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1736190  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1736518  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1736778  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1737319  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1737626  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1737995  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1738673  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1739127  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1739764  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1740017  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1740312  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1740516  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1740806  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1741232  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1741609  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1741917  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1742191  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1742872  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1743136  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1743449  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1744088  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1744435  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1744747  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1745070  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1745502  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1745908  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1746243  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1746581  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1746916  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1747885  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1748551  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1749279  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1750073  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1750748  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1751071  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1751370  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1751603  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1751930  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1752224  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1752467  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1752523  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1752889  0.0  0.0      0     0 ?        Z    Jun15   0:00 [node] <defunct>
root     1754015  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1754291  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1754574  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1754826  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1755873  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1756206  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1756548  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1757362  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1757664  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1757972  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1758292  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1758587  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1759680  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1760097  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1760354  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1762027  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1762525  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1764680  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1765067  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1765477  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1765853  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1766153  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1766584  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1767252  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1767686  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1768333  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1768689  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1768944  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1769234  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1769547  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1769843  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1770180  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1770534  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1772002  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1772269  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1772565  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1772812  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1773133  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1773503  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1773926  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1774266  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1775601  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1775828  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1776160  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1776440  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1776732  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1777102  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1777878  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1778687  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1778908  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1779189  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1779787  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1780114  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1780518  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1781947  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1782333  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1782645  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1782913  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1783155  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1783438  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1783784  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1784148  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1784434  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1784790  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1785582  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1785907  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1786625  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1786943  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1787256  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1787543  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1787807  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1788269  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1788598  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1789277  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1789592  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1789931  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1790222  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1790519  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1790744  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1791088  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1791459  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1792239  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1793300  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1793609  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1793945  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1794281  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1797290  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1798128  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1799457  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1799779  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1800330  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1802335  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1802607  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1802823  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1803145  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1803467  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1803726  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1804964  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1805335  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1805647  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1805937  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1806237  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1806606  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1806928  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1807211  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1808381  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1809442  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1809733  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1810030  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1810383  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1810713  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1811084  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1812574  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1812879  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1813113  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1813418  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1813687  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1814011  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1815468  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1815787  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1816141  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1816436  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1816719  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1817817  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1818973  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1819301  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1819543  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1819905  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1820191  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1820577  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1820980  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1821315  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1821736  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1822420  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1822744  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1822973  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1823248  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1824576  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1825642  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1826269  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1826564  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1827640  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1828068  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1829821  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1830127  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1830429  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1831629  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1832731  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1833020  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1833352  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1833660  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1833927  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1834294  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1836047  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1836387  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1836785  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1837099  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1839834  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1840096  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1840350  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1840648  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1840975  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1841307  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1842444  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1842729  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1843042  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1843356  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1843656  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1843933  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1844243  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1844631  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1845029  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1845438  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1846797  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1847045  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1847374  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1847730  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1848188  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1848914  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1849240  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1849525  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1850347  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1850979  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1851374  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1852145  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1852505  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1852737  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1853073  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1853367  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1853719  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1854052  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1854384  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1854735  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1855933  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1856518  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1856854  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1857830  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1858683  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1859067  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1859344  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1859649  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1859897  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1860318  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1860605  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1860902  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1861305  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1861741  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1862547  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1862843  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1863169  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1863460  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1864060  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1864467  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1865347  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1866421  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1866782  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1867018  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1867618  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1867882  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1868326  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1868634  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1869731  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1870061  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1870343  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1870686  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1871027  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1871311  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1871685  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1873499  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1873858  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1874524  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1874809  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1875199  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1875586  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1876913  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1877738  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1880243  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1880697  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1881030  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1881262  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1881581  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1882343  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1882708  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1883380  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1883657  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1883949  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1884216  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1884601  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1884928  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1885336  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1886051  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1886348  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1886796  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1887183  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1888436  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1888830  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1889279  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1890016  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1890366  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1890599  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1891231  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1891517  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1891831  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1892194  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1892523  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1892922  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1893200  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1893465  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1893835  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1894081  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1894620  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1894913  0.0  0.0      0     0 ?        Z    Jun15   0:04 [node] <defunct>
root     1895262  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1896493  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1896735  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1897009  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1897304  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1897558  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1897879  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1898190  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1898582  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1900044  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1900392  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1900681  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1900946  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1901235  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1901543  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1901837  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1902221  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1902661  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1903046  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1904136  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1904400  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1905283  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1905524  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1905865  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1906177  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1906754  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1907462  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1908173  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1908536  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1908885  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1909647  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1910044  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1911514  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1911839  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1912164  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1912425  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1912815  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1913307  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1914001  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1914786  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1915125  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1915769  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1916165  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1916465  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1916762  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1917146  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1917541  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1917897  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1918341  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1918619  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1919046  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1919363  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1919955  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1920732  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1921085  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1922449  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1922709  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1923257  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1923568  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1924121  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1924427  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1925916  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1926348  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1926612  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1926953  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1928778  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1929265  0.0  0.0      0     0 ?        Z    Jun15   0:00 [node] <defunct>
root     1930169  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1930661  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1930945  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1931281  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1931553  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1932495  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1932774  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1933503  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1933750  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1934014  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1934284  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1934997  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1935273  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1935764  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1936125  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1936391  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1936698  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1937100  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1937385  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1938407  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1939551  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1939886  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1940576  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1940873  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1941197  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1941575  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1941902  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1942294  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1942576  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1943572  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1943930  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1944239  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1944845  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1945597  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1946996  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1947383  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1947676  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1947976  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1948253  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1948958  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1949373  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1949781  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1950085  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1950440  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1951021  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1951321  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1951610  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1952358  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1953102  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1953395  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1953688  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1954447  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1955090  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1955450  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1955794  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1956079  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1956922  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1957255  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1957559  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1958441  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1958705  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1958977  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1959285  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1959634  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1960171  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1960462  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1960786  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1961197  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1963199  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1963480  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1963800  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1964470  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1965752  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1965993  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1966300  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1966546  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1966813  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1967371  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1967690  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1968093  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1968472  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1969141  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1969461  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1970079  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1970672  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1971046  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1971474  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1971839  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1972280  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1972586  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1972966  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1973196  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1973552  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1973855  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1974141  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1974384  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1974681  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1975415  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1975782  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1977051  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1977357  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1977629  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1977941  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1978232  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1978583  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1979261  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1979589  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1980758  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1981091  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1981349  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1981624  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1981956  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1982207  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1982529  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1983551  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1984645  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1984923  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1985243  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1985503  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1985824  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1986136  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1986446  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1986938  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1987295  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1987622  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1988063  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1988417  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1989482  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1989789  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1990519  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     1990914  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1991257  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1991611  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1992202  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1992526  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1992797  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1993095  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1994913  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1995606  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1996231  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1996525  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1996774  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1997081  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1997365  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1997844  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1998189  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1998533  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     1998929  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     1999796  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2000068  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2000354  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2000668  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2000909  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2001281  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2001933  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2002246  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2003383  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2003705  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2003983  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2005469  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2005820  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2006578  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2006850  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2007470  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2007781  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2008402  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2009191  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2010322  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2010646  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2010984  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2011308  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2013336  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2014392  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2014712  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2015000  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2015552  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2015828  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2016198  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2016917  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2017342  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2018099  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2018394  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2018863  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2019515  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2021023  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2021756  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2022375  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2022658  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2023423  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2024065  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2024463  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2025203  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2025488  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2025749  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2026040  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2026404  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2026693  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2027111  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2027465  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2029316  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2029927  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2030239  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2031620  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2033443  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2034175  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2034439  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2035935  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2036989  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2037386  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2037660  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2037988  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2039879  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2040253  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2040597  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2040875  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2041636  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2042068  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2042402  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2043106  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2043453  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2044158  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2044525  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2044804  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2045158  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2045488  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2045810  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2046603  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2046883  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2047158  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2047455  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2047800  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2048143  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2048514  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2048894  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2049241  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2050421  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2051081  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2051408  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2051638  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2054891  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2055461  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2057730  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2058431  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2059118  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2059562  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2060331  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2061072  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2061588  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2061855  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2062096  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2062337  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2062797  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2063169  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2063427  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2064216  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2065629  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2066031  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2067056  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2067403  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2067816  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2068100  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2068435  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2068769  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2069084  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2069304  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2069605  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2070302  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2070701  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2071041  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2071406  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2072014  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2072306  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2072645  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2072976  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2073321  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2073718  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2074115  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2074504  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2074776  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2075204  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2075559  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2075882  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2076687  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2076981  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2077314  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2077658  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2078049  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2078369  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2078641  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2079685  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2079982  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2080299  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2080979  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2081412  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2081647  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2082684  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2083065  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2083415  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2084056  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2084965  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2085809  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2086814  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2087096  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2087696  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2088223  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2088519  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2088945  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2089288  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2090196  0.0  0.0      0     0 ?        Z    Jun15   0:00 [node] <defunct>
root     2090595  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2091235  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2091845  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2092177  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2092468  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2092803  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2093224  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2095205  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2095505  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2095783  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2097197  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2098218  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2098926  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2099276  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2100062  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2100429  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2100795  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2101154  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2101436  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2102052  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2102372  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2102610  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2103288  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2104477  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2104903  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2105153  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2105424  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2105744  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2105803  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2106117  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2106118  0.0  0.0      0     0 ?        Z    Jun15   0:00 [node] <defunct>
root     2106825  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2108007  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2109310  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2109976  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2110324  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2110734  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2111138  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2111572  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2112168  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2112436  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2112703  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2112999  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2113365  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2113739  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2114016  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2114357  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2114726  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2115502  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2115779  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2116315  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2116633  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2118788  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2119079  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2119374  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2119698  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2120020  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2120655  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2120934  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2121228  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2122391  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2122992  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2123280  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2123970  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2124563  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2124848  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2125133  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2125506  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2126261  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2126638  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2127291  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2127521  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2127900  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2129936  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2130303  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2130609  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2130881  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2131152  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2131757  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2132502  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2133933  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2134285  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2134540  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2134819  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2135055  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2135435  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2135731  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2136116  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2136560  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2136854  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2137132  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2137734  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2138066  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2138842  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2139235  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2139491  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2139812  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2140288  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2140652  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2140965  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2141285  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2141637  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2141939  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2142596  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2143279  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2143577  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2144398  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2144693  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2145068  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2145358  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2145641  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2145964  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2146350  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2146733  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2147049  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2148466  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2149115  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2149352  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2149650  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2150017  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2151010  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2151288  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2151701  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2152301  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2152569  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2152884  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2153183  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2153429  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2153687  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2154025  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2154373  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2154697  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2156061  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2156359  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2156682  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2157605  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2157862  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2158613  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2158969  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2159304  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2159597  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2159978  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2160273  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2160614  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2161244  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2161525  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2161909  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2162158  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2163727  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2164088  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2164352  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2164759  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2165591  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2167070  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2167402  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2167684  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2168257  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2168529  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2168872  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2169183  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2169582  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2170661  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2170990  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2171261  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2171534  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2171846  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2172176  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2172512  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2172885  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2173206  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2174609  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2175206  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2175482  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2175819  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2176159  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2176550  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2178153  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2178470  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2178761  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2179066  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2179884  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2180622  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2181355  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2181652  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2181915  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2182203  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2182470  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2182787  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2183134  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2183857  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2184913  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2185229  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2185560  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2185830  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2186142  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2186442  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2187141  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2187524  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2188609  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2188912  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2189155  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2189476  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2189734  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2190072  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2190682  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2191966  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2192148  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2192478  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2192756  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2193371  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2193981  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2194327  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2194707  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2195022  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2196024  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2196368  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2198002  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2199205  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2199883  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2200450  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2200748  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2201143  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2201463  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2201900  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2202925  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2202926  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2203292  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2203591  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2203854  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2204511  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2204798  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2205193  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2205521  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2206673  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2207032  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2207367  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2207694  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2208546  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2208905  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2209224  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2210607  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2210861  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2211154  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2211482  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2211785  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2212128  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2212455  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2212745  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2214163  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2214527  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2214898  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2215225  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2215660  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2216015  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2216728  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2218025  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2218369  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2219352  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2219758  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2221469  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2221762  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2222118  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2222445  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2223061  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2223398  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2223736  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2224595  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2224978  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2225348  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2225665  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2225974  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2227242  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2228654  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2229510  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2230345  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2230613  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2231357  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2231774  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2232153  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2232346  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2232860  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2233106  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2233396  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2234780  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2235546  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2235812  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2236171  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2236514  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2237210  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2237544  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2238892  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2239257  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2239529  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2240453  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2240780  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2240836  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2241475  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2241756  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2242459  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2242823  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2243110  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2243377  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2243605  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2243959  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2244252  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2244624  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2245092  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2245377  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2246066  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2246364  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2246986  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2247291  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2247806  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2248120  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2248427  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2249134  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2249690  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2250272  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2250904  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2251185  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2251914  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2252328  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2253413  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2254031  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2254597  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2254878  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2255119  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2255537  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2256589  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2257023  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2257314  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2257605  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2258013  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2258321  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2258614  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2258944  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2259308  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2259761  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2260119  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2260456  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2260722  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2261016  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2261338  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2261694  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2263262  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2263675  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2264660  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2265445  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2266171  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2266475  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2266864  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2267829  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2268145  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2268477  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2268788  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2269063  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2269369  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2269746  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2270151  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2270892  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2271268  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2271866  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2272148  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2272462  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2272819  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2273126  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2273592  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2274351  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2274665  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2274940  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2275247  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2275573  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2275933  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2276222  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2276824  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2277200  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2278290  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2278568  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2278886  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2279263  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2279555  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2280755  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2281159  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2281549  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2281843  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2282182  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2282453  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2283104  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2283405  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2285859  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2285909  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2286160  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2286467  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2286754  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2287009  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2287328  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2287984  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2288251  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2289299  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2289853  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2290121  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2290397  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2291064  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2292902  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2293516  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2294196  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2294581  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2294979  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2295639  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2296090  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2296416  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2297041  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2297353  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2297986  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2298724  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2299872  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2300273  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2300616  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2301234  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2301615  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2301906  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2302433  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2302729  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2302968  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2303343  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2303682  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2303927  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2304195  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2304479  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2305373  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2305673  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2305945  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2307232  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2307517  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2307783  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2308729  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2311367  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2312378  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2312658  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2313763  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2315453  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2316032  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2316864  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2317287  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2317604  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2317903  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2318205  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2318570  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2318899  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2319194  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2319539  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2319849  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2320284  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2320644  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2320963  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2321199  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2321795  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2322053  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2322378  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2324063  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2324342  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2324792  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2325083  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2325380  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2326556  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2326887  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2327178  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2328269  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2328607  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2328853  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2329109  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2330182  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2330608  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2331600  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2331875  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2332171  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2332441  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2332718  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2333445  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2334137  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2334839  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2335108  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2335394  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2335933  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2337688  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2338127  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2339646  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2341014  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2342764  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2343101  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2343652  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2344838  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2346306  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2346527  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2346881  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2348404  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2348689  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2349826  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2350796  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2351204  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2351547  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2352707  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2352957  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2353323  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2353620  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2354047  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2354701  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2355076  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2355425  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2355737  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2356024  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2356643  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2356963  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2357361  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2359166  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2359394  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2359697  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2360362  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2360726  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2361465  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2362119  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2363009  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2363271  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2363926  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2364270  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2365530  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2365912  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2366182  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2367635  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2369401  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2371502  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2372381  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2372673  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2373031  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2373336  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2373607  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2373973  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2374294  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2374672  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2376080  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2376407  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2376734  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2377050  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2377442  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2378139  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2378498  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2378774  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2379199  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2379447  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2379778  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2380500  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2380788  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2381088  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2381403  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2381749  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2383239  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2383568  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2383899  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2384312  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2384835  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2385314  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2386463  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2386778  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2387134  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2387556  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2387849  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2388317  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2388666  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2390364  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2390613  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2392358  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2393144  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2393405  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2393688  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2394008  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2394333  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2394654  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2395741  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2396722  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2397768  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2398105  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2398360  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2398666  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2399402  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2400169  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2400825  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2401111  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2401420  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2401793  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2402478  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2402747  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2404308  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2404577  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2404879  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2405162  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2405518  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2405841  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2406195  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2406890  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2407236  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2408047  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2408326  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2408622  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2409279  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2410354  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2411079  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2411343  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2412261  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2412544  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2412805  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2413080  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2413455  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2414165  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2414566  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2415205  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2415477  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2415746  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2416287  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2416704  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2416990  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2417417  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2417820  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2418596  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2418990  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2419292  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2419556  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2419881  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2420162  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2420575  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2421041  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2421998  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2422395  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2422766  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2423108  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2423495  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2424428  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2425861  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2426247  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2426554  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2426836  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2427203  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2428975  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2429802  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2430152  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2430510  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2430855  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2431477  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2431866  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2432237  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2432678  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2433750  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2434011  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2434306  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2434614  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2434895  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2435592  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2436352  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2436733  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2437043  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2437333  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2437649  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2437948  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2438772  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2439195  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2439628  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2440281  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2440561  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2440857  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2441441  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2441733  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2442040  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2443535  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2443937  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2444254  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2444553  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2444815  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2445050  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2445367  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2445701  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2446177  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2447032  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2447350  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2447709  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2448021  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2448336  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2448744  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2449126  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2449539  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2449908  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2450323  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2450932  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2451298  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2451598  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2451883  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2452919  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2453482  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2454181  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2454462  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2454781  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2455386  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2455673  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2455982  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2456721  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2457076  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2457425  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2457743  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2458001  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2458316  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2458655  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2458908  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2459578  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2459948  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2460289  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2460666  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2461479  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2461830  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2462162  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2462774  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2463140  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2463502  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2464299  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2465032  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2465377  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2465688  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2465974  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2466290  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2466608  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2467250  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2467603  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2468763  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2469083  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2469623  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2469723  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2470398  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2471225  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2471443  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2472560  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2472839  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2473089  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2474149  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2474702  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2475063  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2475387  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2475694  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2476005  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2476323  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2476924  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2478013  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2479999  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2480276  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2480708  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2481101  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2481804  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2482879  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2483160  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2483431  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2483753  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2484058  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2484865  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2485239  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2485525  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2485857  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2486441  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2486787  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2487073  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2488189  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2488506  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2489096  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2489765  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2490161  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2490531  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2491587  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2492206  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2492860  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2493630  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2493934  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2494280  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2494620  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2495030  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2496723  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2498996  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2499397  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2499672  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2500115  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2502039  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2502368  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2502613  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2502942  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2503206  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2503638  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2504345  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2505565  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2505932  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2506274  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2506579  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2506912  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2507302  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2507705  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2508091  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2508369  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2508766  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2509141  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2509385  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2509971  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2510257  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2510593  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2511217  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2511689  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2512027  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2513366  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2513680  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2513938  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2514481  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2517075  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2518990  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2520452  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2521102  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2521450  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2523334  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2523938  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2524230  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2524550  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2524951  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2525980  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2526344  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2526721  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2527303  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2529540  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2529934  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2530571  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2531286  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2531760  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2531991  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2533107  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2533479  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2534035  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2534295  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2534647  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2534998  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2535678  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2536416  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2536829  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2537134  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2537470  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2537689  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2538685  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2539017  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2539922  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2540314  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2540637  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2540943  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2541230  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2541536  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2541860  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2542159  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2542633  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2543768  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2544074  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2544750  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2546678  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2547487  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2547798  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2548131  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2548453  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2548758  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2549522  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2549929  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2551126  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2551370  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2551735  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2552202  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2552525  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2552850  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2553230  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2553529  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2554239  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2554656  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2555318  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2555577  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2556202  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2556615  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2556945  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2558213  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2558507  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2559458  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2560526  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2561641  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2561971  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2562278  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2562634  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2562957  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2563755  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2564031  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2564372  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2565460  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2565829  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2566115  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2566458  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2566710  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2567362  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2570335  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2571757  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2571996  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2572798  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2573085  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2573455  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2573780  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2575267  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2575608  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2575995  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2576245  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2576552  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2576878  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2577232  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2577531  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2577869  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2578655  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2579009  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2579329  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2579934  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2580224  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2580498  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2580803  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2581276  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2582662  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2582978  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2583307  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2583610  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2583949  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2584291  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2584714  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2585065  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2586519  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2586799  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2587433  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2588032  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2590701  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2591461  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2591858  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2592524  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2592792  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2593063  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2593701  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2594260  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2594708  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2594986  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2595306  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2595618  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2596035  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2596370  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2596678  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2597415  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2599159  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2599404  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2599724  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2602747  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2603634  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2603919  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2604216  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2604769  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2605070  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2605397  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2605795  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2606731  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2607001  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2607250  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2607562  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2608453  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2608894  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2609208  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2609536  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2612692  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2613375  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2613703  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2614396  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2615297  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2615559  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2616206  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2616812  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2617140  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2617398  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2617690  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2618014  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2618326  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2618629  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2618966  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2619220  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2619554  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2619845  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2620157  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2620768  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2621076  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2621387  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2621720  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2622068  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2622978  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2623230  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2623504  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2623814  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2624125  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2624426  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2624747  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2625814  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2626103  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2626426  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2626723  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2627042  0.0  0.0      0     0 ?        Z    Jun15   0:01 [node] <defunct>
root     2627369  0.0  0.0      0     0 ?        Z    Jun15   0:04 [node] <defunct>
root     2628731  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2629132  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2629474  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2629731  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2630049  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2630383  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2630738  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2631014  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2631553  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2631868  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2632171  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2632823  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2633112  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2633427  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2633736  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2634030  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2634317  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2634699  0.0  0.0      0     0 ?        Z    Jun15   0:02 [node] <defunct>
root     2635006  0.0  0.0      0     0 ?        Z    Jun15   0:03 [node] <defunct>
root     2635233  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2635909  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2636278  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2636547  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2636871  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2637172  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2637498  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2637848  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2638194  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2638576  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2639237  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2639547  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2640213  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2640861  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2641228  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2641539  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2642320  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2642658  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2643585  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2643889  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2644164  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2644808  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2645061  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2645359  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2645689  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2645947  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2646519  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2646896  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2647223  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2647524  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2647839  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2648193  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2648478  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2648778  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2649073  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2649373  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2649959  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2650354  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2650758  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2651053  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2651674  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2651951  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2652201  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2652288  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2652605  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2652676  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2654329  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2654606  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2654936  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2655236  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2655583  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2655916  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2656922  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2657183  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2657459  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2657771  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2658029  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2658311  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2658666  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2658959  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2659217  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2659530  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2659836  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2660200  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2660476  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2660742  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2661354  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2661685  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2662672  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2662955  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2663629  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2663984  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2664315  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2665897  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2666139  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2666469  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2666771  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2667308  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2667958  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2668266  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2668567  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2668910  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2669213  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2669459  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2670061  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2671017  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2671421  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2671755  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2672049  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2672317  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2672713  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2672808  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2673392  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2673983  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2674302  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2674910  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2675185  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2675830  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2676526  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2676957  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2677532  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2678103  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2678418  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2679055  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2679449  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2679814  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2680789  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2681071  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2682828  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2683748  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2684007  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2685381  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2685649  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2685946  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2686209  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2686780  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2687099  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2687380  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2687672  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2687929  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2688144  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2688460  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2689022  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2689358  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2689919  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2690518  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2690866  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2691157  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2691452  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2691783  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2692378  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2692987  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2693257  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2693537  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2693809  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2694458  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2695390  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2695685  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2697063  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2697353  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2698382  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2698691  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2699061  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2700076  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2700418  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2700700  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2701012  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2701387  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2701693  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2701976  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2702215  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2703139  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2703446  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2703758  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2704019  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2704576  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2704884  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2705809  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2706080  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2706426  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2707008  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2707382  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2707659  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2707952  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2708220  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2708510  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2709252  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2709975  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2710246  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2711356  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2712050  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2712404  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2712749  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2713103  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2713452  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2713809  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2714118  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2714776  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2715050  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2715373  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2715937  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2716534  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2716867  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2717148  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2717680  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2717993  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2718941  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2719954  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2720273  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2722652  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2723019  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2723241  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2723593  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2724196  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2725074  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2725367  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2725638  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2725972  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2726240  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2726845  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2727189  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2727482  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2727803  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2728795  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2729082  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2729417  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2729725  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2730071  0.0  0.0      0     0 ?        Z    Jun16   0:04 [node] <defunct>
root     2730366  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2731086  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2731384  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2731644  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2732423  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2733725  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2734030  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2734356  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2735178  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2735490  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2735777  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2736037  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2736589  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2736915  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2737260  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2737861  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2738427  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2738699  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2738964  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2739279  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2739556  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2739875  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2740195  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2741073  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2741400  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2741716  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2742008  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2742316  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2742696  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2743027  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2743663  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2743978  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2744295  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2744603  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2744911  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2745194  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2745395  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2745750  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2746098  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2746305  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2746592  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2746893  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2747524  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2747798  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2748163  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2748798  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2749115  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2749801  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2750128  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2750398  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2750714  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2751023  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2751347  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2752008  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2752094  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2752311  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2752514  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2752638  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2753231  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2753614  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2753977  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2754286  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2754523  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2754857  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2755163  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2755470  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2755765  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2756130  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2756428  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2756715  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2757067  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2757426  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2757689  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2757998  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2758357  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2758637  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2759231  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2759458  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2760057  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2760424  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2761083  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2761484  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2761746  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2762094  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2762422  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2762726  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2763006  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2763271  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2763851  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2764500  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2764808  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2765757  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2765978  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2766308  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2766575  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2766880  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2767148  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2767373  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2767781  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2768050  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2768292  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2768586  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2768883  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2769149  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2769467  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2769751  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2770128  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2770443  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2771003  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2771294  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2771538  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2771834  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2772091  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2772780  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2773321  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2773590  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2774214  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2775010  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2775268  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2775646  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2776185  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2776452  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2776980  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2777310  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2778465  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2778812  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2779089  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2779407  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2780055  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2780315  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2780616  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2780936  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2781231  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2781550  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2781871  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2782466  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2782773  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2783461  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2783837  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2785167  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2785449  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2786092  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2786445  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2786977  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2787248  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2788127  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2788355  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2789289  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2789472  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2789797  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2790112  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2791086  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2791372  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2791661  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2792292  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2792642  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2792912  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2793270  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2793592  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2793845  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2794503  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2795013  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2795301  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2796271  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2796555  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2796816  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2797144  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2797460  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2797699  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2797902  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2798246  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2798491  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2798816  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2799091  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2799480  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2800054  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2800325  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2800608  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2801356  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2801751  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2802073  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2802435  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2802805  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2803371  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2803670  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2803939  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2804235  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2804576  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2805609  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2805960  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2806193  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2806468  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2807042  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2807390  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2807927  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2808488  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2808801  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2809125  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2809416  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2809738  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2809979  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2810241  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2810662  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2811022  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2811678  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2811904  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2812618  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2812836  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2813145  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2813466  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2814342  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2814624  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2814986  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2816077  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2816370  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2816740  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2817319  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2817604  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2817929  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2818265  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2818497  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2819074  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2819437  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2819779  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2820072  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2820427  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2820683  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2820943  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2821243  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2821835  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2822130  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2822419  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2822688  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2823005  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2823387  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2823701  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2824036  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2824339  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2825017  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2825268  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2825781  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2826112  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2826757  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2827537  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2827657  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2828181  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2829182  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2829476  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2829721  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2830032  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2830379  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2830749  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2831063  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2831689  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2831980  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2832281  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2832897  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2833198  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2833522  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2834176  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2834435  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2834781  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2835106  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2835343  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2835698  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2835964  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2836305  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2836595  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2836907  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2837193  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2837833  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2838097  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2838423  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2838770  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2839334  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2840023  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2840359  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2840634  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2840939  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2841223  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2841563  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2842271  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2842592  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2842943  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2843317  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2843913  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2844264  0.0  0.0      0     0 ?        Z    Jun16   0:04 [node] <defunct>
root     2844601  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2845224  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2845735  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2846080  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2846420  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2846692  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2847033  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2848264  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2848633  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2848943  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2849239  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2849612  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2849893  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2850210  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2850467  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2850773  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2851411  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2851707  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2852032  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2852409  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2853015  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2853226  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2853542  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2854576  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2854866  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2855182  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2855965  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2856194  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2856531  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2856839  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2857085  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2857428  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2857723  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2858077  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2859065  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2859931  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2860271  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2860890  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2861160  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2861436  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2861749  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2862052  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2862325  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2862653  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2863211  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2863521  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2864121  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2865133  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2866559  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2866867  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2867162  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2867485  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2867799  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2868079  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2868321  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2868611  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2869415  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2869687  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2870339  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2870599  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2870895  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2871206  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2871520  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2872199  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2872741  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2873007  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2873292  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2873557  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2873878  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2874170  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2874477  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2874750  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2875434  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2875742  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2876099  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2876736  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2877101  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2877314  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2877575  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2877955  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2878256  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2878557  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2878889  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2879264  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2879592  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2880251  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2880566  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2880816  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2881125  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2881391  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2881930  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2882564  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2882930  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2884153  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2885095  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2885632  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2885949  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2886889  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2887210  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2887554  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2888192  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2888520  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2888769  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2889014  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2889643  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2890038  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2890321  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2891623  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2891948  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2892275  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2892927  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2893476  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2893762  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2894194  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2894447  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2894723  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2895590  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2895876  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2896477  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2896822  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2897133  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2897439  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2898175  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2898455  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2898792  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2899222  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2899526  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2899829  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2900127  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2900750  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2902077  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2902377  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2902821  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2903217  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2903594  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2903853  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2905479  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2906124  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2906441  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2906699  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2906958  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2907037  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2907268  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2907392  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2907538  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2907806  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2908162  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2908905  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2909238  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2909624  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2909915  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2910251  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2910478  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2910795  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2911040  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2911347  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2911943  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2912233  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2912515  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2912890  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2913283  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2913517  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2913791  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2914450  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2914802  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2915107  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2915437  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2916054  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2916311  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2916630  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2916863  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2917204  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2917599  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2917889  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2918128  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2918456  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2919019  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2919347  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2919672  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2920250  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2920893  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2921542  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2921814  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2922116  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2922450  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2923269  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2923625  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2924519  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2925165  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2925420  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2925679  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2926043  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2926338  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2926633  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2927260  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2927584  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2928147  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2928446  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2928747  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2929070  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2929352  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2929614  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2929923  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2930230  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2930515  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2931103  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2931447  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2931753  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2931975  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2932293  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2932862  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2933272  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2933611  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2933935  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2934181  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2934982  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2935970  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2936269  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2937222  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2937489  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2937801  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2938475  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2938729  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2939033  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2939329  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2939914  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2940154  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2940383  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2940665  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2940930  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2941281  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2941570  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2941966  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2942325  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2942619  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2942961  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2943259  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2943634  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2943974  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2944890  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2945179  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2945495  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2946173  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2946500  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2946843  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2947445  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2948031  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2948296  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2948615  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2949511  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2950202  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2950500  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2950818  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2951120  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2951380  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2951675  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2952295  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2952651  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2952984  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2953694  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2954018  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2954279  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2954925  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2955562  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2955823  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2956742  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2956982  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2957301  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2957600  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2957965  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2958267  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2958576  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2958833  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2959127  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2960071  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2960301  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2960585  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2960911  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2961498  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2961840  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2962712  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2963034  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2964039  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2964653  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2965527  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2965818  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2966135  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2966900  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2967210  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2967609  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2967978  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2968245  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2968945  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2969312  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2969983  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2970322  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2970682  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2970991  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2971327  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2971645  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2971994  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2972315  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2972639  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2972918  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2973186  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2973476  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2973924  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2974265  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2974554  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2975267  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2975540  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2975933  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2976510  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2976805  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2977130  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2977773  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2978426  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2979058  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2979317  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2979709  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2981768  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2983483  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2983858  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2984955  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2985608  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2985904  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2986181  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2986564  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2986798  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2987105  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2987378  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2987775  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2988117  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2988185  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2988418  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2988512  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2988986  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2989295  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2989603  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2989901  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2990549  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2991609  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2991931  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2992597  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2992893  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     2993480  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2993788  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2994060  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2994320  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2994608  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2994954  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2995533  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2995763  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2996056  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2996291  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     2996672  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2996956  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2997211  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2997477  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2997793  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2998351  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2998634  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2998953  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2999572  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     2999856  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3000150  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3000435  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3001985  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3002247  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3002560  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3003262  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3003533  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3004507  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3004865  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3005158  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3005433  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3005718  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3005978  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3006867  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3007163  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3007505  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3008364  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3008631  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3008904  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3009248  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3009507  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3010277  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3010537  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3011095  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3011376  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3011696  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3012658  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3012920  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3013198  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3013451  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3013839  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3014128  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3014417  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3014989  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3015854  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3016400  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3016664  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3016946  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3017248  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3017516  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3018129  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3019800  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3020197  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3021846  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3022135  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3023087  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3023307  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3025030  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3025988  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3026306  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3026682  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3027979  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3028545  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3029945  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3030261  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3030876  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3031171  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3031499  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3031851  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3033218  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3034637  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3035224  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3036369  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3036978  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3038661  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3039610  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3040956  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3041256  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3041486  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3041843  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3042750  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3043062  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3043987  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3044224  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3044576  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3044959  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3045512  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3045771  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3046105  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3046785  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3047148  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3047426  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3048140  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3048430  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3048669  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3048977  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3049223  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3049476  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3050043  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3050371  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3050665  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3051286  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3051596  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3051973  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3052323  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3052574  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3052932  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3053216  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3053538  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3053882  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3055138  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3055416  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3055745  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3056056  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3056290  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3056586  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3056974  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3057519  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3057758  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3058093  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3058343  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3058607  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3059232  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3059460  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3059778  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3060114  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3060441  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3061012  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3061345  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3061634  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3062391  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3062730  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3062958  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3063292  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3063636  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3063940  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3064580  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3064859  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3065258  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3066156  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3066428  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3067695  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3068335  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3068598  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3068960  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3069577  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3069917  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3070750  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3071039  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3071634  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3071917  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3072181  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3072454  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3072815  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3073125  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3073771  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3073956  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3074519  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3074813  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3075840  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3076187  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3076494  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3076801  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3077192  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3077577  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3078180  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3078448  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3078780  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3079346  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3079629  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3079965  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3080229  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3081521  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3082131  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3083301  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3083630  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3084577  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3085078  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3086035  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3086326  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3086975  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3087512  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3087767  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3088098  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3088415  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3088729  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3089013  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3089382  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3089967  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3090202  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3090504  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3090839  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3091103  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3091719  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3092016  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3092266  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3093097  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3093724  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3094043  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3094390  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3094809  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3095084  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3095339  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3095668  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3096038  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3096326  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3096602  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3096897  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3097199  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3097485  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3097761  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3098067  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3098347  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3098965  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3099256  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3099641  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3099986  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3100322  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3100663  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3101461  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3101829  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3102420  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3103001  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3103356  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3103676  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3103938  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3104652  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3104868  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3105494  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3105748  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3106092  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3106450  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3107041  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3107677  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3107935  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3108622  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3108970  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3109563  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3111557  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3111851  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3112544  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3112898  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3113251  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3113597  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3113960  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3114217  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3114470  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3114751  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3115052  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3115397  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3115744  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3116056  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3116072  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3116434  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3116572  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3116812  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3116863  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3117479  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3117755  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3118685  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3119051  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3119342  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3119713  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3120008  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3120346  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3120662  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3121015  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3121886  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3122154  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3123464  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3123787  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3124429  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3124715  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3125066  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3125290  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3125867  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3126182  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3126414  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3128143  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3128373  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3128652  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3129216  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3129808  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3130185  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3130447  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3131003  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3131282  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3131990  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3132567  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3132869  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3133127  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3133651  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3133941  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3134497  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3134775  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3136055  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3136672  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3136933  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3137229  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3137561  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3137855  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3138161  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3138481  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3139375  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3139748  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3140392  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3140997  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3141290  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3141584  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3141844  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3142160  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3142565  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3142836  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3143109  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3143367  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3143908  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3144143  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3144520  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3144815  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3145467  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3145674  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3145990  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3146250  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3146559  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3146814  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3147089  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3147411  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3148098  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3148376  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3148706  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3149343  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3149642  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3149896  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3150155  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3151118  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3151743  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3152007  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3152284  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3152593  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3152816  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3153171  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3153802  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3154198  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3154498  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3155437  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3155714  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3156715  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3157040  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3157579  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3157850  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3158153  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3158469  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3158779  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3159088  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3160341  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3160577  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3160969  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3161342  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3161616  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3161899  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3162274  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3162568  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3162840  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3163090  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3163706  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3163998  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3164620  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3164915  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3165232  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3165568  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3165902  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3166235  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3166551  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3166900  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3167876  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3168214  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3168576  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3168820  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3169153  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3169526  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3169827  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3170109  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3170406  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3170770  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3171744  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3172387  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3172753  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3173083  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3173503  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3174174  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3174742  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3175000  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3175328  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3175599  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3176206  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3176543  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3176778  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3177066  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3177332  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3177958  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3178549  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3178923  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3179871  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3180160  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3180439  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3180729  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3181028  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3181390  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3182341  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3183042  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3183287  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3184203  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3184545  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3184861  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3185198  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3185494  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3185856  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3186176  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3186776  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3187086  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3187384  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3187830  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3188406  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3189016  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3189332  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3189645  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3189931  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3190842  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3191538  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3191807  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3192409  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3192660  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3192907  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3193190  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3193468  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3193724  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3194151  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3194413  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3195153  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3195473  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3196089  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3196755  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3197408  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3197696  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3198000  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3199868  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3200488  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3201539  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3202774  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3203098  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3203486  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3203814  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3204152  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3205461  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3205790  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3206115  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3206444  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3206710  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3207392  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3207686  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3208590  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3208860  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3209443  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3210010  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3210563  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3210790  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3211108  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3212570  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3212818  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3213089  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3213335  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3213625  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3213891  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3214144  0.0  0.0      0     0 ?        Z    Jun16   0:04 [node] <defunct>
root     3214464  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3214691  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3214985  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3215296  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3215569  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3215906  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3216169  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3216492  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3216777  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3218065  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3218352  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3218704  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3218982  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3219324  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3220729  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3220998  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3221240  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3221572  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3222199  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3222509  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3224284  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3224605  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3225662  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3226255  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3226829  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3227164  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3227444  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3227795  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3228086  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3228446  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3228744  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3229086  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3229410  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3229692  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3229958  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3230248  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3230484  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3230838  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3231530  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3231876  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3232533  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3232789  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3233091  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3233758  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3234086  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3234377  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3234675  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3234961  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3235302  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3235893  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3236303  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3236588  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3236861  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3237138  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3237430  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3238010  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3238305  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3238604  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3238863  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3239550  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3239805  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3240106  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3240760  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3241022  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3241297  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3241606  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3242260  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3242635  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3243291  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3243625  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3243905  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3244293  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3245323  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3245624  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3246332  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3246616  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3246944  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3247266  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3247634  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3247934  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3248304  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3248591  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3249560  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3249946  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3250865  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3251226  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3251538  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3252169  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3252528  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3253193  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3253798  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3254081  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3254350  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3254597  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3254863  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3255210  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3255775  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3256431  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3256822  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3257191  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3257466  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3257765  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3258008  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3258624  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3259569  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3259942  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3260220  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3260573  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3262425  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3262798  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3263112  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3263399  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3263703  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3264000  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3264434  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3265119  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3266261  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3266595  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3267160  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3267496  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3268181  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3268770  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3269040  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3269391  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3270570  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3270943  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3271677  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3271948  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3272544  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3272831  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3273143  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3273806  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3274146  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3274405  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3274736  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3275419  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3275714  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3276017  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3276352  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3276624  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3276955  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3277632  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3277889  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3278172  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3278456  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3278797  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3279082  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3279363  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3279684  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3279995  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3280318  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3280646  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3281217  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3282614  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3282970  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3283709  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3283992  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3284277  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3284569  0.0  0.0      0     0 ?        Z    Jun16   0:04 [node] <defunct>
root     3284882  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3285617  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3285957  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3286640  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3287470  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3287781  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3288184  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3289135  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3289743  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3290331  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3290671  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3290965  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3291381  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3291663  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3292261  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3292587  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3292892  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3293176  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3293489  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3293745  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3294335  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3294624  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3295556  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3295810  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3296142  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3296429  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3297327  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3297951  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3298256  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3299107  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3299676  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3300391  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3300609  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3300898  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3301238  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3301513  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3301870  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3302145  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3302519  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3303138  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3303792  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3304127  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3304385  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3304960  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3305284  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3305592  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3306180  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3306464  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3306804  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3307109  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3307661  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3308322  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3308677  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3308910  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3309260  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3309449  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3309999  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3310321  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3310558  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3310880  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3311530  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3311992  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3312284  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3313299  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3313626  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3313935  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3314262  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3314622  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3314854  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3315172  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3315460  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3316433  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3316801  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3317158  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3318034  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3318374  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3319017  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3319356  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3319631  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3320000  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3320310  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3321049  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3321366  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3321639  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3321907  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3322184  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3322428  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3322747  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3323011  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3323297  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3324003  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3324280  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3324590  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3324874  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3325444  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3325645  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3325918  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3326980  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3327370  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3328024  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3328704  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3330020  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3331710  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3332662  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3332926  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3333213  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3333466  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3333742  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3334102  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3334516  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3334818  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3335101  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3335497  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3335847  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3336162  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3336851  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3337161  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3337426  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3338213  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3338471  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3338785  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3339158  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3339485  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3340060  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3340381  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3340965  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3341323  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3341617  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3342273  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3342580  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3342813  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3343131  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3343535  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3343833  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3344098  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3344414  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3345030  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3345397  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3345986  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3346257  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3346557  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3346917  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3347029  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3347219  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3347477  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3347789  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3348495  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3348822  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3349167  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3350078  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3350370  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3350652  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3350961  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3351280  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3351656  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3352626  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3353334  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3353640  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3353969  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3354284  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3354636  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3354931  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3355202  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3355543  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3355804  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3356213  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3356542  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3356817  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3357512  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3358169  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3358511  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3358842  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3359181  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3359463  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3359854  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3360485  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3360752  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3361081  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3361386  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3361904  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3362169  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3362477  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3363117  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3363427  0.0  0.0      0     0 ?        Z    Jun16   0:04 [node] <defunct>
root     3363733  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3364025  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3364301  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3364598  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3365226  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3365507  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3365752  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3366071  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3366375  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3367004  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3368260  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3368512  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3368803  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3370487  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3372369  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3372771  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3373119  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3373460  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3373733  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3374116  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3374466  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3374776  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3375104  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3375451  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3375773  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3376108  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3377167  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3377461  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3377753  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3378041  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3378387  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3378725  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3379106  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3379407  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3380035  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3381030  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3382600  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3382885  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3383482  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3383760  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3384172  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3384428  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3384734  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3385312  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3385567  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3386266  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3387211  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3387831  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3388437  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3388760  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3389110  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3390499  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3390776  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3391092  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3391354  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3391731  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3392091  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3392380  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3393406  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3393683  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3394098  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3394677  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3394915  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3395222  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3395470  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3395741  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3396084  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3396391  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3396765  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3397136  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3397728  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3398272  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3398544  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3398885  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3399217  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3399460  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3400071  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3401008  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3401263  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3402021  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3402367  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3402649  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3403147  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3403407  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3403698  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3404314  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3404701  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3405010  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3405294  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3405552  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3405848  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3406224  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3406451  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3407372  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3407667  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3407954  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3408278  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3408890  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3410402  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3412262  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3412519  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3412846  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3413424  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3413734  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3414366  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3414632  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3415211  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3415492  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3416637  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3416943  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3417250  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3417542  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3418122  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3418436  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3418725  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3419006  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3419592  0.0  0.0      0     0 ?        Z    Jun16   0:04 [node] <defunct>
root     3419936  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3420226  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3420850  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3421741  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3422035  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3422322  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3422624  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3423226  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3423586  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3423891  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3424556  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3425216  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3426263  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3426549  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3426839  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3427105  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3427412  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3427770  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3428053  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3428420  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3428750  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3429394  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3429720  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3430070  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3430323  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3431176  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3431511  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3431765  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3432014  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3432333  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3432583  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3433201  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3433473  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3433762  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3434050  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3434419  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3434816  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3435383  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3435558  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3435610  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3436283  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3436578  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3437909  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3438576  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3438913  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3439238  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3439548  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3439875  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3440229  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3440477  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3440789  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3441030  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3441876  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3442145  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3442467  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3443120  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3443463  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3444098  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3444737  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3445122  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3445392  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3445609  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3445942  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3446557  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3446837  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3447432  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3447711  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3448025  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3448271  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3448632  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3448880  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3449528  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3449920  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3450281  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3450565  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3450838  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3451072  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3451643  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3451961  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3452243  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3452806  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3453092  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3454006  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3454332  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3455357  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3457149  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3457418  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3457725  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3458068  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3460437  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3461071  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3461352  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3462361  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3462662  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3462980  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3463350  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3463652  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3463929  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3464242  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3464607  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3464915  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3465239  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3465560  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3465884  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3466268  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3466598  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3466963  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3467298  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3467919  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3468600  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3468912  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3469619  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3469960  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3470327  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3471259  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3471578  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3472894  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3473150  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3473456  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3473776  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3474664  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3474995  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3475593  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3476658  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3477280  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3477587  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3478506  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3478770  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3479328  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3479640  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3479939  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3480274  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3480540  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3480911  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3481465  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3481756  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3482744  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3483685  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3483949  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3484904  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3485626  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3485997  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3486896  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3487210  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3487500  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3488091  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3488442  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3488780  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3489125  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3490059  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3490359  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3490972  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3491290  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3491527  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3491838  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3492517  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3492849  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3493174  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3493527  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3493850  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3494143  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3494484  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3494801  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3495403  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3495742  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3495983  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3496258  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3496572  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3496866  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3497120  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3497489  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3497833  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3498130  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3498505  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3498807  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3499129  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3499410  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3499779  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3500473  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3501119  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3501430  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3502025  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3502319  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3502622  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3502961  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3503236  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3503554  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3503867  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3504149  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3504467  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3504751  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3505779  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3506718  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3506966  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3507322  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3507593  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3507885  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3508146  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3508789  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3509092  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3509418  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3510075  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3510346  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3510682  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3510994  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3511300  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3511565  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3511871  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3512474  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3512887  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3513208  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3513490  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3514048  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3514177  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3514343  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3515311  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3515846  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3516145  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3516453  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3516721  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3517455  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3517769  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3518075  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3518827  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3519378  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3519795  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3520145  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3520681  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3521389  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3521807  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3522715  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3523412  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3523984  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3524541  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3524845  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3525172  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3525514  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3526418  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3526702  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3527312  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3527640  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3527915  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3528781  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3529352  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3529936  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3530530  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3530854  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3531116  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3531491  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3531837  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3532140  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3532493  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3533106  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3533374  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3533932  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3534247  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3534578  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3534868  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3535135  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3535483  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3536093  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3536618  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3536872  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3537186  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3538835  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3539180  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3539571  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3539900  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3541272  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3541612  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3542265  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3542543  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3542938  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3543521  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3544860  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3545144  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3545440  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3546180  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3546526  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3546850  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3547605  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3547876  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3548235  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3549558  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3549817  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3550188  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3550514  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3550866  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3551161  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3551476  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3551737  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3551992  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3552628  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3552912  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3553173  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3553755  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3554487  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3555436  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3555757  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3556668  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3556958  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3557174  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3557437  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3558115  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3558390  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3559025  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3559550  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3560530  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3561093  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3561354  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3562025  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3562356  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3562665  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3563015  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3563284  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3563561  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3563950  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3565287  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3565595  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3566166  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3566526  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3566738  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3566980  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3567819  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3568877  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3569181  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3569776  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3570048  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3570307  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3570628  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3571279  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3571599  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3571858  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3572243  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3572863  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3573224  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3573520  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3573813  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3574471  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3575219  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3576184  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3577046  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3578666  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3579018  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3579256  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3579666  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3579986  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3580332  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3580675  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3580994  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3581287  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3581944  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3582609  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3583474  0.0  0.0      0     0 ?        Z    Jun16   0:04 [node] <defunct>
root     3584830  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3585208  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3585484  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3586087  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3586383  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3586678  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3587290  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3587665  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3587939  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3588221  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3588903  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3589167  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3589535  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3590154  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3590292  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3590465  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3591276  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3591883  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3592418  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3593098  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3593503  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3593835  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3594152  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3594511  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3594828  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3595796  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3596080  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3596355  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3596674  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3597054  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3597341  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3597629  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3597975  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3598253  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3598535  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3598832  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3599150  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3599456  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3599763  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3600046  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3600766  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3601717  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3602313  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3602663  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3603001  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3603306  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3603657  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3603957  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3604316  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3604923  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3605285  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3605619  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3605964  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3606256  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3606571  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3606914  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3607196  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3607451  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3607760  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3608102  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3608384  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3609004  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3609377  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3609654  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3610561  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3610925  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3611228  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3611583  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3611917  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3612241  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3612553  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3613616  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3613945  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3614276  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3614600  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3614958  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3615194  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3615474  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3615885  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3616460  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3616816  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3617409  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3617735  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3618015  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3618932  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3619160  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3619837  0.0  0.0      0     0 ?        Z    Jun16   0:01 [node] <defunct>
root     3620132  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3620405  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3620724  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3621099  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3621394  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3621739  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3622385  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3622714  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3623002  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3623979  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3624303  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3624544  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3624806  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3625055  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3625697  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3626349  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3626657  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3627660  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3628295  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3628661  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3629012  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3629932  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3630518  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3630759  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3631029  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3631370  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3632065  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3632300  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3632642  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3632935  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3633291  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3633669  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3633995  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3634291  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3635009  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3635314  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3635603  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3635915  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3636231  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3636589  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3636905  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3637187  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3637477  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3637764  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3638297  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3638626  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3638956  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3639291  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3639665  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3639938  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3640491  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3641060  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3641339  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3641628  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3641952  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3642268  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3642668  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3643318  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3643588  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3643900  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3644183  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3644456  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3644735  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3645041  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3645374  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3646048  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3646320  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3646570  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3646867  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3647301  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3647922  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3648262  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3648527  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3648847  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3649133  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3649446  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3650419  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3650992  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3651298  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3651586  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3651890  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3652213  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3652486  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3652803  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3653067  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3653338  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3653619  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3653922  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3654258  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3654614  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3655269  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3655598  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3655970  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3656250  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3656551  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3657221  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3657573  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3657836  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3658170  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3658437  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3660149  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3660493  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3661431  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3661716  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3662069  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3662410  0.0  0.0      0     0 ?        Z    Jun16   0:02 [node] <defunct>
root     3662702  0.0  0.0      0     0 ?        Z    Jun16   0:03 [node] <defunct>
root     3663363  0.0  0.0      0     0 ?        Z    00:00   0:02 [node] <defunct>
root     3663686  0.0  0.0      0     0 ?        Z    00:01   0:02 [node] <defunct>
root     3664724  0.0  0.0      0     0 ?        Z    00:02   0:02 [node] <defunct>
root     3665019  0.0  0.0      0     0 ?        Z    00:03   0:02 [node] <defunct>
root     3665266  0.0  0.0      0     0 ?        Z    00:03   0:02 [node] <defunct>
root     3665521  0.0  0.0      0     0 ?        Z    00:04   0:02 [node] <defunct>
root     3665860  0.0  0.0      0     0 ?        Z    00:04   0:03 [node] <defunct>
root     3666241  0.0  0.0      0     0 ?        Z    00:05   0:03 [node] <defunct>
root     3666886  0.0  0.0      0     0 ?        Z    00:06   0:02 [node] <defunct>
root     3667073  0.0  0.0      0     0 ?        Z    00:06   0:01 [node] <defunct>
root     3667217  0.0  0.0      0     0 ?        Z    00:06   0:03 [node] <defunct>
root     3667468  0.0  0.0      0     0 ?        Z    00:07   0:00 [node] <defunct>
root     3667872  0.0  0.0      0     0 ?        Z    00:07   0:02 [node] <defunct>
root     3668859  0.0  0.0      0     0 ?        Z    00:09   0:02 [node] <defunct>
root     3670142  0.0  0.0      0     0 ?        Z    00:11   0:02 [node] <defunct>
root     3670476  0.0  0.0      0     0 ?        Z    00:12   0:02 [node] <defunct>
root     3671374  0.0  0.0      0     0 ?        Z    00:13   0:03 [node] <defunct>
root     3671971  0.0  0.0      0     0 ?        Z    00:14   0:02 [node] <defunct>
root     3672715  0.0  0.0      0     0 ?        Z    00:15   0:03 [node] <defunct>
root     3673041  0.0  0.0      0     0 ?        Z    00:16   0:02 [node] <defunct>
root     3673402  0.0  0.0      0     0 ?        Z    00:16   0:02 [node] <defunct>
root     3673682  0.0  0.0      0     0 ?        Z    00:17   0:02 [node] <defunct>
root     3675243  0.0  0.0      0     0 ?        Z    00:19   0:02 [node] <defunct>
root     3675533  0.0  0.0      0     0 ?        Z    00:19   0:01 [node] <defunct>
root     3675820  0.0  0.0      0     0 ?        Z    00:20   0:02 [node] <defunct>
root     3676118  0.0  0.0      0     0 ?        Z    00:20   0:02 [node] <defunct>
root     3676760  0.0  0.0      0     0 ?        Z    00:21   0:02 [node] <defunct>
root     3677121  0.0  0.0      0     0 ?        Z    00:22   0:02 [node] <defunct>
root     3677419  0.0  0.0      0     0 ?        Z    00:22   0:02 [node] <defunct>
root     3677970  0.0  0.0      0     0 ?        Z    00:23   0:02 [node] <defunct>
root     3678630  0.1  0.0      0     0 ?        Z    00:24   0:03 [node] <defunct>
root     3679329  0.0  0.0      0     0 ?        Z    00:25   0:02 [node] <defunct>
root     3679673  0.0  0.0      0     0 ?        Z    00:26   0:02 [node] <defunct>
root     3679922  0.1  0.0      0     0 ?        Z    00:26   0:03 [node] <defunct>
root     3681053  0.0  0.0      0     0 ?        Z    00:28   0:02 [node] <defunct>
root     3681356  0.0  0.0      0     0 ?        Z    00:28   0:02 [node] <defunct>
root     3681681  0.0  0.0      0     0 ?        Z    00:28   0:02 [node] <defunct>
root     3681996  0.0  0.0      0     0 ?        Z    00:29   0:02 [node] <defunct>
root     3682278  0.0  0.0      0     0 ?        Z    00:29   0:02 [node] <defunct>
root     3682510  0.0  0.0      0     0 ?        Z    00:30   0:02 [node] <defunct>
root     3682805  0.1  0.0      0     0 ?        Z    00:30   0:02 [node] <defunct>
root     3683635  0.1  0.0      0     0 ?        Z    00:31   0:02 [node] <defunct>
root     3683933  0.0  0.0      0     0 ?        Z    00:32   0:02 [node] <defunct>
root     3684221  0.0  0.0      0     0 ?        Z    00:32   0:02 [node] <defunct>
root     3684537  0.1  0.0      0     0 ?        Z    00:33   0:02 [node] <defunct>
root     3684817  0.0  0.0      0     0 ?        Z    00:33   0:02 [node] <defunct>
root     3685117  0.0  0.0      0     0 ?        Z    00:34   0:02 [node] <defunct>
root     3685547  0.0  0.0      0     0 ?        Z    00:34   0:02 [node] <defunct>
root     3686543  0.0  0.0      0     0 ?        Z    00:36   0:02 [node] <defunct>
root     3686835  0.1  0.0      0     0 ?        Z    00:36   0:02 [node] <defunct>
root     3687968  0.1  0.0      0     0 ?        Z    00:38   0:02 [node] <defunct>
root     3688293  0.1  0.0      0     0 ?        Z    00:38   0:02 [node] <defunct>
root     3688616  0.1  0.0      0     0 ?        Z    00:39   0:03 [node] <defunct>
root     3689241  0.1  0.0      0     0 ?        Z    00:39   0:02 [node] <defunct>
root     3689665  0.1  0.0      0     0 ?        Z    00:40   0:02 [node] <defunct>
root     3689971  0.1  0.0      0     0 ?        Z    00:40   0:03 [node] <defunct>
root     3690266  0.1  0.0      0     0 ?        Z    00:41   0:02 [node] <defunct>
root     3690573  0.1  0.0      0     0 ?        Z    00:41   0:02 [node] <defunct>
root     3690822  0.1  0.0      0     0 ?        Z    00:42   0:02 [node] <defunct>
root     3691120  0.1  0.0      0     0 ?        Z    00:42   0:03 [node] <defunct>
root     3691463  0.1  0.0      0     0 ?        Z    00:43   0:02 [node] <defunct>
root     3692135  0.1  0.0      0     0 ?        Z    00:44   0:02 [node] <defunct>
root     3692465  0.1  0.0      0     0 ?        Z    00:44   0:02 [node] <defunct>
root     3693109  0.1  0.0      0     0 ?        Z    00:45   0:02 [node] <defunct>
root     3693973  0.1  0.0      0     0 ?        Z    00:46   0:02 [node] <defunct>
root     3694397  0.1  0.0      0     0 ?        Z    00:47   0:03 [node] <defunct>
root     3694844  0.1  0.0      0     0 ?        Z    00:47   0:02 [node] <defunct>
root     3695202  0.1  0.0      0     0 ?        Z    00:48   0:02 [node] <defunct>
root     3695671  0.1  0.0      0     0 ?        Z    00:48   0:02 [node] <defunct>
root     3695943  0.1  0.0      0     0 ?        Z    00:48   0:02 [node] <defunct>
root     3696362  0.1  0.0      0     0 ?        Z    00:49   0:02 [node] <defunct>
root     3696745  0.1  0.0      0     0 ?        Z    00:49   0:02 [node] <defunct>
root     3697679  0.1  0.0      0     0 ?        Z    00:51   0:02 [node] <defunct>
root     3698105  0.2  0.0      0     0 ?        Z    00:51   0:03 [node] <defunct>
root     3698812  0.2  0.0      0     0 ?        Z    00:52   0:03 [node] <defunct>
root     3701068  0.2  0.0      0     0 ?        Z    00:55   0:03 [node] <defunct>
root     3701617  0.2  0.0      0     0 ?        Z    00:56   0:02 [node] <defunct>
root     3701920  0.2  0.0      0     0 ?        Z    00:56   0:02 [node] <defunct>
root     3702200  0.1  0.0      0     0 ?        Z    00:56   0:02 [node] <defunct>
root     3702592  0.2  0.0      0     0 ?        Z    00:57   0:03 [node] <defunct>
root     3702911  0.2  0.0      0     0 ?        Z    00:58   0:03 [node] <defunct>
root     3703552  0.2  0.0      0     0 ?        Z    00:59   0:03 [node] <defunct>
root     3704443  0.2  0.0      0     0 ?        Z    01:01   0:02 [node] <defunct>
root     3704811  0.2  0.0      0     0 ?        Z    01:01   0:02 [node] <defunct>
root     3705061  0.4  0.0      0     0 ?        Z    01:02   0:03 [node] <defunct>
root     3709004  0.5  0.0      0     0 ?        Z    01:09   0:02 [node] <defunct>
root     3710004  0.3  0.0      0     0 ?        Z    01:11   0:01 [node] <defunct>
root     3712965  0.0  0.0      0     0 ?        Z    01:18   0:00 [runc:[1:CHILD]] <defunct>

```

### Top 20 CPU
```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
amadeus  3713043 2327  0.1  15488  8600 ?        R    01:18   0:02 ps aux --sort=-%cpu
amadeus  3712791 42.2  0.9  96700 79064 ?        Rs   01:18   0:12 /home/amadeus/.hermes/hermes-agent/venv/bin/python3 /home/amadeus/.hermes/hermes-agent/venv/bin/hermes gateway --accept-hooks run
amadeus  3710486 19.8  0.2  20944 16320 ?        R    01:13   1:03 find / -xdev -type f -size +50  -exec du -h {} ;
root     3712976  9.4  0.1  26080 11728 ?        Ss   01:18   0:00 curl http://localhost:4000/health
root      548785  6.6  2.0 2965072 165904 ?      Ssl  May21 2503:09 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
root     3713008  6.2  0.1 1756324 12752 ?       Dl   01:18   0:00 runc --root /var/run/docker/runtime-runc/moby --log /run/containerd/io.containerd.runtime.v2.task/moby/b9f74869291ba57a79de3b05c28743a2422b22545c6fedb828f7dce4bbae3e3c/log.json --log-format json --systemd-cgroup exec --process /tmp/runc-process1476005625 --detach --pid-file /run/containerd/io.containerd.runtime.v2.task/moby/b9f74869291ba57a79de3b05c28743a2422b22545c6fedb828f7dce4bbae3e3c/d7a36d78cf278c94e661dcc7b353c42350dfc4bbbea44eb28869921dcadae0da.pid b9f74869291ba57a79de3b05c28743a2422b22545c6fedb828f7dce4bbae3e3c
root     3712991  6.1  0.1 1830312 12996 ?       Dl   01:18   0:00 runc --root /var/run/docker/runtime-runc/moby --log /run/containerd/io.containerd.runtime.v2.task/moby/c93a006626cd6529b2a031dcd56decd63bf1c7bca3d31868cdf30c9b98bcedcf/log.json --log-format json --systemd-cgroup exec --process /tmp/runc-process570418011 --detach --pid-file /run/containerd/io.containerd.runtime.v2.task/moby/c93a006626cd6529b2a031dcd56decd63bf1c7bca3d31868cdf30c9b98bcedcf/79a835169e99fb4ee1c43cfd7912ae22fdb52d6fa39680c67fd2d32a066c5035.pid c93a006626cd6529b2a031dcd56decd63bf1c7bca3d31868cdf30c9b98bcedcf
root      928748  4.1  2.8 4012884 231956 ?      Sl   Jun11 343:52 /opt/app/rel/logflare/erts-15.2.7.4/bin/beam.smp -sbwt none -sbwtdcpu none -sbwtdio none -sub true -swt very_low -swtdcpu very_low -swtdio very_low -zdbbl 1028000 -P 8000000 -t 32000000 -Mdai max -- -root /opt/app/rel/logflare -bindir /opt/app/rel/logflare/erts-15.2.7.4/bin -progname erl -- -home /root -- -noshell -s elixir start_cli -mode embedded -setcookie SPKW2COZ7PY4RM4ZE4NMDRBDISU64LHNNZDAKW4NJ4LWRZ2KQDBQ==== -name logflare@127.0.0.1 -config /opt/app/rel/logflare/releases/1.36.1/sys -boot /opt/app/rel/logflare/releases/1.36.1/start -boot_var RELEASE_LIB /opt/app/rel/logflare/lib -kernel prevent_overlapping_partitions false -kernel net_ticktime 45 -- -- -- -extra --no-halt
root     3710785  2.5  0.0      0     0 ?        I<   01:14   0:07 [kworker/1:0H-kblockd]
amadeus  4144233  2.1  3.7 1528744 308388 ?      Ssl  Jun06 335:38 /home/amadeus/.hermes/hermes-agent/venv/bin/python3 /home/amadeus/.hermes/hermes-agent/venv/bin/hermes dashboard --host 127.0.0.1 --port 9119 --no-open --skip-build --tui
root      928886  1.3  0.6 2310780 53716 ?       Sl   Jun11 115:07 /app/erts-15.2.1/bin/beam.smp -e 5000 -P 1000000 -zdbbl 2097151 -- -root /app -bindir /app/erts-15.2.1/bin -progname erl -- -home /root -- -proto_dist inet_tcp -- -noshell -s elixir start_cli -mode embedded -setcookie FtNmrQ6mMXFvMwRM4N6Cl8DTRucgybmL0mJ_EPMc -name supavisor@7d0cedc713fd -config /app/releases/2.7.4/sys -boot /app/releases/2.7.4/start -boot_var RELEASE_LIB /app/lib -kernel inet_dist_listen_min 20000 -kernel inet_dist_listen_max 21000 -- -- -- -extra --no-halt
root     3712951  1.2  0.0      0     0 ?        Zl   01:18   0:00 [runc] <defunct>
root     3705229  1.2  0.0      0     0 ?        I<   01:02   0:11 [kworker/1:2H-kblockd]
root      548154  1.1  0.7 2483136 59912 ?       Ssl  May21 423:35 /usr/bin/containerd
root      928104  1.0  0.6 2311464 51884 ?       Sl   Jun11  91:11 /app/erts-15.2.3/bin/beam.smp -hmax 312500000 -zdbbl 100000 -sbwt none -sbwtdio none -sbwtdcpu none -- -root /app -bindir /app/erts-15.2.3/bin -progname erl -- -home /root -- -proto_dist inet_tcp -- -noshell -s elixir start_cli -mode embedded -setcookie LVP6ERBHZNYVLOQ4JWS4FEHC4SXGCOPI53DCZHKZYQGVDBLGAXKA==== -name realtime@127.0.0.1 -config /app/releases/2.76.5/sys -boot /app/releases/2.76.5/start -boot_var RELEASE_LIB /app/lib -- -- -- -extra --no-halt
root     1480789  0.8  0.4 1240984 37096 ?       Sl   Jun14  27:18 /usr/bin/containerd-shim-runc-v2 -namespace moby -id d8677cd6fb1e64f90247982f1223070026c88f68abdea2b670fabc62f5606ea7 -address /run/containerd/containerd.sock
amadeus   931563  0.7  1.1 2587548 89720 ?       R    Jun11  60:18 nginx: worker process
amadeus   931564  0.6  1.0 2586916 89088 ?       S    Jun11  54:15 nginx: worker process
caddy    1521197  0.6  0.8 1503604 71212 ?       Ssl  Jun14  19:25 imgproxy
root     3712740  0.5  0.0      0     0 ?        Zl   01:18   0:00 [runc] <defunct>
root     3709004  0.5  0.0      0     0 ?        Z    01:09   0:02 [node] <defunct>

```

### Top 20 RAM
```

error: unknown sort specifier

Usage:
 ps [options]

 Try 'ps --help <simple|list|output|threads|misc|all>'
  or 'ps --help <s|l|o|t|m|a>'
 for additional help text.

For more details see ps(1).
```


## 15. Pivot checklist (verify before archive)

- [ ] Coolify installed (`ls /data/coolify/source 2>/dev/null`)
- [ ] N8N container running in Coolify (`docker ps --filter name=n8n`)
- [ ] No `supabase` Docker container running
- [ ] No `dokploy` Docker container
- [ ] Caddy vhost `supabase.kalybana.com` REMOVED
- [ ] Hostinger KVM 2 specs: 4 vCPU / 8 GB RAM / 100 GB SSD
- [ ] Steal time stable (`vmstat 5 5` → steal < 30%)
- [ ] All A'Space systemd services (`aspace-*`) DISABLED

---

**End of cartography. Send to A0 for archival. Next step = run pivot checklist §15, then mark VPS for archive (TRASH_DATE directory per doctrine no-hard-delete).**
