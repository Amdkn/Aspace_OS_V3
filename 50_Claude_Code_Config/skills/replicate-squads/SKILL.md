---
name: replicate-squads
description: >
  Replicate the canonical Marvel/DC squad member folders (0N_<Member>_<Role>) from the Jerry
  Business Pulse domains (30_Business_OS/00_Jerry_Business_Pulse/04_Business_Domains/<domain>/) into
  every project's B3 execution layer (30_Business_OS/10_Projects/<project>/_doctrine/B3_Warp_Core_Execution/<domain>/).
  USE THIS SKILL whenever the user (A0) wants to "replicate the squads", "propagate the Marvel roster
  into the projects", "sync the B3 squad folders", "add the squad members to <project>", or after the
  Jerry Business Pulse roster changes and the per-project B3 execution workspaces need to catch up.
  It is ADD-ONLY (never overwrites existing B3 swarm files / JTBD packets), reads the source roster
  DYNAMICALLY (so it always reflects the current canon), writes project-specific README stubs that
  crosslink to the canon role (Notion AGENT_REGISTRY_DB via Business Pulse) + the J01 area doctrine,
  and writes through the _doctrine junctions (real paths stay < 260 MAX_PATH). Re-run it any time the
  roster evolves — it is idempotent (skips members that already exist).
---

# Replicate Squads — Business Pulse → Project B3 Warp Cores

## Why
A'Space has two homes for the Marvel/DC squads:
- **Canon roster (source of truth)** : `30_Business_OS/00_Jerry_Business_Pulse/04_Business_Domains/<domain>/0N_<Member>_<Role>/`
  — members + roles aligned to **ADR-CANON-001** (Notion `AGENT_REGISTRY_DB`, `Specialty` = role).
- **Per-project execution** : each project under `30_Business_OS/10_Projects/<project>/_doctrine/B3_Warp_Core_Execution/<domain>/`
  is where that squad member actually executes JTBD / proofs / handoffs **for that project**.

This skill keeps the second in sync with the first: every project gets the full squad member folders,
so the B3 execution layer mirrors the canon roster — without ever touching the existing swarm config
(`00_B3_SWARM_CONFIG.md`, `01_B3_AGENT_ROSTER.md`, JTBD packets).

## How
Run the bundled script (idempotent, ADD-only):
```bash
powershell -NoProfile -ExecutionPolicy Bypass -File "<this-skill>/scripts/replicate_squads.ps1"
```
It:
1. Reads the 8 source domains + their `0N_<Member>_<Role>` subfolders **dynamically** from Business Pulse.
2. For each project in `10_Projects` that has a `_doctrine/B3_Warp_Core_Execution`, ensures every domain
   folder exists, then creates any missing member folder + a project-specific `README.md`.
3. Skips members that already exist (safe to re-run after roster edits).

## Hard rules
- **ADD-ONLY** — never delete or overwrite existing B3 files (swarm config, rosters, JTBD packets, proofs).
- **Canon source = Business Pulse** (which mirrors Notion `AGENT_REGISTRY_DB` per ADR-CANON-001). To change
  membership/roles, edit Business Pulse first (or re-pull from Notion), THEN run this skill.
- **Write via the `_doctrine` junction paths** (real deep paths stay < 260 MAX_PATH; folders + README only).
- After running, report the per-project member count (should equal the canon total — currently 53:
  Growth 6 · Sales 6 · Product 7 · Ops 4 · IT 6 · Finance 6 · People 8 · Legal 10).

## Scope notes
- Targets all projects that have a `B3_Warp_Core_Execution` (currently solaris, omk, abc, rilcot, alikaly, marina).
- To pull fresh roles from Notion before replicating, use `notion-search` with
  `data_source_url=collection://e9f082b5-1099-4cf6-943c-0fa7fdb0fc68` (the 8 squad pages carry full rosters),
  update Business Pulse, then run this skill. (The `query-data-source` API connector returns invalid_request_url —
  use `notion-search data_source_url` instead.)
