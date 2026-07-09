---
id: SUMMER_01_CEOS_DESKTOP
layer: L2-Business-Pulse
status: PHASE_1_SKELETON
created: 2026-06-07
parent_jerry: J01_Jerry_Prime_LD01_Business
project_slug: ceo-desktop
project_kind: CEO_Command_Center
mode: Matryoshka_Dashboard
adr_anchors:
  - ADR-FWK-021
  - ADR-INFRA-002
  - ADR-INFRA-003
---

# README — CEO's Desktop

> **A0 routeur** for the `ceo-desktop` project.
> Doctrine lives in `_doctrine/`. This file is a pointer, not a duplicate.

---

## Role

**CEO's Desktop** is the A0 CEO command center for business operations. It is not a product, not a service, not a revenue line. It is the **runtime** through which Amadeus observes, decides, and steers the 8 SOB domains and 8 B3 squads.

**Doctrine** (B1 direction, B2 domain DoD, B3 JTBD): `_doctrine/`
**Project-scoped rules** (addendum to global CLAUDE.md): `CLAUDE.md`
**Handoff relays** (stubs Phase 1): `handoffs/`
**Build-bearing apps** (placeholder Phase 1): `apps/`

## Quick Links

### Doctrine (read first)
- `_doctrine/SUMMERS_VERSE_MANIFEST.md` — B1 cockpit, north star, ICP variants
- `_doctrine/B1_Summer_Direction/00_B1_DIRECTION_INDEX.md` — B1 direction index
- `_doctrine/B2_Business_Domains/00_AAAS_DOMAIN_DEVELOPMENT_MAP.md` — B2 domain map
- `_doctrine/B2_Business_Domains/0X_<Domain>_<Squad>/` — per-domain doctrine (8 folders)

### Relays
- `handoffs/Beth_Alignment_Log.md` — Beth's alignment channel (decisions, vetoes)
- `handoffs/Morty_Global_Queue.md` — Morty's execution channel (Context Packs, dry-runs)
- `handoffs/Sunday_Uplink_Protocols.md` — Sunday's weekly uplink (cadence checkpoint)

### Boundary Notes
- `area_junction_placeholder.md` — Spock/Areas counterpart status (deferred to Phase 2)
- `CLAUDE.md` — project-scoped addendum to global CLAUDE.md

## Doctrine Summary

The CEO's Desktop follows three layered laws:

1. **Matryoshka** (ADR-INFRA-003) — Life Wheel > Business Wheel > Domain Wheel > Rock Wheel. The right layer surfaces to A0 at the right cadence.
2. **Repo-Home Junction** (ADR-INFRA-002) — doctrine lives long, code lives short. The `_doctrine/` folder is the home; future `apps/<role>/` homes build against it.
3. **Canon Tripartite** (ADR-FWK-021) — B1 direction → B2 domain DoD → B3 jobs to be done, with explicit handoffs and proof paths.

## The 8 SOB Operating Modes

Each B2 domain has a B3 squad lead and a cadence:

| # | B2 Domain | B3 Squad | Cadence |
|---|-----------|----------|---------|
| 1 | Growth | Superman / Guardians | Weekly |
| 2 | Sales | Martian Manhunter / Illuminati | Weekly |
| 3 | Product | Flash / Avengers | Weekly |
| 4 | Ops | Batman / Fantastic Four | Bi-weekly |
| 5 | IT | Cyborg / Kang Dynasty | Daily |
| 6 | Finance | Wonder Woman / Thunderbolts | Monthly |
| 7 | People | Green Lantern / X-Men | Monthly |
| 8 | Legal | Aquaman / Eternals | Quarterly |

See `_doctrine/SUMMERS_VERSE_MANIFEST.md` § ICP Variants for the full table.

## Status: PHASE_1_SKELETON

This project is in **Phase 1** (skeleton). The doctrine depth is in place; the build-bearing surface and the Spock/Areas junction are intentionally deferred.

**What's present**:
- B1 direction manifest (`_doctrine/SUMMERS_VERSE_MANIFEST.md`)
- B1 direction index (`_doctrine/B1_Summer_Direction/00_B1_DIRECTION_INDEX.md`)
- B2 domain development map (`_doctrine/B2_Business_Domains/00_AAAS_DOMAIN_DEVELOPMENT_MAP.md`)
- 8 B2 domain folders (`_doctrine/B2_Business_Domains/0X_*`)
- Project-scoped CLAUDE.md addendum (this folder)
- 3 handoff relay stubs (`handoffs/`)
- `apps/` placeholder (`.gitkeep`)

**What's intentionally absent in Phase 1**:
- No `apps/<role>/` build-bearing homes (deferred to Phase 2)
- No Spock/Areas junction in `20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/` (see `area_junction_placeholder.md`)
- No live handoff logs (stubs only)

## Next Steps — Phase 2 (Activation)

Phase 2 is triggered when **all** of the following are true:

1. B2 domain managers are named for **≥4 of 8 SOB** domains
2. B3 squads accept **first handoff** (≥1 JTBD with proof path)
3. Sunday uplink runs **one full 12WY cycle** end-to-end

When those gates are met, the Phase 2 work begins:

1. **Junction creation** — establish `20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_*/ceos_desktop/` Spock/Areas counterpart; replace this folder's `area_junction_placeholder.md` with a junction symlink per ADR-INFRA-002.
2. **First apps home** — pick the highest-cadence B3 (Cyborg/KangDynasty for IT, daily cadence) and create `apps/it-cyborg/` as the first build-bearing home.
3. **Handoff activation** — promote `handoffs/Beth_Alignment_Log.md` and `handoffs/Morty_Global_Queue.md` from stubs to live logs; run one dry-run for each.
4. **Sunday uplink v0.1** — define the weekly template, post the first check-in, time-box the format.

Phase 3 (Graduation) is then triggered when the B1/B2/B3 triad operates rhythmically for one full quarter. See `_doctrine/SUMMERS_VERSE_MANIFEST.md` § "1-Year Vision" for the full graduation gates.

## Pointer

- Full B1 direction: `_doctrine/SUMMERS_VERSE_MANIFEST.md`
- Project rules: `CLAUDE.md`
- Boundary note (Spock/Areas): `area_junction_placeholder.md`
- Global doctrine: `ASpace_OS_V2/CLAUDE.md` and `~/.claude/CLAUDE.md`
