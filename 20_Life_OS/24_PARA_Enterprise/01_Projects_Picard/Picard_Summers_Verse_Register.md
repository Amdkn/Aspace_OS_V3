---
id: PICARD_SUMMERS_VERSE_REGISTER
layer: L2_Business_Pulse
owner: A3_Picard_Projects
status: SHADOW_ACTIVE
created: 2026-05-21
---

# Picard Register - Summer's Verse Projects

Picard supervises the numbered project folders as Summer's Verse candidates. Each numbered project must contain the B1/B2/B3 skeleton before it can be considered structurally ready.

## Register

| Project folder | Summer status | Interface prototype location |
|---|---|---|
| `00_Summers_Verse` | TEMPLATE_CANON | template surface, not a business project |
| `00 Agency as a Service` | STRUCTURED | `B2_Business_Domains/03_Product_Flash_Avengers/00_Interface_Prototypes/` |
| `01 OMK Business OS` | STRUCTURED | `B2_Business_Domains/03_Product_Flash_Avengers/00_Interface_Prototypes/` |
| `01-omk-business-os` | STRUCTURED_MIRROR | `B2_Business_Domains/03_Product_Flash_Avengers/00_Interface_Prototypes/` |
| `02 ABC OS & Child Care BOS` | STRUCTURED_EMPTY | no interface prototype found in root |
| `03_RILCOT_Members_Space_OS` | STRUCTURED | `B2_Business_Domains/03_Product_Flash_Avengers/00_Interface_Prototypes/` |
| `04 Alikaly Bana Holding to LLC` | GRADUATED | `B2_Business_Domains/03_Product_Flash_Avengers/00_Interface_Prototypes/Kalybana Holding/` |
| `05 marina Cleaning BOS & SOP` | GRADUATED | `B2_Business_Domains/03_Product_Flash_Avengers/00_Interface_Prototypes/` |

## Graduation Tracker

All current Summer surfaces now hold full B1/B2/B3 structure. Graduation requires A0 to validate B1 visions in each project before marking GRADUATED. `00_Summers_Verse` is the template and does not graduate.

| Project | B1 Vision | Status |
|---------|-----------|--------|
| `00 Agency as a Service` | Validated | GRADUATED |
| `01 OMK Business OS` | Filled 2026-05-21 | GRADUATED |
| `01-omk-business-os` | Structured mirror | STRUCTURED_MIRROR |
| `02 ABC OS & Child Care BOS` | Filled 2026-05-21 | GRADUATED |
| `03_RILCOT_Members_Space_OS` | Filled 2026-05-21 | GRADUATED |
| `04 Alikaly Bana Holding to LLC` | Filled 2026-05-21 | GRADUATED |
| `05 marina Cleaning BOS & SOP` | Filled 2026-05-21 | GRADUATED |

## Picard Rule

Every new numbered project must be created from `00_Summers_Verse` or checked against `business-pulse-summers-verse-template`.

See `JERRY_SUMMER_FRACTAL_ALIGNMENT.md` for the explicit Jerry Area -> Summer Project mapping.

## Product Isolation Rule

Picard must not mark a project as operational just because Product has a working prototype or a clean build.

Each project must maintain:

- `B2_Business_Domains/B2_DOMAIN_GATE_MATRIX.md`
- one `README.md` in each of the 8 B2 domain folders

Until Ops, IT, Finance, Legal, Sales, Growth, and People have explicit gate status, the project status is `PRODUCT_ONLY_PROTOTYPE`.

## Graduation Rule

A Summer's Verse graduates only when:

1. B1 has 1-year, 3-year, and 10-year vision fields.
2. Four 12WY cycles have named Summer responsibility.
3. B2 domains own Rocks and tactic specifications.
4. B3 produces Lead/Lag execution logs.
5. Data receives archive-ready evidence after the cycle.
6. B2 gate matrix is filled with PASS, CONDITIONAL, or BLOCKED for all 8 domains.

---

## Macro doctrine to reference (DRY) — now complete (2026-06-02)

Every Summer project references the Jerry Area macro doctrine; it never re-derives it. The 8 domain
doctrines AND the 8 canonical JTBD-001 packets are now COMPLETE in the Area (paths in Unix style):

- **B2 doctrines** : `../02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/<NN>/03_<HERO>_<DOMAIN>_PRINCIPLES.md`
  (Growth 18 · Sales 14 · Product 18 · Ops 22 · IT 18 · Finance 12+6 Empire · People 12+6 Harness · Legal 12+6 Abundance)
- **B3 packets** : `../02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/<NN>/JTBD-<DOMAIN>-001_*.md` (8/8)
- **Macro skeleton** : `../02_Areas_Spock/J01_Jerry_Prime_LD01_Business/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md`
- **B1 charter** : `AREA_STANDARD.md` + `B1_Area_Direction/03_DECISION_CHARTER.md`
- **Bridge** : `JERRY_SUMMER_FRACTAL_ALIGNMENT.md` (this folder) — the explicit macro<->micro mapping.

When a project instantiates a domain, drop a one-line `03_<DOMAIN>_PRINCIPLES_REF.md` pointing to the
macro doctrine above (a pointer, not a copy — ADR-MESH-L2-001). The `picard-growth-jtbd-launch` skill
does this for Growth, mode-calibrated.
