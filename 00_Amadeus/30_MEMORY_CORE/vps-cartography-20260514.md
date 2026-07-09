---
source: srv941028.hstgr.cloud (Hostinger KVM 2 VPS, 148.230.92.235)
date: 2026-05-14
type: cartography-snapshot
domain: L0_Tech_OS
tags: [#VPS #cartography #snapshot #post-cleanup #SDD-010 #ADR-RICK-002 #L0_Kernel]
related:
  - SDD-010_meta-cloture-scope-13eme-semaine
  - ADR-RICK-002_paperclip-deprecation-hermes-promotion
  - ADR-RICK-001_openharness-incarnation
totals:
  home_amadeus: "37 GB"
  srv_aspace: "3.2 GB"
notes: |
  Snapshot pris APRÈS le massacre Paperclip purge + cleanup containers + reboot + masking lightdm/apport/hermes-duplicate.
  Pas d'import de la VPS elle-même — seulement la cartographie des dossiers/fichiers comme documentation.
  Cf. SDD-010 §4 "V0 sable mouvant assumé" + §7 anti-patterns documentés.
---

# VPS Cartography — srv941028.hstgr.cloud

**Date** : 2026-05-14T18:24:32Z
**Host** : srv941028.hstgr.cloud
**Auteur** : Claude Architect via SSH
**Contexte** : Snapshot post-cleanup SDD-010 (2026-05-14) — VPS V0 sable mouvant en transition V1

---

## 1. Tailles totales

```
37G	/home/amadeus
3.2G	/srv/aspace
```

## 2. /home/amadeus — Disk Usage (depth 2)

```
37G	/home/amadeus
7.6G	/home/amadeus/.cache
6.1G	/home/amadeus/.npm
4.2G	/home/amadeus/.npm/_cacache
3.7G	/home/amadeus/.git
3.6G	/home/amadeus/.git/objects
3.0G	/home/amadeus/.claude
2.8G	/home/amadeus/.nvm
2.7G	/home/amadeus/.nvm/versions
2.5G	/home/amadeus/.hermes
2.4G	/home/amadeus/.cache/claude-cli-nodejs
2.1G	/home/amadeus/.local
2.0G	/home/amadeus/hermes-workspace
2.0G	/home/amadeus/.vscode-server
2.0G	/home/amadeus/.local/share
1.9G	/home/amadeus/.npm/_npx
1.8G	/home/amadeus/hermes-workspace/node_modules
1.5G	/home/amadeus/.vscode-server/cli
1.4G	/home/amadeus/.cache/camoufox
1.3G	/home/amadeus/.hermes/hermes-agent
1.3G	/home/amadeus/.claude/projects
1.2G	/home/amadeus/hermes-office/node_modules
1.2G	/home/amadeus/hermes-office
1.2G	/home/amadeus/.cache/go-build
1.1G	/home/amadeus/hermes-desktop
1018M	/home/amadeus/hermes-desktop/node_modules
930M	/home/amadeus/.hermes/hermes-office
859M	/home/amadeus/.claude/remote
774M	/home/amadeus/.cache/uv
676M	/home/amadeus/go
635M	/home/amadeus/.claude/worktrees
633M	/home/amadeus/.cache/ms-playwright
606M	/home/amadeus/go/pkg
600M	/home/amadeus/.antigravity-server
489M	/home/amadeus/.cache/puppeteer
348M	/home/amadeus/.antigravity-server/bin
323M	/home/amadeus/snap
318M	/home/amadeus/.vscode-server/extensions
300M	/home/amadeus/50_SERVICES
263M	/home/amadeus/.cache/pip
256M	/home/amadeus/.cache/ms-playwright-go
246M	/home/amadeus/.antigravity-server/extensions
233M	/home/amadeus/.claude/plugins
215M	/home/amadeus/cli-printing-press
211M	/home/amadeus/.opencode
209M	/home/amadeus/.hermes/checkpoints
196M	/home/amadeus/.gemini
180M	/home/amadeus/50_SERVICES/noVNC
165M	/home/amadeus/snap/chromium
158M	/home/amadeus/snap/gemini-cli
```

## 3. /home/amadeus — Tree (depth 3)

```
/home/amadeus
├── .agents
│   └── skills
│       └── find-docs
├── .antigravity-server
│   ├── bin
│   │   └── 1.23.2-15487b3041e65228cae24980a3f796c905ef582c
│   ├── data
│   │   ├── CachedExtensionVSIXs
│   │   ├── CachedProfilesData
│   │   ├── Machine
│   │   ├── User
│   │   ├── logs
│   │   └── machineid
│   ├── extensions
│   │   ├── anthropic.claude-code-2.1.122-linux-x64
│   │   └── extensions.json
│   ├── .15487b3041e65228cae24980a3f796c905ef582c.log
│   ├── .15487b3041e65228cae24980a3f796c905ef582c.pid
│   ├── .15487b3041e65228cae24980a3f796c905ef582c.token
│   └── .installation_lock
├── .cache
│   ├── Microsoft
│   │   └── DeveloperTools
│   ├── at-spi
│   │   └── bus_1
│   ├── camoufox
│   │   ├── addons
│   │   ├── browser
│   │   ├── defaults
│   │   ├── distribution
│   │   ├── fontconfigs
│   │   ├── fonts
│   │   ├── gmp-clearkey
│   │   ├── GeoLite2-City.mmdb
│   │   ├── application.ini
│   │   ├── camoucfg.jvv
│   │   ├── camoufox
│   │   ├── camoufox-bin
│   │   ├── camoufox.cfg
│   │   ├── chrome.css
│   │   ├── dependentlibs.list
│   │   ├── libfreeblpriv3.so
│   │   ├── libgkcodecs.so
│   │   ├── libipcclientcerts.so
│   │   ├── liblgpllibs.so
│   │   ├── libmozavcodec.so
│   │   ├── libmozavutil.so
│   │   ├── libmozgtk.so
│   │   ├── libmozsandbox.so
│   │   ├── libmozsqlite3.so
│   │   ├── libmozwayland.so
│   │   ├── libnspr4.so
│   │   ├── libnss3.so
│   │   ├── libnssckbi.so
│   │   ├── libnssutil3.so
│   │   ├── libplc4.so
│   │   ├── libplds4.so
│   │   ├── libsmime3.so
│   │   ├── libsoftokn3.so
│   │   ├── libssl3.so
│   │   ├── libxul.so
│   │   ├── omni.ja
│   │   ├── platform.ini
│   │   ├── precomplete
│   │   ├── properties.json
│   │   ├── removed-files
│   │   └── version.json
│   ├── chrome-devtools-mcp
│   │   └── latest.json
│   ├── claude
│   │   └── staging
│   ├── claude-cli-nodejs
│   │   ├── -home-amadeus
│   │   ├── -home-amadeus--claude-worktrees-crazy-keller-2de475
│   │   ├── -home-amadeus-Desktop
│   │   ├── -srv-aspace
│   │   ├── -srv-aspace-services-paperclip
│   │   └── -srv-aspace-vault
│   ├── dconf
│   │   └── user
│   ├── doc
│   ├── electron
│   │   └── 628cbe479e4d5dcd0b33c4fd6a8155641dd00d135973eb8b1b6922bb89193ec0
│   ├── evolution
│   │   ├── addressbook
│   │   ├── calendar
│   │   ├── mail
│   │   ├── memos
│   │   ├── sources
│   │   └── tasks
│   ├── fontconfig
│   │   ├── 0bd3dc0958fa2205aaaa8ebb13e2872b-le64.cache-11
│   │   ├── 111149350c6eff283e78acef98e70f62-le64.cache-11
│   │   ├── 188ac73a183f12857f63bb60a4a6d603-le64.cache-11
│   │   ├── 2300eef321c393bfd76478a5c0e95b23-le64.cache-11
│   │   ├── 3047814df9a2f067bd2d96a2b9c36e5a-le64.cache-11
│   │   ├── 32b6488e5b8292a2e95c79d947e009e8-le64.cache-11
│   │   ├── 3830d5c3ddfd5cd38a049b759396e72e-le64.cache-11
│   │   ├── 3f7329c5293ffd510edef78f73874cfd-le64.cache-11
│   │   ├── 4c599c202bc5c08e2d34565a40eac3b2-le64.cache-11
│   │   ├── 4d6aee6d44eccb37054d3216e945f618-le64.cache-11
│   │   ├── 573ec803664ed168555e0e8b6d0f0c7f-le64.cache-11
│   │   ├── 57e423e26b20ab21d0f2f29c145174c3-le64.cache-11
│   │   ├── 6333f38776742d18e214673cd2c24e34-le64.cache-11
│   │   ├── 6cc790b63b123a6a96ee260fcdad32a9-le64.cache-11
│   │   ├── 707971e003b4ae6c8121c3a920e507f5-le64.cache-11
│   │   ├── 7ef2298fde41cc6eeb7af42e48b7d293-le64.cache-11
│   │   ├── 95530828ff6c81d309f8258d8d02a23e-le64.cache-11
│   │   ├── 99e8ed0e538f840c565b6ed5dad60d56-le64.cache-11
│   │   ├── CACHEDIR.TAG
│   │   ├── a4e60e8d1e10d2fdff3fe3037a1845fb-le64.cache-11
│   │   ├── bb9ef35e7661cc55c3d6e0d2d8cc2051-le64.cache-11
│   │   ├── c3bb64600bf7a4aa73b55dc8bb82b27b-le64.cache-11
│   │   ├── c855463f699352c367813e37f3f70ea7-le64.cache-11
│   │   ├── cabbd14511b9e8a55e92af97fb3a0461-le64.cache-11
│   │   ├── d3e5c4ee2ceb1fc347f91d4cefc53bc0-le64.cache-11
│   │   ├── d52a8644073d54c13679302ca1180695-le64.cache-11
│   │   ├── d589a48862398ed80a3d6066f4f56f4c-le64.cache-11
│   │   ├── d82eb4fd963d448e2fcb7d7b793b5df3-le64.cache-11
│   │   ├── da82082e1ef13c4097208324d67c180c-le64.cache-11
│   │   ├── e13b20fdb08344e0e664864cc2ede53d-le64.cache-11
│   │   ├── e52a45a1c8c8fe895fc0fc8c4e6999b8-le64.cache-11
│   │   ├── f1f2465696798768e9653f19e17ccdc8-le64.cache-11
│   │   └── fe547fea3a41b43a38975d292a2b19c7-le64.cache-11
│   ├── go-build
│   │   ├── 00
│   │   ├── 01
│   │   ├── 02
│   │   ├── 03
│   │   ├── 04
│   │   ├── 05
│   │   ├── 06
│   │   ├── 07
│   │   ├── 08
│   │   ├── 09
│   │   ├── 0a
│   │   ├── 0b
│   │   ├── 0c
│   │   ├── 0d
│   │   ├── 0e
│   │   ├── 0f
│   │   ├── 10
│   │   ├── 11
│   │   ├── 12
│   │   ├── 13
│   │   ├── 14
│   │   ├── 15
│   │   ├── 16
│   │   ├── 17
│   │   ├── 18
│   │   ├── 19
│   │   ├── 1a
│   │   ├── 1b
│   │   ├── 1c
│   │   ├── 1d
│   │   ├── 1e
│   │   ├── 1f
│   │   ├── 20
│   │   ├── 21
│   │   ├── 22
│   │   ├── 23
│   │   ├── 24
│   │   ├── 25
│   │   ├── 26
│   │   ├── 27
│   │   ├── 28
│   │   ├── 29
│   │   ├── 2a
│   │   ├── 2b
│   │   ├── 2c
│   │   ├── 2d
│   │   ├── 2e
│   │   ├── 2f
│   │   ├── 30
│   │   ├── 31
│   │   ├── 32
│   │   ├── 33
│   │   ├── 34
│   │   ├── 35
│   │   ├── 36
│   │   ├── 37
│   │   ├── 38
│   │   ├── 39
│   │   ├── 3a
│   │   ├── 3b
│   │   ├── 3c
│   │   ├── 3d
│   │   ├── 3e
│   │   ├── 3f
│   │   ├── 40
│   │   ├── 41
│   │   ├── 42
│   │   ├── 43
│   │   ├── 44
│   │   ├── 45
│   │   ├── 46
│   │   ├── 47
│   │   ├── 48
│   │   ├── 49
│   │   ├── 4a
│   │   ├── 4b
│   │   ├── 4c
│   │   ├── 4d
│   │   ├── 4e
│   │   ├── 4f
│   │   ├── 50
│   │   ├── 51
│   │   ├── 52
│   │   ├── 53
│   │   ├── 54
│   │   ├── 55
│   │   ├── 56
│   │   ├── 57
│   │   ├── 58
│   │   ├── 59
│   │   ├── 5a
│   │   ├── 5b
│   │   ├── 5c
│   │   ├── 5d
│   │   ├── 5e
│   │   ├── 5f
│   │   ├── 60
│   │   ├── 61
│   │   ├── 62
│   │   ├── 63
│   │   ├── 64
│   │   ├── 65
│   │   ├── 66
│   │   ├── 67
│   │   ├── 68
│   │   ├── 69
│   │   ├── 6a
│   │   ├── 6b
│   │   ├── 6c
│   │   ├── 6d
│   │   ├── 6e
│   │   ├── 6f
│   │   ├── 70
│   │   ├── 71
│   │   ├── 72
│   │   ├── 73
│   │   ├── 74
│   │   ├── 75
│   │   ├── 76
│   │   ├── 77
│   │   ├── 78
│   │   ├── 79
│   │   ├── 7a
│   │   ├── 7b
│   │   ├── 7c
│   │   ├── 7d
│   │   ├── 7e
│   │   ├── 7f
│   │   ├── 80
│   │   ├── 81
│   │   ├── 82
│   │   ├── 83
│   │   ├── 84
│   │   ├── 85
│   │   ├── 86
│   │   ├── 87
│   │   ├── 88
│   │   ├── 89
│   │   ├── 8a
│   │   ├── 8b
│   │   ├── 8c
│   │   ├── 8d
│   │   ├── 8e
│   │   ├── 8f
│   │   ├── 90
│   │   ├── 91
│   │   ├── 92
│   │   ├── 93
│   │   ├── 94
│   │   ├── 95
│   │   ├── 96
│   │   ├── 97
│   │   ├── 98
│   │   ├── 99
│   │   ├── 9a
│   │   ├── 9b
│   │   ├── 9c
│   │   ├── 9d
│   │   ├── 9e
│   │   ├── 9f
│   │   ├── a0
│   │   ├── a1
│   │   ├── a2
│   │   ├── a3
│   │   ├── a4
│   │   ├── a5
│   │   ├── a6
│   │   ├── a7
│   │   ├── a8
│   │   ├── a9
│   │   ├── aa
│   │   ├── ab
│   │   ├── ac
│   │   ├── ad
│   │   ├── ae
│   │   ├── af
│   │   ├── b0
│   │   ├── b1
│   │   ├── b2
│   │   ├── b3
│   │   ├── b4
│   │   ├── b5
│   │   ├── b6
│   │   ├── b7
│   │   ├── b8
│   │   ├── b9
│   │   ├── ba
│   │   ├── bb
│   │   ├── bc
│   │   ├── bd
│   │   ├── be
│   │   ├── bf
│   │   ├── c0
│   │   ├── c1
│   │   ├── c2
│   │   ├── c3
│   │   ├── c4
│   │   ├── c5
│   │   ├── c6
│   │   ├── c7
│   │   ├── c8
│   │   ├── c9
│   │   ├── ca
│   │   ├── cb
│   │   ├── cc
│   │   ├── cd
│   │   ├── ce
│   │   ├── cf
│   │   ├── d0
│   │   ├── d1
│   │   ├── d2
│   │   ├── d3
│   │   ├── d4
│   │   ├── d5
│   │   ├── d6
│   │   ├── d7
│   │   ├── d8
│   │   ├── d9
│   │   ├── da
│   │   ├── db
│   │   ├── dc
│   │   ├── dd
│   │   ├── de
│   │   ├── df
│   │   ├── e0
│   │   ├── e1
│   │   ├── e2
│   │   ├── e3
│   │   ├── e4
│   │   ├── e5
│   │   ├── e6
│   │   ├── e7
│   │   ├── e8
│   │   ├── e9
│   │   ├── ea
│   │   ├── eb
│   │   ├── ec
│   │   ├── ed
│   │   ├── ee
│   │   ├── ef
│   │   ├── f0
│   │   ├── f1
│   │   ├── f2
│   │   ├── f3
│   │   ├── f4
│   │   ├── f5
│   │   ├── f6
│   │   ├── f7
│   │   ├── f8
│   │   ├── f9
│   │   ├── fa
│   │   ├── fb
│   │   ├── fc
│   │   ├── fd
│   │   ├── fe
│   │   ├── ff
│   │   ├── README
│   │   └── trim.txt
│   ├── gsd
│   │   └── gsd-update-check.json
│   ├── gstreamer-1.0
│   │   └── registry.x86_64.bin
│   ├── gvfsd
│   ├── keyring-59UJO3
│   │   └── control
│   ├── mesa_shader_cache
│   │   ├── 0f
│   │   ├── 56
│   │   ├── d3
│   │   ├── de
│   │   ├── e9
│   │   ├── index
│   │   └── marker
│   ├── ms-playwright
│   │   ├── .links
│   │   ├── chromium-1217
│   │   ├── chromium_headless_shell-1217
│   │   └── ffmpeg-1011
│   ├── ms-playwright-go
│   │   ├── 1.50.1
│   │   └── 1.57.0
│   ├── node
│   │   └── corepack
│   ├── node-gyp
│   │   └── 24.15.0
│   ├── opencode
│   │   ├── bin
│   │   ├── models.json
│   │   └── version
│   ├── pip
│   │   ├── http-v2
│   │   ├── selfcheck
│   │   └── wheels
│   ├── pipx
│   │   ├── 1ffdd8ee5bac25d
│   │   └── CACHEDIR.TAG
│   ├── pnpm
│   │   └── metadata-v1.3
│   ├── puppeteer
│   │   ├── chrome
│   │   └── chrome-headless-shell
│   ├── sessions
│   ├── thumbnails
│   │   └── large
│   ├── typescript
│   │   └── 5.9
│   ├── uv
│   │   ├── archive-v0
│   │   ├── builds-v0
│   │   ├── interpreter-v4
│   │   ├── sdists-v9
│   │   ├── simple-v21
│   │   ├── wheels-v6
│   │   ├── .gitignore
│   │   ├── .lock
│   │   └── CACHEDIR.TAG
│   ├── vscode-ripgrep
│   │   └── ripgrep-v13.0.0-10-x86_64-unknown-linux-musl.tar.gz
│   ├── xfce4
│   │   └── notifyd
│   └── motd.legal-displayed
├── .claude
│   ├── agent-memory
│   │   ├── beth
│   │   ├── morty
│   │   ├── rick
│   │   └── sovereign-amadeus
│   ├── agents
│   │   ├── beth.md
│   │   ├── gsd-advisor-researcher.md
│   │   ├── gsd-ai-researcher.md
│   │   ├── gsd-assumptions-analyzer.md
│   │   ├── gsd-code-fixer.md
│   │   ├── gsd-code-reviewer.md
│   │   ├── gsd-codebase-mapper.md
│   │   ├── gsd-debug-session-manager.md
│   │   ├── gsd-debugger.md
│   │   ├── gsd-doc-classifier.md
│   │   ├── gsd-doc-synthesizer.md
│   │   ├── gsd-doc-verifier.md
│   │   ├── gsd-doc-writer.md
│   │   ├── gsd-domain-researcher.md
│   │   ├── gsd-eval-auditor.md
│   │   ├── gsd-eval-planner.md
│   │   ├── gsd-executor.md
│   │   ├── gsd-framework-selector.md
│   │   ├── gsd-integration-checker.md
│   │   ├── gsd-intel-updater.md
│   │   ├── gsd-nyquist-auditor.md
│   │   ├── gsd-pattern-mapper.md
│   │   ├── gsd-phase-researcher.md
│   │   ├── gsd-plan-checker.md
│   │   ├── gsd-planner.md
│   │   ├── gsd-project-researcher.md
│   │   ├── gsd-research-synthesizer.md
│   │   ├── gsd-roadmapper.md
│   │   ├── gsd-security-auditor.md
│   │   ├── gsd-ui-auditor.md
│   │   ├── gsd-ui-checker.md
│   │   ├── gsd-ui-researcher.md
│   │   ├── gsd-user-profiler.md
│   │   ├── gsd-verifier.md
│   │   ├── morty.md
│   │   ├── rick.md
│   │   └── sovereign-amadeus.md
│   ├── backups
│   │   ├── .claude.json.backup.1778615381762
│   │   ├── .claude.json.backup.1778615445262
│   │   ├── .claude.json.backup.1778620017865
│   │   ├── .claude.json.backup.1778735408665
│   │   └── .claude.json.backup.1778739884365
│   ├── cache
│   │   └── changelog.md
│   ├── context-mode
```

## 4. /srv/aspace — Disk Usage (depth 2)

```
3.9G	/srv/aspace
1.5G	/srv/aspace/supabase
1.1G	/srv/aspace/archive/paperclip-deprecated-20260513
1.1G	/srv/aspace/archive
734M	/srv/aspace/supabase/apps
595M	/srv/aspace/supabase/.git
477M	/srv/aspace/dashboard
470M	/srv/aspace/dashboard/node_modules
278M	/srv/aspace/web/Life-OS-2026
278M	/srv/aspace/web
206M	/srv/aspace/hermes-workspace
204M	/srv/aspace/venv_litellm/lib
204M	/srv/aspace/venv_litellm
148M	/srv/aspace/supabase/docker
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
8.4M	/srv/aspace/hermes-workspace/src
6.8M	/srv/aspace/dashboard/.next
6.0M	/srv/aspace/vault/30_MEMORY_CORE
5.5M	/srv/aspace/logs
2.2M	/srv/aspace/hermes-workspace/screenshots
868K	/srv/aspace/supabase/i18n
748K	/srv/aspace/supabase/blocks
700K	/srv/aspace/30_MEMORY_CORE/LLM_Wiki
668K	/srv/aspace/supabase/e2e
528K	/srv/aspace/supabase/supabase
516K	/srv/aspace/10_FORGE
512K	/srv/aspace/10_FORGE/12_Blueprints
464K	/srv/aspace/services/openclaw
264K	/srv/aspace/supabase/.github
256K	/srv/aspace/docs
232K	/srv/aspace/00_ORIGIN
224K	/srv/aspace/vault/10_FORGE
212K	/srv/aspace/supabase/.claude
164K	/srv/aspace/main
164K	/srv/aspace/docs/v1.0
164K	/srv/aspace/00_ORIGIN/v1.0
140K	/srv/aspace/hermes-workspace/assets
140K	/srv/aspace/alerts
124K	/srv/aspace/supabase/.agents
124K	/srv/aspace/90_SETUP
120K	/srv/aspace/main/.git
116K	/srv/aspace/hermes-workspace/memory
108K	/srv/aspace/venv_litellm/bin
104K	/srv/aspace/.openharness
96K	/srv/aspace/hermes-workspace/scripts
96K	/srv/aspace/.openharness/autopilot
92K	/srv/aspace/vault/session-auth
```

## 5. /srv/aspace — Tree (depth 4)

```
/srv/aspace
├── .claude
│   └── settings.json
├── .gemini
├── .openclaw
│   └── workspace-state.json
├── .openharness
│   ├── autopilot
│   │   ├── runs
│   │   │   ├── ap-5ea2daaa-attempt-01-run.md
│   │   │   ├── ap-5ea2daaa-run.md
│   │   │   ├── ap-692b9fd3-attempt-01-run.md
│   │   │   ├── ap-692b9fd3-attempt-01-verification.md
│   │   │   ├── ap-692b9fd3-run.md
│   │   │   └── ap-692b9fd3-verification.md
│   │   ├── active_repo_context.md
│   │   ├── autopilot_policy.yaml
│   │   ├── registry.json
│   │   ├── release_policy.yaml
│   │   ├── repo_journal.jsonl
│   │   └── verification_policy.yaml
│   └── plugins
├── 00_ORIGIN
│   ├── personalities
│   │   ├── persona-amy.md
│   │   ├── persona-bill.md
│   │   ├── persona-clara.md
│   │   ├── persona-graham.md
│   │   ├── persona-nardol.md
│   │   ├── persona-river.md
│   │   ├── persona-rory.md
│   │   ├── persona-ryan.md
│   │   ├── persona-yaz.md
│   │   └── personalities-index.json
│   ├── scripts
│   │   └── kernel-boot.sh
│   ├── v1.0
│   │   ├── archive
│   │   │   └── SDD-001_multi-tenant-implementation.archived.md
│   │   ├── ddd
│   │   │   ├── ADR-001_auth-strategy-logic.ddd.md
│   │   │   ├── ADR-001_auth-strategy-persistence.ddd.md
│   │   │   ├── ADR-001_auth-strategy-ui.ddd.md
│   │   │   ├── ADR-002_company-onboarding-logic.ddd.md
│   │   │   ├── ADR-002_company-onboarding-persistence.ddd.md
│   │   │   ├── ADR-002_company-onboarding-ui.ddd.md
│   │   │   ├── ADR-003_continuity-of-memory-logic.ddd.md
│   │   │   ├── ADR-003_continuity-of-memory-persistence.ddd.md
│   │   │   └── ADR-003_continuity-of-memory-ui.ddd.md
│   │   ├── ADR-001_auth-strategy.md
│   │   ├── ADR-002_company-onboarding.md
│   │   ├── ADR-003_continuity-of-memory.md
│   │   └── PRD-001_landing-auth-flow.md
│   ├── LORE.md
│   ├── Rick_Verse_Agents_Brain-Soul-Live.md
│   └── ricks-verse-config-backup.json
├── 10_FORGE
│   └── 12_Blueprints
│       ├── 01-SDD
│       │   ├── .gitkeep
│       │   ├── SDD-000_ricks-verse-constitution.md
│       │   ├── SDD-000b_agent-bootstrap.md
│       │   ├── SDD-000c_aspace-core.md
│       │   ├── SDD-001_solarpunk-kernel-core.md
│       │   ├── SDD-002_a1-rick-harness.md
│       │   ├── SDD-003_tardis-protocol-orchestration.md
│       │   ├── SDD-004_ricks-verse-governance.md
│       │   ├── SDD-005_life-os-l1-integration.md
│       │   ├── SDD-006_business-pulse-l2-pyramide.md
│       │   ├── SDD-007_sob-factory-icp-variants.md
│       │   └── SDD-008_openharness-integration.md
│       ├── 2-PRD
│       │   └── .gitkeep
│       ├── 3-ADR
│       │   └── .gitkeep
│       └── 4-DDD
│           └── .gitkeep
├── 20_RUNTIME
│   ├── 21_Inbox
│   │   ├── A0_TO_A1
│   │   ├── A1_TO_A2
│   │   │   ├── doctor-11
│   │   │   ├── doctor-12
│   │   │   └── doctor-13
│   │   └── A2_TO_A3
│   │       ├── amy
│   │       ├── bill
│   │       ├── clara
│   │       ├── graham
│   │       ├── nardol
│   │       ├── river
│   │       ├── rory
│   │       ├── ryan
│   │       └── yaz
│   └── 22_ActivityLog
├── 30_MEMORY_CORE
│   ├── Gemini_Takeout_2026
│   │   ├── Export Gemini 05
│   │   │   └── 26
│   │   ├── 2025-03_conversations.md
│   │   ├── 2025-05_conversations.md
│   │   ├── 2025-06_conversations.md
│   │   ├── 2025-08_conversations.md
│   │   ├── 2026-03_conversations.md
│   │   ├── 2026-05_conversations.md
│   │   └── _index.md
│   ├── LLM_Wiki
│   │   ├── LLM Wiki
│   │   │   ├── .obsidian
│   │   │   ├── Sans titre
│   │   │   ├── 2026-05-11.md
│   │   │   ├── Bienvenue.md
│   │   │   ├── Sans titre.base
│   │   │   └── Sans titre.canvas
│   │   ├── raw
│   │   │   └── sdd
│   │   └── wiki
│   │       ├── comparisons
│   │       ├── concepts
│   │       ├── entities
│   │       ├── sources
│   │       ├── syntheses
│   │       ├── index.md
│   │       ├── log.md
│   │       └── schema.md
│   ├── daily-summaries
│   ├── incidents
│   ├── system
│   │   ├── daily-summary-20260428.md
│   │   ├── incidents-20260428.jsonl
│   │   ├── incidents.jsonl
│   │   └── swarm-state-20260428.json
│   └── wiki
│       └── WIKI.md
├── 40_SKILLS
│   └── registry.json
├── 90_SETUP
│   ├── launch
│   │   ├── heartbeats
│   │   ├── systemd
│   │   │   ├── aspace-donna-watcher.service
│   │   │   ├── aspace-graham-daily.service
│   │   │   ├── aspace-graham-daily.timer
│   │   │   ├── aspace-rick-watcher.service
│   │   │   ├── aspace-watcher@.service
│   │   │   ├── aspace-yaz-monitor.service
│   │   │   └── aspace-yaz-monitor.timer
│   │   ├── watchers
│   │   │   ├── dlq-watcher.sh
│   │   │   └── inbox-watcher.sh
│   │   ├── ARCHITECTURE.md
│   │   ├── install.sh
│   │   └── status.sh
│   ├── schedulers
│   ├── systemd
│   │   ├── claude.service
│   │   ├── hermes.service
│   │   ├── obsidian.service
│   │   ├── openclaw.service
│   │   ├── opencode.service
│   │   ├── paperclip.service
│   │   └── syncthing.service
│   ├── aspace-status.sh
│   ├── bootstrap.sh
│   ├── install-agents.sh
│   ├── install-runtime.sh
│   └── install-syncthing.sh
├── alerts
│   ├── dedup_state.json
│   ├── pending.jsonl
│   └── pending_tmp.jsonl
├── archive
│   └── paperclip-deprecated-20260513
│       ├── .claude
│       │   └── settings.json
│       ├── .paperclip
│       ├── 23_DLQ_Donna
│       │   ├── escalated
│       │   ├── pending
│       │   └── retrying
│       ├── cli
│       │   ├── dist
│       │   ├── node_modules
│       │   ├── src
│       │   ├── CHANGELOG.md
│       │   ├── README.md
│       │   ├── esbuild.config.mjs
│       │   ├── package.json
│       │   ├── tsconfig.json
│       │   └── vitest.config.ts
│       ├── doc
│       │   ├── assets
│       │   ├── experimental
│       │   ├── plans
│       │   ├── plugins
│       │   ├── spec
│       │   ├── AGENTCOMPANIES_SPEC_INVENTORY.md
│       │   ├── CLI.md
│       │   ├── CLIPHUB.md
│       │   ├── DATABASE.md
│       │   ├── DEPLOYMENT-MODES.md
│       │   ├── DEVELOPING.md
│       │   ├── DOCKER.md
│       │   ├── GOAL.md
│       │   ├── OPENCLAW_ONBOARDING.md
│       │   ├── PRODUCT.md
│       │   ├── PUBLISHING.md
│       │   ├── README-draft.md
│       │   ├── RELEASE-AUTOMATION-SETUP.md
│       │   ├── RELEASING.md
│       │   ├── SPEC-implementation.md
│       │   ├── SPEC.md
│       │   ├── TASKS-mcp.md
│       │   ├── TASKS.md
│       │   ├── UNTRUSTED-PR-REVIEW.md
│       │   ├── execution-semantics.md
│       │   └── memory-landscape.md
│       ├── docker
│       │   ├── openclaw-smoke
│       │   ├── quadlet
│       │   ├── untrusted-review
│       │   ├── Dockerfile.onboard-smoke
│       │   ├── docker-compose.quickstart.yml
│       │   ├── docker-compose.untrusted-review.yml
│       │   └── docker-compose.yml
│       ├── docs
│       │   ├── adapters
│       │   ├── api
│       │   ├── cli
│       │   ├── companies
│       │   ├── deploy
│       │   ├── guides
│       │   ├── images
│       │   ├── plans
│       │   ├── specs
│       │   ├── start
│       │   ├── agents-runtime.md
│       │   ├── docs.json
│       │   ├── favicon.svg
│       │   └── feedback-voting.md
│       ├── evals
│       │   ├── promptfoo
│       │   └── README.md
│       ├── instances
│       │   └── default
│       ├── node_modules
│       │   ├── .bin
│       │   ├── .pnpm
│       │   ├── @playwright
│       │   ├── cross-env -> .pnpm/cross-env@10.1.0/node_modules/cross-env
│       │   ├── esbuild -> .pnpm/esbuild@0.27.3/node_modules/esbuild
│       │   ├── typescript -> .pnpm/typescript@5.9.3/node_modules/typescript
│       │   ├── vitest -> .pnpm/vitest@3.2.4_@types+debug@4.1.12_@types+node@25.2.3_jiti@2.6.1_jsdom@28.1.0_@noble+hashes@2.0_mqcfvgfdrjnnoo74iikdalygga/node_modules/vitest
│       │   └── .modules.yaml
│       ├── packages
│       │   ├── adapter-utils
│       │   ├── adapters
│       │   ├── db
│       │   ├── mcp-server
│       │   ├── plugins
│       │   └── shared
│       ├── patches
│       │   └── embedded-postgres@18.1.0-beta.16.patch
│       ├── releases
│       │   ├── .gitkeep
│       │   ├── v0.2.7.md
│       │   ├── v0.3.0.md
│       │   ├── v0.3.1.md
│       │   ├── v2026.318.0.md
│       │   ├── v2026.325.0.md
│       │   ├── v2026.403.0.md
│       │   ├── v2026.415.0.md
│       │   └── v2026.416.0.md
│       ├── report
│       │   └── 2026-03-13-08-46-token-optimization-implementation.md
│       ├── scripts
│       │   ├── smoke
│       │   ├── backup-db.sh
│       │   ├── build-npm.sh
│       │   ├── check-forbidden-tokens.mjs
│       │   ├── clean-onboard-git.sh
│       │   ├── clean-onboard-npm.sh
│       │   ├── clean-onboard-ref.sh
│       │   ├── create-github-release.sh
│       │   ├── dev-runner-output.mjs
│       │   ├── dev-runner-output.ts
│       │   ├── dev-runner-paths.mjs
│       │   ├── dev-runner.mjs
│       │   ├── dev-runner.ts
│       │   ├── dev-service-profile.ts
│       │   ├── dev-service.ts
│       │   ├── docker-build-test.sh
│       │   ├── docker-entrypoint.sh
│       │   ├── docker-onboard-smoke.sh
│       │   ├── ensure-plugin-build-deps.mjs
│       │   ├── ensure-workspace-package-links.ts
│       │   ├── generate-company-assets.ts
│       │   ├── generate-npm-package-json.mjs
│       │   ├── generate-org-chart-images.ts
│       │   ├── generate-org-chart-satori-comparison.ts
│       │   ├── generate-ui-package-json.mjs
│       │   ├── kill-agent-browsers.sh
│       │   ├── kill-dev.sh
│       │   ├── migrate-inline-env-secrets.ts
│       │   ├── paperclip-commit-metrics.ts
│       │   ├── paperclip-issue-update.sh
│       │   ├── prepare-server-ui-dist.sh
│       │   ├── provision-worktree.sh
│       │   ├── release-lib.sh
│       │   ├── release-package-map.mjs
│       │   ├── release.sh
│       │   ├── rollback-latest.sh
│       │   └── screenshot.cjs
│       ├── server
│       │   ├── dist
│       │   ├── node_modules
│       │   ├── scripts
│       │   ├── src
│       │   ├── ui-dist
│       │   ├── .env
│       │   ├── CHANGELOG.md
│       │   ├── package.json
│       │   ├── tsconfig.json
│       │   └── vitest.config.ts
│       ├── skills
│       │   ├── paperclip
│       │   ├── paperclip-create-agent
│       │   ├── paperclip-create-plugin
│       │   └── para-memory-files
│       ├── state
│       │   └── rick-c137.json
│       ├── tests
│       │   ├── e2e
│       │   └── release-smoke
│       ├── ui
│       │   ├── dist
│       │   ├── node_modules
│       │   ├── public
│       │   ├── src
│       │   ├── README.md
│       │   ├── components.json
│       │   ├── index.html
│       │   ├── package.json
│       │   ├── tsconfig.json
│       │   ├── tsconfig.tsbuildinfo
│       │   ├── vite.config.ts
│       │   └── vitest.config.ts
│       ├── .env
│       ├── AGENTS.md
│       ├── CONTRIBUTING.md
│       ├── Dockerfile
│       ├── FIX_SLASH_COMMANDS.md
│       ├── INSTALLATION_STATUS.md
│       ├── LICENSE
│       ├── README.md
│       ├── ROADMAP.md
│       ├── SECURITY.md
│       ├── SLASH_COMMANDS_README.md
│       ├── SOLUTION.md
│       ├── START_PAPERCLIP.sh
│       ├── adapter-plugin.md
│       ├── config.json
│       ├── config.json.backup-corrupted
│       ├── package.json
│       ├── pm2-start.sh
│       ├── pm2-start.sh.bak.20260512_202059
│       ├── pnpm-lock.yaml
│       ├── pnpm-workspace.yaml
│       ├── slash-commands.json
│       ├── start.sh
│       ├── tsconfig.base.json
│       ├── tsconfig.json
│       └── vitest.config.ts
├── backups
│   ├── db-dumps
│   ├── services-snapshots
│   └── vault-snapshots
├── dashboard
│   ├── .next
│   │   ├── build
│   │   │   ├── chunks
│   │   │   ├── package.json
│   │   │   ├── postcss.js
│   │   │   └── postcss.js.map
│   │   ├── cache
│   │   │   ├── .previewinfo
│   │   │   ├── .rscinfo
│   │   │   └── .tsbuildinfo
│   │   ├── diagnostics
│   │   │   ├── build-diagnostics.json
│   │   │   ├── framework.json
│   │   │   └── route-bundle-stats.json
│   │   ├── server
│   │   │   ├── app
│   │   │   ├── chunks
│   │   │   ├── pages
│   │   │   ├── app-paths-manifest.json
│   │   │   ├── functions-config-manifest.json
│   │   │   ├── interception-route-rewrite-manifest.js
│   │   │   ├── middleware-build-manifest.js
│   │   │   ├── middleware-manifest.json
│   │   │   ├── next-font-manifest.js
│   │   │   ├── next-font-manifest.json
│   │   │   ├── pages-manifest.json
│   │   │   ├── prefetch-hints.json
│   │   │   ├── server-reference-manifest.js
│   │   │   └── server-reference-manifest.json
│   │   ├── static
│   │   │   ├── 6e3d2fJxqrxzNssCj2NMV
│   │   │   ├── chunks
│   │   │   └── media
│   │   ├── types
│   │   │   ├── cache-life.d.ts
│   │   │   ├── routes.d.ts
│   │   │   └── validator.ts
│   │   ├── BUILD_ID
│   │   ├── app-path-routes-manifest.json
│   │   ├── build-manifest.json
│   │   ├── export-marker.json
│   │   ├── fallback-build-manifest.json
│   │   ├── images-manifest.json
│   │   ├── next-minimal-server.js.nft.json
│   │   ├── next-server.js.nft.json
│   │   ├── package.json
│   │   ├── prerender-manifest.json
│   │   ├── required-server-files.js
│   │   ├── required-server-files.json
│   │   ├── routes-manifest.json
│   │   ├── trace
│   │   ├── trace-build
│   │   └── turbopack
│   ├── app
│   │   ├── actions
│   │   │   └── getServiceStatus.ts
│   │   ├── api
│   │   │   └── health
│   │   ├── favicon.ico
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components
│   │   ├── DashboardClient.tsx
│   │   ├── GlassCard.tsx
│   │   ├── ServiceCard.tsx
│   │   ├── Sidebar.tsx
│   │   └── StatusIndicator.tsx
│   ├── hooks
│   │   └── useServicePoll.ts
│   ├── node_modules
│   │   ├── .bin
│   │   │   ├── acorn -> ../acorn/bin/acorn
│   │   │   ├── baseline-browser-mapping -> ../baseline-browser-mapping/dist/cli.cjs
│   │   │   ├── browserslist -> ../browserslist/cli.js
│   │   │   ├── eslint -> ../eslint/bin/eslint.js
│   │   │   ├── jiti -> ../jiti/lib/jiti-cli.mjs
│   │   │   ├── js-yaml -> ../js-yaml/bin/js-yaml.js
│   │   │   ├── jsesc -> ../jsesc/bin/jsesc
│   │   │   ├── json5 -> ../json5/lib/cli.js
│   │   │   ├── loose-envify -> ../loose-envify/cli.js
│   │   │   ├── nanoid -> ../nanoid/bin/nanoid.cjs
│   │   │   ├── napi-postinstall -> ../napi-postinstall/lib/cli.js
│   │   │   ├── next -> ../next/dist/bin/next
│   │   │   ├── node-which -> ../which/bin/node-which
│   │   │   ├── parser -> ../@babel/parser/bin/babel-parser.js
│   │   │   ├── resolve -> ../resolve/bin/resolve
│   │   │   ├── semver -> ../semver/bin/semver.js
│   │   │   ├── tsc -> ../typescript/bin/tsc
│   │   │   ├── tsserver -> ../typescript/bin/tsserver
│   │   │   └── update-browserslist-db -> ../update-browserslist-db/cli.js
│   │   ├── @alloc
│   │   │   └── quick-lru
│   │   ├── @babel
│   │   │   ├── code-frame
│   │   │   ├── compat-data
│   │   │   ├── core
│   │   │   ├── generator
│   │   │   ├── helper-compilation-targets
│   │   │   ├── helper-globals
│   │   │   ├── helper-module-imports
│   │   │   ├── helper-module-transforms
│   │   │   ├── helper-string-parser
│   │   │   ├── helper-validator-identifier
│   │   │   ├── helper-validator-option
│   │   │   ├── helpers
│   │   │   ├── parser
│   │   │   ├── template
│   │   │   ├── traverse
│   │   │   └── types
│   │   ├── @emnapi
│   │   │   ├── core
│   │   │   ├── runtime
│   │   │   └── wasi-threads
│   │   ├── @eslint
│   │   │   ├── config-array
│   │   │   ├── config-helpers
│   │   │   ├── core
│   │   │   ├── eslintrc
│   │   │   ├── js
│   │   │   ├── object-schema
│   │   │   └── plugin-kit
│   │   ├── @eslint-community
│   │   │   ├── eslint-utils
│   │   │   └── regexpp
│   │   ├── @humanfs
│   │   │   ├── core
│   │   │   └── node
│   │   ├── @humanwhocodes
│   │   │   ├── module-importer
│   │   │   └── retry
│   │   ├── @img
│   │   │   ├── colour
│   │   │   ├── sharp-libvips-linux-x64
│   │   │   └── sharp-linux-x64
│   │   ├── @jridgewell
│   │   │   ├── gen-mapping
│   │   │   ├── remapping
│   │   │   ├── resolve-uri
│   │   │   ├── sourcemap-codec
│   │   │   └── trace-mapping
│   │   ├── @napi-rs
│   │   │   └── wasm-runtime
│   │   ├── @next
│   │   │   ├── env
│   │   │   ├── eslint-plugin-next
│   │   │   └── swc-linux-x64-gnu
│   │   ├── @nodelib
│   │   │   ├── fs.scandir
│   │   │   ├── fs.stat
│   │   │   └── fs.walk
│   │   ├── @nolyfill
│   │   │   └── is-core-module
│   │   ├── @rtsao
│   │   │   └── scc
│   │   ├── @swc
│   │   │   └── helpers
│   │   ├── @tailwindcss
│   │   │   ├── node
│   │   │   ├── oxide
│   │   │   ├── oxide-linux-x64-gnu
│   │   │   └── postcss
│   │   ├── @tybys
│   │   │   └── wasm-util
│   │   ├── @types
│   │   │   ├── estree
│   │   │   ├── json-schema
│   │   │   ├── json5
│   │   │   ├── node
│   │   │   ├── react
│   │   │   └── react-dom
│   │   ├── @typescript-eslint
│   │   │   ├── eslint-plugin
│   │   │   ├── parser
│   │   │   ├── project-service
│   │   │   ├── scope-manager
│   │   │   ├── tsconfig-utils
│   │   │   ├── type-utils
│   │   │   ├── types
│   │   │   ├── typescript-estree
│   │   │   ├── utils
│   │   │   └── visitor-keys
│   │   ├── @unrs
│   │   │   └── resolver-binding-linux-x64-gnu
│   │   ├── acorn
│   │   │   ├── bin
│   │   │   ├── dist
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── acorn-jsx
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   └── xhtml.js
│   │   ├── ajv
│   │   │   ├── dist
│   │   │   ├── lib
│   │   │   ├── scripts
│   │   │   ├── .tonic_example.js
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── ansi-styles
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── license
│   │   │   ├── package.json
│   │   │   └── readme.md
│   │   ├── argparse
│   │   │   ├── lib
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── argparse.js
│   │   │   └── package.json
│   │   ├── aria-query
│   │   │   ├── lib
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── array-buffer-byte-length
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   ├── array-includes
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .editorconfig
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── auto.js
│   │   │   ├── implementation.js
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   ├── polyfill.js
│   │   │   └── shim.js
│   │   ├── array.prototype.findlast
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .editorconfig
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── auto.js
│   │   │   ├── implementation.js
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   ├── polyfill.js
│   │   │   └── shim.js
│   │   ├── array.prototype.findlastindex
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── auto.js
│   │   │   ├── implementation.js
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   ├── polyfill.js
│   │   │   └── shim.js
│   │   ├── array.prototype.flat
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .editorconfig
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── auto.js
│   │   │   ├── implementation.js
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   ├── polyfill.js
│   │   │   └── shim.js
│   │   ├── array.prototype.flatmap
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .editorconfig
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── auto.js
│   │   │   ├── implementation.js
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   ├── polyfill.js
│   │   │   └── shim.js
│   │   ├── array.prototype.tosorted
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── auto.js
│   │   │   ├── implementation.js
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   ├── polyfill.js
│   │   │   └── shim.js
│   │   ├── arraybuffer.prototype.slice
│   │   │   ├── test
│   │   │   ├── .editorconfig
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── auto.js
│   │   │   ├── implementation.js
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   ├── polyfill.js
│   │   │   └── shim.js
│   │   ├── ast-types-flow
│   │   │   ├── lib
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── async-function
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.mts
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── index.mjs
│   │   │   ├── legacy.js
│   │   │   ├── package.json
│   │   │   ├── require.mjs
│   │   │   └── tsconfig.json
│   │   ├── available-typed-arrays
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   ├── axe-core
│   │   │   ├── locales
│   │   │   ├── LICENSE
│   │   │   ├── LICENSE-3RD-PARTY.txt
│   │   │   ├── README.md
│   │   │   ├── axe.d.ts
│   │   │   ├── axe.js
│   │   │   ├── axe.min.js
│   │   │   ├── package.json
│   │   │   └── sri-history.json
│   │   ├── axobject-query
│   │   │   ├── lib
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── balanced-match
│   │   │   ├── .github
│   │   │   ├── LICENSE.md
│   │   │   ├── README.md
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── baseline-browser-mapping
│   │   │   ├── dist
│   │   │   ├── LICENSE.txt
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── brace-expansion
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── braces
│   │   │   ├── lib
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── browserslist
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── browser.js
│   │   │   ├── cli.js
│   │   │   ├── error.d.ts
│   │   │   ├── error.js
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── node.js
│   │   │   ├── package.json
│   │   │   └── parse.js
│   │   ├── call-bind
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintignore
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── callBound.js
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── call-bind-apply-helpers
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── actualApply.d.ts
│   │   │   ├── actualApply.js
│   │   │   ├── applyBind.d.ts
│   │   │   ├── applyBind.js
│   │   │   ├── functionApply.d.ts
│   │   │   ├── functionApply.js
│   │   │   ├── functionCall.d.ts
│   │   │   ├── functionCall.js
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   ├── reflectApply.d.ts
│   │   │   ├── reflectApply.js
│   │   │   └── tsconfig.json
│   │   ├── call-bound
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   ├── callsites
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── license
│   │   │   ├── package.json
│   │   │   └── readme.md
│   │   ├── caniuse-lite
│   │   │   ├── data
│   │   │   ├── dist
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── chalk
│   │   │   ├── source
│   │   │   ├── index.d.ts
│   │   │   ├── license
│   │   │   ├── package.json
│   │   │   └── readme.md
│   │   ├── client-only
│   │   │   ├── error.js
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── color-convert
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── conversions.js
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   └── route.js
│   │   ├── color-name
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── concat-map
│   │   │   ├── example
│   │   │   ├── test
│   │   │   ├── .travis.yml
│   │   │   ├── LICENSE
│   │   │   ├── README.markdown
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── convert-source-map
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── cross-spawn
│   │   │   ├── lib
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── csstype
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js.flow
│   │   │   └── package.json
│   │   ├── damerau-levenshtein
│   │   │   ├── scripts
│   │   │   ├── test
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── data-view-buffer
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   ├── data-view-byte-length
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   ├── data-view-byte-offset
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   ├── debug
│   │   │   ├── src
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── deep-is
│   │   │   ├── example
│   │   │   ├── test
│   │   │   ├── .travis.yml
│   │   │   ├── LICENSE
│   │   │   ├── README.markdown
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── define-data-property
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   ├── define-properties
│   │   │   ├── .github
│   │   │   ├── .editorconfig
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── detect-libc
│   │   │   ├── lib
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   └── package.json
│   │   ├── doctrine
│   │   │   ├── lib
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── LICENSE.closure-compiler
│   │   │   ├── LICENSE.esprima
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── dunder-proto
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── get.d.ts
│   │   │   ├── get.js
│   │   │   ├── package.json
│   │   │   ├── set.d.ts
│   │   │   ├── set.js
│   │   │   └── tsconfig.json
│   │   ├── electron-to-chromium
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── chromium-versions.js
│   │   │   ├── chromium-versions.json
│   │   │   ├── full-chromium-versions.js
│   │   │   ├── full-chromium-versions.json
│   │   │   ├── full-versions.js
│   │   │   ├── full-versions.json
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   ├── versions.js
│   │   │   └── versions.json
│   │   ├── emoji-regex
│   │   │   ├── es2015
│   │   │   ├── LICENSE-MIT.txt
│   │   │   ├── README.md
│   │   │   ├── RGI_Emoji.d.ts
│   │   │   ├── RGI_Emoji.js
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   ├── text.d.ts
│   │   │   └── text.js
│   │   ├── enhanced-resolve
│   │   │   ├── lib
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── package.json
│   │   │   └── types.d.ts
│   │   ├── es-abstract
│   │   │   ├── 2015
│   │   │   ├── 2016
│   │   │   ├── 2017
│   │   │   ├── 2018
│   │   │   ├── 2019
│   │   │   ├── 2020
│   │   │   ├── 2021
│   │   │   ├── 2022
│   │   │   ├── 2023
│   │   │   ├── 2024
│   │   │   ├── 2025
│   │   │   ├── 5
│   │   │   ├── helpers
│   │   │   ├── operations
│   │   │   ├── .editorconfig
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── GetIntrinsic.js
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── es2015.js
│   │   │   ├── es2016.js
│   │   │   ├── es2017.js
│   │   │   ├── es2018.js
│   │   │   ├── es2019.js
│   │   │   ├── es2020.js
│   │   │   ├── es2021.js
│   │   │   ├── es2022.js
│   │   │   ├── es2023.js
│   │   │   ├── es2024.js
│   │   │   ├── es2025.js
│   │   │   ├── es5.js
│   │   │   ├── es6.js
│   │   │   ├── es7.js
│   │   │   ├── eslint.config.mjs
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── es-define-property
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   ├── es-errors
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── eval.d.ts
│   │   │   ├── eval.js
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   ├── range.d.ts
│   │   │   ├── range.js
│   │   │   ├── ref.d.ts
│   │   │   ├── ref.js
│   │   │   ├── syntax.d.ts
│   │   │   ├── syntax.js
│   │   │   ├── tsconfig.json
│   │   │   ├── type.d.ts
│   │   │   ├── type.js
│   │   │   ├── uri.d.ts
│   │   │   └── uri.js
│   │   ├── es-iterator-helpers
│   │   │   ├── .github
│   │   │   ├── Iterator
│   │   │   ├── Iterator.concat
│   │   │   ├── Iterator.from
│   │   │   ├── Iterator.prototype
│   │   │   ├── Iterator.prototype.constructor
│   │   │   ├── Iterator.prototype.drop
│   │   │   ├── Iterator.prototype.every
│   │   │   ├── Iterator.prototype.filter
│   │   │   ├── Iterator.prototype.find
│   │   │   ├── Iterator.prototype.flatMap
│   │   │   ├── Iterator.prototype.forEach
│   │   │   ├── Iterator.prototype.includes
│   │   │   ├── Iterator.prototype.map
│   │   │   ├── Iterator.prototype.reduce
│   │   │   ├── Iterator.prototype.some
│   │   │   ├── Iterator.prototype.take
│   │   │   ├── Iterator.prototype.toArray
│   │   │   ├── Iterator.zip
│   │   │   ├── Iterator.zipKeyed
│   │   │   ├── IteratorHelperPrototype
│   │   │   ├── WrapForValidIteratorPrototype
│   │   │   ├── aos
│   │   │   ├── test
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── auto.js
│   │   │   ├── eslint.config.mjs
│   │   │   ├── index.json
│   │   │   ├── package.json
│   │   │   └── shim.js
│   │   ├── es-object-atoms
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── RequireObjectCoercible.d.ts
│   │   │   ├── RequireObjectCoercible.js
│   │   │   ├── ToObject.d.ts
│   │   │   ├── ToObject.js
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── isObject.d.ts
│   │   │   ├── isObject.js
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   ├── es-set-tostringtag
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   ├── es-shim-unscopables
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   ├── es-to-primitive
│   │   │   ├── .github
│   │   │   ├── helpers
│   │   │   ├── test
│   │   │   ├── .editorconfig
│   │   │   ├── .eslintignore
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── es2015.d.ts
│   │   │   ├── es2015.js
│   │   │   ├── es5.d.ts
│   │   │   ├── es5.js
│   │   │   ├── es6.d.ts
│   │   │   ├── es6.js
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   ├── escalade
│   │   │   ├── dist
│   │   │   ├── sync
│   │   │   ├── index.d.mts
│   │   │   ├── index.d.ts
│   │   │   ├── license
│   │   │   ├── package.json
│   │   │   └── readme.md
│   │   ├── escape-string-regexp
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── license
│   │   │   ├── package.json
│   │   │   └── readme.md
│   │   ├── eslint
│   │   │   ├── bin
│   │   │   ├── conf
│   │   │   ├── lib
│   │   │   ├── messages
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── eslint-config-next
│   │   │   ├── dist
│   │   │   ├── node_modules
│   │   │   └── package.json
│   │   ├── eslint-import-resolver-node
│   │   │   ├── node_modules
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── eslint-import-resolver-typescript
│   │   │   ├── lib
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── eslint-module-utils
│   │   │   ├── node_modules
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── ModuleCache.d.ts
│   │   │   ├── ModuleCache.js
│   │   │   ├── contextCompat.d.ts
│   │   │   ├── contextCompat.js
│   │   │   ├── declaredScope.d.ts
│   │   │   ├── declaredScope.js
│   │   │   ├── hash.d.ts
│   │   │   ├── hash.js
│   │   │   ├── ignore.d.ts
│   │   │   ├── ignore.js
│   │   │   ├── module-require.d.ts
│   │   │   ├── module-require.js
│   │   │   ├── moduleVisitor.d.ts
│   │   │   ├── moduleVisitor.js
│   │   │   ├── package.json
│   │   │   ├── parse.d.ts
│   │   │   ├── parse.js
│   │   │   ├── pkgDir.d.ts
│   │   │   ├── pkgDir.js
│   │   │   ├── pkgUp.d.ts
│   │   │   ├── pkgUp.js
│   │   │   ├── readPkgUp.d.ts
│   │   │   ├── readPkgUp.js
│   │   │   ├── resolve.d.ts
│   │   │   ├── resolve.js
│   │   │   ├── tsconfig.json
│   │   │   ├── types.d.ts
│   │   │   ├── unambiguous.d.ts
│   │   │   ├── unambiguous.js
│   │   │   ├── visit.d.ts
│   │   │   └── visit.js
│   │   ├── eslint-plugin-import
│   │   │   ├── config
│   │   │   ├── docs
│   │   │   ├── lib
│   │   │   ├── memo-parser
│   │   │   ├── node_modules
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── SECURITY.md
│   │   │   ├── index.d.ts
│   │   │   └── package.json
│   │   ├── eslint-plugin-jsx-a11y
│   │   │   ├── __mocks__
│   │   │   ├── __tests__
│   │   │   ├── docs
│   │   │   ├── lib
│   │   │   ├── .babelrc
│   │   │   ├── .eslintrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE.md
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── eslint-plugin-react
│   │   │   ├── configs
│   │   │   ├── lib
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.d.ts.map
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── eslint-plugin-react-hooks
│   │   │   ├── cjs
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── eslint-scope
│   │   │   ├── dist
│   │   │   ├── lib
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── eslint-visitor-keys
│   │   │   ├── dist
│   │   │   ├── lib
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── espree
│   │   │   ├── dist
│   │   │   ├── lib
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── espree.js
│   │   │   └── package.json
│   │   ├── esquery
│   │   │   ├── dist
│   │   │   ├── README.md
│   │   │   ├── license.txt
│   │   │   ├── package.json
│   │   │   └── parser.js
│   │   ├── esrecurse
│   │   │   ├── .babelrc
│   │   │   ├── README.md
│   │   │   ├── esrecurse.js
│   │   │   ├── gulpfile.babel.js
│   │   │   └── package.json
│   │   ├── estraverse
│   │   │   ├── .jshintrc
│   │   │   ├── LICENSE.BSD
│   │   │   ├── README.md
│   │   │   ├── estraverse.js
│   │   │   ├── gulpfile.js
│   │   │   └── package.json
│   │   ├── esutils
│   │   │   ├── lib
│   │   │   ├── LICENSE.BSD
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── fast-deep-equal
│   │   │   ├── es6
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   ├── react.d.ts
│   │   │   └── react.js
│   │   ├── fast-glob
│   │   │   ├── node_modules
│   │   │   ├── out
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   └── package.json
│   │   ├── fast-json-stable-stringify
│   │   │   ├── .github
│   │   │   ├── benchmark
│   │   │   ├── example
│   │   │   ├── test
│   │   │   ├── .eslintrc.yml
│   │   │   ├── .travis.yml
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── fast-levenshtein
│   │   │   ├── LICENSE.md
│   │   │   ├── README.md
│   │   │   ├── levenshtein.js
│   │   │   └── package.json
│   │   ├── fastq
│   │   │   ├── test
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── SECURITY.md
│   │   │   ├── bench.js
│   │   │   ├── eslint.config.js
│   │   │   ├── example.js
│   │   │   ├── example.mjs
│   │   │   ├── index.d.ts
│   │   │   ├── package.json
│   │   │   └── queue.js
│   │   ├── file-entry-cache
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── cache.js
│   │   │   └── package.json
│   │   ├── fill-range
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── find-up
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── license
│   │   │   ├── package.json
│   │   │   └── readme.md
│   │   ├── flat-cache
│   │   │   ├── src
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── changelog.md
│   │   │   └── package.json
│   │   ├── flatted
│   │   │   ├── cjs
│   │   │   ├── esm
│   │   │   ├── golang
│   │   │   ├── php
│   │   │   ├── python
│   │   │   ├── types
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── es.js
│   │   │   ├── esm.js
│   │   │   ├── index.js
│   │   │   ├── min.js
│   │   │   └── package.json
│   │   ├── for-each
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .editorconfig
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   ├── function-bind
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── implementation.js
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── function.prototype.name
│   │   │   ├── .github
│   │   │   ├── helpers
│   │   │   ├── test
│   │   │   ├── .editorconfig
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── auto.js
│   │   │   ├── implementation.js
│   │   │   ├── index.js
│   │   │   ├── package.json
│   │   │   ├── polyfill.js
│   │   │   └── shim.js
│   │   ├── functions-have-names
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .editorconfig
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
│   │   │   ├── CHANGELOG.md
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── generator-function
│   │   │   ├── .github
│   │   │   ├── test
│   │   │   ├── .eslintrc
│   │   │   ├── .nycrc
```

## 6. Active systemd services

```
  UNIT                           LOAD   ACTIVE SUB     DESCRIPTION
  accounts-daemon.service        loaded active running Accounts Service
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
  getty@tty1.service             loaded active running Getty on tty1
  hermes-agent.service           loaded active running Hermes Agent Sovereign Service
  ModemManager.service           loaded active running Modem Manager
  multipathd.service             loaded active running Device-Mapper Multipath Device Controller
  NetworkManager.service         loaded active running Network Manager
  openclaw.service               loaded active running OpenClaw - A'Space Gateway Agent
  opencode.service               loaded active running OpenCode - A'Space Alternative Technician
  pm2-amadeus.service            loaded active running PM2 process manager
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
  user@1001.service              loaded active running User Manager for UID 1001
  wpa_supplicant.service         loaded active running WPA supplicant

Legend: LOAD   → Reflects whether the unit definition was properly loaded.
        ACTIVE → The high-level unit activation state, i.e. generalization of SUB.
        SUB    → The low-level unit activation state, values depend on unit type.

43 loaded units listed.
```

## 7. Docker — containers running

```
NAMES                                          IMAGE                                 STATUS
obsidian-web                                   lscr.io/linuxserver/obsidian:latest   Up About an hour
dokploy-postgres.1.l32potm3jm90vbnl5xj6yaqxt   postgres:16                           Up About an hour
dokploy-redis.1.brq9sefxg7y5ctyjajz02am52      redis:7                               Up About an hour
life-web-os-emergency                          0bae651970d6                          Up About an hour
supabase-db                                    supabase/postgres:15.8.1.085          Up About an hour (healthy)
```

## 8. Docker — Swarm services

```
ID             NAME                 MODE         REPLICAS   IMAGE                       PORTS
6d8hdpmbwngo   dokploy              replicated   0/0        dokploy/dokploy:v0.29.1     
vwv8hq5beuu7   dokploy-postgres     replicated   1/1        postgres:16                 
fe9t4uurtb6q   dokploy-redis        replicated   1/1        redis:7                     
npmfxw7lircb   life-web-os-qdw04z   replicated   0/0        life-web-os-qdw04z:latest   *:8005->3000/tcp
```

## 9. Tous les fichiers .md (Markdown docs A0/SDD/ADR)

```
/home/amadeus/.agents/skills/find-docs/SKILL.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/antigravity-code-executor/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/antigravity-remote-wsl/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/css-language-features/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/emmet/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/git-base/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/git/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/github-authentication/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/github/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/grunt/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/gulp/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/html-language-features/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/ipynb/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/jake/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/json-language-features/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/markdown-language-features/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/markdown-math/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/media-preview/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/merge-conflict/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/mermaid-chat-features/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/microsoft-authentication/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/ms-vscode.js-debug-companion/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/ms-vscode.js-debug-companion/SECURITY.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/ms-vscode.js-debug/readme.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/ms-vscode.vscode-js-profile-table/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/npm/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/php-language-features/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/references-view/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/search-result/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/simple-browser/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/terminal-suggest/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/terminal-suggest/dist/fig/README.md
/home/amadeus/.antigravity-server/bin/1.23.2-15487b3041e65228cae24980a3f796c905ef582c/extensions/typescript-language-features/README.md
/home/amadeus/.antigravity-server/extensions/anthropic.claude-code-2.1.122-linux-x64/README.md
/home/amadeus/.antigravity-server/extensions/anthropic.claude-code-2.1.122-linux-x64/resources/walkthrough/step1.md
/home/amadeus/.antigravity-server/extensions/anthropic.claude-code-2.1.122-linux-x64/resources/walkthrough/step2.md
/home/amadeus/.antigravity-server/extensions/anthropic.claude-code-2.1.122-linux-x64/resources/walkthrough/step3.md
/home/amadeus/.antigravity-server/extensions/anthropic.claude-code-2.1.122-linux-x64/resources/walkthrough/step4.md
/home/amadeus/.claude/agents/beth.md
/home/amadeus/.claude/agents/gsd-advisor-researcher.md
/home/amadeus/.claude/agents/gsd-ai-researcher.md
/home/amadeus/.claude/agents/gsd-assumptions-analyzer.md
/home/amadeus/.claude/agents/gsd-code-fixer.md
/home/amadeus/.claude/agents/gsd-code-reviewer.md
/home/amadeus/.claude/agents/gsd-codebase-mapper.md
/home/amadeus/.claude/agents/gsd-debug-session-manager.md
/home/amadeus/.claude/agents/gsd-debugger.md
/home/amadeus/.claude/agents/gsd-doc-classifier.md
/home/amadeus/.claude/agents/gsd-doc-synthesizer.md
/home/amadeus/.claude/agents/gsd-doc-verifier.md
/home/amadeus/.claude/agents/gsd-doc-writer.md
/home/amadeus/.claude/agents/gsd-domain-researcher.md
/home/amadeus/.claude/agents/gsd-eval-auditor.md
/home/amadeus/.claude/agents/gsd-eval-planner.md
/home/amadeus/.claude/agents/gsd-executor.md
/home/amadeus/.claude/agents/gsd-framework-selector.md
/home/amadeus/.claude/agents/gsd-integration-checker.md
/home/amadeus/.claude/agents/gsd-intel-updater.md
/home/amadeus/.claude/agents/gsd-nyquist-auditor.md
/home/amadeus/.claude/agents/gsd-pattern-mapper.md
/home/amadeus/.claude/agents/gsd-phase-researcher.md
/home/amadeus/.claude/agents/gsd-plan-checker.md
/home/amadeus/.claude/agents/gsd-planner.md
/home/amadeus/.claude/agents/gsd-project-researcher.md
/home/amadeus/.claude/agents/gsd-research-synthesizer.md
/home/amadeus/.claude/agents/gsd-roadmapper.md
/home/amadeus/.claude/agents/gsd-security-auditor.md
/home/amadeus/.claude/agents/gsd-ui-auditor.md
/home/amadeus/.claude/agents/gsd-ui-checker.md
/home/amadeus/.claude/agents/gsd-ui-researcher.md
/home/amadeus/.claude/agents/gsd-user-profiler.md
/home/amadeus/.claude/agents/gsd-verifier.md
/home/amadeus/.claude/agents/morty.md
/home/amadeus/.claude/agents/rick.md
/home/amadeus/.claude/agents/sovereign-amadeus.md
/home/amadeus/.claude/cache/changelog.md
/home/amadeus/.claude/get-shit-done/contexts/dev.md
/home/amadeus/.claude/get-shit-done/contexts/research.md
/home/amadeus/.claude/get-shit-done/contexts/review.md
/home/amadeus/.claude/get-shit-done/references/agent-contracts.md
/home/amadeus/.claude/get-shit-done/references/ai-evals.md
/home/amadeus/.claude/get-shit-done/references/ai-frameworks.md
/home/amadeus/.claude/get-shit-done/references/artifact-types.md
/home/amadeus/.claude/get-shit-done/references/autonomous-smart-discuss.md
/home/amadeus/.claude/get-shit-done/references/checkpoints.md
/home/amadeus/.claude/get-shit-done/references/common-bug-patterns.md
/home/amadeus/.claude/get-shit-done/references/context-budget.md
/home/amadeus/.claude/get-shit-done/references/continuation-format.md
/home/amadeus/.claude/get-shit-done/references/debugger-philosophy.md
/home/amadeus/.claude/get-shit-done/references/decimal-phase-calculation.md
/home/amadeus/.claude/get-shit-done/references/doc-conflict-engine.md
/home/amadeus/.claude/get-shit-done/references/domain-probes.md
/home/amadeus/.claude/get-shit-done/references/execute-mvp-tdd.md
/home/amadeus/.claude/get-shit-done/references/executor-examples.md
/home/amadeus/.claude/get-shit-done/references/few-shot-examples/plan-checker.md
/home/amadeus/.claude/get-shit-done/references/few-shot-examples/verifier.md
/home/amadeus/.claude/get-shit-done/references/gate-prompts.md
/home/amadeus/.claude/get-shit-done/references/gates.md
/home/amadeus/.claude/get-shit-done/references/git-integration.md
/home/amadeus/.claude/get-shit-done/references/git-planning-commit.md
/home/amadeus/.claude/get-shit-done/references/ios-scaffold.md
/home/amadeus/.claude/get-shit-done/references/mandatory-initial-read.md
/home/amadeus/.claude/get-shit-done/references/model-profile-resolution.md
/home/amadeus/.claude/get-shit-done/references/model-profiles.md
/home/amadeus/.claude/get-shit-done/references/mvp-concepts.md
/home/amadeus/.claude/get-shit-done/references/phase-argument-parsing.md
/home/amadeus/.claude/get-shit-done/references/planner-antipatterns.md
/home/amadeus/.claude/get-shit-done/references/planner-chunked.md
/home/amadeus/.claude/get-shit-done/references/planner-gap-closure.md
/home/amadeus/.claude/get-shit-done/references/planner-mvp-mode.md
/home/amadeus/.claude/get-shit-done/references/planner-reviews.md
/home/amadeus/.claude/get-shit-done/references/planner-revision.md
/home/amadeus/.claude/get-shit-done/references/planner-source-audit.md
/home/amadeus/.claude/get-shit-done/references/planning-config.md
/home/amadeus/.claude/get-shit-done/references/project-skills-discovery.md
/home/amadeus/.claude/get-shit-done/references/questioning.md
/home/amadeus/.claude/get-shit-done/references/revision-loop.md
/home/amadeus/.claude/get-shit-done/references/scout-codebase.md
/home/amadeus/.claude/get-shit-done/references/skeleton-template.md
/home/amadeus/.claude/get-shit-done/references/sketch-interactivity.md
/home/amadeus/.claude/get-shit-done/references/sketch-theme-system.md
/home/amadeus/.claude/get-shit-done/references/sketch-tooling.md
/home/amadeus/.claude/get-shit-done/references/sketch-variant-patterns.md
/home/amadeus/.claude/get-shit-done/references/spidr-splitting.md
/home/amadeus/.claude/get-shit-done/references/tdd.md
/home/amadeus/.claude/get-shit-done/references/thinking-models-debug.md
/home/amadeus/.claude/get-shit-done/references/thinking-models-execution.md
/home/amadeus/.claude/get-shit-done/references/thinking-models-planning.md
/home/amadeus/.claude/get-shit-done/references/thinking-models-research.md
/home/amadeus/.claude/get-shit-done/references/thinking-models-verification.md
/home/amadeus/.claude/get-shit-done/references/thinking-partner.md
/home/amadeus/.claude/get-shit-done/references/ui-brand.md
/home/amadeus/.claude/get-shit-done/references/universal-anti-patterns.md
/home/amadeus/.claude/get-shit-done/references/user-profiling.md
/home/amadeus/.claude/get-shit-done/references/user-story-template.md
/home/amadeus/.claude/get-shit-done/references/verification-overrides.md
/home/amadeus/.claude/get-shit-done/references/verification-patterns.md
/home/amadeus/.claude/get-shit-done/references/verify-mvp-mode.md
/home/amadeus/.claude/get-shit-done/references/workstream-flag.md
/home/amadeus/.claude/get-shit-done/references/worktree-path-safety.md
/home/amadeus/.claude/get-shit-done/templates/AI-SPEC.md
/home/amadeus/.claude/get-shit-done/templates/DEBUG.md
/home/amadeus/.claude/get-shit-done/templates/README.md
/home/amadeus/.claude/get-shit-done/templates/SECURITY.md
/home/amadeus/.claude/get-shit-done/templates/UAT.md
/home/amadeus/.claude/get-shit-done/templates/UI-SPEC.md
/home/amadeus/.claude/get-shit-done/templates/VALIDATION.md
/home/amadeus/.claude/get-shit-done/templates/claude-md.md
/home/amadeus/.claude/get-shit-done/templates/codebase/architecture.md
/home/amadeus/.claude/get-shit-done/templates/codebase/concerns.md
/home/amadeus/.claude/get-shit-done/templates/codebase/conventions.md
/home/amadeus/.claude/get-shit-done/templates/codebase/integrations.md
/home/amadeus/.claude/get-shit-done/templates/codebase/stack.md
/home/amadeus/.claude/get-shit-done/templates/codebase/structure.md
/home/amadeus/.claude/get-shit-done/templates/codebase/testing.md
/home/amadeus/.claude/get-shit-done/templates/context.md
/home/amadeus/.claude/get-shit-done/templates/continue-here.md
/home/amadeus/.claude/get-shit-done/templates/copilot-instructions.md
/home/amadeus/.claude/get-shit-done/templates/debug-subagent-prompt.md
/home/amadeus/.claude/get-shit-done/templates/dev-preferences.md
/home/amadeus/.claude/get-shit-done/templates/discovery.md
/home/amadeus/.claude/get-shit-done/templates/discussion-log.md
/home/amadeus/.claude/get-shit-done/templates/milestone-archive.md
/home/amadeus/.claude/get-shit-done/templates/milestone.md
/home/amadeus/.claude/get-shit-done/templates/phase-prompt.md
/home/amadeus/.claude/get-shit-done/templates/planner-subagent-prompt.md
/home/amadeus/.claude/get-shit-done/templates/project.md
/home/amadeus/.claude/get-shit-done/templates/requirements.md
/home/amadeus/.claude/get-shit-done/templates/research-project/ARCHITECTURE.md
/home/amadeus/.claude/get-shit-done/templates/research-project/FEATURES.md
/home/amadeus/.claude/get-shit-done/templates/research-project/PITFALLS.md
/home/amadeus/.claude/get-shit-done/templates/research-project/STACK.md
/home/amadeus/.claude/get-shit-done/templates/research-project/SUMMARY.md
/home/amadeus/.claude/get-shit-done/templates/research.md
/home/amadeus/.claude/get-shit-done/templates/retrospective.md
/home/amadeus/.claude/get-shit-done/templates/roadmap.md
/home/amadeus/.claude/get-shit-done/templates/spec.md
/home/amadeus/.claude/get-shit-done/templates/state.md
/home/amadeus/.claude/get-shit-done/templates/summary-complex.md
/home/amadeus/.claude/get-shit-done/templates/summary-minimal.md
/home/amadeus/.claude/get-shit-done/templates/summary-standard.md
/home/amadeus/.claude/get-shit-done/templates/summary.md
/home/amadeus/.claude/get-shit-done/templates/user-profile.md
/home/amadeus/.claude/get-shit-done/templates/user-setup.md
/home/amadeus/.claude/get-shit-done/templates/verification-report.md
/home/amadeus/.claude/get-shit-done/workflows/add-backlog.md
/home/amadeus/.claude/get-shit-done/workflows/add-phase.md
/home/amadeus/.claude/get-shit-done/workflows/add-tests.md
/home/amadeus/.claude/get-shit-done/workflows/add-todo.md
/home/amadeus/.claude/get-shit-done/workflows/ai-integration-phase.md
/home/amadeus/.claude/get-shit-done/workflows/analyze-dependencies.md
/home/amadeus/.claude/get-shit-done/workflows/audit-fix.md
/home/amadeus/.claude/get-shit-done/workflows/audit-milestone.md
/home/amadeus/.claude/get-shit-done/workflows/audit-uat.md
/home/amadeus/.claude/get-shit-done/workflows/autonomous.md
/home/amadeus/.claude/get-shit-done/workflows/check-todos.md
/home/amadeus/.claude/get-shit-done/workflows/cleanup.md
/home/amadeus/.claude/get-shit-done/workflows/code-review-fix.md
/home/amadeus/.claude/get-shit-done/workflows/code-review.md
/home/amadeus/.claude/get-shit-done/workflows/complete-milestone.md
```

## 10. Configs critiques (.json/.yml/.sh dans /srv/aspace)

```
/srv/aspace/.agent-init.sh
/srv/aspace/.claude/settings.json
/srv/aspace/.env
/srv/aspace/.openclaw/workspace-state.json
/srv/aspace/.openharness/autopilot/autopilot_policy.yaml
/srv/aspace/.openharness/autopilot/registry.json
/srv/aspace/.openharness/autopilot/release_policy.yaml
/srv/aspace/.openharness/autopilot/verification_policy.yaml
/srv/aspace/00_ORIGIN/personalities/personalities-index.json
/srv/aspace/00_ORIGIN/ricks-verse-config-backup.json
/srv/aspace/00_ORIGIN/scripts/kernel-boot.sh
/srv/aspace/30_MEMORY_CORE/LLM_Wiki/LLM Wiki/.obsidian/app.json
/srv/aspace/30_MEMORY_CORE/LLM_Wiki/LLM Wiki/.obsidian/appearance.json
/srv/aspace/30_MEMORY_CORE/LLM_Wiki/LLM Wiki/.obsidian/core-plugins.json
/srv/aspace/30_MEMORY_CORE/LLM_Wiki/LLM Wiki/.obsidian/graph.json
/srv/aspace/30_MEMORY_CORE/LLM_Wiki/LLM Wiki/.obsidian/workspace.json
/srv/aspace/30_MEMORY_CORE/system/swarm-state-20260428.json
/srv/aspace/40_SKILLS/registry.json
/srv/aspace/90_SETUP/aspace-status.sh
/srv/aspace/90_SETUP/bootstrap.sh
/srv/aspace/90_SETUP/install-agents.sh
/srv/aspace/90_SETUP/install-runtime.sh
/srv/aspace/90_SETUP/install-syncthing.sh
/srv/aspace/90_SETUP/launch/install.sh
/srv/aspace/90_SETUP/launch/status.sh
/srv/aspace/90_SETUP/launch/watchers/dlq-watcher.sh
/srv/aspace/90_SETUP/launch/watchers/inbox-watcher.sh
/srv/aspace/alerts/dedup_state.json
/srv/aspace/archive/paperclip-deprecated-20260513/.claude/settings.json
/srv/aspace/archive/paperclip-deprecated-20260513/.env
/srv/aspace/archive/paperclip-deprecated-20260513/Dockerfile
/srv/aspace/archive/paperclip-deprecated-20260513/START_PAPERCLIP.sh
/srv/aspace/archive/paperclip-deprecated-20260513/cli/package.json
/srv/aspace/archive/paperclip-deprecated-20260513/cli/tsconfig.json
/srv/aspace/archive/paperclip-deprecated-20260513/config.json
/srv/aspace/archive/paperclip-deprecated-20260513/docker/Dockerfile.onboard-smoke
/srv/aspace/archive/paperclip-deprecated-20260513/docker/docker-compose.quickstart.yml
/srv/aspace/archive/paperclip-deprecated-20260513/docker/docker-compose.untrusted-review.yml
/srv/aspace/archive/paperclip-deprecated-20260513/docker/docker-compose.yml
/srv/aspace/archive/paperclip-deprecated-20260513/docker/openclaw-smoke/Dockerfile
/srv/aspace/archive/paperclip-deprecated-20260513/docker/untrusted-review/Dockerfile
/srv/aspace/archive/paperclip-deprecated-20260513/docs/docs.json
/srv/aspace/archive/paperclip-deprecated-20260513/evals/promptfoo/promptfooconfig.yaml
/srv/aspace/archive/paperclip-deprecated-20260513/package.json
/srv/aspace/archive/paperclip-deprecated-20260513/packages/adapter-utils/package.json
/srv/aspace/archive/paperclip-deprecated-20260513/packages/adapter-utils/tsconfig.json
/srv/aspace/archive/paperclip-deprecated-20260513/packages/db/package.json
/srv/aspace/archive/paperclip-deprecated-20260513/packages/db/tsconfig.json
/srv/aspace/archive/paperclip-deprecated-20260513/packages/mcp-server/package.json
/srv/aspace/archive/paperclip-deprecated-20260513/packages/mcp-server/tsconfig.json
/srv/aspace/archive/paperclip-deprecated-20260513/packages/shared/package.json
/srv/aspace/archive/paperclip-deprecated-20260513/packages/shared/tsconfig.json
/srv/aspace/archive/paperclip-deprecated-20260513/pm2-start.sh
/srv/aspace/archive/paperclip-deprecated-20260513/pnpm-lock.yaml
/srv/aspace/archive/paperclip-deprecated-20260513/pnpm-workspace.yaml
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/backup-db.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/build-npm.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/clean-onboard-git.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/clean-onboard-npm.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/clean-onboard-ref.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/create-github-release.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/docker-build-test.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/docker-entrypoint.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/docker-onboard-smoke.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/kill-agent-browsers.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/kill-dev.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/paperclip-issue-update.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/prepare-server-ui-dist.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/provision-worktree.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/release-lib.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/release.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/rollback-latest.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/smoke/openclaw-docker-ui.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/smoke/openclaw-gateway-e2e.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/smoke/openclaw-join.sh
/srv/aspace/archive/paperclip-deprecated-20260513/scripts/smoke/openclaw-sse-standalone.sh
/srv/aspace/archive/paperclip-deprecated-20260513/server/.env
/srv/aspace/archive/paperclip-deprecated-20260513/server/package.json
/srv/aspace/archive/paperclip-deprecated-20260513/server/tsconfig.json
/srv/aspace/archive/paperclip-deprecated-20260513/slash-commands.json
/srv/aspace/archive/paperclip-deprecated-20260513/start.sh
/srv/aspace/archive/paperclip-deprecated-20260513/state/rick-c137.json
/srv/aspace/archive/paperclip-deprecated-20260513/tsconfig.base.json
/srv/aspace/archive/paperclip-deprecated-20260513/tsconfig.json
/srv/aspace/archive/paperclip-deprecated-20260513/ui/components.json
/srv/aspace/archive/paperclip-deprecated-20260513/ui/package.json
/srv/aspace/archive/paperclip-deprecated-20260513/ui/tsconfig.json
/srv/aspace/dashboard/package-lock.json
/srv/aspace/dashboard/package.json
/srv/aspace/dashboard/tsconfig.json
/srv/aspace/docs/autopilot/snapshot.json
/srv/aspace/docs/personalities/personalities-index.json
/srv/aspace/docs/ricks-verse-config-backup.json
/srv/aspace/docs/scripts/kernel-boot.sh
/srv/aspace/hermes-workspace/.devcontainer/devcontainer.json
/srv/aspace/hermes-workspace/.github/workflows/ci.yml
/srv/aspace/hermes-workspace/.github/workflows/docker-publish.yml
/srv/aspace/hermes-workspace/.github/workflows/security.yml
/srv/aspace/hermes-workspace/.vscode/settings.json
/srv/aspace/hermes-workspace/Dockerfile
```

## 11. PM2 process list

```
┌────┬───────────┬─────────────┬─────────┬─────────┬──────────┬────────┬──────┬───────────┬──────────┬──────────┬──────────┬──────────┐
│ id │ name      │ namespace   │ version │ mode    │ pid      │ uptime │ ↺    │ status    │ cpu      │ mem      │ user     │ watching │
└────┴───────────┴─────────────┴─────────┴─────────┴──────────┴────────┴──────┴───────────┴──────────┴──────────┴──────────┴──────────┘
```

## 12. Archive folder (preserved historical)

```
total 12K
drwxr-xr-x  3 root    root    4.0K May 14 05:21 .
drwxr-xr-x 30 amadeus amadeus 4.0K May 14 05:21 ..
drwxr-xr-x 22 amadeus amadeus 4.0K May 12 20:20 paperclip-deprecated-20260513
```

---
*Cartography générée le 2026-05-14T18:24:32Z*
