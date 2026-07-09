---
name: affine-kanban-gtd
version: 1.0
created: 2026-06-07
phase: EXECUTE
tracker: Affine
actor: Cerritos (GTD) + Protostar (DEAL) crews
---

# 08 — Affine Kanban (GTD + DEAL)

> **Affine** est la source de vérité **opérationnelle** de Life OS. Il porte
> le kanban GTD (5 étapes) + le track DEAL (Liberation 4hWW).

## Colonnes GTD canon (5)

```
[Inbox] ──> [Clarify] ──> [Organize] ──> [Reflect] ──> [Engage]
   │            │             │             │             │
   ▼            ▼             ▼             ▼             ▼
 capture      2-min rule    contexte      weekly        action
                             + priorité    review        immédiate
```

| Colonne | Crew A3 owner | WIP limit |
|---|---|---|
| Inbox | Boimler (capture) | ∞ (vide rapide) |
| Clarify | Boimler (2-min rule) | 5 max |
| Organize | **Rutherford** (⚠️ canon 2026-05-20) | 5 max |
| Reflect | Tendi + Tilly (LD04) | 3 max |
| Engage | Freeman + Asha (SNW) | 3 max |

## DEAL 4hWW (canon Protostar)

| Action | Sens | Crew A3 |
|---|---|---|
| **Drop** | Arrêter de faire | Gwyn |
| **Automate** | Transformer en système | Dal |
| **Delegate** | Transférer à un autre | Janeway (captain) |
| **Concentrate** | Bloquer du temps dédié | Freeman (SNW) |

**Cible** : atteindre 4h de "vraie valeur" / semaine par domain Life Wheel.

## Affine schema (cards)

```
[ID] [Title] [Description] [Column] [WIP-Flag] [VesselID] [CrewID]
[2min?] [Context] [Priority] [DueDate] [EvidenceURL] [PulseTickID]
```

- **Column** : enum(Inbox, Clarify, Organize, Reflect, Engage)
- **2min?** : bool (si true et Clarify exécuté → Done direct, bypass Organize)
- **Context** : tag (calls / computer / home / errand / ...)

## Règle de mouvement

| Depuis | Vers | Trigger |
|---|---|---|
| Inbox | Clarify | Card créée (Boimler capture) |
| Clarify | Organize | 2-min rule épuisée |
| Clarify | Done | 2-min rule succès |
| Organize | Reflect | Context + priorité assignés |
| Reflect | Engage | Weekly review a trié |
| Engage | Done | Action exécutée + evidence_url loggé |
| * | Inbox | Re-capture si contexte perdu |

## 2-min rule (Boimler)

> *"Si ça prend moins de 2 minutes, fais-le maintenant."*
> — David Allen, GTD

Si une card Clarify est résolvable en < 2min :
1. **Exécuter** immédiatement
2. **Logger** `result.status = "2min_success"` dans `outbox/l1/...`
3. **Bypass** Organize et Reflect → Done direct
4. **Pulsar** la phase EXECUTE avec `decision: "2min_rule"`

**Anti-pattern** : 2-min rule détournée en "je fais tout immediate" → burn.

## Anti-patterns

- ❌ Card sans `Context` (rend Reflect aveugle)
- ❌ WIP limit dépassé (Rutherford captain doit le flagger → escalade Beth)
- ❌ Card Engage sans `DueDate` (viole GTD)
- ❌ Crew qui déplace une card sans `PulseTickID` (rend OBSERVE impossible)
- ❌ Hard-delete d'une card (utiliser `Column = "Archive"`)

## Source canonique

- `20_Life_OS/` Cerritos (GTD canon, David Allen) + Protostar (DEAL 4hWW, Fortin)
- Canon lock 2026-05-20 : `Rutherford=Organize` (Tendi=Review, non l'inverse)
- Twin runtime : `L1/lane_C_capsules/03_A3_crews/cerritos/`
