---
source: aspace-vps app decommission
date: 2026-06-04
type: source
domain: 05_IT / VPS Operations
tags: [#VPS, #Docker, #Obsidian, #Multica, #PaperclipAI, #Cleanup]
status: ACTIVE
---

# VPS App Decommission - Obsidian, Multica, Paperclip AI - 2026-06-04

## Executive Summary

A0 requested removal of Obsidian, Multica, and Paperclip AI from `aspace-vps`.

This decommission is intentionally scoped to those apps only. Hermes, Dokploy, Supabase, Caddy, and A'Space Governance Dashboard must remain active.

## Evidence

Obsidian:

- Systemd unit: `/etc/systemd/system/obsidian.service`
- Startup script: `/home/amadeus/.local/bin/obsidian-start.sh`
- Docker container: `obsidian-web`
- Docker image: `lscr.io/linuxserver/obsidian:latest`
- Config/data path: `/home/amadeus/.config/obsidian-web`
- Logs: `/srv/aspace/logs/obsidian.log*`
- Supporting local CLI paths: `/home/amadeus/CLI-Anything/obsidian`, `/home/amadeus/CLI-Anything/skills/cli-anything-obsidian`

Multica:

- Local source/runtime path: `/home/amadeus/multica`
- User config/state: `/home/amadeus/.multica`
- Runtime marker path: `/home/amadeus/20_RUNTIME/multica`
- Binary path: `/home/amadeus/50_SERVICES/bin/multica`
- Config: `/home/amadeus/multica.yml`
- Traefik dynamic config: `/etc/dokploy/traefik/dynamic/multica.yml`
- Docker volumes: `multica_backend_uploads`, `multica_pgdata`
- Docker network: `multica_default`
- No active Multica containers were found at decommission time.

Paperclip AI:

- No active Docker container, image, volume, systemd unit, or PM2 process was found.
- Residual files found:
  - `/home/amadeus/.gemini/antigravity/brain/.../paperclip_validation_analysis.md*`
  - `/etc/caddy/Caddyfile.bak.20260515_paperclip-banishment`

## Preserved Decisions

- Do not touch Hermes Agent, Hermes Workspace, Dokploy, Supabase, or A'Space Dashboard.
- Do not run broad `docker volume prune`.
- Remove only volumes explicitly named for Multica.
- Remove Obsidian container/image/config because A0 explicitly requested deletion.
- Keep `.obsidian` folders inside Memory Core untouched unless A0 explicitly asks to delete Obsidian vault metadata from the knowledge base. Those folders are content metadata, not the VPS app runtime.

## What Is Obsolete

- Obsidian web runtime on VPS port 3000.
- Multica local runtime/source artifacts and old Traefik route.
- Paperclip AI residual analysis/banishment artifacts.

## Archive Decision

Proceed with direct decommission. No runtime backup is created because A0 requested deletion and the target apps are non-canonical for the current Hermes/A'Space VPS runtime.

## Residual Risk

- Removing Obsidian frees the large image and port 3000 but removes the hosted Obsidian UI.
- Removing `multica_pgdata` deletes any leftover Multica Postgres data.
- Paperclip AI appears already decommissioned; only residual metadata is removed.
- Docker/containerd may not release all space until image layers are no longer referenced by active containers.

## Execution Result

Decommission executed after documentation.

Removed:

- `obsidian.service`
- `obsidian-web` container
- `lscr.io/linuxserver/obsidian:latest` image
- Obsidian startup script, config directory, logs, setup unit copies, and AppArmor profile
- Multica local paths, binary, config, Traefik dynamic config
- Docker volumes `multica_backend_uploads` and `multica_pgdata`
- Docker network `multica_default`
- Paperclip AI residual analysis files and old Caddy backup

Preserved:

- Hermes services
- Hermes Workspace
- Dokploy stack
- Supabase Compose stack
- A'Space Dashboard
- Memory Core `.obsidian` vault metadata
- Hermes note-taking skills that reference Obsidian as documentation/capability metadata rather than the deleted VPS app runtime

Validation:

- No Obsidian, Multica, or Paperclip runtime artifacts remained in Docker images, containers, volumes, networks, or systemd.
- A'Space Dashboard, Hermes Gateway, Hermes Dashboard, Hermes Workspace, and Dokploy local routes returned 200.
- Dokploy Swarm services remained `1/1`.
- Supabase remained 13/13 running with the known 3 unhealthy healthchecks.
- Root disk improved to about 55-56%.
