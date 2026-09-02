---
id: ORVILLE_PACKET_TEMPLATE
layer: L1_Life_OS
parent_a2: ORVILLE
role: A2_compilation_gabarit
status: SHADOW_ACTIVE
---

# Orville Packet - gabarit de compilation Ikigai

> Gabarit seul. Aucune decision remplie : Orville seul compile les 9 findings
> A3 (4 Pillars + 5 Horizons). Champs conformes aux Outputs de
> `A2_Orville_Spec.md`.

```yaml
ship: ORVILLE
framework: Ikigai
meaning_alignment: GREEN|YELLOW|RED          # Output 1 (A2_Orville_Spec.md)
beth_recommendation: approve|hold|veto|needs_evidence   # Output 2
morty_route: DISCOVERY_ZORA|SNW_12WY|ENTERPRISE_PARA|CERRITOS_GTD|PROTOSTAR_DEAL  # Output 3
evidence_paths:                              # Output 4 - exact files checked
  - C:\...
pillar_horizon_packet:                       # Output 5 - one pillar x one horizon signal
  horizon: H1|H3|H10|H30|H90
  pillar: Profession|Passion|Mission|Vocation
  alignment_signal: GREEN|YELLOW|RED
  kardashev_ref: Ikigai_Pillars_Horizons_Kardashev.md
```

## Findings recus (9 A3)

| Ring | A3 | Finding |
|---|---|---|
| Profession | Ed Mercer | A REMPLIR PAR ORVILLE |
| Mission | Kelly Grayson | A REMPLIR PAR ORVILLE |
| Passion | Gordon Malloy | A REMPLIR PAR ORVILLE |
| Vocation | Claire Finn | A REMPLIR PAR ORVILLE |
| H1 | Isaac | A REMPLIR PAR ORVILLE |
| H3 | John Lamarr | A REMPLIR PAR ORVILLE |
| H10 | Bortus | A REMPLIR PAR ORVILLE |
| H30 | Alara Kitan | A REMPLIR PAR ORVILLE |
| H90 | Klyden | A REMPLIR PAR ORVILLE |

## Boundaries

- Orville compile ; les A3 n'ecrivent qu'un finding narrow.
- Un `meaning_alignment: RED` declenche le veto Beth (A1) avant tout routage Morty.
- Ce gabarit ne contient aucune decision Ikigai remplie.
