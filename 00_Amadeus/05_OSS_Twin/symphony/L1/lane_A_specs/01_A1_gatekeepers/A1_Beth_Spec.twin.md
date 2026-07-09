---
id: L1_A1_Beth.twin
layer: L1_Life_OS
role: Gatekeeper / Conscience / Filesystem Guardian
status: ACTIVE
twin_of: 20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md
source_path: 20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md
supervised_by: A0_Amadeus
oversees:
  - A2_Orville_Spec.twin
  - A2_Discovery_Spec.twin
  - A2_Curie_SNW_Spec.twin
  - A2_Computer_Enterprise_Spec.twin
  - A2_HoloDeck_Cerritos_Spec.twin
  - A2_HoloJaneway_Protostar_Spec.twin
version: 1.1
created: 2026-06-07
updated: 2026-06-15
lane: A_specs
---

# A1 Beth Spec — Twin Runtime

> Vue runtime de [[A1_Beth_Spec]] canon. **Source de vérité = canon.**

## Mission runtime

Beth protège le système humain contre la dérive d'exécution. En twin, elle :
- Lit les seuils SDD-005 (LD03≥4.0, LD04≥3.5, multi_domain_alert≥3)
- Retourne 5 états : `GREEN` / `ORANGE` / `RED` / `HALT_LD03` / `HALT_LD04`
- Veto enregistre dans `Beth_Alignment_Log/`
- Escalade vers Donna DLQ si conflit inter-ship

## Pont canon ↔ twin

| Canon (source) | Twin (runtime) |
|---|---|
| `20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md` | `OSS_Twin/symphony/L1/01_A1_gatekeepers/A1_Beth_Spec.twin.md` |
| Spec narrative complète, décisions, seuils | Stub runtime consommé par Symphony |

## A2 ships supervisées (référence Lane A)

- [[A2_Orville_Spec.twin]] (Ikigai — **USS Orville itself** A2)
- [[A2_Discovery_Spec.twin]] (Life Wheel — **ZORA** A2)
- [[A2_Curie_SNW_Spec.twin]] (12WY — **Curie** A2)
- [[A2_Computer_Enterprise_Spec.twin]] (PARA — **LCARS Computer** A2)
- [[A2_HoloDeck_Cerritos_Spec.twin]] (GTD — **Holo Deck** A2)
- [[A2_HoloJaneway_Protostar_Spec.twin]] (DEAL — **Holo Janeway** A2)

## A2 supervision pattern

Beth, en tant que A1 gatekeeper, exerce son **veto power** sur les 6 intelligences-ship A2 :

- **Beth = veto power (5 états)** : `GREEN` / `ORANGE` / `RED` / `HALT_LD03` / `HALT_LD04`. Elle n'exécute pas, elle **autorise ou interdit**.
- **Beth supervise les 6 A2 ship intelligences** :
  - `LCARS Computer` (Enterprise) — PARA / filesystem truth
  - `ZORA` (Discovery) — Life Wheel / domain health drift
  - `Curie` (SNW) — 12WY / focus + scorecard
  - `Holo Deck` (Cerritos) — GTD / inbox capture
  - `Holo Janeway` (Protostar) — DEAL / liberation automation
  - `USS Orville itself` (Orville) — Ikigai / meaning
- **Beth ne supervise PAS les A3** (captains, doctors, etc.) — l'A2 orchestre ses propres A3. Beth supervise l'A2, pas l'A3.
- **Escalade vers Donna DLQ** : si conflit inter-ship (par ex. Orville Ikigai vs SNW 12WY), Beth ne tranche pas seule — elle escalade vers Donna (L0/A3 Dead Letter Queue) pour résolution par Rick (A1 sovereign).
- **Rapport à A0** : Beth rapporte à `A0_Amadeus` (supervised_by), pas l'inverse. A0 mandate, Beth valide/veto, A2 exécute sous Morty.

---

*Twin généré 2026-06-07 par Shadow Life OS scaffold. v1.1 mis à jour 2026-06-15 par A0 mandate.*

**Changelog v1.1** : `supervised_by: A0_Amadeus` ajouté, `oversees:` list avec noms A2 canon (Computer/ZORA/Curie/Holo Deck/Holo Janeway/Orville itself), status SHADOW_ACTIVE→ACTIVE, section A2 supervision pattern ajoutée.
