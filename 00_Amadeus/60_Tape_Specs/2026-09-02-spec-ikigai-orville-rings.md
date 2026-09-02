---
titre: Spec Ikigai Orville - initialiser les 9 rings A3 fonctionnels + packet Orville
spec: amy_spec_l1
date: 2026-09-02
work: L1
parent_a2: A2_Orville_Ikigai
---

# Ruban - Ikigai Orville : initialiser les 9 rings A3 fonctionnels

## Verifie reellement (etat du repo au 2026-09-02)

Mesure directe de `C:/Users/amado/ASpace_OS_V3/20_Life_OS/21_Ikigai_Orville/` :
`01_Pillars_Identity/` et `02_Horizons_Time/` contiennent chacun **uniquement
`README.md`**. Or leurs README référencent chacun des sous-dossiers A3 attendus :

- `01_Pillars_Identity/README.md` (crew table) : `01_Profession_Mercer`,
  `02_Mission_Grayson`, `03_Passion_Malloy`, `04_Vocation_Finn`.
- `02_Horizons_Time/README.md` (crew table) : `01_H1_Isaac`, `02_H3_Lamarr`,
  `03_H10_Bortus`, `04_H30_Alara`, `05_H90_Klyden`.

Aucun de ces 9 dossiers n'existe : les rings A3 Ikigai sont des pointeurs
morts. Le contenu canon existe déjà en source unique :
`21_Ikigai_Orville/Ikigai_Pillars_Horizons_Kardashev.md` (tables H1-H90 par
pillar) et `A2_Orville_Spec.md` (outputs `meaning_alignment`,
`beth_recommendation`, `morty_route`, `evidence_paths`). Le ruban n'est pas
redondant : il matérialise l'arborescence déclarée.

## Objectif

1. Créer les 9 sous-dossiers A3 ci-dessus, chacun avec :
   - `README.md` : frontmatter minimal (`id`, `layer: L1_Life_OS`,
     `parent_a2: ORVILLE`, `role: A3_<PILLAR|HORIZON>`, `question` canon
     reprise verbatim du README parent, `status: SHADOW_ACTIVE`), section
     Mission 2-3 lignes, section Handoff Rule ("narrow finding only;
     Orville compile"), section Evidence pointant vers
     `../../Ikigai_Pillars_Horizons_Kardashev.md` (ancre de la ligne du
     pillar/horizon correspondant).
2. Créer `21_Ikigai_Orville/00_Orville_Packet/` avec `packet.template.md` :
   gabarit de compilation Orville conforme aux outputs de
   `A2_Orville_Spec.md` (`meaning_alignment: GREEN|YELLOW|RED`,
   `beth_recommendation`, `morty_route`, `evidence_paths`,
   `pillar_horizon_packet`) — gabarit seulement, aucune décision remplie.

## Interdits

- Ne pas modifier `Ikigai_Pillars_Horizons_Kardashev.md`, `A2_Orville_Spec.md`,
  ni les README parents.
- Aucune décision Ikigai remplie (Orville seul compile ; aucune entrée
  Beth_Alignment_Log n'existe encore → pas de veto à contourner).
- Pas de secret dans les fichiers.

## Criteres d'acceptation (verifiables par commande)

- N1 : les 9 dossiers existent et chacun contient `README.md` (>300 octets).
- N2 : les 4 dossiers Pillar portent les questions canon verbatim
  ("Does this strengthen the craft and economic role?", "Does this serve a
  real need beyond ego?", "Does this preserve energy, curiosity, and joy?",
  "Does this honor gifts, limits, and non-negotiables?") dans leurs README.
- N3 : les 5 dossiers Horizon portent H1/H3/H10/H30/H90 avec les noms
  Isaac/Lamarr/Bortus/Alara/Klyden dans leurs README.
- N4 : chaque README A3 contient au moins une reference relative vers
  `Ikigai_Pillars_Horizons_Kardashev.md`.
- N5 : `00_Orville_Packet/packet.template.md` contient les 5 champs output
  de `A2_Orville_Spec.md` (meaning_alignment, beth_recommendation,
  morty_route, evidence_paths, pillar_horizon_packet).
- N6 : checksums des fichiers canon inchangés (Kardashev, A2 spec, 2 README
  parents) avant/après.
