---
source: amadeus@aspace-vps → C:\Users\amado\
date: 2026-06-17T04:35:00Z
type: archive-handoff
domain: L0_Tech_OS
tags: [#VPS #archive #TGZ #extraction #D6-lessons #pre-pivot]
status: COMPLETE
---

# VPS → Local Windows Archive — 2026-06-17

**Mission** : archiver le VPS (post-pivot phase 1 = Vercel+SupabaseCloud+Coolify+N8N, kill bare-metal) et extraire localement sur `C:\Users\amado\`.

## D1 receipts (5 vérifications)

| # | Mesure | Valeur | Statut |
|---|---|---|---|
| 1 | TGZ size VPS | 827 876 986 B (789 MB) | ✅ |
| 1 | TGZ size local | 827 876 986 B (789 MB) | ✅ identique |
| 2 | md5 VPS | `d7293f5712c289546fa35d15145d7bc1` | ✅ |
| 2 | md5 local | `d7293f5712c289546fa35d15145d7bc1` | ✅ **MATCH** |
| 3 | gzip -t VPS | rc=0 | ✅ valide |
| 3 | gzip -t local | rc=0 | ✅ valide |
| 4 | Files extracted | **48 140** | ✅ |
| 5 | Total size extracted | **1.3 GB** | ✅ |

## Localisation

- **TGZ** : `C:\Users\amado\vps-archive-2026-06-17.tgz` (789 MB)
- **Extracted** : `C:\Users\amado\vps-archive-2026-06-17\` (1.3 GB, 48 140 fichiers)
- **VPS source** : `/tmp/vps-archive.tgz` (peut être supprimé après validation)

## Arborescence extraite

```
C:/Users/amado/vps-archive-2026-06-17/
├── etc/
│   ├── caddy/                          # vhosts + certs refs
│   └── systemd/                        # 48 services
├── home/amadeus/
│   ├── .claude/                        # ✅ CLI config + memory + skills
│   ├── .config/                        # ✅
│   ├── .hermes/                        # ✅ (gateway config, sans data/checkpoints exclus)
│   ├── .ssh/                           # ✅ authorized_keys (sans .bash_history exclus)
│   └── 50_SERVICES/                    # ✅
└── srv/aspace/
    ├── 00_ORIGIN/                      # ✅
    ├── 10_FORGE/                       # ✅
    ├── 20_RUNTIME/                     # ✅
    ├── 30_MEMORY_CORE/                 # ✅ Memory Core canon
    ├── 40_SKILLS/                      # ✅
    ├── 90_SETUP/                       # ✅
    ├── dashboard/                      # ✅ CEO Dashboard Next.js (sans node_modules)
    ├── hermes-workspace/               # ✅ (sans node_modules)
    ├── main/                           # ✅
    ├── services/                       # ✅
    ├── supabase/                       # ✅ (sans docker/volumes/db/data = root-owned)
    ├── vault/                          # ✅
    └── web/                            # ✅
```

## Excludes appliqués (D6 noise filter)

| Pattern | Raison |
|---|---|
| `node_modules` | Reconstructible via `npm install` (1-2 GB typiquement) |
| `.git/objects`, `.git/lfs`, `.git/logs`, `.git/refs`, `.git/hooks`, `.git/info` | Recreatable, source canon = `.claude/memory/wiki` |
| `dist`, `build`, `.next`, `.nuxt` | Build artifacts |
| `.cache`, `.npm`, `.nvm` | User-level caches |
| `venv_litellm` | Python venv recréable |
| `paperclip-deprecated-20260513` | Archive legacy (no-hard-delete respecté) |
| `__pycache__`, `.pytest_cache`, `.mypy_cache`, `.ruff_cache` | Python caches |
| `ms-playwright`, `ms-playwright-go` | Browser binaries, ~300 MB |
| `.claude/{projects,file-history,worktrees,plugins,remote,backups,session-data}` | Caches CLI, archives sessions |
| `_TRASH`, `_ARCHIVE` | Doctrine no-hard-delete (déjà archivés ailleurs) |
| `go-build`, `go/pkg`, `.cargo/registry`, `site-packages` | Toolchain caches |

## D6 root causes identifiés (3 leçons à appliquer aux runs suivants)

### 1. Detached tar via `( cmd & )` subshell > setsid nohup

**Bug** : `setsid nohup bash -c "..." &` n'a PAS survécu à un TaskStop SSH mid-build. Le setsid a été créé dans la même session SSH, donc même controlling terminal.

**Fix** : pattern `( cmd < /dev/null > log 2>&1 & disown )` = subshell double-fork qui détache complètement le process du parent shell. Quand SSH ferme, le grand-parent = init (PID 1), donc survit.

```bash
ssh amadeus@vps '( tar -czf /tmp/x.tgz <excludes> <dirs> \
  < /dev/null > /tmp/build.log 2>&1 \
  && gzip -t /tmp/x.tgz && md5sum /tmp/x.tgz >> /tmp/build.log \
  && echo DONE >> /tmp/build.log \
  || echo FAILED >> /tmp/build.log ) & disown'
```

### 2. Toujours `pkill -9 -f 'tar -czf <path>'` AVANT relance

**Bug** : un tar précédent (PID 3772181) du compact précédent était encore vivant quand le nouveau tar (PID 3799300) a été lancé. Les 2 ont écrit dans le même `/tmp/vps-archive.tgz` = corruption garantie (deux writers sur le même FD).

**Fix** : à chaque reprise de build, `pkill -9 -f 'tar -czf /tmp/vps-archive'` PUIS `rm -f /tmp/vps-archive.tgz` PUIS relancer.

### 3. Git Bash Windows : `/c/...` PAS `C:/...`

**Bug** : `tar -xzf C:/Users/amado/...` → `tar: Cannot connect to C: resolve failed` (Git Bash interprète `C:` comme un hostname à résoudre).

**Fix** : toujours `/c/Users/amado/...` en Git Bash sur Windows (POSIX path style).

## Permission denied (perte assumée, non-bloquant)

| Path | Owner | Impact |
|---|---|---|
| `/srv/aspace/supabase/docker/volumes/db/data` | root:postgres (PG data) | Aucun — DB data non-canon, à migrer vers Supabase Cloud |
| `/var/lib/caddy/.local/share/caddy` | caddy:caddy (TLS certs cache) | Aucun — Caddy régénère via LE ACME |

## VPS dirs absents (skipped par tar, pas d'erreur)

- `/home/amadeus/agent-os` (n'existe pas)
- `/home/amadeus/projects` (n'existe pas)
- `/home/amadeus/work` (n'existe pas)

## À faire après (post-archive)

1. **A0** : vérifier visuellement `C:\Users\amado\vps-archive-2026-06-17\` que le canon est complet
2. **A0** : supprimer `/tmp/vps-archive.tgz` sur VPS (libère 789 MB sur /tmp)
3. **A0** : lancer Phase 1 Business OS pivot (handoff `handoff_business_os_resumption_2026-06-16.md`) — VPS peut être wiped après validation archive
4. **Anti-amnesia** : 1 ligne ajoutée à MEMORY.md topic table ligne 35 + cette handoff file
