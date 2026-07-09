---
name: baserow-lifedb-schema
version: 1.0
created: 2026-06-07
phase: PROBE + WRITE-BACK
tracker: Baserow
actor: Discovery (LD01-LD08) + Orville (Pilars Ikigai)
---

# 05 — Baserow LifeDB Schema (8 LD + Ikigai Pillars)

> **Baserow** est la source de vérité **structurée** de Life OS.
> 9 tables canon : 8 Life Domains (LD01-LD08) + 1 Pilars Ikigai.

## Tables canon (9)

| Table | Life Domain | Captain | Granularité |
|---|---|---|---|
| `LD01_Business` | Carrière / Business | Burnham | 1 row / project actif |
| `LD02_Finances` | Argent / Investissement | Burnham | 1 row / asset ou flux |
| `LD03_Sante` | Santé / Corps | **Culber** (STOP authority) | 1 row / indicateur santé |
| `LD04_Cognition` | Mental / Apprentissage | **Tilly** (STOP authority) | 1 row / sujet d'apprentissage |
| `LD05_Famille` | Famille / Origine | Burnham | 1 row / membre |
| `LD06_Relations` | Amis / Communauté | Burnham | 1 row / relation |
| `LD07_Loisirs` | Loisirs / Créativité | Burnham | 1 row / activité |
| `LD08_Environnement` | Lieu / Cadre de vie | Burnham | 1 row / lieu |
| `PILLARS_Ikigai` | 5 piliers (cross-cutting) | Mercer | 1 row / pilier |

## Schéma commun (toutes les 9 tables)

```
[ID] [Name] [Status] [Tier] [LastTouch] [Notes] [EvidenceURL] [PulseTickID]
```

- **ID** : PK auto-incrément Baserow
- **Name** : text (nom canon du domaine/domaine)
- **Status** : single_select (GREEN/ORANGE/RED/HALT_LD03/HALT_LD04 — miroir Beth)
- **Tier** : single_select (P1/P2/P3 — priorité de routage)
- **LastTouch** : date (dernière fois qu'un crew A3 a touché)
- **Notes** : long_text (log narratif)
- **EvidenceURL** : url (lien Obsidian/Plane/Affine/etc.)
- **PulseTickID** : text (lien vers `agent-os/pulse.log` pour audit)

## Statuts (mapping Beth)

| Statut Baserow | Sens Beth 5-state | Effet routage |
|---|---|---|
| GREEN | OK | A3 crew engageable |
| ORANGE | Vigilance | A3 crew engageable mais report toutes les 4 phases |
| RED | Alerte | A3 crew réduit scope, A2 captain escalate A1 |
| HALT_LD03 | Stop santé | Aucun A3 crew LD03-touchable |
| HALT_LD04 | Stop cognition | Aucun A3 crew LD04-touchable |

## Écriture (rule of write)

Tout crew A3 qui **modifie** une row Baserow DOIT :
1. **Lock** la row via `LastTouch = now()` + `PulseTickID = <tick>`
2. **Écrire** le `result` dans `outbox/l1/YYYY-MM-DD/<mission_id>.json`
3. **Logger** la diff dans `pulse.log` (phase EXECUTE, `decision: "baserow_update"`)

## Anti-patterns

- ❌ Crew A3 qui crée une nouvelle table sans passer par Discovery captain (drift schema)
- ❌ Row sans `EvidenceURL` (rend OBSERVE/LEARN aveugle)
- ❌ Statut mismatch entre Baserow et `pulse.log` (rend l'observabilité fausse)
- ❌ Hard-delete d'une row (utiliser `Status = "archived"` à la place)

## Source canonique

- SDD-007 (Symphony orchestrator — partiellement couvert)
- `20_Life_OS/` Discovery (Life Wheel canon)
- Canon Baserow 2026-05-17 : `Shadow_L1/04_life-os-baserow-12wy-architecture-analysis-20260517.md`
