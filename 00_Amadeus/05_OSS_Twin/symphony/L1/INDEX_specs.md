---
source: Shadow_Life_OS / symphony-L1 / Lane_A
date: 2026-06-07
type: index
layer: L1_Life_OS
lane: A_specs
status: ACTIVE
domain: A0_Sovereign / L1_Life_OS / Twin_Runtime
tags: [#ShadowLifeOS #LaneA #Specs #Twin #L1]
---

# Lane A — Specs Twin Index

> **Lane A (Spec Layer)** : 1-2 jours · twins runtime des specs canon `20_Life_OS/`
> Le canon reste **source de vérité** ; les twins sont des **vues runtime** consommables par Symphony/Agents.

---

## 🛡️ A1 — Gatekeepers (2)

| Twin | Source canon | Role | Status | Version |
|---|---|---|---|---|
| [[A1_Beth_Spec.twin]] | `20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md` | Conscience stratégique / Filesystem Guardian / **Veto power (5 états)** | **ACTIVE** | 1.1 (2026-06-15) |
| [[A1_Morty_Spec.twin]] | `20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md` | Executor A0-aligned / Context Pack router | **ACTIVE** | 1.1 (2026-06-15) |

## 🚀 A2 — Ships (6)

| Twin | Source canon | Framework | A2 name (canon) | Status | Version |
|---|---|---|---|---|---|
| [[A2_Orville_Spec.twin]] | `20_Life_OS/21_Ikigai_Orville/A2_Orville_Spec.md` | Ikigai (Pilars × Horizons × Kardashev) | **USS Orville itself** | ACTIVE | 1.1 (2026-06-15) |
| [[A2_Discovery_Spec.twin]] | `20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md` | Life Wheel (8 LD × ZORA observation) | **ZORA** | ACTIVE | 1.1 (2026-06-15) |
| [[A2_Curie_SNW_Spec.twin]] | `20_Life_OS/23_12WY_SNW/A2_Curie_SNW_Spec.md` | 12-Week Year (5 étapes Pike→Ortegas) | **Curie** | ACTIVE | 1.1 (2026-06-15) |
| [[A2_Computer_Enterprise_Spec.twin]] | `20_Life_OS/24_PARA_Enterprise/A2_Computer_Enterprise_Spec.md` | PARA (Projects/Areas/Resources/Archives) | **LCARS Computer** | ACTIVE | 1.1 (2026-06-15) |
| [[A2_HoloDeck_Cerritos_Spec.twin]] | `20_Life_OS/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md` | GTD (5 étapes Mariner→Freeman) | **Holo Deck** | ACTIVE | 1.1 (2026-06-15) |
| [[A2_HoloJaneway_Protostar_Spec.twin]] | `20_Life_OS/26_DEAL_Protostar/A2_HoloJaneway_Protostar_Spec.md` | DEAL (4 étapes Dal→Gwyn) | **Holo Janeway** (with space) | ACTIVE | 1.1 (2026-06-15) |

## 🛠️ A3 — Crews (par ship)

| Ship | Path canon | Crew count | Status |
|---|---|---|---|
| Orville | `21_Ikigai_Orville/01_Pillars_Identity/` + `02_Horizons_Time/` | 4 Pillars + 5 Horizons = 9 | À twin-er |
| Discovery | `22_Wheel_Discovery/LD0[1-8]_*/` | 8 LDs | À twin-er |
| SNW | `23_12WY_SNW/0[1-5]_*/` | 5 (Pike, Una, M'Benga, Chapel, Ortegas) | À twin-er |
| Enterprise | `24_PARA_Enterprise/01_Projects_Picard/` + `02_Areas_Spock/` + `03_Resources_Geordi/` + `04_Archives_Data/` | 4 (Picard, Spock, Geordi, Data) | À twin-er |
| Cerritos | `25_GTD_Cerritos/0[1-5]_*/` | 5 (Mariner, Boimler, Rutherford, Tendi, Freeman) | À twin-er |
| Protostar | `26_DEAL_Protostar/0[1-4]_*/` | 4 (Dal, Rok-Tahk, Zero, Gwyn) | À twin-er |

**Total A3 à twin-er** : 35 fichiers. Phase 2.

---

## 🔗 Symbiose canon ↔ twin

```
20_Life_OS/<ship>/<X>_Spec.md   ──►   OSS_Twin/symphony/L1/lane_A_specs/<X>_Spec.twin.md
        SOURCE                                 VUE RUNTIME
   (source de vérité)                  (frontmatter `twin_of` pointe)
```

Règle : **jamais modifier le canon depuis le twin**. Le canon évolue, le twin suit.

---

## 📊 État Lane A

- **2026-06-07** : Scaffold créé. 2 A1 + 6 A2 twins squelettes peuplés. A3 à twin-er en phase 2.
- **2026-06-15** : Re-twin v1.1 — 2 A1 (Beth/Morty) + 6 A2 (Orville/ZORA/Curie/Computer/Holo Deck/Holo Janeway) corrigés. Anti-patterns résolus : (a) "Ship Captain" role label → A2 ship intelligence names, (b) Picard ≠ A2 (Computer), (c) Freeman ≠ A2 (Holo Deck), (d) ZORA = Discovery A2, (e) HoloJaneway hyphen → Holo Janeway space, (f) bridge refs `symphony_plane` → `symphony-plane`. 8/8 fichiers ACTIVE. A1 `supervised_by: A0_Amadeus` + `oversees:` list 6 A2 ajoutée.

*Index régénéré manuellement (2026-06-07) — voir Lane A workflow dans `hand_offs/`.*
