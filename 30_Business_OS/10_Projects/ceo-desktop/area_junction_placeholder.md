---
id: AREA_JUNCTION_PLACEHOLDER
project: ceo-desktop
status: PHASE_1_DEFERRED
created: 2026-06-07
target_phase: PHASE_2
target_path: 20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_*/ceos_desktop/
parent_jerry: J01_Jerry_Prime_LD01_Business
adr_anchors:
  - ADR-INFRA-002
  - ADR-INFRA-003
---

# Area Junction Placeholder — Spock/Areas Counterpart

> **This project is currently Picard/Projects.**
> The Spock/Areas counterpart will be created in `20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/` during **Phase 2**, after the Spock/Areas junction is established per ADR-INFRA-002 (Repo-Home Junction Law).

---

## Why This File Exists

A'Space OS V2 doctrine (ADR-INFRA-002) requires that every Picard/Project have a **Spock/Areas counterpart** — the doctrinal "what" lives in Projects (Picard), the operational "where it drifts" lives in Areas (Spock). The junction symlink connects them.

For CEO's Desktop, this junction is **intentionally deferred to Phase 2**. Phase 1 is doctrine-only (skeleton); the operational Areas counterpart is only meaningful once B2 domain managers are named and B3 squads start producing observable drift signals.

## Phase 1 Holding Pattern

For Phase 1, the **Jerry/Area responsibility** for this project is held by **Jerry J01 Prime (parent_jerry=J01_Jerry_Prime_LD01_Business)**. There is no per-project Jerry/Area folder yet; the parent Jerry J01 is the locus.

This means:
- All A0 decisions about CEO's Desktop route through Jerry J01 Prime.
- B2 domain drift, when it emerges, is observed in `_doctrine/B2_Business_Domains/0X_*/` and surfaced in the project manifest.
- No junction symlink is created yet. This file IS the placeholder for that future junction.

## Phase 2 Junction Spec

When Phase 2 activates, the Spock/Areas counterpart will be created at:

```
20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_*/ceos_desktop/
```

The `J01_*` prefix is the parent Jerry's area folder. The `ceos_desktop/` subfolder holds the operational evidence (drift logs, wheel balance scores, lead/lag indicators per the 8 SOB).

A junction symlink will then be created from this file's location to that folder, per ADR-INFRA-002 § "Repo-Home Junction Law". At that point, this `area_junction_placeholder.md` file is replaced by the symlink.

## Trigger Conditions for Phase 2 Junction

Move to Phase 2 (and create the Spock/Areas counterpart) when **all** of:

1. B2 domain managers are named for **≥4 of 8 SOB** domains.
2. B3 squads accept **first handoff** (≥1 JTBD with proof path).
3. Sunday uplink runs **one full 12WY cycle** end-to-end.

These are the same gates as the project-wide Phase 2 transition (see `README.md` § "Next Steps — Phase 2"). The junction is part of that transition, not a separate one.

## Pointer

- Doctrine: `_doctrine/SUMMERS_VERSE_MANIFEST.md`
- Project rules: `CLAUDE.md`
- A0 routeur: `README.md`
- ADR-INFRA-002: Repo-Home Junction Law
- ADR-INFRA-003: CEO Dashboard Matryoshka
- Parent Jerry: J01_Jerry_Prime_LD01_Business
