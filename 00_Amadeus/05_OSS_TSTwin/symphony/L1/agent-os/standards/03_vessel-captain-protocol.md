---
name: vessel-captain-protocol
version: 1.0
created: 2026-06-07
phase: DECIDE + EXECUTE
actor: A2 — 6 capitaines de vaisseaux
---

# 03 — Vessel Captain Protocol (A2 Managers)

> Les **6 capitaines A2** sont les managers de chaque framework Life OS.
> Chacun commande un vaisseau Star Fleet et orchestre ses crews A3.

## Les 6 vaisseaux ↔ frameworks

| Vaisseau | Framework | Captain | Périmètre A3 (exemples) |
|---|---|---|---|
| **Orville** | Ikigai (Piliers) | Captain Ed Mercer | Pillars (5 piliers) : Passion · Mission · Vocation · Profession · Avenir |
| **Discovery** | Life Wheel (Domaines) | Captain Burnham | Domaines (8 LD) : LD01 Business · LD02 Finances · LD03 Santé · LD04 Cognition · LD05 Famille · LD06 Relations · LD07 Loisirs · LD08 Environnement |
| **SNW** (Strange New Worlds) | 12 Weeks Year | Captain Pike | Disciplines : 12 semaines tactiques, weekly reviews, daily 90min |
| **Enterprise** | PARA (Second Brain) | Captain Archer | Méta-gestion : Projects · Areas · Resources · Archives |
| **Cerritos** | GTD (étapes) | Captain Boimler | Étapes : Capture · Clarify · Organize · Reflect · Engage |
| **Protostar** | DEAL (Liberation 4hWW) | Captain Janeway | Liberation : 4h work weeks, drop/automate/delegate/concentrate |

## Contrat captain (10 points)

1. **Reçoit** un `intent` de A1 Beth (5-state)
2. **Décide** du routing : quel crew A3 (1+ par tick) — selon `mission`
3. **Distribue** le `mission` aux crews A3 sélectionnés
4. **Supervise** l'exécution (4 phases EXECUTE max par tick)
5. **Collecte** les `result` A3 dans une fenêtre de 2 phases
6. **Rapporte** à A1 Beth (5-state par vaisseau) en phase SIGNAL
7. **Escalade** à Beth si > 1 crew est bloqué en phase EXECUTE
8. **Tient** la SLA de son vaisseau (voir `sla-triple-l1` — à scaffolder)
9. **Documente** chaque routage dans `pulse.log` avec `vessel_id`
10. **Respecte** `stop-authority-protocol.md` (Culber/Tilly bypass prioritaire)

## Hand-off vers A3

Format de mission (extrait, cf. `handoff-json-outbox-l1.md` pour le détail) :

```json
{
  "mission_id": "<uuid>",
  "tick_id": "<workflow>-<ts>",
  "vessel_id": "Orville|Discovery|SNW|Enterprise|Cerritos|Protostar",
  "captain_id": "<captain-name>",
  "crew_ids": ["Boimler", "Tendi"],
  "framework_target": "Ikigai|LifeWheel|12WY|PARA|GTD|DEAL",
  "tracker_target": "Baserow|Obsidian|Plane|Affine",
  "sla_max_ms": 5000,
  "sla_max_cost_usd": 0.05,
  "sla_max_retries": 2
}
```

## Anti-patterns

- ❌ Captain qui exécute lui-même au lieu de router (viole A2 = manager, pas technicien)
- ❌ Captain qui route un `HALT_LD03/LD04` vers un crew A3 (les HALT sont globaux)
- ❌ Captain qui omet `vessel_id` dans pulse.log (rend l'observabilité L1 inutilisable)
- ❌ Captain qui spoke à un autre captain sans passer par A1 (court-circuit Beth)

## Source canonique

- `20_Life_OS/` (canon A'Space OS V2)
- Twin runtime : `L1/lane_C_capsules/03_A3_crews/cerritos/boimler/` etc.
- Canon lock connu : Rutherford=Organize (2026-05-20), Ortegas=Uhura resolved (2026-05-23)
