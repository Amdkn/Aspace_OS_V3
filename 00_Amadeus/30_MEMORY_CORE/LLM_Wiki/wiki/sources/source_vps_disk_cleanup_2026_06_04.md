---
source: aspace-vps disk audit
date: 2026-06-04
type: source
domain: 05_IT / VPS Operations
tags: [#VPS, #DiskUsage, #Docker, #Hostinger, #AspaceDashboard]
status: ACTIVE
---

# VPS Disk Cleanup Source - 2026-06-04

## Executive Summary

The VPS disk pressure was initially labeled as "Supabase disk usage", but direct evidence showed that Supabase is not the primary disk driver.

Actual pressure sources:

- `/var/lib/containerd`: about 26G
- `/home/amadeus/.cache`: about 8G
- `/home/amadeus/.npm`: about 6.3G
- `/home/amadeus/.git`: about 3.7G
- `/srv/aspace/supabase`: about 1.5G

The cleanup policy is conservative: remove only regenerable caches and inactive Docker objects. Do not delete Docker volumes, database data, Supabase runtime data, or Hostinger snapshots from this workflow.

## Evidence

- Hostinger panel showed root disk around 75G / 100G.
- `df -hT /` on the VPS showed about 76G used on a 96G root filesystem.
- `du -xhd1 /` showed `/home` around 33G and `/var` around 31G.
- `du -xhd1 /var/lib` showed `/var/lib/containerd` around 26G and `/var/lib/docker` around 1.1G.
- `docker system df` showed Docker images around 27.7G, but only about 1.7G immediately reclaimable by Docker's own accounting.
- `/srv/aspace/supabase` was around 1.5G, so Supabase should not be treated as the main disk cleanup target without newer evidence.

## Preserved Decisions

- Keep Supabase in official Docker Compose under `/srv/aspace/supabase/docker`.
- Keep A'Space Supabase partitions under `/srv/aspace/services/supabase`.
- Keep A'Space Dashboard as the governance console.
- Maintain monitoring-first policy: no automatic prune, restart, scale, or repair without A0 approval.

## Cleanup Boundaries

Allowed in the first cleanup pass:

- User caches that tools can regenerate.
- npm cache and npx transient cache.
- uv, Go build, Playwright, Puppeteer, Camoufox, and Claude CLI Node cache.
- apt package cache.
- journald vacuum to a bounded size.
- stopped Docker containers.
- dangling Docker images.
- clearly inactive Docker images with zero active containers.

Forbidden in this pass:

- `docker volume prune`
- `docker system prune --volumes`
- deleting Supabase database volumes or data
- deleting Dokploy volumes
- deleting Hostinger backups or snapshots
- deleting unknown project source directories

## Residual Risk

Some caches may require reinstall/download on next use. Removing old Docker images can slow rollback if the same image is needed again, but active containers and volumes are preserved.

## Execution Result

Cleanup executed after documentation.

Result:

- Root disk improved from about 79% to about 62-63%.
- Used space improved from about 76G to about 59-60G.
- Docker images reclaimable improved from about 4.17G to 0B.
- Docker containers remain active where required.
- Docker volumes were not pruned.
- Supabase remains running with the known health debt only: `analytics`, `realtime`, `supavisor`.

Cleaned:

- npm cache and transient npx cache
- uv cache
- Go build/test cache
- Playwright, Puppeteer, Camoufox, Claude CLI Node caches
- apt cache
- journald archive down to bounded retention
- stopped Docker containers
- dangling/inactive Docker images including old rollback images with zero active containers

Not cleaned:

- Docker volumes
- Supabase data
- Dokploy data
- Hostinger backups or snapshots
- project source directories
